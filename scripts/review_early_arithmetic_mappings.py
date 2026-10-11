"""Explicitly reviewed early arithmetic mappings and unresolved source issues."""
import argparse,fcntl,json
from pathlib import Path
from early_arithmetic_lessons import SPECS,lessons
from number_sense_lessons import source as g
from video_reuse import append_upload_row,update_reuse_checklist,merge_reviewed_duplicate
from build_video_correspondence import validate,read_inventory
from generate_video_batch import save_json,update_overview
from video_example_checks import require_analogous_examples

APPROVED=[(('worksheets/Grade 1/G1Unit 2/G1U2W1.csv', '1'), 'add-count-on-small'), (('worksheets/Grade 1/G1Unit 2/G1U2W1.csv', '3'), 'add-count-on-small'), (('worksheets/Grade 1/G1Unit 2/G1U2W1.csv', '4'), 'add-count-on-small'), (('worksheets/Grade 1/G1Unit 2/G1U2W1.csv', '8'), 'add-count-on-small'), (('worksheets/Grade 1/G1Unit 2/G1U2W1.csv', '9'), 'add-count-on-small'), (('worksheets/Grade 1/G1Unit 2/G1U2W7.csv', '3'), 'add-count-on-small'), (('worksheets/Grade 1/G1Unit 2/G1U2W7.csv', '4'), 'add-count-on-small'), (('worksheets/Grade 1/G1Unit 2/G1U2W9.csv', '5'), 'add-count-on-small'), (('worksheets/Grade 1/G1Unit 2/G1U2W15.csv', '3'), 'add-count-on-small'), (('worksheets/Grade 1/G1Unit 2/G1U2W1.csv', '2'), 'subtract-take-away-small'), (('worksheets/Grade 1/G1Unit 2/G1U2W1.csv', '5'), 'subtract-take-away-small'), (('worksheets/Grade 1/G1Unit 2/G1U2W1.csv', '10'), 'subtract-take-away-small'), (('worksheets/Grade 1/G1Unit 2/G1U2W3.csv', '7'), 'subtract-take-away-small'), (('worksheets/Grade 1/G1Unit 2/G1U2W1.csv', '7'), 'add-subtract-fact-family'), (('worksheets/Grade 1/G1Unit 2/G1U2W2.csv', '1'), 'add-subtract-fact-family'), (('worksheets/Grade 1/G1Unit 2/G1U2W2.csv', '2'), 'add-subtract-fact-family'), (('worksheets/Grade 1/G1Unit 2/G1U2W2.csv', '5'), 'add-subtract-fact-family'), (('worksheets/Grade 1/G1Unit 2/G1U2W2.csv', '8'), 'add-subtract-fact-family'), (('worksheets/Grade 1/G1Unit 2/G1U2W1.csv', '11'), 'arithmetic-add-subtract-whole-numbers-within-20'), (('worksheets/Grade 1/G1Unit 2/G1U2W5.csv', '5'), 'arithmetic-add-subtract-whole-numbers-within-20'), (('worksheets/Grade 1/G1Unit 2/G1U2W5.csv', '10'), 'arithmetic-add-subtract-whole-numbers-within-20'), (('worksheets/Grade 1/G1Unit 2/G1U2W2.csv', '3'), 'add-swap-parts'), (('worksheets/Grade 1/G1Unit 2/G1U2W4.csv', '9'), 'add-swap-parts'), (('worksheets/Grade 1/G1Unit 2/G1U2W2.csv', '4'), 'add-balance-equation'), (('worksheets/Grade 1/G1Unit 2/G1U2W2.csv', '10'), 'add-balance-equation'), (('worksheets/Grade 1/G1Unit 2/G1U2W2.csv', '7'), 'order-compute-both-sides'), (('worksheets/Grade 1/G1Unit 2/G1U2W2.csv', '9'), 'order-compute-both-sides'), (('worksheets/Grade 1/G1Unit 2/G1U2W4.csv', '8'), 'order-compute-both-sides'), (('worksheets/Grade 1/G1Unit 2/G1U2W5.csv', '7'), 'order-compute-both-sides'), (('worksheets/Grade 1/G1Unit 2/G1U2W6.csv', '1'), 'order-compute-both-sides'), (('worksheets/Grade 1/G1Unit 2/G1U2W6.csv', '2'), 'order-compute-both-sides'), (('worksheets/Grade 1/G1Unit 2/G1U2W6.csv', '3'), 'order-compute-both-sides'), (('worksheets/Grade 1/G1Unit 2/G1U2W6.csv', '5'), 'order-compute-both-sides'), (('worksheets/Grade 1/G1Unit 2/G1U2W6.csv', '6'), 'order-compute-both-sides'), (('worksheets/Grade 1/G1Unit 2/G1U2W6.csv', '7'), 'order-compute-both-sides'), (('worksheets/Grade 1/G1Unit 2/G1U2W6.csv', '8'), 'order-compute-both-sides'), (('worksheets/Grade 1/G1Unit 2/G1U2W6.csv', '9'), 'order-compute-both-sides'), (('worksheets/Grade 1/G1Unit 2/G1U2W6.csv', '10'), 'order-compute-both-sides'), (('worksheets/Grade 1/G1Unit 2/G1U2W10.csv', '8'), 'order-compute-both-sides'), (('worksheets/Grade 1/G1Unit 2/G1U2W13.csv', '6'), 'order-compute-both-sides'), (('worksheets/Grade 1/G1Unit 2/G1U2W13.csv', '7'), 'order-compute-both-sides'), (('worksheets/Grade 1/G1Unit 2/G1U2W3.csv', '1'), 'add-parts-to-target'), (('worksheets/Grade 1/G1Unit 2/G1U2W3.csv', '2'), 'add-parts-to-target'), (('worksheets/Grade 1/G1Unit 2/G1U2W3.csv', '3'), 'add-parts-to-target'), (('worksheets/Grade 1/G1Unit 2/G1U2W3.csv', '4'), 'add-parts-to-target'), (('worksheets/Grade 1/G1Unit 2/G1U2W3.csv', '6'), 'order-complete-ten'), (('worksheets/Grade 1/G1Unit 2/G1U2W3.csv', '9'), 'order-complete-ten'), (('worksheets/Grade 1/G1Unit 2/G1U2W4.csv', '4'), 'order-complete-ten'), (('worksheets/Grade 1/G1Unit 2/G1U2W4.csv', '1'), 'count-ten-frames'), (('worksheets/Grade 1/G1Unit 2/G1U2W4.csv', '2'), 'add-bridge-ten-early'), (('worksheets/Grade 1/G1Unit 2/G1U2W4.csv', '5'), 'add-bridge-ten-early'), (('worksheets/Grade 1/G1Unit 2/G1U2W4.csv', '6'), 'add-three-using-ten'), (('worksheets/Grade 1/G1Unit 2/G1U2W4.csv', '10'), 'add-three-using-ten'), (('worksheets/Grade 1/G1Unit 2/G1U2W4.csv', '7'), 'add-regroup-ones-early'), (('worksheets/Grade 1/G1Unit 2/G1U2W15.csv', '6'), 'add-regroup-ones-early'), (('worksheets/Grade 1/G1Unit 2/G1U2W15.csv', '10'), 'add-regroup-ones-early'), (('worksheets/Grade 1/G1Unit 2/G1U2W15.csv', '11'), 'add-regroup-ones-early'), (('worksheets/Grade 1/G1Unit 2/G1U2W5.csv', '1'), 'arithmetic-subtract-whole-numbers-within-20'), (('worksheets/Grade 1/G1Unit 2/G1U2W5.csv', '2'), 'arithmetic-subtract-whole-numbers-within-20'), (('worksheets/Grade 1/G1Unit 2/G1U2W5.csv', '3'), 'arithmetic-subtract-whole-numbers-within-20'), (('worksheets/Grade 1/G1Unit 2/G1U2W5.csv', '6'), 'arithmetic-subtract-whole-numbers-within-20'), (('worksheets/Grade 1/G1Unit 2/G1U2W5.csv', '8'), 'g1-u1-counting-forward'), (('worksheets/Grade 1/G1Unit 2/G1U2W6.csv', '4'), 'order-number-line-direction'), (('worksheets/Grade 1/G1Unit 2/G1U2W7.csv', '2'), 'number-place-value-whole-numbers'), (('worksheets/Grade 1/G1Unit 2/G1U2W8.csv', '1'), 'number-place-value-whole-numbers'), (('worksheets/Grade 1/G1Unit 2/G1U2W8.csv', '2'), 'number-place-value-whole-numbers'), (('worksheets/Grade 1/G1Unit 2/G1U2W11.csv', '2'), 'number-place-value-whole-numbers'), (('worksheets/Grade 1/G1Unit 2/G1U2W11.csv', '3'), 'number-place-value-whole-numbers'), (('worksheets/Grade 1/G1Unit 2/G1U2W7.csv', '5'), 'place-compare-digit-counts'), (('worksheets/Grade 1/G1Unit 2/G1U2W7.csv', '6'), 'place-compare-digit-counts'), (('worksheets/Grade 1/G1Unit 2/G1U2W8.csv', '4'), 'place-compare-digit-counts'), (('worksheets/Grade 1/G1Unit 2/G1U2W7.csv', '7'), 'place-add-one-ten'), (('worksheets/Grade 1/G1Unit 2/G1U2W7.csv', '8'), 'place-add-one-ten'), (('worksheets/Grade 1/G1Unit 2/G1U2W9.csv', '2'), 'place-add-one-ten'), (('worksheets/Grade 1/G1Unit 2/G1U2W7.csv', '9'), 'add-make-next-ten'), (('worksheets/Grade 1/G1Unit 2/G1U2W14.csv', '1'), 'add-make-next-ten'), (('worksheets/Grade 1/G1Unit 2/G1U2W14.csv', '2'), 'add-make-next-ten'), (('worksheets/Grade 1/G1Unit 2/G1U2W14.csv', '3'), 'add-make-next-ten'), (('worksheets/Grade 1/G1Unit 2/G1U2W14.csv', '4'), 'add-make-next-ten'), (('worksheets/Grade 1/G1Unit 2/G1U2W14.csv', '5'), 'add-make-next-ten'), (('worksheets/Grade 1/G1Unit 2/G1U2W14.csv', '6'), 'add-make-next-ten'), (('worksheets/Grade 1/G1Unit 2/G1U2W14.csv', '7'), 'add-make-next-ten'), (('worksheets/Grade 1/G1Unit 2/G1U2W14.csv', '8'), 'add-make-next-ten'), (('worksheets/Grade 1/G1Unit 2/G1U2W14.csv', '9'), 'add-make-next-ten'), (('worksheets/Grade 1/G1Unit 2/G1U2W14.csv', '10'), 'add-make-next-ten'), (('worksheets/Grade 1/G1Unit 2/G1U2W8.csv', '3'), 'place-subtract-two-digit'), (('worksheets/Grade 1/G1Unit 2/G1U2W8.csv', '5'), 'place-subtract-two-digit'), (('worksheets/Grade 1/G1Unit 2/G1U2W8.csv', '6'), 'place-subtract-two-digit'), (('worksheets/Grade 1/G1Unit 2/G1U2W8.csv', '7'), 'place-subtract-two-digit'), (('worksheets/Grade 1/G1Unit 2/G1U2W8.csv', '9'), 'place-subtract-two-digit'), (('worksheets/Grade 1/G1Unit 2/G1U2W13.csv', '1'), 'place-subtract-two-digit'), (('worksheets/Grade 1/G1Unit 2/G1U2W13.csv', '3'), 'place-subtract-two-digit'), (('worksheets/Grade 1/G1Unit 2/G1U2W8.csv', '8'), 'place-compare-two-digit'), (('worksheets/Grade 1/G1Unit 2/G1U2W8.csv', '10'), 'order-ten-less'), (('worksheets/Grade 1/G1Unit 2/G1U2W9.csv', '1'), 'count-fill-ones'), (('worksheets/Grade 1/G1Unit 2/G1U2W9.csv', '4'), 'count-tens-both-directions'), (('worksheets/Grade 1/G1Unit 2/G1U2W10.csv', '7'), 'count-tens-both-directions'), (('worksheets/Grade 1/G1Unit 2/G1U2W9.csv', '6'), 'g1-u1-counting-backward'), (('worksheets/Grade 1/G1Unit 2/G1U2W9.csv', '7'), 'place-cross-hundred-ten'), (('worksheets/Grade 1/G1Unit 2/G1U2W9.csv', '8'), 'arithmetic-follow-changes'), (('worksheets/Grade 1/G1Unit 2/G1U2W9.csv', '10'), 'arithmetic-follow-changes'), (('worksheets/Grade 1/G1Unit 2/G1U2W10.csv', '9'), 'arithmetic-follow-changes'), (('worksheets/Grade 1/G1Unit 2/G1U2W10.csv', '10'), 'arithmetic-follow-changes'), (('worksheets/Grade 1/G1Unit 2/G1U2W10.csv', '11'), 'arithmetic-follow-changes'), (('worksheets/Grade 1/G1Unit 2/G1U2W13.csv', '8'), 'arithmetic-follow-changes'), (('worksheets/Grade 1/G1Unit 2/G1U2W9.csv', '9'), 'place-compare-three-digit-forms'), (('worksheets/Grade 1/G1Unit 2/G1U2W10.csv', '1'), 'place-change-three-digit-units'), (('worksheets/Grade 1/G1Unit 2/G1U2W10.csv', '4'), 'place-change-three-digit-units'), (('worksheets/Grade 1/G1Unit 2/G1U2W10.csv', '5'), 'place-add-one-hundred'), (('worksheets/Grade 1/G1Unit 2/G1U2W10.csv', '6'), 'count-hundreds-pattern'), (('worksheets/Grade 1/G1Unit 2/G1U2W11.csv', '6'), 'arithmetic-add-split-tens-ones'), (('worksheets/Grade 1/G1Unit 2/G1U2W12.csv', '2'), 'arithmetic-add-split-tens-ones'), (('worksheets/Grade 1/G1Unit 2/G1U2W12.csv', '3'), 'arithmetic-add-split-tens-ones'), (('worksheets/Grade 1/G1Unit 2/G1U2W15.csv', '4'), 'arithmetic-add-split-tens-ones'), (('worksheets/Grade 1/G1Unit 2/G1U2W12.csv', '6'), 'add-two-digit-no-regroup'), (('worksheets/Grade 1/G1Unit 2/G1U2W12.csv', '8'), 'add-two-digit-no-regroup'), (('worksheets/Grade 1/G1Unit 2/G1U2W12.csv', '9'), 'add-missing-part-many'), (('worksheets/Grade 1/G1Unit 2/G1U2W13.csv', '4'), 'subtract-missing-part-whole'), (('worksheets/Grade 1/G1Unit 2/G1U2W13.csv', '5'), 'subtract-missing-part-whole'), (('worksheets/Grade 1/G1Unit 2/G1U2W13.csv', '9'), 'subtract-two-digit-regroup'), (('worksheets/Grade 1/G1Unit 2/G1U2W13.csv', '10'), 'subtract-two-digit-regroup')]
assert len(APPROVED)==len(set(ref for ref,vid in APPROVED))
MERGES=[]
SOURCE_NOTES={('worksheets/Grade 1/G1Unit 2/G1U2W2.csv', '6'): 'Source underdetermined: 9 + __ = 10 + __ has many valid nonnegative answer pairs, such as (1,0) and (2,1), but the key accepts only (1,0). Specify the intended total or accept all valid pairs. Left pending; worksheet unchanged.', ('worksheets/Grade 1/G1Unit 2/G1U2W3.csv', '8'): 'Source answer-key error: 1 + __ = __ + 5 = 10 requires (9,5), but the key is (4,5). Left pending; worksheet unchanged.', ('worksheets/Grade 1/G1Unit 2/G1U2W3.csv', '10'): 'Source domain ambiguity: the keyed six ways to make 5 assumes two nonnegative integer addends with reversed orders counted separately. Neither restriction is explicit. Left pending; worksheet unchanged.', ('worksheets/Grade 1/G1Unit 2/G1U2W5.csv', '4'): 'Source malformed equation: the third item says 13 - 3 + __ instead of 13 - 3 = __. The intended key 10 fits subtraction, but the printed item has no equality or target. Left pending; worksheet unchanged.'}
REVIEW_NOTES={}


