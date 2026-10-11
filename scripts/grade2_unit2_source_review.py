"""Reviewed worked solutions and precise corrections for Grade 2 Unit 2.

Each authored entry is tied to a worksheet/question pair. --apply writes a full
before/after record and synchronizes the canonical question identity fields.
"""
import argparse,csv,json,io,fcntl,hashlib
from pathlib import Path
from build_video_correspondence import ROOT,digest,read_inventory,validate
from generate_video_batch import save_json

SOLUTIONS={
'1':[
'45 = 4 tens + 5 ones = 40 + 5. The tens digit is 4 and the ones digit is 5.',
'98 = 9 tens + 8 ones = 90 + 8. The tens digit is 9 and the ones digit is 8.',
'134 = 1 hundred + 3 tens + 4 ones = 100 + 30 + 4. Enter 1, 3, 4.',
'528 = 5 hundreds + 2 tens + 8 ones = 500 + 20 + 8. Enter 5, 2, 8.',
'A value of 30 means 3 tens. In 232, the 3 is in the tens place. In 345 and 356 it is worth 300; in 513 it is worth 3. Choose 232.',
'A value of 500 means 5 hundreds. Only 517 has 5 in the hundreds place. Choose 517.',
'A value of 7 means 7 ones. Only 517 has 7 in the ones place. Choose 517.',
'To make the largest number, put the digits in descending order: 8, 3, 2. The number is 832.',
'Use the largest digit in hundreds, then the next largest in tens: 8, 7, 3. The largest number is 873.',
'Keep 3 in the tens place. Of the remaining digits, 9 is larger than 5, so put 9 in hundreds and 5 in ones. The number is 935.'
],
'1HW':[
'First subtract the used stickers: 20 - 5 = 15. Then add the new stickers: 15 + 8 = 23. There are 23 stickers.',
'First count all the pens: 5 + 3 + 4 = 12. Then subtract the 4 given away: 12 - 4 = 8 pens.',
'After 5 pencils are taken, 20 - 5 = 15 remain. Returning 3 gives 15 + 3 = 18 pencils.',
'The two purchases added 4 + 2 = 6 toys. Undo those additions: 15 - 6 = 9. Check: 9 + 4 + 2 = 15.',
'Work backwards from 15. Undo the delivery: 15 - 6 = 9. Put back the 5 eaten: 9 + 5 = 14. Check: 14 - 5 + 6 = 15 snacks.'
],
'1Rev':[
'63 = 6 tens + 3 ones = 60 + 3. Enter 6, 3.',
'247 = 2 hundreds + 4 tens + 7 ones = 200 + 40 + 7. Enter 2, 4, 7.',
'For 6 to be worth 60, it must be in the tens place. In 264 it is in tens; in 645 it is in hundreds, and in 456 and 736 it is in ones. Choose 264.',
'Arrange the digits from largest to smallest: 9, 4, 2. The largest number is 942.',
'Keep 2 in tens. Put the larger remaining digit, 8, in hundreds and 6 in ones. The largest possible number is 826.'
],
'2':[
'54 has 5 tens and 4 ones, so 54 = 50 + 4. Enter 50, 4.',
'65 has 6 tens and 5 ones, so 65 = 60 + 5. Enter 60, 5.',
'847 has 8 hundreds, 4 tens, and 7 ones. Thus 847 = 800 + 40 + 7. Enter 800, 40, 7.',
'368 has 3 hundreds, 6 tens, and 8 ones. Thus 368 = 300 + 60 + 8. Enter 300, 60, 8.',
'Seven hundred is 700, twenty is 20, and eight is 8. Add: 700 + 20 + 8 = 728.',
'Two hundred is 200, forty is 40, and three is 3. Add: 200 + 40 + 3 = 243.',
'600 + 40 + 5 has 6 hundreds, 4 tens, and 5 ones. The number is 645.',
'900 + 30 + 8 has 9 hundreds, 3 tens, and 8 ones. The number is 938.',
'Seven hundred nineteen is 719 = 700 + 10 + 9. The other expressions give 729 and 7100, so choose 700+10+9.',
'576 = 500 + 70 + 6. Read these parts as five hundred, seventy, six: five hundred seventy-six.'
],
'2HW':[
'For 2 to be worth 20, it must be in tens. Both 429 and 328 have 2 in the tens place. In 234 it is worth 200 and in 402 it is worth 2. Select 429 and 328.',
'Arrange the digits from smallest to largest: 2, 5, 8. The smallest number is 258.',
'Keep 6 in ones. Put the larger remaining digit, 4, in hundreds and 2 in tens. The largest possible number is 426.',
'In 549, the 5 is worth 500 and the 4 is worth 40. Their combined value is 500 + 40 = 540.',
'Write the digits in hundreds, tens, ones order: 4, 0, 7. The zero holds the empty tens place, giving 407.'
],
'2Rev':[
'492 = 4 hundreds + 9 tens + 2 ones = 400 + 90 + 2. Enter 4, 9, 2.',
'A value of 400 means 4 hundreds. Only 475 has 4 in the hundreds place. Choose 475.',
'Put the digits in descending order: 9, 4, 1. The largest number is 941.',
'Put the digits in descending order: 6, 5, 2. The largest number is 652.',
'903 has 9 hundreds, 0 tens, and 3 ones. The zero preserves the tens place. Enter 9, 0, 3.'
],
'3':[
'Each ten is 10 ones. Four tens are 4 × 10 = 40 ones.',
'Each hundred is 10 tens. Six hundreds are 6 × 10 = 60 tens.',
'Ten tens make 1 hundred. Divide 70 tens by 10 tens per hundred: 70 ÷ 10 = 7 hundreds.',
'Ten ones make 1 ten. Divide 50 ones by 10: 50 ÷ 10 = 5 tens.',
'12 ones = 1 ten + 2 ones. Add the extra ten to 7 tens: 8 tens + 2 ones. The missing number is 2.',
'25 ones = 2 tens + 5 ones. Add the 2 tens to 4 tens: 6 tens + 5 ones. The missing number is 6.',
'18 tens = 1 hundred + 8 tens. Add that hundred to 5 hundreds: 6 hundreds + 8 tens. Enter 6.',
'34 tens = 3 hundreds + 4 tens. Add the 3 hundreds to the original 3 hundreds: 6 hundreds + 4 tens. Enter 4.',
'785 = 700 + 80 + 5. Exchange the 7 hundreds for 70 tens; 70 tens + 8 tens = 78 tens. Thus 785 = 0 hundreds + 78 tens + 5 ones.',
'400+50+6 = 456. Also 30+20 = 50, so 400+30+20+6 = 456. Finally 300+100 = 400, so 300+100+50+6 = 456. All three expressions match.'
],
'3HW':[
'912 = 900 + 12, read as nine hundred twelve. Select nine-hundred-twelve.',
'5238 has 5 thousands, 2 hundreds, 3 tens, and 8 ones. Their values are 5000, 200, 30, and 8. Choose 5000+200+30+8.',
'Nine hundred forty-six has 9 hundreds, 4 tens, and 6 ones. Its standard form is 946 and its expanded form is 900+40+6.',
'500+20+3 = 523. Five hundred thirty-one is 531. Both have 5 hundreds, but 531 has 3 tens while 523 has 2 tens. Five hundred thirty-one is greater.',
'482 = 4 hundreds + 8 tens + 2 ones = 400 + 80 + 2. Enter 400, 80, 2.'
],
'3Rev':[
'526 has 5 hundreds, 2 tens, and 6 ones. Expanded form is 500 + 20 + 6. Enter 500, 20, 6.',
'Four hundred fifty-three = 400 + 50 + 3 = 453.',
'800 + 20 + 9 has 8 hundreds, 2 tens, and 9 ones, so the number is 829.',
'Six hundred forty-seven is 647. Both 600+40+7 and 600+47 equal 647. The last option, 600+4+7, equals 611. Select the first two.',
'3745 = 3000 + 700 + 40 + 5. The missing values are 3000 and 40.'
],
'4':[
'5 is greater than 3, so 5 > 3. Enter >.',
'14 has 1 ten; 21 has 2 tens. Therefore 14 < 21. Enter <.',
'Both numbers have 3 tens. Compare ones: 4 < 5, so 34 < 35. Enter <.',
'Compare hundreds first: 367 has 3 hundreds and 456 has 4 hundreds. Therefore 367 < 456. Enter <.',
'The hundreds and tens are equal. Compare ones: 5 > 4, so 745 > 744. Enter >.',
'40 + 9 = 49, and 5 tens 3 ones = 53. Since 49 < 53, enter <.',
'600 + 30 + 5 = 635. Six hundreds, five tens, and three ones make 653. Compare tens after the equal hundreds: 3 < 5, so 635 < 653.',
'7 hundreds 2 tens 3 ones = 723. Both numbers have 7 hundreds; 713 has 1 ten while 723 has 2 tens. Thus 713 < 723.',
'The baker has 800 + 80 + 9 = 889 cookies. The candy store has 819. The hundreds match, but 8 tens exceed 1 ten. The baker has more.',
'7 hundreds 11 tens 8 ones = 700 + 110 + 8 = 818. Since 818 < 819, enter <.'
],
'4HW':[
'Convert each place count to its value: 3 hundreds = 300, 12 tens = 120, and 15 ones = 15. Add: 300 + 120 + 15 = 435.',
'The large boxes hold 5 × 100 = 500 pencils. The smaller boxes hold 22 × 10 = 220. Together they hold 500 + 220 = 720 pencils.',
'16 tens + 5 ones = 160 + 5 = 165. The missing value is 465 - 165 = 300, which is 3 hundreds. Enter 3.',
'200+140+5 = 345; 100+240+5 = 345; 0+340+5 = 345. All three expressions give the same total, so select all three.',
'100+110+5 = 215; 200+10+5 = 215; 0+210+5 = 215. All three expressions give 215, so select all three.'
],
'4Rev':[
'15 tens = 1 hundred + 5 tens. Add the extra hundred to 4 hundreds: 5 hundreds + 5 tens. Enter 5.',
'4 hundreds = 400 ones. The remaining value is 520 - 400 = 120 ones, which equals 12 tens. Enter 12.',
'With no hundreds, all 180 ones must be written as tens. Since 180 ÷ 10 = 18, enter 18.',
'2 hundreds = 200 ones and 15 tens = 150 ones. Add the 12 ones: 200 + 150 + 12 = 362 ones.',
'4 hundreds = 400 pieces and 35 tens = 350 pieces. Total: 400 + 350 = 750. This makes 7 complete groups of 100, with 50 pieces left over.'
],
'5':[
'The image shows 4 rabbits. They form 2 pairs with none left over, so 4 is even. Choose Yes.',
'The image shows 9 basketballs. They form 4 pairs with 1 left over, so 9 is odd. Choose Yes.',
'Image A has 3 caps, B has 2, and C has 5. Only 2 forms complete pairs with none left over. Choose B.',
'Image A has 6 caps, B has 8, and C has 5. Only 5 leaves one cap unpaired, so choose C.',
'The options contain 5, 4, 6, and 1 stars. The even counts are 4 and 6, so choose the groups of four and six stars.',
'The options contain 1, 2, 5, and 6 apples. The odd counts are 1 and 5, so choose the groups of one and five apples.',
'The options contain 5, 6, 7, 2, and 11 stars. The odd counts are 5, 7, and 11. Select those three groups.',
'Image A has 6 caps, B has 10, and C has 14. Each count can be paired without a leftover, so all three are even. Select A, B, and C.',
'The even numbers greater than 3 and less than 9 are 4, 6, and 8. Each is two more than the previous one.',
'Add the two amounts: 3 + 5 = 8 dollars. Since 8 can be split into two equal groups of 4, the total is even.'
],
'5HW':[
'5 hundreds 12 tens 4 ones = 500 + 120 + 4 = 624. Since 624 > 623, enter >.',
'Sarah has 500 + 60 + 2 = 562, and Mike also has 500 + 60 + 2 = 562. Their amounts are equal. Choose Sarah=Mike.',
'The farmer has 600 + 150 + 4 = 754 eggs. The grocery store also has 754. Neither has more; they have the same amount.',
'Red has 700 + 20 = 720 beads; blue has 720; green has 600 + 100 = 700; yellow has 600 + 90 = 690. Red and blue tie for the largest count. Select both.',
'800 + 500 + 50 + 2 = 1300 + 50 + 2 = 1352. Both sides equal 1352, so enter =.'
],
'5Rev':[
'The hundreds are both 8. Compare tens: 2 < 3. Therefore 823 < 832. Enter <.',
'Compare thousands first: 5021 has 5 thousands while 2051 has 2 thousands. Therefore 5021 > 2051. Enter >.',
'Both numbers have 6 hundreds. Compare tens: 7 > 2. Therefore 672 is greater than 627.',
'4 hundreds 2 tens 5 ones = 400 + 20 + 5 = 425. The values are equal, so enter =.',
'700 + 40 + 2 = 742. Seven hundreds, three tens, and nine ones make 739. The hundreds match, but 4 tens exceed 3 tens. Enter >.'
],
'6':[
'A jump of five adds 5. Calculate 53 + 5 = 58. The next number is 58.',
'Add five: 99 + 5 = 104. This jump crosses one hundred.',
'Add 5 each time: 10, 15, 20, 25, 30, 35, 40. The missing numbers are 20, 30, 35.',
'Count from 163 by adding 5: 168, 173, 178, 183, and so on. Among the choices, select 168, 173, and 178.',
'Add ten: 53 + 10 = 63. The next number is 63.',
'Add 100 twice: 470 + 100 = 570, then 570 + 100 = 670. The next two numbers are 570 and 670.',
'Add 10 each time: 199, 209, 219, 229. Enter 209 and 219.',
'The sequence is 20, 25, 30, 35, 40. Of the listed choices, only 25 and 30 occur in this sequence.',
'Take three jumps, not counting the starting point: 85 + 5 = 90; 90 + 5 = 95; 95 + 5 = 100. End at 100.',
'Add 100 repeatedly: 16, 116, 216, 316, and so on. Select 116, 216, and 316.'
],
'6HW':[
'Odd numbers end in 1, 3, 5, 7, or 9. In the choices, 15 ends in 5 and 49 ends in 9. Select 15 and 49.',
'The first even number greater than 40 is 42. Keep adding 2: 42, 44, 46, 48, 50.',
'The first odd number greater than 40 is 41. Keep adding 2: 41, 43, 45, 47, 49.',
'24 ÷ 2 = 12. The two groups can receive 12 pieces each with none left over. Choose Yes.',
'The total is 25 + 31 = 56 dollars. Since 56 ends in 6, it is even; it also splits into two groups of 28.'
],
'6Rev':[
'The two groups contain 6 and 7 birds. Six forms 3 complete pairs, while 7 leaves one unpaired. Choose the group of 6 birds.',
'The two groups contain 4 and 7 pineapples. Four is even; 7 forms 3 pairs and one leftover, so choose the group of 7 pineapples.',
'Between 30 and 40 means greater than 30 and less than 40. The even numbers are 32, 34, 36, 38.',
'22 ÷ 2 = 11. Make two equal groups of 11 kids with no leftover. Choose Yes.',
'The odd numbers greater than 40 and less than 50 are 41, 43, 45, 47, 49.'
]}
PATCHES={
('1HW','5'):{'Hints':'Work backwards from 15. Undo the delivery by subtracting 6, then put back the 5 snacks eaten.'},
('2HW','1'):{'Question Choices':'Select all numbers that have the digit 2 representing a value of 20: ~~234 | 429 | 328 | 402~~','Question Answers':'429,328'},
('3','6'):{'Hints':'Split 25 ones into 20 + 5 = 2 tens + 5 ones. Add the two tens to the existing four tens.'},
('3HW','2'):{'Hints':'5 thousands = 5000; 2 hundreds = 200; 3 tens = 30; 8 ones = 8.'},
('4Rev','5'):{'Question Choices':'Sam has 4 hundreds of Lego pieces and gets 35 tens more. How many complete groups of 100 pieces can he make in total?'},
('5HW','3'):{'Question Choices':'Select who has more eggs. A farmer has 6 hundreds 15 tens 4 ones eggs. A grocery store has 754 eggs. ~~farmer | grocery-store | same amount~~','Question Answers':'same amount'},
('5HW','4'):{'Question Choices':'Select all boxes with the most beads. Red has 7 hundreds 2 tens, blue has 720, green has 600 + 100, and yellow has 6 hundreds 9 tens. ~~red | blue | green | yellow~~','Question Answers':'red,blue'},
('6','8'):{'Hints':'Starting at 20, add 5 each time until 40. This particular sequence has numbers ending in 0 or 5.'},
('6Rev','1'):{'Question Choices':'Select all choices that have an even number of birds: ~~🐦🐦🐦🐦🐦🐦 | 🐦🐦🐦🐦🐦🐦🐦~~'},
('6Rev','2'):{'Question Choices':'Select all choices that have an odd number of pineapples: ~~🍍🍍🍍🍍 | 🍍🍍🍍🍍🍍🍍🍍~~'},
('6Rev','4'):{'Question Choices':'Select. A classroom has 22 kids. Can the teacher split the kids into two equal groups with no leftover? ~~Yes | No~~'}
}
VISUAL_COUNTS={'1':[4],'2':[9],'3':[3,2,5],'4':[6,8,5],'8':[6,10,14]}

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--output',required=True,type=Path);parser.add_argument('--apply',action='store_true');args=parser.parse_args()
 with (ROOT/'videos/.production.lock').open('a+') as lock:
  fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
  mp=args.output/'worksheet-video-correspondence.json';doc=json.loads(mp.read_text())
  assert not any(v['production_status']=='in_progress' for v in doc['videos'].values())
  changes=[];writes=[];total=0
  for w,solutions in SOLUTIONS.items():
   rel=f'worksheets/Grade 2/G2Unit 2/G2U2W{w}.csv';p=ROOT/rel
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
  assert total==120
  # Independent arithmetic checks for the corrected keys and reviewed figures.
  assert (429//10)%10 == (328//10)%10 == 2
  assert 6*100+15*10+4 == 754
  assert 7*100+2*10 == 720 > 600+100 > 6*100+9*10
  assert all(n%2==0 for n in VISUAL_COUNTS['8'])
  assert [i for i,n in enumerate(VISUAL_COUNTS['3']) if n%2==0]==[1]
  assert [i for i,n in enumerate(VISUAL_COUNTS['4']) if n%2]==[2]
  if args.apply:
   report={'reviewed_questions':total,'date':'2026-10-09','scope':'Grade 2 Unit 2; all answers, choices, hints and solutions reviewed; five external source figures inspected in browser','visual_counts':VISUAL_COUNTS,'changes':changes}
   for folder in [ROOT/'videos',args.output]:
    rp=folder/'grade-2-unit-2-source-corrections-2026-10-09.json'
    if changes:assert not rp.exists(),f'Change log already exists: {rp}'
   if changes:
    for folder in [ROOT/'videos',args.output]:save_json(folder/'grade-2-unit-2-source-corrections-2026-10-09.json',report)
   for p,original,updated in writes:
    assert p.read_bytes()==original,'Concurrent source edit: '+str(p)
    if original.decode('utf-8-sig')!=updated:p.write_text(updated)
   validate(doc,read_inventory(),asset_root=args.output.parent);save_json(mp,doc)
  print(f'{total} source questions checked; {len(changes)} rows with improved solutions/corrections. Applied: {args.apply}')

if __name__=='__main__':main()
