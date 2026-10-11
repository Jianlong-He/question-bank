"""Reviewed linear congruences and Chinese Remainder Theorem examples."""
from algebra_lessons import authored
from number_theory_lessons import source
from card_lessons import make_lessons

def e(w,q):return source('CRT',w,q)
SPECS=[
authored('modular-sum-of-products','Reduce a sum of products modulo a number',
 'Find (18 × 23 + 24 × 29 + 31 × 33) mod 7.','5',
 'Find the remainder of eighteen times twenty-three, plus twenty-four times twenty-nine, plus thirty-one times thirty-three, modulo seven.',[
 ('REDUCE THE FACTORS','Use the same modulus for every term','18 × 23 → 4 × 2\n24 × 29 → 3 × 1; 31 × 33 → 3 × 5',
 'Reduce each factor modulo seven. The three products become four times two, three times one, and three times five.'),
 ('REDUCE EACH PRODUCT','Keep each term small before adding','4 × 2 = 8 ≡ 1\n3 × 1 = 3; 3 × 5 = 15 ≡ 1 (mod 7)',
 'The first product leaves one, the second leaves three, and the third leaves one.'),
 ('ADD THE TERM REMAINDERS','Addition also preserves congruence','1 + 3 + 1 = 5',
 'Add the three term remainders to get five.'),
 ('CHECK THE FINAL RANGE','Reduce the final sum again if needed','0 ≤ 5 < 7\nThe remainder is 5.',
 'Five is less than seven, so it is already the final remainder. If the sum reached seven or more, reduce it again.')],e(1,10),expression='(18*23+24*29+31*33)%7',value='5'),
authored('modular-linear-congruence-family','Solve a linear congruence and apply sign restrictions',
 'Solve 24x ≡ 18 (mod 42) for all integers x.\nFind the smallest positive solution\nand the greatest negative solution.','x = 6 + 7k; smallest positive 6; greatest negative -1',
 'Solve twenty-four x congruent to eighteen modulo forty-two. Find all integer solutions, the smallest positive one, and the greatest negative one.',[
 ('CHECK AND DIVIDE BY THE GCD','Divide the coefficient, right side, and modulus together','gcd(24,42)=6, and 6 divides 18.\n24x ≡ 18 (mod 42) → 4x ≡ 3 (mod 7)',
 'The greatest common divisor is six, which divides eighteen. Divide all three numbers by six to get four x congruent to three modulo seven.'),
 ('MULTIPLY BY AN INVERSE','Two is the inverse of four modulo seven','4 × 2 ≡ 1 (mod 7)\nx ≡ 2 × 3 ≡ 6 (mod 7)',
 'Four times two leaves remainder one modulo seven. Multiply by two to obtain x congruent to six.'),
 ('WRITE EVERY INTEGER SOLUTION','The reduced modulus is the solution spacing','x = 6 + 7k, k any integer\n…, −8, −1, 6, 13, …',
 'All solutions are six plus seven k for integer k. The reduced modulus, seven, is the spacing between solutions.'),
 ('APPLY THE REQUESTED SIGN','Choose from the full solution family','Smallest positive: 6. Greatest negative: −1.\nAll positive solutions: 6 + 7k with k ≥ 0.',
 'Six is the smallest positive solution; negative one is the greatest negative solution. For all positive solutions, restrict k to zero or larger.')],e(2,3),equalities=[('(24*6-18)%42','0'),('(24*(-1)-18)%42','0')],identities=[('24*(6+7*k)-18','42*(3+4*k)')]),
authored('crt-general-solution-period','Solve two congruences and identify the full solution family',
 'Solve x ≡ 2 (mod 5), x ≡ 4 (mod 9).\nGive the full family and the solution\nimmediately below the smallest positive one.','x = 22 + 45k; previous solution -23',
 'Solve x congruent to two modulo five and four modulo nine. Give the full solution family and the solution immediately below the smallest positive one.',[
 ('SUBSTITUTE ONE CONDITION','Every solution of the first has this form','x = 5a + 2\n5a + 2 ≡ 4 (mod 9) → 5a ≡ 2 (mod 9)',
 'Write x as five a plus two. Substitute into the second condition to get five a congruent to two modulo nine.'),
 ('FIND THE FIRST REPRESENTATIVE','Two is the inverse of five modulo nine','a ≡ 2 × 2 ≡ 4 (mod 9)\nx = 5 × 4 + 2 = 22',
 'Two is the inverse of five modulo nine. This gives a congruent to four, and the representative x equal to twenty-two.'),
 ('FIND AND CHECK THE TRUE PERIOD','A difference of two solutions is divisible by both moduli','LCM(5,9)=45; x = 22 + 45k, k an integer\n22 mod 5 = 2; 22 mod 9 = 4',
 'Solutions differ by multiples of both five and nine, so the period is their least common multiple, forty-five. Twenty-two passes both remainder checks.'),
 ('MOVE THROUGH THE SOLUTION FAMILY','Check both the starting value and the period','Smallest positive: 22. Previous: 22 − 45 = −23.\nA correct representative with a wrong period is not enough.',
 'Twenty-two is the smallest positive solution. Subtract forty-five to get negative twenty-three, the previous solution. A proposed general solution needs both the correct representative and period.')],e(3,6),equalities=[('22%5','2'),('22%9','4'),('(-23)%5','2'),('(-23)%9','4')]),
authored('crt-three-congruences-range','Solve three congruences within a stated interval',
 'Find N with 100 < N < 250, where\nN mod 5 = 2, N mod 8 = 3,\nand N mod 9 = 7.','187',
 'Find N between one hundred and two hundred fifty, with remainders two, three, and seven when divided by five, eight, and nine.',[
 ('COMBINE THE FIRST TWO CONDITIONS','Write N from the modulus-five condition','N = 5a + 2; 5a ≡ 1 (mod 8)\na ≡ 5 (mod 8), so N = 27 + 40b.',
 'Write N as five a plus two. Modulo eight, five a is one, so a is five modulo eight. Thus N is twenty-seven plus forty b.'),
 ('APPLY THE THIRD CONDITION','Reduce the combined family modulo nine','27 + 40b ≡ 7 (mod 9)\n4b ≡ 7; b ≡ 7 × 7 ≡ 4 (mod 9)',
 'Modulo nine, this becomes four b congruent to seven. The inverse of four is seven, so b is four modulo nine.'),
 ('USE THE SOLUTION PERIOD AND RANGE','Substitute b = 4 + 9k','N = 187 + 360k\nAdjacent values: −173, 187, 547',
 'Substitution gives N equal to one hundred eighty-seven plus three hundred sixty k. The adjacent values show that only one hundred eighty-seven fits the interval.'),
 ('VERIFY EVERY ORIGINAL CONDITION','All three remainders and both bounds must hold','187 mod 5 = 2; mod 8 = 3; mod 9 = 7\n100 < 187 < 250',
 'Check all three divisions and the bounds. Every condition holds, so the unique answer in the interval is one hundred eighty-seven.')],e(4,8),equalities=[('187%5','2'),('187%8','3'),('187%9','7')],identities=[('27+40*(4+9*k)','187+360*k')]),
]
def lessons(doc):
 assert [x for x in range(1,43) if (24*x-18)%42==0]==[6,13,20,27,34,41]
 assert [x for x in range(45) if x%5==2 and x%9==4]==[22]
 assert [x for x in range(101,250) if x%5==2 and x%8==3 and x%9==7]==[187]
 return make_lessons(SPECS,doc)