def apply_review(doc,merge=False):
    changes=[];reviewed=0
    for s in SPECS:
        vid=s['video_id'];title=s['topic']
        if vid not in doc['videos']:
            doc['videos'][vid]={'title':title,'question_type':title,'curriculum':{'kind':'shared','topic':'number'},
             'production_status':'planned','target_duration_seconds':60,'duration_seconds':None,'example':None,
             'assets':{'mp4':None,'captions':None},'youtube':{'video_id':None,'visibility':None},
             'notes':'Distinct early arithmetic method identified through explicit question review.',
             'planning':{'basis':'rule','rule':vid,'review_status':'needs_review'}}
    for (file,qid),vid in sorted(set(APPROVED)):
        p=doc['worksheets'][file]['problems'][qid]
        assert len(p['video_links'])==1,(file,qid)
        # All approved questions are self-contained; no figure is needed.
        p['requires_source_visual']=False
        old=p['video_links'][0]['video_id']
        if old!=vid:changes.append((file,qid,old,vid));p['video_links'][0]['video_id']=vid
        reviewed+=p['mapping_status']!='reviewed'
        p.update(mapping_method='manual',mapping_status='reviewed',mapping_rule='early-arithmetic-review-1',
          notes='Inspected against the authored analogous example: matching early arithmetic method and prerequisite steps; different numerical inputs.' + (' ' + REVIEW_NOTES[(file,qid)] if (file,qid) in REVIEW_NOTES else ''))
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
