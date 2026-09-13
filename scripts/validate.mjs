#!/usr/bin/env node
/**
 * Validate the question bank: curriculum.json, the unit-test catalog, and the
 * CSVs they point at. No dependencies — `node scripts/validate.mjs`.
 *
 * Exit code 1 on any error. Warnings (content nothing links to) are printed
 * but do not fail the run, so a worksheet can be added before it is placed.
 *
 * What is checked
 *   curriculum.json
 *     - parses, is a list of the three top-level sections
 *     - every node is exactly one shape: link {title,url}, videos
 *       {title,youtubeIds}, branch {title,submenu}, or placeholder {title}
 *     - no empty submenu/youtubeIds, no unknown keys
 *     - every `?file=…` link names a file that exists in this repo
 *   unit-tests/catalog/catalog.json
 *     - every entry has grade, unit, file; the file exists
 *     - questionCount matches the CSV's question count
 *   every CSV under worksheets/ and unit-tests/
 *     - has the seven-column header the app reads
 *     - every row has a Question ID, a question and an answer
 *     - a `Choices: A) … | B) …` question's answer letter exists, and every
 *       piece of the list opens with its own letter
 *     - a `Select …` question has exactly one `~~…~~` block, holding two or
 *       more bar-separated options, none of them a stray sentence
 *     - no `||` inside an option list, where it would split the prompt instead
 *     - a `Select …` question's answers all appear among its options
 *   warnings
 *     - worksheet CSVs that no curriculum link points at
 *     - unit-test CSVs that the catalog does not list
 */
import { readFileSync, readdirSync, statSync, existsSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join, relative, resolve } from "node:path";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const errors = [];
const warnings = [];
const err = (m) => errors.push(m);
const warn = (m) => warnings.push(m);

// ---------------------------------------------------------------- files
function walk(dir, out = []) {
  if (!existsSync(dir)) return out;
  for (const name of readdirSync(dir)) {
    const p = join(dir, name);
    if (statSync(p).isDirectory()) walk(p, out);
    else out.push(relative(root, p).split("\\").join("/"));
  }
  return out;
}
const worksheetFiles = new Set(walk(join(root, "worksheets")));
const unitTestFiles = new Set(walk(join(root, "unit-tests")));
const allFiles = new Set([...worksheetFiles, ...unitTestFiles]);

// ---------------------------------------------------------------- CSV
function parseCsv(text) {
  const rows = [];
  let row = [], cell = "", q = false;
  for (let i = 0; i < text.length; i++) {
    const c = text[i];
    if (q) {
      if (c === '"') { if (text[i + 1] === '"') { cell += '"'; i++; } else q = false; }
      else cell += c;
    } else if (c === '"') q = true;
    else if (c === ",") { row.push(cell); cell = ""; }
    else if (c === "\n" || c === "\r") { if (c === "\r" && text[i + 1] === "\n") i++; row.push(cell); rows.push(row); row = []; cell = ""; }
    else cell += c;
  }
  if (cell !== "" || row.length) { row.push(cell); rows.push(row); }
  return rows.filter((r) => r.some((x) => x.trim() !== ""));
}
const HEADER = {
  id: ["Question ID", "QuestionID", "Question Number", "QuestionNumber"],
  choices: ["Question Choices", "QuestionChoices"],
  answers: ["Question Answers", "Question Answer", "QuestionAnswers", "QuestionAnswer"],
};

