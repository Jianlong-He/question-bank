"""Inspected method splits; reuse existing planned template IDs when appropriate."""
from video_reuse import append_upload_row, update_reuse_checklist
import argparse,json,re
from pathlib import Path
from probability_extension_lessons import SPECS
from probability_lessons import enrichment
from number_sense_lessons import source
from build_video_correspondence import validate,read_inventory
from generate_video_batch import save_json,update_overview

GEOMETRIC='pattern-pmf-90d35baa0439'
TAIL='pattern-pmf-4be2809cd266'
HYPER='pattern-pmf-bfe65fc756d0'
TITLES={
 GEOMETRIC:'Find the first success in geometric trials',
 TAIL:'Find geometric tail and cumulative probabilities',
 HYPER:'Calculate hypergeometric sampling probabilities',
 'probability-first-success':'Find the first success without replacement',
 'probability-first-success-first':'Find the probability of success on the first draw',
 'probability-first-success-support':'Find the latest possible first success without replacement',
 'probability-first-success-total':'Sum a complete finite waiting-time distribution',
 'probability-expected-count':'Predict the expected number of occurrences',
}
APPROVED=[(tuple(s['source_ref']),s['video_id']) for s in SPECS]


def pmf(vid,w,ids):APPROVED.extend((enrichment('PMF',w,q),vid) for q in ids)

for w,ids in [(1,[3,4,10]),('1HW',[3]),('1Rev',[1,2])]:pmf('probability-first-success',w,ids)
# The only-success position is uniform if random order is intended; key-testing wording
# does not explicitly randomize, so its interpretation is left for source review.
for w,ids in [(1,[1]),('1HW',[1]),(2,[1])]:pmf('probability-first-success-first',w,ids)
pmf('probability-first-success-total',1,[5]);pmf('probability-first-success-support',1,[6])
for w,ids in [(2,[2,3,4,5,10]),('2HW',[3,4]),('2Rev',[3]),(4,[1,2,3,9]),('4HW',[1,5])]:pmf(GEOMETRIC,w,ids)
for w,ids in [(2,[6,7,8]),('2Rev',[2,4,5]),(4,[4,10]),('4HW',[2,3]),('4Rev',[3,5])]:pmf(TAIL,w,ids)
for w,ids in [(6,[1,3,4,5,6,7,10]),('6HW',[1,2,3,4]),('6Rev',[1,2,3,4,5]),(7,[3,5,9]),('7HW',[2,4]),('7Rev',[3,5])]:pmf(HYPER,w,ids)
for grade,unit,w,q in [(10,13,1,8),(10,13,'1HW',3),(10,13,'1Rev',4),(11,11,1,6),(7,7,1,7),(7,7,'1HW',5)]:
    APPROVED.append((source(grade,unit,w,q),'probability-expected-count'))


def apply_review(doc):
    changes=[];count=0
    vid='probability-expected-count'
    if vid not in doc['videos']:
        doc['videos'][vid]={
          'title':TITLES[vid],'question_type':TITLES[vid],
          'curriculum':{'kind':'shared','topic':'probability'},
          'production_status':'planned','target_duration_seconds':60,'duration_seconds':None,
          'example':None,'assets':{'mp4':None,'captions':None},
          'youtube':{'video_id':None,'visibility':None},
          'notes':'Expected count n*p is distinct from a provided-distribution weighted average.',
          'planning':{'basis':'rule','rule':vid,'review_status':'needs_review'}}
    for (file,qid),vid in sorted(set(APPROVED)):
        p=doc['worksheets'][file]['problems'][qid]
        assert len(p['video_links'])==1 and not p['requires_source_visual'],(file,qid)
        old=p['video_links'][0]['video_id']
        assert old.startswith(('probability-','pattern-pmf-','enrichment-counting-and-probability-1-')),(file,qid,old)
        if old!=vid:
            p['video_links'][0]['video_id']=vid;changes.append((file,qid,old,vid))
        if p['mapping_status']!='reviewed':count+=1
        p.update(mapping_method='manual',mapping_status='reviewed',mapping_rule='probability-extension-review-1',
                 notes='Inspected against the distinct authored example. Matches finite/geometric waiting time, hypergeometric selection, or expected-count method; numerical example inputs differ.')
    for vid,title in TITLES.items():
        doc['videos'][vid]['title']=title;doc['videos'][vid]['question_type']=title
        refs=[p for w in doc['worksheets'].values() for p in w['problems'].values() if any(l['video_id']==vid for l in p['video_links'])]
        assert refs,vid
        if all(p['mapping_status']=='reviewed' for p in refs):
            doc['videos'][vid]['planning']['review_status']='reviewed'
    return changes,count


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True);parser.add_argument('--check',action='store_true');args=parser.parse_args()
    path=args.output/'worksheet-video-correspondence.json';doc=json.loads(path.read_text())
    assert not any(v['production_status']=='in_progress' for v in doc['videos'].values())
    before={k:v['youtube'].copy() for k,v in doc['videos'].items()}
    changes,count=apply_review(doc)
    assert before=={k:doc['videos'][k]['youtube'] for k in before}
    # No orphaned stable IDs are introduced by this review; remaining duplicates
    # must receive an explicit merge/reuse treatment, not be silently deleted.
    for old in set(c[2] for c in changes):
        assert any(l['video_id']==old for w in doc['worksheets'].values() for p in w['problems'].values() for l in p['video_links']),old
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
    print(f'{len(changes)} corrected links; {count} newly reviewed; check only: {args.check}')
    for c in changes:print(*c,sep=' | ')


if __name__=='__main__':main()
