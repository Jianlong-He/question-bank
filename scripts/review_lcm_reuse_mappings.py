"""Explicitly reviewed LCM and fraction arithmetic mappings and unresolved source issues."""
import argparse,fcntl,json
from pathlib import Path
SPECS=[]
def lessons(doc):return []
from number_sense_lessons import source as g
from number_theory_lessons import source as e
from video_reuse import append_upload_row,update_reuse_checklist,merge_reviewed_duplicate
from build_video_correspondence import validate,read_inventory
from generate_video_batch import save_json,update_overview
from video_example_checks import require_analogous_examples

APPROVED=[]
ROWS = [
 ('number-theory-lcm',5,4,'2HW',[1,2]),('number-theory-lcm',5,4,'2Rev',[1]),
 ('number-theory-lcm',5,4,'3Rev',[1,2]),('number-theory-lcm',5,4,'4HW',[1]),
 ('number-theory-lcm',5,4,'4Rev',[1]),('number-theory-lcm',6,6,7,[1,2,3,4]),
 ('number-theory-lcm',6,6,'7HW',[1,2,3]),('number-theory-lcm',6,6,'7Rev',[1]),
 ('number-theory-lcm',6,6,8,[1]),('number-theory-lcm',6,6,'8HW',[1]),
 ('number-theory-lcm',6,6,'8Rev',[1]),
 ('fractions-common-denominator',4,7,2,[1]),
 ('arithmetic-add-fractions-unlike-denominators',5,4,2,[5]),
 ('arithmetic-add-fractions-unlike-denominators',5,4,'2Rev',[3]),
 ('arithmetic-add-fractions-unlike-denominators',5,4,3,[6]),
 ('arithmetic-add-fractions-unlike-denominators',5,4,'3HW',[1]),
 ('arithmetic-add-fractions-unlike-denominators',5,4,'4HW',[3]),
 ('arithmetic-subtract-fractions-unlike-denominators',5,4,'3HW',[3]),
 ('arithmetic-subtract-fractions-unlike-denominators',5,4,4,[3,5]),
 ('arithmetic-subtract-fractions-unlike-denominators',5,4,'4HW',[4]),
 ('arithmetic-subtract-fractions-unlike-denominators',5,4,'4Rev',[3]),
 ('arithmetic-subtract-mixed-numbers',5,4,4,[7]),
]
for vid,grade,unit,w,qs in ROWS:
    APPROVED.extend((g(grade,unit,w,q),vid) for q in qs)
APPROVED.extend((e('prime-factorization',4,q),'number-theory-lcm') for q in [1,2,5,6,8])
assert len(APPROVED)==len(set(ref for ref,vid in APPROVED))
MERGES=[]
SOURCE_NOTES={
 g(6,6,8,5):'Source solution typo: the multiples of 5 list begins 5,10,25,20,25,30, incorrectly putting 25 where 15 belongs. The LCM answer 30 is correct, but the explanation needs correction. Left pending; source unchanged.',
 g(6,6,8,8):'Source solution error: 9 is written as 3^3, and the LCM as 2^2 times 3^3, while the correct expressions use 3^2. The keyed LCM 36 is correct. Left pending; source unchanged.',
}
REVIEW_NOTES={}



def apply_review(doc,merge=False):
    changes=[];reviewed=0
    for s in SPECS:
        vid=s['video_id'];title=s['topic']
        if vid not in doc['videos']:
            doc['videos'][vid]={'title':title,'question_type':title,'curriculum':{'kind':'shared','topic':'number'},
             'production_status':'planned','target_duration_seconds':60,'duration_seconds':None,'example':None,
             'assets':{'mp4':None,'captions':None},'youtube':{'video_id':None,'visibility':None},
             'notes':'Distinct LCM and fraction arithmetic method identified through explicit question review.',
             'planning':{'basis':'rule','rule':vid,'review_status':'needs_review'}}
    for (file,qid),vid in sorted(set(APPROVED)):
        p=doc['worksheets'][file]['problems'][qid]
        assert len(p['video_links'])==1,(file,qid)
        # All approved questions are self-contained; no figure is needed.
        p['requires_source_visual']=False
        old=p['video_links'][0]['video_id']
        if old!=vid:changes.append((file,qid,old,vid));p['video_links'][0]['video_id']=vid
        reviewed+=p['mapping_status']!='reviewed'
        p.update(mapping_method='manual',mapping_status='reviewed',mapping_rule='lcm-reuse-review-1',
          notes='Inspected against the authored analogous example: matching LCM and fraction arithmetic method and prerequisite steps; different numerical inputs.' + (' ' + REVIEW_NOTES[(file,qid)] if (file,qid) in REVIEW_NOTES else ''))
    for (file,qid),note in SOURCE_NOTES.items():
        p=doc['worksheets'][file]['problems'][qid]
        assert p['mapping_status']=='needs_review'
        p['notes']=note
        if note.startswith('Source visual missing:'):p['requires_source_visual']=True
    if merge:
        for old,new,refs in MERGES:
            if doc['videos'][old].get('reuse_video_ids')==[new]:continue
            merge_reviewed_duplicate(doc,old,{ref:new for ref in refs})
    for s in SPECS:
        v=doc['videos'][s['video_id']];v['title']=s['topic'];v['question_type']=s['topic']
        refs=[p for w in doc['worksheets'].values() for p in w['problems'].values() if any(l['video_id']==s['video_id'] for l in p['video_links'])]
        if refs and all(p['mapping_status']=='reviewed' for p in refs):v['planning']['review_status']='reviewed'
    for reused_id in set(vid for ref,vid in APPROVED):
        refs=[p for w in doc['worksheets'].values() for p in w['problems'].values() if any(l['video_id']==reused_id for l in p['video_links'])]
        if all(p['mapping_status']=='reviewed' for p in refs):doc['videos'][reused_id]['planning']['review_status']='reviewed'
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
