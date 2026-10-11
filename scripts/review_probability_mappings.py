"""Explicit, inspected probability references; preserve unrelated draft links."""
import argparse
import json
from pathlib import Path
from probability_lessons import SPECS,enrichment
from number_sense_lessons import source
from build_video_correspondence import validate,read_inventory
from generate_video_batch import save_json,update_overview

REVIEWED=[(tuple(s['source_ref']),s['video_id']) for s in SPECS]
MOVES=[]


def approve(vid,grade,unit,w,ids):
    REVIEWED.extend((source(grade,unit,w,q),vid) for q in ids)


def enr(vid,topic,w,ids):
    REVIEWED.extend((enrichment(topic,w,q),vid) for q in ids)


def move(ref,old,new,review=False):
    MOVES.append((ref,old,new))
    if review:REVIEWED.append((ref,new))


for w,ids in [(1,[1,2,3,6]),('1HW',[1,5]),('1Rev',[3]),(2,[10]),('2Rev',[4])]:
    approve('probability-equally-likely',10,13,w,ids)
for w,ids in [(2,[2,3]),('2HW',[2,3]),(3,[3,4]),('3HW',[2,3]),(4,[4]),('4HW',[3])]:
    approve('probability-equally-likely',7,7,w,ids)
approve('probability-equally-likely',12,8,3,[9])
enr('probability-equally-likely','conditional-probability',1,[1])
for w,ids in [(1,[4,5]),('1HW',[2]),('1Rev',[2])]:approve('probability-experimental',10,13,w,ids)
for w,ids in [(2,[4,6,7]),('2HW',[4]),('2Rev',[1,2])]:approve('probability-experimental',7,7,w,ids)
for w,ids in [(3,[7,8]),('3HW',[5]),('3Rev',[3]),(4,[7,8]),('4HW',[5]),('4Rev',[3]),(5,[7,8]),('5HW',[4]),('5Rev',[3])]:
    for q in ids:move(source(7,7,w,q),'probability-equally-likely','probability-experimental',True)
for w,q in [(1,8),('1Rev',3)]:move(source(7,7,w,q),'probability-independent','probability-experimental',True)
for w,ids in [(3,[1,3]),('3Rev',[1,2])]:approve('probability-independent',10,13,w,ids)
for w,ids in [(1,[4,6]),('1HW',[4]),('1Rev',[3])]:approve('probability-independent',12,8,w,ids)
for grade,unit,w,ids in [(10,13,3,[2,4]),(10,13,'3HW',[1,2]),(10,13,'3Rev',[5]),(12,8,1,[5]),(12,8,'1HW',[5])]:
    for q in ids:move(source(grade,unit,w,q),'probability-equally-likely','probability-independent',True)
enr('probability-independent','conditional-probability','5Rev',[5])
enr('probability-independent','conditional-probability','5HW',[4])
enr('probability-independent','PMF','3HW',[2,4])
for w,ids in [(3,[5,6]),('3HW',[3,4]),('3Rev',[3])]:approve('probability-without-replacement',10,13,w,ids)
approve('probability-without-replacement',12,8,1,[8,9])
for w,ids in [(5,[3,4]),('5HW',[3]),('5Rev',[1])]:approve('probability-without-replacement',7,7,w,ids)
enr('probability-without-replacement','conditional-probability',4,[1,2,4,5])
enr('probability-without-replacement','conditional-probability','4HW',[1,2,3])
enr('probability-without-replacement','conditional-probability','4Rev',[1,2])
enr('probability-without-replacement','conditional-probability','5Rev',[1])
enr('probability-without-replacement','PMF','6HW',[5])
for w,ids in [(1,[2,9]),('1HW',[2]),('1Rev',[4]),(3,[1]),('3HW',[1]),(4,[1]),('4HW',[1])]:
    approve('probability-sample-space',7,7,w,ids)
for w,ids in [(4,[2,3,4]),('4HW',[1,2]),('4Rev',[2])]:approve('probability-addition-rule',10,13,w,ids)
for w,ids in [(1,[1,2,3]),('1HW',[1,2,3]),('1Rev',[1])]:approve('probability-addition-rule',12,8,w,ids)
enr('probability-addition-rule','conditional-probability','3HW',[5])
for w,ids in [(2,[3,6,8,10]),('2HW',[1,2]),('2Rev',[1,3])]:enr('probability-complements','conditional-probability',w,ids)
for topic,w,ids in [('PMF',3,[7]),('PMF','3Rev',[5]),('conditional-probability','4Rev',[3])]:
    for q in ids:move(enrichment(topic,w,q),'probability-binomial','probability-complements',True)
