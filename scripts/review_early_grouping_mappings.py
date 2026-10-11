"""Explicitly reviewed early grouping mappings and unresolved source issues."""
import argparse,fcntl,json
from pathlib import Path
from early_grouping_lessons import SPECS,lessons
from number_sense_lessons import source as g
from video_reuse import append_upload_row,update_reuse_checklist,merge_reviewed_duplicate
from build_video_correspondence import validate,read_inventory
from generate_video_batch import save_json,update_overview
from video_example_checks import require_analogous_examples

APPROVED=[(('worksheets/Grade 2/G2Unit 1/G2U1W1.csv', '1'), 'arithmetic-add-whole-numbers-within-20'), (('worksheets/Grade 2/G2Unit 1/G2U1W1.csv', '2'), 'arithmetic-add-whole-numbers-within-20'), (('worksheets/Grade 2/G2Unit 1/G2U1W1.csv', '3'), 'arithmetic-add-whole-numbers-within-20'), (('worksheets/Grade 2/G2Unit 1/G2U1W1.csv', '4'), 'arithmetic-add-whole-numbers-within-20'), (('worksheets/Grade 2/G2Unit 1/G2U1W1.csv', '5'), 'arithmetic-add-whole-numbers-within-20'), (('worksheets/Grade 2/G2Unit 1/G2U1W1.csv', '6'), 'arithmetic-add-whole-numbers-within-20'), (('worksheets/Grade 2/G2Unit 1/G2U1W1.csv', '8'), 'arithmetic-add-whole-numbers-within-20'), (('worksheets/Grade 2/G2Unit 1/G2U1W1.csv', '9'), 'arithmetic-add-whole-numbers-within-20'), (('worksheets/Grade 2/G2Unit 1/G2U1W1.csv', '10'), 'arithmetic-add-whole-numbers-within-20'), (('worksheets/Grade 2/G2Unit 1/G2U1W1HW.csv', '1'), 'arithmetic-add-whole-numbers-within-20'), (('worksheets/Grade 2/G2Unit 1/G2U1W1HW.csv', '2'), 'arithmetic-add-whole-numbers-within-20'), (('worksheets/Grade 2/G2Unit 1/G2U1W1HW.csv', '4'), 'arithmetic-add-whole-numbers-within-20'), (('worksheets/Grade 2/G2Unit 1/G2U1W1HW.csv', '5'), 'arithmetic-add-whole-numbers-within-20'), (('worksheets/Grade 2/G2Unit 1/G2U1W2HW.csv', '1'), 'arithmetic-add-whole-numbers-within-20'), (('worksheets/Grade 2/G2Unit 1/G2U1W2HW.csv', '3'), 'arithmetic-add-whole-numbers-within-20'), (('worksheets/Grade 2/G2Unit 1/G2U1W2HW.csv', '4'), 'arithmetic-add-whole-numbers-within-20'), (('worksheets/Grade 2/G2Unit 1/G2U1W2HW.csv', '5'), 'arithmetic-add-whole-numbers-within-20'), (('worksheets/Grade 2/G2Unit 1/G2U1W4.csv', '3'), 'arithmetic-add-whole-numbers-within-20'), (('worksheets/Grade 2/G2Unit 1/G2U1W1.csv', '7'), 'add-three-using-ten'), (('worksheets/Grade 2/G2Unit 1/G2U1W1HW.csv', '3'), 'add-three-using-ten'), (('worksheets/Grade 2/G2Unit 1/G2U1W1Rev.csv', '1'), 'add-three-using-ten'), (('worksheets/Grade 2/G2Unit 1/G2U1W1Rev.csv', '3'), 'add-three-using-ten'), (('worksheets/Grade 2/G2Unit 1/G2U1W1Rev.csv', '5'), 'place-regroup-teen-ones'), (('worksheets/Grade 2/G2Unit 1/G2U1W1Rev.csv', '2'), 'add-find-third-part-two-stages'), (('worksheets/Grade 2/G2Unit 1/G2U1W2.csv', '1'), 'count-array-rows-columns'), (('worksheets/Grade 2/G2Unit 1/G2U1W2.csv', '3'), 'count-array-rows-columns'), (('worksheets/Grade 2/G2Unit 1/G2U1W2.csv', '4'), 'count-array-rows-columns'), (('worksheets/Grade 2/G2Unit 1/G2U1W2.csv', '5'), 'count-array-rows-columns'), (('worksheets/Grade 2/G2Unit 1/G2U1W2.csv', '6'), 'count-array-rows-columns'), (('worksheets/Grade 2/G2Unit 1/G2U1W2.csv', '7'), 'count-array-rows-columns'), (('worksheets/Grade 2/G2Unit 1/G2U1W2.csv', '8'), 'count-array-rows-columns'), (('worksheets/Grade 2/G2Unit 1/G2U1W3HW.csv', '2'), 'count-array-rows-columns'), (('worksheets/Grade 2/G2Unit 1/G2U1W3HW.csv', '4'), 'count-array-rows-columns'), (('worksheets/Grade 2/G2Unit 1/G2U1W2Rev.csv', '2'), 'count-array-rows-columns'), (('worksheets/Grade 2/G2Unit 1/G2U1W2.csv', '10'), 'count-daily-groups-week'), (('worksheets/Grade 2/G2Unit 1/G2U1W2Rev.csv', '1'), 'count-daily-groups-week'), (('worksheets/Grade 2/G2Unit 1/G2U1W2Rev.csv', '3'), 'divide-share-small-total'), (('worksheets/Grade 2/G2Unit 1/G2U1W2Rev.csv', '4'), 'compare-equal-group-totals'), (('worksheets/Grade 2/G2Unit 1/G2U1W2Rev.csv', '5'), 'count-combine-equal-packs'), (('worksheets/Grade 2/G2Unit 1/G2U1W2HW.csv', '2'), 'arithmetic-missing-small-part'), (('worksheets/Grade 2/G2Unit 1/G2U1W4.csv', '4'), 'arithmetic-missing-small-part'), (('worksheets/Grade 2/G2Unit 1/G2U1W4.csv', '5'), 'arithmetic-missing-small-part'), (('worksheets/Grade 2/G2Unit 1/G2U1W4.csv', '6'), 'arithmetic-missing-small-part'), (('worksheets/Grade 2/G2Unit 1/G2U1W4.csv', '7'), 'arithmetic-missing-small-part'), (('worksheets/Grade 2/G2Unit 1/G2U1W4.csv', '8'), 'arithmetic-missing-small-part'), (('worksheets/Grade 2/G2Unit 1/G2U1W4HW.csv', '2'), 'arithmetic-missing-small-part'), (('worksheets/Grade 2/G2Unit 1/G2U1W4Rev.csv', '3'), 'arithmetic-missing-small-part'), (('worksheets/Grade 2/G2Unit 1/G2U1W4Rev.csv', '4'), 'arithmetic-missing-small-part'), (('worksheets/Grade 2/G2Unit 1/G2U1W3.csv', '1'), 'arithmetic-subtract-whole-numbers-within-20'), (('worksheets/Grade 2/G2Unit 1/G2U1W3.csv', '2'), 'arithmetic-subtract-whole-numbers-within-20'), (('worksheets/Grade 2/G2Unit 1/G2U1W3.csv', '3'), 'arithmetic-subtract-whole-numbers-within-20'), (('worksheets/Grade 2/G2Unit 1/G2U1W3.csv', '7'), 'arithmetic-subtract-whole-numbers-within-20'), (('worksheets/Grade 2/G2Unit 1/G2U1W3.csv', '8'), 'arithmetic-subtract-whole-numbers-within-20'), (('worksheets/Grade 2/G2Unit 1/G2U1W4.csv', '1'), 'arithmetic-subtract-whole-numbers-within-20'), (('worksheets/Grade 2/G2Unit 1/G2U1W4.csv', '2'), 'arithmetic-subtract-whole-numbers-within-20'), (('worksheets/Grade 2/G2Unit 1/G2U1W4HW.csv', '1'), 'arithmetic-subtract-whole-numbers-within-20'), (('worksheets/Grade 2/G2Unit 1/G2U1W4HW.csv', '3'), 'arithmetic-subtract-whole-numbers-within-20'), (('worksheets/Grade 2/G2Unit 1/G2U1W3.csv', '4'), 'subtract-small-chain'), (('worksheets/Grade 2/G2Unit 1/G2U1W3.csv', '5'), 'subtract-small-chain'), (('worksheets/Grade 2/G2Unit 1/G2U1W3.csv', '6'), 'subtract-small-chain'), (('worksheets/Grade 2/G2Unit 1/G2U1W3Rev.csv', '1'), 'subtract-small-chain'), (('worksheets/Grade 2/G2Unit 1/G2U1W3Rev.csv', '2'), 'subtract-small-chain'), (('worksheets/Grade 2/G2Unit 1/G2U1W3Rev.csv', '4'), 'subtract-small-chain'), (('worksheets/Grade 2/G2Unit 1/G2U1W3Rev.csv', '5'), 'subtract-small-chain'), (('worksheets/Grade 2/G2Unit 1/G2U1W4.csv', '9'), 'subtract-small-chain'), (('worksheets/Grade 2/G2Unit 1/G2U1W3.csv', '9'), 'order-compute-both-sides'), (('worksheets/Grade 2/G2Unit 1/G2U1W3.csv', '10'), 'order-compute-both-sides'), (('worksheets/Grade 2/G2Unit 1/G2U1W3Rev.csv', '3'), 'order-compute-both-sides'), (('worksheets/Grade 2/G2Unit 1/G2U1W4.csv', '10'), 'arithmetic-small-story-changes'), (('worksheets/Grade 2/G2Unit 1/G2U1W4Rev.csv', '1'), 'arithmetic-small-story-changes'), (('worksheets/Grade 2/G2Unit 1/G2U1W4Rev.csv', '2'), 'arithmetic-small-story-changes'), (('worksheets/Grade 2/G2Unit 1/G2U1W4Rev.csv', '5'), 'arithmetic-work-backwards-small')]
APPROVED.append((('worksheets/Grade 2/G2Unit 1/G2U1W2.csv', '2'),"count-array-rows-columns"))
assert len(APPROVED)==len(set(ref for ref,vid in APPROVED))
MERGES=[]
SOURCE_NOTES={('worksheets/Grade 2/G2Unit 1/G2U1W3HW.csv', '1'): 'Source display ambiguity: Row 1 contains the text <3 before two heart symbols. If read as an extra heart, the figure has seven hearts, while the key assumes six. Remove or explain the stray <3 before approving the video mapping. Worksheet unchanged.', ('worksheets/Grade 2/G2Unit 1/G2U1W3HW.csv', '3'): 'Source answer-key ambiguity: both 5+5+5 and 3+3+3+3+3 equal the total of 15 birds, but only the first is accepted. Ask which models the branches directly, or accept both for the stated total. Worksheet unchanged.', ('worksheets/Grade 2/G2Unit 1/G2U1W4HW.csv', '5'): 'Source answer-key error: both 12-3 and 20-11 equal 18-9=9, but only 12-3 is accepted. Both choices should be accepted. Worksheet unchanged.'}
REVIEW_NOTES={('worksheets/Grade 2/G2Unit 1/G2U1W2.csv', '1'): 'Source image opened and visually checked in the in-app browser on 2026-10-08. Five rows of three stars; three columns of five. Key 5+5+5 matches.', ('worksheets/Grade 2/G2Unit 1/G2U1W2.csv', '3'): 'Source image opened and visually checked in the in-app browser on 2026-10-08. Two rows of five stars; both 5+5 and five twos match.', ('worksheets/Grade 2/G2Unit 1/G2U1W2.csv', '4'): 'Source image opened and visually checked in the in-app browser on 2026-10-08. Four rows of two stars; both four twos and 4+4 match.', ('worksheets/Grade 2/G2Unit 1/G2U1W2.csv', '5'): 'Source image opened and visually checked in the in-app browser on 2026-10-08. Three rows of four apples; rows 4+4+4 and columns 3+3+3+3 match.', ('worksheets/Grade 2/G2Unit 1/G2U1W2.csv', '6'): 'Source image opened and visually checked in the in-app browser on 2026-10-08. Three rows of three apples; both totals are nine.', ('worksheets/Grade 2/G2Unit 1/G2U1W4Rev.csv', '1'): 'Follow each person’s changes separately, then compare the final counts.', ('worksheets/Grade 2/G2Unit 1/G2U1W2.csv', '2'): 'Source image opened and visually checked in the in-app browser on 2026-10-08 after retrying a temporary service-unavailable response. Three rows of four stars; key 4+4+4 matches.'}
VISUAL_REFS={('worksheets/Grade 2/G2Unit 1/G2U1W2.csv', '4'), ('worksheets/Grade 2/G2Unit 1/G2U1W2.csv', '2'), ('worksheets/Grade 2/G2Unit 1/G2U1W2.csv', '5'), ('worksheets/Grade 2/G2Unit 1/G2U1W2.csv', '6'), ('worksheets/Grade 2/G2Unit 1/G2U1W2.csv', '3'), ('worksheets/Grade 2/G2Unit 1/G2U1W2.csv', '1')}


