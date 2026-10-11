"""Explicitly reviewed early parity mappings and unresolved source issues."""
import argparse,fcntl,json,csv
from pathlib import Path
from early_parity_lessons import SPECS,lessons
from number_sense_lessons import source as g
from video_reuse import append_upload_row,update_reuse_checklist,merge_reviewed_duplicate
from build_video_correspondence import validate,read_inventory
from generate_video_batch import save_json,update_overview
from video_example_checks import require_analogous_examples

APPROVED=[(('worksheets/Grade 2/G2Unit 2/G2U2W1.csv', '1'), 'number-place-value-whole-numbers'), (('worksheets/Grade 2/G2Unit 2/G2U2W1.csv', '2'), 'number-place-value-whole-numbers'), (('worksheets/Grade 2/G2Unit 2/G2U2W1.csv', '3'), 'number-place-value-expanded-form'), (('worksheets/Grade 2/G2Unit 2/G2U2W1.csv', '4'), 'number-place-value-expanded-form'), (('worksheets/Grade 2/G2Unit 2/G2U2W1.csv', '8'), 'order-arrange-digits'), (('worksheets/Grade 2/G2Unit 2/G2U2W1.csv', '9'), 'order-arrange-digits'), (('worksheets/Grade 2/G2Unit 2/G2U2W1.csv', '10'), 'place-largest-fixed-digit'), (('worksheets/Grade 2/G2Unit 2/G2U2W1Rev.csv', '1'), 'number-place-value-whole-numbers'), (('worksheets/Grade 2/G2Unit 2/G2U2W1Rev.csv', '2'), 'number-place-value-expanded-form'), (('worksheets/Grade 2/G2Unit 2/G2U2W1Rev.csv', '4'), 'order-arrange-digits'), (('worksheets/Grade 2/G2Unit 2/G2U2W1Rev.csv', '5'), 'place-largest-fixed-digit'), (('worksheets/Grade 2/G2Unit 2/G2U2W2.csv', '1'), 'number-place-value-expanded-form'), (('worksheets/Grade 2/G2Unit 2/G2U2W2.csv', '2'), 'number-place-value-expanded-form'), (('worksheets/Grade 2/G2Unit 2/G2U2W2.csv', '3'), 'number-place-value-expanded-form'), (('worksheets/Grade 2/G2Unit 2/G2U2W2.csv', '4'), 'number-place-value-expanded-form'), (('worksheets/Grade 2/G2Unit 2/G2U2W2HW.csv', '2'), 'order-arrange-digits'), (('worksheets/Grade 2/G2Unit 2/G2U2W2HW.csv', '3'), 'place-largest-fixed-digit'), (('worksheets/Grade 2/G2Unit 2/G2U2W2HW.csv', '5'), 'place-zero-placeholder'), (('worksheets/Grade 2/G2Unit 2/G2U2W2Rev.csv', '1'), 'number-place-value-expanded-form'), (('worksheets/Grade 2/G2Unit 2/G2U2W2Rev.csv', '3'), 'order-arrange-digits'), (('worksheets/Grade 2/G2Unit 2/G2U2W2Rev.csv', '4'), 'order-arrange-digits'), (('worksheets/Grade 2/G2Unit 2/G2U2W2Rev.csv', '5'), 'place-zero-placeholder'), (('worksheets/Grade 2/G2Unit 2/G2U2W3.csv', '1'), 'place-convert-adjacent-units'), (('worksheets/Grade 2/G2Unit 2/G2U2W3.csv', '2'), 'place-convert-adjacent-units'), (('worksheets/Grade 2/G2Unit 2/G2U2W3.csv', '3'), 'place-convert-adjacent-units'), (('worksheets/Grade 2/G2Unit 2/G2U2W3.csv', '4'), 'place-convert-adjacent-units'), (('worksheets/Grade 2/G2Unit 2/G2U2W3.csv', '5'), 'place-regroup-extra-small-units'), (('worksheets/Grade 2/G2Unit 2/G2U2W3.csv', '6'), 'place-regroup-extra-small-units'), (('worksheets/Grade 2/G2Unit 2/G2U2W3.csv', '7'), 'place-regroup-extra-small-units'), (('worksheets/Grade 2/G2Unit 2/G2U2W3.csv', '8'), 'place-regroup-extra-small-units'), (('worksheets/Grade 2/G2Unit 2/G2U2W3.csv', '9'), 'place-find-missing-unit-count'), (('worksheets/Grade 2/G2Unit 2/G2U2W3Rev.csv', '1'), 'number-place-value-expanded-form'), (('worksheets/Grade 2/G2Unit 2/G2U2W4.csv', '6'), 'place-compare-two-digit'), (('worksheets/Grade 2/G2Unit 2/G2U2W4.csv', '7'), 'place-compare-three-digit-forms'), (('worksheets/Grade 2/G2Unit 2/G2U2W4.csv', '8'), 'place-compare-three-digit-forms'), (('worksheets/Grade 2/G2Unit 2/G2U2W4.csv', '9'), 'place-compare-three-digit-forms'), (('worksheets/Grade 2/G2Unit 2/G2U2W4.csv', '10'), 'place-compare-after-regrouping'), (('worksheets/Grade 2/G2Unit 2/G2U2W4HW.csv', '1'), 'place-regroup-multiple-places'), (('worksheets/Grade 2/G2Unit 2/G2U2W4HW.csv', '3'), 'place-find-missing-unit-count'), (('worksheets/Grade 2/G2Unit 2/G2U2W4Rev.csv', '1'), 'place-regroup-extra-small-units'), (('worksheets/Grade 2/G2Unit 2/G2U2W4Rev.csv', '2'), 'place-find-missing-unit-count'), (('worksheets/Grade 2/G2Unit 2/G2U2W4Rev.csv', '3'), 'place-find-missing-unit-count'), (('worksheets/Grade 2/G2Unit 2/G2U2W4Rev.csv', '4'), 'place-regroup-multiple-places'), (('worksheets/Grade 2/G2Unit 2/G2U2W4Rev.csv', '5'), 'place-complete-hundred-groups'), (('worksheets/Grade 2/G2Unit 2/G2U2W5HW.csv', '1'), 'place-compare-after-regrouping'), (('worksheets/Grade 2/G2Unit 2/G2U2W5HW.csv', '2'), 'place-compare-three-digit-forms'), (('worksheets/Grade 2/G2Unit 2/G2U2W5Rev.csv', '4'), 'place-compare-three-digit-forms'), (('worksheets/Grade 2/G2Unit 2/G2U2W5Rev.csv', '5'), 'place-compare-three-digit-forms'), (('worksheets/Grade 2/G2Unit 2/G2U2W1.csv', '5'), 'place-digit-value-small'), (('worksheets/Grade 2/G2Unit 2/G2U2W1.csv', '6'), 'place-digit-value-small'), (('worksheets/Grade 2/G2Unit 2/G2U2W1.csv', '7'), 'place-digit-value-small'), (('worksheets/Grade 2/G2Unit 2/G2U2W1Rev.csv', '3'), 'place-digit-value-small'), (('worksheets/Grade 2/G2Unit 2/G2U2W2HW.csv', '1'), 'place-digit-value-small'), (('worksheets/Grade 2/G2Unit 2/G2U2W2HW.csv', '4'), 'place-digit-value-small'), (('worksheets/Grade 2/G2Unit 2/G2U2W2Rev.csv', '2'), 'place-digit-value-small'), (('worksheets/Grade 2/G2Unit 2/G2U2W1HW.csv', '1'), 'arithmetic-small-story-changes'), (('worksheets/Grade 2/G2Unit 2/G2U2W1HW.csv', '2'), 'arithmetic-small-story-changes'), (('worksheets/Grade 2/G2Unit 2/G2U2W1HW.csv', '3'), 'arithmetic-small-story-changes'), (('worksheets/Grade 2/G2Unit 2/G2U2W1HW.csv', '4'), 'arithmetic-work-backwards-small'), (('worksheets/Grade 2/G2Unit 2/G2U2W1HW.csv', '5'), 'arithmetic-work-backwards-small'), (('worksheets/Grade 2/G2Unit 2/G2U2W2.csv', '5'), 'place-three-digit-word-forms'), (('worksheets/Grade 2/G2Unit 2/G2U2W2.csv', '6'), 'place-three-digit-word-forms'), (('worksheets/Grade 2/G2Unit 2/G2U2W2.csv', '7'), 'place-three-digit-word-forms'), (('worksheets/Grade 2/G2Unit 2/G2U2W2.csv', '8'), 'place-three-digit-word-forms'), (('worksheets/Grade 2/G2Unit 2/G2U2W2.csv', '9'), 'place-three-digit-word-forms'), (('worksheets/Grade 2/G2Unit 2/G2U2W2.csv', '10'), 'place-three-digit-word-forms'), (('worksheets/Grade 2/G2Unit 2/G2U2W3HW.csv', '1'), 'place-three-digit-word-forms'), (('worksheets/Grade 2/G2Unit 2/G2U2W3HW.csv', '3'), 'place-three-digit-word-forms'), (('worksheets/Grade 2/G2Unit 2/G2U2W3Rev.csv', '2'), 'place-three-digit-word-forms'), (('worksheets/Grade 2/G2Unit 2/G2U2W3Rev.csv', '3'), 'place-three-digit-word-forms'), (('worksheets/Grade 2/G2Unit 2/G2U2W3.csv', '10'), 'place-equivalent-sums-small'), (('worksheets/Grade 2/G2Unit 2/G2U2W3Rev.csv', '4'), 'place-equivalent-sums-small'), (('worksheets/Grade 2/G2Unit 2/G2U2W4HW.csv', '4'), 'place-equivalent-sums-small'), (('worksheets/Grade 2/G2Unit 2/G2U2W4HW.csv', '5'), 'place-equivalent-sums-small'), (('worksheets/Grade 2/G2Unit 2/G2U2W3HW.csv', '2'), 'place-four-digit-expanded-small'), (('worksheets/Grade 2/G2Unit 2/G2U2W3Rev.csv', '5'), 'place-four-digit-expanded-small'), (('worksheets/Grade 2/G2Unit 2/G2U2W3HW.csv', '4'), 'place-compare-three-digit-forms'), (('worksheets/Grade 2/G2Unit 2/G2U2W3HW.csv', '5'), 'number-place-value-expanded-form'), (('worksheets/Grade 2/G2Unit 2/G2U2W4.csv', '1'), 'order-number-line-direction'), (('worksheets/Grade 2/G2Unit 2/G2U2W4.csv', '2'), 'place-compare-two-digit'), (('worksheets/Grade 2/G2Unit 2/G2U2W4.csv', '3'), 'place-compare-two-digit'), (('worksheets/Grade 2/G2Unit 2/G2U2W4.csv', '4'), 'place-compare-three-digit-forms'), (('worksheets/Grade 2/G2Unit 2/G2U2W4.csv', '5'), 'place-compare-three-digit-forms'), (('worksheets/Grade 2/G2Unit 2/G2U2W4HW.csv', '2'), 'place-regroup-multiple-places'), (('worksheets/Grade 2/G2Unit 2/G2U2W5.csv', '1'), 'parity-pair-object-groups'), (('worksheets/Grade 2/G2Unit 2/G2U2W5.csv', '2'), 'parity-pair-object-groups'), (('worksheets/Grade 2/G2Unit 2/G2U2W5.csv', '3'), 'parity-pair-object-groups'), (('worksheets/Grade 2/G2Unit 2/G2U2W5.csv', '4'), 'parity-pair-object-groups'), (('worksheets/Grade 2/G2Unit 2/G2U2W5.csv', '5'), 'parity-pair-object-groups'), (('worksheets/Grade 2/G2Unit 2/G2U2W5.csv', '6'), 'parity-pair-object-groups'), (('worksheets/Grade 2/G2Unit 2/G2U2W5.csv', '7'), 'parity-pair-object-groups'), (('worksheets/Grade 2/G2Unit 2/G2U2W5.csv', '8'), 'parity-pair-object-groups'), (('worksheets/Grade 2/G2Unit 2/G2U2W6HW.csv', '4'), 'parity-pair-object-groups'), (('worksheets/Grade 2/G2Unit 2/G2U2W6Rev.csv', '1'), 'parity-pair-object-groups'), (('worksheets/Grade 2/G2Unit 2/G2U2W6Rev.csv', '2'), 'parity-pair-object-groups'), (('worksheets/Grade 2/G2Unit 2/G2U2W6Rev.csv', '4'), 'parity-pair-object-groups'), (('worksheets/Grade 2/G2Unit 2/G2U2W5.csv', '9'), 'parity-next-even-odd-sequences'), (('worksheets/Grade 2/G2Unit 2/G2U2W6HW.csv', '2'), 'parity-next-even-odd-sequences'), (('worksheets/Grade 2/G2Unit 2/G2U2W6HW.csv', '3'), 'parity-next-even-odd-sequences'), (('worksheets/Grade 2/G2Unit 2/G2U2W6Rev.csv', '3'), 'parity-next-even-odd-sequences'), (('worksheets/Grade 2/G2Unit 2/G2U2W6Rev.csv', '5'), 'parity-next-even-odd-sequences'), (('worksheets/Grade 2/G2Unit 2/G2U2W5.csv', '10'), 'parity-total-after-addition'), (('worksheets/Grade 2/G2Unit 2/G2U2W6HW.csv', '5'), 'parity-total-after-addition'), (('worksheets/Grade 2/G2Unit 2/G2U2W6HW.csv', '1'), 'parity-last-digit-small'), (('worksheets/Grade 2/G2Unit 2/G2U2W5HW.csv', '3'), 'order-largest-with-ties'), (('worksheets/Grade 2/G2Unit 2/G2U2W5HW.csv', '4'), 'order-largest-with-ties'), (('worksheets/Grade 2/G2Unit 2/G2U2W5HW.csv', '5'), 'place-compare-three-digit-forms'), (('worksheets/Grade 2/G2Unit 2/G2U2W5Rev.csv', '1'), 'place-compare-three-digit-forms'), (('worksheets/Grade 2/G2Unit 2/G2U2W5Rev.csv', '2'), 'place-compare-three-digit-forms'), (('worksheets/Grade 2/G2Unit 2/G2U2W5Rev.csv', '3'), 'place-compare-three-digit-forms'), (('worksheets/Grade 2/G2Unit 2/G2U2W6.csv', '1'), 'count-fives-from-any-start'), (('worksheets/Grade 2/G2Unit 2/G2U2W6.csv', '2'), 'count-fives-from-any-start'), (('worksheets/Grade 2/G2Unit 2/G2U2W6.csv', '4'), 'count-fives-from-any-start'), (('worksheets/Grade 2/G2Unit 2/G2U2W6.csv', '9'), 'count-fives-from-any-start'), (('worksheets/Grade 2/G2Unit 2/G2U2W6.csv', '3'), 'count-fives-both-directions'), (('worksheets/Grade 2/G2Unit 2/G2U2W6.csv', '8'), 'count-fives-both-directions'), (('worksheets/Grade 2/G2Unit 2/G2U2W6.csv', '5'), 'place-add-one-ten'), (('worksheets/Grade 2/G2Unit 2/G2U2W6.csv', '6'), 'count-hundreds-pattern'), (('worksheets/Grade 2/G2Unit 2/G2U2W6.csv', '10'), 'count-hundreds-pattern'), (('worksheets/Grade 2/G2Unit 2/G2U2W6.csv', '7'), 'place-cross-hundred-ten')]
assert len(APPROVED)==len(set(ref for ref,vid in APPROVED))
MERGES=[]
SOURCE_NOTES={}
REVIEW_NOTES={('worksheets/Grade 2/G2Unit 2/G2U2W5.csv', '1'): 'Source image opened and visually checked in the in-app browser on 2026-10-09. Four rabbits, all pairable; Yes/even key correct.', ('worksheets/Grade 2/G2Unit 2/G2U2W5.csv', '2'): 'Source image opened and visually checked in the in-app browser on 2026-10-09. Nine basketballs, one unpaired; Yes/odd key correct.', ('worksheets/Grade 2/G2Unit 2/G2U2W5.csv', '3'): 'Source image opened and visually checked in the in-app browser on 2026-10-09. A has three caps, B two, C five; B is the only even count.', ('worksheets/Grade 2/G2Unit 2/G2U2W5.csv', '4'): 'Source image opened and visually checked in the in-app browser on 2026-10-09. A has six caps, B eight, C five; C is the only odd count.', ('worksheets/Grade 2/G2Unit 2/G2U2W5.csv', '8'): 'Source image opened and visually checked in the in-app browser on 2026-10-09. A has six caps, B ten, C fourteen; all three are even.'}
VISUAL_REFS={('worksheets/Grade 2/G2Unit 2/G2U2W5.csv', '2'), ('worksheets/Grade 2/G2Unit 2/G2U2W5.csv', '8'), ('worksheets/Grade 2/G2Unit 2/G2U2W5.csv', '4'), ('worksheets/Grade 2/G2Unit 2/G2U2W5.csv', '3'), ('worksheets/Grade 2/G2Unit 2/G2U2W5.csv', '1')}


