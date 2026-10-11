"""Find early-ending video streams and re-render affected authored lessons locally."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import fcntl
import importlib
import json
from pathlib import Path
import subprocess
import sys
from generate_video_batch import save_json,update_overview
from build_video_correspondence import validate,read_inventory

from lesson_catalogs import CATALOGS,load_catalog


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True);parser.add_argument('--check',action='store_true');args=parser.parse_args()
    root=Path(__file__).resolve().parents[1];manifest=args.output/'worksheet-video-correspondence.json'
    with (root/'videos/.production.lock').open('a+') as lock:
        fcntl.flock(lock.fileno(),fcntl.LOCK_EX|fcntl.LOCK_NB)
        doc=json.loads(manifest.read_text())
        assert not any(v['production_status']=='in_progress' for v in doc['videos'].values())
        records=[(vid,v) for vid,v in doc['videos'].items() if v['assets']['mp4']]
        def check(item):
            vid,v=item;p=args.output.parent/v['assets']['mp4']
            d=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(p)]))
            duration=float(d['format']['duration']);video=next(s for s in d['streams'] if s['codec_type']=='video')
            gap=duration-float(video['duration'])
            return (vid,round(gap,3)) if abs(gap)>.1 else None
        with ThreadPoolExecutor(max_workers=4) as pool:bad=[x for x in pool.map(check,records) if x]
        affected={vid for vid,gap in bad};batches={};known=set()
        for catalog,module in CATALOGS.items():
            lessons=load_catalog(catalog,doc)
            vids=[l['video_id'] for l in lessons if l['video_id'] in affected]
            if vids:batches[catalog]=vids;known.update(vids)
        assert known==affected,('Missing authoring sources',affected-known)
        print(json.dumps({'affected':len(bad),'largest_gap_seconds':max([gap for _,gap in bad],default=0),
                          'catalog_counts':{k:len(v) for k,v in batches.items()}},indent=2),flush=True)
        if args.check:return
        before={k:v['youtube'].copy() for k,v in doc['videos'].items()}
        for vid,gap in bad:
            doc['videos'][vid]['production_status']='needs_revision'
            doc['videos'][vid]['notes']=f'Video stream ended {gap}s before audio; re-render the complete final still with explicit FPS filtering.'
        assert before=={k:v['youtube'] for k,v in doc['videos'].items()}
        validate(doc,read_inventory(),asset_root=args.output.parent)
        save_json(manifest,doc);update_overview(args.output,doc,sorted(affected))
    for catalog,ids in batches.items():
        print(f'Repairing {catalog}: {len(ids)} videos',flush=True)
        command=[sys.executable,str(root/'scripts/generate_video_batch.py'),'--output',str(args.output),'--catalog',catalog]
        for vid in ids:command+=['--only',vid]
        subprocess.run(command,check=True)
    print('All affected video streams re-rendered. Run the complete library audit.',flush=True)


if __name__=='__main__':main()
