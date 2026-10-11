"""Explicitly reviewed decimal subtraction mappings and unresolved source issues."""
import argparse,fcntl,json
from pathlib import Path
SPECS=[]
def lessons(doc):
    from arithmetic_lessons import lessons as arithmetic
    return [l for l in arithmetic(doc) if l['video_id']=='arithmetic-subtract-decimals']
from number_sense_lessons import source as g
from number_theory_lessons import source as e
from video_reuse import append_upload_row,update_reuse_checklist,merge_reviewed_duplicate
from build_video_correspondence import validate,read_inventory
from generate_video_batch import save_json,update_overview
from video_example_checks import require_analogous_examples

APPROVED=[(('worksheets/Grade 5/G5Unit 3/G5U3W1Rev.csv', '1'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W1Rev.csv', '2'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W1Rev.csv', '4'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W1Rev.csv', '5'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W2.csv', '1'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W2.csv', '2'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W2.csv', '3'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W2.csv', '4'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W2.csv', '6'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W2.csv', '7'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W2.csv', '8'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W2.csv', '10'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W2HW.csv', '1'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W2HW.csv', '2'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W2HW.csv', '3'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W2Rev.csv', '1'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W2Rev.csv', '2'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W2Rev.csv', '4'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W2Rev.csv', '5'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W3.csv', '1'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W3.csv', '2'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W3.csv', '4'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W3.csv', '5'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W3.csv', '6'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W3.csv', '7'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W3.csv', '8'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W3.csv', '9'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W3.csv', '10'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W3HW.csv', '1'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W3HW.csv', '2'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W3HW.csv', '3'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W3HW.csv', '5'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W3Rev.csv', '1'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W3Rev.csv', '2'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W3Rev.csv', '4'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W4.csv', '1'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W4.csv', '2'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W4.csv', '3'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W4.csv', '4'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W4.csv', '5'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W4.csv', '6'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W4.csv', '7'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W4.csv', '8'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W4.csv', '9'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W4.csv', '10'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W4HW.csv', '1'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W4HW.csv', '2'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W4HW.csv', '3'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W4HW.csv', '4'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W4HW.csv', '5'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W4Rev.csv', '1'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W4Rev.csv', '2'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W4Rev.csv', '3'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W4Rev.csv', '4'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W5Rev.csv', '1'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W5Rev.csv', '2'), 'arithmetic-subtract-decimals'), (('worksheets/Grade 5/G5Unit 3/G5U3W5Rev.csv', '5'), 'arithmetic-subtract-decimals')]
MERGES=[]
SOURCE_NOTES={}
REVIEW_NOTES={}



def apply_review(doc,merge=False):
    changes=[];reviewed=0
    for s in SPECS:
        vid=s['video_id'];title=s['topic']
        if vid not in doc['videos']:
            doc['videos'][vid]={'title':title,'question_type':title,'curriculum':{'kind':'shared','topic':'number'},
             'production_status':'planned','target_duration_seconds':60,'duration_seconds':None,'example':None,
             'assets':{'mp4':None,'captions':None},'youtube':{'video_id':None,'visibility':None},
             'notes':'Distinct decimal subtraction method identified through explicit question review.',
             'planning':{'basis':'rule','rule':vid,'review_status':'needs_review'}}
    for (file,qid),vid in sorted(set(APPROVED)):
        p=doc['worksheets'][file]['problems'][qid]
        assert len(p['video_links'])==1,(file,qid)
        # All approved questions are self-contained; no figure is needed.
        p['requires_source_visual']=False
        old=p['video_links'][0]['video_id']
        if old!=vid:changes.append((file,qid,old,vid));p['video_links'][0]['video_id']=vid
        reviewed+=p['mapping_status']!='reviewed'
        p.update(mapping_method='manual',mapping_status='reviewed',mapping_rule='decimal-subtraction-review-1',
          notes='Inspected against the authored analogous example: matching decimal subtraction method and prerequisite steps; different numerical inputs.' + (' ' + REVIEW_NOTES[(file,qid)] if (file,qid) in REVIEW_NOTES else ''))
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
            lesson=lessons(doc)[0];record=doc['videos'][lesson['video_id']]
            if record.get('example')!={'question':lesson['question'],'answer':lesson['answer']}:
                record['production_status']='needs_revision'
            save_json(path,doc);(args.output/'youtube-upload-checklist.md').write_text(update_reuse_checklist('\n'.join(lines)+'\n',doc));update_overview(args.output,doc,[s['video_id'] for s in SPECS])
        print(f'{len(changes)} corrected links; {reviewed} newly reviewed refs. Check only: {args.check}; merge requested: {args.merge}')

if __name__=='__main__':main()
