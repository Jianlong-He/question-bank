"""Grade 2 Unit 4 answer and solution audit; one trading story stays pending."""
import argparse,csv,json,io,fcntl
from pathlib import Path
from build_video_correspondence import ROOT,digest,read_inventory,validate
from generate_video_batch import save_json
SOLUTIONS={
'1':[
'10 is one ten. Increase the tens count in 123 from 2 to 3: 123+10 = 133.',
'100 is one hundred. Increase the hundreds count in 457 from 4 to 5: 457+100 = 557.',
'30 is three tens. Four tens plus three tens make seven tens; keep 1 hundred and 5 ones. The answer is 175.',
'200 is two hundreds. Six hundreds plus two hundreds make eight hundreds; keep 3 tens and 2 ones. The answer is 832.',
'Add ones: 5+3 = 8. Add tens: 4+1 = 5. Keep 2 hundreds. Thus 245+13 = 258.',
'Add ones: 3+6 = 9; tens: 2+5 = 7; hundreds: 1+4 = 5. The sum is 579.',
'Break 156 into 100+50+6. Combine 6+14 = 20, then add 100+50+20 = 170.',
'Add ones: 6+3 = 9; tens: 6+2 = 8; hundreds: 4+3 = 7. The sum is 789.',
'Add ones: 5+5 = 10, so regroup one ten and write zero ones. Add tens: 7+1+1 = 9. Add hundreds: 3+1 = 4. The sum is 490.',
'Add ones: 8+2 = 10, so regroup one ten. The tens total is 2+5+1 = 8. Keep the 1 hundred. The sum is 180.'
],
'1HW':[
'Buying more markers means add: 32+15. Add tens: 30+10 = 40; ones: 2+5 = 7. Sam has 47 markers.',
'Subtract the puzzles sold: 64-28. Regroup 64 as 5 tens and 14 ones. Then 14-8 = 6 ones and 5-2 = 3 tens. There are 36 puzzles left.',
'Add the two types of books: 45+36. Five plus six is 11 ones, so regroup one ten. The tens are 4+3+1 = 8. The total is 81 books.',
'Add the rescued birds: 58+34. Eight plus four gives 12 ones. Regroup one ten: 5+3+1 = 9 tens and 2 ones. The zoo has 92 birds.',
'Fewer means subtract: 82-25. Regroup 82 as 7 tens and 12 ones. Subtract: 12-5 = 7 ones and 7-2 = 5 tens. The gardener will plant 57 flowers.'
],
'1Rev':[
'After the first sale: 70-25 = 45 pens. After the delivery: 45+40 = 85. After the last sale: 85-30 = 55 pens remain.',
'Jerry has 20 more than Tom: 35+20 = 55. Ann has 10 fewer than Jerry: 55-10 = 45 marbles.',
'Update each group separately. Cows: 55-30 = 25. Sheep: 45+20 = 65. Add the new counts: 25+65 = 90 animals.',
'Total pages read: 20+15+5 = 40. Subtract from the book total: 100-40 = 60 pages still to read.',
'Tuesday: 30+20 = 50 lunches. Wednesday: 50-10 = 40 lunches. The first three days total 30+50+40 = 120. Remaining weekly capacity: 150-120 = 30 lunches.'
],
'2':[
'Subtract one ten from 998. Nine tens become eight tens; hundreds and ones stay the same. The result is 988.',
'Subtract one hundred from 532. Five hundreds become four hundreds; tens and ones stay the same. The result is 432.',
'Subtract four tens from seven tens, keeping six hundreds and five ones. Thus 675-40 = 635.',
'Subtract three hundreds from six hundreds, keeping seven tens and five ones. Thus 675-300 = 375.',
'Subtract ones: 7-3 = 4. Subtract tens: 8-5 = 3. Keep six hundreds. The result is 634.',
'Subtract ones: 7-2 = 5. Subtract tens: 6-1 = 5. Keep four hundreds. The result is 455.',
'Subtract ones: 5-4 = 1; tens: 7-2 = 5; hundreds: 3-1 = 2. The result is 251.',
'Subtract ones: 6-4 = 2; tens: 8-3 = 5; hundreds: 7-2 = 5. The result is 552.',
'Subtract ones: 6-4 = 2. Regroup one hundred as ten tens, giving 6 hundreds and 13 tens. Subtract tens: 13-5 = 8; hundreds: 6-3 = 3. The result is 382.',
'Subtract ones: 6-1 = 5. Regroup one hundred as ten tens, giving 4 hundreds and 13 tens. Subtract tens: 13-5 = 8; hundreds: 4-1 = 3. The result is 385.'
],
'2HW':[
'First add the purchase: 35+20 = 55 cards. Then subtract the gift: 55-15 = 40 cards remain.',
'Planting 25 new trees increases the count: 65+25 = 90. Trimming branches does not remove trees, so the count remains 90.',
None,
'After the sale, 60-35 = 25 cookies remain. Baking 25 more gives 25+25 = 50 cookies.',
'The original total is 50+25 = 75 cards. Giving away 15 leaves 60. Receiving 10 more gives 60+10 = 70 cards.'
],
'2Rev':[
'Subtract one ten from 887: eight tens become seven tens. The result is 877.',
'Subtract two hundreds from 641: six hundreds become four hundreds. The result is 441.',
'Subtract ones: 8-4 = 4; tens: 7-3 = 4. Keep five hundreds. The result is 544.',
'Subtract ones: 5-3 = 2; tens: 8-4 = 4; hundreds: 6-2 = 4. The result is 442.',
'Subtract ones: 4-1 = 3. Regroup one hundred to get 5 hundreds and 12 tens. Subtract tens: 12-6 = 6; hundreds: 5-2 = 3. The result is 363.'
],
'3':[
'Add tens: 20+10+10+30 = 70. Add ones: 3+2+1+3 = 9. Combine: 70+9 = 79.',
'Add tens: 10+10+30+10 = 60. Add ones: 5+0+2+1 = 8. Combine: 60+8 = 68.',
'Add tens: 0+0+10+30 = 40. Add ones: 4+2+2+1 = 9. Combine: 40+9 = 49.',
'Add tens: 40+20+10+10 = 80. Add ones: 3+8+1+5 = 17. Combine and regroup: 80+17 = 97.',
'Add tens: 30+20+10+10 = 70. Add ones: 2+8+3+8 = 21. Combine and regroup: 70+21 = 91.',
'Add tens: 50+10+0+10 = 70. Add ones: 3+6+8+2 = 19. Combine: 70+19 = 89.',
'Add every colour once: 11+13 = 24, then 24+22 = 46, and 46+2 = 48 marbles.',
'Add tens: 20+30+10+50 = 110. Add ones: 5+1+6+5 = 17. The total is 110+17 = 127. Choose 127.',
'Pair convenient amounts: 53+71 = 124 and 51+49 = 100. Add: 124+100 = 224 pages.',
'Four classes each need 68 pencils: 68+68+68+68. Two classes need 136, and another two need 136. Total: 136+136 = 272 pencils.'
],
'3HW':[
'Add ones: 4+2 = 6; tens: 3+5 = 8; hundreds: 2+3 = 5. The sum is 586.',
'Add ones: 7+3 = 10, so regroup one ten. Tens: 6+1+1 = 8. Keep two hundreds. The sum is 280.',
'Add ones: 8+1 = 9; tens: 7+1 = 8; hundreds: 5+2 = 7. The sum is 789.',
'Add ones: 5+5 = 10, so regroup one ten. Tens: 8+1+1 = 10 tens, so regroup one hundred. Hundreds: 4+1+1 = 6. The sum is 600.',
'Add ones: 6+4 = 10, so regroup one ten. Tens: 4+5+1 = 10 tens, so regroup one hundred. Hundreds: 2+1 = 3. The sum is 300.'
],
'3Rev':[
'Add two tens to the four tens in 245. The result has two hundreds, six tens and five ones: 265.',
'Add two hundreds to the five hundreds in 562. The result is 762.',
'Add four tens to the two tens in 327. The result has three hundreds, six tens and seven ones: 367.',
'Add one hundred to the seven hundreds in 714. The result is 814.',
'Add ones: 6+1 = 7. Add tens: 5+2 = 7. Keep three hundreds. The sum is 377.'
]}
PATCHES={('2HW','2'):{'Question Answers':'90','Hints':'Planting adds trees. Trimming changes the branches but does not remove trees, so only add 65 and 25.'}}
VISUAL_NOTES={'G2U4W1 Q7':'Supplemental image opened in the browser: 156=100+50+6, then 6+14=20 and 100+50+20. Correct method; the new solution supplies the final total 170.'}
PENDING={('worksheets/Grade 2/G2Unit 4/G2U4W2HW.csv','3'):'Source underdetermined: Maria trades 20 rocks, but the question does not say what she receives in exchange. After collecting 80 and giving away 20, she has 60 plus any rocks received. The key 60 assumes none received. Leave pending until the intended exchange is clarified; no video approved and source row unchanged.'}

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--output',required=True,type=Path);parser.add_argument('--apply',action='store_true');args=parser.parse_args()
 with (ROOT/'videos/.production.lock').open('a+') as lock:
  fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
  mp=args.output/'worksheet-video-correspondence.json';doc=json.loads(mp.read_text())
  assert not any(v['production_status']=='in_progress' for v in doc['videos'].values())
  changes=[];writes=[];total=0
  for w,solutions in SOLUTIONS.items():
   rel=f'worksheets/Grade 2/G2Unit 4/G2U4W{w}.csv';p=ROOT/rel
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
  assert total==59
  assert 65+25 == 90
  for (f,q),note in PENDING.items():
   assert doc['worksheets'][f]['problems'][q]['mapping_status']=='needs_review'
   doc['worksheets'][f]['problems'][q]['notes']=note
  if args.apply:
   report={'reviewed_questions':total,'date':'2026-10-09','scope':'Grade 2 Unit 4: 59 answer/solution rows verified; one underdetermined trade remains pending; one supplemental image inspected','visual_review':VISUAL_NOTES,'changes':changes}
   for folder in [ROOT/'videos',args.output]:
    rp=folder/'grade-2-unit-4-source-corrections-2026-10-09.json'
    if changes:assert not rp.exists(),f'Change log already exists: {rp}'
   if changes:
    for folder in [ROOT/'videos',args.output]:save_json(folder/'grade-2-unit-4-source-corrections-2026-10-09.json',report)
   for p,original,updated in writes:
    assert p.read_bytes()==original,'Concurrent source edit: '+str(p)
    if original.decode('utf-8-sig')!=updated:p.write_text(updated)
   validate(doc,read_inventory(),asset_root=args.output.parent);save_json(mp,doc)
  print(f'{total} source questions checked; {len(changes)} rows with improved solutions/corrections. Applied: {args.apply}')

if __name__=='__main__':main()
