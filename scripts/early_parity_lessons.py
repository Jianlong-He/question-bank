"""Original early place-value, parity, and skip-counting examples."""
from algebra_lessons import authored
from card_lessons import make_lessons,draw_card
from number_sense_lessons import source
import generate_sample_videos as v

def g(w,q):return source(2,2,w,q)
SPECS=[]
def add(vid,title,question,answer,opening,steps,ref,expression,value,equalities=()):
 SPECS.append(authored(vid,title,question,answer,opening,steps,ref,expression=expression,value=value,equalities=equalities))

add('place-digit-value-small','Find a digit from the value it represents',
 'Which number has a 6 worth 600?\n263, 682, 346, or 526?','682',
 'Which number has a six worth six hundred: two hundred sixty-three, six hundred eighty-two, three hundred forty-six, or five hundred twenty-six?',[
 ('MATCH THE UNIT','Six hundred means six hundreds','600 = 6 hundreds',
 'Six hundred means six hundreds. We need the six to be in the hundreds place.'),
 ('READ FROM THE RIGHT','Ones, tens, then hundreds','Hundreds | Tens | Ones',
 'Read the places from the right: ones, tens, then hundreds.'),
 ('CHECK EACH SIX','The digit’s place changes its value','263: 60; 682: 600\n346: 6; 526: 6',
 'The six is worth sixty in two hundred sixty-three, six hundred in six hundred eighty-two, and six in both other numbers.'),
 ('SELECT THE MATCH','Choose the number with six hundreds','682 = 600 + 80 + 2',
 'Choose six hundred eighty-two. Its six stands for six hundreds, or six hundred.')],g(1,6),'6*100','600')
add('place-three-digit-word-forms','Write a number in digits, words, and expanded form',
 'Write six hundred eighty-four in digits.\nThen write its expanded form.','684;600 + 80 + 4',
 'Write six hundred eighty-four in digits, then write its expanded form.',[
 ('LIST THE PLACE COUNTS','Read one place at a time','6 hundreds; 8 tens; 4 ones',
 'Six hundred gives six hundreds. Eighty gives eight tens. Four gives four ones.'),
 ('WRITE THE DIGITS','Use hundreds, tens, ones order','6 | 8 | 4 → 684',
 'Write six, eight, four in hundreds, tens, ones order. The standard form is six hundred eighty-four.'),
 ('EXPAND THE VALUES','Show the value of every digit','684 = 600 + 80 + 4',
 'Expanded form shows each digit’s value: six hundred plus eighty plus four.'),
 ('READ IT BACK','All three forms name the same number','684 = six hundred eighty-four\n= 600 + 80 + 4',
 'Read the parts back as six hundred eighty-four. Digits, words, and expanded form all describe the same number.')],g(2,5),'600+80+4','684')
add('place-equivalent-sums-small','Check different ways to represent the same number',
 'Which expressions equal 538?\n500 + 30 + 8; 400 + 130 + 8; 500 + 3 + 8','First and second expressions',
 'Which expressions equal five hundred thirty-eight? Check all three, because more than one may be correct.',[
 ('CHECK THE USUAL EXPANSION','Five hundreds, three tens, eight ones','500 + 30 + 8 = 538',
 'Five hundred plus thirty plus eight is five hundred thirty-eight. The first expression matches.'),
 ('CHECK THE REGROUPED FORM','Thirteen tens have a value of 130','400 + 130 + 8 = 538',
 'Four hundred plus one hundred thirty plus eight is also five hundred thirty-eight. The second matches too.'),
 ('CHECK EVERY OPTION','Three ones are not three tens','500 + 3 + 8 = 511',
 'The third expression has three ones instead of three tens. It adds to five hundred eleven, so it does not match.'),
 ('SELECT ALL MATCHES','Different groupings can keep the same total','538 = 5 hundreds + 3 tens + 8 ones\n= 4 hundreds + 13 tens + 8 ones',
 'Choose the first and second expressions. Trading one hundred for ten tens changes the grouping, but keeps the total the same.')],g(3,10),'400+130+8','538',[('500+3+8','511')])
