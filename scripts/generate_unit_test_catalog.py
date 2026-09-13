#!/usr/bin/env python3
"""
Rebuild `unit-tests/catalog/catalog.json`, the index the site's launcher reads.

Every field in the catalog is derived from the CSVs themselves — the grade from
the folder, the unit name from the filename, the question count and the timer
from the rows — so the catalog is a *build product*, not a document. It used to
live in the site repository and be generated from whatever unit tests happened
to be checked out there, which is exactly how it came to list 62 of these 138
tests. The bank owns its own index now.

    python3 scripts/generate_unit_test_catalog.py            # write it
    python3 scripts/generate_unit_test_catalog.py --check    # CI: diff only

--check writes nothing and exits 1 if the committed file differs, naming the
command that fixes it. Two things go stale on their own and are the reason this
exists: `questionCount` after a row is added, and `totalTimeSeconds` after a
`Question Time` is edited. Neither is visible in a CSV diff.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UNIT_TESTS_DIR = ROOT / "unit-tests"
CATALOG_PATH = UNIT_TESTS_DIR / "catalog" / "catalog.json"
SKIP_DIRS = {"catalog", "__pycache__"}
ENRICHMENT_DIR = "enrichment"
SMALL_WORDS = {"and", "or", "of", "the", "a", "an", "to", "by", "in", "on", "for", "with"}

# Enrichment tracks sort after every school grade, in folder order.
LAST_SCHOOL_GRADE = 12


def folder_to_grade(folder_name: str) -> tuple[int, str, str]:
    """`4th-grade-math` -> (4, "4th grade math", "Grade 4")."""
    if folder_name == "grade-9":
        return (9, "9th grade math", "Grade 9")

    match = re.fullmatch(r"(\d+)(st|nd|rd|th)-grade-math", folder_name)
    if not match:
        raise ValueError(f"Unsupported unit-test folder name: {folder_name}")

    grade_number = int(match.group(1))
    return (grade_number, f"{match.group(1)}{match.group(2)} grade math", f"Grade {grade_number}")


def titleize(stem: str) -> str:
    """Folder and file slugs into the words a learner sees.

    Hyphens and underscores become spaces, small words stay lowercase after the
    first, and `3d` is `3D`. A hyphen *between digits* is a lesson number —
    `1-1` — and survives, which is what keeps "Modular Arithmetic 1-1" from
    flattening to "Modular Arithmetic 1 1".
    """
    clean_stem = re.sub(r"\.csv$", "", stem, flags=re.IGNORECASE).strip()
    parts = [part.strip() for part in clean_stem.split(" - ") if part.strip()]
    if len(parts) > 1 and parts[0].lower() == parts[1].lower():
        clean_stem = parts[0]
    elif parts:
        clean_stem = parts[0]

    protected = re.sub(r"(?<=\d)-(?=\d)", "\x00", clean_stem)
    words = protected.replace("_", " ").replace("-", " ").split()

    output = []
    for index, word in enumerate(words):
        lower = word.lower()
        if lower == "3d":
            output.append("3D")
        elif index and lower in SMALL_WORDS:
            output.append(lower)
        else:
            output.append(lower.capitalize())

    unit = " ".join(output).replace("\x00", "-")
    return re.sub(r"\bUnit Test\b$", "", unit, flags=re.IGNORECASE).strip()


def load_metrics(csv_path: Path) -> tuple[int, int]:
    """The row count, and the sum of `Question Time` — the whole-test timer."""
    with csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))

    total_seconds = 0
    for row in rows:
        try:
            raw_seconds = row.get("Question Time", row.get("Question Time (seconds)", ""))
            total_seconds += max(0, int(str(raw_seconds).strip() or "0"))
        except ValueError:
            continue

    return len(rows), total_seconds


def entry(
    csv_path: Path, grade_order: int, grade: str, unit: str, title: str, description: str
) -> dict[str, object]:
    question_count, total_time_seconds = load_metrics(csv_path)
    return {
        "gradeOrder": grade_order,
        "grade": grade,
        "unit": unit,
        "title": title,
        "description": description,
        "file": csv_path.relative_to(ROOT).as_posix(),
        "questionCount": question_count,
        "totalTimeSeconds": total_time_seconds,
    }


def school_entries(folder: Path) -> list[dict[str, object]]:
    grade_order, grade_label, grade_title = folder_to_grade(folder.name)
    entries = []
    for csv_path in sorted(folder.glob("*.csv")):
        unit = titleize(csv_path.stem)
        entries.append(
            entry(
                csv_path,
                grade_order,
                grade_label,
                unit,
                f"{grade_title} {unit} Unit Test",
                f"{grade_title} unit test for {unit} with a single full-worksheet timer.",
            )
        )
    return entries


def enrichment_entries(folder: Path) -> list[dict[str, object]]:
    """`enrichment/<track>/<topic>/<topic>-<lesson>-unit-test.csv`.

    A track is a course, not a grade, so it gets its own grade label and sorts
    after Grade 12. The tests sit one level deeper than a school grade's do,
    which is why this walks rather than globs.
    """
    entries = []
    tracks = sorted(child for child in folder.iterdir() if child.is_dir())

    for index, track in enumerate(tracks, start=1):
        track_name = titleize(track.name)
        grade_order = LAST_SCHOOL_GRADE + index

        for csv_path in sorted(track.rglob("*.csv")):
            stem = re.sub(r"-unit-test$", "", csv_path.stem, flags=re.IGNORECASE)
            lesson_match = re.fullmatch(r"(.*?)-(\d+-\d+)", stem)
            topic = titleize(lesson_match.group(1) if lesson_match else stem)
            lesson = lesson_match.group(2) if lesson_match else ""
            unit = f"{topic} {lesson}".strip()

            entries.append(
                entry(
                    csv_path,
                    grade_order,
                    f"Enrichment: {track_name}",
                    unit,
                    f"{track_name} {unit} Unit Test",
                    f"Enrichment {track_name} unit test for {topic}"
                    + (f" lesson {lesson}" if lesson else "")
                    + " with a single full-worksheet timer.",
                )
            )
    return entries


def build_catalog() -> list[dict[str, object]]:
    entries: list[dict[str, object]] = []

    for folder in sorted(UNIT_TESTS_DIR.iterdir()):
        if not folder.is_dir() or folder.name in SKIP_DIRS:
            continue
        if folder.name == ENRICHMENT_DIR:
            entries.extend(enrichment_entries(folder))
        else:
            entries.extend(school_entries(folder))

    entries.sort(key=lambda item: (int(item["gradeOrder"]), str(item["unit"])))
    return entries


def render(catalog: list[dict[str, object]]) -> str:
    return json.dumps(catalog, indent=4) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check", action="store_true", help="write nothing; fail if the committed file differs"
    )
    args = parser.parse_args()

    catalog = build_catalog()
    rendered = render(catalog)

    if args.check:
        current = CATALOG_PATH.read_text(encoding="utf-8") if CATALOG_PATH.exists() else ""
        if current == rendered:
            print(f"catalog.json is up to date ({len(catalog)} entries)")
            return 0
        print(
            f"catalog.json is out of date. Regenerate it with:\n"
            f"    python3 scripts/generate_unit_test_catalog.py",
            file=sys.stderr,
        )
        return 1

    CATALOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CATALOG_PATH.write_text(rendered, encoding="utf-8")
    print(f"Wrote {len(catalog)} unit test catalog entries to {CATALOG_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
