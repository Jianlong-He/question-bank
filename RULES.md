# Content, naming, and media rules

## File and folder names

- Grade worksheets live at `worksheets/Grade <G>/G<G>Unit <U>/G<G>U<U>W<W>[variant].csv`.
- Grade tests live at `unit-tests/Grade <G>/G<G>Unit<U>.csv`. The test filename has no space after `Unit`; worksheet unit folders do.
- Enrichment is a course, not a grade. Use `E-NT1` for Number Theory 1 and `E-CP1` for Counting and Probability 1. Worksheets use `E-<course>U<U>W<W>[variant].csv`; tests use `E-<course>U<U>T<T>.csv`.
- Enrichment unit folders are `U<number><topic>`, numbered in curriculum order, for example `U4conditional-probability`. Use the exact [course/unit directory list in README.md](README.md#file-and-folder-naming) across worksheets, tests, images, and videos. Do not invent a grade number for enrichment.
- New grade worksheet variants use `HW` and `Rev`. Preserve existing suffixes such as `_HW`, `_Revision`, `HWa`, and `HWb`, and existing compound numbers such as `W1-1`.
- Keep regular, homework, and revision images in separate folders named after their full CSV stems. Do not combine `G7U6W1`, `G7U6W1HW`, and `G7U6W1Rev`.
- A question is identified by its source CSV path and its local `Question ID`. Renames must preserve question IDs and update references to the source path.

## CSV and media fields

- New files use the seven core headers documented in [README.md](README.md#csv-schema). Every worksheet also has a `video` column; use `image` where image links are present. Existing header aliases and column order must survive unrelated edits.
- Read and write CSV with a CSV library, using UTF-8 with optional BOM. Quote commas, line breaks, and embedded quotes correctly. Every record must match its header's field count.
- The canonical image column is `image`, not `imageURL` or `imagesURL`. Local paths do not belong in URL columns.
- `image` values are relative to the external image root. `video` values are relative to `https://media.ktoinfinity.com/videos/sample-solution-videos/`. Omit `images/`, `videos/`, and `sample-solution-videos/` prefixes in the corresponding CSV cells. Never store absolute filesystem paths.
- A cell contains one path, a JSON array of paths for multiple assets, or an empty string. Video cells also support ` | ` between paths. Preserve spaces and capitalization; URL-encode segments only when building a URL. Do not use commas as path separators.
- Correspondence JSON files live at the repository root and use repository-relative source CSV paths and historical media paths. Keep `images/` and `videos/` there; strip one leading prefix only when writing the corresponding CSV media cell.
- Worksheet images live under `images/worksheet-images/<CSV parent folders>/<CSV stem>/`. Filenames use `WS-<worksheet-code>Q<question-id>I<image-index>.<ext>`, for example `WS-G7U6W1HWQ1I2.png` or `WS-E-NT1U3W4Q1I1.png`.
- Unit-test images live under `images/unit-test-images/<CSV parent folders>/<CSV stem>/`. Use `UT-G7U6Q1I1.png` for grade tests and `UT-E-NT1U1T2Q1I1.png` for enrichment tests. Here, parent folders mean the path below `worksheets/` or `unit-tests/`, respectively.
- Image indexes start at 1. Keep the actual extension. Normalize legacy `_HW` and `_Revision` to `HW` and `Rev` in image codes only; the containing folder retains the exact CSV stem.
- Image correspondence entries with `use_for_question: false` are superseded and must not be copied into CSV cells.
- Grade videos live under `videos/Grade <G>/Unit <U>/`; enrichment videos use the numbered enrichment course/unit folders. Keep lesson slugs and stable video IDs. Reused videos may live outside the consuming worksheet's unit.

## Question and answer syntax

How to write a `Select …` question in a worksheet or unit-test CSV so the app
renders one button per option and marks the answer correctly. The rules here
describe the syntax mirrored by `node scripts/validate.mjs`. Fill-in questions
remain valid without `Select` or `Choices:` markers.

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
- Do not use the old forms: options after a colon without markers, or a
  whitespace/comma-separated option block.

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

## Question quality checklist

1. For optioned questions, use either `Select` with exactly one `~~…~~` block per prompt variant, or a lettered `Choices:` list. Plain fill-in questions do not need either form.
2. Separate options with ` | ` and keep the scenario outside the option block. Every keyed choice must appear among the options.
3. Check the mathematics independently. Avoid multiple true options in a single-answer question. Specify domains, approximations, distributions, and units when they affect the answer.
4. Ensure the question, key, hints, solution, and linked image agree. Distinguish a limit from a function value, and an excluded upper bound from an attainable value.
5. For questions with many valid answers, provide an unambiguous constraint that selects the stored answer or use a grader that validates all valid solutions. Do not assume a finite list covers infinitely many integer pairs.

Order questions from easiest to hardest — for enrichment sheets the app samples
unit tests from the middle of the sheet, so the order matters there.

## Rename and validation checklist

1. Match the directory and filename patterns above, keeping enrichment units in curriculum order.
2. Update `data/curriculum.json` links and regenerate `unit-tests/catalog/catalog.json` when affected. Check school-grade unit labels against `data/grade-units.json`.
3. Update source paths, worksheet keys, and curriculum metadata in `worksheet-video-correspondence.json`, preserving video IDs, problem mappings, review status, and media records. Match renamed sources by their complete question IDs and text, not by a guessed filename.
4. Update the image source manifests and rebuild `image-question-correspondence.json` where affected. Keep current question text in the correspondence record.
5. Update every affected `image` and `video` CSV cell using its media-folder-relative path. Check references from other units too: videos can be shared.
6. Update generator output directories and hard-coded source references so a later run does not recreate old folders. Download scripts must preserve their existing URL manifests when current CSVs have no URL columns.
7. Keep historical migration and audit evidence intact; add an outcome or follow-up instead of globally replacing old paths in reports.
8. Run `node --test scripts/validate.test.mjs`, `node scripts/validate.mjs`, and `python3 scripts/generate_unit_test_catalog.py --check`. Validation checks media path formatting and source CSV existence, without requiring local media or checking remote availability. Check hosted asset availability separately when changing media links. Syntax validation does not replace mathematical review.
