"""Grade 2 Unit 5 answer and solution audit; all 40 questions verified."""
import argparse,csv,json,io,fcntl
from pathlib import Path
from build_video_correspondence import ROOT,digest,read_inventory,validate
from generate_video_batch import save_json
SOLUTIONS={'1': ['A quarter is 25 cents. Two quarters are 25+25 = 50 cents.', 'A nickel is 5 cents. Three nickels are 5+5+5 = 15 cents.', 'A dime is 10 cents. Three dimes are 10+10+10 = 30 cents.', 'Add the coin values: one quarter is 25 cents and one nickel is 5 cents. Thus 25+5 = 30 cents.', 'One quarter is 25 cents and one dime is 10 cents. Add: 25+10 = 35 cents.', 'Two quarters make 50 cents, two nickels make 10 cents, and two dimes make 20 cents. Total: 50+10+20 = 80 cents.', 'Two quarters make 50 cents, one nickel makes 5 cents, three dimes make 30 cents, and one penny makes 1 cent. Total: 50+5+30+1 = 86 cents.', 'Two one-dollar bills make 2 dollars. Two five-dollar bills make 10 dollars. One ten-dollar bill makes 10 dollars. Add: 2+10+10 = 22 dollars.', 'Convert every choice to cents: 2 quarters are 50, 60 pennies are 60, 7 dimes are 70, and 10 nickels are 50. The greatest value is 70 cents, so select 7-dimes.', 'The price is 5+5 = 10 dollars, plus 45 cents. The payment is 10 dollars plus 25+10+10 = 45 cents. Both equal $10.45, so Yes, it is exactly enough.'], '1HW': ['Subtract ones: 9-4 = 5. Subtract tens: 8-1 = 7. Keep five hundreds. The result is 575.', 'Subtract ones: 8-5 = 3; tens: 6-3 = 3; hundreds: 4-2 = 2. The result is 233.', 'Subtract ones: 7-6 = 1; tens: 5-2 = 3; hundreds: 9-4 = 5. The result is 531.', 'Subtract ones: 5-3 = 2. Regroup one hundred to make 7 hundreds and 14 tens. Tens: 14-6 = 8; hundreds: 7-2 = 5. The result is 582.', 'Subtract ones: 4-1 = 3. Regroup one hundred to make 5 hundreds and 12 tens. Tens: 12-7 = 5; hundreds: 5-3 = 2. The result is 253.'], '1Rev': ['Subtract two tens from seven tens, keeping eight hundreds and five ones. The result is 855.', 'Subtract one hundred from four hundreds, keeping nine tens and two ones. The result is 392.', 'Subtract three tens from eight tens, keeping five hundreds and six ones. The result is 556.', 'Subtract five hundreds from nine hundreds, keeping four tens and three ones. The result is 443.', 'Subtract ones: 4-2 = 2. Subtract tens: 9-3 = 6. Keep seven hundreds. The result is 762.'], '2': ['The short hour hand points to 8. The long minute hand points to 12, meaning zero minutes. The time is 8:00. Fill the blanks with 8 and 00.', 'The short hour hand is between 1 and 2, so the hour is 1. The long minute hand points to 5; count 5, 10, 15, 20, 25 minutes. The time is 1:25. Ignore the thin red second hand.', 'The short hour hand is between 8 and 9. The long minute hand points to 7, meaning 35 minutes. The time is 8:35. Ignore the thin red second hand.', 'The short hour hand is between 10 and 11 and has not reached 11. The long minute hand points to 10, meaning 50 minutes. The time is 10:50.', 'The short hour hand is almost at 4 but has not reached it, so the hour is still 3. The long minute hand points to 11, meaning 55 minutes. The time is 3:55.', 'The short hour hand is between 9 and 10. The long minute hand points to 4, meaning 20 minutes. The time is 9:20.', 'The short hour hand is between 4 and 5 and has not reached 5. The long minute hand points to 10, meaning 50 minutes. The time is 4:50.', 'The short hour hand has passed 11. The long minute hand points to 2, meaning 10 minutes. The time is 11:10.', 'The clock shows 1:25: the short hand has passed 1 and the long hand points to 5. Five minutes later means add 25+5 = 30 minutes. The time will be 1:30.', 'The clock shows 8:35: the short hand is between 8 and 9 and the long hand points to 7. Ten minutes before means subtract 35-10 = 25 minutes. The earlier time is 8:25.'], '2HW': ['Add tens: 60+20+0+20 = 100. Add ones: 3+6+9+2 = 20. Combine: 100+20 = 120.', 'Add each colour once: 22+23 = 45, then 45+32 = 77, and 77+4 = 81 marbles.', 'Add tens: 30+40+20+60 = 150. Add ones: 5+1+6+5 = 17. Total: 150+17 = 167. Select 167.', 'Pair the page counts: 63+81 = 144 and 61+59 = 120. Add: 144+120 = 264 pages.', 'Four classes need 78+78+78+78 pencils. Each pair of classes needs 156. Add both pairs: 156+156 = 312 pencils.'], '2Rev': ['Add tens: 30+20+10+40 = 100. Add ones: 4+1+2+2 = 9. Total: 100+9 = 109.', 'Add tens: 20+20+40+20 = 100. Add ones: 5+0+2+1 = 8. Total: 100+8 = 108.', 'Add tens: 0+0+10+40 = 50. Add ones: 5+3+4+2 = 14. Total: 50+14 = 64.', 'Add tens: 50+30+20+20 = 120. Add ones: 4+9+2+5 = 20. Total: 120+20 = 140.', 'Add tens: 40+30+20+20 = 110. Add ones: 2+8+3+8 = 21. Total: 110+21 = 131.']}
PATCHES={}
VISUAL_NOTES={'G2U5W2 Q1-Q10':'All eight unique source clock images were opened and visually checked. Q1-Q8 show 8:00, 1:25, 8:35, 10:50, 3:55, 9:20, 4:50, 11:10 respectively. Q9 reuses 1:25 and asks five minutes later, giving 1:30; Q10 reuses 8:35 and asks ten minutes earlier, giving 8:25. All keys are correct.'}
PENDING={}

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--output',required=True,type=Path);parser.add_argument('--apply',action='store_true');args=parser.parse_args()
 with (ROOT/'videos/.production.lock').open('a+') as lock:
  fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
  mp=args.output/'worksheet-video-correspondence.json';doc=json.loads(mp.read_text())
  assert not any(v['production_status']=='in_progress' for v in doc['videos'].values())
  changes=[];writes=[];total=0
  for w,solutions in SOLUTIONS.items():
   rel=f'worksheets/Grade 2/G2Unit 5/G2U5W{w}.csv';p=ROOT/rel
   original=p.read_bytes();reader=csv.DictReader(io.StringIO(original.decode('utf-8-sig')));fields=reader.fieldnames;rows=list(reader)
   assert len(rows)==len(solutions)
   for row in rows:
    q=row['Question ID']
    if solutions[int(q)-1] is None:continue
    before=dict(row);row['Solution']=solutions[int(q)-1];row.update(PATCHES.get((w,q),{}))
    if row!=before:changes.append({'worksheet':rel,'question_id':q,'before':before,'after':dict(row)})
    assert row['Solution'] and row['Question Answers']
    prob=doc['worksheets'][rel]['problems'][q];prob['question_text']=row['Question Choices'];prob['question_sha256']=digest(row['Question Choices'])
    total+=1
   buf=io.StringIO(newline='');writer=csv.DictWriter(buf,fieldnames=fields,lineterminator='\n');writer.writeheader();writer.writerows(rows)
   writes.append((p,original,buf.getvalue()))
  assert total==40
  for (f,q),note in PENDING.items():
   assert doc['worksheets'][f]['problems'][q]['mapping_status']=='needs_review'
   doc['worksheets'][f]['problems'][q]['notes']=note
  if args.apply:
   report={'reviewed_questions':total,'date':'2026-10-09','scope':'Grade 2 Unit 5: 40 answer/solution rows verified; all eight source clock images inspected','visual_review':VISUAL_NOTES,'changes':changes}
   for folder in [ROOT/'videos',args.output]:
    rp=folder/'grade-2-unit-5-source-corrections-2026-10-09.json'
    if changes:assert not rp.exists(),f'Change log already exists: {rp}'
   if changes:
    for folder in [ROOT/'videos',args.output]:save_json(folder/'grade-2-unit-5-source-corrections-2026-10-09.json',report)
   for p,original,updated in writes:
    assert p.read_bytes()==original,'Concurrent source edit: '+str(p)
    if original.decode('utf-8-sig')!=updated:p.write_text(updated)
   validate(doc,read_inventory(),asset_root=args.output.parent);save_json(mp,doc)
  print(f'{total} source questions checked; {len(changes)} rows with improved solutions/corrections. Applied: {args.apply}')

if __name__=='__main__':main()
