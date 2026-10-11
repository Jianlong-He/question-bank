"""Original Grade 2 skip-counting and missing-number worked examples."""
from algebra_lessons import authored
from card_lessons import make_lessons
from number_sense_lessons import source

def g(w,q):return source(2,3,w,q)
SPECS=[]
def add(vid,title,question,answer,opening,steps,ref,expression,value,equalities=()):
 SPECS.append(authored(vid,title,question,answer,opening,steps,ref,expression=expression,value=value,equalities=equalities))
add('count-fixed-tens-hundreds-jumps','Count a fixed number of jumps of ten or one hundred',
 'Start at 235. Take 3 jumps of ten.\nThen restart at 235 and take 3 jumps of one hundred.','265;535',
 'Start at two hundred thirty-five and take three jumps of ten. Then restart and take three jumps of one hundred.',[
 ('COUNT THE TENS JUMPS','Do not count the starting point as a jump','235 → 245 → 255 → 265',
 'Three jumps of ten land on two hundred forty-five, two hundred fifty-five, then two hundred sixty-five.'),
 ('CHECK THE TOTAL CHANGE','Three tens add thirty','235 + 30 = 265',
 'Three jumps of ten add thirty altogether. Two hundred thirty-five plus thirty is two hundred sixty-five.'),
 ('RESTART FOR HUNDREDS','Use the original starting number again','235 → 335 → 435 → 535',
 'Restart at two hundred thirty-five. Three jumps of one hundred land on three hundred thirty-five, four hundred thirty-five, then five hundred thirty-five.'),
 ('CHECK THE JUMP SIZE','Three hundreds add three hundred','235 + 300 = 535',
 'The number of jumps stayed three, but the jump size changed. Three hundreds add three hundred, giving five hundred thirty-five.')],g('1HW',1),'235+3*10','265',[('235+3*100','535')])
add('count-common-fives-tens','Find numbers shared by two skip-counting patterns',
 'Starting at 60, count to 100 by fives and by tens.\nWhich numbers appear in both lists?','60,70,80,90,100',
 'Starting at sixty, count to one hundred by fives and by tens. Which numbers appear in both lists?',[
 ('WRITE THE FIVES LIST','Include the starting and ending numbers','60, 65, 70, 75, 80, 85, 90, 95, 100',
 'The fives list is sixty, sixty-five, seventy, seventy-five, eighty, eighty-five, ninety, ninety-five, one hundred.'),
 ('WRITE THE TENS LIST','Each jump adds ten','60, 70, 80, 90, 100',
 'The tens list is sixty, seventy, eighty, ninety, one hundred.'),
 ('KEEP THE SHARED NUMBERS','A match must occur in both lists','Shared: 60, 70, 80, 90, 100',
 'Every number in the tens list is also in the fives list. Keep those five shared numbers.'),
 ('EXPLAIN THE PATTERN','One jump of ten equals two jumps of five','5 + 5 = 10',
 'Two jumps of five make one jump of ten. From the same starting number, every second fives jump lands on a tens-list number.')],g('1HW',5),'5+5','10')
add('equation-missing-part-regroup-small','Find a missing part or starting whole',
 'Fill the gaps:\n36 + __ = 54\n__ − 17 = 29','18;46',
 'Find the missing numbers in thirty-six plus something equals fifty-four, and something minus seventeen equals twenty-nine.',[
 ('FIND THE MISSING PART','Subtract the known part from the whole','54 − 36 = 18',
 'For the first gap, subtract thirty-six from fifty-four. Regroup as four tens and fourteen ones. Fourteen minus six is eight; four tens minus three tens is one ten.'),
 ('CHECK THE ADDITION','Put eighteen in the gap','36 + 18 = 54',
 'Thirty-six plus eighteen equals fifty-four, so the missing part is eighteen.'),
 ('FIND THE STARTING WHOLE','Put back the amount that was removed','29 + 17 = 46',
 'The second gap is the starting whole. Put back seventeen: twenty-nine plus seventeen equals forty-six.'),
 ('CHECK THE SUBTRACTION','Use the original equation','46 − 17 = 29',
 'Check forty-six minus seventeen. It equals twenty-nine, so the starting whole is forty-six.')],g(3,7),'54-36','18',[('29+17','46'),('46-17','29')])
