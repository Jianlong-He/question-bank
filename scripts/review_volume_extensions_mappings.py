"""Explicit review of equal-block volume, fractional lengths and volume changes."""
import argparse, fcntl, json
from pathlib import Path
from volume_extensions_lessons import SPECS, lessons
from number_sense_lessons import source as g
from video_reuse import append_upload_row, update_reuse_checklist
from build_video_correspondence import validate, read_inventory
from generate_video_batch import save_json, update_overview
from video_example_checks import require_analogous_examples

APPROVED=[(tuple(s['source_ref']),s['video_id']) for s in SPECS]
def gr(vid,grade,unit,w,qs):APPROVED.extend((g(grade,unit,w,q),vid) for q in qs)
for w,qs in [(1,[5,7]),('1HW',[5]),('1Rev',[5])]:gr('geometry-volume-count-blocks',5,11,w,qs)
for w,qs in [(1,[10]),('1HW',[4]),(3,[2]),('3Rev',[2])]:gr('geometry-volume-layers-of-blocks',5,11,w,qs)
gr('geometry-volume-compare-block-counts',5,11,'1Rev',[4])
gr('geometry-volume-compare-block-sizes',6,10,'2Rev',[1])
gr('geometry-volume-cube-fractional-side',6,10,'2HW',[2])
for w,qs in [(2,[4,6,8,10]),('2HW',[4]),('2Rev',[2,4,5])]:gr('geometry-volume-prism-fractional-dimensions',6,10,w,qs)
for w,qs in [(3,[2,4,9]),('3HW',[2,3]),('3Rev',[4])]:gr('geometry-volume-dimension-scale-factors',6,10,w,qs)
gr('geometry-volume-dimension-scale-factors',10,8,4,[10]);gr('geometry-volume-dimension-scale-factors',10,8,'4Rev',[2])
gr('geometry-volume-water-level-change',6,10,3,[5,10]);gr('geometry-volume-water-level-change',6,10,'3HW',[4]);gr('geometry-volume-water-level-change',6,10,'3Rev',[5])
gr('geometry-volume-container-minus-block',5,11,'3HW',[5])


def apply_review(doc):
    changes=[];reviewed=0
    for s in SPECS:
        vid=s['video_id'];title=s['topic']
        if vid not in doc['videos']:
            doc['videos'][vid]={'title':title,'question_type':title,'curriculum':{'kind':'shared','topic':'volume'},
              'production_status':'planned','target_duration_seconds':60,'duration_seconds':None,
              'example':None,'assets':{'mp4':None,'captions':None},'youtube':{'video_id':None,'visibility':None},
              'notes':'Distinct volume method identified from inspected worksheet questions and solutions.',
              'planning':{'basis':'rule','rule':vid,'review_status':'needs_review'}}
    for (file,qid),vid in sorted(set(APPROVED)):
        p=doc['worksheets'][file]['problems'][qid]
        assert len(p['video_links'])==1 and not p['requires_source_visual'],(file,qid)
        old=p['video_links'][0]['video_id'];assert vid in doc['videos'],vid
        if old!=vid:changes.append((file,qid,old,vid));p['video_links'][0]['video_id']=vid
        reviewed+=p['mapping_status']!='reviewed'
        p.update(mapping_method='manual',mapping_status='reviewed',mapping_rule='volume-extensions-review-1',
          notes='Inspected against the original analogous example: matching volume method and prerequisites, with different numerical data.')
    for s in SPECS:
        v=doc['videos'][s['video_id']];v['title']=s['topic'];v['question_type']=s['topic']
        refs=[p for w in doc['worksheets'].values() for p in w['problems'].values() if any(l['video_id']==s['video_id'] for l in p['video_links'])]
        if refs and all(p['mapping_status']=='reviewed' for p in refs):v['planning']['review_status']='reviewed'
    return changes,reviewed


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True);parser.add_argument('--check',action='store_true');args=parser.parse_args()
    with (Path(__file__).resolve().parents[1]/'videos/.production.lock').open('a+') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        path=args.output/'worksheet-video-correspondence.json';doc=json.loads(path.read_text())
        assert not any(v['production_status']=='in_progress' for v in doc['videos'].values())
        before={k:(v['youtube'].copy(),v['assets'].copy()) for k,v in doc['videos'].items()}
        changes,reviewed=apply_review(doc)
        assert before=={k:(doc['videos'][k]['youtube'],doc['videos'][k]['assets']) for k in before}
        validate(doc,read_inventory(),asset_root=args.output.parent)
        require_analogous_examples(doc,lessons(doc))
        content=(args.output/'youtube-upload-checklist.md').read_text()
        for vid in sorted(set(doc['videos'])-set(before)):content=append_upload_row(content,vid,doc['videos'][vid]['title'])
        content=update_reuse_checklist(content,doc)
        if not args.check:
            save_json(path,doc);(args.output/'youtube-upload-checklist.md').write_text(content)
            update_overview(args.output,doc,[s['video_id'] for s in SPECS])
        print(f'{len(changes)} corrected links; {reviewed} newly reviewed refs. Check only: {args.check}')
        for c in changes:print(*c,sep=' | ')

if __name__=='__main__':main()
