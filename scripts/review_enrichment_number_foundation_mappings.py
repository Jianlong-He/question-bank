"""Explicitly reviewed enrichment number foundation mappings and unresolved source issues."""
import argparse,fcntl,json
from pathlib import Path
from enrichment_number_foundation_lessons import SPECS,lessons
from number_sense_lessons import source as g
from video_reuse import append_upload_row,update_reuse_checklist,merge_reviewed_duplicate
from build_video_correspondence import validate,read_inventory
from generate_video_batch import save_json,update_overview
from video_example_checks import require_analogous_examples

APPROVED=[(('worksheets/enrichment/number-theory 1/U2prime-factorization/E-NT1U2W1.csv', '2'), 'number-theory-prime-decomposition'), (('worksheets/enrichment/number-theory 1/U2prime-factorization/E-NT1U2W1.csv', '3'), 'number-theory-prime-decomposition'), (('worksheets/enrichment/number-theory 1/U2prime-factorization/E-NT1U2W1.csv', '4'), 'number-theory-prime-decomposition'), (('worksheets/enrichment/number-theory 1/U2prime-factorization/E-NT1U2W1.csv', '5'), 'number-theory-prime-decomposition'), (('worksheets/enrichment/number-theory 1/U2prime-factorization/E-NT1U2W1.csv', '7'), 'number-theory-prime-decomposition'), (('worksheets/enrichment/number-theory 1/U2prime-factorization/E-NT1U2W1.csv', '8'), 'number-theory-prime-decomposition'), (('worksheets/enrichment/number-theory 1/U2prime-factorization/E-NT1U2W1.csv', '9'), 'number-theory-prime-decomposition'), (('worksheets/enrichment/number-theory 1/U2prime-factorization/E-NT1U2W2HWa.csv', '1'), 'number-theory-prime-decomposition'), (('worksheets/enrichment/number-theory 1/U2prime-factorization/E-NT1U2W2HWa.csv', '3'), 'number-theory-prime-decomposition'), (('worksheets/enrichment/number-theory 1/U2prime-factorization/E-NT1U2W2HWb.csv', '1'), 'number-theory-prime-decomposition'), (('worksheets/enrichment/number-theory 1/U2prime-factorization/E-NT1U2W2HWb.csv', '3'), 'number-theory-prime-decomposition'), (('worksheets/enrichment/number-theory 1/U2prime-factorization/E-NT1U2W1.csv', '6'), 'number-theory-prime-composite'), (('worksheets/enrichment/number-theory 1/U2prime-factorization/E-NT1U2W1.csv', '10'), 'lcm-prime-factor-method'), (('worksheets/enrichment/number-theory 1/U2prime-factorization/E-NT1U2W1HWa.csv', '3'), 'lcm-prime-factor-method'), (('worksheets/enrichment/number-theory 1/U2prime-factorization/E-NT1U2W4.csv', '10'), 'number-theory-synchronized-events'), (('worksheets/enrichment/number-theory 1/U2prime-factorization/E-NT1U2W6.csv', '2'), 'number-theory-synchronized-events'), (('worksheets/enrichment/number-theory 1/U2prime-factorization/E-NT1U2W6.csv', '4'), 'number-theory-synchronized-events'), (('worksheets/enrichment/number-theory 1/U2prime-factorization/E-NT1U2W6.csv', '6'), 'number-theory-synchronized-events'), (('worksheets/enrichment/number-theory 1/U2prime-factorization/E-NT1U2W6.csv', '8'), 'number-theory-synchronized-events'), (('worksheets/enrichment/number-theory 1/U2prime-factorization/E-NT1U2W2HWa.csv', '4'), 'order-gcf-identical-packs'), (('worksheets/enrichment/number-theory 1/U2prime-factorization/E-NT1U2W6.csv', '1'), 'order-gcf-identical-packs'), (('worksheets/enrichment/number-theory 1/U2prime-factorization/E-NT1U2W6.csv', '5'), 'order-gcf-identical-packs'), (('worksheets/enrichment/number-theory 1/U2prime-factorization/E-NT1U2W2HWb.csv', '4'), 'order-gcf-group-size'), (('worksheets/enrichment/number-theory 1/U2prime-factorization/E-NT1U2W6.csv', '3'), 'gcf-square-tiling'), (('worksheets/enrichment/number-theory 1/U2prime-factorization/E-NT1U2W3.csv', '2'), 'gcf-extended-euclid'), (('worksheets/enrichment/number-theory 1/U2prime-factorization/E-NT1U2W3.csv', '5'), 'gcf-extended-euclid'), (('worksheets/enrichment/number-theory 1/U2prime-factorization/E-NT1U2W3.csv', '9'), 'gcf-extended-euclid'), (('worksheets/enrichment/number-theory 1/U2prime-factorization/E-NT1U2W3HWb.csv', '4'), 'gcf-extended-euclid'), (('worksheets/enrichment/number-theory 1/U2prime-factorization/E-NT1U2W3.csv', '4'), 'gcf-jug-measurement'), (('worksheets/enrichment/number-theory 1/U2prime-factorization/E-NT1U2W3.csv', '6'), 'gcf-jug-measurement'), (('worksheets/enrichment/number-theory 1/U4number-theory1_review/E-NT1U4W1.csv', '4'), 'number-theory-prime-decomposition'), (('worksheets/enrichment/number-theory 1/U4number-theory1_review/E-NT1U4W1.csv', '1'), 'modular-signed-addition'), (('worksheets/enrichment/number-theory 1/U4number-theory1_review/E-NT1U4W2.csv', '4'), 'number-theory-prime-decomposition'), (('worksheets/enrichment/number-theory 1/U4number-theory1_review/E-NT1U4W2.csv', '1'), 'modular-signed-addition'), (('worksheets/enrichment/number-theory 1/U4number-theory1_review/E-NT1U4W3.csv', '4'), 'number-theory-prime-decomposition'), (('worksheets/enrichment/number-theory 1/U4number-theory1_review/E-NT1U4W3.csv', '1'), 'modular-signed-addition'), (('worksheets/enrichment/number-theory 1/U4number-theory1_review/E-NT1U4W4.csv', '4'), 'number-theory-prime-decomposition'), (('worksheets/enrichment/number-theory 1/U4number-theory1_review/E-NT1U4W4.csv', '1'), 'modular-signed-addition'), (('worksheets/enrichment/number-theory 1/U4number-theory1_review/E-NT1U4W1.csv', '10'), 'number-theory-build-bezout-signs'), (('worksheets/enrichment/number-theory 1/U4number-theory1_review/E-NT1U4W2.csv', '6'), 'number-theory-synchronized-events'), (('worksheets/enrichment/number-theory 1/U4number-theory1_review/E-NT1U4W2.csv', '7'), 'divide-two-digit-remainder'), (('worksheets/enrichment/number-theory 1/U4number-theory1_review/E-NT1U4W3.csv', '6'), 'number-theory-synchronized-events'), (('worksheets/enrichment/number-theory 1/U4number-theory1_review/E-NT1U4W3.csv', '7'), 'divide-two-digit-remainder'), (('worksheets/enrichment/number-theory 1/U4number-theory1_review/E-NT1U4W4.csv', '6'), 'number-theory-synchronized-events'), (('worksheets/enrichment/number-theory 1/U4number-theory1_review/E-NT1U4W4.csv', '7'), 'divide-two-digit-remainder'), (('worksheets/enrichment/number-theory 1/U4number-theory1_review/E-NT1U4W2.csv', '3'), 'modular-numbered-clock-events'), (('worksheets/enrichment/number-theory 1/U4number-theory1_review/E-NT1U4W2.csv', '10'), 'number-theory-nonnegative-stamp-equation'), (('worksheets/enrichment/number-theory 1/U4number-theory1_review/E-NT1U4W3.csv', '3'), 'enrichment-cycles-elapsed-remainder'), (('worksheets/enrichment/number-theory 1/U4number-theory1_review/E-NT1U4W4.csv', '3'), 'modular-clock-elapsed-hours')]
assert len(APPROVED)==len(set(ref for ref,vid in APPROVED))
MERGES=[]
SOURCE_NOTES={}
REVIEW_NOTES={('worksheets/enrichment/number-theory 1/U2prime-factorization/E-NT1U2W6.csv', '6'): 'Verified mathematical result 9:00 AM. The source also accepts and prints the nonstandard time 8:60; the linked lesson uses normal clock notation and carries full hours correctly.', ('worksheets/enrichment/number-theory 1/U2prime-factorization/E-NT1U2W6.csv', '8'): 'Interpreted the recurring events as synchronized at time zero, as assumed by the keyed LCM answer. The analogous example states the common start explicitly.', ('worksheets/enrichment/number-theory 1/U2prime-factorization/E-NT1U2W1.csv', '6'): 'The linked fresh prime example teaches exactly two positive factors. Applying that definition to the source number shows why its single positive factor does not meet the definition.'}


