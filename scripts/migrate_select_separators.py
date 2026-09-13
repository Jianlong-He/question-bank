#!/usr/bin/env python3
"""
Rewrite every `~~…~~` option block to use the bar as its only separator.

Before this change the app split a Select row's options by trying three
separators in order — a bar, then a comma followed by a space, then whitespace
— and keeping the first that produced more than one piece. Which rule won
depended on what the option text happened to contain, so a scenario sentence
written inside the markers became one button per word, `Linear, Nonlinear |
None` quietly meant something different from `Linear, Nonlinear`, and any
multi-word option had to be wrapped in quotes to survive. The parser now splits
on the bar and nothing else; this script converts the bank to match.

It reads each block with the *old* cascade and writes it back bar-separated, so
every row keeps exactly the options it had. Quotes that were only there to
protect spaces are dropped; an option holding a bar of its own is quoted so the
bar stays part of the option. Running it twice is a no-op.

    python3 scripts/migrate_select_separators.py [--root DIR] [--check]

--check reports what would change and writes nothing.
"""
import argparse
import csv
import io
import os
import re
import sys

BOUNDARY = set(" \t\r\n,|")


def protected_spans(text):
    """Every `"…"` and `$…$` run, as [start, end) pairs — mirrors tokens.ts."""
    spans = []
    i = 0
    at = lambda k: k < 0 or k >= len(text) or text[k] in BOUNDARY
    while i < len(text):
        ch = text[i]
        if (ch == '"' or ch == "$") and at(i - 1):
            j = i + 1
            while j < len(text) and not (text[j] == ch and at(j + 1)):
                j += 1
            if j < len(text):
                spans.append((i, j + 1, ch == '"'))
                i = j + 1
                continue
        i += 1
    return spans


def split_outside(text, seps):
    spans = protected_spans(text)
    parts, cur, k, i = [], "", 0, 0
    while i < len(text):
        s = spans[k] if k < len(spans) else None
        if s and s[0] <= i < s[1]:
            if not (s[2] and (i == s[0] or i == s[1] - 1)):
                cur += text[i]
            if i == s[1] - 1:
                k += 1
            i += 1
            continue
        if text[i] in seps:
            parts.append(cur)
            cur = ""
            i += 1
            continue
        cur += text[i]
        i += 1
    parts.append(cur)
    return parts


def read_options_the_old_way(block):
    """The three-separator cascade the parser used before this change."""
    clean = lambda ps: [p.strip() for p in ps if p.strip()]

    by_bar = split_outside(block, {"|"})
    if len(by_bar) > 1:
        return clean(by_bar)

    marked = re.sub(r",\s+", "\x00", block)
    by_comma = split_outside(marked, {"\x00"})
    if len(by_comma) > 1:
        return clean([p.replace("\x00", ", ") for p in by_comma])

    return clean([re.sub(r",+$", "", v) for v in split_outside(block, {" ", "\t"})])


def render_option(option):
    """Bare, unless a bar of its own would be read as a separator."""
    if "|" not in option:
        return option
    if option.startswith("$") and option.endswith("$") and len(option) > 1:
        return option
    return '"%s"' % option


def convert_block(block):
    return " | ".join(render_option(o) for o in read_options_the_old_way(block))


VARIANT = "||"


def split_variants(cell):
    """`||` separates prompts, except inside a `~~` block or a `Choices:` list."""
    m = re.search(r"~~[\s\S]*?~~", cell)
    lo, hi = (m.start(), m.end()) if m else (-1, -1)
    c = cell.lower().find("choices:")
    parts, start, i = [], 0, 0
    while i < len(cell) - 1:
        if cell[i : i + 2] != VARIANT:
            i += 1
            continue
        if lo >= 0 and lo <= i < hi:
            i += 1
            continue
        if c >= 0 and i > c:
            i += 1
            continue
        parts.append(cell[start:i])
        start = i + 2
        i += 2
    if not parts:
        return [cell]
    parts.append(cell[start:])
    return parts


def convert_cell(cell):
    out = []
    for variant in split_variants(cell):
        if re.match(r"^\s*select\b", variant, re.I):
            variant = re.sub(
                r"~~([\s\S]*?)~~", lambda m: "~~" + convert_block(m.group(1)) + "~~", variant
            )
        out.append(variant)
    return VARIANT.join(out)


HEADER_CHOICES = ("Question Choices", "QuestionChoices")


def scan_fields(raw):
    """Every field in `raw` as (row, col, start, end, quoted) over the raw text.

    Editing through offsets rather than re-serialising the file is what keeps a
    diff down to the option blocks: the bank mixes fully quoted files with
    unquoted ones, and rewriting either with a CSV writer would restyle every
    row it did not need to touch.
    """
    fields = []
    row = col = 0
    i = 0
    n = len(raw)
    while i <= n:
        start = i
        quoted = i < n and raw[i] == '"'
        if quoted:
            i += 1
            while i < n:
                if raw[i] == '"':
                    if i + 1 < n and raw[i + 1] == '"':
                        i += 2
                        continue
                    i += 1
                    break
                i += 1
        while i < n and raw[i] not in ',\r\n':
            i += 1
        fields.append((row, col, start, i, quoted))
        if i >= n:
            break
        if raw[i] == ',':
            col += 1
            i += 1
            continue
        if raw[i] == '\r' and i + 1 < n and raw[i + 1] == '\n':
            i += 2
        else:
            i += 1
        row += 1
        col = 0
    return fields


def unescape(raw_field, quoted):
    return raw_field[1:-1].replace('""', '"') if quoted and len(raw_field) >= 2 else raw_field


def escape(value, quoted):
    if quoted or any(c in value for c in ',"\r\n'):
        return '"%s"' % value.replace('"', '""')
    return value


def process(path, check):
    raw = io.open(path, encoding="utf-8", newline="").read()
    if not raw.strip():
        return 0, None
    bom = raw.startswith("﻿")
    body = raw[1:] if bom else raw

    fields = scan_fields(body)
    header = [unescape(body[s:e], q).strip() for (r, c, s, e, q) in fields if r == 0]
    col = next((header.index(n) for n in HEADER_CHOICES if n in header), None)
    if col is None:
        return 0, None

    edits = []
    for (r, c, s, e, q) in fields:
        if r == 0 or c != col:
            continue
        before = unescape(body[s:e], q)
        after = convert_cell(before)
        if after != before:
            edits.append((s, e, escape(after, q)))

    if edits and not check:
        out = body
        for s, e, text in reversed(edits):
            out = out[:s] + text + out[e:]
        io.open(path, "w", encoding="utf-8", newline="").write(("﻿" if bom else "") + out)
    return len(edits), None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=os.path.join(os.path.dirname(__file__), ".."))
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    root = os.path.abspath(args.root)
    total_rows = total_files = 0
    problems = []
    for base, dirs, names in os.walk(root):
        dirs[:] = [d for d in dirs if d != ".git"]
        for name in sorted(names):
            if not name.lower().endswith(".csv"):
                continue
            path = os.path.join(base, name)
            changed, problem = process(path, args.check)
            if problem:
                problems.append(problem)
            if changed:
                total_files += 1
                total_rows += changed
    verb = "would convert" if args.check else "converted"
    print("%s %d option block(s) in %d file(s)" % (verb, total_rows, total_files))
    for p in problems:
        print("  !", p)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
