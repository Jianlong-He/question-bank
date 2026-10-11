"""Explicit PMF/counting review, including composed coverage where methods combine."""
import argparse,json
from pathlib import Path
from pmf_counting_lessons import SPECS
from probability_lessons import enrichment
from number_sense_lessons import source
from video_reuse import append_upload_row,update_reuse_checklist
from build_video_correspondence import validate,read_inventory
from generate_video_batch import save_json,update_overview

NEW={s['video_id']:s['topic'] for s in SPECS if s['video_id'] in {
 'probability-pmf-normalization','probability-geometric-ratio','probability-geometric-disjoint-times','probability-hypergeometric-complement'}}
APPROVED=[(tuple(s['source_ref']),s['video_id']) for s in SPECS]
CORRECTIONS=[]


def e(vid,topic,w,ids):APPROVED.extend((enrichment(topic,w,q),vid) for q in ids)
def g(vid,grade,unit,w,ids):APPROVED.extend((source(grade,unit,w,q),vid) for q in ids)


e('probability-pmf-normalization','PMF',1,[9]);e('probability-pmf-normalization','PMF','1Rev',[5])
for w,ids in [(2,[9]),('2HW',[5]),('2Rev',[1]),(4,[8]),('4HW',[4])]:e('probability-geometric-ratio','PMF',w,ids)
for w,ids in [(7,[1,2,4,7,8]),('7Rev',[1,2,4])]:e('pattern-pmf-803aa2d4d578','PMF',w,ids)
for w,ids in [(2,[2,9]),('2HW',[3]),('2Rev',[2,4]),(3,[7])]:e('probability-hypergeometric-complement','conditional-probability',w,ids)
e('counting-combinations','PMF',6,[2]);e('counting-combinations','PMF','7HW',[3]);e('counting-combinations','PMF',3,[2])
for w,ids in [(1,[7]),('1HW',[4,5]),('1Rev',[5]),(2,[3,5,6]),('2HW',[1,2,3,4,5]),('2Rev',[2]),(3,[2,3,7]),('3HW',[2]),('3Rev',[2])]:e('counting-combinations','PeCo',w,ids)
for grade,unit,w,ids in [(10,13,2,[1]),(10,13,'2Rev',[5]),(12,8,3,[1]),(12,8,'3HW',[1,5]),(12,8,'3Rev',[2,5])]:g('counting-combinations',grade,unit,w,ids)
for w,ids in [(2,[1,2]),('2HW',[1,2]),('2Rev',[1])]:g('counting-factorials',12,8,w,ids)
for w,ids in [(4,[3]),('4HW',[3]),(5,[2]),('5HW',[2])]:e('counting-factorials','PCF',w,ids)
APPROVED.append((('worksheets/enrichment/number-theory 1/U6RSA/E-NT1U6W3.csv','1'),'counting-factorials'))
g('pattern-probability-and-combinatorics-748de98e98f6',12,8,5,[5])
e('enrichment-counting-and-probability-1-first-red-on-second-draw','PMF','1HW',[2])
# Expanded cross-topic use needs a different hypergeometric example: the old 5-red,
# 6-blue data exactly matched this favourable-count question. Its revised example
# uses 6 red and 7 blue; the existing filename is retained and re-rendered.
e('pattern-pmf-bfe65fc756d0','PeCo','2Rev',[5])
for w,ids in [(1,[4,8,9,10]),('1HW',[1,2,3]),('1Rev',[1,2,3]),(3,[5]),('3HW',[4]),('3Rev',[4])]:
    CORRECTIONS.extend((enrichment('PeCo',w,q),'counting-permutations') for q in ids)
CORRECTIONS += [(source(9,15,2,5),'geometry-translation'),(source(9,15,'2HW',5),'geometry-translation'),
                (source(9,15,3,6),'geometry-reflection'),(source(9,18,1,8),'geometry-midpoint'),
                (enrichment('PCF','3HW',5),'counting-product-rule'),
                (enrichment('counting-and-classification','4HW',5),'counting-product-rule'),
                (enrichment('counting-and-classification','2Rev',1),'counting-permutations')]
COMPOSED=[enrichment('PMF',4,6),enrichment('PMF','4Rev',4)]


