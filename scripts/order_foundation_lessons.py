"""Fresh comparison, ordering and early-number examples."""
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons,draw_card
import generate_sample_videos as v
SPECS=[
authored('order-whole-threshold','Find numbers greater than or less than a target',
 'Which of 9, 12, 16 and 20 are greater than 12?\nWhich are less than 12?', 'Greater: 16, 20; less: 9',
 'Look at nine, twelve, sixteen, and twenty. Which numbers are greater than twelve, and which are less?',[
 ('USE NUMBER ORDER','Numbers increase as we move to the right','9 < 12 < 16 < 20',
 'Put the numbers in counting order. Numbers farther right are greater.'),
 ('GREATER THAN','Choose numbers to the right of twelve','16 > 12 and 20 > 12',
 'Sixteen and twenty are to the right of twelve. Both are greater than twelve.'),
 ('LESS THAN','Choose numbers to the left of twelve','9 < 12',
 'Nine is to the left of twelve, so nine is less than twelve.'),
 ('EQUAL IS DIFFERENT','Twelve is neither greater nor less than itself','12 = 12\nGreater: 16, 20; less: 9',
 'Twelve equals twelve. Do not include it when a question says strictly greater than or less than.')],
 g(1,1,5,1),equalities=[('12-9','3'),('16-12','4'),('20-12','8')]),
authored('order-add-then-compare','Add first, then compare with a target',
 'Is 4 + 5 greater than 9?', 'No; it equals 9',
 'Is four plus five greater than nine? First find the sum.',[
 ('ADD','Count five more after four','5, 6, 7, 8, 9',
 'Start at four and count five more: five, six, seven, eight, nine.'),
 ('REPLACE THE SUM','Four plus five makes nine','4 + 5 = 9',
 'The sum is nine. Replace four plus five with nine.'),
 ('COMPARE','The two values are equal','9 = 9',
 'Compare nine with nine. Neither is greater because they are equal.'),
 ('ANSWER THE QUESTION','Greater than does not include equal to','No: 4 + 5 is equal to 9.',
 'The answer is no. Adding gives a number equal to the target, not greater than it.')],
 g(1,1,5,8),equalities=[('4+5','9')]),
authored('order-skip-past-limit','Skip-count until you pass a limit',
 'Count by twos from 13.\nStop at the first number greater than 24.', '25',
 'Count by twos from thirteen. Stop at the first number greater than twenty-four.',[
 ('CHOOSE THE STEP','Add two each time','13 → 15 → 17',
 'Start at thirteen. Add two to get fifteen, then add two again to get seventeen.'),
 ('KEEP COUNTING','Use the same step','17 → 19 → 21 → 23',
 'Keep adding two: nineteen, twenty-one, twenty-three.'),
 ('CHECK THE LIMIT','Twenty-three has not passed twenty-four','23 < 24\n23 + 2 = 25',
 'Twenty-three is still below twenty-four. One more step takes us to twenty-five.'),
 ('STOP AT THE FIRST MATCH','Twenty-five is greater than twenty-four','25 > 24\nLast number: 25',
 'Twenty-five is greater than twenty-four, so stop there. It is the first number in this counting pattern past the limit.')],
 g(1,1,7,8),equalities=[('13+2*6','25'),('23+2','25')]),
authored('order-complete-ten','Find how many more make ten',
 'How many must be added to 6 to make 10?', '4',
 'How many must we add to six to make ten?',[
 ('SHOW THE START','Six of ten spaces are filled','6 + __ = 10',
 'Imagine a frame with ten spaces. Six spaces are filled.'),
 ('COUNT EMPTY SPACES','Four spaces still need filling','7, 8, 9, 10: four more',
 'Count the empty spaces, or count on from six: seven, eight, nine, ten. That takes four counts.'),
 ('WRITE THE MISSING NUMBER','Six and four make ten','6 + 4 = 10',
 'The missing number is four. Six plus four equals ten.'),
 ('CHECK WITH SUBTRACTION','Subtract the amount already there','10 − 6 = 4',
 'Check by subtracting six from ten. Four spaces remain, so four is the amount to add.')],
 g(1,2,3,5),equalities=[('6+4','10'),('10-6','4')]),
authored('order-ten-less','Find ten less using place value',
 'What number is ten less than 74?', '64',
 'What number is ten less than seventy-four?',[
 ('READ THE PLACES','Seventy-four has seven tens and four ones','74 = 7 tens + 4 ones',
 'Seventy-four has seven tens and four ones.'),
 ('REMOVE ONE TEN','Ten less means one fewer group of ten','7 tens − 1 ten = 6 tens',
 'Take away one ten. Seven tens becomes six tens.'),
 ('KEEP THE ONES','The four ones have not changed','6 tens + 4 ones = 64',
 'Keep the four ones. Six tens and four ones make sixty-four.'),
 ('CHECK','Add the ten back','74 − 10 = 64\n64 + 10 = 74',
 'Sixty-four is ten less than seventy-four. Add ten back to check that we return to seventy-four.')],
 g(1,2,9,3),equalities=[('74-10','64'),('64+10','74')]),
authored('order-arrange-digits','Arrange digits to make the largest or smallest number',
 'Use 6, 1 and 4 once each to make the largest and smallest numbers.\nThen repeat with 6, 0 and 4.', '641 and 146; 640 and 406',
 'Make the largest and smallest numbers using six, one, and four once each. Then try six, zero, and four.',[
 ('MAKE THE LARGEST','Put larger digits in higher-value places','6, 4, 1 → 641',
 'For the largest number, put the largest digit first, then the next largest. Six hundred forty-one is largest.'),
 ('MAKE THE SMALLEST','Put smaller digits in higher-value places','1, 4, 6 → 146',
 'For the smallest number, reverse that order. One hundred forty-six is smallest.'),
 ('HANDLE ZERO','A three-digit number cannot start with zero','Largest: 640\nSmallest: 406, not 046',
 'With zero, the largest is six hundred forty. The smallest must start with the smallest nonzero digit, four. Then put zero before six to get four hundred six.'),
 ('CHECK THE DIGITS','Use every digit exactly once','641 and 146 use 6, 1, 4.\n640 and 406 use 6, 0, 4.',
 'Check that no digit was repeated or lost. The same place-value rule works with longer numbers.')],
 g(2,2,1,8),equalities=[('600+40+1','641'),('100+40+6','146'),('400+6','406')]),
authored('order-fraction-over-one','Compare a fraction with denominator one to one whole',
 'Is 9/1 less than, equal to, or greater than 1?', 'Greater than 1',
 'Is nine over one less than, equal to, or greater than one?',[
 ('READ THE DENOMINATOR','Each part is one whole','1/1 = 1 whole',
 'A denominator of one means each part is a whole.'),
 ('COUNT THE WHOLES','The numerator counts nine of those parts','9/1 = 9 wholes = 9',
 'The numerator says we have nine whole parts. Nine over one equals nine.'),
 ('COMPARE','Nine wholes is more than one whole','9 > 1',
 'Nine wholes is more than one whole, so nine is greater than one.'),
 ('WRITE THE SYMBOL','The wide end faces the greater value','9/1 > 1',
 'Write the greater-than symbol, with its wide end toward nine over one.')],
 g(3,5,4,3),equalities=[('9/1','9')]),
authored('order-decimals-place','Order decimals using matching place values',
 'Order 4.307, 4.37 and 4.037 from least to greatest.\nThen write them from greatest to least.', '4.037, 4.307, 4.37; reverse for greatest to least',
 'Order four point three zero seven, four point three seven, and four point zero three seven in both directions.',[
 ('MATCH PLACES','A trailing zero does not change the value','4.307   4.370   4.037',
 'Write the same number of decimal places. Four point three seven becomes four point three seven zero.'),
 ('COMPARE LEFT TO RIGHT','Whole parts match; compare tenths first','4.037 is smallest: its tenths digit is 0.',
 'The whole parts are all four. Compare tenths. The number with zero tenths is the smallest.'),
 ('BREAK THE TIE','For the remaining pair, compare hundredths','4.307 < 4.370 because 0 < 7 in hundredths.',
 'The other two have three tenths. Compare their hundredths: zero is less than seven, so four point three zero seven comes next.'),
 ('READ BOTH DIRECTIONS','Reverse the order for greatest to least','Least first: 4.037, 4.307, 4.37\nGreatest first: 4.37, 4.307, 4.037',
 'Write the numbers in increasing order, then reverse that list for decreasing order. Use place values, not the number of written digits.')],
 g(5,1,4,5),equalities=[('4.37','4.370')]),
authored('order-signed-integers','Order negative numbers, zero and positive numbers',
 'Order −45, 62, 0, 18, −9, 4 and −2 from least to greatest.', '−45, −9, −2, 0, 4, 18, 62',
 'Order negative forty-five, sixty-two, zero, eighteen, negative nine, four, and negative two from least to greatest.',[
 ('SORT BY SIGN','Negatives come before zero, then positives','Negative: −45, −9, −2\nZero: 0\nPositive: 62, 18, 4',
 'Separate the negative numbers, zero, and positive numbers. Every negative number is less than zero.'),
 ('ORDER THE NEGATIVES','Farther left on a number line means smaller','−45 < −9 < −2',
 'Among negatives, the number farther from zero is smaller. Negative forty-five comes before negative nine, then negative two.'),
 ('ORDER THE POSITIVES','Use ordinary counting order','4 < 18 < 62',
 'For the positive numbers, four is smallest, then eighteen, then sixty-two.'),
 ('JOIN THE GROUPS','Read from smallest to greatest','−45 < −9 < −2 < 0 < 4 < 18 < 62',
 'Join the ordered negatives, zero, and ordered positives. Check that every step moves right on the number line.')],
 g(6,5,1,7),equalities=[('-45+36','-9'),('-9+7','-2')]),
]
def draw_foundation(spec,d,scene,p):
 if spec['video_id']=='order-whole-threshold' and scene==1:
  d.line((350,620,1570,620),fill=v.INK,width=5)
  for n in range(8,22):
   x=350+(n-8)*90
   d.line((x,605,x,635),fill=v.INK,width=3)
   v.text(d,(x-18,662),str(n),30,v.MUTED)
   if n in [9,12,16,20]:d.ellipse((x-12,608,x+12,632),fill=v.TEAL)
  v.centered(d,425,'9 < 12 < 16 < 20',66,v.TEAL,True)
 elif spec['video_id']=='order-complete-ten' and scene in [1,2]:
  for i in range(10):
   x=575+(i%5)*155;y=420+(i//5)*155
   d.rectangle((x,y,x+140,y+140),outline=v.INK,width=4)
   if i<6:d.ellipse((x+25,y+25,x+115,y+115),fill=v.TEAL)
   elif scene==2:d.ellipse((x+25,y+25,x+115,y+115),outline=v.TEAL,width=6)
  v.centered(d,810,'6 filled + 4 empty = 10 spaces',48,v.TEAL,True)
 else:draw_card(spec,d,scene,p)
def lessons(doc):
 L=make_lessons(SPECS,doc)
 for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:draw_foundation(s,d,scene,p)
 return L
