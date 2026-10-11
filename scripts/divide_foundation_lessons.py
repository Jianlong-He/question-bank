"""Equal groups, division by place, and single-digit long-division methods."""
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons,draw_card
import generate_sample_videos as video
SPECS=[
authored('divide-count-equal-groups','Find the number of equal groups',
 'Pack 24 counters into bags with 6 counters in each.\nHow many bags are needed?', '4 bags',
 'Pack twenty-four counters into bags with six counters in each. How many bags are needed?',[
 ('CHOOSE DIVISION','Divide the total by the size of each group','24 ÷ 6',
 'We know the total number of counters and how many go in each bag. Divide twenty-four by six to find the number of bags.'),
 ('MAKE EQUAL GROUPS','Each bag contains six counters','6 + 6 + 6 + 6 = 24',
 'Make groups of six. Four equal groups use all twenty-four counters.'),
 ('COUNT THE GROUPS','There are four groups, so there are four bags','24 ÷ 6 = 4 bags',
 'There are four bags. The answer counts bags, not counters in a bag.'),
 ('CHECK BY MULTIPLYING','Number of bags times counters in each returns the total','4 bags × 6 counters per bag = 24 counters',
 'Four bags times six counters in each is twenty-four counters. Every counter is packed, with none left over.')],
 g(2,1,2,9),equalities=[('24/6','4'),('6+6+6+6','24'),('4*6','24')]),
authored('divide-place-unit-multiples','Divide tens, hundreds and thousands by a single digit',
 'Find 4200 ÷ 7. Then find 420 ÷ 7 and 42000 ÷ 7.', '600; 60; 6000',
 'Find forty-two hundred divided by seven. Then use the same fact for four hundred twenty and forty-two thousand divided by seven.',[
 ('NAME THE UNIT','Forty-two hundred means forty-two groups of one hundred','4200 = 42 hundreds',
 'Four thousand two hundred can be written as forty-two hundreds. Keep track of the unit hundreds.'),
 ('DIVIDE THE COUNT','Forty-two divided by seven is six','42 hundreds ÷ 7 = 6 hundreds = 600',
 'Forty-two divided by seven is six, so forty-two hundreds divided by seven is six hundreds, or six hundred.'),
 ('CHANGE THE UNIT','The same division fact works with tens and thousands','420 ÷ 7 = 42 tens ÷ 7 = 60\n42000 ÷ 7 = 42 thousands ÷ 7 = 6000',
 'For four hundred twenty, divide forty-two tens to get six tens. For forty-two thousand, the result is six thousands.'),
 ('CHECK','The quotient times the divisor returns the dividend','600 × 7 = 4200',
 'Check that six hundred times seven is four thousand two hundred. Divide the count, then restore its place-value unit.')],
 g(4,5,2,1),equalities=[('4200/7','600'),('420/7','60'),('42000/7','6000'),('600*7','4200')]),
authored('divide-single-digit-long','Divide by a single digit using place values',
 'Share 732 counters equally among 3 tables.\nHow many counters does each table receive?', '244 counters',
 'Share seven hundred thirty-two counters equally among three tables. Divide seven hundred thirty-two by three.',[
 ('HUNDREDS','Divide, subtract, then regroup the remainder','7 hundreds ÷ 3 = 2 hundreds each\n7 − 6 = 1 hundred left',
 'Seven hundreds divided among three gives two hundreds each, using six hundreds. One hundred remains.'),
 ('TENS','Exchange the remaining hundred for ten tens','10 tens + 3 tens = 13 tens\n13 ÷ 3 = 4 tens each, 1 ten left',
 'Exchange the leftover hundred for ten tens. Add the original three tens to get thirteen tens. Give four tens to each table; one ten remains.'),
 ('ONES','Exchange the remaining ten for ten ones','10 ones + 2 ones = 12 ones\n12 ÷ 3 = 4 ones each',
 'Exchange the leftover ten for ten ones. Add the original two ones. Twelve divided by three gives four ones each, with nothing left.'),
 ('COMBINE AND CHECK','Read the quotient by place','2 hundreds + 4 tens + 4 ones = 244\n244 × 3 = 732',
 'Each table receives two hundred forty-four counters. Multiplying by three returns seven hundred thirty-two, checking the equal shares.')],
 g(4,5,4,5),equalities=[('732/3','244'),('7-6','1'),('13-3*4','1'),('12/3','4'),('244*3','732')]),
authored('divide-zero-in-quotient','Keep a zero when a quotient place has no full group',
 'Find 1632 ÷ 4.', '408',
 'Find one thousand six hundred thirty-two divided by four. Keep each quotient digit in its correct place.',[
 ('FIRST USABLE GROUP','One thousand is too small; use sixteen hundreds','16 hundreds ÷ 4 = 4 hundreds\n16 − 16 = 0 hundreds left',
 'One thousand cannot give a whole thousand to each group. Use sixteen hundreds instead. Dividing by four gives four hundreds each.'),
 ('ZERO TENS','Three tens cannot give one full ten to each group','3 tens ÷ 4: 0 tens each, 3 tens left\nQuotient so far: 4 hundreds, 0 tens',
 'The next place has three tens. That cannot give one full ten to each of four groups. Write zero in the tens place; do not skip it.'),
 ('ONES','Regroup the leftover tens and include the two ones','3 tens + 2 ones = 32 ones\n32 ÷ 4 = 8 ones each',
 'Regroup the three tens as thirty ones and add the original two. Thirty-two divided by four gives eight ones each.'),
 ('ANSWER AND CHECK','The zero keeps four in the hundreds place','1632 ÷ 4 = 408\n408 × 4 = 1632',
 'The quotient is four hundred eight. The zero holds the empty tens place. Multiplying by four checks the result.')],
 g(4,5,'2HW',5),equalities=[('1632/4','408'),('16/4','4'),('3*10+2','32'),('32/4','8'),('408*4','1632')]),
]
def draw_bags(d,scene,p):
 if scene!=2:return draw_card(SPECS[0],d,scene,p)
 for bag in range(4):
  x=220+390*bag
  d.rounded_rectangle((x,400,x+320,775),radius=35,fill='white',outline='#b4beba',width=3)
  for i in range(6):
   xx=x+100+(i%2)*120;yy=470+(i//2)*110
   d.ellipse((xx-20,yy-20,xx+20,yy+20),fill=video.TEAL)

def lessons(doc):
 result=make_lessons(SPECS,doc)
 video.DRAW['divide-count-equal-groups']=draw_bags
 return result
