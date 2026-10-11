"""Finalize a fully rendered, individually reviewed grade/unit batch."""
import argparse,collections,copy,csv,fcntl,importlib,json
from pathlib import Path
from build_video_correspondence import ROOT,read_inventory,validate
from generate_video_batch import save_json,update_overview
from video_reuse import update_reuse_checklist

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);p.add_argument('--catalog',choices=['early-parity','early-equations','early-story','early-money-time'],required=True);p.add_argument('--unit',type=int,required=True);args=p.parse_args()
 expected={'early-parity':(2,120),'early-equations':(3,100),'early-story':(4,60),'early-money-time':(5,40)};unit,total=expected[args.catalog];assert args.unit==unit
 module=args.catalog.replace('-','_');specs=importlib.import_module(module+'_lessons').SPECS
 with (ROOT/'videos/.production.lock').open('a+') as lock:
  fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
  out=args.output;d=json.loads((out/'worksheet-video-correspondence.json').read_text());before=copy.deepcopy(d)
  assert not any(v['production_status']=='in_progress' for v in d['videos'].values())
  ids=[s['video_id'] for s in specs]
  assert all(d['videos'][v]['production_status']=='rendered' and d['videos'][v]['duration_seconds']<60 for v in ids)
  # Recheck exact audited source rows, not just the presence of a solution.
  audit=json.loads((ROOT/f'videos/grade-2-unit-{unit}-source-corrections-2026-10-09.json').read_text())
  rows={}
  for c in audit['changes']:
   f,q=c['worksheet'],c['question_id']
   if f not in rows:
    with (ROOT/f).open(encoding='utf-8-sig',newline='') as stream:rows[f]={r['Question ID']:r for r in csv.DictReader(stream)}
   assert rows[f][q]==c['after'],(f,q)
  ps=[p for f,w in d['worksheets'].items() if f.startswith(f'worksheets/Grade 2/G2Unit {unit}/') for p in w['problems'].values()]
  reviewed=[p for p in ps if p['mapping_status']=='reviewed']
  expected_reviewed=59 if unit==4 else total
  assert len(ps)==total and len(reviewed)==expected_reviewed
  if unit==4:
   from grade2_unit4_source_review import PENDING
   pending={(f,q) for f,w in d['worksheets'].items() if f.startswith('worksheets/Grade 2/G2Unit 4/') for q,p in w['problems'].items() if p['mapping_status']!='reviewed'}
   assert pending==set(PENDING)
  assert all(d['videos'][l['video_id']]['production_status']=='rendered' for p in reviewed for l in p['video_links'])
  oldrefs=json.loads((ROOT/f'videos/{args.catalog}-original-references.json').read_text())
  linked={l['video_id'] for w in d['worksheets'].values() for p in w['problems'].values() for l in p['video_links']};retired=[]
  for old,refs in oldrefs.items():
   v=d['videos'][old]
   if old in linked or v['production_status']!='planned':continue
   assert not v['youtube']['video_id'] and all(x is None for x in v['assets'].values()),old
   targets=set()
   for f,q in refs:
    pb=d['worksheets'][f]['problems'][q];assert pb['mapping_status']=='reviewed' and len(pb['video_links'])==1,(old,f,q)
    if pb['requires_source_visual']:assert 'Source image opened and visually checked' in pb['notes'],(f,q)
    t=pb['video_links'][0]['video_id'];assert t!=old and d['videos'][t]['production_status']=='rendered';targets.add(t)
   assert targets
   v.update(production_status='retired',reuse_video_ids=sorted(targets),notes=f'Original draft retained for lookup after Grade 2 Unit {unit} review. Every original reference was individually checked and assigned to a rendered analogous lesson; no separate upload is required.')
   v['planning']['review_status']='reviewed';retired.append(old)
  assert all(v in linked for v,r in d['videos'].items() if r['production_status']=='planned')
  for k,v in before['videos'].items():assert (v['youtube'],v['assets'])==(d['videos'][k]['youtube'],d['videos'][k]['assets'])
  validate(d,read_inventory(),asset_root=out.parent);save_json(out/'worksheet-video-correspondence.json',d)
  cp=out/'youtube-upload-checklist.md';cp.write_text(update_reuse_checklist(cp.read_text(),d));update_overview(out,d,ids)
  stats=dict(collections.Counter(v['production_status'] for v in d['videos'].values()))
  report=[f'# Grade 2 Unit {unit} production and source review','',f'Completed 2026-10-09: {expected_reviewed}/{total} questions have verified answers, hints, full worked solutions, and reviewed links to completed analogous videos. Added {len(ids)} new videos; other questions reuse existing lessons.','',f'[Detailed before/after changes](grade-2-unit-{unit}-source-corrections-2026-10-09.json)','',f'All {len(ids)} new lessons use local Kokoro af_heart at speed 0.95, no subtitles, and permanent video-ID filenames. New source examples use different inputs from their linked worksheet questions.','',f'Retired {len(retired)} unused duplicate drafts only after verifying all their original references and completed replacement media. YouTube entries and existing assets were preserved.','']
  if unit==2:report+=['Answer-key fixes: G2U2W2HW Q1 accepts both 429 and 328; G2U2W5HW Q3 correctly accepts equal amounts; G2U2W5HW Q4 accepts both tied boxes. Also repaired hints and clarified object labels/group wording. All five image-based source figures were visually inspected.','']
  if unit==3:report+=['Corrected the missing-number sequence in G2U3W1HW Q4; clarified the continuation in G2U3W1Rev Q3; accepted both correct addition expansions in G2U3W3HW Q2; repaired the false +6 intermediate sum and blanks in Q3; clarified Q4’s stated method. Removed the optional G2U3W5 Q7 image whose caption confused the amount sold with the amount left. All eight supplemental solution figures were inspected; the change log retains the removed URL.','']
  if unit==4:report+=['Corrected G2U4W2HW Q2 to 90 trees: trimming branches does not remove trees. G2U4W2HW Q3 remains pending because the trade does not specify what Maria receives. All other 59 source rows have full verified solutions.','']
  if unit==5:report+=['All forty answer keys are correct. Replaced answer-only solutions with worked explanations and inspected all eight unique clock images used in ten questions.','']
  state='ALL UNBLOCKED QUESTIONS COMPLETE' if unit==4 else 'COMPLETE'
  checkpoint=f'\n2026-10-09 — Grade 2 Unit {unit} {state}: {expected_reviewed}/{total} mappings reviewed and linked to rendered media; all {expected_reviewed} source answers/hints/solutions individually reviewed and full worked solutions saved. {len(ids)} new {args.catalog} videos rendered and individually verified; {len(retired)} fully covered duplicate drafts retired with reference evidence. Library status: {stats}. Canonical T7 JSON/checklist/overview updated, YouTube IDs/assets preserved. Detailed source before/after log: grade-2-unit-{unit}-source-corrections-2026-10-09.json; review notes: grade-2-unit-{unit}-source-review.md. NEXT: Grade 2 Unit {unit+1}, ascending thereafter. Final full media/schema audit follows.\n'
  for folder in [ROOT/'videos',out]:
   (folder/f'grade-2-unit-{unit}-source-review.md').write_text('\n'.join(report))
   with (folder/'production-worklog.txt').open('a') as f:f.write(checkpoint)
   (folder/'grade-priority-next-methods.txt').write_text(f'Continue Grade 2 Unit {unit+1}. Unit {unit}: {expected_reviewed}/{total} complete with source answers and worked solutions audited. Grade 2 Unit 4 has one underdetermined rock-trading story pending. Grade 1 still has seven recorded source issues and Grade 2 Unit 1 has three earlier source issues; apply the latest authorization to clear errors, keep genuine ambiguity pending. Final retrospective source-solution audit is still required for earlier batches. Enrichment videos complete. Use T7 canonical manifest, preserve uploads, and take the production lock.\n')
  print(json.dumps({'unit':unit,'new_videos':len(ids),'reviewed_questions':expected_reviewed,'pending_questions':total-expected_reviewed,'retired_drafts':len(retired),'duration_range':[min(d['videos'][v]['duration_seconds'] for v in ids),max(d['videos'][v]['duration_seconds'] for v in ids)],'library':stats},indent=2))
if __name__=='__main__':main()
