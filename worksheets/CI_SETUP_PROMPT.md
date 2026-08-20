# Prompt: build CI for the question-bank repository

Give this file to an AI assistant working inside the **question-bank**
repository. It is self-contained — the assistant does not need any other
context. Delete it from the content tree once the CI exists.

---

## Your task

Create three files in this repository:

1. `scripts/validate_csvs.py`
2. `.github/workflows/validate.yml`
3. `.github/workflows/publish.yml`

## What this repository is

A private repository holding every question the KtoInfinity math site serves.
Two content trees, one CSV format:

```
worksheets/    course-content and practice sheets   (~1,073 CSVs)
unit-tests/    graded unit tests                    (~62 CSVs)
```

It is private because every CSV contains `Question Answers` and `Solution`
columns. This repository is the answer key.

The site lives in a separate repository (`content_base`). It syncs this
content at build time, so nothing here is fetched by a browser directly.

## The CSV format

Seven columns:

```
Question ID,Question Choices,Question Answers,Question Time,Hints Allowed,Hints,Solution
```

Some files add an eighth image column (`ImageURL` or `Image URL`).
`Question Time` is whole seconds. Multiple acceptable answers are separated
by `|`, for example `1/2|0.5`.

## The two consumers, and why they disagree

**This is the most important section. Read it before writing any validation.**

The content has exactly two readers, and they tolerate different things. A
validator that is stricter than both produces false alarms, which is worse
than no validator — it trains people to ignore CI.

### Reader 1 — the game (`matterofmath/game.js`, reads `worksheets/`)

It parses CSV with its own splitter, not a library:

```js
const lines = text.trim().split(/\r?\n/);
const header = lines.shift().split(/,(?=(?:[^"]*"[^"]*")*[^"]*$)/).map(unquote);
```

Three consequences you must respect:

- `text.trim()` removes U+FEFF, so **a UTF-8 BOM is harmless here.**
- The split regex only breaks on commas followed by an even number of quotes,
  so **a space before an opening quote is tolerated**: `, "1/2, 3/10"` parses
  correctly even though Python's `csv` module mis-splits it.
- Columns resolve through aliases, so `Question Answer` is as valid as
  `Question Answers`. The full alias list:

  | canonical | accepted |
  | --- | --- |
  | Question ID | `Question ID`, `QuestionID`, `Question Number`, `QuestionNumber` |
  | Question Choices | `Question Choices`, `QuestionChoices` |
  | Question Answers | `Question Answers`, `Question Answer`, `QuestionAnswers`, `QuestionAnswer` |
  | Question Time | `Question Time`, `Question Time (seconds)`, `QuestionTime` |
  | Hints Allowed | `Hints Allowed`, `HintsAllowed` |
  | Solution | `Solution`, `Solutions` |
  | Image | `Image URL`, `ImageURL`, `Image`, `ImageUrl`, `image_url` |

- A missing or empty `Question ID` falls back to the row's position, so an
  unnamed id column is not fatal.

### Reader 2 — the catalog generator (Python, reads `unit-tests/` only)

The site runs a script that walks `unit-tests/`, reads each CSV with Python's
`csv.DictReader`, and derives a catalog including a question count and a total
time. Python's reader **is** strict about quoting. So the same quoting problem
that the game shrugs off will corrupt a unit test's metadata.

It also maps folder names to grades and raises on anything unexpected:

```python
grade-9                    -> Grade 9
<N>st|nd|rd|th-grade-math  -> Grade N     e.g. 1st-grade-math, 5th-grade-math
anything else              -> ValueError, build fails
```

### Severity rules that follow

| condition | `worksheets/` | `unit-tests/` |
| --- | --- | --- |
| file is not valid UTF-8 | **error** | **error** |
| no column matching a required canonical name (after aliases) | **error** | **error** |
| file has no data rows | **error** | **error** |
| folder name outside the grade pattern | n/a | **error** |
| answer empty under a strict reader | warning | **error** |
| `Question Time` non-numeric under a strict reader | warning | **error** |
| UTF-8 BOM present | warning | warning |
| header ends with empty columns | warning | warning |

Not valid UTF-8 is always an error because the site fetches these files and
decodes them as UTF-8; bad bytes become replacement characters a learner sees.

## Requirements for `scripts/validate_csvs.py`

- Python 3.12, standard library only.
- Walk `worksheets/` and `unit-tests/`, skipping any `catalog/` directory.
- Apply the severity table above. Print a summary line, then warnings, then
  errors, each with the file path and row number.
- Exit `1` if there is at least one error, `0` otherwise. Warnings never fail.
- Exit `1` and say so if it finds no CSV files at all — that means a broken
  checkout, and silently passing would be worse.
- Explain in a module docstring *why* BOMs and quote spacing are warnings for
  worksheets but errors for unit tests. The next person will otherwise assume
  it is a bug and tighten it.
- Do not modify, reformat, or rewrite any CSV. This script only reports.

## Requirements for `.github/workflows/validate.yml`

Run on `push` and `pull_request`. Check out the repository, set up Python
3.12, run `python3 scripts/validate_csvs.py`.

## Requirements for `.github/workflows/publish.yml`

Run on push to `main` only. It tells the site repository to rebuild:

- Run the validator first. Never dispatch content that would fail the site
  build.
- Then send a `repository_dispatch` to `plkt0610/content_base` with event type
  `question-bank-updated`, using `peter-evans/repository-dispatch@v3` and a
  token from `secrets.SITE_DISPATCH_TOKEN`.
- Include the current commit in the payload as `{"sha": "${{ github.sha }}"}`.
  The site checks out that exact commit, so a later push cannot change what a
  build deploys and the shipped content stays identifiable.

## How to know you got it right

Run the validator against the real content in this repository. A correct
implementation reports **zero errors** and roughly **150 warnings** (mostly
BOMs in the enrichment worksheets, plus quote-spacing in a few Grade 7 files).

If you see a large number of *errors*, you have almost certainly been stricter
than the game's parser — re-read the consumers section. The common mistakes
are treating a BOM as fatal, using `csv.DictReader` semantics to judge
`worksheets/`, and checking column names without the alias table.

## Out of scope

Do not write a check for whether a CSV is *referenced* by the site. Nothing in
this repository can know that: reachability is defined by `app.js` in the site
repository, which has its own `scripts/check_content_links.py` for it.
