"""Record the inspected straightforward enrichment links for this authored batch."""
import argparse
import json
from pathlib import Path
from number_theory_lessons import SPECS, source
from build_video_correspondence import read_inventory, validate
from generate_video_batch import save_json, update_overview


REVIEWED = [(source('Euclidean-division',2,q),'number-theory-euclidean-algorithm') for q in [6,8,9,10]]
REVIEWED += [(source('RSA',2,q),'number-theory-euler-totient') for q in [2,3,5,6,9]]
REVIEWED += [(source('RSA',4,1),'number-theory-euler-totient')]
REVIEWED += [(source('modular-arithmetic',3,q),'number-theory-modular-inverse') for q in range(1,9)]
REVIEWED += [(source('RSA',3,6),'number-theory-modular-inverse')]
REVIEWED += [(source('modular-arithmetic','3HWa',q),'number-theory-modular-inverse') for q in [1,2]]
REVIEWED += [(source('modular-arithmetic','3HWb',q),'number-theory-modular-inverse') for q in [1,2]]
REVIEWED += [(source('number-theory1_review',w,2),'number-theory-modular-inverse') for w in [2,3,4]]
REVIEWED += [(source('modular-arithmetic',2,q),'number-theory-modular-multiplication') for q in range(1,9)]
REVIEWED += [(source('modular-arithmetic',w,1),'number-theory-modular-multiplication') for w in ['2HWa','2HWb']]
REVIEWED += [(source('CRT',1,3),'number-theory-modular-multiplication')]
REVIEWED += [(source('RSA',6,2),'number-theory-rsa-encryption')]


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
    path=args.output/'worksheet-video-correspondence.json';doc=json.loads(path.read_text())
    assert not any(v['production_status']=='in_progress' for v in doc['videos'].values())
    for (file,qid),vid in REVIEWED:
        p=doc['worksheets'][file]['problems'][qid]
        assert len(p['video_links'])==1 and p['video_links'][0]['video_id']==vid,(file,qid)
        assert not p['requires_source_visual'],(file,qid)
        p.update(mapping_method='manual',mapping_status='reviewed',mapping_rule='number-theory-content-review-1',
                 notes='Reviewed against the authored enrichment example: same calculation method with different input values. Multi-part extensions, proofs and reverse questions are reviewed separately.')
    validate(doc,read_inventory(),asset_root=args.output.parent)
    save_json(path,doc)
    update_overview(args.output,doc,[s['video_id'] for s in SPECS])
    print(f'Reviewed {len(REVIEWED)} enrichment problem mappings.')


if __name__=='__main__':main()
