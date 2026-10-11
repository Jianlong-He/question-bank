"""Explicitly reviewed dilation mappings and unresolved source issues."""
import argparse,fcntl,json
from pathlib import Path
from dilation_lessons import SPECS,lessons
from number_sense_lessons import source as g
from video_reuse import append_upload_row,update_reuse_checklist,merge_reviewed_duplicate
from build_video_correspondence import validate,read_inventory
from generate_video_batch import save_json,update_overview
from video_example_checks import require_analogous_examples

APPROVED=[]
# Each explicit row was checked against its full question, answer and solution.
ASSIGNMENTS = """image-length 10 10 1 1
area 10 10 1 2
area 10 10 1HW 2
volume 10 10 1 3,4
volume 10 10 1HW 1
volume 10 10 1Rev 1,4
volume 10 10 3 8
volume 10 10 3Rev 3
length-ratio 10 11 5 9
length-ratio 10 11 5HW 4
length-ratio 10 8 1 2
length-ratio 10 8 1HW 1
angle-preservation 10 8 1 7
angle-preservation 10 8 1Rev 3
area 10 8 2 3,4,5
area 10 8 2HW 2,3
area 10 8 2Rev 2
length-ratio 10 8 2 7
length-ratio 10 8 2HW 4
similarity-congruence 10 8 2 9
similarity-congruence 10 8 2Rev 4
length-from-area 10 8 2Rev 3
image-length 7 8 1 1,2,6
image-length 7 8 1HW 1,2,5
length-ratio 7 8 1 3,5
length-ratio 7 8 1HW 3,4
image-length 7 8 2 1
image-length 7 8 2HW 1
length-ratio 7 8 2 2,3,5
length-ratio 7 8 2HW 2,3
length-ratio 7 8 2Rev 1
image-length 7 8 3 1,6
image-length 7 8 3HW 1,4
length-ratio 7 8 3 2,3,5
length-ratio 7 8 3HW 2,3
length-ratio 7 8 3Rev 1
area 7 8 4HW 5
area 7 8 4Rev 3
area 7 8 5HW 4
area 7 8 5Rev 4
origin-coordinates 8 6 10 1,5
origin-coordinates 8 6 10HW 1
origin-coordinates 8 6 10Rev 1
angle-preservation 8 6 10 2
angle-preservation 8 6 10HW 2
coordinate-factor 8 6 10 3
coordinate-factor 8 6 10HW 3
perimeter 8 6 10 4
perimeter 8 6 10HW 4
length-ratio 8 6 10 6,7
length-ratio 8 6 10HW 5
length-ratio 8 6 10Rev 2
image-length 8 6 10 8
image-length 8 6 10Rev 3
similarity-congruence 8 6 10 9,10
similarity-congruence 8 6 10Rev 4,5
image-length 8 6 11 1,8
image-length 8 6 11HW 1
image-length 8 6 11Rev 3
origin-coordinates 8 6 11 2,5
origin-coordinates 8 6 11HW 2,5
similarity-congruence 8 6 11 3
similarity-congruence 8 6 11HW 3
length-ratio 8 6 11 4,6,7,9
length-ratio 8 6 11HW 4
length-ratio 8 6 11Rev 1,2,4
origin-coordinates 8 6 8 7
origin-coordinates 8 6 8Rev 3
perimeter 8 6 8 8
perimeter 8 6 8HW 5
origin-coordinates 8 6 9 1,5
origin-coordinates 8 6 9HW 1,4
length-ratio 8 6 9 2
length-ratio 8 6 9HW 2
angle-preservation 8 6 9 3
angle-preservation 8 6 9HW 3
similarity-congruence 8 6 9 4,9
similarity-congruence 8 6 9Rev 1,4
coordinate-factor 8 6 9 6,7
coordinate-factor 8 6 9HW 5
coordinate-factor 8 6 9Rev 2
 enlargement-reduction 9 15 1 4,9
 enlargement-reduction 9 15 1HW 4
similarity-congruence 9 15 1 6
similarity-congruence 9 15 1Rev 5
origin-coordinates 9 15 4 1,2,10
origin-coordinates 9 15 4HW 1,2
origin-coordinates 9 15 4Rev 1,2
length-ratio 9 15 4 3,9
length-ratio 9 15 4HW 3
length-ratio 9 15 4Rev 3
 enlargement-reduction 9 15 4 4,5
 enlargement-reduction 9 15 4HW 4,5
center-line 9 15 4 6
image-length 9 15 4 7
angle-preservation 9 15 4 8
similarity-congruence 9 15 4Rev 4
perimeter 9 15 4Rev 5
similarity-congruence 9 16 1 6
similarity-congruence 9 16 1HW 5
image-length 9 16 2 1
image-length 9 16 2HW 1,5
image-length 9 16 2Rev 1
area 9 16 2 2
area 9 16 2HW 2
area 9 16 2Rev 2
angle-preservation 9 16 2 3
angle-preservation 9 16 2HW 3
angle-preservation 9 16 2Rev 3
center-line 9 16 2 4
center-line 9 16 2HW 4
similarity-congruence 9 16 2 9
length-ratio 9 16 2 10
perimeter 9 16 2Rev 4
similarity-congruence 9 16 2Rev 5
similarity-congruence 9 17 1 2
similarity-congruence 9 17 1HW 2
similarity-congruence 9 17 1Rev 4,5
"""
for row in ASSIGNMENTS.splitlines():
    method,grade,unit,w,qs=row.split()
    APPROVED.extend((g(int(grade),int(unit),w,q),'geometry-dilation-'+method) for q in qs.split(','))
