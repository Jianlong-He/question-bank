"""Larger place values, decimal shifts, rounding constraints and last-two-digit sums."""
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons
ENR=('worksheets/enrichment/number-theory 1/U1modular-arithmetic/E-NT1U1W1HWa.csv','5')
SPECS=[
authored('place-large-number-chart','Build and read a place-value chart',
 'Fill a place-value chart for 6,405,827.\nThen rebuild the number from its place counts.',
 '6 millions, 4 hundred thousands, 0 ten thousands, 5 thousands, 8 hundreds, 2 tens, 7 ones',
 'Fill a place-value chart for six million, four hundred five thousand, eight hundred twenty-seven. Then rebuild the number from its place counts.',[
 ('START AT THE RIGHT','The last three digits give hundreds, tens and ones','827: 8 hundreds, 2 tens, 7 ones',
 'Start at the right. Seven is in ones, two is in tens, and eight is in hundreds.'),
 ('NEXT THREE PLACES','Keep the zero in the ten-thousands place','405: 4 hundred thousands\n0 ten thousands, 5 thousands',
 'The next group gives five thousands, zero ten thousands, and four hundred thousands. Keep the zero as a placeholder.'),
 ('MILLIONS','The remaining digit counts millions','6 millions = 6,000,000',
 'The remaining six counts millions.'),
 ('REBUILD AND CHECK','Match each count to its label, even in a different order','6,000,000 + 400,000 + 5,000\n+ 800 + 20 + 7 = 6,405,827',
 'Add the place values to rebuild the number. If the blanks are listed in a different order, match each label to its digit instead of copying digits from left to right.')],
 g(3,3,1,3),equalities=[('6000000+400000+5000+800+20+7','6405827')]),
authored('place-locate-digit-value','Find a digit position and its value',
 'What is the value of 4 in 6,405,827?\nWhich number has 7 hundreds: 9,752 or 5,792?',
 '400,000; both 9,752 and 5,792 have 7 hundreds',
 'What is the value of four in six million, four hundred five thousand, eight hundred twenty-seven? Which of these numbers has seven hundreds: nine thousand seven hundred fifty-two, or five thousand seven hundred ninety-two?',[
 ('COUNT FROM THE RIGHT','Name places starting with ones','ones, tens, hundreds\nthousands, ten thousands, hundred thousands\nthen millions',
 'Count places from the right: ones, tens, hundreds, thousands, ten thousands, hundred thousands, and millions.'),
 ('MULTIPLY BY THE UNIT','The digit is four; its place unit is one hundred thousand','4 × 100,000 = 400,000',
 'Four is in the hundred-thousands place. Its value is four times one hundred thousand, or four hundred thousand.'),
 ('CHECK EACH OPTION','The hundreds place is third from the right','9,752: hundreds digit = 7\n5,792: hundreds digit = 7',
 'For the second question, inspect the third digit from the right in each number. Both have seven in that position.'),
 ('DISTINGUISH DIGIT AND VALUE','Check every option when more than one can work','Digit 7 in hundreds has value 700\nBoth numbers qualify',
 'Both numbers qualify. A digit tells the count; its place determines the value. Seven hundreds has value seven hundred.')],
 g(3,3,1,6),equalities=[('4*100000','400000'),('(9752-52)/100%10','7'),('(5792-92)/100%10','7')]),
authored('place-times-divide-ten-shifts','Track a digit when multiplying or dividing by ten',
 'Track the digit 6 in 268 × 10.\nTrack the digit 8 in 8,430 ÷ 10.', '6 moves from tens to hundreds; 8 moves from thousands to hundreds',
 'Track the digit six when two hundred sixty-eight is multiplied by ten. Then track eight when eight thousand four hundred thirty is divided by ten.',[
 ('MULTIPLY','Each digit moves to the next larger place','268 × 10 = 2,680',
 'Multiplying by ten makes each digit worth ten times as much. Two hundred sixty-eight becomes two thousand six hundred eighty.'),
 ('TRACK SIX','Its value changes from sixty to six hundred','6: tens → hundreds\n60 × 10 = 600',
 'The six moves from tens to hundreds. Its value changes from sixty to six hundred.'),
 ('DIVIDE','Each digit moves to the next smaller place','8,430 ÷ 10 = 843',
 'Dividing by ten makes each digit worth one tenth as much. Eight thousand four hundred thirty becomes eight hundred forty-three.'),
 ('TRACK EIGHT','Its value changes from eight thousand to eight hundred','8: thousands → hundreds\n8,000 ÷ 10 = 800',
 'The eight moves from thousands to hundreds. On a place-value chart, multiplication moves digits one place left, and division moves them one place right.')],
 g(4,1,4,3),equalities=[('268*10','2680'),('8430/10','843'),('60*10','600'),('8000/10','800')]),
authored('place-unit-count-sharing','Convert tens to individual objects before sharing',
 'A library has 2,463 tens of cards.\nIt shares them equally among 10 schools.\nHow many individual cards does each school receive?', '2,463 cards per school',
 'A library has two thousand four hundred sixty-three tens of cards. It shares them equally among ten schools. How many individual cards does each school receive?',[
 ('IDENTIFY THE UNIT','The given count is a count of tens','1 ten = 10 individual cards',
 'The starting count is in tens. Each ten means ten individual cards.'),
 ('CONVERT','Multiply the count by ten','2,463 × 10 = 24,630 cards',
 'Multiply by ten. The library has twenty-four thousand six hundred thirty individual cards.'),
 ('SHARE','Divide the individual-card total by ten schools','24,630 ÷ 10 = 2,463',
 'Now divide the total by ten schools. Each school receives two thousand four hundred sixty-three cards.'),
 ('CHECK THE UNIT','The same digits now count individual cards per school','2,463 cards × 10 schools = 24,630 cards',
 'Multiply back to check. The multiplication and division by ten cancel numerically, but the answer unit is individual cards per school.')],
 g(4,1,'4HW',3),equalities=[('2463*10','24630'),('24630/10','2463')]),
authored('place-divide-large-unit-count','Divide a large place-unit count and name the resulting digits',
 'Divide 3,587 ten-thousands by 10.\nName the digits from millions through ones.', '3,587,000; digits 3, 5, 8, 7, 0, 0, 0',
 'Divide three thousand five hundred eighty-seven ten-thousands by ten. Then name the digits from millions through ones.',[
 ('CONVERT THE UNIT','Each ten-thousand has value ten thousand','3,587 × 10,000 = 35,870,000',
 'First convert the unit count to a number. Multiply by ten thousand to get thirty-five million, eight hundred seventy thousand.'),
 ('DIVIDE','Move each digit one place to the right','35,870,000 ÷ 10 = 3,587,000',
 'Divide by ten. Each digit moves one place right, giving three million, five hundred eighty-seven thousand.'),
 ('READ THE LARGER PLACES','Read labels and digits together','Millions: 3; hundred thousands: 5\nTen thousands: 8; thousands: 7',
 'The millions digit is three, hundred thousands is five, ten thousands is eight, and thousands is seven.'),
 ('KEEP EMPTY PLACES','Hundreds, tens and ones are all zero','Hundreds: 0; tens: 0; ones: 0\n3, 5, 8, 7, 0, 0, 0',
 'The hundreds, tens and ones digits are all zero. Include every requested place, even when its digit is zero.')],
 g(4,1,'4HW',5),equalities=[('3587*10000','35870000'),('35870000/10','3587000')]),
authored('place-rounding-missing-digit','Find all missing digits that give a requested rounding result',
 'Which digits make 72_6 round to 7,200 to the nearest hundred?\nWhich digits make 83_2 round to 8,400?', 'First: 0, 1, 2, 3, 4. Second: 5, 6, 7, 8, 9.',
 'Which missing tens digits make seventy-two blank six round to seven thousand two hundred to the nearest hundred? Which make eighty-three blank two round to eight thousand four hundred?',[
 ('FIND THE DECIDING PLACE','For nearest hundred, inspect the tens digit','Keep hundreds; inspect tens\n0–4: down; 5–9: up',
 'To round to the nearest hundred, inspect the tens digit. Zero through four rounds down; five through nine rounds up.'),
 ('FIRST CONDITION','The hundreds must stay at two','72_6 → 7,200\nAllowed tens digits: 0, 1, 2, 3, 4',
 'In the first number, the hundreds must stay at two. The missing tens digit can be any digit from zero through four.'),
 ('SECOND CONDITION','The hundreds must increase from three to four','83_2 → 8,400\nAllowed tens digits: 5, 6, 7, 8, 9',
 'In the second number, the hundreds must increase from three to four. The missing tens digit can be five through nine.'),
 ('USE THE SAME RULE AT ANY PLACE','Inspect one place to the right of the rounding place','Nearest ten: inspect ones\nNearest thousand: inspect hundreds\nChoose every offered digit that fits',
 'For another rounding place, inspect the next place to its right. If choices are supplied, select every offered digit in the allowed range.')],
 g(4,2,1,5),equalities=[('7200+46','7246'),('8300+52','8352')]),
authored('place-tens-digit-of-sum','Find the tens digit of a sum using only the last two digits',
 'What is the tens digit of 6,347 + 928 + 15,269?', '4',
 'What is the tens digit of six thousand three hundred forty-seven plus nine hundred twenty-eight plus fifteen thousand two hundred sixty-nine?',[
 ('KEEP TWO DIGITS','Hundreds and larger places cannot affect the last two digits','6,347 → 47; 928 → 28; 15,269 → 69',
 'We only need the last two digits. Whole hundreds do not change the tens or ones digits of a sum.'),
 ('ADD THE SMALL PARTS','Include any carry from the ones','47 + 28 + 69 = 144',
 'Add forty-seven, twenty-eight and sixty-nine. The result is one hundred forty-four. This addition includes the carry from the ones.'),
 ('KEEP THE LAST TWO','Remove the complete hundred','144 − 100 = 44',
 'Remove the complete hundred. The last two digits of the original sum are forty-four.'),
 ('READ THE TENS','The tens digit is the left digit of forty-four','44 → tens digit 4\nFull check: 6,347 + 928 + 15,269 = 22,544',
 'The tens digit is four. The full sum is twenty-two thousand five hundred forty-four, which confirms the shortcut.')],
 ENR,equalities=[('47+28+69','144'),('(6347+928+15269)%100','44'),('6347+928+15269','22544')]),
]
def lessons(doc):return make_lessons(SPECS,doc)

# Exhaustively verify both digit ranges under nearest-hundred rounding.
assert [d for d in range(10) if ((7206+10*d+50)//100)*100==7200]==list(range(5))
assert [d for d in range(10) if ((8302+10*d+50)//100)*100==8400]==list(range(5,10))
