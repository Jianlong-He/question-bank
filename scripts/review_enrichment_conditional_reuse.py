"""Retain explicitly reviewed duplicate conditional-probability draft IDs."""
import argparse,fcntl,json
from pathlib import Path
from video_reuse import merge_reviewed_duplicate,update_reuse_checklist
from build_video_correspondence import validate,read_inventory
from generate_video_batch import save_json,update_overview
from video_example_checks import require_analogous_examples
MERGES=[('pattern-conditional-probability-014698168df7', [(('worksheets/enrichment/counting-and-probability 1/U4conditional-probability/E-CP1U4W6.csv', '7'), 'counting-teams-multiple-reservations')]), ('pattern-conditional-probability-078be3f64567', [(('worksheets/enrichment/counting-and-probability 1/U4conditional-probability/E-CP1U4W5.csv', '2'), 'probability-independent')]), ('pattern-conditional-probability-335d42662ec6', [(('worksheets/enrichment/counting-and-probability 1/U4conditional-probability/E-CP1U4W5.csv', '1'), 'probability-independent')]), ('pattern-conditional-probability-3526a5ff16a1', [(('worksheets/enrichment/counting-and-probability 1/U4conditional-probability/E-CP1U4W6.csv', '2'), 'counting-labelled-teams')]), ('pattern-conditional-probability-354e7ba0682d', [(('worksheets/enrichment/counting-and-probability 1/U4conditional-probability/E-CP1U4W6.csv', '8'), 'counting-team-fixed-pair')]), ('pattern-conditional-probability-3a902e7d7c79', [(('worksheets/enrichment/counting-and-probability 1/U4conditional-probability/E-CP1U4W5Rev.csv', '2'), 'probability-test-independence')]), ('pattern-conditional-probability-4db4b282be8e', [(('worksheets/enrichment/counting-and-probability 1/U4conditional-probability/E-CP1U4W6Rev.csv', '1'), 'counting-labelled-teams')]), ('pattern-conditional-probability-87aaec5ce678', [(('worksheets/enrichment/counting-and-probability 1/U4conditional-probability/E-CP1U4W6HW.csv', '1'), 'counting-labelled-teams')]), ('pattern-conditional-probability-986adea95d05', [(('worksheets/enrichment/counting-and-probability 1/U4conditional-probability/E-CP1U4W6Rev.csv', '4'), 'counting-team-fixed-pair')]), ('pattern-conditional-probability-a186f0394d05', [(('worksheets/enrichment/counting-and-probability 1/U4conditional-probability/E-CP1U4W3Rev.csv', '2'), 'counting-two-set-union-neither')]), ('pattern-conditional-probability-a65cc220e4ee', [(('worksheets/enrichment/counting-and-probability 1/U4conditional-probability/E-CP1U4W5HW.csv', '2'), 'probability-independent')]), ('pattern-conditional-probability-bbf402d9e017', [(('worksheets/enrichment/counting-and-probability 1/U4conditional-probability/E-CP1U4W5.csv', '6'), 'probability-pairwise-not-mutual')]), ('pattern-conditional-probability-ef39c683f8ce', [(('worksheets/enrichment/counting-and-probability 1/U4conditional-probability/E-CP1U4W6.csv', '1'), 'counting-labelled-teams'), (('worksheets/enrichment/counting-and-probability 1/U4conditional-probability/E-CP1U4W6HW.csv', '2'), 'counting-labelled-teams')]), ('pattern-conditional-probability-f85d0de6358a', [(('worksheets/enrichment/counting-and-probability 1/U4conditional-probability/E-CP1U4W3.csv', '10'), 'probability-three-set-union')]), ('pattern-conditional-probability-fe2765aec9cf', [(('worksheets/enrichment/counting-and-probability 1/U4conditional-probability/E-CP1U4W5Rev.csv', '3'), 'probability-test-independence')])]

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True);parser.add_argument('--check',action='store_true');args=parser.parse_args()
    with (Path(__file__).resolve().parents[1]/'videos/.production.lock').open('a') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        path=args.output/'worksheet-video-correspondence.json';d=json.loads(path.read_text())
        assert not any(v['production_status']=='in_progress' for v in d['videos'].values())
        before={k:(v['youtube'].copy(),v['assets'].copy()) for k,v in d['videos'].items()}
        for old,items in MERGES:
            targets=dict(items)
            if d['videos'][old].get('reuse_video_ids')==sorted(set(targets.values())):continue
            assert not any(l['video_id']==old for w in d['worksheets'].values() for p in w['problems'].values() for l in p['video_links'])
            for (f,q),target in targets.items():
                p=d['worksheets'][f]['problems'][q]
                assert p['mapping_status']=='reviewed' and len(p['video_links'])==1 and p['video_links'][0]['video_id']==target
                assert d['videos'][target]['production_status']=='rendered'
            for (f,q),target in targets.items():d['worksheets'][f]['problems'][q]['video_links'][0]['video_id']=old
            merge_reviewed_duplicate(d,old,targets)
        assert before=={k:(v['youtube'],v['assets']) for k,v in d['videos'].items()}
        validate(d,read_inventory(),asset_root=args.output.parent)
        targets={t for old,items in MERGES for ref,t in items}
        require_analogous_examples(d,[{'video_id':v,'question':d['videos'][v]['example']['question']} for v in targets])
        content=update_reuse_checklist((args.output/'youtube-upload-checklist.md').read_text(),d)
        if not args.check:
            save_json(path,d);(args.output/'youtube-upload-checklist.md').write_text(content);update_overview(args.output,d,[])
        print(len(MERGES),'verified draft reuse records; check only:',args.check)
if __name__=='__main__':main()
