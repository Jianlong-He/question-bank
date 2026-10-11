"""Apply the explicit, bounded worksheet review accompanying the algebra batch.

This is not a classifier: only named references and inspected small groups are
changed. Automatically grouped links outside this review stay needs_review.
"""
import argparse
import json
from pathlib import Path
from algebra_lessons import SPECS
from build_video_correspondence import read_inventory, validate
from generate_video_batch import save_json, update_overview


def ref(grade, unit, worksheet, qid):
    return (f'worksheets/Grade {grade}/G{grade}Unit {unit}/G{grade}U{unit}W{worksheet}.csv', str(qid))


CORRECTIONS = [
    (ref(11,9,'2',6), 'linear-equations-solve-both-sides', 'algebra-rearrange-formula', 'Isolates a formula variable in terms of other variables.'),
    (ref(11,9,'2',7), 'linear-equations-solve-both-sides', 'algebra-rearrange-formula', 'Rearranges the perimeter formula; no numerical root is requested.'),
    (ref(11,9,'2HW',5), 'linear-equations-solve-both-sides', 'algebra-rearrange-formula', 'Rearranges the perimeter formula; no numerical root is requested.'),
    (ref(11,9,'2Rev',4), 'linear-equations-solve-both-sides', 'algebra-rearrange-formula', 'Isolates a formula variable in terms of other variables.'),
    (ref(8,3,'2',4), 'linear-equations-solve-both-sides', 'algebra-evaluate', 'Substitutes a known x into a function; it is not an equation with unknowns on both sides.'),
    (ref(8,3,'2HW',4), 'linear-equations-solve-both-sides', 'algebra-evaluate', 'Substitutes a known x into a function; it is not an equation with unknowns on both sides.'),
    (ref(9,6,'1',1), 'linear-equations-solve-both-sides', 'systems-check-solution', 'Checks an ordered pair in two equations.'),
    (ref(9,6,'1HW',1), 'linear-equations-solve-both-sides', 'systems-check-solution', 'Checks an ordered pair in two equations.'),
    (ref(9,6,'2',1), 'linear-equations-solve-both-sides', 'systems-solve-substitution', 'Solves two simultaneous equations by substitution.'),
    (ref(9,6,'2HW',1), 'linear-equations-solve-both-sides', 'systems-solve-substitution', 'Solves two simultaneous equations by substitution.'),
    (ref(12,10,'7',7), 'factoring-polynomials', 'rational-functions-features', 'An uncanceled denominator factor identifies a candidate vertical asymptote.'),
    (ref(7,8,'5',10), 'factoring-polynomials', 'geometry-dilation', 'Finds a scale factor after converting centimetres and kilometres to matching units.'),
    (ref(7,8,'5Rev',5), 'factoring-polynomials', 'geometry-dilation', 'Finds a scale factor after converting centimetres and kilometres to matching units.'),
    (ref(3,2,'3',2), 'linear-equations-solve-both-sides', 'arithmetic-multiply-whole-numbers', 'Identifies multiplication distributed over a sum; source has an incorrect given product 8 times 10 equals 54, which must not be repeated in a video.'),
    (ref(3,2,'3Rev',2), 'linear-equations-solve-both-sides', 'arithmetic-multiply-whole-numbers', 'Identifies multiplication distributed over a sum, as taught in the partial-products example.'),
]


REVIEWED = [(tuple(s['source_ref']), s['video_id']) for s in SPECS]
REVIEWED += [(ref(10,2,w,q),'factoring-grouping') for w,q in [('2',7),('2HW',5),('2Rev',4)]]
REVIEWED += [(ref(7,6,'4Rev',1),'absolute-value-equations')]
REVIEWED += [(ref(6,5,w,q),'absolute-value-evaluation') for w,q in [('3',2),('3',3),('3',5),('3HW',1),('3HW',2),('3Rev',1),('3Rev',2),('4',2),('4HW',2)]]
REVIEWED += [(ref(9,2,w,q),'linear-equations-solve-both-sides') for w,q in [('1',1),('1',4),('1',5),('1HW',1),('1HW',3),('1Rev',2)]]
REVIEWED += [(ref(8,2,'3Rev',5),'linear-equations-solve-both-sides')]


def apply_review(doc):
    corrected = reviewed = 0
    for (file,qid),old,new,reason in CORRECTIONS:
        p=doc['worksheets'][file]['problems'][qid]
        if all(l['video_id']==new for l in p['video_links']):
            continue
        assert len(p['video_links'])==1 and p['video_links'][0]['video_id']==old,(file,qid)
        assert new in doc['videos']
        p['video_links'][0]['video_id']=new
        p.update(mapping_method='manual',mapping_status='needs_review',mapping_rule='algebra-content-review-1',
                 notes=reason+' Mapping corrected by content review; the destination example still needs its suitability review.')
        corrected+=1
    for (file,qid),vid in REVIEWED:
        p=doc['worksheets'][file]['problems'][qid]
        assert len(p['video_links'])==1 and p['video_links'][0]['video_id']==vid,(file,qid)
        assert not p['requires_source_visual'],(file,qid)
        if p['mapping_status']=='reviewed':continue
        p.update(mapping_method='manual',mapping_status='reviewed',mapping_rule='algebra-content-review-1',
                 notes='Reviewed against the authored algebra example: same solving method, new question values, and suitable prerequisites. The example is not the worksheet answer.')
        reviewed+=1
    for vid,title in [('absolute-value-equations','Solve equations containing an absolute-value constant')]:
        doc['videos'][vid]['title']=title
        doc['videos'][vid]['question_type']=title
    for vid in ['factoring-grouping','absolute-value-equations']:
        refs=[p for w in doc['worksheets'].values() for p in w['problems'].values() if any(l['video_id']==vid for l in p['video_links'])]
        assert refs and all(p['mapping_status']=='reviewed' for p in refs)
        doc['videos'][vid]['planning']['review_status']='reviewed'
    return corrected,reviewed


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    path=args.output/'worksheet-video-correspondence.json'
    doc=json.loads(path.read_text())
    assert not any(v['production_status']=='in_progress' for v in doc['videos'].values()),'Do not review while rendering.'
    before={k:v['youtube'].copy() for k,v in doc['videos'].items()}
    corrected,reviewed=apply_review(doc)
    assert before=={k:v['youtube'] for k,v in doc['videos'].items()}
    validate(doc,read_inventory(),asset_root=args.output.parent)
    save_json(path,doc)
    checklist=args.output/'youtube-upload-checklist.md'
    lines=checklist.read_text().splitlines()
    for i,line in enumerate(lines):
        if line.startswith('All 3,153 videos in the current plan:'):
            lines[i]='All 3,153 videos in the current plan. Each shared video appears once, even when it serves multiple worksheets or grades. See production-progress.txt for current completion counts.'
        if line.startswith('Filenames below are the planned export filenames:'):
            lines[i]='Filenames below are the export filenames: each permanent video ID followed by `.mp4`.'
        if '| absolute-value-equations.mp4 |' in line:
            cells=line.split('|');cells[1]=' '+doc['videos']['absolute-value-equations']['title']+' ';lines[i]='|'.join(cells)
    checklist.write_text('\n'.join(lines)+'\n')
    update_overview(args.output,doc,[s['video_id'] for s in SPECS])
    print(f'Corrected {corrected} mappings; reviewed {reviewed} worksheet problems; upload IDs preserved.')


if __name__=='__main__':main()
