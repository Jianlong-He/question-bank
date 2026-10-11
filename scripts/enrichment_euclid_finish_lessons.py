"""Remaining Euclidean-division methods using fresh integer examples."""
from algebra_lessons import authored
from number_theory_lessons import source as e
from card_lessons import make_lessons

SPECS=[
authored('number-theory-divisibility-remainder','Use Euclidean division to test divisibility',
 'Use Euclidean division to decide\nwhether 14 divides 269.','No; remainder 3',
 'Use Euclidean division to decide whether fourteen divides two hundred sixty-nine.',[
 ('FIND THE QUOTIENT','Choose the largest multiple no greater than the dividend','14 × 19 = 266\n14 × 20 = 280 > 269',
 'Nineteen copies of fourteen make two hundred sixty-six. Twenty copies would be too large.'),
 ('FIND THE REMAINDER','Subtract the largest allowed multiple','269 − 266 = 3\n269 = 14 × 19 + 3',
 'Subtract two hundred sixty-six from two hundred sixty-nine. The remainder is three.'),
 ('CHECK THE DIVISION','The remainder must lie between zero and the divisor','Quotient q = 19, remainder r = 3\n0 ≤ 3 < 14',
 'The quotient is nineteen and the remainder is three. Check that the remainder is nonnegative and smaller than fourteen.'),
 ('DECIDE DIVISIBILITY','A divisor must leave remainder zero','3 ≠ 0, so 14 does not divide 269.\na = bq + r: b divides a exactly when r = 0.',
 'Since the remainder is not zero, fourteen does not divide two hundred sixty-nine. Exact divisibility means a zero remainder.')],e('Euclidean-division',1,5),expression='269%14',value='3',equalities=[('14*19+3','269')]),
authored('number-theory-parity-integer-equation','Read parity restrictions from an integer equation',
 'Integers a, b, c satisfy 4a + bc = 3.\nWhat parity must b and c have?\nMust a be odd or even?','b and c odd; a may be either',
 'Integers a, b, and c satisfy four a plus b c equals three. What parity must b and c have, and must a be odd or even?',[
 ('ISOLATE THE PRODUCT','An odd number minus an even number is odd','bc = 3 − 4a\n4a is even, so bc is odd.',
 'Move four a to the other side. Three minus an even number is odd, so the product b c is odd.'),
 ('REASON ABOUT FACTORS','An even factor would make the product even','An odd product requires both factors odd.\nb is odd and c is odd.',
 'An odd product requires both factors to be odd. If either factor were even, the product would be even.'),
 ('CHECK THE OTHER VARIABLE','Choose b equal to one to construct solutions','Set b = 1 and c = 3 − 4a.\nEvery integer a then gives an integer c.',
 'The parity of a is unrestricted. For any integer a, choose b equal to one and c equal to three minus four a.'),
 ('SHOW BOTH PARITIES','Two valid examples rule out a fixed parity for a','a=1, b=1, c=−1: 4 − 1 = 3\na=2, b=1, c=−5: 8 − 5 = 3',
 'For example, a can be one or two. Both produce valid solutions, so a may be odd or even.')],e('Euclidean-division',4,1),equalities=[('4*1+1*(-1)','3'),('4*2+1*(-5)','3')],identities=[('4*a+(3-4*a)','3')]),
authored('number-theory-bezout-solution-family','Adjust Bezout coefficients to meet sign conditions',
 'Given 9(−3) + 14(2) = 1, find integer solutions\nto 9x + 14y = 1 with y > 0 and with x > 0.\nThen find the inverse of 9 modulo 14.','(-3,2); (11,-7); inverse 11',
 'Given nine times negative three plus fourteen times two equals one, find solutions with positive y and with positive x. Then find the inverse of nine modulo fourteen.',[
 ('START WITH ONE SOLUTION','The supplied identity already has positive y','x = −3, y = 2\n9(−3) + 14(2) = 1',
 'The given solution has x negative three and y two. It already satisfies y greater than zero.'),
 ('SHIFT THE COEFFICIENTS','Add the other coefficient to x and subtract nine from y','x = −3 + 14t, y = 2 − 9t\n9(14t) + 14(−9t) = 0',
 'For any integer t, adding fourteen t to x and subtracting nine t from y keeps the total unchanged.'),
 ('MAKE x POSITIVE','Choose t equal to one','x = 11, y = −7\n9(11) + 14(−7) = 99 − 98 = 1',
 'Choose t equal to one. Then x is eleven and y is negative seven. Their combination still equals one.'),
 ('READ THE MODULAR INVERSE','The multiple of fourteen disappears modulo fourteen','9 × 11 ≡ 1 (mod 14)\nInverse of 9 modulo 14: 11',
 'Modulo fourteen, the term containing fourteen disappears. Nine times eleven leaves remainder one, so eleven is the inverse.')],e('Euclidean-division',4,8),equalities=[('9*(-3)+14*2','1'),('9*11+14*(-7)','1'),('9*11%14','1')],identities=[('9*(-3+14*t)+14*(2-9*t)','1')]),
authored('number-theory-nonnegative-stamp-equation','Solve a stamp equation with nonnegative counts',
 'Stamps cost 23 cents or 14 cents.\nCan you make exactly $1.53?\nFind the number of each stamp.','Yes; 3 at 23 cents and 6 at 14 cents',
 'Stamps cost twenty-three cents or fourteen cents. Can you make exactly one dollar and fifty-three cents? Find the number of each stamp.',[
 ('MODEL IN CENTS','Stamp counts must be nonnegative integers','23x + 14y = 153\nx counts 23-cent stamps; y counts 14-cent stamps.',
 'Work in cents. Write twenty-three x plus fourteen y equals one hundred fifty-three, with nonnegative integer counts.'),
 ('REDUCE MODULO FOURTEEN','The term fourteen y leaves remainder zero','9x ≡ 13 (mod 14)\n9 × 11 ≡ 1 (mod 14)',
 'Reduce modulo fourteen. Nine x is congruent to thirteen. Eleven is the inverse of nine because their product leaves remainder one.'),
 ('USE THE COUNT BOUND','Nonnegative y limits how many expensive stamps fit','x ≡ 11 × 13 ≡ 3 (mod 14)\n0 ≤ x ≤ 6, so x = 3.',
 'Multiply by eleven to get x congruent to three. At most six expensive stamps fit, so x must be three.'),
 ('RECOVER y AND CHECK','Subtract the expensive stamps and divide by fourteen','y = (153 − 23 × 3)/14 = 6\n23 × 3 + 14 × 6 = 153',
 'Subtract the cost of three expensive stamps and divide by fourteen. Six cheaper stamps finish the total. Both counts are nonnegative integers.')],e('Euclidean-division',4,9),expression='(153-23*3)/14',value='6',equalities=[('23*3+14*6','153'),('(11*13)%14','3')]),
]
def lessons(doc):
 assert [(x,y) for x in range(7) for y in range(11) if 23*x+14*y==153]==[(3,6)]
 return make_lessons(SPECS,doc)
