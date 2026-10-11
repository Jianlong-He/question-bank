"""Worked Euclidean calculations, parity reductions and GCD/LCM relationships."""
from math import gcd,lcm
from algebra_lessons import authored
from number_theory_lessons import source as e
from card_lessons import make_lessons
SPECS=[
authored('gcf-linear-parity','Reduce a parameterized GCD to a parity test',
 'For integers m > 3, find gcd(2m, m − 1).\nSeparate odd and even m.', '2 for odd m; 1 for even m',
 'For integers m greater than three, find the greatest common divisor of two m and m minus one. Separate odd and even values of m.',[
 ('DIVIDE SYMBOLICALLY','Subtract twice the second number','2m = 2(m − 1) + 2',
 'Subtract twice m minus one from two m. The remainder is two.'),
 ('REDUCE THE GCD','A Euclidean step preserves the GCD','gcd(2m, m − 1) = gcd(m − 1, 2)',
 'The greatest common divisor is unchanged, so we only need the greatest common divisor of m minus one and two.'),
 ('ODD INPUT','An odd m makes m minus one even','m odd → m − 1 even → GCD = 2',
 'When m is odd, m minus one is even. Its greatest common divisor with two is two.'),
 ('EVEN INPUT','An even m makes m minus one odd','m even → m − 1 odd → GCD = 1\nExamples: gcd(10,4)=2; gcd(12,5)=1',
 'When m is even, m minus one is odd, so the greatest common divisor is one. Reducing to a small constant reveals the needed parity test.')],
 e('Euclidean-division',1,9),identities=[('2*m','2*(m-1)+2')],equalities=[('2*5','10'),('2*6','12')]),
authored('gcf-quadratic-parity','Reduce a quadratic GCD using a square and a remainder',
 'For integers t > 3, find gcd(t² − 2t + 3, t − 1).\nSeparate odd and even t.', '2 for odd t; 1 for even t',
 'For integers t greater than three, find the greatest common divisor of t squared minus two t plus three, and t minus one. Separate odd and even t.',[
 ('REWRITE THE QUADRATIC','Complete a square to expose a multiple of the divisor','t² − 2t + 3 = (t − 1)² + 2',
 'Rewrite the quadratic as t minus one squared, plus two.'),
 ('REMOVE THE MULTIPLE','The squared term is divisible by t minus one','gcd((t − 1)² + 2, t − 1)\n= gcd(2, t − 1)',
 'The square is a multiple of t minus one. Removing that multiple leaves a remainder of two.'),
 ('TEST ODD t','Then t minus one is even','t odd → gcd(2, t − 1) = 2',
 'If t is odd, t minus one is even. The greatest common divisor is two.'),
 ('TEST EVEN t','Then t minus one is odd','t even → gcd(2, t − 1) = 1\nCheck t=6: gcd(27,5)=1',
 'If t is even, t minus one is odd, so the greatest common divisor is one. Rewriting the polynomial makes the same small-remainder method available.')],
 e('Euclidean-division',1,10),identities=[('t**2-2*t+3','(t-1)**2+2')],equalities=[('6**2-2*6+3','27')]),
authored('gcf-lcm-product-formula','Find the LCM from the product and GCD',
 'Find lcm(28,42) using the product divided by the GCD.', '84',
 'Find the least common multiple of twenty-eight and forty-two using their product divided by their greatest common divisor.',[
 ('FIND THE GCD','Use a short Euclidean calculation','42 = 1 × 28 + 14\n28 = 2 × 14 + 0; GCD = 14',
 'The Euclidean algorithm gives greatest common divisor fourteen.'),
 ('FIND THE PRODUCT','Multiply the two positive numbers','28 × 42 = 1,176',
 'The product of the two numbers is one thousand one hundred seventy-six.'),
 ('USE THE RELATIONSHIP','For positive numbers, GCD times LCM equals their product','LCM = product ÷ GCD\n1,176 ÷ 14 = 84',
 'For positive integers, the greatest common divisor times the least common multiple equals their product. Divide the product by fourteen to get eighty-four.'),
 ('CHECK','The result is a multiple of each original number','84 = 3 × 28 = 2 × 42',
 'Eighty-four is three times twenty-eight and twice forty-two. If the product and greatest common divisor are already given, begin directly with the division formula.')],
 e('Euclidean-division',2,1),equalities=[('28*42','1176'),('1176/14','84'),('3*28','2*42')]),
authored('gcf-lcm-prime-exponents','Use minimum and maximum prime exponents for GCD and LCM',
 'Find the GCD and LCM of\nA = 2³ × 3² × 5² and B = 2² × 3⁴ × 7.', 'GCD 36; LCM 113,400',
 'Find the greatest common divisor and least common multiple of two cubed times three squared times five squared, and two squared times three to the fourth times seven.',[
 ('GCD RULE','Use shared primes with the smaller exponent','GCD = 2² × 3² = 36',
 'For the greatest common divisor, use only shared primes, taking the smaller exponent. Two squared times three squared is thirty-six.'),
 ('LCM RULE','Use every prime with the larger exponent','LCM = 2³ × 3⁴ × 5² × 7',
 'For the least common multiple, include every prime appearing in either number, using its larger exponent.'),
 ('CALCULATE','Evaluate the powers before multiplying','8 × 81 × 25 × 7 = 113,400',
 'Multiply eight, eighty-one, twenty-five and seven. The least common multiple is one hundred thirteen thousand four hundred.'),
 ('CHECK THE PRODUCT','GCD times LCM must equal A times B','A = 1,800; B = 2,268\n36 × 113,400 = 1,800 × 2,268',
 'The original numbers are one thousand eight hundred and two thousand two hundred sixty-eight. Their product matches the greatest common divisor times the least common multiple.')],
 e('prime-factorization',5,10),equalities=[('2**3*3**2*5**2','1800'),('2**2*3**4*7','2268'),('2**2*3**2','36'),('8*81*25*7','113400'),('36*113400','1800*2268')]),
authored('gcf-euclidean-trace','Record Euclidean quotients and remainders in order',
 'Find gcd(76,29). Record each quotient q\nand remainder r, including the final zero remainder.', 'GCD 1; q: 2,1,1,1,1,1,3; r: 18,11,7,4,3,1,0',
 'Find the greatest common divisor of seventy-six and twenty-nine. Record each quotient and remainder, including the final zero remainder.',[
 ('FIRST THREE STEPS','In each row, dividend equals quotient times divisor plus remainder','76 = 2 × 29 + 18\n29 = 1 × 18 + 11\n18 = 1 × 11 + 7',
 'Each row has a quotient and a remainder. The first three quotients are two, one, one. Their remainders are eighteen, eleven, seven.'),
 ('KEEP REPEATING','Use the previous divisor and remainder as the new pair','11 = 1 × 7 + 4\n7 = 1 × 4 + 3',
 'Continue with the previous divisor and remainder. The next quotients are one and one, with remainders four and three.'),
 ('STOP AT ZERO','The last nonzero remainder is the GCD','4 = 1 × 3 + 1\n3 = 3 × 1 + 0\nGCD = 1',
 'Four divided by three leaves one. Three divided by one leaves zero. Stop; the last nonzero remainder is one.'),
 ('READ IN ORDER','Match the requested step numbers to their rows','q: 2, 1, 1, 1, 1, 1, 3\nr: 18, 11, 7, 4, 3, 1, 0',
 'Read quotients and remainders in row order. Include only the step numbers requested by your question; here we included every step through zero.')],
 e('Euclidean-division',3,3),equalities=[('76','2*29+18'),('29','18+11'),('18','11+7'),('11','7+4'),('7','4+3'),('4','3+1'),('3','3*1')]),
authored('gcf-extended-euclid','Find integer coefficients by reversing Euclidean divisions',
 'Find gcd(114,42), then integers x,y\nsuch that 114x + 42y equals that GCD.', 'GCD 6; x=3, y=−8',
 'Find the greatest common divisor of one hundred fourteen and forty-two, then find integers x and y whose linear combination equals that greatest common divisor.',[
 ('START EUCLID','Divide, then repeat with divisor and remainder','114 = 2 × 42 + 30\n42 = 1 × 30 + 12',
 'The first two divisions leave remainders thirty and twelve.'),
 ('FIND THE GCD','Continue until the remainder is zero','30 = 2 × 12 + 6\n12 = 2 × 6 + 0\nGCD = 6',
 'The next remainder is six, followed by zero. The greatest common divisor is six.'),
 ('SUBSTITUTE BACKWARDS','Replace the remainders by earlier expressions','6 = 30 − 2 × 12\n= 30 − 2(42 − 30)\n= 3 × 30 − 2 × 42',
 'Solve the last nonzero-remainder equation for six. Replace twelve with forty-two minus thirty, then combine the thirty terms.'),
 ('USE THE ORIGINAL NUMBERS','Replace thirty, then read the coefficients','6 = 3(114 − 2 × 42) − 2 × 42\n= 3 × 114 − 8 × 42\nx=3, y=−8; check: 342 − 336 = 6',
 'Replace thirty with one hundred fourteen minus twice forty-two. This gives three times one hundred fourteen minus eight times forty-two. Thus x is three and y is negative eight.')],
 e('Euclidean-division',3,7),equalities=[('114','2*42+30'),('42','30+12'),('30','2*12+6'),('12','2*6'),('3*114-8*42','6')]),
]
def lessons(doc):return make_lessons(SPECS,doc)
assert gcd(28,42)==14 and lcm(28,42)==84
assert gcd(1800,2268)==36 and lcm(1800,2268)==113400
assert gcd(76,29)==1 and gcd(114,42)==6
for n in range(4,100):
 assert gcd(2*n,n-1)==(2 if n%2 else 1)
 assert gcd(n*n-2*n+3,n-1)==(2 if n%2 else 1)
