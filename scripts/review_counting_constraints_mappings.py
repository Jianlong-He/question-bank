"""Explicit review of constrained counting; preserves IDs and user upload cells."""
import argparse,json,fcntl
from pathlib import Path
from counting_constraints_lessons import SPECS
from probability_lessons import enrichment as e
from number_sense_lessons import source as g
from video_reuse import append_upload_row,update_reuse_checklist,merge_reviewed_duplicate
from build_video_correspondence import validate,read_inventory
from generate_video_batch import save_json,update_overview

APPROVED=[(tuple(s['source_ref']),s['video_id']) for s in SPECS]
def en(vid,topic,w,qs):APPROVED.extend((e(topic,w,q),vid) for q in qs)
en('counting-fixed-roles','PeCo','4HW',[1])
en('counting-required-member','PeCo','2Rev',[4])
en('counting-combination-symmetry','PeCo','3Rev',[1])
en('counting-pairs-with-repetition','PeCo','3HW',[5]);en('counting-pairs-with-repetition','PeCo','3Rev',[5])
for w,qs in [(4,[2,3,5,7,8]),('4Rev',[2,3,5])]:en('counting-two-ordered-rows','PeCo',w,qs)
for w,qs in [(4,[9,10]),('4HW',[5]),('4Rev',[4])]:en('counting-nonempty-ordered-rows','PeCo',w,qs)
en('counting-identical-pair-adjacency','PCF','5Rev',[5])
en('counting-fixed-code-positions','counting-and-classification',4,[9]);en('counting-fixed-code-positions','counting-and-classification','4Rev',[2,4])
en('counting-fixed-code-positions','PCF',6,[2,4]);en('counting-fixed-code-positions','PCF','6HW',[2,4])
en('pattern-pmf-d313e72dd673','PeCo',3,[6])
APPROVED.append((g(12,8,2,9),'counting-permutations'))
MERGES=[('pattern-peco-ca584d004330','counting-arrangements',e('PeCo',4,1)),
 ('pattern-peco-94790bd16d4a','counting-two-ordered-rows',e('PeCo',4,4)),
 ('pattern-peco-497866a77824','counting-two-rows-insertion',e('PeCo',4,6))]


def apply_review(doc,merge=False):
    changed=[];reviewed=0
    for s in SPECS:
        vid=s['video_id'];title=s['topic']
        if vid not in doc['videos']:
            doc['videos'][vid]={
             'title':title,'question_type':title,'curriculum':{'kind':'shared','topic':'counting'},
             'production_status':'planned','target_duration_seconds':60,'duration_seconds':None,
             'example':None,'assets':{'mp4':None,'captions':None},'youtube':{'video_id':None,'visibility':None},
             'notes':'Distinct constrained counting method identified from inspected worksheet questions and solutions.',
             'planning':{'basis':'rule','rule':vid,'review_status':'needs_review'}}
    for (file,qid),vid in sorted(set(APPROVED)):
        p=doc['worksheets'][file]['problems'][qid]
        assert len(p['video_links'])==1 and not p['requires_source_visual'],(file,qid)
        old=p['video_links'][0]['video_id']
        if old!=vid:changed.append((file,qid,old,vid));p['video_links'][0]['video_id']=vid
        if p['mapping_status']!='reviewed':reviewed+=1
        p.update(mapping_method='manual',mapping_status='reviewed',mapping_rule='counting-constraints-review-1',
                 notes='Question and CSV solution inspected: matching assumptions and counting method, with different worked-example data.')
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
    with (Path(__file__).resolve().parents[1]/'videos/.production.lock').open('a+') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        path=args.output/'worksheet-video-correspondence.json';doc=json.loads(path.read_text())
        assert not any(v['production_status']=='in_progress' for v in doc['videos'].values())
        before={k:(v['youtube'].copy(),v['assets'].copy()) for k,v in doc['videos'].items()}
        changes,reviewed,merged=apply_review(doc,args.merge)
        assert before=={k:(doc['videos'][k]['youtube'],doc['videos'][k]['assets']) for k in before}
        validate(doc,read_inventory(),asset_root=args.output.parent)
        from counting_constraints_lessons import lessons
        from video_example_checks import require_analogous_examples
        require_analogous_examples(doc,lessons(doc))
        content=(args.output/'youtube-upload-checklist.md').read_text()
        for vid in sorted(set(doc['videos'])-set(before)):content=append_upload_row(content,vid,doc['videos'][vid]['title'])
        content=update_reuse_checklist(content,doc)
        if not args.check:
            save_json(path,doc);(args.output/'youtube-upload-checklist.md').write_text(content)
            update_overview(args.output,doc,[s['video_id'] for s in SPECS])
        print(f'{len(changes)} corrected links; {reviewed} newly reviewed refs; {merged} drafts reused. Check only: {args.check}')
        for c in changes:print(*c,sep=' | ')

if __name__=='__main__':main()
