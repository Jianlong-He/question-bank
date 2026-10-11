"""Explicitly reviewed core percentage mappings and unresolved source issues."""
import argparse,fcntl,json
from pathlib import Path
from percent_core_lessons import SPECS,lessons
from number_sense_lessons import source as g
from video_reuse import append_upload_row,update_reuse_checklist,merge_reviewed_duplicate
from build_video_correspondence import validate,read_inventory
from generate_video_batch import save_json,update_overview
from video_example_checks import require_analogous_examples

APPROVED=[]
ASSIGNMENTS = """percent-hundred-grid 6 3 2 1,2
percent-hundred-grid 6 3 2HW 1,2
percent-wholes-and-hundredths 6 3 2 3,4,9
percent-wholes-and-hundredths 6 3 2HW 3
percent-wholes-and-hundredths 6 3 2Rev 1,4
percent-problems 6 3 2 5,6,10
percent-problems 6 3 2HW 4,5
percent-problems 6 3 2Rev 5
percent-problems 6 3 3 1,2,3,4
percent-problems 6 3 3HW 1,2,3,4
percent-problems 6 3 5 5,7
percent-problems 6 3 5HW 3,4
percent-problems 6 3 5Rev 3
percent-problems 7 2 1 10
percent-problems 7 2 1Rev 5
percent-problems 7 2 2 5,10
percent-problems 7 2 2HW 4
percent-problems 7 2 2Rev 4
percent-problems 7 2 3 4,6
percent-problems 7 2 3HW 3,4
percent-problems 7 2 4 4,5
percent-problems 7 2 4HW 3,4
percent-problems 7 2 5 4,6
percent-problems 7 2 5HW 3,4
percent-problems 9 11 1 5
percent-problems 9 11 1HW 5
percent-problems 9 11 1Rev 4
percent-of-quantity 6 3 3 8
percent-of-quantity 6 3 3HW 5
percent-of-quantity 6 3 4 1,2,3,4,5,7
percent-of-quantity 6 3 4HW 1,2,3,5
percent-of-quantity 6 3 4Rev 1,2
percent-of-quantity 6 3 5 3
percent-of-quantity 6 3 5HW 1,2
percent-of-quantity 6 3 5Rev 2
percent-of-quantity 7 2 1 9
percent-of-quantity 7 2 1Rev 4
percent-of-quantity 7 2 2 4
percent-of-quantity 7 2 2HW 3
percent-of-quantity 7 2 3 3
percent-of-quantity 7 2 3HW 2
percent-of-quantity 7 2 4 3
percent-of-quantity 7 2 4HW 2
percent-of-quantity 7 2 5 3
percent-of-quantity 7 2 5HW 2
percent-less-than-one 6 3 5 2
percent-less-than-one 6 3 5Rev 1
percent-find-whole 6 3 3 5,7,10
percent-find-whole 6 3 3Rev 1,2,4,5
percent-find-whole 6 3 4 9
percent-find-whole 6 3 4Rev 4
percent-find-whole 6 3 5 9
percent-find-whole 6 3 5HW 5
percent-find-whole 7 2 3 8,10
percent-find-whole 7 2 3HW 5
percent-find-whole 7 2 3Rev 5
percent-find-whole 7 2 4 8,10
percent-find-whole 7 2 4HW 5
percent-find-whole 7 2 4Rev 5
percent-find-whole 7 2 5 10
percent-find-whole 7 2 5Rev 5
percent-compare-groups 6 3 3 9
percent-compare-groups 6 3 3Rev 3
percent-ratio-above-one-hundred 6 3 5 8
percent-ratio-above-one-hundred 6 3 5Rev 4
percent-reverse-increase 7 2 2 8
percent-reverse-increase 7 2 2Rev 2
percent-tip-and-total 7 2 3 9
percent-tip-and-total 7 2 3Rev 4
percent-fixed-rate-time-intervals 7 2 3 7
percent-fixed-rate-time-intervals 7 2 3Rev 2
statistics-box-plot-summary 6 11 9 3
"""
for row in ASSIGNMENTS.splitlines():
    vid,grade,unit,w,qs=row.split()
    APPROVED.extend((g(int(grade),int(unit),w,q),vid) for q in qs.split(','))