def apply_review(doc,merge=False):
    changes=[];reviewed=0
    for s in SPECS:
        vid=s['video_id'];title=s['topic']
        if vid not in doc['videos']:
            doc['videos'][vid]={'title':title,'question_type':title,'curriculum':{'kind':'shared','topic':'number'},
             'production_status':'planned','target_duration_seconds':60,'duration_seconds':None,'example':None,
             'assets':{'mp4':None,'captions':None},'youtube':{'video_id':None,'visibility':None},
             'notes':'Distinct early grouping method identified through explicit question review.',
             'planning':{'basis':'rule','rule':vid,'review_status':'needs_review'}}
    for (file,qid),vid in sorted(set(APPROVED)):
        p=doc['worksheets'][file]['problems'][qid]
        assert len(p['video_links'])==1,(file,qid)
        # Retain figure dependence when the actual source image was checked.
        p['requires_source_visual']=(file,qid) in VISUAL_REFS
        old=p['video_links'][0]['video_id']
        if old!=vid:changes.append((file,qid,old,vid));p['video_links'][0]['video_id']=vid
        reviewed+=p['mapping_status']!='reviewed'
        p.update(mapping_method='manual',mapping_status='reviewed',mapping_rule='early-grouping-review-1',
          notes='Inspected against the authored analogous example: matching early grouping method and prerequisite steps; different numerical inputs.' + (' ' + REVIEW_NOTES[(file,qid)] if (file,qid) in REVIEW_NOTES else ''))
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
