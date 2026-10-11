"""Read-only audit of the canonical manifest, checklist, examples and MP4 files.

Each new render is fully decoded by the renderer. This inexpensive resumable
library audit checks stream metadata and references without re-encoding anything.
"""
import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import re
import subprocess
from build_video_correspondence import read_inventory, validate
from video_example_checks import require_analogous_examples


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True)
    from lesson_catalogs import CATALOGS
    parser.add_argument('--catalog',action='append',choices=sorted(CATALOGS),help='Limit expensive example/media checks to these catalogs; global inventory/checklist checks still run.')
    args=parser.parse_args()
    root=args.output.resolve();doc=json.loads((root/'worksheet-video-correspondence.json').read_text())
    validate(doc,read_inventory(),asset_root=root.parent)
    from lesson_catalogs import CATALOGS,load_catalog
    names=args.catalog or list(CATALOGS)
    selected=set() if args.catalog else None
    for name in names:
        batch=load_catalog(name,doc)
        require_analogous_examples(doc,batch)
        if selected is not None:selected.update(l['video_id'] for l in batch)
    all_records=[(k,v) for k,v in doc['videos'].items() if v['production_status']=='rendered']
    records=[(k,v) for k,v in all_records if selected is None or k in selected]
    def check(item):
        vid,v=item;path=root.parent/v['assets']['mp4']
        assert path.name==vid+'.mp4' and v['assets']['captions'] is None,vid
        data=json.loads(subprocess.check_output(['/opt/homebrew/bin/ffprobe','-v','error','-show_streams','-show_format','-of','json',str(path)]))
        vs=[s for s in data['streams'] if s['codec_type']=='video'];aa=[s for s in data['streams'] if s['codec_type']=='audio']
        assert len(vs)==1 and vs[0]['codec_name']=='h264' and (vs[0]['width'],vs[0]['height'])==(1920,1080),vid
        assert len(aa)==1 and aa[0]['codec_name']=='aac',vid
        assert not any(s['codec_type']=='subtitle' for s in data['streams']),vid
        duration=float(data['format']['duration'])
        assert 0<duration<60 and abs(duration-v['duration_seconds'])<.2,(vid,duration,v['duration_seconds'])
        assert abs(float(vs[0]['duration'])-duration)<.1,(vid,'Video stream ends early',vs[0]['duration'],duration)
        assert abs(float(aa[0]['duration'])-duration)<.1,(vid,'Audio stream duration mismatch')
        assert not any(path.with_suffix(suffix).exists() for suffix in ['.jpg','.json','.srt']),vid
        return path.stat().st_size,duration
    with ThreadPoolExecutor(max_workers=4) as pool:results=list(pool.map(check,records))
    files={p for p in root.rglob('*.mp4') if not p.name.startswith('._')}
    assert files=={root.parent/v['assets']['mp4'] for vid,v in all_records},'Unregistered or missing MP4s; finish any revision first.'
    rows=re.findall(r'\| ([a-z0-9-]+)\.mp4 \|',(root/'youtube-upload-checklist.md').read_text())
    active={k for k,v in doc['videos'].items() if v['production_status']!='retired'}
    assert len(rows)==len(set(rows))==len(active) and set(rows)==active
    print(json.dumps({
        'rendered':len(all_records),'media_checked':len(records),'audit_scope':args.catalog or 'full','video_records':len(doc['videos']),'required_videos':len(active),
        'status_counts':dict(Counter(v['production_status'] for v in doc['videos'].values())),
        'checked_media_bytes':sum(r[0] for r in results),'checked_media_minutes':round(sum(r[1] for r in results)/60,2),
        'mapping_status':dict(Counter(p['mapping_status'] for w in doc['worksheets'].values() for p in w['problems'].values())),
        'checklist_rows':len(rows)},indent=2))


if __name__=='__main__':main()
