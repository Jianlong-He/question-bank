"""Produce authored lessons on the selected drive, with MP4-only lesson exports.

Default execution overlaps local narration with rendering. Repeat --catalog to
combine batches; --serial disables overlap; --plan previews pending work.
--speech prepares audio only; --preview FILE creates a contact sheet. Production updates
the master correspondence JSON, and resumes without redoing completed exports.
"""
import argparse
import asyncio
import fcntl
import html
import json
import os
import tempfile
import time
from contextlib import closing
from video_pipeline import ready_lessons,pending_lessons
from pathlib import Path

from PIL import Image, ImageDraw
import generate_sample_videos as video
from production_lessons import check_answers
from lesson_catalogs import CATALOGS,load_catalogs
from video_example_checks import require_analogous_examples
from build_video_correspondence import read_inventory, summary, validate


def save_json(path,data):
    pending=path.with_name(path.name+'.pending')
    pending.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
    pending.replace(path)


def update_overview(output,doc,batch_ids):
    report=summary(doc)
    save_json(output/'correspondence-summary.json',report)
    done=[vid for vid in batch_ids if doc['videos'][vid]['production_status']=='rendered']
    lines=['VIDEO PRODUCTION PROGRESS','',f'Current batch: {len(done)} / {len(batch_ids)} rendered.',
           f'Library: {report["production_status_counts"].get("rendered",0)} / {report["required_video_count"]} required videos rendered; {report["video_count"]} retained IDs.',
           f'Voice: {video.VOICE}; speed {video.VOICE_RATE}. Local generation only.',
           'Exports: MP4; no subtitles, per-video JSON, or JPG files.','']
    for vid in batch_ids:lines.append(f'{doc["videos"][vid]["production_status"]}: {vid}.mp4')
    (output/'production-progress.txt').write_text('\n'.join(lines)+'\n')
    cards=[]
    for vid,v in doc['videos'].items():
        if v['production_status']!='rendered' or not v['assets']['mp4']:continue
        src=html.escape(str((output.parent/v['assets']['mp4']).relative_to(output)),quote=True)
        cards.append(f'<article><h2>{html.escape(v["title"])}</h2><p>{v["duration_seconds"]:.1f} seconds</p>'
                     f'<video controls preload="metadata" src="{src}"></video>'
                     f'<p><a href="{src}" download>{html.escape(vid)}.mp4</a></p></article>')
    (output/'index.html').write_text('''<!doctype html><html lang="en"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Worksheet video library</title>
<style>body{font:18px system-ui;background:#f6f5f0;color:#172c3a;margin:0;padding:40px}main{max-width:1200px;margin:auto}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(350px,1fr));gap:24px}article{background:white;padding:24px;border-radius:16px}
video{width:100%}a{color:#087f78;overflow-wrap:anywhere}</style><main><h1>Worksheet video library</h1>
<p>Similar worked examples with local narration. No subtitles.</p><p><a href="youtube-upload-checklist.md">Enter YouTube IDs</a>
 · <a href="production-progress.txt">Production progress</a></p><section class="grid">'''+''.join(cards)+'</section></main></html>')


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--speech',action='store_true',help='Prepare narration only.')
    parser.add_argument('--serial',action='store_true',help='Prepare all audio before rendering; useful for benchmarks.')
    parser.add_argument('--plan',action='store_true',help='Read-only list of pending work; no synthesis or exports.')
    parser.add_argument('--limit',type=int,default=50,help='Maximum pending lessons per production run.')
    parser.add_argument('--preview',type=Path)
    parser.add_argument('--only',action='append',default=[])
    parser.add_argument('--catalog',choices=sorted(CATALOGS),action='append',help='Repeat to combine catalogs in one run.')
    args=parser.parse_args()
    output=args.output.resolve()
    assert output.is_dir(),'Select an existing videos directory.'
    manifest=output/'worksheet-video-correspondence.json'
    doc=json.loads(manifest.read_text())
    batch=load_catalogs(args.catalog or ['foundation'],doc)
    if args.only:
        assert set(args.only)<={l['video_id'] for l in batch},'Unknown authored video ID.'
        batch=[l for l in batch if l['video_id'] in args.only]
    check_answers()
    assert all(l['video_id'] in doc['videos'] for l in batch)
    require_analogous_examples(doc,batch)
    if args.preview:
        sheet=Image.new('RGB',(3200,len(batch)*360),video.BG)
        for row,lesson in enumerate(batch):
            for scene in range(5):
                frame=video.base(lesson,scene)
                video.DRAW[lesson.get('draw_key',lesson.get('grade'))](ImageDraw.Draw(frame),scene,1)
                sheet.paste(frame.resize((640,360)),(scene*640,row*360))
        sheet.save(args.preview,quality=94)
        print(f'Preview: {args.preview}',flush=True)
        return
    inventory=read_inventory()
    validate(doc,inventory,asset_root=output.parent)
    ids=[l['video_id'] for l in batch]
    upload_list=(output/'youtube-upload-checklist.md').read_text()
    assert all(vid+'.mp4' in upload_list for vid in ids)
    assert args.limit>0,'Limit must be positive.'
    selected_count=len(batch)
    pending=pending_lessons(batch,doc,output.parent)
    batch=pending[:args.limit]
    ids=[l['video_id'] for l in batch]
    if args.plan:
        print(json.dumps({'pending_in_catalogs':len(pending),'selected':ids,
                          'skipped_completed':selected_count-len(pending)},indent=2))
        return
    if not batch:
        print('No pending videos. Completed exports left untouched.',flush=True)
        return
    # Only explicit worksheet review authorizes generation, never an automatic cluster.
    for lesson in batch:
        for qid in lesson['ids']:
            assert doc['worksheets'][lesson['source']]['problems'][qid]['mapping_status']=='reviewed',('Review source answer, solution and mapping first',lesson['video_id'],qid)
    from synthesize_video_narration import synthesize
    speech_metrics=[];render_metrics=[];started=time.perf_counter();completed=[]
    def prepare(items,publish,stop):
        synthesize(items,on_ready=publish,stop_event=stop,metrics=speech_metrics)
    if args.speech:
        synthesize(batch,metrics=speech_metrics)
        print(json.dumps({'speech':speech_metrics,'wall_seconds':round(time.perf_counter()-started,3)},indent=2))
        return
    success=False
    try:
        with closing(ready_lessons(batch,prepare,overlap=not args.serial)) as prepared:
            for number,lesson in enumerate(prepared,1):
                vid=lesson['video_id']
                doc=json.loads(manifest.read_text())
                record=doc['videos'][vid]
                print(f'[{number}/{len(batch)}] {lesson["title"]}',flush=True)
                record['production_status']='in_progress'
                save_json(manifest,doc)
                render_started=time.perf_counter()
                try:
                    with tempfile.TemporaryDirectory(prefix='.render-',dir=output) as scratch:
                        entry,_=video.render(lesson,Path(scratch),output_root=output,write_companions=False)
                except BaseException:
                    doc=json.loads(manifest.read_text())
                    doc['videos'][vid]['production_status']='needs_revision' if doc['videos'][vid]['assets']['mp4'] else 'planned'
                    save_json(manifest,doc)
                    raise
                doc=json.loads(manifest.read_text())
                record=doc['videos'][vid]
                record['production_status']='rendered'
                record['assets']={'mp4':str((output/entry['video']).relative_to(output.parent)),'captions':None}
                record['duration_seconds']=entry['duration_seconds']
                record['example']={'question':lesson['question'],'answer':lesson['answer']}
                record['notes']='Rendered with local Kokoro af_heart narration at 0.95 speed, no subtitles, and an analogous worked example. Worksheet mappings marked needs_review still require a suitability check.'
                # Renderer already fully decoded this MP4 and checked its audio/video timing.
                save_json(manifest,doc)
                completed.append(vid)
                render_metrics.append({'video_id':vid,'render_seconds':round(time.perf_counter()-render_started,3)})
                if number%10==0:update_overview(output,doc,ids)
        validate(doc,inventory,asset_root=output.parent)
        success=True
    finally:
        doc=json.loads(manifest.read_text())
        update_overview(output,doc,ids)
        save_json(output/'production-last-run.json',{
            'mode':'serial' if args.serial else 'overlapped','success':success,
            'catalogs':args.catalog or ['foundation'],'selected':ids,'completed':completed,
            'wall_seconds':round(time.perf_counter()-started,3),
            'speech':speech_metrics,'render':render_metrics})
    print(f'Batch complete: {len(completed)} videos; {len(pending)-len(batch)} still pending in these catalogs. Output: {output}',flush=True)


if __name__=='__main__':
    # Heartbeat runs may resume while a previous export is still active.
    # A kernel lock is released automatically even if the process is interrupted.
    lock_path=Path(__file__).resolve().parents[1]/'videos'/'.production.lock'
    with lock_path.open('a+') as lock:
        try:
            fcntl.flock(lock.fileno(),fcntl.LOCK_EX|fcntl.LOCK_NB)
        except BlockingIOError:
            raise SystemExit('Another video preparation/export is active. Resume after it completes.')
        lock.seek(0);lock.truncate();lock.write(str(os.getpid()));lock.flush()
        main()
