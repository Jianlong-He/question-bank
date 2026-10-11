#!/usr/bin/env python3
"""Render and verify the agreed Grade 1–12 unit-test image list.

Uses the bundled Python with Pillow/NumPy. Source question CSVs remain read-only.
"""
from pathlib import Path
import csv
import hashlib
import json
import math
from PIL import Image, ImageDraw
from unit_test_visual_specs import SPECS
from unit_test_visuals_lower import render_lower
from unit_test_visuals_upper import render_upper
from unit_test_visuals_common import font, INK
from unit_test_visuals_next import next_specs, render_next

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'images/unit-test-images'
REPORT=ROOT/'images/generated-unit-test-images.json'
LOWER_SHARED={'vertical','trapezoid'}


def main():
    entries=[];sources={};seen=set()
    previous={e['output_file']:e['sha256'] for e in json.loads(REPORT.read_text())['images']} if REPORT.exists() else {}
    for s in sorted(SPECS+next_specs(),key=lambda s:(s['grade'],s['unit'],s['qid'])):
        g,u,q=s['grade'],s['unit'],s['qid'];key=(g,u,q)
        assert key not in seen,key
        seen.add(key)
        source=ROOT/f'unit-tests/Grade {g}/G{g}Unit{u}.csv'
        sources[str(source.relative_to(ROOT))]=hashlib.sha256(source.read_bytes()).hexdigest()
        rows=list(csv.DictReader(source.open(encoding='utf-8-sig',newline='')))
        row=next(r for r in rows if r['Question ID'].strip()==str(q))
        if 'expected_question' in s:
            assert row['Question Choices']==s['expected_question'],key
        has_original=any(v and v.strip() for k,v in row.items() if k and 'image' in k.lower())
        assert not has_original or (key==(3,4,10) and s.get('image_index')==2 and '21 circles' in row['Question Choices']),key
        im=(render_next if s['kind']=='next' else render_lower if g<=6 or s['kind'] in LOWER_SHARED else render_upper)(s)
        target=OUT/f'Grade {g}'/source.stem/f'UT-G{g}U{u}Q{q}I{s.get("image_index",1)}.png'
        target.parent.mkdir(parents=True,exist_ok=True)
        if target.exists():
            with Image.open(target) as old:identical=im.size==old.size and im.convert('RGB').tobytes()==old.convert('RGB').tobytes()
            if not identical:
                assert previous.get(str(target.relative_to(ROOT)))==hashlib.sha256(target.read_bytes()).hexdigest(),target
                im.save(target)
        else:im.save(target)
        with Image.open(target) as check:check.verify()
        entries.append({**s,'source_csv':str(source.relative_to(ROOT)),'question_id':str(q),
                        'question':row['Question Choices'],'output_file':str(target.relative_to(ROOT)),
                        'dimensions':list(im.size),'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
                        'method':'Deterministic mathematical drawing with Pillow/NumPy'})
    assert all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in sources.items())
    summary=dict(images_created=len(entries),unit_tests=len(sources),csv_contents_changed=False,
                 by_grade={str(g):sum(e['grade']==g for e in entries) for g in range(1,13)})
    REPORT.write_text(json.dumps(dict(summary=summary,images=entries,source_sha256=sources),indent=2)+'\n')
    preview=ROOT/'images/unit-test-previews';preview.mkdir(exist_ok=True)
    additional=[e for e in entries if e.get('batch')=='additional-68']
    for page,start in enumerate(range(0,len(additional),8),1):
        group=additional[start:start+8];sheet=Image.new('RGB',(1280,math.ceil(len(group)/2)*540),'#e8edf1');d=ImageDraw.Draw(sheet)
        for i,e in enumerate(group):
            with Image.open(ROOT/e['output_file']) as im:
                im.thumbnail((624,480));x=(i%2)*640+(640-im.width)//2;y=(i//2)*540
                sheet.paste(im,(x,y))
            d.text(((i%2)*640+14,(i//2)*540+496),Path(e['output_file']).stem,font=font(23),fill=INK)
        sheet.save(preview/f'additional-{page:02d}.jpg',quality=95)
    for page,start in enumerate(range(0,len(entries),8),1):
        group=entries[start:start+8];sheet=Image.new('RGB',(1280,math.ceil(len(group)/2)*540),'#e8edf1');d=ImageDraw.Draw(sheet)
        for i,e in enumerate(group):
            with Image.open(ROOT/e['output_file']) as im:
                im.thumbnail((624,480));x=(i%2)*640+(640-im.width)//2;y=(i//2)*540
                sheet.paste(im,(x,y))
            d.text(((i%2)*640+14,(i//2)*540+496),Path(e['output_file']).stem,font=font(23),fill=INK)
        sheet.save(preview/f'generated-{page:02d}.jpg',quality=95)
    # Download previews are kept separate from the newly drawn images.
    downloaded=json.loads((ROOT/'images/unit-test-image-downloads.json').read_text())['images']
    for page,start in enumerate(range(0,len(downloaded),12),1):
        group=downloaded[start:start+12];sheet=Image.new('RGB',(1440,math.ceil(len(group)/3)*420),'#e8edf1');d=ImageDraw.Draw(sheet)
        for i,e in enumerate(group):
            with Image.open(ROOT/e['output_file']) as im:
                im=im.convert('RGB');im.thumbnail((464,360));x=(i%3)*480+(480-im.width)//2;y=(i//3)*420
                sheet.paste(im,(x,y))
            d.text(((i%3)*480+10,(i//3)*420+374),Path(e['output_file']).stem,font=font(21),fill=INK)
        sheet.save(preview/f'downloaded-{page:02d}.jpg',quality=94)
    print(json.dumps(summary,indent=2))


if __name__=='__main__':main()
