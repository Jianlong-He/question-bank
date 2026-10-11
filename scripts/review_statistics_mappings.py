"""Explicit statistical-method splits and inspected worksheet suitability checks."""
from video_reuse import append_upload_row, update_reuse_checklist
import argparse
import json
from pathlib import Path
import re
from statistics_lessons import SPECS
from number_sense_lessons import source
from build_video_correspondence import validate, read_inventory
from generate_video_batch import save_json, update_overview


NEW={
 'statistics-mean-absolute-deviation':'Find the mean absolute deviation',
 'statistics-missing-value-from-mean':'Find a missing data value from the mean',
 'statistics-box-plot-summary':'Read a box plot, range and interquartile range',
}
TITLES={
 'statistics-spread':'Compare spread using the range',
 'statistics-normal-distribution':'Read a normal distribution and standard-deviation intervals',
 'statistics-standard-deviation':'Apply the normal-distribution empirical rule',
}
REVIEWED=[(tuple(s['source_ref']),s['video_id']) for s in SPECS]


def add(vid,grade,unit,worksheet,ids):
    REVIEWED.extend((source(grade,unit,worksheet,q),vid) for q in ids)


for w,ids in [(4,[1,2,3,6]),('4HW',[1,2,5]),('4Rev',[1]),(6,[1]),('6HW',[1]),(10,[2]),('10HW',[2])]:
    add('statistics-mean',6,11,w,ids)
for w,ids in [(2,[1,7]),('2HW',[1]),('2Rev',[1])]:add('statistics-mean',9,10,w,ids)
for w,ids in [(4,[4,7,8,10]),('4HW',[3]),('4Rev',[2,3]),(6,[2,6]),('6HW',[2]),('6Rev',[1])]:
    add('statistics-median',6,11,w,ids)
for w,ids in [(2,[2]),('2HW',[2,5]),('2Rev',[2]),(3,[3]),('3HW',[2]),('3Rev',[2])]:
    add('statistics-median',9,10,w,ids)
for w,ids in [(2,[8]),('2HW',[5]),('2Rev',[5]),(4,[5,11]),('4HW',[4]),('4Rev',[5]),(5,[8]),('5Rev',[4]),(6,[3,9]),('6HW',[3]),('6Rev',[4])]:
    add('statistics-mode',6,11,w,ids)
for w in [2,'2HW','2Rev']:add('statistics-mode',9,10,w,[3])
for w,ids in [(1,[2,5,9]),('1HW',[1,4]),('1Rev',[4]),(2,[5,10]),('2HW',[3]),('2Rev',[4])]:
    add('statistics-spread',6,11,w,ids)
for w,ids in [(1,[1,2,6,8,9]),('1HW',[1,2]),('1Rev',[3])]:
    add('statistics-normal-distribution',11,12,w,ids)
for w,ids in [(1,[3,4,5]),('1HW',[3,4,5]),('1Rev',[1,2])]:
    add('statistics-standard-deviation',11,12,w,ids)
add('statistics-z-scores',11,12,1,[10]);add('statistics-z-scores',11,12,'1Rev',[4,5])
for w,ids in [(10,[3]),('10HW',[3]),(6,[2,4]),('6HW',[2]),('6Rev',[1])]:
    add('statistics-regression',8,7,w,ids)
add('statistics-correlation',11,10,1,[7])
BOX_REFS=[]
def box(grade,unit,w,ids,review=True):
    refs=[source(grade,unit,w,q) for q in ids];BOX_REFS.extend(refs)
    if review:REVIEWED.extend((r,'statistics-box-plot-summary') for r in refs)
box(6,11,8,[1,2,10]);box(6,11,'8HW',[1,2,3,4]);box(6,11,'8Rev',[1,2,3,5])
box(6,11,8,[4,5,6,9],False);box(6,11,'8HW',[5],False);box(6,11,'8Rev',[4],False)
box(6,11,'9HW',[1]);box(6,11,'9Rev',[1])
box(9,10,3,[1,2,4,7,8]);box(9,10,'3HW',[1,3]);box(9,10,'3Rev',[1,4])


