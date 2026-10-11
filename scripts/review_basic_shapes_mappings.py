"""Explicit direct-formula links; advanced and misclassified questions stay pending."""
import argparse, fcntl, json
from pathlib import Path
from basic_shapes_lessons import SPECS, lessons
from number_sense_lessons import source as g
from video_reuse import update_reuse_checklist
from build_video_correspondence import validate, read_inventory
from generate_video_batch import save_json, update_overview
from video_example_checks import require_analogous_examples

APPROVED=[(tuple(s['source_ref']),s['video_id']) for s in SPECS]
def gr(vid,grade,unit,w,qs):APPROVED.extend((g(grade,unit,w,q),vid) for q in qs)
gr('geometry-area-square',3,10,'3Rev',[3])
for w in [3,'3Rev']:gr('geometry-area-square',3,11,w,[1])
for w in [1,'1HW']:gr('geometry-area-square',4,13,w,[4])
for w,qs in [(1,[3,6]),('1HW',[1]),('1Rev',[3]),(3,[2]),('3Rev',[2])]:gr('geometry-perimeter-square',3,11,w,qs)
gr('geometry-perimeter-square',4,13,1,[6]);gr('geometry-perimeter-square',4,13,'1Rev',[1]);gr('geometry-perimeter-square',7,1,3,[6])
for w,qs in [(1,[2,8]),('1HW',[3]),('1Rev',[2])]:gr('geometry-perimeter-rectangle',3,11,w,qs)
for w in [1,'1HW']:gr('geometry-perimeter-rectangle',4,13,w,[1])
for w,qs in [(1,[1,5]),('1Rev',[1,5])]:gr('geometry-perimeter-triangle',3,11,w,qs)
gr('geometry-perimeter-triangle',7,1,'3HW',[4])
for w,qs in [(1,[2,3,4]),('1HW',[2,3]),('1Rev',[1])]:gr('geometry-area-parallelogram',6,8,w,qs)
for w,qs in [(2,[1,3]),('2HW',[1]),('2Rev',[1]),(3,[4]),('3HW',[3])]:gr('geometry-area-triangle',6,8,w,qs)
for w,qs in [(2,[2,10]),('2HW',[2,5])]:gr('geometry-area-triangle',6,8,w,qs)
gr('geometry-area-triangle',6,10,4,[4]);gr('geometry-area-triangle',6,10,'4HW',[3])
for w,qs in [(2,[2]),('2HW',[2]),('2Rev',[5])]:gr('geometry-area-triangle',9,18,w,qs)
for w,qs in [(4,[2,3,4,5]),('4HW',[2,3]),('4Rev',[1])]:gr('geometry-area-trapezoid',6,8,w,qs)
for w in [2,'2HW','2Rev']:gr('geometry-area-trapezoid',9,18,w,[1])
gr('geometry-area-circle',7,9,1,[5]);gr('geometry-area-circle',7,9,'1HW',[3]);gr('geometry-area-circle',7,9,'2HW',[4])
gr('geometry-area-circle',10,11,5,[4]);gr('geometry-area-circle',10,11,'5Rev',[3,5])


def apply_review(doc):
    changes=[];reviewed=0
    assert all(s['video_id'] in doc['videos'] for s in SPECS)
    for (file,qid),vid in sorted(set(APPROVED)):
        p=doc['worksheets'][file]['problems'][qid]
        assert len(p['video_links'])==1 and not p['requires_source_visual'],(file,qid)
        old=p['video_links'][0]['video_id']
        if old!=vid:changes.append((file,qid,old,vid));p['video_links'][0]['video_id']=vid
        reviewed+=p['mapping_status']!='reviewed'
        p.update(mapping_method='manual',mapping_status='reviewed',mapping_rule='basic-shapes-review-1',
          notes='Inspected direct formula or explicitly explained formula relationship; video uses a different numerical example and correct geometric units.')
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
        validate(doc,read_inventory(),asset_root=args.output.parent);require_analogous_examples(doc,lessons(doc))
        lines=(args.output/'youtube-upload-checklist.md').read_text().splitlines()
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
