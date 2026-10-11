"""Explicit review of prism, cylinder, sphere and pyramid methods."""
import argparse,fcntl,json
from pathlib import Path
from solid_geometry_lessons import SPECS,lessons
from number_sense_lessons import source as g
from video_reuse import append_upload_row,update_reuse_checklist,merge_reviewed_duplicate
from build_video_correspondence import validate,read_inventory
from generate_video_batch import save_json,update_overview
from video_example_checks import require_analogous_examples

APPROVED=[(tuple(s['source_ref']),s['video_id']) for s in SPECS]
def gr(vid,grade,unit,w,qs):APPROVED.extend((g(grade,unit,w,q),vid) for q in qs)
gr('geometry-volume-cylinder',11,9,3,[9])
gr('geometry-volume-compare-cylinders',8,5,'8Rev',[5])
gr('geometry-volume-sphere',8,5,'8Rev',[3]);gr('geometry-volume-sphere',10,10,2,[5]);gr('geometry-volume-sphere',10,10,'2Rev',[2])
gr('geometry-volume-triangle',6,10,'3Rev',[2]);gr('geometry-volume-triangle',7,9,5,[9]);gr('geometry-volume-triangle',7,9,'5HW',[5])
gr('geometry-surface-area-cube',6,10,'4HW',[5]);gr('geometry-surface-area-cube',6,10,'4Rev',[4])
gr('geometry-surface-area-rectangular-prism',6,10,'4Rev',[3]);gr('geometry-surface-area-rectangular-prism',6,10,'5HW',[2]);gr('geometry-surface-area-rectangular-prism',6,10,'5Rev',[2,5])
gr('geometry-surface-area-pyramid',6,10,'5HW',[3]);gr('geometry-surface-area-pyramid',6,10,'5Rev',[4])
gr('geometry-surface-area-scale-factor',6,10,'5HW',[5])
gr('measurement-density-from-mass-volume',10,10,3,[7]);gr('measurement-density-from-mass-volume',10,10,'3Rev',[2])
# Further questions explicitly inspected in the coordinate-category review dump.
# Several category names are misleading; these questions need ordinary area/volume methods.
gr('geometry-area-unit-square-count-compare',3,10,1,[1])
gr('geometry-equal-area-different-sides',3,10,2,[5,7,10]);gr('geometry-equal-area-different-sides',3,10,'2HW',[2,5]);gr('geometry-equal-area-different-sides',3,10,'2Rev',[5])
gr('geometry-area-add-known-parts',3,10,5,[2,4,5])
gr('geometry-area-two-rectangles',3,10,5,[3]);gr('geometry-area-two-rectangles',3,10,'5Rev',[3])
gr('geometry-area-subtract-known-cutout',3,10,5,[8,9,10]);gr('geometry-area-subtract-known-cutout',3,10,'5HW',[5])
gr('geometry-volume-dimension-scale-factors',6,10,3,[3]);gr('geometry-volume-dimension-scale-factors',6,10,'3Rev',[1])
gr('geometry-parallelogram-height-from-area',6,8,1,[5,8]);gr('geometry-parallelogram-height-from-area',6,8,'1HW',[4]);gr('geometry-parallelogram-height-from-area',6,8,'1Rev',[4])
gr('geometry-volume-split-conservation',5,11,3,[4,6]);gr('geometry-volume-split-conservation',5,11,'3HW',[2]);gr('geometry-volume-split-conservation',5,11,'3Rev',[4])
TEXT_SUFFICIENT=[g(3,10,5,q) for q in [2,4,5]]
MERGES=[
 ('geometry-volume-cylinder-missing-dimension','geometry-volume-cylinder',[g(10,10,2,9),g(10,10,'2HW',4),g(10,10,'2Rev',5)]),
 ('geometry-volume-sphere-missing-dimension','geometry-volume-sphere',[g(10,10,2,10),g(10,10,'2HW',5)]),
 ('geometry-volume-pyramid-missing-dimension','geometry-volume-pyramid',[g(10,10,2,7),g(10,10,'2HW',2),g(10,10,'2Rev',4)]),
 ('geometry-volume-triangle-missing-dimension','geometry-volume-triangle',[g(10,10,2,6),g(10,10,'2Rev',3)]),
 ('geometry-area-pyramid','geometry-surface-area-pyramid',[g(6,10,5,5),g(6,10,'5Rev',3)]),
]
# This draft's four original refs were all moved by the explicit review above.
# Preserve its stable ID as a reuse record once both completed targets are verified.
EMPTY_DRAFT_REFS={
 'geometry-volume-general-coordinates':{
  g(5,11,3,6):'geometry-volume-split-conservation',
  g(5,11,'3HW',2):'geometry-volume-split-conservation',
  g(6,10,3,3):'geometry-volume-dimension-scale-factors',
  g(6,10,'3Rev',1):'geometry-volume-dimension-scale-factors',
 }
}
SOURCE_NOTES={g(6,10,3,6):'The source solution labels triangular base area as cm; this should be square centimetres. Its final volume is correct. The analogous lesson uses correct square/cubic units.'}
VISUAL_PENDING={ref:'The question refers to an absent net or box image. Dimensions occur only in the solution; inspect the original visual before certifying the mapping.'
 for ref in [g(6,10,4,7),g(6,10,4,10),g(6,10,5,3),g(6,10,5,10),g(6,10,5,6)]}


