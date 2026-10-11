"""Explicitly reviewed early measurement mappings and unresolved source issues."""
import argparse,fcntl,json
from pathlib import Path
from early_measurement_lessons import SPECS,lessons
from number_sense_lessons import source as g
from video_reuse import append_upload_row,update_reuse_checklist,merge_reviewed_duplicate
from build_video_correspondence import validate,read_inventory
from generate_video_batch import save_json,update_overview
from video_example_checks import require_analogous_examples

APPROVED=[(('worksheets/Grade 1/G1Unit 3/G1U3W1.csv', '1'), 'measure-touching-unit-blocks'), (('worksheets/Grade 1/G1Unit 3/G1U3W1.csv', '10'), 'measure-touching-unit-blocks'), (('worksheets/Grade 1/G1Unit 3/G1U3W1.csv', '3'), 'measure-compare-unit-heights'), (('worksheets/Grade 1/G1Unit 3/G1U3W1.csv', '4'), 'measure-compare-unit-heights'), (('worksheets/Grade 1/G1Unit 3/G1U3W1.csv', '6'), 'measure-compare-unit-heights'), (('worksheets/Grade 1/G1Unit 3/G1U3W1.csv', '8'), 'measure-compare-unit-heights'), (('worksheets/Grade 1/G1Unit 3/G1U3W1.csv', '9'), 'measure-compare-unit-heights'), (('worksheets/Grade 1/G1Unit 3/G1U3W1.csv', '7'), 'g1-u1-counting-forward'), (('worksheets/Grade 1/G1Unit 3/G1U3W2.csv', '1'), 'data-read-small-bar-chart'), (('worksheets/Grade 1/G1Unit 3/G1U3W2.csv', '2'), 'data-read-small-bar-chart'), (('worksheets/Grade 1/G1Unit 3/G1U3W2.csv', '3'), 'data-read-small-bar-chart'), (('worksheets/Grade 1/G1Unit 3/G1U3W2.csv', '4'), 'data-read-small-bar-chart'), (('worksheets/Grade 1/G1Unit 3/G1U3W2.csv', '6'), 'data-read-small-bar-chart'), (('worksheets/Grade 1/G1Unit 3/G1U3W2.csv', '7'), 'data-read-small-bar-chart'), (('worksheets/Grade 1/G1Unit 3/G1U3W2.csv', '9'), 'data-read-small-bar-chart'), (('worksheets/Grade 1/G1Unit 3/G1U3W2.csv', '5'), 'data-combine-compare-chart-values'), (('worksheets/Grade 1/G1Unit 3/G1U3W2.csv', '8'), 'data-combine-compare-chart-values'), (('worksheets/Grade 1/G1Unit 3/G1U3W2.csv', '10'), 'data-combine-compare-chart-values'), (('worksheets/Grade 1/G1Unit 3/G1U3W3.csv', '1'), 'time-read-analogue-early'), (('worksheets/Grade 1/G1Unit 3/G1U3W3.csv', '2'), 'time-read-analogue-early'), (('worksheets/Grade 1/G1Unit 3/G1U3W3.csv', '3'), 'time-read-analogue-early'), (('worksheets/Grade 1/G1Unit 3/G1U3W3.csv', '4'), 'time-read-analogue-early'), (('worksheets/Grade 1/G1Unit 3/G1U3W3.csv', '5'), 'time-read-analogue-early'), (('worksheets/Grade 1/G1Unit 3/G1U3W3.csv', '9'), 'time-read-analogue-early'), (('worksheets/Grade 1/G1Unit 3/G1U3W3.csv', '10'), 'time-read-analogue-early'), (('worksheets/Grade 1/G1Unit 3/G1U3W3.csv', '12'), 'time-read-analogue-early'), (('worksheets/Grade 1/G1Unit 3/G1U3W3.csv', '6'), 'time-read-oclock-early'), (('worksheets/Grade 1/G1Unit 3/G1U3W3.csv', '11'), 'time-read-oclock-early'), (('worksheets/Grade 1/G1Unit 3/G1U3W3.csv', '13'), 'time-read-oclock-early'), (('worksheets/Grade 1/G1Unit 3/G1U3W3.csv', '7'), 'time-digital-minutes-past'), (('worksheets/Grade 1/G1Unit 3/G1U3W3.csv', '8'), 'time-digital-minutes-past'), (('worksheets/Grade 1/G1Unit 3/G1U3W4.csv', '1'), 'calendar-neighbouring-weekdays'), (('worksheets/Grade 1/G1Unit 3/G1U3W4.csv', '2'), 'calendar-neighbouring-weekdays'), (('worksheets/Grade 1/G1Unit 3/G1U3W4.csv', '3'), 'calendar-neighbouring-weekdays'), (('worksheets/Grade 1/G1Unit 3/G1U3W4.csv', '9'), 'calendar-neighbouring-weekdays'), (('worksheets/Grade 1/G1Unit 3/G1U3W4.csv', '4'), 'calendar-season-cycle'), (('worksheets/Grade 1/G1Unit 3/G1U3W4.csv', '5'), 'calendar-season-cycle'), (('worksheets/Grade 1/G1Unit 3/G1U3W4.csv', '6'), 'calendar-neighbouring-months'), (('worksheets/Grade 1/G1Unit 3/G1U3W4.csv', '7'), 'calendar-neighbouring-months'), (('worksheets/Grade 1/G1Unit 3/G1U3W4.csv', '8'), 'calendar-weeks-plus-days'), (('worksheets/Grade 1/G1Unit 3/G1U3W4.csv', '10'), 'calendar-weeks-plus-days'), (('worksheets/Grade 1/G1Unit 3/G1U3W4.csv', '11'), 'calendar-month-lengths'), (('worksheets/Grade 1/G1Unit 3/G1U3W5.csv', '1'), 'geometry-count-polygon-features'), (('worksheets/Grade 1/G1Unit 3/G1U3W5.csv', '3'), 'geometry-count-polygon-features'), (('worksheets/Grade 1/G1Unit 3/G1U3W5.csv', '6'), 'geometry-count-polygon-features'), (('worksheets/Grade 1/G1Unit 3/G1U3W5.csv', '7'), 'geometry-count-polygon-features'), (('worksheets/Grade 1/G1Unit 3/G1U3W6.csv', '8'), 'geometry-count-polygon-features'), (('worksheets/Grade 1/G1Unit 3/G1U3W5.csv', '2'), 'shape-square-properties-early'), (('worksheets/Grade 1/G1Unit 3/G1U3W5.csv', '8'), 'shape-square-properties-early'), (('worksheets/Grade 1/G1Unit 3/G1U3W5.csv', '10'), 'shape-square-properties-early'), (('worksheets/Grade 1/G1Unit 3/G1U3W6.csv', '10'), 'shape-square-properties-early'), (('worksheets/Grade 1/G1Unit 3/G1U3W5.csv', '4'), 'shape-round-and-straight'), (('worksheets/Grade 1/G1Unit 3/G1U3W5.csv', '5'), 'shape-round-and-straight'), (('worksheets/Grade 1/G1Unit 3/G1U3W5.csv', '9'), 'shape-round-and-straight'), (('worksheets/Grade 1/G1Unit 3/G1U3W6.csv', '1'), 'shape-round-and-straight'), (('worksheets/Grade 1/G1Unit 3/G1U3W6.csv', '3'), 'shape-round-and-straight'), (('worksheets/Grade 1/G1Unit 3/G1U3W6.csv', '4'), 'shape-round-and-straight'), (('worksheets/Grade 1/G1Unit 3/G1U3W6.csv', '6'), 'shape-rhombus-trapezoid-early'), (('worksheets/Grade 1/G1Unit 3/G1U3W6.csv', '7'), 'shape-rhombus-trapezoid-early'), (('worksheets/Grade 1/G1Unit 3/G1U3W7.csv', '1'), 'fractions-name-equal-parts'), (('worksheets/Grade 1/G1Unit 3/G1U3W7.csv', '2'), 'fractions-name-equal-parts'), (('worksheets/Grade 1/G1Unit 3/G1U3W7.csv', '3'), 'fractions-name-equal-parts'), (('worksheets/Grade 1/G1Unit 3/G1U3W7.csv', '4'), 'fractions-name-equal-parts'), (('worksheets/Grade 1/G1Unit 3/G1U3W7.csv', '8'), 'fractions-name-equal-parts'), (('worksheets/Grade 1/G1Unit 3/G1U3W7.csv', '9'), 'fractions-name-equal-parts'), (('worksheets/Grade 1/G1Unit 3/G1U3W7.csv', '6'), 'fractions-equal-size-check'), (('worksheets/Grade 1/G1Unit 3/G1U3W7.csv', '7'), 'fractions-equal-size-check')]
assert len(APPROVED)==len(set(ref for ref,vid in APPROVED))
MERGES=[]
SOURCE_NOTES={('worksheets/Grade 1/G1Unit 3/G1U3W1.csv', '2'): 'Source image/key mismatch: inspected the linked dragon image in the browser on 2026-10-08. Its measurement row has 8 front-facing unit blocks, but the accepted answer is 7. Review the picture or change the key to 8. Left pending; source unchanged.', ('worksheets/Grade 1/G1Unit 3/G1U3W1.csv', '5'): 'Source image/key mismatch: inspected the linked line diagram in the browser on 2026-10-08. B is longest, A is intermediate, and C is shortest. The key C,A,B reverses the requested longest-to-shortest order. Left pending; source unchanged.', ('worksheets/Grade 1/G1Unit 3/G1U3W6.csv', '2'): 'Source choice ambiguity: the linked picture is an upright square (verified in the browser on 2026-10-08), so both Square and Rectangle are mathematically true, as worksheet Q9 itself recognizes. Ask for the most specific name or accept both classifications. Left pending; source unchanged.'}
REVIEW_NOTES={}
VISUAL_REFS={(f'worksheets/Grade 1/G1Unit 3/G1U3W{w}.csv',str(q)) for w,qs in [(1,[1]),(2,list(range(1,11))),(5,[1,4,5,6,8]),(6,[1,3,6,7]),(7,[1,2,3])] for q in qs}
for ref in VISUAL_REFS:
    REVIEW_NOTES[ref]='Source image opened and visually checked in the browser on 2026-10-08; see grade-1-source-visual-review.md. Original example diagram uses different data or geometry.'