// Mirrors frontend/src/learning: Select options split on whitespace outside
// "…" and $…$ spans; answers split on ';' (if present) else ',' outside spans.
function spans(text) {
  const out = []; const B = /[\s,|]/;
  const at = (i) => i < 0 || i >= text.length || B.test(text[i]);
  for (let i = 0; i < text.length; i++) {
    const ch = text[i];
    if ((ch === '"' || ch === "$") && at(i - 1)) {
      let j = i + 1;
      while (j < text.length && !(text[j] === ch && at(j + 1))) j++;
      if (j < text.length) { out.push([i, j + 1, ch === '"']); i = j; }
    }
  }
  return out;
}
function splitOutside(text, sep) {
  const sp = spans(text); const parts = []; let cur = "", k = 0;
  for (let i = 0; i < text.length; i++) {
    const s = sp[k];
    if (s && i >= s[0] && i < s[1]) { if (!(s[2] && (i === s[0] || i === s[1] - 1))) cur += text[i]; if (i === s[1] - 1) k++; continue; }
    if (sep.test(text[i])) { parts.push(cur); cur = ""; continue; }
    cur += text[i];
  }
  parts.push(cur);
  return parts;
}
function answerSets(raw) {
  return raw.split(/\s*\|\s*/).map((set) => {
    const bySemi = splitOutside(set, /;/);
    const parts = bySemi.length > 1 ? bySemi : splitOutside(set, /,/);
    return parts.map((x) => x.trim()).filter(Boolean);
  }).filter((s) => s.length);
}
// The app's one Select separator (see RULES.md §2): a bar, outside "…" and $…$
// spans. Nothing else divides options, so a comma, a space or a period inside
// an option is just text.
function splitSelectOptions(after) {
  return splitOutside(after, /\|/).map((p) => p.trim()).filter(Boolean);
}

// `||` separates prompts — but not inside a ~~…~~ block or a Choices: list, where
// it is a mis-authored option rather than a second prompt.
function splitVariants(cell) {
  const block = cell.match(/~~[\s\S]*?~~/);
  const lo = block?.index ?? -1;
  const hi = lo >= 0 ? lo + block[0].length : -1;
  const choicesAt = cell.search(/Choices:/i);
  const parts = [];
  let from = 0;
  for (let i = 0; i < cell.length - 1; i++) {
    if (cell[i] !== "|" || cell[i + 1] !== "|") continue;
    if (lo >= 0 && i >= lo && i < hi) continue;
    if (choicesAt >= 0 && i > choicesAt) continue;
    parts.push(cell.slice(from, i));
    from = i + 2;
    i++;
  }
  if (!parts.length) return [cell];
  parts.push(cell.slice(from));
  return parts.map((p) => p.trim()).filter(Boolean);
}

