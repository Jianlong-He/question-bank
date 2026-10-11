"""Authored algebra lessons with exact identities, roots, and numeric checks.

Source references select an appropriate grade/unit for the shared export. They do
not certify the suitability of every automatically grouped worksheet link.
"""
from card_lessons import spec, make_lessons


def authored(vid, topic, question, answer, opening, steps, source,
             identities=(), equation=None, equalities=(), expression=None, value=None):
    lesson = spec(vid, topic, question, answer, expression, value, opening, steps, equalities)
    lesson['source_ref'] = source
    lesson['identities'] = identities
    if equation:
        lesson['linear_equation'] = equation
    return lesson


SPECS = [
authored('algebra-combine-like-terms', 'Combining like terms',
 'Simplify 7x + 11 − 3x + 5.', '4x + 16',
 "Let's simplify seven x plus eleven, minus three x, plus five. Keep the variable terms separate from the constants.", [
 ('SORT', 'Match terms with the same variable part', '(7x − 3x) + (11 + 5)',
  'Seven x and negative three x are like terms. Eleven and five are constants, so they form another group.'),
 ('VARIABLE TERMS', 'Subtract the coefficients', '7x − 3x = (7 − 3)x = 4x',
  'Subtract the coefficients: seven minus three is four. The variable part stays x.'),
 ('CONSTANTS', 'Add the numbers', '11 + 5 = 16\n7x + 11 − 3x + 5 = 4x + 16',
  'Eleven plus five is sixteen. The simplified expression is four x plus sixteen.'),
 ('FINISH', 'Unlike terms stay separate', '4x + 16',
  'Four x and sixteen are not like terms, so we cannot combine them any further.')],
 ('worksheets/Grade 6/G6Unit 6/G6U6W12.csv', '5'),
 identities=[('7*x+11-3*x+5','4*x+16')]),

authored('algebra-distributive', 'The distributive property',
 'Expand 4(3x − 7).', '12x − 28',
 "Let's expand four times the quantity three x minus seven. The outside factor multiplies every term inside.", [
 ('DISTRIBUTE', 'Multiply both terms by 4', '4(3x − 7) = 4 × 3x − 4 × 7',
  'Multiply four by three x, and multiply four by negative seven.'),
 ('FIRST PRODUCT', 'Multiply the coefficients', '4 × 3x = 12x',
  'Four times three x is twelve x.'),
 ('SECOND PRODUCT', 'Keep the subtraction sign', '4 × (−7) = −28\n4(3x − 7) = 12x − 28',
  'Four times negative seven is negative twenty-eight. The expanded expression is twelve x minus twenty-eight.'),
 ('CHECK', 'Factor out the common 4', '12x − 28 = 4(3x − 7)',
  'Factor four out of both terms. We recover the original expression, which checks our distribution.')],
 ('worksheets/Grade 9/G9Unit 1/G9U1W2.csv', '3'),
 identities=[('4*(3*x-7)','12*x-28')]),

authored('algebra-evaluate', 'Substituting values',
 'Evaluate 3a² − 2b\nwhen a = −2 and b = 5.', '2',
 "Let's evaluate three a squared minus two b, when a is negative two and b is five.", [
 ('SUBSTITUTE', 'Replace each variable with its value', '3(−2)² − 2(5)',
  'Put negative two in parentheses wherever a appears. Replace b with five.'),
 ('POWERS FIRST', 'Square the entire negative number', '(−2)² = 4\n3(4) − 2(5)',
  'Negative two squared is positive four. Evaluate the power before multiplying by three.'),
 ('MULTIPLY', 'Complete both products', '12 − 10',
  'Three times four is twelve, and two times five is ten.'),
 ('SUBTRACT', 'Finish the calculation', '12 − 10 = 2',
  'Twelve minus ten is two. The expression has value two for these given values.')],
 ('worksheets/Grade 6/G6Unit 6/G6U6W2.csv', '8'),
 expression='3*(-2)**2-2*5', value='2', equalities=[('(-2)**2','4')]),

authored('algebra-rearrange-formula', 'Rearranging a formula',
 'Make t the subject:\nW = 3rt + 8, where r ≠ 0.', 't = (W − 8)/(3r), r ≠ 0',
 "Let's make t the subject of W equals three r t plus eight. We are told r is not zero.", [
 ('UNDO ADDITION', 'Subtract 8 from both sides', 'W − 8 = 3rt',
  'Subtract eight from both sides. This leaves three r times t on the right.'),
 ('UNDO MULTIPLICATION', 'Divide both sides by 3r', '(W − 8)/(3r) = t',
  'Divide both sides by three r. This is allowed because r is not zero.'),
 ('REWRITE', 'Put the subject on the left', 't = (W − 8)/(3r)',
  'Write t on the left. The entire quantity W minus eight belongs in the numerator.'),
 ('CHECK', 'Substitute back into the formula', '3r × [(W − 8)/(3r)] + 8\n= W − 8 + 8 = W',
  'Substitute the result back. The factor three r cancels, then subtracting and adding eight leaves W.')],
 ('worksheets/Grade 6/G6Unit 7/G6U7W8.csv', '2'),
 identities=[('3*r*t+8-8','3*r*t'), ('W-8+8','W')],
 equalities=[('3*2*((44-8)/(3*2))+8','44')]),

authored('linear-equations-solve-one-side', 'Solving a two-step equation',
 'Solve 5x − 9 = 61.', 'x = 14',
 "Let's solve five x minus nine equals sixty-one. Undo the operations in reverse order.", [
 ('ADD', 'Add 9 to both sides', '5x − 9 + 9 = 61 + 9\n5x = 70',
  'Add nine to both sides. Five x is seventy.'),
 ('DIVIDE', 'Divide both sides by 5', '5x/5 = 70/5\nx = 14',
  'Divide both sides by five. The solution is x equals fourteen.'),
 ('SUBSTITUTE', 'Use the original equation', '5(14) − 9 = 70 − 9',
  'Check by substituting fourteen into the original equation. Five times fourteen minus nine is seventy minus nine.'),
 ('CHECK', 'Both sides match', '61 = 61\nx = 14',
  'Both sides equal sixty-one, so fourteen is correct.')],
 ('worksheets/Grade 7/G7Unit 6/G7U6W3.csv', '2'),
 equation=('5*x-9','61','x','14'), equalities=[('5*14-9','61')]),

authored('linear-equations-solve-both-sides', 'Variables on both sides',
 'Solve 7x − 5 = 3x + 39.', 'x = 11',
 "Let's solve seven x minus five equals three x plus thirty-nine. Collect the variable terms on one side.", [
 ('COLLECT VARIABLES', 'Subtract 3x from both sides', '7x − 3x − 5 = 39\n4x − 5 = 39',
  'Subtract three x from both sides. That leaves four x minus five equals thirty-nine.'),
 ('COLLECT NUMBERS', 'Add 5 to both sides', '4x = 44',
  'Add five to both sides. Four x equals forty-four.'),
 ('ISOLATE', 'Divide both sides by 4', 'x = 44/4 = 11',
  'Divide by four. The solution is x equals eleven.'),
 ('CHECK', 'Evaluate both original sides', '7(11) − 5 = 72\n3(11) + 39 = 72',
  'Substitute eleven. The left side is seventy-two and the right side is also seventy-two.')],
 ('worksheets/Grade 8/G8Unit 2/G8U2W3.csv', '10'),
 equation=('7*x-5','3*x+39','x','11'), equalities=[('7*11-5','3*11+39')]),

authored('linear-equations-solve-parentheses', 'Equations with parentheses',
 'Solve 3(2x − 5) = 51.', 'x = 11',
 "Let's solve three times the quantity two x minus five equals fifty-one. Start by expanding the parentheses.", [
 ('EXPAND', 'Distribute the 3 to both terms', '6x − 15 = 51',
  'Three times two x is six x. Three times negative five is negative fifteen.'),
 ('ADD', 'Add 15 to both sides', '6x = 66',
  'Add fifteen to both sides. Six x equals sixty-six.'),
 ('DIVIDE', 'Divide both sides by 6', 'x = 66/6 = 11',
  'Divide by six to get x equals eleven.'),
 ('CHECK', 'Check inside the original parentheses', '3(2 × 11 − 5)\n= 3 × 17 = 51',
  'In the original equation, two times eleven minus five is seventeen. Three times seventeen is fifty-one.')],
 ('worksheets/Grade 7/G7Unit 6/G7U6W3.csv', '6'),
 equation=('3*(2*x-5)','51','x','11'), identities=[('3*(2*x-5)','6*x-15')],
 equalities=[('3*(2*11-5)','51')]),

authored('absolute-value-equations', 'An absolute-value constant in an equation',
 'Solve −x + |−23| = −48.', 'x = 71',
 "Let's solve negative x plus the absolute value of negative twenty-three equals negative forty-eight.", [
 ('ABSOLUTE VALUE', 'Find the distance from zero', '|−23| = 23\n−x + 23 = −48',
  'The absolute value of negative twenty-three is positive twenty-three, its distance from zero.'),
 ('SUBTRACT', 'Subtract 23 from both sides', '−x = −48 − 23 = −71',
  'Subtract twenty-three from both sides. Negative x equals negative seventy-one.'),
 ('DIVIDE', 'Divide both sides by −1', 'x = 71',
  'Divide both sides by negative one. This gives x equals positive seventy-one.'),
 ('CHECK', 'Substitute into the original equation', '−71 + |−23|\n= −71 + 23 = −48',
  'Check the original equation. Negative seventy-one plus twenty-three is negative forty-eight.')],
 ('worksheets/Grade 7/G7Unit 6/G7U6W4.csv', '1'),
 equation=('-x+abs(-23)','-48','x','71'), identities=[('abs(-23)','23')],
 equalities=[('-71+23','-48')]),

authored('absolute-value-evaluation', 'Finding absolute value',
 'Find |−37|.', '37',
 "Let's find the absolute value of negative thirty-seven. Absolute value means distance from zero.", [
 ('MEANING', 'Read the bars as absolute value', '|−37| = distance from −37 to 0',
  'The two vertical bars ask for the distance from negative thirty-seven to zero.'),
 ('DISTANCE', 'Count the distance, without direction', '−37 is 37 units from 0.',
  'Negative thirty-seven lies thirty-seven units to the left of zero.'),
 ('ANSWER', 'Distance is never negative', '|−37| = 37',
  'The distance is thirty-seven. Absolute value is never negative.'),
 ('CHECK', 'Opposite numbers have equal distances', '|37| = |−37| = 37',
  'Positive thirty-seven is the same distance from zero, so its absolute value is also thirty-seven.')],
 ('worksheets/Grade 6/G6Unit 5/G6U5W3.csv', '1'),
 identities=[('abs(-37)','37'),('abs(37)','37')]),

authored('rational-expressions-simplify', 'Simplifying a rational expression',
 'Simplify (x² − 121)/(x − 11).', 'x + 11, with x ≠ 11',
 "Let's simplify x squared minus one hundred twenty-one, divided by x minus eleven.", [
 ('RESTRICTION', 'The original denominator cannot be zero', 'x − 11 ≠ 0\nx ≠ 11',
  'First record the restriction. X cannot be eleven because that would make the original denominator zero.'),
 ('FACTOR', 'Use a difference of squares', 'x² − 121 = (x − 11)(x + 11)',
  'One hundred twenty-one is eleven squared. Factor the numerator as x minus eleven times x plus eleven.'),
 ('CANCEL FACTORS', 'Cancel the common nonzero factor', '[(x − 11)(x + 11)]/(x − 11)\n= x + 11,   x ≠ 11',
  'Cancel the common factor x minus eleven. Keep the restriction with the simplified answer.'),
 ('CHECK', 'Try an allowed value: x = 12', '(144 − 121)/(12 − 11) = 23\n12 + 11 = 23',
  'At x equals twelve, both forms give twenty-three. Remember, eleven is still excluded.')],
 ('worksheets/Grade 11/G11Unit 13/G11U13W1.csv', '3'),
 identities=[('x**2-121','(x-11)*(x+11)')],
 equalities=[('(12**2-121)/(12-11)','12+11')]),

authored('rational-equations', 'Solving a rational equation',
 'Solve 3/x + 1/4 = 1/2.', 'x = 12',
 "Let's solve three over x plus one quarter equals one half. X must not be zero.", [
 ('RESTRICTION', 'Keep the denominator nonzero', 'x ≠ 0',
  'Zero is excluded because three divided by zero is undefined.'),
 ('CLEAR DENOMINATORS', 'Multiply every term by 4x', '12 + x = 2x',
  'Multiply every term by four x. Three over x becomes twelve, one quarter becomes x, and one half becomes two x.'),
 ('SOLVE', 'Subtract x from both sides', '12 = x\nx = 12',
  'Subtract x from both sides. X equals twelve, which is allowed by the restriction.'),
 ('CHECK', 'Substitute into the original equation', '3/12 + 1/4\n= 1/4 + 1/4 = 1/2',
  'Three twelfths plus one quarter is one half. Twelve satisfies the original equation.')],
 ('worksheets/Grade 11/G11Unit 7/G11U7W1.csv', '4'),
 equation=('12+x','2*x','x','12'), equalities=[('3/12+1/4','1/2')]),

authored('factoring-polynomials', 'Factoring a quadratic trinomial',
 'Factor x² + 13x + 36.', '(x + 4)(x + 9)',
 "Let's factor x squared plus thirteen x plus thirty-six. The coefficient of x squared is one.", [
 ('FIND TWO NUMBERS', 'Their product is 36 and sum is 13', '4 × 9 = 36\n4 + 9 = 13',
  'Look for two numbers whose product is thirty-six and whose sum is thirteen. Four and nine work.'),
 ('WRITE FACTORS', 'Use those numbers in the binomials', 'x² + 13x + 36 = (x + 4)(x + 9)',
  'Put four and nine into the two factors: x plus four, times x plus nine.'),
 ('EXPAND TO CHECK', 'Multiply every term', '(x + 4)(x + 9)\n= x² + 9x + 4x + 36',
  'Expand to check. We get x squared plus nine x plus four x plus thirty-six.'),
 ('COMBINE', 'Recover the original polynomial', 'x² + 13x + 36',
  'Nine x plus four x is thirteen x. The expansion matches our original polynomial.')],
 ('worksheets/Grade 10/G10Unit 2/G10U2W2.csv', '3'),
 identities=[('x**2+13*x+36','(x+4)*(x+9)')],
 equalities=[('4*9','36'),('4+9','13')]),

authored('factoring-grouping', 'Factoring by grouping',
 'Factor 2x² + 10x + 7x + 35.', '(x + 5)(2x + 7)',
 "Let's factor two x squared plus ten x plus seven x plus thirty-five, using grouping.", [
 ('GROUP', 'Make two pairs of terms', '(2x² + 10x) + (7x + 35)',
  'Group the first two terms and the last two terms.'),
 ('FACTOR EACH PAIR', 'Take out each common factor', '2x(x + 5) + 7(x + 5)',
  'Factor two x from the first pair and seven from the second. Both groups now contain x plus five.'),
 ('FACTOR AGAIN', 'Take out the shared binomial', '(x + 5)(2x + 7)',
  'Treat x plus five as one common factor. The remaining factor is two x plus seven.'),
 ('CHECK', 'Distribute to recover all four terms', '(x + 5)(2x + 7)\n= 2x² + 7x + 10x + 35',
  'Expand the result. We recover the same four terms, so the factorization is correct.')],
 ('worksheets/Grade 10/G10Unit 2/G10U2W2.csv', '6'),
 identities=[('2*x**2+10*x+7*x+35','2*x*(x+5)+7*(x+5)'),
             ('2*x**2+10*x+7*x+35','(x+5)*(2*x+7)')]),
]


def lessons(doc):
    return make_lessons(SPECS, doc)
