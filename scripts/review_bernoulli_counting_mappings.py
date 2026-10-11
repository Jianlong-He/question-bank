"""Review the final PMF methods against their CSV questions and worked solutions."""
import argparse,json,fcntl
from pathlib import Path
from bernoulli_counting_lessons import SPECS
from probability_lessons import enrichment as e
from video_reuse import append_upload_row,update_reuse_checklist,merge_reviewed_duplicate
from build_video_correspondence import validate,read_inventory
from generate_video_batch import save_json,update_overview

NEW={s['video_id']:s['topic'] for s in SPECS if s['video_id'] in {
 'probability-binomial-upper-tail','probability-not-all-successes','counting-binomial-coefficient-nonnegative',
 'counting-inclusive-index-range','probability-single-trial-failure'}}
APPROVED=[(tuple(s['source_ref']),s['video_id']) for s in SPECS]

def add(vid,w,qs):APPROVED.extend((e('PMF',w,q),vid) for q in qs)
add('probability-single-trial-failure','3Rev',[1])
add('pattern-pmf-d93d36d25e19',3,[3,4,9]);add('pattern-pmf-d93d36d25e19','3Rev',[2,3])
add('pattern-pmf-d93d36d25e19','3HW',[2,4])
add('pattern-pmf-fc49f9797eeb',5,[4]);add('pattern-pmf-fc49f9797eeb','5HW',[1])
add('counting-combinations','5HW',[2])
add('probability-first-success-first',5,[5]);add('probability-first-success-first','5HW',[3])
add('enrichment-counting-and-probability-1-first-red-on-second-draw','1HW',[4])

# Complete original ref sets are checked by merge_reviewed_duplicate. Wait until
# the replacement has been rendered before retiring any draft or removing its row.
MERGES=[
 ('pattern-pmf-2231a9075127','pattern-pmf-488f17f2e44d',e('PMF','3Rev',4)),
 ('pattern-pmf-e5ed9a51d9bd','pattern-pmf-d93d36d25e19',e('PMF','3HW',3)),
 ('pattern-pmf-3b1fd5258ab0','pattern-pmf-ea9fc03d2b5b',e('PMF','3HW',5)),
 ('pattern-pmf-b3239265ae44','counting-combinations',e('PMF',5,3)),
 ('pattern-pmf-19e53928ef08','probability-equally-likely',e('PMF','3HW',1)),
]


def apply_review(doc,merge=False):
    changed=[];reviewed=0
    for vid,title in NEW.items():
        if vid not in doc['videos']:
            doc['videos'][vid]={
             'title':title,'question_type':title,'curriculum':{'kind':'shared','topic':'probability'},
             'production_status':'planned','target_duration_seconds':60,'duration_seconds':None,
             'example':None,'assets':{'mp4':None,'captions':None},'youtube':{'video_id':None,'visibility':None},
             'notes':'Distinct method found in explicit PMF question and solution review.',
             'planning':{'basis':'rule','rule':vid,'review_status':'needs_review'}}
    for (file,qid),vid in sorted(set(APPROVED)):
        p=doc['worksheets'][file]['problems'][qid]
        assert len(p['video_links'])==1 and not p['requires_source_visual'],(file,qid)
        old=p['video_links'][0]['video_id']
        if old!=vid:changed.append((file,qid,old,vid));p['video_links'][0]['video_id']=vid
        if p['mapping_status']!='reviewed':reviewed+=1
        p.update(mapping_method='manual',mapping_status='reviewed',mapping_rule='bernoulli-counting-review-1',
                 notes='Question and CSV solution inspected: the analogous example teaches the same method with different inputs.')
        if (file,qid)==e('PMF','1HW',4):p['notes']+=' The worksheet hints assume uniformly random key order, matching the random-draw model.'
    merged=0
    if merge:
        for old,new,ref in MERGES:
            if doc['videos'][old].get('reuse_video_ids')==[new]:continue
            merge_reviewed_duplicate(doc,old,{ref:new});merged+=1
    for s in SPECS:
        v=doc['videos'][s['video_id']];v['title']=s['topic'];v['question_type']=s['topic']
        refs=[p for w in doc['worksheets'].values() for p in w['problems'].values() if any(l['video_id']==s['video_id'] for l in p['video_links'])]
        if refs and all(p['mapping_status']=='reviewed' for p in refs):v['planning']['review_status']='reviewed'
    return changed,reviewed,merged


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True);parser.add_argument('--check',action='store_true');parser.add_argument('--merge',action='store_true');args=parser.parse_args()
    root=Path(__file__).resolve().parents[1]
    with (root/'videos/.production.lock').open('a+') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        path=args.output/'worksheet-video-correspondence.json';doc=json.loads(path.read_text())
        assert not any(v['production_status']=='in_progress' for v in doc['videos'].values())
        before={k:(v['youtube'].copy(),v['assets'].copy()) for k,v in doc['videos'].items()}
        changed,reviewed,merged=apply_review(doc,args.merge)
        assert before=={k:(doc['videos'][k]['youtube'],doc['videos'][k]['assets']) for k in before}
        validate(doc,read_inventory(),asset_root=args.output.parent)
        from bernoulli_counting_lessons import lessons
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
        print(f'{len(changed)} corrected links; {reviewed} newly reviewed refs; {merged} drafts reused. Check only: {args.check}')
        for c in changed:print(*c,sep=' | ')


if __name__=='__main__':main()