add('parity-pair-object-groups','Decide even or odd by making pairs',
 'Group P has 12 counters. Group Q has 13.\nWhich group has an even number?','P is even; Q is odd',
 'Group P has twelve counters and group Q has thirteen. Which group has an even number?',[
 ('PAIR GROUP P','Put two counters in each pair','12 = 2 + 2 + 2 + 2 + 2 + 2',
 'Group P makes six pairs. Every counter has a partner.'),
 ('EVEN MEANS NO LEFTOVER','All twelve counters belong to pairs','12 is even.',
 'No counter is left over, so twelve is even.'),
 ('PAIR GROUP Q','One counter has no partner','13 = 2 + 2 + 2 + 2 + 2 + 2 + 1',
 'Group Q makes six pairs with one counter left over. Thirteen is odd.'),
 ('COMPARE THE GROUPS','No leftover: even. One leftover: odd.','P: 12, even\nQ: 13, odd',
 'Group P is even and group Q is odd. Pairing works even when the counters are arranged differently.')],g(5,1),'6*2','12',[('6*2+1','13')])
add('parity-last-digit-small','Use the last digit to decide even or odd',
 'Are 146 and 283 even or odd?','146 is even;283 is odd',
 'Are one hundred forty-six and two hundred eighty-three even or odd?',[
 ('CHECK THE ONES DIGIT','Full tens can always be paired','Even endings: 0, 2, 4, 6, 8',
 'Full tens can be paired with no leftover, so check the ones digit. Zero, two, four, six, and eight are even endings.'),
 ('CLASSIFY THE FIRST NUMBER','146 ends in six','146 is even.',
 'One hundred forty-six ends in six. Six can be paired evenly, so the whole number is even.'),
 ('CLASSIFY THE SECOND NUMBER','283 ends in three','Odd endings: 1, 3, 5, 7, 9\n283 is odd.',
 'Two hundred eighty-three ends in three. One, three, five, seven, and nine are odd endings.'),
 ('USE THE SAME TEST EVERY TIME','Look at the last digit only','146 → 6 → even\n283 → 3 → odd',
 'Always inspect the last digit. The earlier digits do not change whether the number is even or odd.')],g('6HW',1),'146%2','0',[('283%2','1')])
add('parity-next-even-odd-sequences','List the next even and odd numbers',
 'Write the next four even numbers after 66.\nThen write the next four odd numbers after 66.','68,70,72,74;67,69,71,73',
 'Write the next four even numbers after sixty-six, then the next four odd numbers after sixty-six.',[
 ('FIND THE FIRST EVEN NUMBER','After means greater than sixty-six','First even number: 68',
 'After sixty-six means greater than sixty-six. The first even number is sixty-eight.'),
 ('STEP BY TWO','Even numbers are two apart','68, 70, 72, 74',
 'Add two each time. The next four even numbers are sixty-eight, seventy, seventy-two, and seventy-four.'),
 ('FIND THE FIRST ODD NUMBER','Sixty-seven is the next odd number','First odd number: 67',
 'For odd numbers, start at sixty-seven, the first odd number above sixty-six.'),
 ('STEP BY TWO AGAIN','Odd numbers are also two apart','67, 69, 71, 73',
 'Again add two each time. The next four odd numbers are sixty-seven, sixty-nine, seventy-one, and seventy-three.')],g(5,9),'68+2+2+2','74',[('67+2+2+2','73')])
add('parity-total-after-addition','Add first, then decide whether the total is even or odd',
 'A jar has 17 blue and 26 green beads.\nIs the total number of beads even or odd?','43;odd',
 'A jar has seventeen blue beads and twenty-six green beads. Is the total number of beads even or odd?',[
 ('FIND THE TOTAL','The question is about all the beads','17 + 26',
 'The question asks about all the beads, so add the two amounts first.'),
 ('ADD TENS AND ONES','Regroup thirteen ones as one ten and three ones','10 + 20 = 30; 7 + 6 = 13\n30 + 13 = 43',
 'The tens make thirty. Seven plus six makes thirteen ones. Thirty plus thirteen is forty-three.'),
 ('READ THE LAST DIGIT','Forty-three ends in three','43 → 3 → odd',
 'Forty-three ends in three. Three is an odd ending, so the total is odd.'),
 ('CHECK BY PAIRING','One bead would have no partner','43 = 21 pairs + 1 bead',
 'Forty-three beads make twenty-one pairs with one bead left over. That confirms an odd total.')],g(5,10),'17+26','43',[('21*2+1','43')])
