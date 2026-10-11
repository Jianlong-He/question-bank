"""Individually reviewed Grade 2 Unit 3 answers and worked solutions."""
import argparse,csv,json,io,fcntl
from pathlib import Path
from build_video_correspondence import ROOT,digest,read_inventory,validate
from generate_video_batch import save_json
SOLUTIONS={
'1':[
'Add tens: 20 + 10 = 30. Add ones: 4 + 3 = 7. Combine: 24 + 13 = 30 + 7 = 37.',
'Add tens: 10 + 50 = 60. Add ones: 6 + 2 = 8. Combine: 16 + 52 = 60 + 8 = 68.',
'25 = 20 + 5 and 62 = 60 + 2. Group the tens and ones: 20+60+5+2 = 87. Choose 20+60+5+2.',
'49 = 40 + 9 and 11 = 10 + 1. The matching expression is 40+10+9+1 = 60. The other choices give 69 and 132.',
'Add ones: 8 + 5 = 13 = 1 ten + 3 ones. Add tens: 2 + 1 + 1 = 4 tens. The total is 43.',
'Add ones: 5 + 7 = 12 = 1 ten + 2 ones. Add tens: 4 + 2 + 1 = 7 tens. The total is 72.',
'Add ones: 6 + 7 = 13 = 1 ten + 3 ones. Add tens: 4 + 3 + 1 = 8 tens. The total is 83.',
'The boxes together hold 27 + 32 cars. Add tens: 20 + 30 = 50; add ones: 7 + 2 = 9. Total: 59 cars.',
'20+40+1+2 = 63; 50+10+3+0 = 63; 30+30+2+1 = 63. Select all three expressions.',
'Add 35 + 48. The ones give 5 + 8 = 13, or 1 ten and 3 ones. The tens give 3 + 4 + 1 = 8. Total: 83 apples.'
],
'1HW':[
'Four jumps of ten are 40. Count 215, 225, 235, 245, 255. The ending number is 255; the starting point is not a jump.',
'Four jumps of one hundred add 400. Count 310, 410, 510, 610, 710. End at 710.',
'Include the first group, 410, then add 100 four times. The five group sizes are 410, 510, 610, 710, and 810 marbles.',
'The complete pattern is 210, 220, 230, 240, 250, 260, 270, 280. Comparing it with the spoken list shows the missing numbers are 240 and 270.',
'Counting by fives from 40 gives 40,45,50,55,60,65,70,75,80. Counting by tens from 40 gives 40,50,60,70,80. The shared numbers are 40,50,60,70,80.'
],
'1Rev':[
'Add five to 105: 105 + 5 = 110. The next number is 110.',
'Add five each time: 50,55,60,65,70,75,80,85. The missing numbers are 65,75,80.',
'The sequence already shows 120 and 130. Continue by adding ten: 140,150,160 are the next three numbers.',
'Add ten each time: 350,360,370,380. The missing numbers are 360 and 370.',
'The sequence from 40 to 60 is 40,45,50,55,60. Select all five of these choices; 43 and 53 are not in the sequence.'
],
'2':[
'87 is 8 tens and 7 ones. Subtract 3 ones: 7 - 3 = 4. Keep the 8 tens, giving 84.',
'68 is 6 tens and 8 ones. Subtract 5 ones: 8 - 5 = 3. Keep the 6 tens, giving 63.',
'30 is 3 tens. Subtract 3 tens from 7 tens, leaving 4 tens. Keep the 5 ones: 75 - 30 = 45.',
'20 is 2 tens. Subtract 2 tens from 4 tens, leaving 2 tens. Keep the 3 ones: 43 - 20 = 23.',
'Subtract ones: 6 - 4 = 2. Subtract tens: 8 - 3 = 5. The result is 52.',
'Subtract ones: 5 - 2 = 3. Subtract tens: 6 - 1 = 5. The result is 53.',
'Regroup 43 as 3 tens and 13 ones. Subtract 6 ones: 13 - 6 = 7. Keep the 3 tens, giving 37.',
'Regroup 86 as 7 tens and 16 ones. Subtract 9 ones: 16 - 9 = 7. Keep the 7 tens, giving 77.',
'First 87 - 3 = 84. Then 84 - 2 = 82. Equivalently, subtract 3 + 2 = 5 from 87 to get 82.',
'First 67 - 1 = 66. Then 66 - 3 = 63. Altogether, 4 were subtracted.'
],
'2HW':[
'Subtract 4 from the ones: 8 - 4 = 4. Keep 7 tens, so 78 - 4 = 74.',
'Subtract 2 tens from 6 tens, keeping 5 ones: 65 - 20 = 45.',
'Subtract ones: 7 - 5 = 2. Subtract tens: 9 - 4 = 5. Thus 97 - 45 = 52.',
'Regroup 52 as 4 tens and 12 ones. Subtract 7 ones to get 5 ones; keep 4 tens. The result is 45.',
'First 76 - 2 = 74; then 74 - 3 = 71. The total removed is 5.'
],
'2Rev':[
'64 = 60 + 4 and 27 = 20 + 7. Thus (60+20)+(4+7) = 80+11 = 91. Enter 60,7,80,91.',
'40+32 = 72; 50+22 = 72; 60+12 = 72. All three expressions have the required total.',
'45+37 gives 70 from the tens and 12 from the ones. Regroup 12 ones as 1 ten and 2 ones. Seven tens plus one ten makes 8 tens, with 2 ones left. Enter 8,2.',
'7+5 = 12 ones = 1 ten and 2 ones. Then 6+2+1 = 9 tens. The result is 9 tens and 2 ones, or 92. Enter 12,1,2,1,9,9,2,92.',
'First add the first two boxes: 34+26 = 60. Then add the third box: 60+35 = 95 cars.'
],
'3':[
'Undo adding 3: 36 - 3 = 33. Check: 33 + 3 = 36.',
'Undo adding 12: 35 - 12 = 23. Check: 23 + 12 = 35.',
'Undo adding 45: 49 - 45 = 4. Check: 4 + 45 = 49.',
'Find the difference between the starting and remaining amounts: 57 - 52 = 5. Check: 57 - 5 = 52.',
'Find how much was removed: 68 - 62 = 6. Check: 68 - 6 = 62.',
'Find how much was removed: 45 - 33 = 12. Check: 45 - 12 = 33.',
'The missing part is 35 - 28. Regroup 35 as 2 tens and 15 ones; subtract to get 7. Check: 28 + 7 = 35.',
'The missing part is 45 - 28. Regroup as 3 tens and 15 ones: 15-8 = 7 ones and 3-2 = 1 ten. The answer is 17. Check: 28+17 = 45.',
'The missing part is 52 - 44. Regroup as 4 tens and 12 ones: 12-4 = 8 and 4-4 = 0 tens. Check: 52-8 = 44.',
'Find the starting whole by putting back the 11 removed: 28+11 = 39. Check: 39-11 = 28.'
],
'3HW':[
'Add tens: 30+10 = 40. Add ones: 5+4 = 9. The total is 49.',
'32 = 30+2 and 16 = 10+6. Both 30+2+10+6 and 30+10+2+6 equal 48. The last option treats tens as ones and equals 12. Select the first two.',
'43 = 40+3 and 32 = 30+2. Adding gives (40+3)+(30+2) = 70+5 = 75. Enter 3,30,70,75.',
'Split 15 into 10 and 5. First 38+10 = 48. Then 48+5 = 53. Enter 48,48,53.',
'Add ones: 7+4 = 11, or 1 ten and 1 one. Add tens: 5+2+1 = 8 tens. Total: 81.'
],
'3Rev':[
'59-4 = 55; then 55-3 = 52. Equivalently, 59-7 = 52.',
'82-7 = 75; then 75-4 = 71. The first subtraction regroups 82 as 7 tens and 12 ones.',
'68-20 = 48; then 48-10 = 38. Altogether, subtract 3 tens.',
'95-42 = 53; then 53-13 = 40. Check: 42+13+40 = 95.',
'93-48 = 45; then 45-25 = 20. In the first step, regroup 93 as 8 tens and 13 ones.'
],
'4':[
'Buying more apples means add: 6+8 = 14. Jess has 14 apples.',
'Selling cookies means subtract: 16-5 = 11. There are 11 cookies left.',
'Add the two types: 14+23 = 37 books. The tens give 30 and the ones give 7.',
'Add the donated paintings: 47+21 = 68. The tens give 60 and the ones give 8.',
'The new planting count is 17 fewer than 78, so subtract: 78-17 = 61 trees will be planted.',
'Tom has 2 fewer than Nick, so 48-2 = 46 stickers.',
'Buying more mangoes means add: 16+8 = 24. Six plus eight makes 14 ones; regroup to get 2 tens and 4 ones.',
'Add both contributions: 64+27. Four plus seven makes 11 ones, and 6+2+1 = 9 tens. Total: 91 cookies.',
'Subtract the purchased cartons: 82-6. Regroup 82 as 7 tens and 12 ones; 12-6 = 6. There are 76 cartons left.',
'The gift is the increase from 47 to 89: 89-47 = 42. Check: 47+42 = 89 toy cars.'
],
'4HW':[
'Subtract ones: 8-5 = 3. Keep 4 tens, so 48-5 = 43.',
'Regroup 52 as 4 tens and 12 ones. Subtract 8 ones to leave 4 ones. The result is 44.',
'Subtract 2 tens from 6 tens and keep 4 ones: 64-20 = 44.',
'Subtract ones: 9-5 = 4. Subtract tens: 7-3 = 4. Thus 79-35 = 44.',
'Regroup 74 as 6 tens and 14 ones. Subtract ones: 14-6 = 8; subtract tens: 6-2 = 4. The result is 48.'
],
'4Rev':[
'The removed amount is 75-50 = 25. Check: 75-25 = 50.',
'Add the known parts: 30+15 = 45. Subtract them from the whole: 75-45 = 30. Check: 30+30+15 = 75.',
'First 90-25 = 65. Now 65 minus the gap must equal 40, so the gap is 65-40 = 25. Check: 90-25-25 = 40.',
'Calculate the right side: 70-15 = 55. The gap plus 20 equals 55, so the gap is 55-20 = 35. Check: 35+20 = 55.',
'Calculate the right side: 35+20 = 55. The removed part is 80-55 = 25. Check: 80-25 = 55.'
],
'5':[
'Add the first gift: 5+2 = 7. Add the purchase: 7+8 = 15 stickers.',
'After the morning sale, 9-3 = 6 remain. After the afternoon sale, 6-5 = 1 action figure remains.',
'First add the purchase: 7+5 = 12. Then subtract the gift: 12-2 = 10 stickers remain.',
'After the delivery, 11+7 = 18 books. Lending 6 leaves 18-6 = 12 books.',
'Pages already read: 5+6 = 11. Add the 8 unread pages: 11+8 = 19 pages in the book.',
'Count all three parts: 24+11 = 35 decorated cookies; 35+12 = 47 cookies in the original batch.',
'After selling 5 muffins, 14-5 = 9 remain. Baking 10 more gives 9+10 = 19 muffins. Nine is the amount remaining after the sale, not the amount sold.',
'First count all the cards: 67+19 = 86. Giving away 15 leaves 86-15 = 71 trading cards.',
'After the sale, 55-19 = 36 toy cars. After the delivery, 36+32 = 68 toy cars.',
'Ben has 28-7 = 21 stamps. Celia has 5 fewer than Ben, so 21-5 = 16 stamps.'
],
'5HW':[
'Undo adding 15: 40-15 = 25. Check: 25+15 = 40.',
'Find the missing part: 50-32 = 18. Check: 32+18 = 50.',
'Find the amount removed: 65-40 = 25. Check: 65-25 = 40.',
'Put back the 20 removed: 35+20 = 55. Check: 55-20 = 35.',
'Add the known parts: 18+14 = 32. The missing part is 60-32 = 28. Check: 18+28+14 = 60.'
],
'5Rev':[
'Fewer means subtract: 55-38. Regroup 55 as 4 tens and 15 ones; 15-8 = 7 ones and 4-3 = 1 ten. Mia has 17 cards.',
'Subtract shipped boxes: 94-46. Regroup 94 as 8 tens and 14 ones; 14-6 = 8 ones and 8-4 = 4 tens. There are 48 boxes left.',
'Undo the donation: 89-42 = 47 chairs before the donation. Check: 47+42 = 89.',
'Jordan brings 36 fewer than 75: 75-36. Regroup as 6 tens and 15 ones; 15-6 = 9 ones and 6-3 = 3 tens. Jordan brings 39 cupcakes.',
'The number bought is the starting count minus the remaining count: 95-48 = 47. Check: 47+48 = 95 loaves.'
]}
PATCHES={
('1HW','4'):{'Question Choices':'Benny is counting by tens. He says 210, 220, 230, 250, 260, 280, skipping two numbers. What are the two numbers he missed? Write them in order.'},
('1Rev','3'):{'Question Choices':'Continue the sequence 120, 130 by counting by tens. What are the next three numbers?'},
('3HW','2'):{'Question Choices':'Select all expressions that correctly show the addition of 32 + 16: ~~30+2+10+6 | 30+10+2+6 | 3+2+1+6~~','Question Answers':'30+2+10+6,30+10+2+6'},
('3HW','3'):{'Question Choices':'Fill: 43 + 32 = (40 + __) + (__ + 2) = __ + 5 = __','Hints':'Write 43 as 40+3 and 32 as 30+2. Then combine the tens and combine the ones.'},
('3HW','4'):{'Question Choices':'Fill the missing numbers when adding 38 + 15. Split 15 into 10 and 5, then add the tens first and the ones next: 38 + 10 = __, then __ + 5 = __'},
('5','7'):{'Image URL':''}
}
VISUAL_NOTES={
'G2U3W1 Q5':'The linked solution image correctly regroups 8+5=13 and adds 2+1+1=4 tens.',
'G2U3W1 Q6':'The linked solution image correctly regroups 5+7=12 and adds 4+2+1=7 tens.',
'G2U3W1 Q7':'The linked solution image correctly regroups 6+7=13 and adds 4+3+1=8 tens.',
'G2U3W2 Q7':'The linked image correctly changes 43 to 3 tens and 13 ones, then subtracts six ones.',
'G2U3W2 Q8':'The linked image correctly changes 86 to 7 tens and 16 ones, then subtracts nine ones.',
'G2U3W5 Q3':'The linked image correctly shows the first addition, 7+5=12; the new text solution finishes the subtraction.',
'G2U3W5 Q5':'The linked image correctly adds 5+6=11 read pages and says to add unread pages; the new text solution finishes 11+8=19.',
'G2U3W5 Q7':'The linked image incorrectly labels 14-5=9 as the number sold; it is the number remaining. Removed this optional misleading image link and supplied a complete correct text solution. Original URL is retained in the change log.'}

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--output',required=True,type=Path);parser.add_argument('--apply',action='store_true');args=parser.parse_args()
 with (ROOT/'videos/.production.lock').open('a+') as lock:
  fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
  mp=args.output/'worksheet-video-correspondence.json';doc=json.loads(mp.read_text())
  assert not any(v['production_status']=='in_progress' for v in doc['videos'].values())
  changes=[];writes=[];total=0
  for w,solutions in SOLUTIONS.items():
   rel=f'worksheets/Grade 2/G2Unit 3/G2U3W{w}.csv';p=ROOT/rel
   original=p.read_bytes();reader=csv.DictReader(io.StringIO(original.decode('utf-8-sig')));fields=reader.fieldnames;rows=list(reader)
   assert len(rows)==len(solutions)
   for row in rows:
    q=row['Question ID'];before=dict(row);row['Solution']=solutions[int(q)-1];row.update(PATCHES.get((w,q),{}))
    if row!=before:changes.append({'worksheet':rel,'question_id':q,'before':before,'after':dict(row)})
    assert row['Solution'] and row['Question Answers']
    prob=doc['worksheets'][rel]['problems'][q];prob['question_text']=row['Question Choices'];prob['question_sha256']=digest(row['Question Choices'])
    total+=1
   buf=io.StringIO(newline='');writer=csv.DictWriter(buf,fieldnames=fields,lineterminator='\n');writer.writeheader();writer.writerows(rows)
   writes.append((p,original,buf.getvalue()))
  assert total==100
  # Independently check the corrected decompositions and sequence gaps.
  assert 30+2+10+6 == 30+10+2+6 == 32+16 == 48
  assert (40+3)+(30+2) == 70+5 == 43+32 == 75
  assert sorted(set(range(210,281,10))-{210,220,230,250,260,280}) == [240,270]
  assert 14-5+10 == 19
  if args.apply:
   report={'reviewed_questions':total,'date':'2026-10-09','scope':'Grade 2 Unit 3; all answers, choices, hints and solutions reviewed; eight external solution figures inspected in browser','visual_review':VISUAL_NOTES,'changes':changes}
   for folder in [ROOT/'videos',args.output]:
    rp=folder/'grade-2-unit-3-source-corrections-2026-10-09.json'
    if changes:assert not rp.exists(),f'Change log already exists: {rp}'
   if changes:
    for folder in [ROOT/'videos',args.output]:save_json(folder/'grade-2-unit-3-source-corrections-2026-10-09.json',report)
   for p,original,updated in writes:
    assert p.read_bytes()==original,'Concurrent source edit: '+str(p)
    if original.decode('utf-8-sig')!=updated:p.write_text(updated)
   validate(doc,read_inventory(),asset_root=args.output.parent);save_json(mp,doc)
  print(f'{total} source questions checked; {len(changes)} rows with improved solutions/corrections. Applied: {args.apply}')

if __name__=='__main__':main()
