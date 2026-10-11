"""Explicitly reviewed congruence mappings and unresolved source issues."""
import argparse,fcntl,json
from pathlib import Path
from congruence_lessons import SPECS,lessons
from number_sense_lessons import source as g
from video_reuse import append_upload_row,update_reuse_checklist,merge_reviewed_duplicate
from build_video_correspondence import validate,read_inventory
from generate_video_batch import save_json,update_overview
from video_example_checks import require_analogous_examples

APPROVED=[]
ASSIGNMENTS = """geometry-congruence-sas 9 17 1 6
geometry-congruence-sas 9 17 5 6
geometry-congruence-corresponding-parts 9 17 2 2
geometry-congruence-corresponding-parts 9 17 2HW 2
geometry-congruence-corresponding-parts 9 17 2Rev 2
geometry-congruence-hypotenuse-leg 9 17 1 10
geometry-congruence-hypotenuse-leg 9 17 2 10
geometry-angle-bisector-halves 9 17 5 9
geometry-congruence 9 17 1 3,4
geometry-congruence 9 17 1HW 3,4
geometry-congruence 9 17 1Rev 2,3
geometry-congruence-corresponding-parts 8 6 6 9
geometry-congruence-corresponding-parts 8 6 6Rev 4
geometry-congruence-corresponding-parts 9 17 2 3,4,8,9
geometry-congruence-corresponding-parts 9 17 2HW 3,4
geometry-congruence-corresponding-parts 9 17 2Rev 3
geometry-congruence-corresponding-parts 9 17 5 7,10
geometry-congruence-corresponding-parts 9 17 5Rev 5
geometry-congruence-sss 9 17 1 5
geometry-congruence-sss 9 17 2 7
geometry-congruence-sss 9 17 2Rev 4
geometry-congruence-sas 9 17 2 5
geometry-congruence-sas 9 17 2HW 5
geometry-congruence-asa 9 17 1 7
geometry-congruence-asa 9 17 2 6
geometry-congruence-asa 9 17 2Rev 5
geometry-congruence-asa 10 8 1 4
geometry-congruence-asa 10 8 1HW 3
geometry-congruence-aas 9 17 1 8
geometry-congruence-ssa-ambiguity 9 17 1 9
geometry-congruence-parallelogram-diagonal 9 17 4 4
geometry-congruence-parallelogram-diagonal 9 17 4Rev 1
geometry-congruence-rigid-area 9 16 1 3
geometry-congruence-rigid-area 9 16 1HW 3
geometry-translation-rigid-properties 8 6 7 2,3
geometry-translation-rigid-properties 8 6 7HW 2
geometry-translation-rigid-properties 8 6 7Rev 1
geometry-translation-rigid-properties 9 15 1 10
geometry-translation-rigid-properties 9 16 1 1,2,9
geometry-translation-rigid-properties 9 16 1HW 1,2
geometry-translation-rigid-properties 9 17 1 1
geometry-translation-rigid-properties 9 17 1HW 1
geometry-vertical-angle-equation-one-side 9 16 3 7
geometry-vertical-angle-equation-one-side 9 17 5 2
geometry-vertical-angle-equation-one-side 9 17 5HW 2
geometry-isosceles-base-angles 9 17 3 5
geometry-triangle-classify-from-angles 9 17 3 6
geometry-quadrilateral-side-angle-classification 9 18 3 8
"""
for row in ASSIGNMENTS.splitlines():
    vid,grade,unit,w,qs=row.split()
    APPROVED.extend((g(int(grade),int(unit),w,q),vid) for q in qs.split(','))
APPROVED.append((('worksheets/enrichment/number-theory 1/U1modular-arithmetic/E-NT1U1W1-1.csv','8'),'number-theory-congruence-difference'))
assert len(APPROVED)==len(set(ref for ref,vid in APPROVED))==61
MERGES=[]
SOURCE_NOTES={}
for w in ('1','1HW'):
    SOURCE_NOTES[g(8,6,w,1)]='Source scope issue: dilation is excluded without a scale factor. A dilation with factor 1 (or -1 for signed factors) preserves distances. Specify a non-unit absolute factor or qualify the question. Left pending; source unchanged.'
for w,q in [('7',10),('7Rev',5)]:
    SOURCE_NOTES[g(8,6,w,q)]='Source scope issue: the explanation infers similarity for arbitrary shapes from equal angles alone; that is insufficient for general polygons. Different corresponding side lengths exclude congruence, but similarity needs proportional sides, or a triangle restriction. Left pending; source unchanged.'
REVIEW_NOTES={}
for w in ('1','1HW'):
    q='4' if w=='1' else '3'
    REVIEW_NOTES[g(10,8,w,q)]='The ASA lesson explicitly distinguishes AA similarity from ASA congruence, including why angles alone fix shape but not size.'


def apply_review(doc,merge=False):
    changes=[];reviewed=0
    for s in SPECS:
        vid=s['video_id'];title=s['topic']
        if vid not in doc['videos']:
            doc['videos'][vid]={'title':title,'question_type':title,'curriculum':{'kind':'shared','topic':'geometry'},
             'production_status':'planned','target_duration_seconds':60,'duration_seconds':None,'example':None,
             'assets':{'mp4':None,'captions':None},'youtube':{'video_id':None,'visibility':None},
             'notes':'Distinct congruence method identified through explicit question review.',
             'planning':{'basis':'rule','rule':vid,'review_status':'needs_review'}}
    for (file,qid),vid in sorted(set(APPROVED)):
        p=doc['worksheets'][file]['problems'][qid]
        assert len(p['video_links'])==1,(file,qid)
        # All approved questions are self-contained; no figure is needed.
        p['requires_source_visual']=False
        old=p['video_links'][0]['video_id']
        if old!=vid:changes.append((file,qid,old,vid));p['video_links'][0]['video_id']=vid
        reviewed+=p['mapping_status']!='reviewed'
        p.update(mapping_method='manual',mapping_status='reviewed',mapping_rule='congruence-review-1',
          notes='Inspected against the authored analogous example: matching congruence method and prerequisite steps; different numerical inputs.' + (' ' + REVIEW_NOTES[(file,qid)] if (file,qid) in REVIEW_NOTES else ''))
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
