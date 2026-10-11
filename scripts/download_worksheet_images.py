#!/usr/bin/env python3
"""Import legacy image URL columns; current `image` cells contain local paths.

Preserve the existing URL manifest when there are no URL columns to import.
"""
import argparse
import concurrent.futures
import csv
import hashlib
import json
from pathlib import Path
import re
import subprocess
import tempfile
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'worksheets'
DEST = ROOT / 'images' / 'worksheet-images'
REPORT = ROOT / 'images' / 'worksheet-image-downloads.json'


def enrichment_units():
    result = {}

    def visit(nodes):
        for node in nodes:
            courses = {'Number Theory 1': 'NT1', 'Combinatorics and Probability 1': 'CP1'}
            if node.get('title') in courses:
                for number, unit in enumerate(node['submenu'], 1):
                    def collect(item):
                        url = item.get('url', '')
                        if 'file=worksheets/enrichment/' in url:
                            source = url.split('file=', 1)[1].split('&', 1)[0]
                            result[str(Path(source).parent)] = (courses[node['title']], number)
                        for child in item.get('submenu', []):
                            collect(child)
                    collect(unit)
            visit(node.get('submenu', []))

    visit(json.loads((ROOT / 'data/curriculum.json').read_text()))
    return result


def inventory():
    units = enrichment_units()
    entries = []
    hashes = {}
    targets = set()
    for path in sorted(SOURCE.rglob('*.csv')):
        relative = path.relative_to(ROOT)
        hashes[str(relative)] = hashlib.sha256(path.read_bytes()).hexdigest()
        with path.open(encoding='utf-8-sig', newline='') as handle:
            reader = csv.DictReader(handle)
            columns = [name for name in reader.fieldnames or []
                       if re.sub(r'[^a-z]', '', name.lower()) in
                       {'imageurl', 'imagesurl', 'imageurls', 'imagesurls'}]
            for row in reader:
                urls = []
                for column in columns:
                    value = (row.get(column) or '').strip()
                    if not value:
                        continue
                    found = re.findall(r'https?://[^\s|,;<>"\[\]]+', value)
                    if not found:
                        raise ValueError(f'Unrecognized image cell: {relative}: {value}')
                    urls.extend(found)
                if not urls:
                    continue
                question = row['Question ID'].strip()
                if not re.fullmatch(r'\d+', question):
                    raise ValueError(f'Invalid question ID: {relative}: {question}')
                if 'enrichment' in path.parts:
                    course, unit = units[str(relative.parent)]
                    match = re.fullmatch(rf'E-{course}U{unit}W\d+(?:-\d+)?[A-Za-z]*', path.stem)
                    if not match:
                        raise ValueError(f'Unknown worksheet name: {relative}')
                    code = path.stem
                else:
                    if not re.fullmatch(r'G\d+U\d+W\d+(?:_?[A-Za-z]+)?', path.stem):
                        raise ValueError(f'Unknown worksheet name: {relative}')
                    code = path.stem.replace('_Revision', 'Rev').replace('_HW', 'HW')
                for index, url in enumerate(urls, 1):
                    if urlsplit(url).hostname != 'i.ibb.co':
                        raise ValueError(f'Unexpected image host: {url}')
                    target = DEST / path.relative_to(SOURCE).parent / path.stem / f'WS-{code}Q{question}I{index}'
                    if str(target) in targets:
                        raise ValueError(f'Duplicate output name: {target}')
                    targets.add(str(target))
                    entries.append(dict(source_csv=str(relative), question_id=question,
                                        image_index=index, url=url,
                                        output_stem=str(target.relative_to(ROOT))))
    return entries, hashes


def image_extension(data):
    if data.startswith(b'\x89PNG\r\n\x1a\n'):
        return '.png'
    if data.startswith(b'\xff\xd8\xff'):
        return '.jpg'
    if data.startswith((b'GIF87a', b'GIF89a')):
        return '.gif'
    if data.startswith(b'RIFF') and data[8:12] == b'WEBP':
        return '.webp'
    raise ValueError('Response is not a recognized image')


def fetch(url):
    with tempfile.TemporaryDirectory(prefix='worksheet-image-') as folder:
        path = Path(folder) / 'download'
        command = ['curl', '--location', '--fail', '--silent', '--show-error',
                   '--proto', '=https', '--proto-redir', '=https',
                   '--connect-timeout', '15', '--max-time', '60',
                   '--retry', '2', '--retry-delay', '1', '--output', str(path), url]
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode:
            raise RuntimeError(result.stderr.strip())
        data = path.read_bytes()
        return data, image_extension(data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--download', action='store_true')
    args = parser.parse_args()
    entries, hashes = inventory()
    if not entries:
        print('No legacy image URLs found; preserving the existing download manifest.')
        return
    urls = sorted({entry['url'] for entry in entries})
    print(f'{len(hashes)} CSVs scanned; {len(entries)} image references; '
          f'{len(urls)} distinct URLs; no naming collisions.', flush=True)
    if not args.download:
        print(json.dumps(entries[:2] + entries[-1:], indent=2))
        return
    # Keep the worksheet directory structure, including units without images.
    for path in SOURCE.rglob('*'):
        if path.is_dir():
            (DEST / path.relative_to(SOURCE)).mkdir(parents=True, exist_ok=True)
    by_url = {}
    for entry in entries:
        by_url.setdefault(entry['url'], []).append(entry)
    completed = 0
    failures = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        futures = {pool.submit(fetch, url): url for url in urls}
        for future in concurrent.futures.as_completed(futures):
            url = futures[future]
            try:
                data, extension = future.result()
                digest = hashlib.sha256(data).hexdigest()
                for entry in by_url[url]:
                    target = ROOT / (entry['output_stem'] + extension)
                    target.parent.mkdir(parents=True, exist_ok=True)
                    if target.exists() and target.read_bytes() != data:
                        raise ValueError(f'Refusing to overwrite different content: {target}')
                    if not target.exists():
                        with target.open('xb') as handle:
                            handle.write(data)
                    entry.update(output_file=str(target.relative_to(ROOT)),
                                 status='downloaded', bytes=len(data), sha256=digest)
            except Exception as error:
                failures.append(dict(url=url, error=str(error)))
                for entry in by_url[url]:
                    if 'status' not in entry:
                        entry.update(status='failed', error=str(error))
                print(f'FAILED {url}: {error}', flush=True)
            completed += 1
            if completed % 25 == 0 or completed == len(urls):
                print(f'{completed}/{len(urls)} URLs processed; {len(failures)} failures', flush=True)
    changed_sources = [name for name, digest in hashes.items()
                       if hashlib.sha256((ROOT / name).read_bytes()).hexdigest() != digest]
    summary = dict(csv_files_scanned=len(hashes), image_references=len(entries),
                   unique_urls=len(urls), downloaded=sum(e['status'] == 'downloaded' for e in entries),
                   failed=sum(e['status'] == 'failed' for e in entries),
                   changed_sources=changed_sources)
    REPORT.write_text(json.dumps(dict(summary=summary, images=entries, failures=failures), indent=2) + '\n')
    print(json.dumps(summary, indent=2), flush=True)
    if failures or changed_sources:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
