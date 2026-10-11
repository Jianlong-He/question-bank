"""Decimal division by place units and equivalent scaled quotients."""
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons
SPECS=[
authored('divide-decimal-ten-hundred','Divide a decimal by ten or one hundred',
 'Find 6.4 ÷ 10 and 6.4 ÷ 100.', '0.64; 0.064',
 'Find six point four divided by ten and six point four divided by one hundred.',[
 ('DIVIDE BY TEN','Each digit moves one place to the right on the place-value chart','6.4 ÷ 10 = 0.64',
 'Dividing by ten makes each digit worth one tenth as much. Six ones becomes six tenths, and four tenths becomes four hundredths.'),
 ('DIVIDE BY ONE HUNDRED','One hundred is ten times ten','6.4 ÷ 100 = 6.4 ÷ 10 ÷ 10',
 'Dividing by one hundred is the same as dividing by ten twice.'),
 ('SECOND PLACE SHIFT','Use zero to hold the empty tenths place','6.4 → 0.64 → 0.064',
 'The first division gives zero point six four. The second gives zero point zero six four. Keep the zero in the tenths place.'),
 ('CHECK','Multiply each result by its divisor','0.64 × 10 = 6.4\n0.064 × 100 = 6.4',
 'Multiply each answer by its divisor to return to six point four. Division by ten or one hundred makes a positive number smaller.')],
 g(5,1,'3Rev',4),equalities=[('6.4/10','0.64'),('6.4/100','0.064'),('0.064*100','6.4')]),
authored('divide-decimal-by-whole-place','Divide a decimal by sharing its place-value units',
 'Find 0.756 ÷ 3.', '0.252',
 'Find zero point seven five six divided by three. Write the decimal as a count of thousandths.',[
 ('NAME THE UNIT','Seven hundred fifty-six thousandths is zero point seven five six','0.756 = 756/1000\n756 thousandths ÷ 3',
 'Zero point seven five six is seven hundred fifty-six thousandths. Divide that count by three, keeping the unit thousandths.'),
 ('DIVIDE THE COUNT','Split into two convenient multiples of three','756 ÷ 3 = (750 + 6) ÷ 3\n= 250 + 2 = 252',
 'Split seven hundred fifty-six into seven hundred fifty and six. Dividing each by three gives two hundred fifty and two, or two hundred fifty-two.'),
 ('RESTORE THE UNIT','The quotient is still a number of thousandths','252 thousandths = 252/1000 = 0.252',
 'The result is two hundred fifty-two thousandths, or zero point two five two. Keep all three decimal places here.'),
 ('CHECK','Multiply by the original whole-number divisor','0.252 × 3 = 0.756',
 'Multiply zero point two five two by three to recover the original decimal. The same method works with tenths or hundredths: divide the count and keep its unit.')],
 g(5,9,2,1),equalities=[('0.756/3','0.252'),('750/3+6/3','252'),('252/1000','0.252'),('0.252*3','0.756')]),
authored('divide-unit-decimal-reciprocal','Divide by one tenth, one hundredth or one thousandth',
 'Find 2.7 ÷ 0.1, 2.7 ÷ 0.01 and 2.7 ÷ 0.001.', '27; 270; 2700',
 'Divide two point seven by one tenth, one hundredth, and one thousandth. We are counting how many small units fit.',[
 ('COUNT TENTHS','One whole contains ten tenths','2.7 ÷ 0.1 = 2.7 × 10 = 27',
 'One whole contains ten tenths. Two point seven contains twenty-seven tenths, so dividing by one tenth is multiplying by ten.'),
 ('COUNT HUNDREDTHS','One whole contains one hundred hundredths','2.7 ÷ 0.01 = 2.7 × 100 = 270',
 'For hundredths, there are one hundred units per whole. Multiply by one hundred to get two hundred seventy.'),
 ('COUNT THOUSANDTHS','One whole contains one thousand thousandths','2.7 ÷ 0.001 = 2.7 × 1000 = 2700',
 'For thousandths, multiply by one thousand. There are two thousand seven hundred thousandths in two point seven.'),
 ('CHECK THE COUNT','Number of units times the size of one unit gives the total','27 × 0.1 = 2.7\n270 × 0.01 = 2.7\n2700 × 0.001 = 2.7',
 'Multiply each count by its unit size to check. A smaller positive divisor gives a larger count of groups.')],
 g(5,9,3,6),equalities=[('2.7/0.1','27'),('2.7/0.01','270'),('2.7/0.001','2700')]),
authored('divide-small-decimal-scale','Choose a scale that makes a decimal divisor a whole number',
 'Find 4.32 ÷ 0.12 and 1.44 ÷ 0.004.', '36; 360',
 'Find four point three two divided by zero point one two, and one point four four divided by zero point zero zero four.',[
 ('FIRST SCALE','Two decimal places in the divisor: multiply both by one hundred','4.32 ÷ 0.12 = 432 ÷ 12',
 'The first divisor has two decimal places. Multiply both numbers by one hundred. Scaling both equally keeps the quotient unchanged.'),
 ('FIRST QUOTIENT','Use convenient multiples of twelve','432 ÷ 12 = (360 + 72) ÷ 12\n= 30 + 6 = 36',
 'Divide four hundred thirty-two by twelve. Three hundred sixty gives thirty groups, and seventy-two gives six more. The quotient is thirty-six.'),
 ('SECOND SCALE','Three decimal places in the divisor: multiply both by one thousand','1.44 ÷ 0.004 = 1440 ÷ 4 = 360',
 'The second divisor needs a factor of one thousand. Scale both numbers, giving fourteen hundred forty divided by four, or three hundred sixty.'),
 ('CHECK BOTH','Multiply by the original decimal divisors','36 × 0.12 = 4.32\n360 × 0.004 = 1.44',
 'Multiply each quotient by its original divisor to check. Choose ten, one hundred, or one thousand according to how many places the divisor needs.')],
 g(5,9,3,9),equalities=[('4.32/0.12','36'),('432/12','36'),('1.44/0.004','360'),('1440/4','360'),('36*0.12','4.32'),('360*0.004','1.44')]),
]
def lessons(doc):return make_lessons(SPECS,doc)
