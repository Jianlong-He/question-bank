"""Bounded content review for the number-sense production batch.

Only the explicitly inspected worksheet references below are approved. Other
links remain drafts, even when they point at a newly completed MP4.
"""
from video_reuse import append_upload_row, update_reuse_checklist
import argparse
import json
import re
from pathlib import Path
from number_sense_lessons import SPECS, source
from build_video_correspondence import read_inventory, validate
from generate_video_batch import save_json, update_overview


REVIEWED = [(tuple(s['source_ref']),s['video_id']) for s in SPECS if s['video_id']!='fractions-compare']


def add(vid,grade,unit,worksheet,ids):
    REVIEWED.extend((source(grade,unit,worksheet,q),vid) for q in ids)


add('number-place-value-whole-numbers',1,1,3,[10])
add('number-place-value-whole-numbers',1,1,4,[4,5,6])
add('number-place-value-expanded-form',2,2,2,[1,2,4])
add('number-place-value-expanded-form',2,2,'3Rev',[1])
add('number-place-value-decimals',5,1,1,[1,3,5])
add('number-place-value-decimals',5,1,'1HW',[2,3])
add('number-place-value-decimals',5,1,'2Rev',[5])
add('number-place-value-decimals',5,1,'3Rev',[2])
add('number-place-value-decimals',5,1,'5Rev',[1])
add('number-rounding-whole',3,3,2,[2,6])
add('number-rounding-decimals',5,1,5,[5,7])
add('number-rounding-decimals',5,1,'5HW',[2,5])
add('fractions-equivalent',4,7,1,[1,2,10])
add('fractions-equivalent',5,4,1,[4,5])
add('fractions-common-denominator',4,7,2,[2,3,6,8])
add('fractions-common-denominator',4,7,'2HW',[1,2,3])
add('fractions-common-denominator',4,7,'2Rev',[1,2,3])
add('fractions-mixed-improper',4,8,3,range(1,11))
add('fractions-mixed-improper',4,8,'3HW',range(1,6))
add('fractions-mixed-improper',4,8,'3Rev',range(1,6))
add('decimal-fraction-conversion-to-decimal',5,2,1,range(1,8))
add('decimal-fraction-conversion-to-decimal',5,2,'1HW',[1,2,4])
add('decimal-fraction-conversion-to-fraction',5,2,1,[8,10])
add('decimal-fraction-conversion-to-fraction',5,2,'1HW',[3,5])
add('number-theory-factors',4,6,1,[1,2,3,4])
add('number-theory-factors',4,6,'1HW',[3])
add('number-theory-factors',4,6,'1Rev',[1,2,3,4])
add('number-theory-gcf',6,6,9,[1,2,4,5,6,7])
add('number-theory-gcf',6,6,'9HW',[1,2,3,4])
add('number-theory-gcf',6,6,'9Rev',[1,2,3])
add('number-theory-lcm',5,4,2,[2,3,8])
add('number-theory-lcm',5,4,3,[1,2])
add('number-theory-lcm',5,4,4,[4,6])
add('number-theory-prime-composite',4,6,'2Rev',[1])


