"""Explicit review of inverse measurement, rings and composed area functions."""
import argparse,fcntl,json
from pathlib import Path
from inverse_measurement_lessons import SPECS,lessons
from number_sense_lessons import source as g
from video_reuse import append_upload_row,update_reuse_checklist,merge_reviewed_duplicate
from build_video_correspondence import validate,read_inventory
from generate_video_batch import save_json,update_overview
from video_example_checks import require_analogous_examples

APPROVED=[(tuple(s['source_ref']),s['video_id']) for s in SPECS]
def gr(vid,grade,unit,w,qs):APPROVED.extend((g(grade,unit,w,q),vid) for q in qs)
gr('geometry-area-square-missing-dimension',3,10,'3HW',[5]);gr('geometry-area-square-missing-dimension',3,11,3,[3]);gr('geometry-area-square-missing-dimension',3,11,'3Rev',[3])
gr('geometry-perimeter-from-area-rectangle',3,11,3,[8]);gr('geometry-perimeter-from-area-rectangle',3,11,'3HW',[1,3])
gr('geometry-perimeter-triangle-missing-dimension',3,11,'2Rev',[3])
gr('geometry-perimeter-two-equal-missing-sides',3,11,2,[10]);gr('geometry-perimeter-two-equal-missing-sides',3,11,'2HW',[4,5])
gr('geometry-parallelogram-base-from-area',6,8,'1Rev',[2])
gr('geometry-parallelogram-rearrangement',6,8,'1Rev',[5])
gr('measurement-area-value-equal-price',3,10,4,[10]);gr('measurement-area-value-equal-price',3,10,'4HW',[4,5])
gr('geometry-volume-rectangular-prism-coordinates',5,11,'2Rev',[4])
gr('geometry-area-triangle-side-equation',6,8,'2Rev',[5])
gr('geometry-area-circle-coordinates',7,9,'3Rev',[5]);gr('geometry-area-circle-coordinates',7,9,4,[10]);gr('geometry-area-circle-coordinates',7,9,'4Rev',[5]);gr('geometry-area-circle-coordinates',7,9,5,[8]);gr('geometry-area-circle-coordinates',7,9,'5Rev',[4])
gr('geometry-area-general-coordinates',12,1,'2HW',[2])
MERGES=[
 ('geometry-perimeter-from-area-square','geometry-area-square-missing-dimension',[g(3,11,3,4),g(3,11,'3Rev',4)]),
 ('geometry-perimeter-square-missing-dimension','geometry-square-area-from-perimeter',[g(4,13,1,2),g(4,13,'1HW',2)]),
]
SOURCE_NOTES={
 g(3,10,3,10):'The source labels side length in square units; the answer should use linear units. The linked lesson distinguishes side, perimeter and area units.',
 g(3,11,3,3):'The source solution starts with an incorrect square-unit label for side length; the correct side is in linear units.',
 g(3,11,2,3):'The source solution incorrectly writes 8 + 14 as 26; it is 22. The final missing-side answer of 12 cm is correct.',
 g(3,11,2,10):'The question uses metres, while the solution switches to centimetres. The numerical answer is correct; the requested side length is 16 metres.'
}


def apply_review(doc,merge=False):
    changes=[];reviewed=0
    for s in SPECS:
        vid=s['video_id'];title=s['topic']
        if vid not in doc['videos']:
            doc['videos'][vid]={'title':title,'question_type':title,'curriculum':{'kind':'shared','topic':'measurement'},
             'production_status':'planned','target_duration_seconds':60,'duration_seconds':None,'example':None,
             'assets':{'mp4':None,'captions':None},'youtube':{'video_id':None,'visibility':None},
             'notes':'Distinct measurement method identified through explicit question review.',
             'planning':{'basis':'rule','rule':vid,'review_status':'needs_review'}}
    for (file,qid),vid in sorted(set(APPROVED)):
        p=doc['worksheets'][file]['problems'][qid]
        assert len(p['video_links'])==1 and not p['requires_source_visual'],(file,qid)
        old=p['video_links'][0]['video_id']
        if old!=vid:changes.append((file,qid,old,vid));p['video_links'][0]['video_id']=vid
        reviewed+=p['mapping_status']!='reviewed'
        p.update(mapping_method='manual',mapping_status='reviewed',mapping_rule='inverse-measurement-review-1',
          notes='Inspected against the authored analogous example: matching measurement or function-composition method and prerequisite steps; different numerical inputs.')
    for (file,qid),note in SOURCE_NOTES.items():doc['worksheets'][file]['problems'][qid]['notes'] += ' ' + note
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
