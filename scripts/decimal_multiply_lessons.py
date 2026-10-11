"""Decimal multiplication through place units and powers of ten."""
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons
SPECS=[
authored('multiply-decimal-ten-hundred','Multiply decimals by ten and one hundred',
 'Find 4.08 × 10 and 0.00037 × 100.', '40.8; 0.037',
 'Find four point zero eight times ten, and zero point zero zero zero three seven times one hundred.',[
 ('TIMES TEN','Every digit moves one place left on the place-value chart','4.08 × 10 = 40.8',
 'Multiplying by ten moves every digit to a place worth ten times as much. Four point zero eight becomes forty point eight.'),
 ('TIMES ONE HUNDRED','Multiply by ten twice','0.00037 × 10 = 0.0037\n0.0037 × 10 = 0.037',
 'For one hundred, multiply by ten twice. The first step gives zero point zero zero three seven. The second gives zero point zero three seven.'),
 ('KEEP NEEDED ZEROS','The result can still be less than one','0.00037 × 100 = 0.037\n0.037 is thirty-seven thousandths.',
 'The result is thirty-seven thousandths. Keep the zero in the tenths place. Removing it would change the value.'),
 ('CHECK BY DIVIDING','Reverse the scale change','40.8 ÷ 10 = 4.08\n0.037 ÷ 100 = 0.00037',
 'Divide by the original factor to check each answer. Multiplication increases each digit’s place value; it does not simply add zeros to the end of a decimal.')],
 g(5,1,'2Rev',4),equalities=[('4.08*10','40.8'),('0.00037*100','0.037'),('0.00037*10','0.0037'),('0.037/100','0.00037')]),
authored('multiply-decimal-by-whole-place','Multiply a decimal by a whole number using place units',
 'Find 6 × 0.245.', '1.47',
 'Find six times zero point two four five. Think of the decimal as a number of thousandths.',[
 ('NAME THE UNIT','Zero point two four five is two hundred forty-five thousandths','0.245 = 245/1000\n6 × 245 thousandths',
 'Zero point two four five is two hundred forty-five thousandths. Multiply the count by six while keeping the unit thousandths.'),
 ('MULTIPLY THE COUNT','Split two hundred forty-five by place','6 × 245 = 1200 + 240 + 30 = 1470',
 'Six times two hundred is twelve hundred. Six times forty is two hundred forty. Six times five is thirty. Add them to get fourteen hundred seventy.'),
 ('RESTORE THE UNIT','One thousand thousandths makes one whole','1470 thousandths = 1470/1000 = 1.470',
 'Fourteen hundred seventy thousandths is one point four seven zero. The unit determines the decimal position.'),
 ('SIMPLIFY AND CHECK','A trailing decimal zero does not change the value','1.470 = 1.47\n1.47 ÷ 6 = 0.245',
 'Remove the unnecessary trailing zero to write one point four seven. Dividing by six returns zero point two four five, checking the product.')],
 g(5,8,1,6),equalities=[('6*0.245','1.47'),('6*245','1470'),('1200+240+30','1470'),('1470/1000','1.470'),('1.47/6','0.245')]),
]
def lessons(doc):return make_lessons(SPECS,doc)
