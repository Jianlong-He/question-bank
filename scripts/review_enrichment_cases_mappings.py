"""Reviewed enrichment cases and reuse of existing grade and counting methods."""
import argparse,fcntl,json
from pathlib import Path
from enrichment_cases_lessons import SPECS,lessons
from probability_lessons import enrichment as e
from video_reuse import append_upload_row,update_reuse_checklist,merge_reviewed_duplicate
from build_video_correspondence import validate,read_inventory
from generate_video_batch import save_json,update_overview
from video_example_checks import require_analogous_examples

APPROVED=[(tuple(s['source_ref']),s['video_id']) for s in SPECS]
def en(vid,topic,w,qs):APPROVED.extend((e(topic,w,q),vid) for q in qs)
en('counting-all-equal-choices','PCF','6HW',[3])
en('counting-triples-fixed-product','PCF','6Rev',[1])
en('counting-triples-product-threshold','PCF',6,[9])
en('counting-codes-at-least-one-target','PCF','6Rev',[3])
for w,qs in [(3,[4,9]),('3HW',[3]),('3Rev',[3])]:en('counting-pascal-identity','PeCo',w,qs)
en('counting-permutation-overcount-factor','PeCo','1Rev',[4]);en('counting-permutation-overcount-factor','PeCo',2,[7])
for w,qs in [(4,[1,2]),('4HW',[1,2]),(5,[1]),('5HW',[1])]:en('arithmetic-evaluate-powers','PCF',w,qs)
en('arithmetic-distribute-two-sums','PCF','3Rev',[5])
en('geometry-volume-rectangular-prism','PCF','1Rev',[2])
for w,qs in [(2,[1,4,8]),('2Rev',[3]),(3,[10])]:en('enrichment-counting-and-probability-1-choose-three','PeCo',w,qs)
en('enrichment-counting-and-probability-1-choosing-a-pair','PeCo',2,[2]);en('enrichment-counting-and-probability-1-choosing-a-pair','PeCo','2Rev',[1])
en('counting-combination-symmetry','PeCo',3,[1])
MERGES=[
 ('pattern-pcf-f39efd97d137','g3-u1-equal-groups',[e('PCF',1,3)]),
 ('pattern-pcf-7994442dd560','g3-u1-equal-groups',[e('PCF','1HW',3)]),
 ('pattern-pcf-9d3707bb426f','geometry-volume-rectangular-prism',[e('PCF',1,7)]),
 ('pattern-pcf-975d2d4c80ad','counting-permutations',[e('PCF',4,7)]),
 ('pattern-pcf-52f25f9bee77','counting-permutations',[e('PCF',4,8)]),
 ('pattern-pcf-8bf23665aea7','counting-permutations',[e('PCF','4Rev',2)]),
 ('pattern-pcf-208e5b70fcc8','counting-permutations',[e('PCF','4Rev',3)]),
 ('pattern-pcf-6f5e3b65d9c8','counting-sum-then-product',[e('PCF',3,8)]),
 ('pattern-pcf-7f47a3825c7f','counting-dice-consecutive-runs',[e('PCF','6Rev',2)]),
 ('pattern-pcf-30392f9f7add','pattern-pcf-1c8d6c2baaec',[e('PCF','1Rev',4)])]


def apply_review(doc,merge=False):
    changes=[];reviewed=0
    for s in SPECS:
        vid=s['video_id'];title=s['topic']
        if vid not in doc['videos']:
            doc['videos'][vid]={'title':title,'question_type':title,'curriculum':{'kind':'shared','topic':'counting'},
             'production_status':'planned','target_duration_seconds':60,'duration_seconds':None,'example':None,
             'assets':{'mp4':None,'captions':None},'youtube':{'video_id':None,'visibility':None},
             'notes':'Distinct counting method identified through explicit question review.',
             'planning':{'basis':'rule','rule':vid,'review_status':'needs_review'}}
    for (file,qid),vid in sorted(set(APPROVED)):
        p=doc['worksheets'][file]['problems'][qid]
        assert len(p['video_links'])==1 and not p['requires_source_visual'],(file,qid)
        old=p['video_links'][0]['video_id']
        if old!=vid:changes.append((file,qid,old,vid));p['video_links'][0]['video_id']=vid
        reviewed+=p['mapping_status']!='reviewed'
        p.update(mapping_method='manual',mapping_status='reviewed',mapping_rule='enrichment-cases-review-1',
          notes='Inspected against the authored analogous example: matching counting method and prerequisite steps; different numerical inputs.')
    if merge:
        for old,new,refs in MERGES:
            if doc['videos'][old].get('reuse_video_ids')==[new]:continue
            merge_reviewed_duplicate(doc,old,{ref:new for ref in refs})
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
        # Recheck every completed lesson receiving additional worksheet links.
        for vid,v in doc['videos'].items():
            if v['production_status']=='rendered' and v.get('example'):
                require_analogous_examples(doc,[{'video_id':vid,'question':v['example']['question']}])
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