def apply_review(doc,merge=False):
    changes=[];reviewed=0
    for s in SPECS:
        vid=s['video_id'];title=s['topic']
        if vid not in doc['videos']:
            doc['videos'][vid]={'title':title,'question_type':title,'curriculum':{'kind':'shared','topic':'number'},
             'production_status':'planned','target_duration_seconds':60,'duration_seconds':None,'example':None,
             'assets':{'mp4':None,'captions':None},'youtube':{'video_id':None,'visibility':None},
             'notes':'Distinct enrichment number foundation method identified through explicit question review.',
             'planning':{'basis':'rule','rule':vid,'review_status':'needs_review'}}
    for (file,qid),vid in sorted(set(APPROVED)):
        p=doc['worksheets'][file]['problems'][qid]
        assert len(p['video_links'])==1,(file,qid)
        # All approved questions are self-contained; no figure is needed.
        p['requires_source_visual']=False
        old=p['video_links'][0]['video_id']
        if old!=vid:changes.append((file,qid,old,vid));p['video_links'][0]['video_id']=vid
        reviewed+=p['mapping_status']!='reviewed'
        p.update(mapping_method='manual',mapping_status='reviewed',mapping_rule='enrichment-number-foundation-review-1',
          notes='Inspected against the authored analogous example: matching enrichment number foundation method and prerequisite steps; different numerical inputs.' + (' ' + REVIEW_NOTES[(file,qid)] if (file,qid) in REVIEW_NOTES else ''))
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
