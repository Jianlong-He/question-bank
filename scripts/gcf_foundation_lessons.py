"""Greatest common factors in prime factors, algebra, and candidate constraints."""
from algebra_lessons import authored
from number_sense_lessons import source as g
from number_theory_lessons import source as e
from card_lessons import make_lessons
SPECS=[
authored('gcf-monomials','Find the greatest common factor of monomials',
 'Find the GCF of 28x⁴y² and 42x²y⁵.', '14x²y²',
 'Find the greatest common factor of twenty-eight x to the fourth y squared, and forty-two x squared y to the fifth.',[
 ('COEFFICIENTS','Find the greatest common factor of the numbers','28 = 2² × 7; 42 = 2 × 3 × 7\nGCF(28, 42) = 14',
 'First find the coefficient greatest common factor. Twenty-eight and forty-two share two times seven, or fourteen.'),
 ('COMMON X FACTOR','Use the smaller exponent','x⁴ and x² share x²',
 'Both terms contain x. Take the smaller exponent, two, so the common x factor is x squared.'),
 ('COMMON Y FACTOR','Again use the smaller exponent','y² and y⁵ share y²',
 'For y, the smaller exponent is also two. The common y factor is y squared. Include only variables present in both terms.'),
 ('COMBINE AND CHECK','Multiply the common numerical and variable factors','GCF = 14x²y²\n28x⁴y² = 14x²y²(2x²)\n42x²y⁵ = 14x²y²(3y³)',
 'Combine the factors to get fourteen x squared y squared. Dividing it out leaves two x squared and three y cubed, with no additional common factor.')],
 g(10,2,1,10),equalities=[('2**2*7','28'),('2*3*7','42')],identities=[('14*x**2*y**2*(2*x**2)','28*x**4*y**2'),('14*x**2*y**2*(3*y**3)','42*x**2*y**5')]),
authored('gcf-factor-number-expression','Factor a numerical sum or difference using the GCF',
 'Factor 42 + 63 and 70 − 28.\nUse the GCF as the outside factor in each expression.', '21(2 + 3); 14(5 − 2)',
 'Factor forty-two plus sixty-three, and seventy minus twenty-eight. Use the greatest common factor as the outside factor in each expression.',[
 ('FIRST COMMON FACTOR','Forty-two and sixty-three share twenty-one','42 = 21 × 2; 63 = 21 × 3',
 'The greatest common factor of forty-two and sixty-three is twenty-one. The remaining factors are two and three.'),
 ('FACTOR THE SUM','Put the GCF outside; keep addition inside','42 + 63 = 21(2 + 3)',
 'Place twenty-one outside parentheses, with two plus three inside.'),
 ('FACTOR THE DIFFERENCE','Seventy and twenty-eight share fourteen','70 = 14 × 5; 28 = 14 × 2\n70 − 28 = 14(5 − 2)',
 'For the difference, the greatest common factor is fourteen. Divide both terms by fourteen, leaving five minus two inside parentheses.'),
 ('EXPAND TO CHECK','Multiply the outside factor by every inside term','21(2 + 3) = 42 + 63\n14(5 − 2) = 70 − 28',
 'Distribute the outside factor to check. Preserve the operation and the term order, especially for subtraction.')],
 g(6,6,10,1),equalities=[('42+63','21*(2+3)'),('70-28','14*(5-2)')]),
authored('gcf-factor-linear-expression','Factor a common numerical factor from every term',
 'Factor 28m + 42n + 70 using the GCF.', '14(2m + 3n + 5)',
 'Factor twenty-eight m plus forty-two n plus seventy using the greatest common factor.',[
 ('FIND THE COMMON NUMBER','Find a factor shared by all three coefficients','28 = 14 × 2; 42 = 14 × 3\n70 = 14 × 5',
 'The coefficient greatest common factor is fourteen. It divides twenty-eight, forty-two, and seventy.'),
 ('CHECK VARIABLES','No variable appears in every term','28m, 42n, 70\nCommon factor: 14 only',
 'There is no common variable because the last term is a constant, and the other terms use different variables.'),
 ('DIVIDE EVERY TERM','Keep the remaining terms inside parentheses','28m + 42n + 70 = 14(2m + 3n + 5)',
 'Divide each term by fourteen, leaving two m, three n, and five. Put fourteen outside parentheses.'),
 ('EXPAND TO CHECK','Each inside term must recover an original term','14(2m) + 14(3n) + 14(5)\n= 28m + 42n + 70',
 'Distribute fourteen back across all three terms. You recover the original expression. The same method works for two terms.')],
 g(6,6,11,8),equalities=[('14*2','28'),('14*3','42'),('14*5','70')],identities=[('14*(2*m+3*n+5)','28*m+42*n+70')]),
authored('gcf-prime-factorization','Find a GCF using shared prime factors',
 'Use prime factorization to find the GCF of 54, 90 and 126.', '18',
 'Use prime factorization to find the greatest common factor of fifty-four, ninety, and one hundred twenty-six.',[
 ('FACTOR EACH NUMBER','Write each number as a product of primes','54 = 2 × 3³\n90 = 2 × 3² × 5\n126 = 2 × 3² × 7',
 'Fifty-four is two times three cubed. Ninety is two times three squared times five. One hundred twenty-six is two times three squared times seven.'),
 ('KEEP SHARED PRIMES','Two and three appear in every factorization','Common primes: 2 and 3\nDiscard 5 and 7',
 'Keep only primes that appear in every number: two and three. Five and seven are not shared by all three.'),
 ('TAKE THE SMALLEST POWERS','The shared power cannot exceed any given exponent','Smallest powers: 2¹ and 3²\nGCF = 2 × 3² = 18',
 'Use the smallest exponent of each shared prime. That gives two times three squared, or eighteen.'),
 ('CHECK','Eighteen divides every number','54 = 18 × 3; 90 = 18 × 5\n126 = 18 × 7',
 'Eighteen divides all three numbers. The remaining factors three, five and seven have no shared factor above one. For two numbers, use the same shared-prime rule.')],
 e('prime-factorization',2,3),equalities=[('2*3**3','54'),('2*3**2*5','90'),('2*3**2*7','126'),('2*3**2','18')]),
authored('gcf-find-possible-number','Find numbers that give a specified GCF',
 'For positive integers x ≤ 60, find every x\nsuch that GCF(30, x) = 10.', '10, 20, 40, 50',
 'For positive integers x at most sixty, find every x such that the greatest common factor of thirty and x is ten.',[
 ('LIST CANDIDATES','Ten must divide x','Possible multiples: 10, 20, 30, 40, 50, 60',
 'Ten must divide x, so list its positive multiples up to sixty.'),
 ('CHECK THE EXTRA FACTOR','Thirty is ten times three','30 = 10 × 3\nGCF(30, 10k) = 10 when GCF(3, k) = 1',
 'Write thirty as ten times three and x as ten times k. After taking out ten, three and k must have no common factor above one.'),
 ('REJECT LARGER COMMON FACTORS','Exclude candidates whose k is divisible by three','Reject 30 and 60\nTheir GCF with 30 is 30',
 'Reject thirty and sixty, because both are divisible by thirty. Their greatest common factor is too large.'),
 ('LIST ALL VALID VALUES','Check that each remaining GCF is exactly ten','x = 10, 20, 40, 50',
 'The valid values are ten, twenty, forty and fifty. Being a multiple of the target factor is necessary, but you must also rule out a larger common factor.')],
 g(6,6,9,9),equalities=[('10*3','30'),('10*6','60')]),
]
def lessons(doc):return make_lessons(SPECS,doc)
from math import gcd
assert gcd(28,42)==14 and gcd(42,63)==21 and gcd(70,28)==14
assert gcd(28,42,70)==14 and gcd(54,90,126)==18
assert [x for x in range(1,61) if gcd(30,x)==10]==[10,20,40,50]
