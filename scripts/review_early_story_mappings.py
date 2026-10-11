"""Explicitly reviewed early story mappings and unresolved source issues."""
import argparse,fcntl,json,csv
from pathlib import Path
from early_story_lessons import SPECS,lessons
from number_sense_lessons import source as g
from video_reuse import append_upload_row,update_reuse_checklist,merge_reviewed_duplicate
from build_video_correspondence import validate,read_inventory
from generate_video_batch import save_json,update_overview
from video_example_checks import require_analogous_examples

APPROVED=[(('worksheets/Grade 2/G2Unit 4/G2U4W1.csv', '1'), 'add-tens-hundreds-place'), (('worksheets/Grade 2/G2Unit 4/G2U4W1.csv', '2'), 'add-tens-hundreds-place'), (('worksheets/Grade 2/G2Unit 4/G2U4W1.csv', '3'), 'add-tens-hundreds-place'), (('worksheets/Grade 2/G2Unit 4/G2U4W1.csv', '4'), 'add-tens-hundreds-place'), (('worksheets/Grade 2/G2Unit 4/G2U4W1.csv', '5'), 'add-three-digit-no-regroup'), (('worksheets/Grade 2/G2Unit 4/G2U4W1.csv', '6'), 'add-three-digit-no-regroup'), (('worksheets/Grade 2/G2Unit 4/G2U4W1.csv', '7'), 'arithmetic-add-whole-numbers-column-method'), (('worksheets/Grade 2/G2Unit 4/G2U4W1.csv', '8'), 'add-three-digit-no-regroup'), (('worksheets/Grade 2/G2Unit 4/G2U4W1.csv', '9'), 'arithmetic-add-whole-numbers-column-method'), (('worksheets/Grade 2/G2Unit 4/G2U4W1.csv', '10'), 'arithmetic-add-whole-numbers-column-method'), (('worksheets/Grade 2/G2Unit 4/G2U4W2.csv', '1'), 'place-three-digit-arithmetic'), (('worksheets/Grade 2/G2Unit 4/G2U4W2.csv', '2'), 'place-three-digit-arithmetic'), (('worksheets/Grade 2/G2Unit 4/G2U4W2.csv', '3'), 'place-three-digit-arithmetic'), (('worksheets/Grade 2/G2Unit 4/G2U4W2.csv', '4'), 'place-three-digit-arithmetic'), (('worksheets/Grade 2/G2Unit 4/G2U4W2.csv', '5'), 'place-three-digit-arithmetic'), (('worksheets/Grade 2/G2Unit 4/G2U4W2.csv', '6'), 'place-three-digit-arithmetic'), (('worksheets/Grade 2/G2Unit 4/G2U4W2.csv', '7'), 'place-three-digit-arithmetic'), (('worksheets/Grade 2/G2Unit 4/G2U4W2.csv', '8'), 'place-three-digit-arithmetic'), (('worksheets/Grade 2/G2Unit 4/G2U4W2.csv', '9'), 'arithmetic-subtract-whole-numbers-column-method'), (('worksheets/Grade 2/G2Unit 4/G2U4W2.csv', '10'), 'arithmetic-subtract-whole-numbers-column-method'), (('worksheets/Grade 2/G2Unit 4/G2U4W2Rev.csv', '1'), 'place-three-digit-arithmetic'), (('worksheets/Grade 2/G2Unit 4/G2U4W2Rev.csv', '2'), 'place-three-digit-arithmetic'), (('worksheets/Grade 2/G2Unit 4/G2U4W2Rev.csv', '3'), 'place-three-digit-arithmetic'), (('worksheets/Grade 2/G2Unit 4/G2U4W2Rev.csv', '4'), 'place-three-digit-arithmetic'), (('worksheets/Grade 2/G2Unit 4/G2U4W2Rev.csv', '5'), 'arithmetic-subtract-whole-numbers-column-method'), (('worksheets/Grade 2/G2Unit 4/G2U4W3.csv', '1'), 'add-four-numbers-place'), (('worksheets/Grade 2/G2Unit 4/G2U4W3.csv', '2'), 'add-four-numbers-place'), (('worksheets/Grade 2/G2Unit 4/G2U4W3.csv', '3'), 'add-four-numbers-place'), (('worksheets/Grade 2/G2Unit 4/G2U4W3.csv', '4'), 'add-four-numbers-place'), (('worksheets/Grade 2/G2Unit 4/G2U4W3.csv', '5'), 'add-four-numbers-place'), (('worksheets/Grade 2/G2Unit 4/G2U4W3.csv', '6'), 'add-four-numbers-place'), (('worksheets/Grade 2/G2Unit 4/G2U4W3HW.csv', '1'), 'add-three-digit-no-regroup'), (('worksheets/Grade 2/G2Unit 4/G2U4W3HW.csv', '2'), 'arithmetic-add-whole-numbers-column-method'), (('worksheets/Grade 2/G2Unit 4/G2U4W3HW.csv', '3'), 'add-three-digit-no-regroup'), (('worksheets/Grade 2/G2Unit 4/G2U4W3HW.csv', '4'), 'arithmetic-add-whole-numbers-column-method'), (('worksheets/Grade 2/G2Unit 4/G2U4W3HW.csv', '5'), 'arithmetic-add-whole-numbers-column-method'), (('worksheets/Grade 2/G2Unit 4/G2U4W3Rev.csv', '1'), 'add-tens-hundreds-place'), (('worksheets/Grade 2/G2Unit 4/G2U4W3Rev.csv', '2'), 'add-tens-hundreds-place'), (('worksheets/Grade 2/G2Unit 4/G2U4W3Rev.csv', '3'), 'add-tens-hundreds-place'), (('worksheets/Grade 2/G2Unit 4/G2U4W3Rev.csv', '4'), 'add-tens-hundreds-place'), (('worksheets/Grade 2/G2Unit 4/G2U4W3Rev.csv', '5'), 'add-three-digit-no-regroup'), (('worksheets/Grade 2/G2Unit 4/G2U4W1HW.csv', '1'), 'add-two-digit-no-regroup'), (('worksheets/Grade 2/G2Unit 4/G2U4W1HW.csv', '2'), 'subtract-two-digit-chain'), (('worksheets/Grade 2/G2Unit 4/G2U4W1HW.csv', '3'), 'arithmetic-add-split-tens-ones'), (('worksheets/Grade 2/G2Unit 4/G2U4W1HW.csv', '4'), 'arithmetic-add-split-tens-ones'), (('worksheets/Grade 2/G2Unit 4/G2U4W1HW.csv', '5'), 'subtract-two-digit-regroup'), (('worksheets/Grade 2/G2Unit 4/G2U4W1Rev.csv', '1'), 'arithmetic-two-digit-story-regroup'), (('worksheets/Grade 2/G2Unit 4/G2U4W1Rev.csv', '2'), 'arithmetic-small-story-changes'), (('worksheets/Grade 2/G2Unit 4/G2U4W1Rev.csv', '3'), 'story-change-two-groups'), (('worksheets/Grade 2/G2Unit 4/G2U4W1Rev.csv', '4'), 'subtract-small-chain'), (('worksheets/Grade 2/G2Unit 4/G2U4W1Rev.csv', '5'), 'story-remaining-weekly-capacity'), (('worksheets/Grade 2/G2Unit 4/G2U4W2HW.csv', '1'), 'arithmetic-small-story-changes'), (('worksheets/Grade 2/G2Unit 4/G2U4W2HW.csv', '2'), 'story-ignore-no-count-change'), (('worksheets/Grade 2/G2Unit 4/G2U4W2HW.csv', '4'), 'arithmetic-two-digit-story-regroup'), (('worksheets/Grade 2/G2Unit 4/G2U4W2HW.csv', '5'), 'story-change-two-groups'), (('worksheets/Grade 2/G2Unit 4/G2U4W3.csv', '7'), 'add-four-numbers-place'), (('worksheets/Grade 2/G2Unit 4/G2U4W3.csv', '8'), 'add-four-numbers-place'), (('worksheets/Grade 2/G2Unit 4/G2U4W3.csv', '9'), 'add-four-numbers-place'), (('worksheets/Grade 2/G2Unit 4/G2U4W3.csv', '10'), 'add-four-numbers-place')]
assert len(APPROVED)==len(set(ref for ref,vid in APPROVED))
MERGES=[]
from grade2_unit4_source_review import PENDING
SOURCE_NOTES=PENDING
REVIEW_NOTES={}


