"""Explicit review of angle calculation or equation methods, with degree/radian separation."""
import argparse,fcntl,json
from pathlib import Path
from angle_equation_lessons import SPECS,lessons
from number_sense_lessons import source as g
from video_reuse import append_upload_row,update_reuse_checklist,merge_reviewed_duplicate
from build_video_correspondence import validate,read_inventory
from generate_video_batch import save_json,update_overview
from video_example_checks import require_analogous_examples

APPROVED=[(tuple(s['source_ref']),s['video_id']) for s in SPECS]
def gr(vid,grade,unit,w,qs):APPROVED.extend((g(grade,unit,w,q),vid) for q in qs)
gr('geometry-angle-relationships',7,9,'3HW',[3]);gr('geometry-angle-relationships',8,5,1,[2]);gr('geometry-angle-relationships',8,5,'1HW',[1]);gr('geometry-angle-relationships',8,5,2,[3]);gr('geometry-angle-relationships',8,5,'2HW',[3]);gr('geometry-angle-relationships',8,5,3,[3]);gr('geometry-angle-relationships',8,5,'3HW',[3]);gr('geometry-angle-relationships',9,17,'5Rev',[2])
gr('geometry-complementary-angle-equation',7,9,'1HW',[5]);gr('geometry-complementary-angle-equation',7,9,2,[7]);gr('geometry-complementary-angle-equation',7,9,'2HW',[5]);gr('geometry-complementary-angle-equation',7,9,4,[3]);gr('geometry-complementary-angle-equation',7,9,'4HW',[2])
gr('geometry-supplementary-angle-equation',7,9,'1HW',[4]);gr('geometry-supplementary-angle-equation',7,9,4,[4]);gr('geometry-supplementary-angle-equation',7,9,'4Rev',[2])
gr('geometry-vertical-angle-equation-one-side',7,9,'1Rev',[4]);gr('geometry-vertical-angle-equation-one-side',7,9,3,[1]);gr('geometry-vertical-angle-equation-one-side',7,9,'3HW',[1]);gr('geometry-vertical-angle-equation-one-side',8,5,1,[1]);gr('geometry-vertical-angle-equation-one-side',8,5,'1Rev',[1])
gr('geometry-vertical-angle-equation-both-sides',8,5,'2HW',[4]);gr('geometry-vertical-angle-equation-both-sides',8,5,'2Rev',[5]);gr('geometry-vertical-angle-equation-both-sides',8,5,3,[4]);gr('geometry-vertical-angle-equation-both-sides',8,5,'3HW',[4])
gr('geometry-complementary-angle-ratio',7,9,'1Rev',[5])
gr('geometry-supplementary-angle-multiple',7,9,'3Rev',[2]);gr('geometry-supplementary-angle-multiple',7,9,5,[2]);gr('geometry-supplementary-angle-multiple',7,9,'5HW',[1])
gr('geometry-supplementary-angle-difference',7,9,'2Rev',[3]);gr('geometry-supplementary-angle-difference',7,9,3,[2]);gr('geometry-supplementary-angle-difference',7,9,'3Rev',[1])
gr('geometry-complementary-angle-word-equation',7,9,'5Rev',[1])
gr('geometry-triangle-angle-equation',7,9,4,[7]);gr('geometry-triangle-angle-equation',7,9,'4HW',[3]);gr('geometry-triangle-angle-equation',7,9,5,[5]);gr('geometry-triangle-angle-equation',7,9,'5HW',[3]);gr('geometry-triangle-angle-equation',8,5,2,[5,7,9]);gr('geometry-triangle-angle-equation',8,5,'2Rev',[1,3,4]);gr('geometry-triangle-angle-equation',8,5,3,[5,7,9,10]);gr('geometry-triangle-angle-equation',8,5,'3Rev',[1,3,4])
gr('geometry-angle-measure-triangle-sum',7,9,'3HW',[4]);gr('geometry-angle-measure-triangle-sum',8,5,1,[4,5]);gr('geometry-angle-measure-triangle-sum',8,5,'1HW',[2,3]);gr('geometry-angle-measure-triangle-sum',8,5,3,[2]);gr('geometry-angle-measure-triangle-sum',8,5,'3HW',[2]);gr('geometry-angle-measure-triangle-sum',9,17,2,[1]);gr('geometry-angle-measure-triangle-sum',9,17,'2HW',[1]);gr('geometry-angle-measure-triangle-sum',9,17,'2Rev',[1]);gr('geometry-angle-measure-triangle-sum',9,17,3,[1,2]);gr('geometry-angle-measure-triangle-sum',9,17,'3HW',[1,2]);gr('geometry-angle-measure-triangle-sum',9,17,'3Rev',[1])
gr('geometry-isosceles-base-angles',7,9,'5Rev',[2]);gr('geometry-isosceles-base-angles',7,9,'3Rev',[3]);gr('geometry-isosceles-base-angles',7,9,4,[6]);gr('geometry-isosceles-base-angles',7,9,'4Rev',[4])
gr('geometry-equilateral-angle-equation',8,5,'3HW',[5]);gr('geometry-equilateral-angle-equation',9,17,3,[7]);gr('geometry-equilateral-angle-equation',9,17,'3HW',[5])
# Independently inspected additional questions covered by existing circle/right-triangle lessons.
gr('geometry-sector-area-radians',10,11,1,[3]);gr('geometry-regular-polygon-central-angle',10,11,4,[3]);gr('geometry-regular-polygon-central-angle',10,11,'4Rev',[1]);gr('geometry-triangle-30-60-90',10,9,2,[9]);gr('geometry-triangle-30-60-90',10,9,'2Rev',[3]);gr('geometry-pythagorean',8,5,4,[1]);gr('geometry-pythagorean',8,5,'4HW',[1])
MERGES=[]
SOURCE_NOTES={}
MISSING_VISUALS=[g(4,11,w,q) for w in [2,'2Rev'] for q in [1,2,3,4]]
MISSING_VISUALS += [g(4,11,4,10),g(4,11,'4HW',5)]
MISSING_VISUALS += [g(4,12,1,q) for q in [4,5,6]]
MISSING_VISUALS += [g(4,12,2,q) for q in range(1,11)]
MISSING_VISUALS += [g(4,12,3,q) for q in range(1,7)]
MISSING_VISUALS += [g(4,12,'3HW',1)] + [g(4,12,'3Rev',q) for q in range(1,6)]



