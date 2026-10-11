"""Explicitly inspected area and density links; preserve media and YouTube fields."""
import argparse, fcntl, json
from pathlib import Path
from area_density_lessons import SPECS, lessons
from number_sense_lessons import source as g
from video_reuse import append_upload_row, update_reuse_checklist
from build_video_correspondence import validate, read_inventory
from generate_video_batch import save_json, update_overview
from video_example_checks import require_analogous_examples

APPROVED=[(tuple(s['source_ref']),s['video_id']) for s in SPECS]
# These five "figure" keyword flags were checked against full CSV rows. Every
# dimension/area is in the text; image fields are absent or empty, and the given
# solutions explicitly add the two pieces. No external diagram is needed.
TEXT_SUFFICIENT={g(3,10,5,6),g(3,10,5,7),g(3,10,'5HW',1),g(3,10,'5HW',2),g(3,10,'5Rev',2)}
def gr(vid,grade,unit,w,qs):APPROVED.extend((g(grade,unit,w,q),vid) for q in qs)
for w,qs in [(2,[9]),('2HW',[4]),(3,[8,9]),('3HW',[3,4]),(4,[1,3,6]),('4HW',[1]),('4Rev',[1,3])]:
    gr('geometry-area-rectangle-missing-dimension',3,10,w,qs)
for w,qs in [(3,[5,7]),('3HW',[2]),('3Rev',[5])]:gr('geometry-area-rectangle-missing-dimension',3,11,w,qs)
for w,qs in [(4,[7,8]),('4HW',[2,3]),('5Rev',[2])]:gr('geometry-area-add-known-parts',3,10,w,qs)
gr('geometry-area-add-known-parts',6,8,3,[6]);gr('geometry-area-add-known-parts',6,8,'3HW',[5])
gr('geometry-area-two-rectangles',3,10,5,[6,7]);gr('geometry-area-two-rectangles',3,10,'5HW',[1,2])
gr('geometry-area-subtract-known-cutout',3,10,'5HW',[3,4])
gr('geometry-equal-area-different-sides',3,10,'2HW',[3])
gr('geometry-equal-perimeter-different-area',4,13,'1Rev',[5])
gr('geometry-area-from-perimeter-and-side',3,11,'3HW',[4])
gr('geometry-rectangle-from-area-and-perimeter',4,13,1,[7,8]);gr('geometry-rectangle-from-area-and-perimeter',4,13,'1Rev',[2,3])
gr('measurement-density-from-mass-volume',10,10,3,[1,2]);gr('measurement-density-from-mass-volume',10,10,'3HW',[1]);gr('measurement-density-from-mass-volume',10,10,'3Rev',[1])
gr('measurement-mass-from-density-volume',10,10,'3HW',[2]);gr('measurement-volume-from-mass-density',10,10,'3HW',[3])
gr('measurement-density-from-mass-volume',9,3,1,[7]);gr('measurement-density-from-mass-volume',9,3,'1Rev',[3])
gr('geometry-area-subtract-known-cutout',7,9,5,[10]);gr('geometry-area-subtract-known-cutout',7,9,'5Rev',[5])
gr('geometry-area-rectangle-plus-triangle',6,8,3,[7,9,10]);gr('geometry-area-rectangle-plus-triangle',6,8,'3Rev',[2,4,5])
# Inspected false matches to rectangle "missing dimension" and general volume.
for w,qs in [(2,[8]),('2HW',[3]),(3,[5]),('3Rev',[5])]:gr('geometry-area-rectangle',4,4,w,qs)
for w,qs in [(2,[8,9]),('2HW',[3,5]),('2Rev',[5]),(3,[3])]:gr('geometry-volume-rectangular-prism',5,11,w,qs)
gr('geometry-volume-rectangular-prism-missing-dimension',5,11,2,[10]);gr('geometry-volume-rectangular-prism-missing-dimension',5,11,'2HW',[4])
gr('geometry-volume-rectangular-prism',5,11,'3Rev',[3])
gr('geometry-volume-rectangular-prism',6,10,3,[1]);gr('geometry-volume-rectangular-prism',6,10,'3HW',[1])
gr('geometry-volume-rectangular-prism',9,3,'2HW',[1]);gr('geometry-volume-rectangular-prism',10,10,2,[1])


