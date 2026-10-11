"""Explicitly reviewed rotation mappings and unresolved source issues."""
import argparse,fcntl,json
from pathlib import Path
from rotation_lessons import SPECS,lessons
from number_sense_lessons import source as g
from video_reuse import append_upload_row,update_reuse_checklist,merge_reviewed_duplicate
from build_video_correspondence import validate,read_inventory
from generate_video_batch import save_json,update_overview
from video_example_checks import require_analogous_examples

APPROVED=[]
# Each explicit row was checked against its full question, answer and solution.
ASSIGNMENTS = """quarter-ccw 8 6 1 3
quarter-ccw 8 6 1Rev 1
quarter-ccw 8 6 2 7,8
quarter-ccw 8 6 2Rev 3,4
half-turn 8 6 1 9
half-turn 8 6 1HW 5
half-turn 8 6 3 3,8
half-turn 8 6 3HW 3
half-turn 8 6 3Rev 3
quarter-cw 8 6 3 7
quarter-cw 8 6 3Rev 2
quarter-cw 8 6 5 1,8
quarter-cw 8 6 5Rev 1,3
half-turn 8 6 5 4
half-turn 8 6 5HW 3
half-turn 8 6 6 7
half-turn 8 6 6HW 5
half-turn 8 6 8Rev 1
 equivalent-directions 8 6 8 3
 equivalent-directions 8 6 8HW 3
center-angle 9 15 1 2,8
center-angle 9 15 1HW 2
center-angle 9 15 3 8
quarter-ccw 9 15 3 1
quarter-ccw 9 15 3HW 1
quarter-ccw 9 15 3Rev 1
quarter-cw 9 15 3 2
quarter-cw 9 15 3HW 2
quarter-cw 9 15 3Rev 2
half-turn 9 15 3 3
half-turn 9 15 3HW 3
half-turn 9 15 3Rev 3
regular-polygon 9 16 3 4
regular-polygon 9 16 3HW 4,5
regular-polygon 9 16 3Rev 4
parallelogram 9 16 3 5
odd-function 11 6 2 7
"""
for row in ASSIGNMENTS.splitlines():
    method,grade,unit,w,qs=row.split()
    APPROVED.extend((g(int(grade),int(unit),w,q),'geometry-rotation-'+method) for q in qs.split(','))
for grade,unit,w,q in [(8,6,6,2),(8,6,'6HW',2),(9,16,1,10),(9,16,'1Rev',1)]:
    APPROVED.append((g(grade,unit,w,q),'geometry-reflection-rigid-properties'))
assert len(APPROVED)==len(set(ref for ref,vid in APPROVED))
MERGES=[]
SOURCE_NOTES={}
for w,qs in [(4,[3,5,8,10]),('4HW',[3]),('4Rev',[2,3,5]),(6,[1]),('6HW',[1]),(7,[7]),('7HW',[5])]:
    for q in qs:SOURCE_NOTES[g(8,6,w,q)]='Source scope issue: the coordinate rotation rule in the key assumes the origin as center, but the question omits that center. Leave pending until that assumption is documented or made explicit; no source edits.'
for unit,w,q in [(15,3,10),(16,2,8)]:
    SOURCE_NOTES[g(9,unit,w,q)]='Source scope issue: rotation angles add as in the key only when both rotations share the same center. The question does not state this condition. Left pending; no source edits.'
for w,q in [(2,3),('2Rev',1)]:
    SOURCE_NOTES[g(8,6,w,q)]='Source wording issue: a half-turn preserves orientation but reverses both horizontal and vertical coordinates relative to the center. The phrase does not flip left/right can describe a different operation. Clarify turn versus mirror image; leave pending.'
REVIEW_NOTES={g(9,15,1,8):'The center is the unique fixed point of a nonidentity plane rotation. The full-turn identity is an exception; the new example is a nonidentity turn.'}