def apply_review(doc):
    changes=[];count=0
    for vid,title in NEW.items():
        if vid not in doc['videos']:
            doc['videos'][vid]={
             'title':title,'question_type':title,'curriculum':{'kind':'shared','topic':'probability'},
             'production_status':'planned','target_duration_seconds':60,'duration_seconds':None,
             'example':None,'assets':{'mp4':None,'captions':None},'youtube':{'video_id':None,'visibility':None},
             'notes':'Explicit distinct probability method identified while reviewing the worksheet plan.',
             'planning':{'basis':'rule','rule':vid,'review_status':'needs_review'}}
    def assign(ref,vid,review):
        nonlocal count
        file,qid=ref;p=doc['worksheets'][file]['problems'][qid]
        assert len(p['video_links'])==1 and not p['requires_source_visual'],ref
        old=p['video_links'][0]['video_id']
        assert doc['videos'][old]['production_status']!='retired',old
        if old!=vid:p['video_links'][0]['video_id']=vid;changes.append((file,qid,old,vid))
        if review and p['mapping_status']!='reviewed':count+=1
        p.update(mapping_method='manual',mapping_status='reviewed' if review else 'needs_review',mapping_rule='pmf-counting-review-1',
                 notes=('Inspected against the authored example: same method, different numerical inputs, suitable prerequisites.' if review else
                        'Corrected a counting keyword false match; the destination method still needs example review.'))
    for ref,vid in CORRECTIONS:assign(ref,vid,False)
    for ref,vid in sorted(set(APPROVED)):assign(ref,vid,True)
    for file,qid in COMPOSED:
        p=doc['worksheets'][file]['problems'][qid]
        if p['mapping_status']!='reviewed':count+=1
        old=[l['video_id'] for l in p['video_links']]
        p['video_links']=[{'video_id':vid,'coverage':'partial','example_mode':'similar_question','variant_index':None,'start_seconds':0,'end_seconds':None}
                          for vid in ['probability-geometric-ratio','pattern-pmf-4be2809cd266']]
        p.update(mapping_method='manual',mapping_status='reviewed',mapping_rule='pmf-counting-review-1',
                 notes='Two reviewed shared examples together cover this problem: recognize the successive ratio as failure probability, then raise that failure probability to the required waiting time.')
        if old!=[l['video_id'] for l in p['video_links']]:changes.append((file,qid,','.join(old),'ratio + geometric tail'))
    for s in SPECS:
        v=doc['videos'][s['video_id']];v['title']=s['topic'];v['question_type']=s['topic']
        refs=[p for w in doc['worksheets'].values() for p in w['problems'].values() if any(l['video_id']==s['video_id'] for l in p['video_links'])]
        if refs and all(p['mapping_status']=='reviewed' for p in refs):v['planning']['review_status']='reviewed'
    hyper=doc['videos']['pattern-pmf-bfe65fc756d0']
    if hyper.get('example',{}).get('answer')!='63/143':
        hyper['production_status']='needs_revision'
        hyper['notes']='Re-render the revised 6-red/7-blue example before publication; the earlier 5-red/6-blue example matched a newly discovered related worksheet count.'
    return changes,count


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True);parser.add_argument('--check',action='store_true');args=parser.parse_args()
    path=args.output/'worksheet-video-correspondence.json';doc=json.loads(path.read_text())
    assert not any(v['production_status']=='in_progress' for v in doc['videos'].values())
    before={k:v['youtube'].copy() for k,v in doc['videos'].items()}
    changes,count=apply_review(doc)
    assert before=={k:doc['videos'][k]['youtube'] for k in before}
    validate(doc,read_inventory(),asset_root=args.output.parent)
    content=(args.output/'youtube-upload-checklist.md').read_text()
    for vid in sorted(set(doc['videos'])-set(before)):content=append_upload_row(content,vid,doc['videos'][vid]['title'])
    titles={s['video_id']:s['topic'] for s in SPECS};lines=content.splitlines()
    for i,line in enumerate(lines):
        for vid,title in titles.items():
            if f'| {vid}.mp4 |' in line:
                cells=line.split('|');cells[1]=' '+title+' ';lines[i]='|'.join(cells)
    content=update_reuse_checklist('\n'.join(lines)+'\n',doc)
    if not args.check:
        save_json(path,doc);(args.output/'youtube-upload-checklist.md').write_text(content)
        update_overview(args.output,doc,[s['video_id'] for s in SPECS])
    print(f'{len(changes)} corrected links; {count} newly reviewed references. Check only: {args.check}')
    for c in changes:print(*c,sep=' | ')


if __name__=='__main__':main()
