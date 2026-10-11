"""Explicitly reviewed foundational equation mappings and unresolved source issues."""
import argparse,fcntl,json
from pathlib import Path
from linear_foundation_lessons import SPECS,lessons
from number_sense_lessons import source as g
from video_reuse import append_upload_row,update_reuse_checklist,merge_reviewed_duplicate
from build_video_correspondence import validate,read_inventory
from generate_video_batch import save_json,update_overview
from video_example_checks import require_analogous_examples

APPROVED=[]
ASSIGNMENTS = """linear-one-step-add-subtract 6 7 1 8,9
linear-one-step-add-subtract 6 7 1HW 4,5
linear-one-step-add-subtract 6 7 2 2
linear-one-step-add-subtract 6 7 2HW 2
linear-one-step-add-subtract 6 7 3 1
linear-one-step-add-subtract 6 7 3HW 1
linear-unknown-subtrahend 6 7 2 10
linear-unknown-subtrahend 6 7 2Rev 5
linear-unknown-subtrahend 6 7 3 2
linear-unknown-subtrahend 6 7 3Rev 1
linear-one-step-multiply-divide 6 7 2 3
linear-one-step-multiply-divide 6 7 2HW 3
linear-one-step-multiply-divide 6 7 4 1,2,4,5,6
linear-one-step-multiply-divide 6 7 4HW 1,3,4
linear-one-step-multiply-divide 6 7 4Rev 1
linear-decimal-additive-equation 6 7 3 4
linear-decimal-additive-equation 6 7 3HW 3
linear-decimal-multiplier-equation 6 7 4 7,8
linear-decimal-multiplier-equation 6 7 4HW 5
linear-decimal-multiplier-equation 6 7 4Rev 2
linear-decimal-multiplier-equation 6 7 5 5
linear-decimal-multiplier-equation 6 7 5HW 4
linear-fraction-additive-equations 6 7 3 5,6
linear-fraction-additive-equations 6 7 3HW 4
linear-fraction-additive-equations 6 7 3Rev 2
linear-fraction-coefficient-equation 6 7 5 2,3,4
linear-fraction-coefficient-equation 6 7 5HW 2,3
linear-fraction-coefficient-equation 6 7 5Rev 1
linear-fraction-coefficient-equation 8 2 3 8
linear-fraction-coefficient-equation 8 2 3Rev 3
linear-combine-coefficients-equation 6 7 4 3
linear-combine-coefficients-equation 6 7 4HW 2
linear-combine-coefficients-equation 6 7 4Rev 5
linear-mixed-coefficients-equation 6 7 5 6
linear-mixed-coefficients-equation 6 7 5Rev 2
linear-price-times-quantity-equation 6 7 5 9,10
linear-price-times-quantity-equation 6 7 5HW 5
linear-price-times-quantity-equation 6 7 5Rev 5
linear-equations-solve-one-side 7 6 4 2,7
linear-equations-solve-one-side 7 6 4HW 1
linear-equations-solve-one-side 7 6 4Rev 3
"""
for row in ASSIGNMENTS.splitlines():
    vid,grade,unit,w,qs=row.split()
    APPROVED.extend((g(int(grade),int(unit),w,q),vid) for q in qs.split(','))
assert len(APPROVED)==len(set(ref for ref,vid in APPROVED))
MERGES=[]
SOURCE_NOTES={g(7,6,3,1):'Source answer-key error: decimal -22.5 and mixed number -22 1/2 are correct, but accepted fraction -105/2 is not equivalent; it should be -45/2. Left pending; source unchanged.'}
REVIEW_NOTES={}


def apply_review(doc,merge=False):
    changes=[];reviewed=0
    for s in SPECS:
        vid=s['video_id'];title=s['topic']
        if vid not in doc['videos']:
            doc['videos'][vid]={'title':title,'question_type':title,'curriculum':{'kind':'shared','topic':'algebra'},
             'production_status':'planned','target_duration_seconds':60,'duration_seconds':None,'example':None,
             'assets':{'mp4':None,'captions':None},'youtube':{'video_id':None,'visibility':None},
             'notes':'Distinct foundational equation method identified through explicit question review.',
             'planning':{'basis':'rule','rule':vid,'review_status':'needs_review'}}
    for (file,qid),vid in sorted(set(APPROVED)):
        p=doc['worksheets'][file]['problems'][qid]
        assert len(p['video_links'])==1,(file,qid)
        # All approved questions are self-contained; no figure is needed.
        p['requires_source_visual']=False
        old=p['video_links'][0]['video_id']
        if old!=vid:changes.append((file,qid,old,vid));p['video_links'][0]['video_id']=vid
        reviewed+=p['mapping_status']!='reviewed'
        p.update(mapping_method='manual',mapping_status='reviewed',mapping_rule='linear-foundation-review-1',
          notes='Inspected against the authored analogous example: matching foundational equation method and prerequisite steps; different numerical inputs.' + (' ' + REVIEW_NOTES[(file,qid)] if (file,qid) in REVIEW_NOTES else ''))
    for (file,qid),note in SOURCE_NOTES.items():
        p=doc['worksheets'][file]['problems'][qid]
        assert p['mapping_status']=='needs_review'
        p['notes']=note
        if note.startswith('Source visual missing:'):p['requires_source_visual']=True
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
