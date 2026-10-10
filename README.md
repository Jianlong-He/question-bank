# Question Bank

A repository of K–12 and enrichment math practice content stored as plain CSV files, with corresponding teaching videos:

- **`worksheets/`** — per-unit practice, revision, and homework worksheets for Grades 1–12, plus enrichment tracks.
- **`unit-tests/`** — timed unit tests for Grades 1–12 and enrichment, indexed by a JSON catalog.
- **`videos/`** — MP4 teaching videos and a JSON correspondence file linking worksheet questions to videos.

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
│   └── enrichment/
│       ├── counting-and-probability 1/
│       │   └── <subtopic>/…       # PCF, PeCo, conditional-probability, …
│       └── number-theory 1/
│           └── <subtopic>/…       # CRT, RSA, modular-arithmetic, …
├── unit-tests/
│   ├── 1st-grade-math/ … 12th-grade-math/
│   │   └── <unit name>.csv
│   ├── enrichment/
│   └── catalog/
│       └── catalog.json           # index of all unit tests
└── videos/
    ├── Grade 1/ … Grade 12/
    │   └── Unit <U>/<video-id>.mp4
    ├── enrichment/
    │   └── <track>/<topic>/<video-id>.mp4
    └── worksheet-video-correspondence.json
```

### Content at a glance

| Grade | Unit folders | Worksheet CSVs |
|---:|---:|---:|
| 1 | 3 | 30 |
| 2 | 8 | 90 |
| 3 | 14 | 135 |
| 4 | 14 | 186 |
| 5 | 16 | 177 |
| 6 | 11 | 201 |
| 7 | 9 | 135 |
| 8 | 7 | 198 |
| 9 | 18 | 207 |
| 10 | 13 | 153 |
| 11 | 13 | 129 |
| 12 | 10 | 144 |
| enrichment | 2 tracks | 124 |

As of the October 2026 video update:

- 1,909 worksheet CSVs containing 12,921 question rows.
- 138 unit-test CSVs, all listed in `unit-tests/catalog/catalog.json`.
- 1,770 MP4 videos, including enrichment videos.
- 12,879 worksheet rows have video paths; 42 have blank video cells.

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

Every CSV starts with these seven columns. Worksheet CSVs append an eighth column, `video`; unit-test CSVs keep the seven-column format.

| Column | Description |
|---|---|
| `Question ID` | Sequential number within the file, starting at 1 |
| `Question Choices` | The question text. For multiple choice, options are appended inline as `Choices: A) … \| B) … \| C) … \| D) …` |
| `Question Answers` | The correct answer — a letter (`A`–`D`) for multiple choice, or the literal value for fill-in questions |
| `Question Time` | Seconds allotted for the question (typically `60`) |
| `Hints Allowed` | `Y` or `N` |
| `Hints` | Semicolon-separated hint steps; empty when `Hints Allowed` is `N` |
| `Solution` | Worked solution or answer explanation |
| `video` (worksheets only) | Repository-relative MP4 path; multiple paths separated by ` \| `; blank when no usable match is available |

### Examples

Fill-in-the-blank (worksheet):

```csv
Question ID,Question Choices,Question Answers,Question Time,Hints Allowed,Hints,Solution,video
1,Fill: 5 minutes = ___ seconds,300,60,N,,300,
```

With hints:

```csv
1,Calculate 124 × 16 by breaking 16 into 10 + 6.,1984,60,Y,Compute 124 × 10 and 124 × 6;Add them,124 × 16 = 1240 + 744 = 1984.,
```

Multiple choice (unit test, fields quoted):

```csv
"1","A solid is built using unit cubes. The figure has 2 identical layers, and each layer contains 16 cubes. What is the total volume of the figure in cubic units Choices: A) 16 | B) 24 | C) 32 | D) 48 Answer with the letter only.","C","60","N","","Correct answer: C (32)."
```

Note that some files quote all fields and some quote none — parse with a proper CSV reader rather than splitting on commas, since question text frequently contains commas.

---

## Worksheet videos

The `video` column contains file paths relative to the **repository root**, not the CSV's folder. For example, Question 1 in `worksheets/Grade 1/G1Unit 1/G1U1W1.csv` links to:

```text
videos/Grade 1/Unit 1/count-objects-one-to-one.mp4
```

Some questions have more than one video. Question 6 in `worksheets/enrichment/counting-and-probability 1/PMF/PMF_worksheet4.csv` contains:

```text
videos/enrichment/counting-and-probability 1/PMF/probability-geometric-ratio.mp4 | videos/enrichment/counting-and-probability 1/PMF/pattern-pmf-4be2809cd266.mp4
```

Parse the CSV first, then split only the `video` cell on ` | ` and remove empty entries. Preserve the path's spelling and case. The separator represents multiple available videos; it does not align videos with question variants.

Blank cells mean no usable match was assigned. In this update, 31 question rows have no MP4 path in the correspondence file, and 11 have question text that differs from the recorded mapping. A blank cell should produce no video button.

### Correspondence JSON

[`videos/worksheet-video-correspondence.json`](videos/worksheet-video-correspondence.json) records the detailed mappings:

1. Find the worksheet by its exact repository-relative path in `worksheets`.
2. Find the question by its exact CSV `Question ID` in that worksheet's `problems` object.
3. Check `question_sha256` against the SHA-256 of the UTF-8 decoded `Question Choices` cell, without normalization, to detect changed question text.
4. Follow each `video_links[].video_id` into the top-level `videos` object, then read `assets.mp4`.
5. Add distinct paths whose MP4 files exist. Leave the cell blank if no valid path remains.

The JSON also records mapping review status, coverage, question variant indexes, and playback start/end times. Use it when a player needs those details; the CSV column stores paths only. A `needs_review` mapping is a draft assignment, and a rendered video does not by itself establish that the mapping has been reviewed. The JSON includes planned and retired video records as well as rendered assets, so its number of video records exceeds the number of MP4 files.

### Loading videos on a website

Reading a CSV or the correspondence JSON does not download the videos. Render video controls for the current question and create a player when the student selects a video. Use `preload="none"` and assign the selected video's source on demand; avoid creating a player for every video in the repository.

Resolve paths against the base URL where the repository's files are served, and URL-encode each path segment because folder names contain spaces. The resulting URL must serve MP4 data, rather than a repository file-view HTML page. For multiple paths, let the student choose which video to play.

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
3. Preserve the first seven column names and their order. For worksheets, append the lowercase `video` column; for unit tests, use only the seven-column header.
4. Number `Question ID` from 1, with no gaps.
5. For a new unit test, add a corresponding entry to `unit-tests/catalog/catalog.json` and make sure `questionCount` matches the row count.
6. For a worksheet video, add the MP4 under `videos/`, update the correspondence JSON, and populate the worksheet's `video` cell with its repository-relative path. Recheck the question text and hash when editing an existing mapped question.
7. Run `node scripts/validate.mjs` for CSV and curriculum checks. Separately verify that every nonblank `video` path resolves to an existing MP4; the validator does not check video mappings.

## Conventions and caveats

- Some legacy Grade 2 filenames carry a doubled extension (`… - place_value.csv.csv`); the catalog references them as-is, so don't rename without updating `catalog.json`.
- Folder and file names contain spaces. Quote paths in shell commands.
- `worksheets/Grade 4/G4Unit 8/` includes a reference-material PDF alongside the CSVs.
