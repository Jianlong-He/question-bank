"""Explicit arithmetic-property and measurement review across grades and PCF."""
import argparse,json,fcntl
from pathlib import Path
from measurement_properties_lessons import SPECS
from probability_lessons import enrichment as e
from number_sense_lessons import source as g
from video_reuse import append_upload_row,update_reuse_checklist,merge_reviewed_duplicate
from build_video_correspondence import validate,read_inventory
from generate_video_batch import save_json,update_overview
APPROVED=[(tuple(s['source_ref']),s['video_id']) for s in SPECS]
def en(vid,w,qs):APPROVED.extend((e('PCF',w,q),vid) for q in qs)
def gr(vid,grade,unit,w,qs):APPROVED.extend((g(grade,unit,w,q),vid) for q in qs)
gr('arithmetic-commutative-property',3,2,'3Rev',[5])
for w,qs in [(1,[4]),('1HW',[4]),(2,[1,2,3,4]),('2HW',[1,2,3,4])]:en('arithmetic-regroup-products',w,qs)
en('pattern-pcf-370425ce3b84',2,[6]);en('pattern-pcf-370425ce3b84',3,[1,2])
for w,qs in [(2,[7,10]),('2Rev',[2,5]),(3,[4,10]),('3HW',[3])]:en('arithmetic-distribute-two-sums',w,qs)
for w,qs in [(1,[5]),(2,[1,2,3,4,6]),('2HW',[1]),('2Rev',[1,2,3,4]),(3,[1,2,4,5,6]),('3HW',[1]),('3Rev',[1,2,4,5]),(4,[2,4]),('4Rev',[2,4]),(5,[1]),('5Rev',[1])]:gr('geometry-area-rectangle',3,10,w,qs)
for w in [1,'1HW']:gr('geometry-area-rectangle',4,13,w,[5])
for w in [3,'3Rev']:gr('geometry-area-rectangle',4,4,w,[1])
for w in [1,'1Rev']:gr('geometry-area-rectangle',5,11,w,[2])
for w,qs in [(1,[1]),('1HW',[1]),(3,[3]),('3HW',[2])]:gr('geometry-area-rectangle',6,8,w,qs)
gr('geometry-area-rectangle',6,10,4,[5]);gr('geometry-area-rectangle',6,10,'4HW',[4])
en('geometry-area-rectangle',1,[1]);en('geometry-area-rectangle','1HW',[1])
gr('geometry-volume-rectangular-prism',5,11,2,[1,4,6]);gr('geometry-volume-rectangular-prism',10,10,3,[9]);gr('geometry-volume-rectangular-prism',10,10,'3HW',[5]);gr('geometry-volume-rectangular-prism',10,10,'2HW',[1])
for w,qs in [(1,[2,6]),('1HW',[2]),('1Rev',[1])]:en('geometry-volume-rectangular-prism',w,qs)
gr('geometry-volume-cube',5,11,'2Rev',[2]);en('geometry-volume-cube',1,[5]);en('geometry-volume-cube','1HW',[5])
gr('geometry-volume-rectangular-prism-missing-dimension',5,11,'3HW',[3]);en('geometry-volume-rectangular-prism-missing-dimension',1,[10]);en('geometry-volume-rectangular-prism-missing-dimension','1Rev',[5])
for w,qs in [(3,[1,2,5]),('3HW',[1,4]),('3Rev',[1])]:gr('geometry-area-conservation',6,8,w,qs)
gr('number-place-value-maximize-difference',4,2,'3HW',[3])
MERGES=[
 ('pattern-pcf-3baee6ca92a3','pattern-pcf-370425ce3b84',[e('PCF','2HW',5),e('PCF','2Rev',1),e('PCF','3HW',1)]),
 ('pattern-pcf-aadf8ee9b218','pattern-pcf-370425ce3b84',[e('PCF',2,q) for q in [8,9]]+[e('PCF',3,q) for q in [3,5,6,7,9]]),
 ('pattern-pcf-e6b87fc76cec','pattern-pcf-370425ce3b84',[e('PCF','2Rev',q) for q in [3,4]]+[e('PCF','3HW',q) for q in [2,4]]+[e('PCF','3Rev',q) for q in [1,2,3,4]]),
 ('pattern-pcf-b0b73248aea4','pattern-pcf-276f557682ac',[e('PCF','1Rev',3)])]