// A Select row keeps its options between ~~ and ~~ (RULES.md §1); the prompt
// is everything else, colons included. No block, or an empty one, is an error.
function questionShape(prompt) {
  const p = prompt.trim();
  if (/^select\b/i.test(p)) {
    const block = p.match(/~~([\s\S]*?)~~/);
    if (!block) return { kind: "text", problem: "a Select row needs its options between ~~ and ~~" };
    if ((p.match(/~~/g) || []).length !== 2) return { kind: "text", problem: "a Select row must contain exactly one ~~…~~ block" };
    if (block[1].includes("||")) return { kind: "text", problem: "`||` inside the ~~…~~ block — it separates prompts, so an option cannot contain it" };
    const opts = splitSelectOptions(block[1]);
    if (!opts.length) return { kind: "text", problem: "the ~~…~~ block is empty" };
    if (opts.length < 2) return { kind: "select", opts, problem: "the ~~…~~ block holds one option — separate options with ` | `" };
    const prose = opts.find((o) => o.split(/\s+/).length > 8 || /\.\s/.test(o));
    if (prose) return { kind: "select", opts, problem: `an option reads as a sentence ("${prose.slice(0, 48)}…") — move it into the prompt` };
    return { kind: "select", opts };
  }
  if (p.includes("~~")) return { kind: "text", problem: "~~ is only for Select rows" };
  const m = p.match(/^(.*?)(?:\s+)?Choices:\s*(.+?)(?:\s+Answer with the letter only\.?)?$/is);
  if (m && m[1].trim() && m[2].trim()) {
    // Split only where a new `X)` marker opens, so an option may hold bars of
    // its own — `C) |a| > |b| | D) |a| = |b|` is two options, not six.
    const pieces = m[2].split(/\s*\|\s*(?=[A-Za-z]\)\s)/);
    const letters = pieces.map((o) => o.trim().match(/^([A-Za-z])\)\s*(.+)$/)).filter(Boolean).map((o) => o[1].toUpperCase());
    if (letters.length && letters.length !== pieces.length) return { kind: "letter", opts: letters, problem: "a piece of the Choices: list does not open with a letter and a bracket" };
    if (letters.length && m[2].includes("||")) return { kind: "letter", opts: letters, problem: "`||` inside the Choices: list — it separates prompts, so an option cannot contain it" };
    if (letters.length) return { kind: "letter", opts: letters };
  }
  return { kind: "text" };
}
function checkCsv(rel) {
  let rows;
  try { rows = parseCsv(readFileSync(join(root, rel), "utf8").replace(/^\uFEFF/, "")); }
  catch (e) { err(`${rel}: cannot read (${e.message})`); return 0; }
  if (!rows.length) { err(`${rel}: empty file`); return 0; }
  const header = rows[0].map((h) => h.trim());
  const col = {};
  for (const [k, names] of Object.entries(HEADER)) { const i = header.findIndex((h) => names.includes(h)); if (i >= 0) col[k] = i; }
  for (const k of ["id", "choices", "answers"]) if (!(k in col)) err(`${rel}: header lacks "${HEADER[k][0]}" (found: ${header.join(" | ")})`);
  if (!("choices" in col) || !("answers" in col)) return 0;
  const ids = new Set();
  for (let n = 1; n < rows.length; n++) {
    const r = rows[n], line = n + 1;
    const id = (r[col.id] ?? "").trim(), q = (r[col.choices] ?? "").trim(), a = (r[col.answers] ?? "").trim();
    if (!id) warn(`${rel}:${line}: no Question ID (the app falls back to row order)`);
    ids.add(id);
    if (!q) { err(`${rel}:${line} (Q${id}): empty Question Choices`); continue; }
    if (!a) { err(`${rel}:${line} (Q${id}): empty Question Answers`); continue; }
    for (const variant of splitVariants(q)) {
      const shape = questionShape(variant);
      if (shape.problem) err(`${rel}:${line} (Q${id}): ${shape.problem}`);
      if (shape.kind === "letter") {
        for (const set of answerSets(a)) for (const x of set) if (!shape.opts.includes(x.toUpperCase())) err(`${rel}:${line} (Q${id}): answer "${x}" is not one of the letters ${shape.opts.join("")}`);
      } else if (shape.kind === "select") {
        // The marker is case-insensitive, ignores a $…$ wrapper and spaces,
        // reads ²/³ as ^2/^3, and accepts any one of the `|` alternatives.
        const bare = (v) => v.trim().replace(/^\$(.*)\$$/s, "$1").replace(/\s+/g, "").replace(/²/g, "^2").replace(/³/g, "^3").toLowerCase();
        const opts = shape.opts.map(bare);
        // Like the app's expectedAnswersForInputs: alternatives separated by
        // `|` are merged per position, and a position passes if any matches.
        const sets = answerSets(a);
        const width = Math.max(...sets.map((s) => s.length));
        for (let pos = 0; pos < width; pos++) {
          const alts = sets.map((s) => s[pos]).filter(Boolean).flatMap((x) => x.split(/\s*\|\s*/));
          if (alts.length && !alts.some((alt) => opts.includes(bare(alt)))) err(`${rel}:${line} (Q${id}): Select answer "${alts.join("|")}" is not among the options [${shape.opts.join(" · ")}]`);
        }
        if (width > shape.opts.length) err(`${rel}:${line} (Q${id}): more answers than options`);
      }
    }
  }
  return ids.size;
}

// ---------------------------------------------------------------- curriculum
const KNOWN = new Set(["title", "url", "youtubeIds", "submenu"]);
const SECTIONS = ["Course Contents", "Worksheets", "Games"];
const referenced = new Set();
let curriculum = null;
try { curriculum = JSON.parse(readFileSync(join(root, "data", "curriculum.json"), "utf8")); }
catch (e) { err(`curriculum.json: ${e.message}`); }

