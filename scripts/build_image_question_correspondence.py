#!/usr/bin/env python3
"""Build the image-to-question index from the four asset manifests and source CSVs."""
import csv
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'images/image-question-correspondence.json'
MANIFESTS = [
    ('worksheet-image-downloads.json', 'downloaded'),
    ('generated-question-graphs.json', 'generated'),
    ('unit-test-image-downloads.json', 'downloaded'),
    ('generated-unit-test-images.json', 'generated'),
]


def main():
    images, sources, seen = [], {}, set()
    for manifest, origin in MANIFESTS:
        for asset in json.loads((ROOT / 'images' / manifest).read_text())['images']:
            image_file, source_csv = asset['output_file'], asset['source_csv']
            assert image_file not in seen, f'Duplicate image: {image_file}'
            seen.add(image_file)
            assert (ROOT / image_file).is_file(), image_file
            if source_csv not in sources:
                with (ROOT / source_csv).open(encoding='utf-8-sig', newline='') as handle:
                    rows = list(csv.DictReader(handle))
                indexed = {row['Question ID'].strip(): row for row in rows}
                assert len(indexed) == len(rows), f'Duplicate question IDs: {source_csv}'
                sources[source_csv] = indexed
            qid = str(asset['question_id']).strip()
            row = sources[source_csv][qid]
            match = re.search(r'Q(\d+)I(\d+)$', Path(image_file).stem)
            assert match and match[1] == qid, (image_file, qid)
            entry = {
                'image_file': image_file,
                'source_type': 'worksheet' if source_csv.startswith('worksheets/') else 'unit_test',
                'source_csv': source_csv,
                'source_name': Path(source_csv).stem,
                'question_id': qid,
                'question_text': row['Question Choices'],
                'image_index': int(match[2]),
                'image_origin': origin,
                'use_for_question': True,
            }
            if asset.get('url'):
                entry['original_url'] = asset['url']
            if asset.get('source_image_correction'):
                entry['note'] = asset['source_image_correction']
            images.append(entry)

    original = 'images/unit-test-images/Grade 3/G3Unit4/UT-G3U4Q10I1.png'
    correction = 'images/unit-test-images/Grade 3/G3Unit4/UT-G3U4Q10I2.png'
    assert original in seen and correction in seen
    for entry in images:
        if entry['image_file'] == original:
            entry.update(use_for_question=False, replaced_by=correction,
                         note='Original URL image shows 18 circles, but the question specifies 21. Use the corrected I2 image.')

    actual = {str(p.relative_to(ROOT))
              for directory in ['worksheet-images', 'unit-test-images']
              for p in (ROOT / 'images' / directory).rglob('*')
              if p.is_file() and p.suffix.lower() in {'.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg'}}
    assert actual == seen, {'unmapped_images': sorted(actual-seen), 'missing_images': sorted(seen-actual)}
    images.sort(key=lambda e: (e['source_csv'], int(e['question_id']), e['image_index']))
    counts = Counter(e['source_type'] for e in images)
    document = {
        'schema_version': 1,
        'path_base': 'project_root',
        'description': 'One entry per question image. All paths are relative to the project root (the parent of the images folder). Preview/contact-sheet images are excluded. Question IDs are local to their source CSV. Respect use_for_question when displaying images.',
        'summary': {
            'total_images': len(images),
            'worksheet_images': counts['worksheet'],
            'unit_test_images': counts['unit_test'],
            'source_csv_files': len(sources),
            'questions_with_images': len({(e['source_csv'], e['question_id']) for e in images}),
            'usable_images': sum(e['use_for_question'] for e in images),
            'superseded_images': sum(not e['use_for_question'] for e in images),
        },
        'images': images,
    }
    OUTPUT.write_text(json.dumps(document, ensure_ascii=False, indent=2) + '\n')
    assert json.loads(OUTPUT.read_text()) == document
    print(json.dumps(document['summary'], indent=2))
    print(str(OUTPUT))


if __name__ == '__main__':
    main()
