"""Multiplication by splitting and place-value scaling, with checked examples."""
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons,draw_card
import generate_sample_videos as video
SPECS=[
authored('multiply-two-digit-single-distribute','Multiply a two-digit number by splitting tens and ones',
 'Find 54 × 6 using the distributive property.', '324',
 'Find fifty-four times six using the distributive property. Split fifty-four into tens and ones.',[
 ('SPLIT','Fifty-four is fifty plus four','54 × 6 = (50 + 4) × 6',
 'Fifty-four is fifty plus four. Both parts must be multiplied by six.'),
 ('TENS PRODUCT','Multiply fifty by six','50 × 6 = 300',
 'Five tens times six is thirty tens, or three hundred.'),
 ('ONES PRODUCT','Multiply four by six','4 × 6 = 24',
 'Four ones times six gives twenty-four ones.'),
 ('ADD THE PARTS','Combine the two partial products','300 + 24 = 324\n54 × 6 = 324',
 'Add three hundred and twenty-four to get three hundred twenty-four. Distribution means multiplying each part, then adding the results.')],
 g(3,2,4,8),equalities=[('54*6','324'),('50*6','300'),('4*6','24'),('300+24','324')]),
authored('multiply-whole-ten-hundred-thousand','Multiply whole numbers by ten, one hundred and one thousand',
 'Find 47 × 10, 47 × 100 and 47 × 1000.', '470; 4700; 47000',
 'Find forty-seven times ten, times one hundred, and times one thousand. Watch the place values.',[
 ('TIMES TEN','Each digit moves one place to the left','47 × 10 = 470',
 'Multiplying by ten moves each digit one place left on a place-value chart. Forty-seven becomes four hundred seventy.'),
 ('TIMES ONE HUNDRED','One hundred is ten times ten','47 × 100 = 47 × 10 × 10 = 4700',
 'One hundred is ten times ten, so move each digit two places left. The result is four thousand seven hundred.'),
 ('TIMES ONE THOUSAND','One thousand is ten times ten times ten','47 × 1000 = 47000',
 'For one thousand, move each digit three places left. Zeros hold the empty places. The product is forty-seven thousand.'),
 ('CHECK THE SCALE','Division reverses the place-value change','470 ÷ 10 = 47\n4700 ÷ 100 = 47\n47000 ÷ 1000 = 47',
 'Divide each answer by the same factor to recover forty-seven. The digits keep their order while their place values increase.')],
 g(4,3,2,1),equalities=[('47*10','470'),('47*100','4700'),('47*1000','47000')]),
authored('multiply-single-digit-place-units','Multiply a single digit by tens, hundreds or thousands',
 'Find 7 × 400. Then find 7 × 40 and 7 × 4000.', '2800; 280; 28000',
 'Find seven times four hundred. Then use the same fact for seven times forty and seven times four thousand.',[
 ('COUNT THE HUNDREDS','Four hundred means four groups of one hundred','7 × 400 = 7 × 4 hundreds',
 'Four hundred is four hundreds. Seven copies of four hundreds means seven times four hundreds.'),
 ('MULTIPLY THE COUNTS','Seven times four is twenty-eight','7 × 4 = 28\n28 hundreds = 2800',
 'Seven times four is twenty-eight. Twenty-eight hundreds is two thousand eight hundred.'),
 ('CHANGE THE UNIT','Use the same basic fact with tens or thousands','7 × 40 = 28 tens = 280\n7 × 4000 = 28 thousands = 28000',
 'For forty, the unit is tens, giving two hundred eighty. For four thousand, the unit is thousands, giving twenty-eight thousand.'),
 ('CHECK','Keep the place-value unit attached to the count','2800 ÷ 7 = 400',
 'Check that two thousand eight hundred divided by seven gives four hundred. Multiply the small counts, then restore their place-value unit.')],
 g(3,7,2,4),equalities=[('7*400','2800'),('7*40','280'),('7*4000','28000'),('2800/7','400')]),
authored('multiply-tens-equal-groups','Multiply tens by tens to count equal groups',
 'A hall has 20 rows with 80 seats in each row.\nHow many seats are there?', '1600 seats',
 'A hall has twenty rows with eighty seats in each row. How many seats are there altogether?',[
 ('MULTIPLY EQUAL GROUPS','Rows times seats in each row gives total seats','20 × 80',
 'Each row has the same number of seats, so multiply the number of rows by the seats in each row.'),
 ('SPLIT THE TENS','Twenty is two tens; eighty is eight tens','20 × 80 = (2 × 10)(8 × 10)',
 'Write twenty as two times ten and eighty as eight times ten.'),
 ('REGROUP','Multiply the counts and the place-value units','(2 × 8)(10 × 10) = 16 × 100',
 'Two times eight gives sixteen. Ten times ten gives one hundred. Tens times tens produce hundreds.'),
 ('ANSWER AND CHECK','There are sixteen hundreds of seats','16 × 100 = 1600 seats\n1600 ÷ 20 = 80 seats per row',
 'Sixteen hundreds is sixteen hundred seats. Dividing by twenty rows returns eighty seats per row, checking the total.')],
 g(4,4,'1Rev',5),equalities=[('20*80','1600'),('(2*8)*(10*10)','1600'),('1600/20','80')]),
authored('multiply-large-trailing-zeros','Multiply large place-value multiples',
 'Find 700 × 6000.', '4200000',
 'Find seven hundred times six thousand. Separate the basic multiplication fact from the place values.',[
 ('FACTOR BY PLACE','Seven hundred is seven hundreds; six thousand is six thousands','700 × 6000 = (7 × 100)(6 × 1000)',
 'Write seven hundred as seven times one hundred, and six thousand as six times one thousand.'),
 ('REGROUP','Pair the small counts and the place-value factors','(7 × 6)(100 × 1000)',
 'Regroup the factors. Multiply seven by six, and one hundred by one thousand.'),
 ('CALCULATE','Forty-two groups of one hundred thousand','7 × 6 = 42; 100 × 1000 = 100000\n42 × 100000 = 4200000',
 'Seven times six is forty-two. One hundred times one thousand is one hundred thousand. Their product is four million two hundred thousand.'),
 ('CHECK','Divide by one original factor','4200000 ÷ 6000 = 700',
 'Divide four million two hundred thousand by six thousand to recover seven hundred. The zeros come from place-value factors, not from changing the basic fact.')],
 g(5,5,1,4),equalities=[('700*6000','4200000'),('100*1000','100000'),('4200000/6000','700')]),
authored('multiply-basic-equal-groups','Understand a multiplication fact as equal groups',
 'Find 4 × 8.', '32',
 'Find four times eight. Think of four equal groups with eight in each group.',[
 ('MAKE GROUPS','Four groups, eight dots in each','4 groups × 8 in each group',
 'Draw four groups. Each group contains eight dots.'),
 ('ADD EQUAL AMOUNTS','Add eight once for each group','8 + 8 + 8 + 8',
 'The matching addition is eight plus eight plus eight plus eight.'),
 ('COUNT THE TOTAL','Count by eights four times','8 → 16 → 24 → 32',
 'Count by eights: eight, sixteen, twenty-four, thirty-two. Four groups give thirty-two altogether.'),
 ('ANSWER AND CHECK','Multiplication is a shorter way to write equal-group addition','4 × 8 = 32\n32 ÷ 4 = 8',
 'Four times eight is thirty-two. Sharing thirty-two into four equal groups gives eight in each group, checking the multiplication.')],
 ('worksheets/enrichment/counting-and-probability 1/U1counting-and-classification/E-CP1U1W1.csv','1'),
 equalities=[('4*8','32'),('8+8+8+8','32'),('32/4','8')]),
]
def draw_groups(d,scene,p):
 if scene!=1:return draw_card(SPECS[-1],d,scene,p)
 for row in range(4):
  y=435+105*row
  d.rounded_rectangle((460,y-30,1470,y+30),radius=20,fill='white')
  for col in range(8):
   x=555+115*col;d.ellipse((x-15,y-15,x+15,y+15),fill=video.TEAL)

def lessons(doc):
 result=make_lessons(SPECS,doc)
 video.DRAW['multiply-basic-equal-groups']=draw_groups
 return result
