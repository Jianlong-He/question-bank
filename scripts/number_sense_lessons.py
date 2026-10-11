"""Checked elementary number-sense examples with explicit worksheet representatives."""
from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction as F
from math import gcd, lcm
from algebra_lessons import authored
from card_lessons import make_lessons


def source(grade,unit,worksheet,qid):
    return (f'worksheets/Grade {grade}/G{grade}Unit {unit}/G{grade}U{unit}W{worksheet}.csv',str(qid))


SPECS = [
authored('number-theory-smallest-with-prime-divisor-count','Smallest number with a given divisor count',
 'Find the smallest positive integer\nwith exactly 7 positive divisors.', '64',
 "Let's find the smallest positive integer with exactly seven positive divisors.",[
 ('DIVISOR COUNT', 'Add 1 to each prime exponent, then multiply', 'If n = pᵃqᵇ…, then d(n) = (a + 1)(b + 1)…',
  'In a prime factorization, add one to each exponent and multiply. This gives the number of positive divisors.'),
 ('USE SEVEN', 'A prime divisor count allows one prime factor', '7 is prime → n = p⁶',
  'Seven is prime, so only one prime factor can occur. Its exponent must be six, because six plus one is seven.'),
 ('MINIMIZE', 'Use the smallest prime, 2', 'n = 2⁶ = 64',
  'Choose the smallest prime, two, to make the number as small as possible. Two to the sixth power is sixty-four.'),
 ('CHECK', 'List all seven divisors', '1, 2, 4, 8, 16, 32, 64',
  'The divisors are one, two, four, eight, sixteen, thirty-two, and sixty-four. There are exactly seven.')],
 ('worksheets/enrichment/number-theory 1/U2prime-factorization/E-NT1U2W1HWb.csv','4'),
 expression='2**6',value='64'),

authored('number-place-value-whole-numbers','Tens and ones',
 'Write 67 as tens and ones.', '6 tens and 7 ones',
 "Let's break sixty-seven into tens and ones.",[
 ('TENS', 'The left digit counts the tens', '6 tens = 60',
  'The six is in the tens place. Six tens have a value of sixty.'),
 ('ONES', 'The right digit counts the ones', '7 ones = 7',
  'The seven is in the ones place. Seven ones have a value of seven.'),
 ('PUT THEM TOGETHER', 'Add the two place values', '60 + 7 = 67',
  'Sixty plus seven makes sixty-seven.'),
 ('ANSWER', 'Read the digits by place', '67 = 6 tens + 7 ones',
  'So sixty-seven is six tens and seven ones. The place tells us the value of each digit.')],
 source(1,1,3,9), expression='6*10+7',value='67'),

authored('number-place-value-expanded-form','Expanded form',
 'Write 594 in expanded form.', '500 + 90 + 4',
 "Let's write five hundred ninety-four in expanded form. Show the value of each digit.",[
 ('HUNDREDS', 'Start with the hundreds digit', '5 hundreds = 500',
  'The five is in the hundreds place. Its value is five hundred.'),
 ('TENS', 'Find the value of the tens digit', '9 tens = 90',
  'The nine is in the tens place. Its value is ninety.'),
 ('ONES', 'Find the value of the ones digit', '4 ones = 4',
  'The four is in the ones place. Its value is four.'),
 ('EXPANDED FORM', 'Add the place values', '594 = 500 + 90 + 4',
  'Expanded form is five hundred plus ninety plus four. Adding those parts gives our original number.')],
 source(2,2,2,3),expression='500+90+4',value='594'),

authored('number-place-value-decimals','Decimal place value',
 'What digit is in the hundredths\nplace of 43.682?', '8, with value 0.08',
 "Let's find the hundredths digit in forty-three point six eight two.",[
 ('START AT THE DECIMAL', 'Count places to the right', 'tenths → hundredths → thousandths',
  'Start at the decimal point. The places to its right are tenths, hundredths, then thousandths.'),
 ('MATCH THE DIGITS', 'Each digit has its own place', '6 tenths     8 hundredths     2 thousandths',
  'Six is in the tenths place, eight is in the hundredths place, and two is in the thousandths place.'),
 ('IDENTIFY', 'The hundredths digit is 8', '43.682 → 8 hundredths',
  'The digit we need is eight.'),
 ('VALUE', 'A digit and its value are different', '8 hundredths = 8/100 = 0.08',
  'Its place value is eight hundredths, or zero point zero eight. The digit is eight, but its value is not eight wholes.')],
 source(5,1,1,2),expression='8/100',value='0.08',equalities=[('43+6/10+8/100+2/1000','43.682')]),

authored('number-rounding-whole','Rounding to the nearest ten',
 'Round 73 to the nearest ten.', '70',
 "Let's round seventy-three to the nearest ten. We want the closest multiple of ten.",[
 ('NEIGHBOURS', 'Find the tens on either side', '70 < 73 < 80',
  'Seventy-three lies between seventy and eighty.'),
 ('LOOK RIGHT', 'Check the ones digit', 'Ones digit: 3\n0–4: keep the tens; 5–9: increase them.',
  'Look at the ones digit, three. Zero through four means keep the tens digit. Five through nine means increase it.'),
 ('ROUND', 'Keep 7 tens and replace ones with 0', '73 → 70',
  'Keep seven tens, then replace the ones digit with zero. The rounded number is seventy.'),
 ('CHECK', 'Compare the distances', '73 − 70 = 3\n80 − 73 = 7',
  'Seventy-three is three away from seventy and seven away from eighty, so seventy is closer.')],
 source(3,3,2,1),expression='7*10',value='70',equalities=[('73-70','3'),('80-73','7')]),

authored('number-rounding-decimals','Rounding a decimal',
 'Round 6.374 to the nearest hundredth.', '6.37',
 "Let's round six point three seven four to the nearest hundredth, which means two decimal places.",[
 ('TARGET PLACE', 'Keep through the hundredths', '6.374\nHundredths digit: 7',
  'The hundredths digit is seven. It is the second digit after the decimal point.'),
 ('LOOK RIGHT', 'Use the thousandths digit to decide', 'Next digit: 4\n0–4: keep; 5–9: increase by 1.',
  'The next digit is four. Since it is less than five, keep the hundredths digit unchanged.'),
 ('ROUND', 'Remove digits beyond the target place', '6.374 → 6.37',
  'Remove the digits beyond the hundredths place. Our rounded number is six point three seven.'),
 ('CHECK', 'Choose the nearer hundredth', '6.374 − 6.37 = 0.004\n6.38 − 6.374 = 0.006',
  'The number is closer to six point three seven than to six point three eight. That checks the answer.')],
 source(5,1,5,2),expression='637/100',value='6.37',equalities=[('6.374-6.37','0.004'),('6.38-6.374','0.006')]),

authored('fractions-equivalent','Equivalent fractions',
 'Find the missing numerator:\n5/11 = ?/44', '20',
 "Let's find the missing numerator. Five elevenths equals how many forty-fourths?",[
 ('FIND THE SCALE', 'Compare the denominators', '11 × 4 = 44',
  'Eleven times four is forty-four. The denominator was multiplied by four.'),
 ('MATCH THE SCALE', 'Multiply the numerator by 4 too', '5 × 4 = 20',
  'To keep the fraction equal, multiply the numerator by the same number. Five times four is twenty.'),
 ('ANSWER', 'Write the equivalent fraction', '5/11 = 20/44',
  'The missing numerator is twenty. Five elevenths equals twenty forty-fourths.'),
 ('CHECK', 'Divide both parts by 4', '(20 ÷ 4)/(44 ÷ 4) = 5/11',
  'Divide the numerator and denominator by four. We get five elevenths back.')],
 source(4,7,1,3),expression='5*4',value='20',equalities=[('5/11','20/44')]),

authored('fractions-compare','Comparing unlike fractions',
 'Which is larger: 7/12 or 5/8?', '5/8',
 "Let's compare seven twelfths and five eighths. Rewrite them using the same denominator.",[
 ('COMMON DENOMINATOR', 'Use 24 equal parts', '12 × 2 = 24\n8 × 3 = 24',
  'Twenty-four is a common multiple of twelve and eight, so we can compare twenty-fourths.'),
 ('EQUIVALENT FRACTIONS', 'Scale both parts of each fraction', '7/12 = 14/24\n5/8 = 15/24',
  'Seven twelfths becomes fourteen twenty-fourths. Five eighths becomes fifteen twenty-fourths.'),
 ('COMPARE', 'With equal denominators, compare numerators', '15/24 > 14/24',
  'The parts are the same size now. Fifteen parts is more than fourteen parts.'),
 ('ANSWER', 'Return to the original fractions', '5/8 > 7/12',
  'So five eighths is larger than seven twelfths. Matching denominators made the comparison fair.')],
 source(4,7,3,2),expression='5/8-7/12',value='1/24',equalities=[('7/12','14/24'),('5/8','15/24')]),

authored('fractions-common-denominator','Finding the least common denominator',
 'Rewrite 5/12 and 7/18\nwith their least common denominator.', '15/36 and 14/36; LCD = 36',
 "Let's rewrite five twelfths and seven eighteenths with their least common denominator.",[
 ('LIST MULTIPLES', 'Use multiples of both denominators', '12: 12, 24, 36, …\n18: 18, 36, …',
  'List multiples of twelve and eighteen. The first multiple they share is thirty-six.'),
 ('FIRST FRACTION', 'Multiply numerator and denominator by 3', '5/12 = (5 × 3)/(12 × 3) = 15/36',
  'Multiply both parts of five twelfths by three to get fifteen thirty-sixths.'),
 ('SECOND FRACTION', 'Multiply numerator and denominator by 2', '7/18 = (7 × 2)/(18 × 2) = 14/36',
  'Multiply both parts of seven eighteenths by two to get fourteen thirty-sixths.'),
 ('ANSWER', 'Both fractions now use the same size parts', 'LCD = 36\n5/12 = 15/36;   7/18 = 14/36',
  'The least common denominator is thirty-six. The equivalent fractions are fifteen thirty-sixths and fourteen thirty-sixths.')],
 source(4,7,2,7),expression='12*3',value='36',equalities=[('5/12','15/36'),('7/18','14/36')]),

authored('fractions-mixed-improper','Mixed numbers and improper fractions',
 'Convert 4 3/7 to an improper fraction.', '31/7',
 "Let's convert four and three sevenths into an improper fraction. Count everything in sevenths.",[
 ('CONVERT THE WHOLES', 'Each whole contains 7 sevenths', '4 × 7 = 28\n4 wholes = 28 sevenths',
  'Each whole is seven sevenths. Four wholes contain twenty-eight sevenths.'),
 ('ADD THE FRACTION', 'Include the extra 3 sevenths', '28 + 3 = 31 sevenths',
  'Add the extra three sevenths. That makes thirty-one sevenths.'),
 ('ANSWER', 'Keep the denominator', '4 3/7 = 31/7',
  'The denominator stays seven because the parts are still sevenths. The improper fraction is thirty-one over seven.'),
 ('CONVERT BACK', 'Divide the numerator by the denominator', '31 = 4 × 7 + 3\n31/7 = 4 3/7',
  'To convert back, divide thirty-one by seven. The quotient is four and the remainder is three, giving four and three sevenths.')],
 source(4,8,3,2),expression='4+3/7',value='31/7',equalities=[('31','4*7+3')]),

authored('decimal-fraction-conversion-to-decimal','A fraction as a decimal',
 'Write 3/8 as a decimal.', '0.375',
 "Let's write three eighths as a decimal. Use an equivalent fraction with a power of ten in the denominator.",[
 ('CHOOSE A DENOMINATOR', 'Use thousandths', '8 × 125 = 1000',
  'Eight times one hundred twenty-five is one thousand, so we can use thousandths.'),
 ('SCALE BOTH PARTS', 'Multiply numerator and denominator by 125', '3/8 = 375/1000',
  'Multiply both parts by one hundred twenty-five. Three times one hundred twenty-five is three hundred seventy-five.'),
 ('WRITE THE DECIMAL', 'Thousandths use three decimal places', '375/1000 = 0.375',
  'Three hundred seventy-five thousandths is zero point three seven five.'),
 ('CHECK', 'Multiply by the original denominator', '0.375 × 8 = 3',
  'Multiply the decimal by eight. We get three, so our conversion is correct.')],
 source(5,2,1,2),expression='3/8',value='0.375',equalities=[('8*125','1000'),('0.375*8','3')]),

authored('decimal-fraction-conversion-to-fraction','A decimal as a fraction',
 'Write 0.84 as a fraction in simplest form.', '21/25',
 "Let's write zero point eight four as a fraction in simplest form.",[
 ('READ THE PLACE', 'Two decimal places mean hundredths', '0.84 = 84 hundredths',
  'The final digit is in the hundredths place. This is eighty-four hundredths.'),
 ('WRITE A FRACTION', 'Put 84 over 100', '0.84 = 84/100',
  'Write eighty-four over one hundred.'),
 ('SIMPLIFY', 'Divide numerator and denominator by 4', '84/100 = (84 ÷ 4)/(100 ÷ 4)\n= 21/25',
  'Both numbers are divisible by four. Dividing gives twenty-one over twenty-five.'),
 ('CHECK', 'Confirm no common factor remains', '21 = 3 × 7\n25 = 5 × 5',
  'Twenty-one and twenty-five share no prime factor, so twenty-one twenty-fifths is in simplest form.')],
 source(5,2,1,9),expression='84/100',value='21/25',equalities=[('21*4','84'),('25*4','100')]),

authored('number-theory-factors','Finding every factor',
 'List all positive factors of 44.', '1, 2, 4, 11, 22, 44',
 "Let's list all positive factors of forty-four. Find factor pairs so none are missed.",[
 ('START WITH ONE', 'One pairs with the number itself', '1 × 44 = 44',
  'One times forty-four is forty-four, so one and forty-four are factors.'),
 ('TEST SMALL NUMBERS', 'Try the next possible factors', '2 × 22 = 44\n4 × 11 = 44',
  'Two pairs with twenty-two, and four pairs with eleven. Three, five, and six do not divide forty-four evenly.'),
 ('KNOW WHEN TO STOP', 'Two factors of 7 or more would be too large', '7 × 7 = 49 > 44',
  'Any new pair would need two factors of seven or more. But seven times seven is already forty-nine, larger than forty-four, so we have found every pair.'),
 ('LIST IN ORDER', 'Include both numbers from every pair', '1, 2, 4, 11, 22, 44',
  'Put both numbers from each pair in order: one, two, four, eleven, twenty-two, forty-four.')],
 source(4,6,1,8),expression='4*11',value='44',equalities=[('1*44','44'),('2*22','44')]),

authored('number-theory-gcf','Greatest common factor',
 'Find the greatest common factor\nof 42 and 70.', '14',
 "Let's find the greatest common factor of forty-two and seventy. List each number's factors.",[
 ('FACTORS OF 42', 'Use factor pairs', '42: 1, 2, 3, 6, 7, 14, 21, 42',
  'The factors of forty-two are one, two, three, six, seven, fourteen, twenty-one, and forty-two.'),
 ('FACTORS OF 70', 'List the second set of factors', '70: 1, 2, 5, 7, 10, 14, 35, 70',
  'The factors of seventy are one, two, five, seven, ten, fourteen, thirty-five, and seventy.'),
 ('COMMON FACTORS', 'Keep the factors found in both lists', 'Common factors: 1, 2, 7, 14',
  'Both lists contain one, two, seven, and fourteen.'),
 ('GREATEST', 'Choose the largest common factor', 'GCF(42, 70) = 14\n42 = 14 × 3;   70 = 14 × 5',
  'Fourteen is the largest common factor. It divides both numbers evenly.')],
 source(6,6,9,3),expression='42/3',value='14',equalities=[('14*3','42'),('14*5','70')]),

authored('number-theory-lcm','Least common multiple',
 'Find the least common multiple\nof 8 and 14.', '56',
 "Let's find the least common multiple of eight and fourteen. We need the smallest positive number in both multiplication tables.",[
 ('MULTIPLES OF 8', 'Count by eights', '8, 16, 24, 32, 40, 48, 56, …',
  'The multiples of eight begin eight, sixteen, twenty-four, thirty-two, forty, forty-eight, fifty-six.'),
 ('MULTIPLES OF 14', 'Count by fourteens', '14, 28, 42, 56, …',
  'The multiples of fourteen begin fourteen, twenty-eight, forty-two, fifty-six.'),
 ('FIRST COMMON MULTIPLE', 'Choose the first number in both lists', 'LCM(8, 14) = 56',
  'Fifty-six is the first number in both lists, so it is the least common multiple.'),
 ('CHECK', 'Both numbers divide it evenly', '56 ÷ 8 = 7\n56 ÷ 14 = 4',
  'Fifty-six divided by eight is seven, and divided by fourteen is four. Both quotients are whole numbers.')],
 source(5,4,2,1),expression='8*7',value='56',equalities=[('56/8','7'),('56/14','4')]),

authored('number-theory-prime-composite','Prime or composite?',
 'Is 41 prime or composite?', 'Prime',
 "Let's decide whether forty-one is prime or composite. A prime number has exactly two positive factors.",[
 ('LIMIT THE SEARCH', 'Every factor pair needs a factor below 7', '7 × 7 = 49 > 41\nTest primes 2, 3 and 5.',
  'Two factors of seven or more would make a product larger than forty-one. We only need to test the primes below seven: two, three, and five.'),
 ('TEST 2 AND 3', 'Check divisibility', '41 is odd.\n4 + 1 = 5, not a multiple of 3.',
  'Forty-one is odd, so two is not a factor. Its digit sum is five, so three is not a factor.'),
 ('TEST 5', 'Check the last digit', '41 ends in 1, not 0 or 5.',
  'It does not end in zero or five, so five is not a factor either.'),
 ('CONCLUDE', 'Only 1 and 41 are factors', 'Factors: 1, 41\n41 is prime.',
  'None of the tested primes divides forty-one. Its only positive factors are one and forty-one, so it is prime.')],
 source(4,6,2,1),expression='41%2',value='1',equalities=[('41%3','2'),('41%5','1')]),
]


def factors(n):return [d for d in range(1,n+1) if n%d==0]


def check_answers():
    assert next(n for n in range(1,65) if len(factors(n))==7)==64
    assert Decimal('73').quantize(Decimal('1E1'),rounding=ROUND_HALF_UP)==Decimal('70')
    assert Decimal('6.374').quantize(Decimal('.01'),rounding=ROUND_HALF_UP)==Decimal('6.37')
    assert F(5,8)>F(7,12)
    assert lcm(12,18)==36
    assert factors(44)==[1,2,4,11,22,44]
    assert factors(42)==[1,2,3,6,7,14,21,42]
    assert factors(70)==[1,2,5,7,10,14,35,70]
    assert gcd(42,70)==14 and lcm(8,14)==56
    assert gcd(21,25)==1 and factors(41)==[1,41]


def lessons(doc):
    check_answers()
    return make_lessons(SPECS,doc)