def apply_review(doc,merge=False):
    # A reviewed mapping requires the exact audited answer/solution row.
    root=Path(__file__).resolve().parents[1]
    audit=json.loads((root/'videos/grade-2-unit-4-source-corrections-2026-10-09.json').read_text())
    expected={(r['worksheet'],r['question_id']):r['after'] for r in audit['changes']}
    current={}
    for file,qid in expected:
        if file not in current:
            with (root/file).open(encoding='utf-8-sig',newline='') as f:current[file]={r['Question ID']:r for r in csv.DictReader(f)}
        assert current[file][qid]==expected[(file,qid)],('Source changed since answer/solution audit',file,qid)
    assert len(expected)==59
    changes=[];reviewed=0
    for s in SPECS:
        vid=s['video_id'];title=s['topic']
        if vid not in doc['videos']:
            doc['videos'][vid]={'title':title,'question_type':title,'curriculum':{'kind':'shared','topic':'number'},
             'production_status':'planned','target_duration_seconds':60,'duration_seconds':None,'example':None,
             'assets':{'mp4':None,'captions':None},'youtube':{'video_id':None,'visibility':None},
             'notes':'Distinct early story method identified through explicit question review.',
             'planning':{'basis':'rule','rule':vid,'review_status':'needs_review'}}
    for (file,qid),vid in sorted(set(APPROVED)):
        p=doc['worksheets'][file]['problems'][qid]
        assert len(p['video_links'])==1,(file,qid)
        # All approved questions are self-contained; no figure is needed.
        p['requires_source_visual']=False
        old=p['video_links'][0]['video_id']
        if old!=vid:changes.append((file,qid,old,vid));p['video_links'][0]['video_id']=vid
        reviewed+=p['mapping_status']!='reviewed'
        p.update(mapping_method='manual',mapping_status='reviewed',mapping_rule='early-story-review-1',
          notes='Worksheet answer, choices, hints and full worked solution reviewed; corrections recorded in grade-2-unit-4-source-corrections-2026-10-09.json. The supplemental W1 Q7 image was visually checked. Linked video uses different inputs to teach the matching method.' + (' ' + REVIEW_NOTES[(file,qid)] if (file,qid) in REVIEW_NOTES else ''))
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