add('count-fives-from-any-start','Skip count by five from any starting number',
 'Start at 97. Take three jumps of 5.\nWhat numbers do you land on?','102,107,112',
 'Start at ninety-seven and take three jumps of five. What numbers do you land on?',[
 ('MAKE THE FIRST JUMP','Add five to the starting number','97 + 5 = 102',
 'The first jump adds five to ninety-seven. We cross one hundred and land on one hundred two.'),
 ('MAKE THE SECOND JUMP','Add five again','102 + 5 = 107',
 'Add five again to reach one hundred seven.'),
 ('MAKE THE THIRD JUMP','Count jumps, not the starting point','107 + 5 = 112',
 'A third jump of five lands on one hundred twelve. The starting point is not a jump.'),
 ('CHECK THE PATTERN','The gap stays five at every step','97 → 102 → 107 → 112',
 'Every gap is five. Starting at ninety-seven gives endings of seven and two, so counting by fives does not always end in zero or five.')],g(6,1),'97+3*5','112')

add('order-largest-with-ties','Find the largest amount and include every tie',
 'Boxes A, B, C, D hold counters.\nA: 5 hundreds 3 tens; B: 530\nC: 400 + 120; D: 5 hundreds 1 ten\nWhich boxes have the most?','A and B;530 each',
 'Four boxes hold counters. Write each amount as a number, then find every box with the largest total.',[
 ('CONVERT THE AMOUNTS','Use the same number form for all boxes','A: 500 + 30 = 530; B: 530\nC: 400 + 120 = 520; D: 500 + 10 = 510',
 'A has five hundred thirty, and B also has five hundred thirty. C has five hundred twenty, and D has five hundred ten.'),
 ('COMPARE FROM THE LEFT','The hundreds match, so compare tens','530 > 520 > 510',
 'The hundreds digits match. Compare tens: three tens are greater than two tens or one ten.'),
 ('INCLUDE BOTH MAXIMUMS','Equal amounts tie for the largest','A = B = 530',
 'A and B both have the largest amount, five hundred thirty. Neither has more than the other.'),
 ('SELECT EVERY TIED BOX','A question can have more than one answer','Most counters: A and B',
 'Select both A and B. Check every box so that you do not miss an equal largest amount.')],g('5HW',4),'500+30','530',[('400+120','520'),('500+10','510')])
add('place-four-digit-expanded-small','Expand and rebuild a four-digit number',
 'Write 4716 in expanded form.\nWhat value belongs to each digit?','4000 + 700 + 10 + 6',
 'Write four thousand seven hundred sixteen in expanded form. What value belongs to each digit?',[
 ('NAME THE PLACES','Start with the largest place','Thousands | Hundreds | Tens | Ones\n4 | 7 | 1 | 6',
 'The places are thousands, hundreds, tens, and ones. The digits are four, seven, one, six.'),
 ('FIND THE VALUES','Multiply each digit by its place unit','4 thousands = 4000; 7 hundreds = 700\n1 ten = 10; 6 ones = 6',
 'Four thousands are four thousand. Seven hundreds are seven hundred. One ten is ten, and six ones are six.'),
 ('WRITE THE EXPANSION','Add all four place values','4716 = 4000 + 700 + 10 + 6',
 'Write the four values as a sum: four thousand plus seven hundred plus ten plus six.'),
 ('REBUILD THE NUMBER','Missing parts must keep their place value','4000 + 700 + 10 + 6 = 4716',
 'Adding the parts gives four thousand seven hundred sixteen again. If a part is missing, use the digit and its place to restore it.')],g('3HW',2),'4000+700+10+6','4716')

def draw_pairs(s,d,scene,p):
 if scene==4:return draw_card(s,d,scene,p)
 d.rounded_rectangle((145,360,1775,850),radius=35,fill='white')
 for row,n in enumerate([12,13]):
  y=480+row*210
  v.text(d,(225,y),f'{"P" if row==0 else "Q"}: {n}',42,v.INK,True)
  for i in range(n):
   x=510+(i//2)*165+(i%2)*53
   d.ellipse((x-19,y-19,x+19,y+19),fill=v.TEAL)
  if scene in [1,2] and row==0 or scene==3 and row==1:
   for pair in range(6):
    x=510+pair*165;d.rounded_rectangle((x-33,y-35,x+86,y+35),radius=15,outline=v.INK,width=3)
  if row==1 and scene==3:v.text(d,(1580,y+50),'1 left',30,v.INK,True,anchor='mm')
 v.centered(d,797,['Which group can be paired with none left over?','P makes six complete pairs.','No leftover means even.','Q has one counter left over.'][scene],38,v.INK,True)

def lessons(doc):
 batch=make_lessons(SPECS,doc)
 s=next(s for s in SPECS if s['video_id']=='parity-pair-object-groups')
 v.DRAW[s['video_id']]=lambda d,scene,p:draw_pairs(s,d,scene,p)
 return batch