move(enrichment('conditional-probability','2HW',5),'probability-equally-likely','probability-complements',True)
for w,ids in [(1,[2,3,4,5,9]),('1HW',[1,2,3,5]),('1Rev',[1,2,4])]:enr('probability-conditional','conditional-probability',w,ids)
for w,ids in [(1,[7,8]),('1HW',[5]),('1Rev',[3,4]),(7,[6]),('7HW',[5])]:enr('probability-discrete-distribution','PMF',w,ids)
approve('probability-discrete-distribution',12,8,'4HW',[5])
for w,ids in [(5,[2,3,8,10]),('5HW',[2,3]),('5Rev',[1,2,5])]:approve('probability-expected-value',12,8,w,ids)
for w,q in [(5,4),('5HW',4),('5Rev',3)]:move(source(12,8,w,q),'probability-equally-likely','probability-expected-value',True)
for w,ids in [(1,[1,3,5,10]),('1HW',[1,2,5]),('1Rev',[1,3])]:approve('probability-binomial',11,11,w,ids)
for w,ids in [(1,[4]),('1HW',[3]),('1Rev',[2,5])]:
    for q in ids:move(source(11,11,w,q),'probability-equally-likely','probability-binomial',True)
enr('probability-binomial','PMF',3,[6]);enr('probability-binomial','PMF','5Rev',[3,4])
for w,ids in [(5,[6,7,8]),('5HW',[5]),('5Rev',[1])]:
    for q in ids:move(enrichment('PMF',w,q),'probability-equally-likely','probability-binomial',True)
for w,ids in [(5,[10]),('5HW',[4]),('5Rev',[5])]:
    for q in ids:move(enrichment('PMF',w,q),'probability-independent','probability-binomial',True)
# Clear unrelated keyword matches without certifying those destination lessons.
for w,q in [(1,4),('1HW',4),('1Rev',3)]:move(source(11,1,w,q),'probability-binomial','polynomials-structure')
for w,q in [(1,6),('1Rev',2),(2,6),('2Rev',2)]:move(source(7,6,w,q),'probability-binomial','factoring-polynomials')
for w,ids in [(1,[8,10]),('1HW',[5]),('1Rev',[5]),(2,[7]),('2HW',[5]),(3,[3]),('3HW',[2]),(4,[3]),('4HW',[2]),(5,[1]),('5Rev',[1])]:
    for q in ids:move(source(7,9,w,q),'probability-complements','geometry-angle-relationships')
for w,ids in [(2,[4,7]),('2HW',[3]),('2Rev',[3])]:
    for q in ids:move(source(5,14,w,q),'probability-conditional','measurement-unit-choice')
for w,q in [(7,2),('7HW',4)]:move(source(6,11,w,q),'probability-complements','statistics-median',True)
move(source(11,10,'1Rev',2),'probability-equally-likely','statistics-sampling')


def apply_review(doc):
    changes=[];count=0
    for (file,qid),old,new in MOVES:
        p=doc['worksheets'][file]['problems'][qid]
        assert new in doc['videos']
        assert len(p['video_links'])==1,(file,qid)
        if p['video_links'][0]['video_id']==new:continue
        assert p['video_links'][0]['video_id']==old,(file,qid,old,p['video_links'])
        p['video_links'][0]['video_id']=new
        p.update(mapping_method='manual',mapping_status='needs_review',mapping_rule='probability-content-review-1',
                 notes='Inspected problem method corrects an overly broad keyword match. Destination coverage remains draft unless separately approved.')
        changes.append((file,qid,old,new))
    for (file,qid),vid in set(REVIEWED):
        p=doc['worksheets'][file]['problems'][qid]
        assert len(p['video_links'])==1 and p['video_links'][0]['video_id']==vid,(file,qid,vid,p['video_links'])
        assert not p['requires_source_visual'],(file,qid)
        if p['mapping_status']=='reviewed':continue
        p.update(mapping_method='manual',mapping_status='reviewed',mapping_rule='probability-content-review-1',
                 notes='Inspected against the authored analogous example: same calculation or concept, distinct example inputs, suitable prerequisites. Other links remain draft.')
        count+=1
    return changes,count


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True);parser.add_argument('--check',action='store_true');args=parser.parse_args()
    path=args.output/'worksheet-video-correspondence.json';doc=json.loads(path.read_text())
    assert not any(v['production_status']=='in_progress' for v in doc['videos'].values())
    before={k:v['youtube'].copy() for k,v in doc['videos'].items()}
    changes,count=apply_review(doc)
    assert before=={k:v['youtube'] for k,v in doc['videos'].items()}
    validate(doc,read_inventory(),asset_root=args.output.parent)
    if not args.check:
        save_json(path,doc);update_overview(args.output,doc,[s['video_id'] for s in SPECS])
    print(f'{len(changes)} corrected links; {count} reviewed references; check only: {args.check}')
    for change in changes:print(*change,sep=' | ')


if __name__=='__main__':main()
