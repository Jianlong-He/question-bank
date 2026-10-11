"""Render the eight approved sample scripts to an explicit video directory.

Uses the existing offline Kokoro narration cache. No subtitles or network calls.
Updates the destination repository's correspondence file, never the source copy.
"""
import argparse
import copy
import html
import json
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw
import generate_sample_videos as video
import generate_enrichment_videos as enrichment
from build_video_correspondence import read_inventory, summary, validate
from video_example_checks import require_analogous_examples


def lessons_for(doc):
    lessons=[]
    for source in [*video.LESSONS,*enrichment.LESSONS]:
        lesson=copy.deepcopy(source)
        if 'grade' in lesson:
            vid=f'g{lesson["grade"]}-u{lesson["unit"]}-{lesson["slug"]}'
        else:
            candidates=[vid for vid in doc['videos']
                        if vid.startswith('enrichment-') and vid.endswith('-'+lesson['slug'])]
            assert len(candidates)==1,(lesson['slug'],candidates)
            vid=candidates[0]
        assert vid in doc['videos'],vid
        lesson['video_id']=vid
        for index in range(len(lesson['scenes'])):
            assert video.narration_path(lesson,index).is_file(),(vid,index)
        lessons.append(lesson)
    return lessons


def contact_sheet(lessons):
    sheet=Image.new('RGB',(3200,360*len(lessons)),video.BG)
    for row,lesson in enumerate(lessons):
        for scene in range(5):
            im=video.base(lesson,scene)
            video.DRAW[lesson.get('draw_key',lesson.get('grade'))](ImageDraw.Draw(im),scene,1)
            sheet.paste(im.resize((640,360)),(scene*640,row*360))
    return sheet


def save_json(path,value):
    pending=path.with_name(path.name+'.pending')
    pending.write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n')
    pending.replace(path)


def write_preview(output,entries):
    cards=[]
    for e in entries:
        src=html.escape(e['video'],quote=True)
        cards.append(f'<article><h2>{html.escape(e["title"])}</h2>'
                     f'<p>{e["duration_seconds"]:.1f} seconds</p>'
                     f'<video controls preload="metadata" poster="{src[:-4]}-poster.jpg" src="{src}"></video>'
                     f'<p><a href="{src}" download>{html.escape(e["video_id"])}.mp4</a></p></article>')
    (output/'index.html').write_text('''<!doctype html><html lang="en"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Worksheet sample videos</title><style>
body{font:18px system-ui;background:#f6f5f0;color:#172c3a;margin:0;padding:40px}
main{max-width:1200px;margin:auto}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(360px,1fr));gap:24px}
article{background:white;padding:24px;border-radius:16px}video{width:100%}a{color:#087f78;overflow-wrap:anywhere}
</style><main><h1>Worksheet video samples</h1><p>Local narration, animated mathematical working, and no subtitles.</p>
<p><a href="youtube-upload-checklist.md">YouTube upload list</a></p><section class="grid">'''+''.join(cards)+'</section></main></html>')


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--preview',type=Path)
    parser.add_argument('--only',action='append',default=[],help='Render only this video ID; repeat to select several.')
    args=parser.parse_args()
    output=args.output.resolve()
    assert output.is_dir(),'Choose an existing video folder.'
    manifest=output/'worksheet-video-correspondence.json'
    doc=json.loads(manifest.read_text())
    lessons=lessons_for(doc)
    if args.only:
        assert set(args.only)<={l['video_id'] for l in lessons},'Unknown sample video ID.'
        lessons=[l for l in lessons if l['video_id'] in args.only]
    require_analogous_examples(doc,lessons)
    enrichment.check_answers()
    assert 27+1==28 and 4*2==8 and (4//2,10//2)==(2,5) and abs(3-3)+2==2
    if args.preview:
        contact_sheet(lessons).save(args.preview,quality=92)
        print(f'Preview: {args.preview}',flush=True)
        return
    entries=[]
    for number,lesson in enumerate(lessons,1):
        print(f'[{number}/{len(lessons)}] {lesson["title"]}',flush=True)
        with tempfile.TemporaryDirectory(prefix='.render-',dir=output) as scratch:
            entry,_=video.render(lesson,Path(scratch),output_root=output)
        entries.append(entry)
        vid=lesson['video_id']
        # Reload before changing just this entry, preserving any concurrent upload edits.
        doc=json.loads(manifest.read_text())
        record=doc['videos'][vid]
        record['assets']={'mp4':str((output/entry['video']).relative_to(output.parent)),'captions':None}
        record['production_status']='rendered'
        record['duration_seconds']=entry['duration_seconds']
        record['example']={'question':lesson['question'],'answer':lesson['answer']}
        record['notes']=(record['notes'] or '')+' Regenerated with local narration and no subtitles; export filename matches the permanent video ID.'
        validate(doc,read_inventory(),asset_root=output.parent)
        save_json(manifest,doc)
        save_json(output/'sample-production-report.json',{'completed':len(entries),'batch_size':len(lessons),'videos':[{'video_id':e['video_id'],'file':e['video'],'duration_seconds':e['duration_seconds'],'subtitles':False} for e in entries]})
    contact_sheet(lessons_for(doc)).save(output/'sample-contact-sheet.jpg',quality=92)
    # Preserve unrelated catalog entries while replacing the eight regenerated samples.
    catalog_path=output/'catalog.json'
    old_catalog=json.loads(catalog_path.read_text()) if catalog_path.exists() else []
    slugs={e['slug'] for e in entries}
    catalog=[e for e in old_catalog if e.get('slug') not in slugs]+entries
    save_json(catalog_path,catalog)
    save_json(output/'correspondence-summary.json',summary(doc))
    write_preview(output,catalog)
    print(f'Completed {len(entries)} samples in {output}',flush=True)


if __name__=='__main__':
    main()