def apply_review(doc,merge=False):
    # A reviewed mapping requires the exact audited answer/solution row.
    root=Path(__file__).resolve().parents[1]
    audit=json.loads((root/'videos/grade-2-unit-2-source-corrections-2026-10-09.json').read_text())
    expected={(r['worksheet'],r['question_id']):r['after'] for r in audit['changes']}
    current={}
    for file,qid in expected:
        if file not in current:
            with (root/file).open(encoding='utf-8-sig',newline='') as f:current[file]={r['Question ID']:r for r in csv.DictReader(f)}
        assert current[file][qid]==expected[(file,qid)],('Source changed since answer/solution audit',file,qid)
    assert len(expected)==120
    changes=[];reviewed=0
    for s in SPECS:
        vid=s['video_id'];title=s['topic']
        if vid not in doc['videos']:
            doc['videos'][vid]={'title':title,'question_type':title,'curriculum':{'kind':'shared','topic':'number'},
             'production_status':'planned','target_duration_seconds':60,'duration_seconds':None,'example':None,
             'assets':{'mp4':None,'captions':None},'youtube':{'video_id':None,'visibility':None},
             'notes':'Distinct early parity method identified through explicit question review.',
             'planning':{'basis':'rule','rule':vid,'review_status':'needs_review'}}
    for (file,qid),vid in sorted(set(APPROVED)):
        p=doc['worksheets'][file]['problems'][qid]
        assert len(p['video_links'])==1,(file,qid)
        # Preserve the dependence on source figures that were actually inspected.
        p['requires_source_visual']=(file,qid) in VISUAL_REFS
        old=p['video_links'][0]['video_id']
        if old!=vid:changes.append((file,qid,old,vid));p['video_links'][0]['video_id']=vid
        reviewed+=p['mapping_status']!='reviewed'
        p.update(mapping_method='manual',mapping_status='reviewed',mapping_rule='early-parity-review-1',
          notes='Worksheet answer, choices, hints and complete worked solution independently reviewed; corrections recorded in grade-2-unit-2-source-corrections-2026-10-09.json. Linked video teaches the matching method using different numerical inputs.' + (' ' + REVIEW_NOTES[(file,qid)] if (file,qid) in REVIEW_NOTES else ''))
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
