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
Select all irrational numbers: ~~$\sqrt{2}$ $\pi$ $3.14$~~
Select. David has a soccer game at 4:15 p.m. When should he leave? ~~3:30PM 3:20PM 3:40PM~~
Select the first step to solve by elimination: $3x + y = 12$ and $3x - y = 6$: ~~Add-equations Subtract-equations~~
```

Rules:

- **Exactly one `~~…~~` block per prompt** (per variant, if the cell uses `||`).
  A `Select` row without one is answered in a text box; the validator reports it.
- The block usually goes last, after the question, but it may sit anywhere —
  `Select ~~Yes, No~~ Is 5 × 7/9 less than 40/9?` works. The prompt shown to
  the learner is the cell with the block removed.
- A colon before the block is optional and only for reading: `Select the prime
  numbers: ~~1 3 7 9~~` and `Select the prime numbers ~~1 3 7 9~~` are the same.
- `~~` is reserved for this. A single `~` (used for ≡ in some number-theory
  solutions) is fine.
- The old form, options after a colon with no markers, is no longer read. All
  1,322 Select rows in the bank were converted on 2026-09-11.

## 2. How the options are separated

Inside the `~~…~~` block the parser tries three separators, in this order. Use the first
one that fits.

| Separator | Use it for | Example |
|---|---|---|
| ` \| ` (bar) | options with spaces in them | `Divide by 5 \| Subtract 2 \| Subtract 5` |
| `, ` (comma + space) | short lists, single words or numbers | `Yes, No` · `4, 5, 7, 8, 12` · `right triangle, obtuse triangle` |
| space | single tokens, math | `$\sqrt{2}$ $\pi$ $3.14$` · `Acute Right Obtuse` |

Rules that follow from this:

- **A bar wins.** If there is any ` | ` inside the block, it is the only separator;
  commas and spaces inside the options are then part of the option.
- **A comma only separates when it is followed by a space.** `1,000 999` is two
  options; `4, 5, 8` is three.
- **Math is one token.** Anything between `$…$` is never split, whatever it
  contains: `$(3, 3)$ $(4, 1)$` is two options; `$|x|$ $|y|$` is two options.
  Prices are not math — `$4 $5 $6` is three options, because a lone `$` with no
  closing `$` at a word boundary is just a dollar sign.
- **Quotes are also allowed** but no longer needed: `"Radius 4, Height 3"` is one
  option and the quotes are removed from the button. Prefer the bar.
- **Don't mix styles in one question.** `Linear, Nonlinear | None` uses the bar,
  so `Linear, Nonlinear` becomes one button.

## 3. The answer must be an option, written the same way

`Question Answers` must match one of the options inside the `~~…~~` block. Matching
ignores case, spaces and a `$…$` wrapper, and `²`/`³` equal `^2`/`^3` — but it
does not guess at spelling or punctuation.

```
✓  options: Linear Nonlinear None      answer: Nonlinear
✗  options: Linear Nonlinear None      answer: Non-linear
```

- **Several correct options** are separated by a comma: `4, 5, 8`. The learner
  must pick exactly those.
- **A correct option that contains a comma** (a coordinate pair, a list) uses
  `;` between answers instead, and then every comma is literal:
  `$(3,3)$; $(-2,-2)$`.
- **Alternative spellings** of one answer are separated by `|`: `None|none|0`.
  Any one of them matching an option is enough. (This `|` is in the *answers*
  cell; it does not conflict with the bar between options.)

## 4. Checklist before committing

1. The cell starts with `Select` and has **exactly one `~~…~~` block** holding
   the options.
2. The options use **one** separator: bar, comma-space, or space.
3. Every answer appears among the options, spelled the same way.
4. `node scripts/validate.mjs` reports no error for the file.

Order questions from easiest to hardest — for enrichment sheets the app samples
unit tests from the middle of the sheet, so the order matters there.
