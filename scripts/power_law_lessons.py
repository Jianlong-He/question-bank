"""Exponent laws, scientific products, and a factored enrichment ratio."""
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons
SPECS=[
authored('power-scientific-product','Multiply numbers in scientific notation',
 'Multiply (4 × 10³)(6 × 10²).\nGive the answer in scientific notation.', '2.4 × 10⁶',
 'Multiply four times ten cubed by six times ten squared. Give the answer in scientific notation.',[
 ('COEFFICIENTS','Multiply the ordinary number parts','4 × 6 = 24',
 'Multiply the coefficients, four and six, to get twenty-four.'),
 ('POWERS OF TEN','Add exponents when multiplying the same base','3 + 2 = 5\n10³ × 10² = 10⁵',
 'For powers with the same base, multiplication adds the exponents. Ten cubed times ten squared is ten to the fifth.'),
 ('COMBINE','Attach the product of the powers','24 × 10⁵',
 'Combine the results to get twenty-four times ten to the fifth.'),
 ('NORMALIZE','The coefficient must be at least one and less than ten','24 × 10⁵ = 2.4 × 10 × 10⁵\n= 2.4 × 10⁶',
 'Twenty-four is too large for a scientific-notation coefficient. Write it as two point four times ten. That extra ten increases the exponent to six. The final answer is two point four times ten to the sixth.')],
 g(8,1,4,2),equalities=[('(4*10**3)*(6*10**2)','2.4*10**6'),('10**3*10**2','10**5'),('24*10**5','2.4*10**6')]),
authored('power-same-base-product-quotient','Combine products and quotients of the same base',
 'Simplify (5² × 5⁴)/5³.', '5³ = 125',
 'Simplify five squared times five to the fourth, divided by five cubed.',[
 ('MULTIPLY SAME BASE','Add the numerator exponents','2 + 4 = 6\n5² × 5⁴ = 5⁶',
 'The numerator has two powers with the same base. Add their exponents: two plus four gives six.'),
 ('DIVIDE SAME BASE','Subtract the denominator exponent','6 − 3 = 3\n5⁶/5³ = 5³',
 'Dividing powers of the same nonzero base subtracts exponents. Six minus three is three.'),
 ('EVALUATE','Five cubed means three factors of five','5³ = 5 × 5 × 5 = 125',
 'Five cubed is five times five times five, or one hundred twenty-five.'),
 ('CHECK THE FACTORS','Three of the six numerator factors cancel','(5 × 5 × 5 × 5 × 5 × 5)/(5 × 5 × 5)\n= 5 × 5 × 5 = 125',
 'There are six factors of five on top and three below. Cancel three matching factors, leaving three on top. This confirms one hundred twenty-five.')],
 g(8,1,4,4),equalities=[('(5**2*5**4)/(5**3)','125'),('5**2*5**4','5**6'),('5**6/5**3','5**3')]),
authored('power-common-exponent-product','Combine factors raised to the same exponent',
 'Simplify 3² × 4².', '144',
 'Simplify three squared times four squared. Both factors have the same exponent.',[
 ('EXPAND THE POWERS','Each square contains two equal factors','3² × 4² = (3 × 3)(4 × 4)',
 'Expand each square into two factors. We have two threes and two fours.'),
 ('REGROUP THE FACTORS','Pair each three with a four','(3 × 3)(4 × 4) = (3 × 4)(3 × 4)',
 'Reorder and regroup the multiplication so each three pairs with a four.'),
 ('COMBINE THE BASES','Keep the shared exponent','(3 × 4)(3 × 4) = 12²',
 'Each pair makes twelve. The product is twelve squared. When multiplying powers with the same exponent, we can multiply the bases and keep that exponent.'),
 ('ANSWER AND CHECK','Compare with evaluating the original squares','12² = 144\n3² × 4² = 9 × 16 = 144',
 'Twelve squared is one hundred forty-four. Checking the original squares gives nine times sixteen, also one hundred forty-four.')],
 g(8,1,5,7),equalities=[('3**2*4**2','144'),('(3*4)**2','144'),('9*16','144')]),
authored('power-factor-ratio-enrichment','Factor shared powers before simplifying a large ratio',
 'Simplify (3¹² + 3¹⁰)/(3¹³ − 3¹¹)\nusing prime-power factors.', '5/12',
 'Simplify three to the twelfth plus three to the tenth, divided by three to the thirteenth minus three to the eleventh. Use common factors.',[
 ('FACTOR THE NUMERATOR','Take out the smaller power of three','3¹² + 3¹⁰ = 3¹⁰(3² + 1) = 3¹⁰ × 10',
 'Take three to the tenth out of the numerator. The remaining bracket is three squared plus one, which equals ten.'),
 ('FACTOR THE DENOMINATOR','Again take out the smaller power','3¹³ − 3¹¹ = 3¹¹(3² − 1) = 3¹¹ × 8',
 'Take three to the eleventh out of the denominator. The remaining bracket is three squared minus one, or eight.'),
 ('CANCEL A COMMON FACTOR','Cancel three to the tenth from top and bottom','(3¹⁰ × 10)/(3¹¹ × 8)\n= 10/(3 × 8) = 10/24',
 'Cancel the common factor three to the tenth. One factor of three remains in the denominator, leaving ten over twenty-four.'),
 ('REDUCE','Divide numerator and denominator by two','10/24 = 5/12',
 'Divide both parts by two to obtain five twelfths. Factoring first avoids evaluating large powers. Only common factors can cancel; separate terms of a sum cannot.')],
 ('worksheets/enrichment/number-theory 1/U2prime-factorization/E-NT1U2W3HWb.csv','3'),
 equalities=[('(3**12+3**10)/(3**13-3**11)','5/12'),('3**12+3**10','3**10*10'),('3**13-3**11','3**11*8'),('10/24','5/12')]),
]
def lessons(doc):return make_lessons(SPECS,doc)
