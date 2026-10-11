"""Fresh modular-arithmetic examples, grouped by explicitly reviewed method."""
from algebra_lessons import authored
from number_theory_lessons import source
from card_lessons import make_lessons

def e(w,q): return source('modular-arithmetic',w,q)
SPECS=[
authored('modular-signed-addition','Reduce positive and negative sums modulo a number',
 'Find the least nonnegative remainders:\n23 + 16 (mod 7) and 6 − 24 (mod 7).','4 and 3',
 'Find the least nonnegative remainders of twenty-three plus sixteen, and six minus twenty-four, modulo seven.',[
 ('CALCULATE FIRST','Addition and subtraction work as usual','23 + 16 = 39\n6 − 24 = −18',
 'First calculate each expression normally. The results are thirty-nine and negative eighteen.'),
 ('REDUCE THE POSITIVE TOTAL','Remove whole multiples of seven','39 = 7 × 5 + 4\n39 mod 7 = 4',
 'Thirty-nine is five sevens plus four. Removing whole sevens leaves remainder four.'),
 ('REDUCE THE NEGATIVE TOTAL','Add whole multiples until the result is nonnegative','−18 + 3 × 7 = 3\n−18 mod 7 = 3',
 'For negative eighteen, add three sevens to reach three. Adding a multiple of seven does not change the remainder.'),
 ('CHECK THE RANGE','Modulo seven uses remainders zero through six','0 ≤ 4 < 7 and 0 ≤ 3 < 7\nRemainders: 4 and 3',
 'Both remainders lie from zero through six. Keep reducing until the answer is in that range.')],e('1-1',1),equalities=[('(23+16)%7','4'),('(6-24)%7','3')]),
authored('modular-additive-unknown','Solve an additive congruence in the required range',
 'Find x and y from 0 through 8:\n(25 + x) mod 9 = 2\n(25 − y) mod 9 = 2','x = 4; y = 5',
 'Find x and y from zero through eight. Twenty-five plus x, and twenty-five minus y, must each leave remainder two modulo nine.',[
 ('REDUCE THE CONSTANT','Replace twenty-five by its remainder','25 ≡ 7 (mod 9)\n7 + x ≡ 2; 7 − y ≡ 2 (mod 9)',
 'Twenty-five leaves remainder seven modulo nine. Use seven in each equation.'),
 ('SOLVE THE ADDITION','Subtract seven and reduce the result','x ≡ 2 − 7 ≡ −5 ≡ 4 (mod 9)\nx = 4 within the required range.',
 'Subtract seven to get x congruent to negative five. Add nine to obtain four, the value in the required range.'),
 ('SOLVE THE SUBTRACTION','Isolate the variable carefully','7 − y ≡ 2 (mod 9)\ny ≡ 7 − 2 ≡ 5 (mod 9)',
 'For the subtraction equation, y is congruent to seven minus two. That gives y equal to five.'),
 ('CHECK BOTH ANSWERS','Use the original expressions','25 + 4 = 29 = 9 × 3 + 2\n25 − 5 = 20 = 9 × 2 + 2',
 'Check the original expressions. Twenty-nine and twenty both leave remainder two when divided by nine.')],e('1-1',9),equalities=[('(25+4)%9','2'),('(25-5)%9','2')]),
authored('modular-nested-order','Evaluate nested remainders in the stated order',
 'Compare using <, =, or >:\n((8 × 4) mod 9) mod 4\nand ((8 × 4) mod 4) mod 9.','1 > 0',
 'Compare two nested remainder calculations. Both start with eight times four, but one uses modulo nine first and the other uses modulo four first.',[
 ('CALCULATE THE COMMON INPUT','Both expressions begin with the same product','8 × 4 = 32',
 'Eight times four is thirty-two. Now follow the parentheses separately on each side.'),
 ('FOLLOW THE FIRST ORDER','Modulo nine, then modulo four','32 mod 9 = 5\n5 mod 4 = 1',
 'On the first side, thirty-two modulo nine is five. Then five modulo four is one.'),
 ('FOLLOW THE OTHER ORDER','Modulo four, then modulo nine','32 mod 4 = 0\n0 mod 9 = 0',
 'On the other side, thirty-two modulo four is zero. Zero modulo nine is still zero.'),
 ('COMPARE THE FINAL VALUES','The order of the remainder operations matters','1 > 0\nUse the greater-than symbol.',
 'One is greater than zero. Changing the order of these remainder operations can change the answer.')],e('1HWb',1),equalities=[('(8*4%9)%4','1'),('(8*4%4)%9','0')]),
authored('modular-common-remainder-bound','Use an LCM to find a number with a common remainder',
 'Find the smallest integer N > 70\nthat leaves remainder 2 when divided\nby 4, 6, and 10.','122',
 'Find the smallest integer greater than seventy that leaves remainder two when divided by four, six, and ten.',[
 ('REMOVE THE SHARED REMAINDER','Subtracting two makes every division exact','N − 2 is divisible by 4, 6, and 10.',
 'Subtract the shared remainder, two. The result must be a common multiple of four, six, and ten.'),
 ('FIND THE COMMON PERIOD','Use the highest power of each prime','4 = 2²; 6 = 2 × 3; 10 = 2 × 5\nLCM = 2² × 3 × 5 = 60',
 'The least common multiple uses two squared, three, and five. It is sixty.'),
 ('APPLY THE LOWER BOUND','Add two to consecutive multiples of sixty','N = 60k + 2\n2, 62, 122, 182, …; first above 70 is 122.',
 'All candidates have the form sixty k plus two. Two and sixty-two are too small. The first candidate above seventy is one hundred twenty-two.'),
 ('CHECK ALL THREE DIVISORS','Each division must leave exactly two','122 = 4 × 30 + 2 = 6 × 20 + 2\n122 = 10 × 12 + 2',
 'Check each divisor. One hundred twenty-two leaves remainder two in all three divisions and meets the lower bound.')],e('1HWa',2),equalities=[('4*30+2','122'),('6*20+2','122'),('10*12+2','122')]),
authored('modular-unknown-modulus','Find possible moduli by factoring the difference',
 'Find every integer n > 12 such that\n11 × 9 has least nonnegative remainder 3\nwhen divided by n.','16, 24, 32, 48, 96',
 'Find every integer n greater than twelve such that eleven times nine leaves least nonnegative remainder three when divided by n.',[
 ('REMOVE THE REMAINDER','The modulus divides the product minus the remainder','11 × 9 = 99\n99 − 3 = 96, so n divides 96.',
 'The product is ninety-nine. Subtract the required remainder, three. The modulus must divide ninety-six.'),
 ('LIST EVERY POSITIVE DIVISOR','Factor ninety-six to avoid missing candidates','96 = 2⁵ × 3\nDivisors: 1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 96',
 'Factor ninety-six as two to the fifth times three. List every positive divisor, including ninety-six itself.'),
 ('APPLY BOTH RESTRICTIONS','The modulus exceeds both the bound and the remainder','n > 12 and n > 3\nAllowed: 16, 24, 32, 48, 96',
 'The question requires n greater than twelve. A canonical remainder of three also requires n greater than three. Keep only the divisors meeting both restrictions.'),
 ('VERIFY AND SELECT','The same method handles a requested smallest modulus','99 = 16 × 6 + 3; smallest allowed n is 16.\nRemainder 1 would mean the factors are inverses.',
 'For example, ninety-nine is six sixteens plus three. Sixteen is the smallest allowed modulus. With remainder one, this method finds moduli where two factors are inverses.')],e(2,10),equalities=[('11*9-3','96'),('16*6+3','99')]),
authored('modular-signed-products','Reduce factors before multiplying modulo a number',
 'Find the least nonnegative remainder\nof (−13) × 25 × 38 modulo 9.','7',
 'Find the least nonnegative remainder of negative thirteen times twenty-five times thirty-eight modulo nine.',[
 ('REDUCE EACH FACTOR','Whole multiples of nine do not affect the remainder','−13 ≡ 5; 25 ≡ 7; 38 ≡ 2 (mod 9)',
 'Reduce each factor. Negative thirteen is congruent to five, twenty-five to seven, and thirty-eight to two.'),
 ('MULTIPLY SMALLER NUMBERS','Use the same modulus throughout','(−13) × 25 × 38 ≡ 5 × 7 × 2 (mod 9)',
 'Replace the original factors with their remainders. Now multiply five, seven, and two.'),
 ('REDUCE AS YOU GO','Intermediate reduction keeps the arithmetic small','5 × 7 = 35 ≡ 8 (mod 9)\n8 × 2 = 16 ≡ 7 (mod 9)',
 'Five times seven is thirty-five, which reduces to eight. Eight times two is sixteen, which reduces to seven.'),
 ('CHECK THE REQUIRED RANGE','A remainder modulo nine lies from zero to eight','0 ≤ 7 < 9\nThe least nonnegative remainder is 7.',
 'Seven is in the required range. You can reduce after each multiplication, even when the original product contains a negative factor.')],e('2HWa',3),expression='(-13*25*38)%9',value='7',equalities=[('(-13)%9','5'),('(25*38)%9','5')]),
authored('modular-polynomial-substitution','Substitute a known remainder into a polynomial',
 'An integer n + 2 is divisible by 5.\nFind the remainder of n² + 3 modulo 5.','2',
 'An integer n plus two is divisible by five. Find the remainder of n squared plus three modulo five.',[
 ('TRANSLATE DIVISIBILITY','A multiple of five has remainder zero','n + 2 ≡ 0 (mod 5)\nn ≡ −2 ≡ 3 (mod 5)',
 'Since n plus two is a multiple of five, n is congruent to negative two, or equivalently three.'),
 ('SUBSTITUTE THE REMAINDER','Sums and products preserve congruence','n² + 3 ≡ 3² + 3 (mod 5)',
 'Replace n by its remainder, three. Squaring is multiplication, so it preserves the congruence.'),
 ('EVALUATE AND REDUCE','The polynomial value still needs reduction','3² + 3 = 12\n12 = 5 × 2 + 2',
 'Three squared plus three equals twelve. Twelve is two fives plus two, so the remainder is two.'),
 ('EXPLAIN WHY IT IS GENERAL','Any integer with the given remainder works','n = 5k + 3\nn² + 3 = 5(5k² + 6k + 2) + 2',
 'Writing n as five k plus three shows that the polynomial is always a multiple of five plus two.')],e('2HWb',5),expression='(3**2+3)%5',value='2',identities=[('(5*k+3)**2+3','5*(5*k**2+6*k+2)+2')]),
authored('modular-symbolic-factors','Find a constant remainder from symbolic factors',
 'For every integer n > 6, find\n((n − 3)(n − 2)) mod n.','6',
 'For every integer n greater than six, find the remainder of n minus three times n minus two, modulo n.',[
 ('REDUCE THE FACTORS','A whole copy of n disappears modulo n','n − 3 ≡ −3 (mod n)\nn − 2 ≡ −2 (mod n)',
 'Modulo n, a whole copy of n contributes zero. The two factors are congruent to negative three and negative two.'),
 ('MULTIPLY THE REMAINDERS','Two negative factors give a positive product','(n − 3)(n − 2) ≡ (−3)(−2) ≡ 6 (mod n)',
 'Multiply the reduced factors. Negative three times negative two is six.'),
 ('VERIFY WITH EXPANSION','Separate a multiple of n from a constant','(n − 3)(n − 2) = n² − 5n + 6\n= n(n − 5) + 6',
 'Expanding gives n squared minus five n plus six. The first two terms form a multiple of n.'),
 ('CHECK THE DOMAIN','A canonical remainder must be smaller than the modulus','n > 6 ensures 0 ≤ 6 < n.\nTherefore the remainder is always 6.',
 'Because n is greater than six, six is already an allowed remainder. That domain condition makes the answer constant.')],e(3,10),identities=[('(n-3)*(n-2)','n*(n-5)+6')]),
authored('modular-no-inverse','Show when a modular inverse does not exist',
 'Does 10 have an inverse modulo 35?\nExplain without testing every possible value.','No inverse',
 'Does ten have an inverse modulo thirty-five? Explain without testing every possible value.',[
 ('STATE THE INVERSE CONDITION','An inverse would make the product congruent to one','10x ≡ 1 (mod 35)\nThis means 10x − 35k = 1 for some integers x, k.',
 'An inverse would make ten x congruent to one. Equivalently, ten x minus thirty-five k would equal one for some integers.'),
 ('FIND THE COMMON DIVISOR','Both coefficients share a factor of five','gcd(10, 35) = 5\n10x − 35k = 5(2x − 7k)',
 'Ten and thirty-five have greatest common divisor five. The entire left side is therefore a multiple of five.'),
 ('IDENTIFY THE CONTRADICTION','A multiple of five cannot equal one','5(2x − 7k) = 1 is impossible for integers x, k.',
 'No integer multiple of five equals one. The required equation is impossible, so no inverse exists.'),
 ('USE THE GENERAL CRITERION','Check the greatest common divisor first','a has an inverse modulo m exactly when gcd(a,m)=1.\nHere gcd(10,35)=5, so there is no inverse.',
 'In general, a number has an inverse modulo m exactly when its greatest common divisor with m is one.')],e('3HWa',5),identities=[('10*x-35*k','5*(2*x-7*k)')]),
]
def lessons(doc):
 assert [d for d in range(13,100) if 99%d==3]==[16,24,32,48,96]
 assert all((n-3)*(n-2)%n==6 for n in range(7,100))
 assert not any(10*x%35==1 for x in range(35))
 return make_lessons(SPECS,doc)
