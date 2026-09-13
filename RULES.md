# Writing Select questions

How to write a `Select …` question in a worksheet or unit-test CSV so the app
renders one button per option and marks the answer correctly. The rules here
are exactly what the parser does; `node scripts/validate.mjs` checks every row
against them.

## 1. The options go between `~~` and `~~`

A Select row is a `Question Choices` cell that starts with the word `Select` and
holds its options between two `~~` markers. The parser takes what is between
the markers as the option list and **everything else as the prompt** — colons,
times, ratios and equations in the prompt mean nothing to it.

```
Select all irrational numbers: ~~$\sqrt{2}$ | $\pi$ | $3.14$~~
Select. David has a soccer game at 4:15 p.m. When should he leave? ~~3:30PM | 3:20PM | 3:40PM~~
Select the first step to solve by elimination: $3x + y = 12$ and $3x - y = 6$: ~~Add equations | Subtract equations~~
```

Rules:

- **Exactly one `~~…~~` block per prompt** (per variant, if the cell uses `||`).
  A `Select` row without one is answered in a text box; the validator reports it.
- The block usually goes last, after the question, but it may sit anywhere —
  `Select ~~Yes | No~~ Is 5 × 7/9 less than 40/9?` works. The prompt shown to
  the learner is the cell with the block removed.
- A colon before the block is optional and only for reading: `Select the prime
  numbers: ~~1 | 3 | 7 | 9~~` and `Select the prime numbers ~~1 | 3 | 7 | 9~~`
  are the same.
- `~~` is reserved for this. A single `~` (used for ≡ in some number-theory
  solutions) is fine.
- **Only options go inside the markers.** A scenario or a sentence setting the
  question up belongs in the prompt, before them.

## 2. One separator: the bar

Inside the `~~…~~` block, ` | ` separates the options and nothing else does.

```
~~Divide by 5 | Subtract 2 | Subtract 5~~
~~right triangle | obtuse triangle~~
~~Yes | No~~
~~$\sqrt{2}$ | $\pi$ | $3.14$~~
```

Rules that follow from this:

- **A comma, a space or a period inside an option is just text.** `4, 5, 8` is
  one option; `4 | 5 | 8` is three. `Radius 4, Height 3` needs no quoting.
- **Math is one token either way.** Anything between `$…$` is never split, so a
  bar inside it belongs to the option: `$|x|$ | $|y|$` is two options.
- An option that must contain a bare `|` outside `$…$` is wrapped in quotes:
  `"a | b" | c`. The quotes are removed from the button.
- **A `||` never appears inside the block.** `||` separates two whole prompts,
  so an option cannot hold one; write `Triangle and quadrilateral`, not
  `Triangle||Quadrilateral`.
- The old forms — options after a colon with no markers, and the
  whitespace-or-comma separated block — are no longer read. All 1,343 Select
  rows in the bank were converted on 2026-09-13.

## 3. The answer must be an option, written the same way

`Question Answers` must match one of the options inside the `~~…~~` block. Matching
ignores case, spaces and a `$…$` wrapper, and `²`/`³` equal `^2`/`^3` — but it
does not guess at spelling or punctuation.

```
✓  options: Linear | Nonlinear | None      answer: Nonlinear
✗  options: Linear | Nonlinear | None      answer: Non-linear
```

- **Several correct options** are separated by a comma: `4, 5, 8`. The learner
  must pick exactly those.
- **A correct option that contains a comma** (a coordinate pair, a list) uses
  `;` between answers instead, and then every comma is literal:
  `$(3,3)$; $(-2,-2)$`.
- **Alternative spellings** of one answer are separated by `|`: `None|none|0`.
  Any one of them matching an option is enough. (This `|` is in the *answers*
  cell, between whole answers; it does not conflict with the bar between
  options.)

## 4. Multiple choice with letters

The other optioned form is the lettered one, used by the unit tests:

```
What is P(A and B) Choices: A) 0.9 | B) 0.2 | C) 0.1 | D) 0.45 Answer with the letter only.
```

- The list splits at each ` | ` that opens a new `X)` marker, so an option may
  hold bars of its own: `C) |a| > |b| | D) |a| = |b|` is two options.
- `Question Answers` is the letter. Two letters separated by `|` mean either is
  accepted, for a question with two equally correct options (`A|B`).
- A `||` cannot appear in the list, for the same reason as in §2.

## 5. Checklist before committing

1. The cell starts with `Select` and has **exactly one `~~…~~` block** holding
   the options — or it is a lettered `Choices:` row.
2. Options are separated by ` | `, and nothing inside the markers is a sentence.
3. Every answer appears among the options, spelled the same way.
4. `node scripts/validate.mjs` reports no error for the file.

Order questions from easiest to hardest — for enrichment sheets the app samples
unit tests from the middle of the sheet, so the order matters there.