def apply_review(doc):
    changes=[]
    for vid,title in NEW.items():
        if vid not in doc['videos']:
            doc['videos'][vid]={
                'title':title,'question_type':title,'curriculum':{'kind':'shared','topic':'statistics'},
                'production_status':'planned','target_duration_seconds':60,'duration_seconds':None,
                'example':None,'assets':{'mp4':None,'captions':None},'youtube':{'video_id':None,'visibility':None},
                'notes':'A distinct teaching method split from a broader draft statistics group.',
                'planning':{'basis':'rule','rule':vid,'review_status':'needs_review'}}
    def move(ref,old,new,reason):
        file,qid=ref;p=doc['worksheets'][file]['problems'][qid]
        if len(p['video_links'])==1 and p['video_links'][0]['video_id']==new:return
        assert len(p['video_links'])==1 and p['video_links'][0]['video_id'] in old,(ref,p['video_links'])
        previous=p['video_links'][0]['video_id'];p['video_links'][0]['video_id']=new
        p.update(mapping_method='manual',mapping_status='needs_review',mapping_rule='statistics-content-review-1',
                 notes=reason+' Destination example suitability still requires review unless explicitly approved below.')
        changes.append((file,qid,previous,new))
    newly_reviewable=[]
    for file,w in doc['worksheets'].items():
        for qid,p in w['problems'].items():
            if not any(l['video_id']=='statistics-mean' for l in p['video_links']):continue
            q=p['question_text'].lower()
            if file.startswith('worksheets/Grade 6/G6Unit 11/G6U11W10') and ('deviation' in q or 'distance of each value' in q):
                move((file,qid),{'statistics-mean'},'statistics-mean-absolute-deviation','Finds or interprets distances from the mean and their average.')
                newly_reviewable.append(((file,qid),'statistics-mean-absolute-deviation'))
            elif re.search(r'missing (?:age|number|value)',q) and 'mean' in q and file.startswith(('worksheets/Grade 6/G6Unit 11/','worksheets/Grade 9/G9Unit 10/')):
                move((file,qid),{'statistics-mean'},'statistics-missing-value-from-mean','Uses mean times count to recover a total and subtract known values.')
                newly_reviewable.append(((file,qid),'statistics-missing-value-from-mean'))
    for ref in BOX_REFS:
        move(ref,{'statistics-mean','statistics-median','statistics-spread','statistics-data-displays'},'statistics-box-plot-summary',
             'Reads a five-number summary, quartile interval or range from a box plot.')
    for worksheet in [2,'2HW','2Rev']:
        ref=source(9,10,worksheet,4)
        move(ref,{'statistics-mean'},'statistics-missing-value-from-mean','Uses the mean and count to solve for the unknown data value.')
        newly_reviewable.append((ref,'statistics-missing-value-from-mean'))
    for qid in [4,5]:
        ref=source(1,1,3,qid)
        move(ref,{'statistics-mean'},'number-place-value-whole-numbers','The word mean asks for digit place value, not a statistical average.')
        newly_reviewable.append((ref,'number-place-value-whole-numbers'))
    for w,q in [(2,7),('2Rev',3)]:
        ref=source(8,7,w,q)
        move(ref,{'statistics-regression'},'statistics-correlation','A negative slope identifies negative association.')
        newly_reviewable.append((ref,'statistics-correlation'))
    # Preserve manual approvals on repeated runs; direct move references are fixed.
    approved=set(REVIEWED+newly_reviewable)
    count=0
    for (file,qid),vid in sorted(approved):
        p=doc['worksheets'][file]['problems'][qid]
        assert len(p['video_links'])==1 and p['video_links'][0]['video_id']==vid,(file,qid,vid)
        assert not p['requires_source_visual'],(file,qid)
        if p['mapping_status']=='reviewed':continue
        p.update(mapping_method='manual',mapping_status='reviewed',mapping_rule='statistics-content-review-1',
                 notes='Reviewed against the authored statistics example: same method, original example data and suitable prerequisites. Other draft links in the group remain unapproved.')
        count+=1
    for vid in ['statistics-mean-absolute-deviation','statistics-missing-value-from-mean','statistics-standard-deviation','statistics-z-scores']:
        refs=[p for w in doc['worksheets'].values() for p in w['problems'].values() if any(l['video_id']==vid for l in p['video_links'])]
        assert refs and all(p['mapping_status']=='reviewed' for p in refs),vid
        doc['videos'][vid]['planning']['review_status']='reviewed'
    for vid,title in TITLES.items():
        doc['videos'][vid]['title']=title
        doc['videos'][vid]['question_type']=title
    return changes,count


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True);parser.add_argument('--check',action='store_true');args=parser.parse_args()
    path=args.output/'worksheet-video-correspondence.json';doc=json.loads(path.read_text())
    assert not any(v['production_status']=='in_progress' for v in doc['videos'].values())
    before={k:v['youtube'].copy() for k,v in doc['videos'].items()}
    changes,count=apply_review(doc)
    assert before=={k:doc['videos'][k]['youtube'] for k in before}
    validate(doc,read_inventory(),asset_root=args.output.parent)
    if not args.check:
        save_json(path,doc)
        checklist=args.output/'youtube-upload-checklist.md';content=checklist.read_text()
        for vid in sorted(set(doc['videos'])-set(before)):
            assert vid+'.mp4' not in content
            content=append_upload_row(content,vid,doc["videos"][vid]["title"])
        lines=content.splitlines()
        for i,line in enumerate(lines):
            for vid,title in TITLES.items():
                if f'| {vid}.mp4 |' in line:
                    cells=line.split('|');cells[1]=' '+title+' ';lines[i]='|'.join(cells)
        content='\n'.join(lines)+'\n'
        content=re.sub(r'All [\d,]+ videos in the current plan\.',f'All {len(doc["videos"]):,} videos in the current plan.',content)
        checklist.write_text(update_reuse_checklist(content,doc))
        update_overview(args.output,doc,[s['video_id'] for s in SPECS])
    print(f'{len(changes)} corrected links; {count} reviewed problem mappings. Check only: {args.check}')
    for c in changes:print(*c,sep=' | ')


if __name__=='__main__':main()
