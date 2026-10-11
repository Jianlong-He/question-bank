"""Explicit evidence-backed reuse of completed videos for duplicate draft IDs."""
import argparse,json
from pathlib import Path
from probability_lessons import enrichment
from video_reuse import merge_reviewed_duplicate,update_reuse_checklist,validate_reuse
from build_video_correspondence import validate,read_inventory
from generate_video_batch import save_json,update_overview

MERGES=[
 ('pattern-pmf-de69f7ad9399','pattern-pmf-4be2809cd266',enrichment('PMF','4Rev',2),
  'X is geometric with p=0.4. Find P(X>3).'),
 ('pattern-pmf-0b76bfe87b9e','probability-discrete-distribution',enrichment('PMF',6,8),
  'Three children are randomly chosen from 4 donut lovers and 6 french-fry lovers. Let k be the number of donut lovers chosen. Given p(0)=1/6, p(1)=1/2 and p(3)=1/30, use the fact that the probabilities add to 1 to find p(2).'),
 ('pattern-pmf-813812a947ee','pattern-pmf-2e87e898b750',enrichment('PMF','4Rev',1),
  'X is geometric and P(X>1)=0.85. Find p(1).'),
]
SPLIT_ID='pattern-pmf-a4e74a08fa9c'
SPLIT_REFS={enrichment('PMF','2HW',1):'probability-first-success-first',
            enrichment('PMF','2HW',2):'pattern-pmf-90d35baa0439'}
SPLIT_QUESTION='A bowl contains 1 candy and 2 cockroaches. Drawn cockroaches are replaced before the next draw. Let X be the draw on which the candy is first picked. Find p({k}).'


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True);parser.add_argument('--check',action='store_true');args=parser.parse_args()
    path=args.output/'worksheet-video-correspondence.json';doc=json.loads(path.read_text())
    assert not any(v['production_status']=='in_progress' for v in doc['videos'].values())
    before={k:(v['youtube'].copy(),v['assets'].copy()) for k,v in doc['videos'].items()}
    count=0
    for old,new,ref,question in MERGES:
        assert doc['worksheets'][ref[0]]['problems'][ref[1]]['question_text']==question,ref
        if doc['videos'][old].get('reuse_video_ids')==[new]:continue
        merge_reviewed_duplicate(doc,old,{ref:new});count+=1
    for (file,qid),target in SPLIT_REFS.items():
        assert doc['worksheets'][file]['problems'][qid]['question_text']==SPLIT_QUESTION.format(k=qid)
    if doc['videos'][SPLIT_ID].get('reuse_video_ids')!=sorted(set(SPLIT_REFS.values())):
        merge_reviewed_duplicate(doc,SPLIT_ID,SPLIT_REFS);count+=1
    doc['schema_version']='1.2.0';validate_reuse(doc)
    assert before=={k:(v['youtube'],v['assets']) for k,v in doc['videos'].items()}
    validate(doc,read_inventory(),asset_root=args.output.parent)
    checklist=args.output/'youtube-upload-checklist.md'
    updated=update_reuse_checklist(checklist.read_text(),doc)
    if not args.check:
        schema=json.loads((Path(__file__).resolve().parents[1]/'videos/worksheet-video-correspondence.schema.json').read_text())
        save_json(args.output/'worksheet-video-correspondence.schema.json',schema)
        save_json(path,doc);checklist.write_text(updated)
        update_overview(args.output,doc,sorted({new for old,new,ref,q in MERGES}|set(SPLIT_REFS.values())))
        info=args.output/'correspondence-format.txt';s=info.read_text()
        marker='\nVERIFIED SHARED-VIDEO REUSE (schema 1.2.0)\n'
        s=s.split(marker)[0]+marker+('A retired draft record with reuse_video_ids retains its original permanent ID.\n'
          'Its reviewed worksheet links point directly to the listed completed shared videos.\n'
          'No separate MP4 or upload is required for the retired draft.\n'
          'The upload table includes only active videos; its footer lists retained reuse IDs.\n'
          'Uploaded or media-bearing records are never automatically merged.\n')
        info.write_text(s)
    print(f'{count} duplicate drafts now reuse verified videos. All permanent IDs and upload data retained. Check only: {args.check}')


if __name__=='__main__':main()
