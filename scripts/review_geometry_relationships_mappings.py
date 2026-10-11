"""Individually inspected inverse formulas and geometry relationships."""
import argparse,fcntl,json
from pathlib import Path
from geometry_relationships_lessons import SPECS,lessons
from number_sense_lessons import source as g
from video_reuse import append_upload_row,update_reuse_checklist,merge_reviewed_duplicate
from build_video_correspondence import validate,read_inventory
from generate_video_batch import save_json,update_overview
from video_example_checks import require_analogous_examples

APPROVED=[(tuple(s['source_ref']),s['video_id']) for s in SPECS]
# Full CSV rows inspected: "picture frame" is a context noun, no diagram is
# referenced or attached; perimeter and length are fully specified in the text.
TEXT_SUFFICIENT={g(4,13,1,3),g(4,13,'1HW',3)}
def gr(vid,grade,unit,w,qs):APPROVED.extend((g(grade,unit,w,q),vid) for q in qs)
gr('geometry-medial-triangle-measures',10,8,3,[3,4]);gr('geometry-medial-triangle-measures',10,8,'3HW',[1,2])
gr('geometry-circle-area-scaling',10,11,'5HW',[5]);gr('geometry-circle-area-scaling',7,9,2,[4]);gr('geometry-circle-area-scaling',7,9,'2HW',[3])
gr('geometry-area-semicircle',7,9,'1Rev',[3]);gr('geometry-circle-diameter-from-area',7,9,'2HW',[1])
for w in [5,6,7]:gr('geometry-area-isosceles-pythagoras',8,5,w,[5]);gr('geometry-area-isosceles-pythagoras',8,5,f'{w}Rev',[1])
gr('geometry-square-area-from-perimeter',3,11,'3HW',[5]);gr('geometry-parallelogram-height-from-area',6,8,'1Rev',[3])
for w,qs in [(2,[5,6,7,8]),('2HW',[4]),('2Rev',[2,3,4])]:gr('geometry-area-triangle-missing-dimension',6,8,w,qs)
for w,qs in [(4,[8,9,10]),('4HW',[5]),('4Rev',[3,4])]:gr('geometry-area-trapezoid-missing-dimension',6,8,w,qs)
gr('geometry-rectangle-perimeter-equation',8,2,'3HW',[3])
gr('geometry-area-two-triangles',6,8,'4HW',[1]);gr('geometry-area-two-triangles',6,8,3,[8]);gr('geometry-area-two-triangles',6,8,'3Rev',[3])
gr('geometry-triangle-equal-height-compare-bases',6,8,'4Rev',[5])
for w,qs in [(2,[5,6]),('2HW',[1]),('2Rev',[5])]:gr('geometry-perimeter-rectangle-missing-dimension',3,11,w,qs)
for w in [1,'1HW']:gr('geometry-perimeter-rectangle-missing-dimension',4,13,w,[3])
gr('geometry-perimeter-rectangle-missing-dimension',10,3,5,[6]);gr('geometry-perimeter-rectangle-missing-dimension',10,3,'5Rev',[1])
# Direct-formula questions wrongly grouped as missing-dimension problems.
gr('geometry-area-triangle',6,8,2,[4]);gr('geometry-area-triangle',6,8,'2HW',[3])
gr('geometry-area-trapezoid',6,8,4,[6]);gr('geometry-area-trapezoid',6,8,'4HW',[4])
MERGE_REFS=[g(10,11,5,5),g(10,11,'5HW',2)]


def apply_review(doc,merge=False):
    changes=[];reviewed=0
    for s in SPECS:
        vid=s['video_id'];title=s['topic']
        if vid not in doc['videos']:
            doc['videos'][vid]={'title':title,'question_type':title,'curriculum':{'kind':'shared','topic':'geometry'},
             'production_status':'planned','target_duration_seconds':60,'duration_seconds':None,'example':None,
             'assets':{'mp4':None,'captions':None},'youtube':{'video_id':None,'visibility':None},
             'notes':'Distinct geometry method identified through explicit question review.',
             'planning':{'basis':'rule','rule':vid,'review_status':'needs_review'}}
    for (file,qid),vid in sorted(set(APPROVED)):
        p=doc['worksheets'][file]['problems'][qid]
        if (file,qid) in TEXT_SUFFICIENT:p['requires_source_visual']=False
        assert len(p['video_links'])==1 and not p['requires_source_visual'],(file,qid)
        old=p['video_links'][0]['video_id']
        if old!=vid:changes.append((file,qid,old,vid));p['video_links'][0]['video_id']=vid
        reviewed+=p['mapping_status']!='reviewed'
        p.update(mapping_method='manual',mapping_status='reviewed',mapping_rule='geometry-relationships-review-1',
          notes='Inspected against the authored analogous example: matching inverse formula, geometric relationship or prerequisite steps; different numerical inputs.')
    if merge and doc['videos']['geometry-area-circle-missing-dimension']['production_status']!='retired':
        merge_reviewed_duplicate(doc,'geometry-area-circle-missing-dimension',{ref:'geometry-area-circle' for ref in MERGE_REFS})
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
        from basic_shapes_lessons import lessons as basics
        require_analogous_examples(doc,basics(doc))
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
