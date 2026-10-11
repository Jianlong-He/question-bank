"""Checked analogous GCD applications in divisibility, measuring and modular powers."""
from math import gcd
from algebra_lessons import authored
from number_theory_lessons import source as e
from card_lessons import make_lessons
SPECS=[
authored('gcf-coprime-divisibility','Use a combination equal to one to cancel a coprime factor',
 'For an integer k, suppose 8 divides 15k.\nUse a linear combination to show that 8 divides k.', '8 divides k',
 'For an integer k, suppose eight divides fifteen k. Use a linear combination to show that eight divides k.',[
 ('COPRIME FACTORS','Eight and fifteen share no factor above one','gcd(8,15) = 1',
 'Eight and fifteen are coprime. This is the condition that allows the cancellation.'),
 ('BUILD ONE','Find an integer combination equal to one','2 × 8 − 15 = 1',
 'Two times eight minus fifteen equals one.'),
 ('MULTIPLY BY k','Keep equality when multiplying every term','2 × 8k − 15k = k',
 'Multiply the identity by k. Two times eight k minus fifteen k equals k.'),
 ('CHECK DIVISIBILITY','Both terms on the left are divisible by eight','8 divides 2 × 8k\n8 divides 15k by the assumption\nTherefore 8 divides k',
 'The first term is divisible by eight, and the second is divisible by eight by assumption. Their difference is therefore divisible by eight, proving the result.')],
 e('Euclidean-division',4,10),equalities=[('2*8-15','1')],identities=[('2*8*k-15*k','k')]),
authored('gcf-jug-measurement','Use GCD and integer combinations in a jug problem',
 'Jugs hold 14 L and 10 L. Find the smallest positive measurable amount.\nExpress it as 14x + 10y, then give a combination for 6 L.', '2 L; x=−2,y=3; for 6 L, x=−6,y=9',
 'Jugs hold fourteen and ten litres. Find the smallest positive measurable amount, express it as fourteen x plus ten y, then give a combination for six litres.',[
 ('FIND THE GCD','Apply Euclidean division','14 = 10 + 4\n10 = 2 × 4 + 2; gcd(14,10) = 2',
 'Euclidean division gives remainders four and two. The greatest common divisor is two litres.'),
 ('FIND COEFFICIENTS','Substitute four equals fourteen minus ten','2 = 10 − 2(14 − 10)\n= −2 × 14 + 3 × 10',
 'Substitute backwards. Two equals negative two times fourteen plus three times ten, so x is negative two and y is three.'),
 ('INTERPRET THE AMOUNT','Three ten-litre fills minus two fourteen-litre removals','30 − 28 = 2 L',
 'With pouring between the jugs, three ten-litre fills and two fourteen-litre removals leave two litres. Every reachable amount is a multiple of two, so no smaller positive amount is possible.'),
 ('SCALE TO THE TARGET','Six litres is three times the GCD','6 = −6 × 14 + 9 × 10\nx=−6, y=9',
 'Multiply the combination by three to reach six litres. The coefficients become negative six and nine. Negative coefficients mean removing water, not negative water.')],
 e('prime-factorization','3HWa',4),equalities=[('14','10+4'),('10','2*4+2'),('-2*14+3*10','2'),('-6*14+9*10','6')]),
authored('gcf-square-tiling','Use the GCD to size square tiles and handle changed dimensions',
 'A courtyard is 90 m by 54 m. Find the largest square tile side.\nExpress the GCD as 90x + 54y. What if the length becomes 99 m?', '18 m; x=−1,y=2; changed side length 9 m',
 'A courtyard is ninety metres by fifty-four metres. Find the largest square tile side and express the greatest common divisor as ninety x plus fifty-four y. Then change the length to ninety-nine metres.',[
 ('DIVIDE BOTH DIMENSIONS','The tile side must divide both lengths','90 = 54 + 36\n54 = 36 + 18; 36 = 2 × 18\nGCD = 18 m',
 'The tile side must divide both dimensions without a remainder. The Euclidean algorithm gives greatest common divisor eighteen, so use eighteen-metre squares.'),
 ('FIND THE COEFFICIENTS','Reverse the remainder equations','18 = 54 − (90 − 54)\n= −90 + 2 × 54\nx=−1, y=2',
 'Substitute backwards to get eighteen equals negative ninety plus twice fifty-four. Thus x is negative one and y is two.'),
 ('CHANGE THE LENGTH','Recompute the GCD for the new pair','99 = 54 + 45\n54 = 45 + 9; 45 = 5 × 9\nNew GCD = 9 m',
 'For ninety-nine by fifty-four, repeat the calculation. The new greatest common divisor is nine.'),
 ('CHECK THE FIT','Both dimensions must contain whole numbers of tile sides','90/18 = 5; 54/18 = 3\n99/9 = 11; 54/9 = 6',
 'The original layout is five by three tiles. The changed layout is eleven by six tiles. Always recompute after a dimension changes.')],
 e('prime-factorization','3HWb',5),equalities=[('90','54+36'),('54','36+18'),('-90+2*54','18'),('99','54+45'),('54','45+9'),('90/18','5'),('99/9','11')]),
authored('gcf-noncoprime-power-cycle','Use a residue cycle when Euler does not apply directly',
 'Find 6⁷ modulo 21.\nCan Euler’s theorem be applied directly?', '6; Euler does not apply directly because gcd(6,21)=3',
 'Find six to the seventh power modulo twenty-one. Can Euler’s theorem be applied directly?',[
 ('CHECK THE CONDITION','Euler requires the base and modulus to be coprime','gcd(6,21) = 3 ≠ 1',
 'The base and modulus share a factor of three. Euler’s theorem cannot be applied directly.'),
 ('COMPUTE SMALL POWERS','Reduce after each multiplication','6¹ ≡ 6\n6² = 36 ≡ 15\n6³ ≡ 15 × 6 = 90 ≡ 6   (mod 21)',
 'The first residues are six, fifteen, then six again. Reduce after every multiplication to keep numbers small.'),
 ('IDENTIFY THE CYCLE','Multiplication by six alternates these two residues','6 → 15 → 6 → 15 → ...\nOdd positive exponents give 6',
 'Multiplying six by six gives residue fifteen, and multiplying fifteen by six gives residue six. The residues alternate, with six at odd exponents.'),
 ('USE THE EXPONENT','Seven is odd','6⁷ ≡ 6 (mod 21)',
 'Seven is odd, so the answer is six. Checking the repeating residues provides a valid method even though the coprimality condition failed.')],
 e('RSA',4,8),equalities=[('6**2%21','15'),('15*6%21','6'),('6**7%21','6')]),
authored('gcf-noncoprime-power-prime-factors','Split a noncoprime modular power into prime moduli',
 'Find 5¹³ modulo 35.\nUse the prime factors 5 and 7 of the modulus.', '5',
 'Find five to the thirteenth power modulo thirty-five, using the prime factors five and seven of the modulus.',[
 ('MODULO FIVE','The power is a multiple of five','5¹³ ≡ 0 (mod 5)',
 'The power is divisible by five, so its remainder modulo five is zero.'),
 ('MODULO SEVEN','Five is coprime to the prime seven','5⁶ ≡ 1 (mod 7)\n5¹³ = (5⁶)² × 5 ≡ 5 (mod 7)',
 'Modulo seven, five is coprime to the modulus. Fermat’s theorem gives five to the sixth congruent to one. The thirteenth power therefore leaves remainder five.'),
 ('COMBINE','Look for a residue with both properties','Multiples of 5 below 35: 0,5,10,15,20,25,30\n5 is the one with remainder 5 modulo 7',
 'Among multiples of five below thirty-five, only five leaves remainder five when divided by seven.'),
 ('WHY IT IS UNIQUE','The two prime factors are coprime','5¹³ ≡ 5 (mod 35)',
 'Both five and seven divide the difference between the power and five, so their product thirty-five divides it. This gives the unique residue five.')],
 e('RSA',4,10),equalities=[('5**13%5','0'),('5**6%7','1'),('5**13%7','5'),('5**13%35','5')]),
authored('gcf-rsa-inverse-condition','Check the correct coprimality condition for an RSA exponent',
 'For a toy RSA example, p=5 and q=17.\nIs e=5 allowed? Find an inverse d modulo ϕ(n).', 'ϕ(n)=64; e=5 is allowed; d=13',
 'For a toy RSA example, the primes are five and seventeen. Is public exponent five allowed, and what inverse d works modulo phi of n?',[
 ('COMPUTE PHI','For two distinct primes, multiply one less than each','n = 5 × 17 = 85\nϕ(n) = 4 × 16 = 64',
 'The modulus is eighty-five, and phi is four times sixteen, which is sixty-four.'),
 ('CHECK THE RIGHT PAIR','The exponent must be coprime to phi','gcd(5,64) = 1',
 'Five and sixty-four are coprime, so five has a modular inverse modulo sixty-four.'),
 ('FIND THE INVERSE','Look for a product one more than a multiple of sixty-four','5 × 13 = 65 = 64 + 1\nd = 13',
 'Five times thirteen equals sixty-five, one more than sixty-four. Therefore thirteen is a valid private exponent for this toy example.'),
 ('INTERPRET THE CONDITION','Sharing a factor with p does not block this inverse','gcd(e,p) = gcd(5,5) = 5\nBut gcd(e,ϕ(n)) = 1, so the inverse exists',
 'Here e shares a factor with p, yet the inverse exists. The required condition concerns e and phi. A common factor above one with phi would prevent a product congruent to one.')],
 e('RSA',5,1),equalities=[('5*17','85'),('4*16','64'),('5*13','65'),('(5*13)%64','1')]),
]
def lessons(doc):return make_lessons(SPECS,doc)
assert gcd(8,15)==1 and gcd(14,10)==2 and gcd(90,54)==18 and gcd(99,54)==9
assert gcd(6,21)==3 and gcd(5,64)==1
assert [v for v in range(35) if v%5==0 and v%7==5]==[5]
