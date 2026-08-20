# Question Bank

A repository of K–12 math practice content stored as plain CSV files. It contains two collections:

- **`worksheets/`** — per-unit practice, revision, and homework worksheets for Grades 1–12, plus enrichment tracks.
- **`unit-tests/`** — timed, multiple-choice unit tests for Grades 1–6 and Grade 9, indexed by a JSON catalog.

Everything is data — there is no application code in this repo. The CSVs are meant to be consumed by a worksheet/quiz renderer.

---

## Repository layout

```
question-bank/
├── worksheets/
│   ├── Grade 1/ … Grade 12/
│   │   ├── G<N>Unit <U>/          # e.g. G4Unit 14
│   │   │   ├── G4U14W1.csv        # practice worksheet
│   │   │   ├── G4U14W8_Revision.csv
│   │   │   └── G4U14W10_HW.csv
│   │   └── grade<N>half/          # half-year variants (Grades 2–5)
│   │       └── Unit <U>/
│   └── enrichment/
│       ├── counting-and-probability 1/
│       │   └── <subtopic>/…       # PCF, PeCo, conditional-probability, …
│       └── number-theory 1/
│           └── <subtopic>/…       # CRT, RSA, modular-arithmetic, …
└── unit-tests/
    ├── 1st-grade-math/ … 6th-grade-math/, grade-9/
    │   └── <unit name>.csv
    └── catalog/
        └── catalog.json           # index of all unit tests
```

### Content at a glance

| Grade | Unit folders | Half-year set | Worksheet CSVs |
|---:|---:|:---:|---:|
| 1 | 3 | — | 30 |
| 2 | 8 | ✓ | 72 |
| 3 | 14 | ✓ | 135 |
| 4 | 14 | ✓ | 186 |
| 5 | 16 | ✓ | 175 |
| 6 | 10 | — | 64 |
| 7 | 9 | — | 45 |
| 8 | 7 | — | 66 |
| 9 | 18 | — | 69 |
| 10 | 13 | — | 51 |
| 11 | 13 | — | 43 |
| 12 | 10 | — | 48 |
| enrichment | 2 tracks | — | 89 |

Unit tests: 62 tests across Grades 1–6 and Grade 9, all listed in `unit-tests/catalog/catalog.json`.

---

## File naming

**Worksheets** follow `G<grade>U<unit>W<worksheet>[suffix].csv`:

| Example | Meaning |
|---|---|
| `G10U3W1.csv` | Grade 10, Unit 3, Worksheet 1 — standard practice |
| `G4U14W8_Revision.csv` / `G9U2W3Rev.csv` | Revision worksheet |
| `G4U14W10_HW.csv` / `G8U6W4HW.csv` | Homework worksheet |

Both the underscored (`_Revision`, `_HW`) and bare (`Rev`, `HW`) suffix styles appear in the repo; treat them as equivalent.

**Enrichment** files use `<subtopic>_worksheet<N>[Rev].csv`, e.g. `prime-factorization_worksheet4.csv`.

**Unit tests** are named after the unit itself, e.g. `unit-tests/5th-grade-math/volume.csv`.

---

## CSV schema

Every CSV — worksheet and unit test alike — uses the same seven columns:

| Column | Description |
|---|---|
| `Question ID` | Sequential number within the file, starting at 1 |
| `Question Choices` | The question text. For multiple choice, options are appended inline as `Choices: A) … \| B) … \| C) … \| D) …` |
| `Question Answers` | The correct answer — a letter (`A`–`D`) for multiple choice, or the literal value for fill-in questions |
| `Question Time` | Seconds allotted for the question (typically `60`) |
| `Hints Allowed` | `Y` or `N` |
| `Hints` | Semicolon-separated hint steps; empty when `Hints Allowed` is `N` |
| `Solution` | Worked solution or answer explanation |

### Examples

Fill-in-the-blank (worksheet):

```csv
Question ID,Question Choices,Question Answers,Question Time,Hints Allowed,Hints,Solution
1,Fill: 5 minutes = ___ seconds,300,60,N,,300
```

With hints:

```csv
1,Calculate 124 × 16 by breaking 16 into 10 + 6.,1984,60,Y,Compute 124 × 10 and 124 × 6;Add them,124 × 16 = 1240 + 744 = 1984.
```

Multiple choice (unit test, fields quoted):

```csv
"1","A solid is built using unit cubes. The figure has 2 identical layers, and each layer contains 16 cubes. What is the total volume of the figure in cubic units Choices: A) 16 | B) 24 | C) 32 | D) 48 Answer with the letter only.","C","60","N","","Correct answer: C (32)."
```

Note that some files quote all fields and some quote none — parse with a proper CSV reader rather than splitting on commas, since question text frequently contains commas.

---

## Unit test catalog

`unit-tests/catalog/catalog.json` is an array of entries describing each test:

```json
{
  "gradeOrder": 5,
  "grade": "5th grade math",
  "unit": "Volume",
  "title": "Grade 5 Volume Unit Test",
  "description": "Grade 5 unit test for Volume with a single full-worksheet timer.",
  "file": "unit-tests/5th-grade-math/volume.csv",
  "questionCount": 12,
  "totalTimeSeconds": 720
}
```

`file` paths are relative to the repository root. `totalTimeSeconds` is a single timer for the whole test, not per question.

---

## Working with the data

Read a worksheet in Python:

```python
import csv

with open("unit-tests/5th-grade-math/volume.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        print(row["Question ID"], row["Question Answers"])
```

Load the catalog and resolve each test:

```python
import json, pathlib

catalog = json.loads(pathlib.Path("unit-tests/catalog/catalog.json").read_text())
for entry in catalog:
    assert pathlib.Path(entry["file"]).exists(), entry["file"]
```

---

## Adding content

1. Place the file in the matching grade/unit folder, creating `G<N>Unit <U>/` if it doesn't exist.
2. Follow the naming convention above.
3. Use the seven-column header exactly as written — column names and order matter to the renderer.
4. Number `Question ID` from 1, with no gaps.
5. For a new unit test, add a corresponding entry to `unit-tests/catalog/catalog.json` and make sure `questionCount` matches the row count.

## Conventions and caveats

- Some legacy Grade 2 filenames carry a doubled extension (`… - place_value.csv.csv`); the catalog references them as-is, so don't rename without updating `catalog.json`.
- Folder and file names contain spaces. Quote paths in shell commands.
- `worksheets/Grade 4/G4Unit 8/` includes a reference-material PDF alongside the CSVs.