CORRECTIONS=[(g(10,2,2,10),'factoring-polynomials'),(g(10,2,'2Rev',5),'factoring-polynomials'),
 (g(3,10,2,9),'geometry-area-rectangle-missing-dimension'),(g(3,10,'2HW',4),'geometry-area-rectangle-missing-dimension')]


def apply_review(doc,merge=False):
    changed=[];reviewed=0
    for s in SPECS:
        vid=s['video_id'];title=s['topic']
        if vid not in doc['videos']:
            doc['videos'][vid]={'title':title,'question_type':title,'curriculum':{'kind':'shared','topic':'arithmetic'},
             'production_status':'planned','target_duration_seconds':60,'duration_seconds':None,
             'example':None,'assets':{'mp4':None,'captions':None},'youtube':{'video_id':None,'visibility':None},
             'notes':'Distinct method identified from inspected grade and enrichment questions.',
             'planning':{'basis':'rule','rule':vid,'review_status':'needs_review'}}
    for (file,qid),vid,review in [(r,v,False) for r,v in CORRECTIONS]+[(r,v,True) for r,v in sorted(set(APPROVED))]:
        p=doc['worksheets'][file]['problems'][qid]
        assert len(p['video_links'])==1 and not p['requires_source_visual'],(file,qid)
        old=p['video_links'][0]['video_id'];assert vid in doc['videos'],vid
        if old!=vid:changed.append((file,qid,old,vid));p['video_links'][0]['video_id']=vid
        if review and p['mapping_status']!='reviewed':reviewed+=1
        p.update(mapping_method='manual',mapping_status='reviewed' if review else 'needs_review',mapping_rule='measurement-properties-review-1',
          notes='Inspected against the worked example: same method with different numerical data and suitable prerequisites.' if review else 'Corrected a rectangle keyword false match; destination still needs example review.')
    merged=0
    if merge:
        for old,new,refs in MERGES:
            if doc['videos'][old].get('reuse_video_ids')==[new]:continue
            merge_reviewed_duplicate(doc,old,{ref:new for ref in refs});merged+=1
    for s in SPECS:
        v=doc['videos'][s['video_id']];v['title']=s['topic'];v['question_type']=s['topic']
        refs=[p for w in doc['worksheets'].values() for p in w['problems'].values() if any(l['video_id']==s['video_id'] for l in p['video_links'])]
        if refs and all(p['mapping_status']=='reviewed' for p in refs):v['planning']['review_status']='reviewed'
    return changed,reviewed,merged


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True);parser.add_argument('--check',action='store_true');parser.add_argument('--merge',action='store_true');args=parser.parse_args()
    with (Path(__file__).resolve().parents[1]/'videos/.production.lock').open('a+') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        path=args.output/'worksheet-video-correspondence.json';doc=json.loads(path.read_text())
        assert not any(v['production_status']=='in_progress' for v in doc['videos'].values())
        before={k:(v['youtube'].copy(),v['assets'].copy()) for k,v in doc['videos'].items()}
        changes,reviewed,merged=apply_review(doc,args.merge)
        assert before=={k:(doc['videos'][k]['youtube'],doc['videos'][k]['assets']) for k in before}
        validate(doc,read_inventory(),asset_root=args.output.parent)
        from measurement_properties_lessons import lessons
        from video_example_checks import require_analogous_examples
        require_analogous_examples(doc,lessons(doc))
        content=(args.output/'youtube-upload-checklist.md').read_text()
        for vid in sorted(set(doc['videos'])-set(before)):content=append_upload_row(content,vid,doc['videos'][vid]['title'])
        lines=content.splitlines()
        for i,line in enumerate(lines):
            for s in SPECS:
                if f'| {s["video_id"]}.mp4 |' in line:
                    cells=line.split('|');cells[1]=' '+s['topic']+' ';lines[i]='|'.join(cells)
        content=update_reuse_checklist('\n'.join(lines)+'\n',doc)
        if not args.check:
            save_json(path,doc);(args.output/'youtube-upload-checklist.md').write_text(content)
            update_overview(args.output,doc,[s['video_id'] for s in SPECS])
        print(f'{len(changes)} corrected links; {reviewed} newly reviewed refs; {merged} drafts reused. Check only: {args.check}')
        for c in changes:print(*c,sep=' | ')

if __name__=='__main__':main()
