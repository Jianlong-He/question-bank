# Math Question Bank

Math practice and unit-test questions for Grades 1–12 and enrichment, stored as CSV files with references to externally hosted images and teaching videos. This repository contains content and maintenance scripts; the learning application lives elsewhere.

Read [RULES.md](RULES.md) before adding or changing questions, filenames, folders, or media references.

## Repository layout

```text
worksheets/
  Grade 7/G7Unit 6/G7U6W1.csv
  Grade 7/G7Unit 6/G7U6W1HW.csv
  Grade 7/G7Unit 6/G7U6W1Rev.csv
  enrichment/number-theory 1/U3Euclidean-division/E-NT1U3W4.csv
unit-tests/
  Grade 7/G7Unit6.csv
  enrichment/number-theory 1/U1modular-arithmetic/E-NT1U1T1.csv
  catalog/catalog.json
image-question-correspondence.json
worksheet-video-correspondence.json
data/curriculum.json
scripts/
reports/
```

Media binaries are stored outside this repository; local `images/` and `videos/` folders are not required for validation. Image parent folders mirror the path below `worksheets/` or `unit-tests/`. There are no separate half-year folders in the current collection.

### Current inventory

Counts as of 2026-10-11:

| Collection | Worksheet unit folders | Worksheet CSVs |
|---|---:|---:|
| Grade 1 | 3 | 30 |
| Grade 2 | 8 | 90 |
| Grade 3 | 14 | 135 |
| Grade 4 | 14 | 186 |
| Grade 5 | 16 | 177 |
| Grade 6 | 11 | 201 |
| Grade 7 | 9 | 135 |
| Grade 8 | 7 | 198 |
| Grade 9 | 18 | 207 |
| Grade 10 | 13 | 153 |
| Grade 11 | 13 | 129 |
| Grade 12 | 10 | 144 |
| Enrichment: 2 courses | 11 | 124 |
| **Total** | **147** | **1,909** |

There are also **138 unit-test CSVs containing 1,587 questions**, indexed by `unit-tests/catalog/catalog.json`. Enrichment tests currently cover Number Theory 1 units 1 and 2.

## File and folder naming

| Content | Convention | Example |
|---|---|---|
| Grade worksheet folder | `worksheets/Grade <G>/G<G>Unit <U>/` | `worksheets/Grade 7/G7Unit 6/` |
| Grade worksheet | `G<G>U<U>W<W>[variant].csv` | `G7U6W1.csv` |
| Grade unit test | `unit-tests/Grade <G>/G<G>Unit<U>.csv` | `unit-tests/Grade 7/G7Unit6.csv` |
| Enrichment worksheet | `E-<course>U<U>W<W>[variant].csv` | `E-NT1U3W4.csv` |
| Enrichment unit test | `E-<course>U<U>T<T>.csv` | `E-NT1U1T2.csv` |

Use `HW` for homework and `Rev` for revision in new grade worksheets. Existing `_HW`, `_Revision`, `HWa`, `HWb`, and compound worksheet numbers such as `W1-1` are supported; preserve them during unrelated edits. Question IDs belong to their CSV and stay stable when it moves.

Enrichment folders use `U<number><topic>`, with no separator between the number and topic. Numbers follow curriculum order within the course; enrichment courses are not school grades. Use the same course/unit folder names under worksheets, unit tests where present, worksheet images, and videos:

| Course directory | Code | Unit directories, in order |
|---|---|---|
| `counting-and-probability 1` | `CP1` | `U1counting-and-classification`, `U2PCF`, `U3PeCo`, `U4conditional-probability`, `U5PMF` |
| `number-theory 1` | `NT1` | `U1modular-arithmetic`, `U2prime-factorization`, `U3Euclidean-division`, `U4number-theory1_review`, `U5CRT`, `U6RSA` |

Preserve capitalization and spaces exactly. School-grade unit names and numbers are recorded in `data/grade-units.json`.

## CSV schema

Use these seven core columns for new files, followed by media columns as needed:

| Column | Content |
|---|---|
| `Question ID` | Unique numeric ID within the file; start new files at 1 |
| `Question Choices` | Prompt, with inline options when applicable |
| `Question Answers` | Answer letter, literal answer, or supported answer alternatives |
| `Question Time` | Time in seconds |
| `Hints Allowed` | `Y` or `N` |
| `Hints` | Hint steps; blank when disabled |
| `Solution` | Correct explanation consistent with the prompt and answer |
| `image` | Optional relative image path, JSON array of paths, or blank |
| `video` | Relative video path, ` | `-separated paths, JSON array of paths, or blank; present in every worksheet CSV |

