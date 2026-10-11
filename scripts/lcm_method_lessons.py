"""Distinct LCM methods for numbers, fractions and polynomials."""
from math import lcm
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons
SPECS=[
authored('lcm-polynomial-factors','Find a polynomial LCM from complete factorizations',
 'Find the LCM of x² − 25 and x² + 10x + 25.', '(x − 5)(x + 5)²',
 'Find the least common multiple of x squared minus twenty-five, and x squared plus ten x plus twenty-five.',[
 ('FIRST POLYNOMIAL','Use the difference of two squares','x² − 25 = (x − 5)(x + 5)',
 'The first polynomial is a difference of squares. It factors as x minus five times x plus five.'),
 ('SECOND POLYNOMIAL','Recognize a perfect-square trinomial','x² + 10x + 25 = (x + 5)²',
 'The second polynomial is a perfect square. The positive middle term gives x plus five squared.'),
 ('TAKE EACH FACTOR','Use the greatest exponent found in either expression','Factor x − 5: power 1\nFactor x + 5: power 2',
 'Include every distinct factor, using its greatest exponent from either polynomial. We need one copy of x minus five and two copies of x plus five.'),
 ('WRITE AND CHECK','The LCM contains every factor required by both','LCM = (x − 5)(x + 5)²',
 'The least common multiple is x minus five times x plus five squared. It is divisible by both original polynomials, with no unnecessary factors.')],
 g(11,13,6,9),identities=[('x**2-25','(x-5)*(x+5)'),('x**2+10*x+25','(x+5)**2'),('(x**2-25)*(x+5)','(x-5)*(x+5)**2')]),
authored('lcm-three-number-multiples','Find a common multiple shared by three numbers',
 'Find the LCM of 4, 6 and 15 by checking multiples.', '60',
 'Find the least common multiple of four, six and fifteen by checking multiples.',[
 ('START WITH THE LARGEST','Any common multiple must be a multiple of fifteen','15, 30, 45, 60, ...',
 'Start with multiples of the largest number, fifteen. Any common multiple must occur in this list.'),
 ('TEST IN ORDER','Check divisibility by both remaining numbers','15: not divisible by 4\n30: not divisible by 4\n45: not divisible by 4',
 'Test the multiples in order. Fifteen, thirty and forty-five fail because none is divisible by four.'),
 ('FIRST SUCCESS','Sixty is divisible by all three numbers','60 ÷ 4 = 15\n60 ÷ 6 = 10\n60 ÷ 15 = 4',
 'Sixty divides evenly by four, six and fifteen. It works for all three numbers.'),
 ('WHY LEAST','Every smaller candidate in the list failed','LCM(4,6,15) = 60',
 'Because every smaller multiple of fifteen failed, sixty is the least common multiple. Do not stop at a number shared by only two of the three.')],
 g(5,4,2,9),equalities=[('60/4','15'),('60/6','10'),('60/15','4')]),
authored('lcm-prime-factor-method','Find an LCM by taking the largest prime powers',
 'Use prime factorization to find the LCM of 18, 40 and 60.', '360',
 'Use prime factorization to find the least common multiple of eighteen, forty and sixty.',[
 ('FACTOR COMPLETELY','Break every composite factor into primes','18 = 2 × 3²\n40 = 2³ × 5\n60 = 2² × 3 × 5',
 'Eighteen is two times three squared. Forty is two cubed times five. Sixty is two squared times three times five.'),
 ('COLLECT PRIME POWERS','Take the largest exponent of every prime','For 2: power 3; for 3: power 2\nFor 5: power 1',
 'The largest needed powers are two cubed, three squared, and five. This supplies enough of each prime for every original number.'),
 ('MULTIPLY','Use one copy of each selected prime power','LCM = 2³ × 3² × 5\n= 8 × 9 × 5 = 360',
 'Multiply eight, nine and five to get three hundred sixty.'),
 ('CHECK','Every original number divides the LCM','360 ÷ 18 = 20; 360 ÷ 40 = 9\n360 ÷ 60 = 6',
 'All three numbers divide three hundred sixty. Taking just the largest required powers makes it the least common multiple. For two numbers, use the same rule.')],
 g(6,6,7,5),equalities=[('2*3**2','18'),('2**3*5','40'),('2**2*3*5','60'),('8*9*5','360'),('360/18','20'),('360/40','9'),('360/60','6')]),
authored('lcm-find-possible-number','Find all positive integers with a specified LCM',
 'Find every positive integer y such that LCM(8,y) = 24.', '3, 6, 12, 24',
 'Find every positive integer y such that the least common multiple of eight and y is twenty-four.',[
 ('RESTRICT CANDIDATES','Every y must divide the target LCM','Divisors of 24:\n1, 2, 3, 4, 6, 8, 12, 24',
 'Since twenty-four is a multiple of y, y must be a positive divisor of twenty-four. List those divisors.'),
 ('FIND THE MISSING PRIME','Eight already supplies all three factors of two','8 = 2³; 24 = 2³ × 3',
 'Eight already supplies two cubed. To make the least common multiple twenty-four, y must supply a factor of three.'),
 ('KEEP THE VALID CANDIDATES','Choose the listed divisors that contain three','3, 6, 12, 24',
 'Keep the divisors containing three: three, six, twelve and twenty-four. Each has no prime power beyond those allowed in twenty-four.'),
 ('CHECK COMPLETENESS','Each candidate supplies exactly what is needed','LCM(8,3)=24; LCM(8,6)=24\nLCM(8,12)=24; LCM(8,24)=24',
 'Each candidate has least common multiple twenty-four with eight. All other divisors lacked the factor three, so the list is complete.')],
 g(6,6,7,10),equalities=[('2**3','8'),('2**3*3','24')]),
authored('lcm-fraction-sum-mixed-answer','Add fractions with the LCD and simplify to a mixed number',
 'Add 7/10 + 11/14 using the least common denominator.\nWrite the answer as a mixed number in simplest form.', '1 17/35',
 'Add seven tenths and eleven fourteenths using the least common denominator. Write the result as a mixed number in simplest form.',[
 ('FIND THE LCD','Use the largest prime powers from ten and fourteen','10 = 2 × 5; 14 = 2 × 7\nLCD = 2 × 5 × 7 = 70',
 'The least common multiple of ten and fourteen is seventy. That is our least common denominator.'),
 ('REWRITE BOTH FRACTIONS','Multiply numerator and denominator by the same number','7/10 = 49/70\n11/14 = 55/70',
 'Multiply both parts of seven tenths by seven to get forty-nine seventieths. Multiply both parts of eleven fourteenths by five to get fifty-five seventieths.'),
 ('ADD AND SIMPLIFY','Add numerators, then reduce by two','49/70 + 55/70 = 104/70 = 52/35',
 'Add the numerators to get one hundred four seventieths. Divide numerator and denominator by two, giving fifty-two thirty-fifths.'),
 ('CONVERT TO MIXED FORM','Divide fifty-two by thirty-five','52 = 1 × 35 + 17\n52/35 = 1 17/35',
 'Fifty-two contains one whole thirty-five and seventeen left over. The answer is one and seventeen thirty-fifths, already in simplest form.')],
 g(5,4,3,7),equalities=[('7/10','49/70'),('11/14','55/70'),('7/10+11/14','52/35'),('52/35','1+17/35')]),
authored('lcm-three-fraction-subtraction','Subtract three fractions using one least common denominator',
 'Subtract step by step: 5/6 − 1/5 − 1/10.\nUse the least common denominator.', '8/15',
 'Subtract five sixths minus one fifth minus one tenth, step by step, using the least common denominator.',[
 ('FIND THE LCD','Thirty is the LCM of six, five and ten','6 = 2 × 3; 5 = 5; 10 = 2 × 5\nLCD = 30',
 'The least common multiple of six, five and ten is thirty.'),
 ('REWRITE EACH FRACTION','Keep all three fractions on the same denominator','5/6 = 25/30\n1/5 = 6/30\n1/10 = 3/30',
 'The equivalent fractions are twenty-five thirtieths, six thirtieths, and three thirtieths.'),
 ('SUBTRACT LEFT TO RIGHT','Both subtractions reduce the numerator','25/30 − 6/30 = 19/30\n19/30 − 3/30 = 16/30',
 'First subtract six from twenty-five to get nineteen. Then subtract three to get sixteen. Keep the denominator thirty.'),
 ('SIMPLIFY','Divide numerator and denominator by two','16/30 = 8/15',
 'Reduce sixteen thirtieths by dividing both parts by two. The result is eight fifteenths. Keep both subtraction signs; do not subtract the second fraction from the third first.')],
 g(5,4,4,8),equalities=[('5/6-1/5','19/30'),('19/30-1/10','16/30'),('16/30','8/15')]),
]
def lessons(doc):return make_lessons(SPECS,doc)
assert lcm(4,6,15)==60 and lcm(18,40,60)==360 and lcm(10,14)==70
assert [n for n in range(1,25) if lcm(8,n)==24]==[3,6,12,24]
