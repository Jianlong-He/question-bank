"""Explicit cross-grade counting review; separate false matches from verified links."""
import argparse,json,fcntl
from pathlib import Path
from counting_methods_lessons import SPECS
from probability_lessons import enrichment as e
from number_sense_lessons import source as g
from video_reuse import append_upload_row,update_reuse_checklist
from build_video_correspondence import validate,read_inventory
from generate_video_batch import save_json,update_overview

NEW={s['video_id']:s['topic'] for s in SPECS if s['video_id'] not in {'counting-product-rule','counting-permutations','counting-arrangements'}}
NEW.update({'arithmetic-commutative-property':'Changing factor order without changing the product',
 'geometry-area-conservation':'Area stays the same when pieces are rearranged',
 'number-place-value-maximize-difference':'Arrange digits to maximize a difference'})
APPROVED=[(tuple(s['source_ref']),s['video_id']) for s in SPECS];CORRECTIONS=[]

def en(vid,topic,w,qs):APPROVED.extend((e(topic,w,q),vid) for q in qs)
def gr(vid,grade,unit,w,qs):APPROVED.extend((g(grade,unit,w,q),vid) for q in qs)

for w,qs in [(3,[2]),('3Rev',[1]),(4,[2,5]),('4Rev',[1,2]),(5,[1]),('5HW',[1])]:gr('counting-product-rule',7,7,w,qs)
for w,qs in [(1,[2]),(2,[4,8]),('2Rev',[3])]:en('counting-product-rule','counting-and-classification',w,qs)
for w,qs in [(4,[6,10]),('4Rev',[1,5]),(5,[4]),('5HW',[4]),(6,[1]),('6HW',[1])]:en('pattern-pmf-d313e72dd673','PCF',w,qs)
for w,qs in [(2,[1,7]),('2HW',[1]),(3,[1]),('3HW',[1])]:en('pattern-pmf-d313e72dd673','counting-and-classification',w,qs)
for w,qs in [(1,[6]),('1HW',[5]),(3,[7]),('3Rev',[2])]:en('counting-addition-rule','counting-and-classification',w,qs)
for w,qs in [(4,[6]),('4HW',[5]),('4Rev',[1])]:en('counting-sum-then-product','counting-and-classification',w,qs)
for w,qs in [(2,[9]),('2Rev',[4]),(3,[6]),('3Rev',[1])]:en('counting-product-then-sum','counting-and-classification',w,qs)
for w,qs in [(2,[4,5,6]),('2HW',[4,5]),('2Rev',[2,3,5])]:gr('counting-permutations',12,8,w,qs)
for w,qs in [(4,[4,9]),('4HW',[4]),('4Rev',[4]),(5,[3,6]),('5HW',[3]),('5Rev',[1]),(6,[5]),('6HW',[5]),('6Rev',[5])]:en('counting-permutations','PCF',w,qs)
for w,qs in [(1,[1,2,4,8,9]),('1HW',[1,2,3]),('1Rev',[1,2,3]),(3,[5]),('3HW',[4]),('3Rev',[4])]:en('counting-permutations','PeCo',w,qs)
en('counting-permutations','counting-and-classification','2Rev',[1])
for w,qs in [(2,[7]),('2Rev',[4])]:gr('counting-arrangements',12,8,w,qs)
for w,qs in [(4,[5]),('4HW',[5]),(5,[5]),('5HW',[5])]:en('counting-arrangements','PCF',w,qs)
en('counting-arrangements','PeCo',1,[3]);en('counting-arrangements','PeCo','4Rev',[1])
for w,qs in [(5,[7,8]),('5Rev',[2,3])]:en('counting-repeated-arrangements','PCF',w,qs)
en('counting-adjacent-distinct-pair','PCF','5Rev',[4])

for w in [3,'3Rev']:CORRECTIONS.append((g(3,2,w,5),'arithmetic-commutative-property'))
for w in [1,'1HW']:CORRECTIONS.append((g(8,6,w,2),'geometry-translation'))
for w in [2,'2HW','2Rev']:CORRECTIONS.append((g(9,15,w,1),'geometry-translation'))
for w in [3,'3HW','3Rev']:CORRECTIONS.append((g(9,15,w,1),'geometry-rotation'))
for w in [4,'4HW','4Rev']:CORRECTIONS.append((g(9,15,w,1),'geometry-dilation'))
CORRECTIONS += [(g(2,1,2,9),'arithmetic-divide-whole-numbers'),(g(2,1,'3HW',5),'arithmetic-divide-whole-numbers'),
 (g(4,4,'1Rev',5),'arithmetic-multiply-whole-numbers'),(g(4,5,2,9),'arithmetic-divide-whole-numbers'),(g(4,5,'2HW',4),'arithmetic-divide-whole-numbers'),
 (g(4,2,3,10),'number-place-value-maximize-difference'),(g(4,2,'3HW',3),'number-place-value-maximize-difference')]
for w,qs in [(3,[1,2,5]),('3HW',[1,4]),('3Rev',[1])]:CORRECTIONS.extend((g(6,8,w,q),'geometry-area-conservation') for q in qs)


def apply_review(doc):
    changes=[];reviewed=0
    for vid,title in NEW.items():
        if vid not in doc['videos']:
            doc['videos'][vid]={
             'title':title,'question_type':title,'curriculum':{'kind':'shared','topic':'counting'},
             'production_status':'planned','target_duration_seconds':60,'duration_seconds':None,
             'example':None,'assets':{'mp4':None,'captions':None},'youtube':{'video_id':None,'visibility':None},
             'notes':'Distinct method found during explicit counting question and solution review.',
             'planning':{'basis':'rule','rule':vid,'review_status':'needs_review'}}
    for (file,qid),vid,approve in [(r,v,False) for r,v in CORRECTIONS]+[(r,v,True) for r,v in sorted(set(APPROVED))]:
        p=doc['worksheets'][file]['problems'][qid]
        assert len(p['video_links'])==1,(file,qid)
        if approve:assert not p['requires_source_visual'],(file,qid)
        old=p['video_links'][0]['video_id']
        if old!=vid:changes.append((file,qid,old,vid));p['video_links'][0]['video_id']=vid
        if approve and p['mapping_status']!='reviewed':reviewed+=1
        p.update(mapping_method='manual',mapping_status='reviewed' if approve else 'needs_review',mapping_rule='counting-methods-review-1',
          notes='Question and solution inspected: same counting method, different sample data.' if approve else 'Corrected a counting keyword false match. The destination example and prerequisites still need review.')
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
        from counting_methods_lessons import lessons
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
        print(f'{len(changes)} corrected links; {reviewed} newly reviewed refs. Check only: {args.check}')
        for c in changes:print(*c,sep=' | ')

if __name__=='__main__':main()
