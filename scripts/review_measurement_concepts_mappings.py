"""Explicit review of capacity, volume concepts and decompositions."""
import argparse,fcntl,json
from pathlib import Path
from measurement_concepts_lessons import SPECS,lessons
from number_sense_lessons import source as g
from video_reuse import append_upload_row,update_reuse_checklist,merge_reviewed_duplicate
from build_video_correspondence import validate,read_inventory
from generate_video_batch import save_json,update_overview
from video_example_checks import require_analogous_examples

APPROVED=[(tuple(s['source_ref']),s['video_id']) for s in SPECS]
def gr(vid,grade,unit,w,qs):APPROVED.extend((g(grade,unit,w,q),vid) for q in qs)
gr('measurement-capacity-metric-estimates',4,14,2,[2,3,4,8]);gr('measurement-capacity-metric-estimates',4,14,'2HW',[3]);gr('measurement-capacity-metric-estimates',4,14,'2Rev',[1,2,3,4])
gr('measurement-capacity-customary-estimates',4,14,2,[6,9,10]);gr('measurement-capacity-customary-estimates',4,14,'2HW',[1,2,5])
gr('measurement-volume-cubic-units',5,11,1,[9]);gr('measurement-volume-cubic-units',5,11,'1HW',[3]);gr('measurement-volume-cubic-units',5,11,2,[3]);gr('measurement-volume-cubic-units',5,11,'2Rev',[3])
gr('geometry-volume-factor-order',5,11,'2HW',[1,2])
gr('geometry-volume-composite-convert-cubic-units',5,11,'3HW',[4])
gr('measurement-choose-area-perimeter-volume',9,3,'1Rev',[4])
gr('geometry-volume-cavalieri',10,10,'1HW',[5])
gr('geometry-volume-cone',10,10,'2Rev',[1]);gr('geometry-volume-cone',8,5,8,[8]);gr('geometry-volume-cone',8,5,'8HW',[5])
MERGES=[('geometry-volume-cone-missing-dimension','geometry-volume-cone',[
 g(10,10,2,8),g(10,10,'2HW',3),g(8,5,8,2),g(8,5,8,6),g(8,5,'8HW',2),g(8,5,'8Rev',2)])]
SOURCE_NOTES={g(5,11,3,8):'Source answer 264 is cubic metres; requested cubic centimetres require 264,000,000. The linked analogous lesson explicitly teaches this conversion. Source CSV unchanged.',
 g(5,11,'3HW',4):'Source answer 132 is cubic metres; requested cubic centimetres require 132,000,000. The linked analogous lesson explicitly teaches this conversion. Source CSV unchanged.'}
VISUAL_PENDING={g(5,6,5,2):'Answer choices A and B are not defined in the CSV; inspect the original choices before certifying the mapping.',
 g(5,6,5,7):'Question refers to shading above but does not state the shaded count; inspect the source diagram before certifying.',
 g(5,6,5,10):'Question asks for a shaded area but does not state the shaded count; inspect the source diagram before certifying.'}


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
        p.update(mapping_method='manual',mapping_status='reviewed',mapping_rule='measurement-concepts-review-1',
          notes='Inspected against the authored analogous example: matching measurement method and prerequisite steps; different numerical inputs.')
    for (file,qid),note in SOURCE_NOTES.items():doc['worksheets'][file]['problems'][qid]['notes'] += ' ' + note
    for (file,qid),note in VISUAL_PENDING.items():
        problem=doc['worksheets'][file]['problems'][qid]
        assert problem['mapping_status']=='needs_review'
        problem.update(requires_source_visual=True,notes=note)
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