def apply_review(doc):
    changes=[]
    new_id='number-theory-smallest-with-prime-divisor-count'
    if new_id not in doc['videos']:
        title='Find the smallest number with a prime number of divisors'
        doc['videos'][new_id]={
            'title':title,'question_type':title,'curriculum':{'kind':'shared','topic':'number-theory'},
            'production_status':'planned','target_duration_seconds':60,'duration_seconds':None,
            'example':None,'assets':{'mp4':None,'captions':None},'youtube':{'video_id':None,'visibility':None},
            'notes':'Split from integer factor-pair listing after reviewing the reverse divisor-count problem.',
            'planning':{'basis':'rule','rule':new_id,'review_status':'reviewed'}}
    def move(ref,old,new,reason):
        file,qid=ref;p=doc['worksheets'][file]['problems'][qid]
        if len(p['video_links'])==1 and p['video_links'][0]['video_id']==new:return
        assert len(p['video_links'])==1 and p['video_links'][0]['video_id']==old,(ref,old)
        assert new in doc['videos']
        p['video_links'][0]['video_id']=new
        p.update(mapping_method='manual',mapping_status='needs_review',mapping_rule='number-sense-content-review-1',
                 notes=reason+' The destination example still needs its suitability check.')
        changes.append((file,qid,old,new))
    # These two whole grade/unit families were inspected in the factor-pairs group.
    for file,w in doc['worksheets'].items():
        for qid,p in w['problems'].items():
            if not any(l['video_id']=='number-theory-factors' for l in p['video_links']):continue
            if file.startswith('worksheets/Grade 11/G11Unit 3/'):
                target='polynomials-long-division' if file.endswith('/G11U3W2.csv') and qid=='8' else 'polynomials-zeros'
                move((file,qid),'number-theory-factors',target,'The question concerns polynomial factors and zeros, rather than positive integer factor pairs.')
            elif file.startswith(('worksheets/Grade 7/G7Unit 8/','worksheets/Grade 8/G8Unit 6/')):
                assert 'scaled' in p['question_text'].lower() or 'dilated' in p['question_text'].lower()
                move((file,qid),'number-theory-factors','geometry-dilation','The question uses a geometric scale factor, not integer factor pairs.')
    move(('worksheets/enrichment/number-theory 1/U2prime-factorization/E-NT1U2W1HWb.csv','4'),
         'number-theory-factors',new_id,'Constructs the smallest number having a specified prime divisor count.')
    for worksheet,qid,old in [('3',7,'fractions-equivalent'),('3HW',2,'fractions-equivalent'),
                              ('3',10,'algebra-rearrange-formula'),('3HW',5,'algebra-rearrange-formula')]:
        move(source(4,8,worksheet,qid),old,'fractions-mixed-improper','Converts a mixed number into an improper fraction with its original denominator.')
    for worksheet in ['3','3Rev']:
        move(source(10,4,worksheet,3 if worksheet=='3' else 1),'number-theory-prime-composite','numbers-rational-irrational',
             'Classifies the square root of a prime as rational or irrational; the primality of the input is already given.')
    base='worksheets/enrichment/counting-and-probability 1/U4conditional-probability/'
    move((base+'E-CP1U4W1.csv','1'),'number-theory-prime-composite','probability-equally-likely',
         'Counts favorable prime outcomes in a probability sample space.')
    move((base+'E-CP1U4W1Rev.csv','1'),'number-theory-prime-composite','probability-conditional',
         'Conditions on a prime result before counting the desired outcomes.')
    reviewed=0
    for (file,qid),vid in sorted(set(REVIEWED)):
        p=doc['worksheets'][file]['problems'][qid]
        assert len(p['video_links'])==1 and p['video_links'][0]['video_id']==vid,(file,qid,vid)
        assert not p['requires_source_visual'],(file,qid)
        if p['mapping_status']=='reviewed':continue
        p.update(mapping_method='manual',mapping_status='reviewed',mapping_rule='number-sense-content-review-1',
                 notes='Reviewed against the authored number-sense example: the same method with different input values and appropriate prerequisites. This does not approve other draft links in the group.')
        reviewed+=1
    refs=[p for w in doc['worksheets'].values() for p in w['problems'].values() if any(l['video_id']=='number-theory-factors' for l in p['video_links'])]
    assert refs and all(p['mapping_status']=='reviewed' for p in refs)
    doc['videos']['number-theory-factors']['planning']['review_status']='reviewed'
    return changes,reviewed


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True);parser.add_argument('--check',action='store_true');args=parser.parse_args()
    path=args.output/'worksheet-video-correspondence.json';doc=json.loads(path.read_text())
    assert not any(v['production_status']=='in_progress' for v in doc['videos'].values()),'Wait for the active export.'
    before={k:v['youtube'].copy() for k,v in doc['videos'].items()}
    changes,reviewed=apply_review(doc)
    assert before=={k:doc['videos'][k]['youtube'] for k in before}
    validate(doc,read_inventory(),asset_root=args.output.parent)
    if not args.check:
        save_json(path,doc)
        checklist=args.output/'youtube-upload-checklist.md'
        content=checklist.read_text()
        for vid in set(doc['videos'])-set(before):
            assert vid+'.mp4' not in content
            content=append_upload_row(content,vid,doc["videos"][vid]["title"])
        content=re.sub(r'All [\d,]+ videos in the current plan\.',f'All {len(doc["videos"]):,} videos in the current plan.',content)
        checklist.write_text(update_reuse_checklist(content,doc))
        update_overview(args.output,doc,[s['video_id'] for s in SPECS])
    print(f'{len(changes)} corrected links; {reviewed} newly reviewed problems. Check only: {args.check}')
    for c in changes:print(*c,sep=' | ')


if __name__=='__main__':main()