function checkNode(node, path) {
  const where = path.join(" > ") || "(root)";
  if (node === null || typeof node !== "object" || Array.isArray(node)) { err(`${where}: expected an object`); return; }
  if (typeof node.title !== "string" || !node.title.trim()) err(`${where}: every node needs a non-empty title`);
  for (const k of Object.keys(node)) if (!KNOWN.has(k)) err(`${where}: unexpected key "${k}"`);
  const hasUrl = "url" in node, hasVideos = "youtubeIds" in node, hasKids = "submenu" in node;
  if (hasUrl) {
    if (typeof node.url !== "string" || !node.url.trim()) err(`${where}: url must be a non-empty string`);
    else {
      const m = node.url.match(/[?&]file=([^&]+)/);
      if (m) {
        const file = decodeURIComponent(m[1]);
        referenced.add(file);
        if (!allFiles.has(file)) err(`${where}: links to "${file}", which is not in this repo`);
      }
    }
  }
  if (hasVideos && (!Array.isArray(node.youtubeIds) || !node.youtubeIds.length || node.youtubeIds.some((v) => typeof v !== "string" || !v.trim())))
    err(`${where}: youtubeIds must be a non-empty array of strings, or absent`);
  if (hasKids) {
    if (!Array.isArray(node.submenu) || !node.submenu.length) err(`${where}: submenu must be a non-empty array, or absent`);
    else node.submenu.forEach((c) => checkNode(c, [...path, node.title]));
  }
  if (hasUrl && hasKids) err(`${where}: a node cannot be both a link and a branch`);
}
if (curriculum !== null) {
  if (!Array.isArray(curriculum)) err("curriculum.json: top level must be a list of sections");
  else {
    const titles = curriculum.map((s) => s && s.title);
    for (const s of SECTIONS) if (!titles.includes(s)) err(`curriculum.json: missing top-level section "${s}"`);
    curriculum.forEach((s) => checkNode(s, []));
  }
}

// ---------------------------------------------------------------- catalog
const catalogPath = "unit-tests/catalog/catalog.json";
const catalogued = new Set([catalogPath]);
try {
  const catalog = JSON.parse(readFileSync(join(root, catalogPath), "utf8"));
  if (!Array.isArray(catalog)) err(`${catalogPath}: must be a list`);
  else catalog.forEach((e, i) => {
    const where = `${catalogPath}[${i}]`;
    for (const k of ["grade", "unit", "file"]) if (typeof e[k] !== "string" || !e[k].trim()) err(`${where}: missing "${k}"`);
    if (typeof e.file === "string") {
      catalogued.add(e.file);
      if (!allFiles.has(e.file)) err(`${where}: file "${e.file}" is not in this repo`);
      else {
        const n = checkCsv(e.file);
        if (Number.isFinite(e.questionCount) && n && e.questionCount !== n) err(`${where}: questionCount is ${e.questionCount} but "${e.file}" has ${n} questions`);
      }
    }
  });
} catch (e) { err(`${catalogPath}: ${e.message}`); }

// ---------------------------------------------------------------- CSVs
let csvCount = 0;
for (const rel of allFiles) {
  if (!rel.toLowerCase().endsWith(".csv") || catalogued.has(rel)) continue;
  checkCsv(rel); csvCount++;
}
for (const rel of worksheetFiles) if (rel.toLowerCase().endsWith(".csv") && !referenced.has(rel)) warn(`no curriculum link points at ${rel}`);
for (const rel of unitTestFiles) if (rel.toLowerCase().endsWith(".csv") && !catalogued.has(rel)) warn(`catalog does not list ${rel}`);

// ---------------------------------------------------------------- report
for (const w of warnings) console.log(`warning: ${w}`);
for (const e of errors) console.error(`error: ${e}`);
console.log(`\nchecked ${csvCount + catalogued.size - 1} CSVs, ${referenced.size} curriculum links — ${errors.length} error(s), ${warnings.length} warning(s)`);
process.exit(errors.length ? 1 : 0);