assert len(APPROVED)==len(set(ref for ref,vid in APPROVED))
MERGES=[]
SOURCE_NOTES={}
for w,q in [(1,4),('1Rev',1),(2,4),('2Rev',2),(3,4),('3Rev',2)]:
    SOURCE_NOTES[g(7,8,w,q)]='Source issue: only three side measurements are supplied for an incompletely specified polygon; matching these ratios does not prove that the whole shapes are scaled copies. Shape/angle information or corrected wording is needed. Left pending; no inferred diagram.'
for w,q in [(4,7),(4,8),(5,7),(5,8)]:
    SOURCE_NOTES[g(7,8,w,q)]='Source issue: CSV answer field is truncated by malformed quoting before a comma. The area-scaling method is clear, but the parsed multi-part answer requires repair. Left pending; source CSV unchanged.'
for w,q in [(5,10),('5Rev',5)]:
    SOURCE_NOTES[g(7,8,w,q)]='Source issue: the supplied answer 24 has units km/cm. A dimensionless real/drawing scale factor requires common units and equals 2400000. Clarify whether the intended answer is a map rate or a dimensionless scale factor. Left pending.'
REVIEW_NOTES={}
for w,qs in [(10,[9]),('10Rev',[4]),(9,[9]),('9Rev',[4])]:
    for q in qs:REVIEW_NOTES[g(8,6,w,q)]='The source implicitly assumes positive k. The lesson states that scope explicitly; negative k=-1 preserves lengths despite k not equaling 1.'
for w,q in [(9,4),('9Rev',1)]:
    REVIEW_NOTES[g(8,6,w,q)]='Similarity is guaranteed for a nondegenerate dilation; congruence is also possible at k=1. The lesson teaches this exception rather than repeating the source claim that size always changes.'
# These four isolated questions omit the center needed to determine k.
for w,qs in [(9,[6,7]),('9HW',[5]),('9Rev',[2])]:
    for q in qs:
        ref=g(8,6,w,q)
        APPROVED=[item for item in APPROVED if item[0]!=ref]
        SOURCE_NOTES[ref]='Source issue: the stated point and image do not uniquely determine the scale factor without the dilation center. The answer assumes the origin. Left pending until the center is made explicit; no source CSV edits.'


def apply_review(doc,merge=False):
    changes=[];reviewed=0
    for s in SPECS:
        vid=s['video_id'];title=s['topic']
        if vid not in doc['videos']:
            doc['videos'][vid]={'title':title,'question_type':title,'curriculum':{'kind':'shared','topic':'geometry'},
             'production_status':'planned','target_duration_seconds':60,'duration_seconds':None,'example':None,
             'assets':{'mp4':None,'captions':None},'youtube':{'video_id':None,'visibility':None},
             'notes':'Distinct dilation method identified through explicit question review.',
             'planning':{'basis':'rule','rule':vid,'review_status':'needs_review'}}
    for (file,qid),vid in sorted(set(APPROVED)):
        p=doc['worksheets'][file]['problems'][qid]
        assert len(p['video_links'])==1,(file,qid)
        # All approved questions are self-contained; no figure is needed.
        p['requires_source_visual']=False
        old=p['video_links'][0]['video_id']
        if old!=vid:changes.append((file,qid,old,vid));p['video_links'][0]['video_id']=vid
        reviewed+=p['mapping_status']!='reviewed'
        p.update(mapping_method='manual',mapping_status='reviewed',mapping_rule='dilation-review-1',
          notes='Inspected against the authored analogous example: matching dilation method and prerequisite steps; different numerical inputs.' + (' ' + REVIEW_NOTES[(file,qid)] if (file,qid) in REVIEW_NOTES else ''))
    for (file,qid),note in SOURCE_NOTES.items():
        p=doc['worksheets'][file]['problems'][qid]
        assert p['mapping_status']=='needs_review'
        p['notes']=note
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
