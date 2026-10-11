"""Explicitly reviewed arithmetic estimation mappings and unresolved source issues."""
import argparse,fcntl,json
from pathlib import Path
from estimation_foundation_lessons import SPECS,lessons
from number_sense_lessons import source as g
from video_reuse import append_upload_row,update_reuse_checklist,merge_reviewed_duplicate
from build_video_correspondence import validate,read_inventory
from generate_video_batch import save_json,update_overview
from video_example_checks import require_analogous_examples

APPROVED=[]
ASSIGNMENTS = """estimate-whole-sum-difference 3 3 3 4,8
estimate-whole-sum-difference 3 3 3HW 3
estimate-whole-sum-difference 3 3 3Rev 4
estimate-closest-sum 3 3 3 9
estimate-closest-sum 3 3 3HW 4
estimate-compare-expressions 3 3 3 10
estimate-compare-expressions 3 3 3HW 5
estimate-one-factor 4 3 4 1,2,3,4,5,6,7,8
estimate-one-factor 4 3 4HW 1
estimate-one-factor 4 3 4Rev 1,2,4
estimate-two-factors-and-error 4 4 2 4,5,7,9
estimate-two-factors-and-error 4 4 2HW 2,4
estimate-two-factors-and-error 4 4 2Rev 4,5
estimate-two-factors-and-error 4 4 3 2,4
estimate-two-factors-and-error 4 4 3Rev 2,4
estimate-decimal-sum 5 2 2 1,2,3,4,5,6,7,8,10
estimate-decimal-sum 5 2 2HW 1,2,3,4
estimate-decimal-difference 5 3 1 1,2,3,4,5,6,7,8
estimate-decimal-difference 5 3 1HW 1,2,3,4
estimate-round-decimal-divisor 5 9 1 1,2
estimate-round-decimal-divisor 5 9 1HW 1
estimate-round-decimal-divisor 5 9 1Rev 1
"""
for row in ASSIGNMENTS.splitlines():
    vid,grade,unit,w,qs=row.split()
    APPROVED.extend((g(int(grade),int(unit),w,q),vid) for q in qs.split(','))
assert len(APPROVED)==len(set(ref for ref,vid in APPROVED))
MERGES=[]
SOURCE_NOTES={
 g(5,5,1,5):'Source solution error: the selected estimate 100 x 20 = 2000 is correct, but the worked solution then writes 200, dropping a factor of ten. Left pending; source unchanged.',
 g(5,8,1,1):'Source answer-format error: the requested rounded-factor estimate is 10, but the key also accepts the exact product 11, which does not follow the stated rounding instruction. Left pending; source unchanged.',
 g(5,8,1,2):'Source answer-format error: the requested rounded-factor estimate is 30, but the key also accepts the exact product 29.4. Left pending; source unchanged.',
 g(5,8,'1HW',1):'Source answer-format error: the requested rounded-factor estimate is 40, but the key also accepts the exact product 39.2. Left pending; source unchanged.',
 g(5,8,'1Rev',1):'Source answer-format error: the requested rounded-factor estimate is 18, but the key also accepts the exact product 18.6. Left pending; source unchanged.',
 g(5,8,1,3):'Source method ambiguity: no rounding place is specified, yet only 1750 is accepted using 68 to 70 and 23 to the compatible number 25. Nearest-ten rounding gives 1400. Clarify the compatible-number instruction or accepted estimates. Left pending; source unchanged.',
 g(5,8,'1Rev',2):'Source method ambiguity: no rounding place is specified, yet only 1750 is accepted using 72 to 70 and 24 to the compatible number 25. Nearest-ten rounding gives 1400. Left pending; source unchanged.',
 g(5,8,1,4):'Source solution mismatch: the prompt uses 99.3, but the solution starts with 99.2. Both round to 100, so the supplied estimates remain valid, but the source explanation needs its input corrected. Left pending; source unchanged.',
 g(5,8,1,5):'Source solution mismatch: the prompt uses 4.3, but the solution starts with 4.1. Both round to 4, so the estimates remain valid, but the explanation needs its input corrected. Left pending; source unchanged.',
}
REVIEW_NOTES={}


def apply_review(doc,merge=False):
    changes=[];reviewed=0
    for s in SPECS:
        vid=s['video_id'];title=s['topic']
        if vid not in doc['videos']:
            doc['videos'][vid]={'title':title,'question_type':title,'curriculum':{'kind':'shared','topic':'number'},
             'production_status':'planned','target_duration_seconds':60,'duration_seconds':None,'example':None,
             'assets':{'mp4':None,'captions':None},'youtube':{'video_id':None,'visibility':None},
             'notes':'Distinct arithmetic estimation method identified through explicit question review.',
             'planning':{'basis':'rule','rule':vid,'review_status':'needs_review'}}
    for (file,qid),vid in sorted(set(APPROVED)):
        p=doc['worksheets'][file]['problems'][qid]
        assert len(p['video_links'])==1,(file,qid)
        # All approved questions are self-contained; no figure is needed.
        p['requires_source_visual']=False
        old=p['video_links'][0]['video_id']
        if old!=vid:changes.append((file,qid,old,vid));p['video_links'][0]['video_id']=vid
        reviewed+=p['mapping_status']!='reviewed'
        p.update(mapping_method='manual',mapping_status='reviewed',mapping_rule='estimation-foundation-review-1',
          notes='Inspected against the authored analogous example: matching arithmetic estimation method and prerequisite steps; different numerical inputs.' + (' ' + REVIEW_NOTES[(file,qid)] if (file,qid) in REVIEW_NOTES else ''))
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