def apply_review(doc,merge=False):
    changes=[];reviewed=0
    for file,qid in TEXT_SUFFICIENT:
        doc['worksheets'][file]['problems'][qid]['requires_source_visual']=False
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
        p.update(mapping_method='manual',mapping_status='reviewed',mapping_rule='solid-geometry-review-1',
          notes='Inspected against the authored analogous example: matching measurement method and prerequisite steps; different numerical inputs.')
    for file,qid in TEXT_SUFFICIENT:
        doc['worksheets'][file]['problems'][qid]['notes'] += ' All component areas are explicitly stated in the question; no source diagram is needed to determine the additive method.'
    for (file,qid),note in SOURCE_NOTES.items():doc['worksheets'][file]['problems'][qid]['notes'] += ' ' + note
    for (file,qid),note in VISUAL_PENDING.items():
        problem=doc['worksheets'][file]['problems'][qid]
        assert problem['mapping_status']=='needs_review'
        problem.update(requires_source_visual=True,notes=note)
    if merge:
        for old,new,refs in MERGES:
            if doc['videos'][old].get('reuse_video_ids')==[new]:continue
            merge_reviewed_duplicate(doc,old,{ref:new for ref in refs})
        for old,ref_targets in EMPTY_DRAFT_REFS.items():
            draft=doc['videos'][old];targets=sorted(set(ref_targets.values()))
            if draft.get('reuse_video_ids')==targets:continue
            assert draft['production_status']=='planned' and not draft['youtube']['video_id']
            assert all(value is None for value in draft['assets'].values())
            assert not any(link['video_id']==old for w in doc['worksheets'].values() for problem in w['problems'].values() for link in problem['video_links'])
            for (file,qid),target in ref_targets.items():
                problem=doc['worksheets'][file]['problems'][qid]
                assert problem['mapping_status']=='reviewed' and not problem['requires_source_visual']
                assert len(problem['video_links'])==1 and problem['video_links'][0]['video_id']==target
                assert doc['videos'][target]['production_status']=='rendered' and not doc['videos'][target].get('reuse_video_ids')
            draft.update(production_status='retired',reuse_video_ids=targets,
                notes='All four original refs explicitly reviewed: G5U11W3 Q6 and G5U11W3HW Q2 use volume addition; G6U10W3 Q3 and G6U10W3Rev Q1 use dimension scale factors. Completed shared videos cover every original ref. Stable ID retained; no separate export needed.')
            draft['planning']['review_status']='reviewed'
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