Existing unit tests may use `Question Answer`, `Question Time (seconds)`, and `Yes`/`No`. Some legacy worksheets retain unnamed empty columns. Preserve existing headers during unrelated edits and read columns by name; `image` and `video` do not have a fixed position. Do not reintroduce `imageURL` or `imagesURL` as the canonical media column.

Use a proper CSV reader/writer. Quote fields containing commas, quotes, or line breaks; double embedded quotes. Every row must have the same field count as its header. Read with `utf-8-sig` to support files with or without a UTF-8 BOM. See [question and answer syntax](RULES.md#question-and-answer-syntax).

## Images and videos

CSV `image` paths are relative to the external image root, without a leading `images/`. CSV `video` paths are relative to **`https://media.ktoinfinity.com/videos/sample-solution-videos/`**, without a leading `videos/` or `sample-solution-videos/`. Preserve spaces in stored paths and URL-encode each path segment when building a playback URL. Correspondence JSON media paths retain their historical `images/` and `videos/` prefixes; they do not require files in this checkout. Blank cells mean no linked asset. Multiple videos may use ` | `; both media columns also support a JSON array of strings inside one properly quoted CSV cell.

For example, a decoded `image` cell may contain:

```text
worksheet-images/Grade 7/G7Unit 6/G7U6W1/WS-G7U6W1Q1I2.png
```

| Image filename example | Meaning |
|---|---|
| `WS-G7U6W1Q1I2.png` | Grade 7, Unit 6, Worksheet 1, question 1, image 2 |
| `WS-G7U6W1HWQ1I1.png` | Homework counterpart, question 1, image 1 |
| `WS-G7U6W1RevQ1I1.png` | Revision counterpart, question 1, image 1 |
| `WS-E-NT1U3W4Q1I1.png` | Number Theory 1, Unit 3, Worksheet 4, question 1, image 1 |
| `UT-G7U6Q1I1.png` | Grade 7, Unit 6 test, question 1, image 1 |
| `UT-E-NT1U1T2Q1I1.png` | Number Theory 1, Unit 1, Test 2, question 1, image 1 |

Every worksheet with images gets a subfolder named exactly after its CSV stem. Regular, homework, and revision worksheets therefore have separate folders. For legacy suffixes, the folder keeps the exact CSV stem while the image code normalizes `_HW` to `HW` and `_Revision` to `Rev`. Unit-test image folders also use their CSV stem. Keep the actual image extension.

Find images by `(source_csv, question_id)` in `image-question-correspondence.json`. Only entries with `use_for_question: true` populate image cells; superseded assets remain documented. Image indexes start at 1.

Find worksheet video links in `worksheet-video-correspondence.json`, then resolve each `video_id` through `videos[video_id].assets.mp4`. Video filenames are lesson slugs. A video may be shared across worksheets, grades, and courses. Preserve stable video IDs and reviewed mappings when paths change. Do not invent a path for a missing asset or a `not_needed` mapping.

## Catalogs, generators, and validation

`data/curriculum.json` contains worksheet links. The test catalog records each test's repository-relative `file`, question count, and total timer derived from the CSV.

```sh
node --test scripts/validate.test.mjs
node scripts/validate.mjs
python3 scripts/generate_unit_test_catalog.py --check
```

These commands run validator regression tests, validate the content, and check the generated test catalog. Content validation checks question syntax, naming, row widths, media path formatting, and correspondence source CSVs. It reads correspondence JSON files from the repository root. It does not require local media copies, contact the media host, verify remote asset availability, or prove mathematical correctness. The legacy media generators require their local production assets and manifests; they are not part of this hosted-media CI check.

After adding or changing tests, run `python3 scripts/generate_unit_test_catalog.py`. After changing image assets or source paths, update their source manifests and run `python3 scripts/build_image_question_correspondence.py`. Synchronize affected CSV media cells separately, removing the media-root prefix. Rebuilding a correspondence JSON does not update CSV cells.

Image download scripts ingest legacy URL columns; current `image` cells hold relative paths. Their download manifests retain original URLs. Empty URL scans must preserve existing manifests. Video generators must use numbered enrichment folders.

When renaming content, update active curriculum links, catalogs, media mappings, source manifests, CSV media cells, and generator paths together. Historical audit and migration reports may contain old paths as evidence. See the [rename checklist](RULES.md#rename-and-validation-checklist).