def apply_review(doc,merge=False):
    changes=[];reviewed=0
    for s in SPECS:
        vid=s['video_id'];title=s['topic']
        if vid not in doc['videos']:
            doc['videos'][vid]={'title':title,'question_type':title,'curriculum':{'kind':'shared','topic':'measurement'},
             'production_status':'planned','target_duration_seconds':60,'duration_seconds':None,'example':None,
             'assets':{'mp4':None,'captions':None},'youtube':{'video_id':None,'visibility':None},
             'notes':'Distinct measurement method identified through explicit question review.',
             'planning':{'basis':'rule','rule':vid,'review_status':'needs_review'}}
    for (file,qid),vid in sorted(set(APPROVED)):
        p=doc['worksheets'][file]['problems'][qid]
        assert len(p['video_links'])==1 and not p['requires_source_visual'],(file,qid)
        old=p['video_links'][0]['video_id']
        if old!=vid:changes.append((file,qid,old,vid));p['video_links'][0]['video_id']=vid
        reviewed+=p['mapping_status']!='reviewed'
        p.update(mapping_method='manual',mapping_status='reviewed',mapping_rule='angle-equation-review-1',
          notes='Inspected against the authored analogous example: matching angle calculation or equation method and prerequisite steps; different numerical inputs.')
    for file,qid in MISSING_VISUALS:
        p=doc['worksheets'][file]['problems'][qid]
        assert p['mapping_status']=='needs_review'
        p['requires_source_visual']=True
        p['notes']='The question depends on an angle or triangle diagram absent from the worksheet CSV and available source files. Keep pending until the original visual can be inspected; do not infer it from the answer key.'
    for (file,qid),note in SOURCE_NOTES.items():doc['worksheets'][file]['problems'][qid]['notes'] += ' ' + note
    if merge:
        for old,new,refs in MERGES:
            if doc['videos'][old].get('reuse_video_ids')==[new]:continue
            merge_reviewed_duplicate(doc,old,{ref:new for ref in refs})
    for s in SPECS:
        v=doc['videos'][s['video_id']];v['title']=s['topic'];v['question_type']=s['topic']
        refs=[p for w in doc['worksheets'].values() for p in w['problems'].values() if any(l['video_id']==s['video_id'] for l in p['video_links'])]
        if refs and all(p['mapping_status']=='reviewed' for p in refs):v['planning']['review_status']='reviewed'
    return changes,reviewed


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True);parser.add_argument('--check',action='store_true');parser.add_argument('--merge',action='store_true');args=parser.parse_args()
    with (Path(__file__).resolve().parents[1]/'videos/.production.lock').open('a+') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        path=args.output/'worksheet-video-correspondence.json';doc=json.loads(path.read_text())
        assert not any(v['production_status']=='in_progress' for v in doc['videos'].values())
        before={k:(v['youtube'].copy(),v['assets'].copy()) for k,v in doc['videos'].items()}
        changes,reviewed=apply_review(doc,args.merge)
        assert before=={k:(doc['videos'][k]['youtube'],doc['videos'][k]['assets']) for k in before}
        validate(doc,read_inventory(),asset_root=args.output.parent);require_analogous_examples(doc,lessons(doc))
        # Recheck every completed lesson receiving additional worksheet links.
        for vid,v in doc['videos'].items():
            if v['production_status']=='rendered' and v.get('example'):
                require_analogous_examples(doc,[{'video_id':vid,'question':v['example']['question']}])
        content=(args.output/'youtube-upload-checklist.md').read_text()
        for vid in sorted(set(doc['videos'])-set(before)):content=append_upload_row(content,vid,doc['videos'][vid]['title'])
        lines=content.splitlines()
        for i,line in enumerate(lines):
            for s in SPECS:
                if f'| {s["video_id"]}.mp4 |' in line:
                    cells=line.split('|');cells[1]=' '+s['topic']+' ';lines[i]='|'.join(cells)
        if not args.check:
            save_json(path,doc);(args.output/'youtube-upload-checklist.md').write_text(update_reuse_checklist('\n'.join(lines)+'\n',doc));update_overview(args.output,doc,[s['video_id'] for s in SPECS])
        print(f'{len(changes)} corrected links; {reviewed} newly reviewed refs. Check only: {args.check}; merge requested: {args.merge}')

if __name__=='__main__':main()