REVIEW_NOTES[('worksheets/Grade 1/G1Unit 3/G1U3W5.csv','9')]='The illustrated circle has no straight sides or corners; this mapping uses the worksheet’s elementary straight-side convention.'



def apply_review(doc,merge=False):
    changes=[];reviewed=0
    for s in SPECS:
        vid=s['video_id'];title=s['topic']
        if vid not in doc['videos']:
            doc['videos'][vid]={'title':title,'question_type':title,'curriculum':{'kind':'shared','topic':'number'},
             'production_status':'planned','target_duration_seconds':60,'duration_seconds':None,'example':None,
             'assets':{'mp4':None,'captions':None},'youtube':{'video_id':None,'visibility':None},
             'notes':'Distinct early measurement method identified through explicit question review.',
             'planning':{'basis':'rule','rule':vid,'review_status':'needs_review'}}
    for (file,qid),vid in sorted(set(APPROVED)):
        p=doc['worksheets'][file]['problems'][qid]
        assert len(p['video_links'])==1,(file,qid)
        # All approved questions are self-contained; no figure is needed.
        p['requires_source_visual']=(file,qid) in VISUAL_REFS
        old=p['video_links'][0]['video_id']
        if old!=vid:changes.append((file,qid,old,vid));p['video_links'][0]['video_id']=vid
        reviewed+=p['mapping_status']!='reviewed'
        p.update(mapping_method='manual',mapping_status='reviewed',mapping_rule='early-measurement-review-1',
          notes='Inspected against the authored analogous example: matching early measurement method and prerequisite steps; different numerical inputs.' + (' ' + REVIEW_NOTES[(file,qid)] if (file,qid) in REVIEW_NOTES else ''))
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
