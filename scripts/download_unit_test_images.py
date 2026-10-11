#!/usr/bin/env python3
"""Import legacy image URL cells without changing CSVs or local `image` paths."""
import concurrent.futures
import csv
import hashlib
import json
import re
from pathlib import Path
from PIL import Image
from download_worksheet_images import fetch

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'images/unit-test-images'
REPORT = ROOT / 'images/unit-test-image-downloads.json'


def main():
    entries, hashes = [], {}
    for source in sorted((ROOT / 'unit-tests').rglob('*.csv')):
        hashes[str(source.relative_to(ROOT))] = hashlib.sha256(source.read_bytes()).hexdigest()
        for row in csv.DictReader(source.open(encoding='utf-8-sig', newline='')):
            urls = []
            for key, value in row.items():
                if key and re.sub('[^a-z]', '', key.lower()) in {'imageurl', 'imagesurl', 'imageurls', 'imagesurls'} and value.strip():
                    found = re.findall(r'https?://[^\s|,;<>"\[\]]+', value)
                    if not found:
                        raise ValueError((source, value))
                    urls.extend(found)
            if not urls:
                continue
            match = re.fullmatch(r'G(\d+)Unit\s*(\d+)', source.stem)
            code = f'G{match[1]}U{match[2]}' if match else source.stem
            qid = row['Question ID'].strip()
            assert qid.isdigit()
            for index, url in enumerate(urls, 1):
                target = DEST / source.relative_to(ROOT/'unit-tests').parent / source.stem / f'UT-{code}Q{qid}I{index}'
                entries.append(dict(source_csv=str(source.relative_to(ROOT)), question_id=qid,
                                    image_index=index, url=url, output_stem=str(target.relative_to(ROOT))))
    if not entries:
        print('No legacy image URLs found; preserving the existing download manifest.')
        return
    assert len({e['output_stem'] for e in entries}) == len(entries)
    by_url = {}
    for entry in entries:
        by_url.setdefault(entry['url'], []).append(entry)
    failures = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        jobs = {pool.submit(fetch, url): url for url in by_url}
        for job in concurrent.futures.as_completed(jobs):
            url = jobs[job]
            try:
                data, ext = job.result()
                for entry in by_url[url]:
                    target = ROOT / (entry['output_stem'] + ext)
                    target.parent.mkdir(parents=True, exist_ok=True)
                    if target.exists() and target.read_bytes() != data:
                        raise ValueError(f'Existing image differs: {target}')
                    if not target.exists():
                        target.write_bytes(data)
                    with Image.open(target) as im:
                        dimensions = list(im.size)
                        im.verify()
                    entry.update(output_file=str(target.relative_to(ROOT)), status='downloaded',
                                 bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), dimensions=dimensions)
            except Exception as error:
                failures.append(dict(url=url, error=str(error)))
                for entry in by_url[url]:
                    entry.update(status='failed', error=str(error))
    changed = [p for p, h in hashes.items() if hashlib.sha256((ROOT/p).read_bytes()).hexdigest() != h]
    summary = dict(csv_files_scanned=len(hashes), image_references=len(entries), unique_urls=len(by_url),
                   downloaded=sum(e['status']=='downloaded' for e in entries), failures=len(failures), changed_sources=changed)
    REPORT.write_text(json.dumps(dict(summary=summary, images=entries, failures=failures), indent=2)+'\n')
    print(json.dumps(summary, indent=2))
    if failures:
        print(json.dumps(failures, indent=2))
    assert not failures and not changed


if __name__ == '__main__':
    main()