assert len(APPROVED)==len(set(ref for ref,vid in APPROVED))
MERGES=[]
SOURCE_NOTES={
 g(6,3,3,6):'Source solution error: final arithmetic prints 150 / 0.16 but the correct divisor is 1.6. The stated answer 93.75 is correct for 150 / 1.6. Leave pending until the explanation is corrected; source unchanged.',
 g(6,3,5,1):'Source solution typo: the fraction method prints (1/100) times 8.76, but it must multiply 876. Answer 8.76 is correct. Leave pending; source unchanged.',
 g(6,3,5,4):'Source solution typo: explanation starts with 148 although the answer and subsequent work are 48. Leave pending; source unchanged.',
 g(6,3,5,6):'Source solution typo: explanation starts with fraction 5/30 although the question and subsequent work use 6/30. Answer 20 percent is correct. Leave pending; source unchanged.',
 g(7,2,2,7):'Source CSV parsing error: question is cut off after the dollar9 reduction; the answer field contains the rest of the question instead of the answer. Repair source quoting before approving the mapping; source unchanged.',
 g(6,11,8,7):'Source visual missing: the numerical interval alone does not identify Q1 and Q3. The referenced box plot is needed to verify the keyed 50 percent. Left pending; source unchanged.'}
for w,q in [('2',8),('2Rev',3)]:
    SOURCE_NOTES[g(6,3,w,q)]='Source reference-whole ambiguity: percentages in the key use one grid as 100 percent, while the wording can refer to the combined two grids. State the reference whole explicitly. Left pending; source unchanged.'
for w,q in [('4',7),('4Rev',3)]:
    SOURCE_NOTES[g(7,2,w,q)]='Source changing-base ambiguity: the plant grows by a percentage of its total height each interval, but the key adds fixed percentages. Specify a fixed reference height to exclude compounding. Left pending; source unchanged.'
for w,q in [('5',8),('5HW',5)]:
    SOURCE_NOTES[g(7,2,w,q)]='Source initial-amount ambiguity: the tank reaches its stated percentage after adding the stated volume, but is not stated to be initially empty. The key equates added volume with final contents. Specify the initial amount; left pending, source unchanged.'
REVIEW_NOTES={}


def apply_review(doc,merge=False):
    changes=[];reviewed=0
    for s in SPECS:
        vid=s['video_id'];title=s['topic']
        if vid not in doc['videos']:
            doc['videos'][vid]={'title':title,'question_type':title,'curriculum':{'kind':'shared','topic':'percentages'},
             'production_status':'planned','target_duration_seconds':60,'duration_seconds':None,'example':None,
             'assets':{'mp4':None,'captions':None},'youtube':{'video_id':None,'visibility':None},
             'notes':'Distinct core percentage method identified through explicit question review.',
             'planning':{'basis':'rule','rule':vid,'review_status':'needs_review'}}
    for (file,qid),vid in sorted(set(APPROVED)):
        p=doc['worksheets'][file]['problems'][qid]
        assert len(p['video_links'])==1,(file,qid)
        # All approved questions are self-contained; no figure is needed.
        p['requires_source_visual']=False
        old=p['video_links'][0]['video_id']
        if old!=vid:changes.append((file,qid,old,vid));p['video_links'][0]['video_id']=vid
        reviewed+=p['mapping_status']!='reviewed'
        p.update(mapping_method='manual',mapping_status='reviewed',mapping_rule='percent-core-review-1',
          notes='Inspected against the authored analogous example: matching core percentage method and prerequisite steps; different numerical inputs.' + (' ' + REVIEW_NOTES[(file,qid)] if (file,qid) in REVIEW_NOTES else ''))
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