for w,q in [('1',6),('1HW',1)]:
    SOURCE_NOTES[g(5,11,w,q)]='Source scope issue: a larger visible cube count after rotation does not establish that every cube has been counted. The unit-cube volume is also implicit. State that the final count includes all cubes and each is one cubic unit. Left pending; source unchanged.'


def apply_review(doc,merge=False):
    changes=[];reviewed=0
    for s in SPECS:
        vid=s['video_id'];title=s['topic']
        if vid not in doc['videos']:
            doc['videos'][vid]={'title':title,'question_type':title,'curriculum':{'kind':'shared','topic':'geometry'},
             'production_status':'planned','target_duration_seconds':60,'duration_seconds':None,'example':None,
             'assets':{'mp4':None,'captions':None},'youtube':{'video_id':None,'visibility':None},
             'notes':'Distinct rotation method identified through explicit question review.',
             'planning':{'basis':'rule','rule':vid,'review_status':'needs_review'}}
    for (file,qid),vid in sorted(set(APPROVED)):
        p=doc['worksheets'][file]['problems'][qid]
        assert len(p['video_links'])==1,(file,qid)
        # All approved questions are self-contained; no figure is needed.
        p['requires_source_visual']=False
        old=p['video_links'][0]['video_id']
        if old!=vid:changes.append((file,qid,old,vid));p['video_links'][0]['video_id']=vid
        reviewed+=p['mapping_status']!='reviewed'
        p.update(mapping_method='manual',mapping_status='reviewed',mapping_rule='rotation-review-1',
          notes='Inspected against the authored analogous example: matching rotation method or shared rigid-transformation property and prerequisite steps; different numerical inputs.' + (' ' + REVIEW_NOTES[(file,qid)] if (file,qid) in REVIEW_NOTES else ''))
    for (file,qid),note in SOURCE_NOTES.items():
        p=doc['worksheets'][file]['problems'][qid]
        assert p['mapping_status']=='needs_review'
        p['notes']=note
        if note.startswith('Source visual missing:'):p['requires_source_visual']=True
    if merge:
        # All three variants of this one row were inspected and teach the same
        # half-turn method. Two original template IDs must stay discoverable.
        ref=g(8,6,8,5);p=doc['worksheets'][ref[0]]['problems'][ref[1]]
        target='geometry-rotation-half-turn'
        old_ids=['pattern-geometric-transformations-efcc57195f6c','pattern-geometric-transformations-f3d633629d9b']
        assert doc['videos'][target]['production_status']=='rendered'
        if p['video_links'][0]['video_id']!=target:
            assert {l['video_id'] for l in p['video_links']}==set(old_ids+['geometry-rotation'])
            assert {l['variant_index'] for l in p['video_links']}=={0,1,2}
            for old_id in old_ids:
                old=doc['videos'][old_id]
                assert old['production_status']=='planned' and not old['youtube']['video_id']
                assert all(x is None for x in old['assets'].values())
                refs={(f,q) for f,w in doc['worksheets'].items() for q,pp in w['problems'].items() if any(l['video_id']==old_id for l in pp['video_links'])}
                assert refs=={ref}
            changes.append((*ref,','.join(old_ids),target));reviewed+=p['mapping_status']!='reviewed'
            link=p['video_links'][0].copy();link.update(video_id=target,variant_index=None)
            p.update(video_links=[link],mapping_method='manual',mapping_status='reviewed',mapping_rule='rotation-variant-reuse-1',notes='All three variants inspected: coordinate pairs, sign-negation rule and transformation naming are covered by the verified analogous half-turn example. Original template IDs retained as reuse records.')
            for old_id in old_ids:
                old=doc['videos'][old_id]
                old.update(production_status='retired',reuse_video_ids=[target],notes='Inspected variant-specific draft reuses the completed half-turn lesson. Original ID retained for lookup; no separate upload needed.')
                old['planning']['review_status']='reviewed'
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
