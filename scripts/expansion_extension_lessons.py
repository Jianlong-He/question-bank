"""Expansion with two variables, cubes, imaginary units and fractional factors."""
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons
SPECS=[
authored('expand-square-two-variables','Square a binomial with two variable terms',
 'Expand (5p − 2q)².\nHow does the result change for (5p + 2q)²?', '25p² − 20pq + 4q²; 25p² + 20pq + 4q²',
 'Expand five p minus two q squared. Then consider five p plus two q squared.',[
 ('MULTIPLY TWO COPIES','Every term multiplies both terms in the other bracket','(5p − 2q)(5p − 2q)',
 'Write the square as two identical factors. Every term in the first factor multiplies both terms in the second.'),
 ('FORM FOUR PRODUCTS','The middle products each contain both variables','25p² − 10pq − 10pq + 4q²',
 'The products are twenty-five p squared, negative ten p q twice, and positive four q squared.'),
 ('COMBINE AND COMPARE','Changing to a plus sign changes the two cross products','Minus: 25p² − 20pq + 4q²\nPlus: 25p² + 20pq + 4q²',
 'Combine the middle terms. The minus case has negative twenty p q. For the plus case, both cross products become positive, giving positive twenty p q.'),
 ('GENERAL PATTERN','Square both terms and include twice their product','(A + B)² = A² + 2AB + B²\n(A − B)² = A² − 2AB + B²',
 'The general rule is the first square, plus or minus twice the product, plus the second square. Do not omit the middle term.')],
 g(11,2,3,7),identities=[('(5*p-2*q)**2','25*p**2-20*p*q+4*q**2'),('(5*p+2*q)**2','25*p**2+20*p*q+4*q**2')]),
authored('expand-binomial-cube','Expand a cubed binomial using repeated multiplication',
 'Expand (x + 3)³.', 'x³ + 9x² + 27x + 27',
 'Expand x plus three cubed. A cube means three identical factors.',[
 ('SQUARE TWO FACTORS','Begin with two copies of x plus three','(x + 3)³ = (x + 3)²(x + 3)\n(x + 3)² = x² + 6x + 9',
 'First multiply two copies of x plus three. That gives x squared plus six x plus nine.'),
 ('MULTIPLY BY THE THIRD','Distribute both x and three across the trinomial','x(x² + 6x + 9) + 3(x² + 6x + 9)',
 'Now multiply the trinomial by the remaining factor. Distribute x across all three terms, then distribute three.'),
 ('WRITE SIX PRODUCTS','Keep like powers together','x³ + 6x² + 9x + 3x² + 18x + 27',
 'This produces x cubed, six x squared, nine x, three x squared, eighteen x, and twenty-seven.'),
 ('COMBINE','Add coefficients of matching powers','x³ + 9x² + 27x + 27',
 'Combine the x squared terms to get nine x squared, and the x terms to get twenty-seven x. The expansion is x cubed plus nine x squared plus twenty-seven x plus twenty-seven.')],
 g(12,9,3,3),identities=[('(x+3)**2','x**2+6*x+9'),('(x+3)**3','x**3+9*x**2+27*x+27')]),
authored('expand-imaginary-conjugates','Use the imaginary-unit rule when expanding conjugate factors',
 'Expand (x − 4i)(x + 4i), where i² = −1.', 'x² + 16',
 'Expand x minus four i times x plus four i, where i squared equals negative one.',[
 ('MULTIPLY','Distribute all four products','x² + 4ix − 4ix − 16i²',
 'The four products are x squared, positive four i x, negative four i x, and negative sixteen i squared.'),
 ('CANCEL','The imaginary cross terms are opposites','4ix − 4ix = 0\nx² − 16i²',
 'The cross terms cancel, leaving x squared minus sixteen i squared.'),
 ('USE THE DEFINITION','Replace i squared with negative one','x² − 16(−1) = x² + 16',
 'Replace i squared by negative one. Subtracting sixteen times negative one adds sixteen.'),
 ('CHECK THE SIGN','The final constant is positive','(x − 4i)(x + 4i) = x² + 16',
 'The result is x squared plus sixteen. The matching sum-and-difference pattern still works; the extra sign change comes from i squared being negative one.')],
 g(12,3,2,9),identities=[('(x-4*i)*(x+4*i)','x**2-16*i**2')],equalities=[('-16*(-1)','16')]),
authored('expand-numerical-brackets','Rewrite numerical brackets with the distributive property',
 'Distribute in 6(8 + 5) and 4(7 − 9) + 11.\nKeep the products visible before evaluating.', '6 × 8 + 6 × 5 = 78; 4 × 7 − 4 × 9 + 11 = 3',
 'Distribute in six times eight plus five, and four times seven minus nine plus eleven. Keep the products visible before evaluating.',[
 ('SUM IN BRACKETS','The factor multiplies both terms','6(8 + 5) = 6 × 8 + 6 × 5',
 'For the first expression, multiply six by eight and by five. The two products stay connected by a plus sign.'),
 ('DIFFERENCE IN BRACKETS','The minus sign stays with the second product','4(7 − 9) + 11 = 4 × 7 − 4 × 9 + 11',
 'For the second expression, multiply four by seven and by nine. Keep the subtraction sign. The eleven is outside the brackets, so it stays unchanged.'),
 ('EVALUATE IF REQUESTED','Multiply before adding and subtracting','48 + 30 = 78\n28 − 36 + 11 = 3',
 'The first expression evaluates to seventy-eight. The second evaluates to three. If only an expanded form is requested, give the product expression.'),
 ('CHECK','Evaluating the original brackets gives the same values','6 × 13 = 78\n4 × (−2) + 11 = 3',
 'Check by evaluating inside the original brackets. Both methods agree. Distribute only the factor attached to that bracket.')],
 g(6,6,10,6),equalities=[('6*(8+5)','6*8+6*5'),('4*(7-9)+11','4*7-4*9+11'),('6*(8+5)','78'),('4*(7-9)+11','3')]),
authored('expand-fractional-factor','Multiply every term by a fractional factor',
 'Expand and simplify (2/3)(9a − 6b + 12).', '6a − 4b + 8',
 'Expand and simplify two thirds times nine a minus six b plus twelve.',[
 ('DISTRIBUTE','Multiply every term, including its sign','(2/3)(9a) + (2/3)(−6b) + (2/3)(12)',
 'Multiply all three terms by two thirds. Keep the negative sign attached to six b.'),
 ('FIRST TWO TERMS','Divide by three and then multiply by two','(2/3)(9a) = 6a\n(2/3)(−6b) = −4b',
 'Nine divided by three is three, then times two gives six a. Negative six divided by three is negative two, then times two gives negative four b.'),
 ('CONSTANT','Use the same fractional factor on twelve','(2/3)(12) = 8',
 'Twelve divided by three is four, and four times two is eight.'),
 ('COLLECT','Unlike variable terms remain separate','6a − 4b + 8',
 'The result is six a minus four b plus eight. These are unlike terms, so leave them separate. Every term received the same fractional factor.')],
 g(6,6,11,5),identities=[('(2/3)*(9*a-6*b+12)','6*a-4*b+8')]),
]
assert (7-4j)*(7+4j)==7**2+16

def lessons(doc):return make_lessons(SPECS,doc)