def apply_review(doc):
    changes=[];reviewed=0
    for s in SPECS:
        vid=s['video_id'];title=s['topic']
        if vid not in doc['videos']:
            doc['videos'][vid]={'title':title,'question_type':title,'curriculum':{'kind':'shared','topic':'measurement'},
              'production_status':'planned','target_duration_seconds':60,'duration_seconds':None,
              'example':None,'assets':{'mp4':None,'captions':None},'youtube':{'video_id':None,'visibility':None},
              'notes':'Distinct method identified by inspecting worksheet questions and worked solutions.',
              'planning':{'basis':'rule','rule':vid,'review_status':'needs_review'}}
    for (file,qid),vid in sorted(set(APPROVED)):
        p=doc['worksheets'][file]['problems'][qid]
        if (file,qid) in TEXT_SUFFICIENT:p['requires_source_visual']=False
        assert len(p['video_links'])==1 and not p['requires_source_visual'],(file,qid)
        old=p['video_links'][0]['video_id'];assert vid in doc['videos'],vid
        if old!=vid:changes.append((file,qid,old,vid));p['video_links'][0]['video_id']=vid
        reviewed+=p['mapping_status']!='reviewed'
        p.update(mapping_method='manual',mapping_status='reviewed',mapping_rule='area-density-review-1',
          notes='Inspected against the authored lesson: same area or density method with different numerical data. Side lengths use linear units; areas use square units.')
    for s in SPECS:
        v=doc['videos'][s['video_id']];v['title']=s['topic'];v['question_type']=s['topic']
        refs=[p for w in doc['worksheets'].values() for p in w['problems'].values() if any(l['video_id']==s['video_id'] for l in p['video_links'])]
        if refs and all(p['mapping_status']=='reviewed' for p in refs):v['planning']['review_status']='reviewed'
    return changes,reviewed


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True);parser.add_argument('--check',action='store_true');args=parser.parse_args()
    with (Path(__file__).resolve().parents[1]/'videos/.production.lock').open('a+') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        path=args.output/'worksheet-video-correspondence.json';doc=json.loads(path.read_text())
        assert not any(v['production_status']=='in_progress' for v in doc['videos'].values())
        before={k:(v['youtube'].copy(),v['assets'].copy()) for k,v in doc['videos'].items()}
        changes,reviewed=apply_review(doc)
        assert before=={k:(doc['videos'][k]['youtube'],doc['videos'][k]['assets']) for k in before}
        validate(doc,read_inventory(),asset_root=args.output.parent)
        require_analogous_examples(doc,lessons(doc))
        from measurement_properties_lessons import lessons as previous
        require_analogous_examples(doc,previous(doc))
        content=(args.output/'youtube-upload-checklist.md').read_text()
        for vid in sorted(set(doc['videos'])-set(before)):content=append_upload_row(content,vid,doc['videos'][vid]['title'])
        lines=content.splitlines()
        for i,line in enumerate(lines):
            for s in SPECS:
                if f'| {s["video_id"]}.mp4 |' in line:
                    cells=line.split('|');cells[1]=' '+s['topic']+' ';lines[i]='|'.join(cells)
        if not args.check:
            save_json(path,doc);(args.output/'youtube-upload-checklist.md').write_text(update_reuse_checklist('\n'.join(lines)+'\n',doc))
            update_overview(args.output,doc,[s['video_id'] for s in SPECS])
        print(f'{len(changes)} corrected links; {reviewed} newly reviewed refs. Check only: {args.check}')
        for c in changes:print(*c,sep=' | ')

if __name__=='__main__':main()