add('equation-evaluate-then-find-part','Calculate known expressions before finding a missing part',
 'Fill the gaps:\n64 − __ = 18 + 23\n__ + 16 = 80 − 27','23;37',
 'Fill both gaps. First calculate the side whose numbers are already known.',[
 ('CALCULATE THE FIRST TOTAL','Work out eighteen plus twenty-three','18 + 23 = 41\n64 − __ = 41',
 'Eighteen plus twenty-three is forty-one. The first equation becomes sixty-four minus something equals forty-one.'),
 ('FIND THE FIRST GAP','Compare the starting and remaining amounts','64 − 41 = 23\n64 − 23 = 41',
 'The difference between sixty-four and forty-one is twenty-three. That is the amount removed.'),
 ('CALCULATE THE SECOND TOTAL','Work out eighty minus twenty-seven','80 − 27 = 53\n__ + 16 = 53',
 'For the second equation, eighty minus twenty-seven is fifty-three. The gap plus sixteen must equal fifty-three.'),
 ('FIND AND CHECK THE SECOND GAP','Subtract the known part','53 − 16 = 37\n37 + 16 = 53',
 'Subtract sixteen from fifty-three to get thirty-seven. Check: thirty-seven plus sixteen is fifty-three.')],g('4Rev',4),'64-(18+23)','23',[('80-27-16','37')])
add('add-three-two-digit-parts','Add three two-digit parts and check the total',
 'Three boxes hold 26, 18, and 33 pencils.\nHow many pencils are there altogether?','77 pencils',
 'Three boxes hold twenty-six, eighteen, and thirty-three pencils. How many pencils are there altogether?',[
 ('ADD THE FIRST TWO BOXES','Combine two parts first','26 + 18 = 44',
 'First add twenty-six and eighteen. Six plus eight makes fourteen ones. Regroup one ten to get forty-four.'),
 ('INCLUDE THE LAST BOX','Add the third part to the subtotal','44 + 33 = 77',
 'Now add thirty-three to forty-four. Four tens plus three tens is seven tens, and four ones plus three ones is seven ones.'),
 ('CHECK BY PLACE VALUE','All tens and all ones must be counted','20 + 10 + 30 = 60\n6 + 8 + 3 = 17',
 'Check by adding all the tens: sixty. Add all the ones: seventeen.'),
 ('COMBINE THE CHECK TOTALS','Sixty plus seventeen confirms the answer','60 + 17 = 77 pencils',
 'Sixty plus seventeen is seventy-seven. All three boxes together hold seventy-seven pencils.')],g('2Rev',5),'26+18+33','77')
add('arithmetic-two-digit-story-regroup','Follow two-digit changes with regrouping',
 'A shop has 43 notebooks. It sells 18,\nthen receives 27 more. How many does it have now?','52 notebooks',
 'A shop has forty-three notebooks. It sells eighteen, then receives twenty-seven more. How many does it have now?',[
 ('SUBTRACT THE SALE','Regroup before subtracting the ones','43 = 3 tens + 13 ones\n43 − 18 = 25',
 'Selling means subtract. Regroup forty-three as three tens and thirteen ones. Subtract eighteen to leave twenty-five.'),
 ('ADD THE DELIVERY','Use the amount left after the sale','25 + 27',
 'The shop then receives twenty-seven notebooks. Add them to the twenty-five still there.'),
 ('REGROUP THE NEW ONES','Twelve ones become one ten and two ones','5 + 7 = 12\n2 tens + 2 tens + 1 ten = 5 tens',
 'Five plus seven is twelve ones. Regroup one ten, then combine the tens to get five tens and two ones.'),
 ('STATE AND CHECK THE TOTAL','The delivery exceeds the sale by nine','25 + 27 = 52\n27 − 18 = 9; 43 + 9 = 52',
 'There are fifty-two notebooks. As a check, nine more arrived than were sold, so the final count is nine more than forty-three.')],g(5,9),'43-18+27','52')

def lessons(doc):return make_lessons(SPECS,doc)
