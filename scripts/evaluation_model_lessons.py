"""Exponential, inverse-variation and factored-function evaluation examples."""
import math
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons
SPECS=[
authored('evaluation-exponential-integer-base','Evaluate an exponential model with a whole-number base',
 'For A = 40 × 4^t, find A when t = 3.', '2560',
 'For A equals forty times four to the power t, find A when t is three.',[
 ('SUBSTITUTE','Put three in the exponent position','A = 40 × 4³',
 'Replace t with three. The input belongs in the exponent, not as another multiplication factor.'),
 ('POWER FIRST','Multiply three copies of four','4³ = 4 × 4 × 4 = 64',
 'Four cubed is four times four times four, or sixty-four.'),
 ('MULTIPLY','Apply the starting multiplier after the power','A = 40 × 64 = 2560',
 'Multiply sixty-four by forty to get two thousand five hundred sixty.'),
 ('CHECK','Track three repeated multiplications by four','40 → 160 → 640 → 2560',
 'Starting with forty, multiply by four three times. The result agrees. The exponent acts on the base four, not on the whole product.')],
 g(10,7,1,6),equalities=[('40*4**3','2560')]),
authored('evaluation-exponential-decimal-base','Evaluate exponential models with decimal bases',
 'Find A = 300(1.02)^t when t = 2.\nFind y = 12(0.25)^x when x = 2.', 'A = 312.12; y = 0.75',
 'Find A equals three hundred times one point zero two to the power t when t is two. Then find y equals twelve times zero point two five to the power x when x is two.',[
 ('FIRST POWER','Square the growth multiplier','(1.02)² = 1.02 × 1.02 = 1.0404',
 'Substitute two for t. Square one point zero two to get one point zero four zero four.'),
 ('FIRST OUTPUT','Multiply by the starting amount','A = 300 × 1.0404 = 312.12',
 'Multiply by three hundred. The first output is three hundred twelve point one two.'),
 ('SECOND POWER','Square the decay multiplier','(0.25)² = 0.25 × 0.25 = 0.0625',
 'For the second model, square zero point two five. The result is zero point zero six two five.'),
 ('SECOND OUTPUT','Multiply after evaluating the power','y = 12 × 0.0625 = 0.75',
 'Multiplying by twelve gives zero point seven five. A base above one increases a positive starting value; a base between zero and one decreases it.')],
 g(9,14,2,7),equalities=[('300*1.02**2','312.12'),('12*.25**2','.75')]),
authored('evaluation-continuous-decay-percent','Find the percent remaining in an exponential decay model',
 'Q = 800e^(−0.25t). What percent of the initial\nquantity remains at t = 3? Round to one decimal percent.', '47.2%',
 'Q equals eight hundred e to the power negative zero point two five t. What percent remains at t equals three? Round to one decimal percent.',[
 ('INITIAL VALUE','At time zero the exponential factor is one','Q(0) = 800e⁰ = 800',
 'At time zero, e to the zero power is one, so the initial quantity is eight hundred.'),
 ('FORM A RATIO','Divide the later quantity by the initial quantity','Q(3)/Q(0) = 800e^(−0.75)/800\n= e^(−0.75)',
 'At time three, the exponent is negative zero point seven five. Dividing by the initial amount cancels the factor eight hundred.'),
 ('USE THE EXPONENTIAL KEY','Evaluate the remaining fraction with a calculator','e^(−0.75) ≈ 0.4723666',
 'Use the calculator exponential function to evaluate e to negative zero point seven five. Keep extra digits for the next step.'),
 ('CONVERT AND ROUND','Multiply the fraction by one hundred','Percent remaining ≈ 47.23666%\nRounded to one decimal percent: 47.2%',
 'Multiply by one hundred to convert the fraction to a percent. The hundredths digit is three, so the answer rounds to forty-seven point two percent.')],
 g(11,5,4,9),equalities=[('-.25*3','-.75'),('800/800','1')]),
authored('evaluation-inverse-variation-constant','Find the constant of inverse variation',
 'y varies inversely with x. If y = 14 when x = 5,\nfind the constant of variation k.', 'k = 70',
 'Y varies inversely with x. If y is fourteen when x is five, find the constant of variation k.',[
 ('INVERSE MODEL','Write the inverse-variation rule','y = k/x, with x ≠ 0',
 'Inverse variation means y equals k divided by x, where x is nonzero.'),
 ('ISOLATE THE CONSTANT','Multiply both sides by x','xy = k',
 'Multiply both sides by x. The constant is the product x times y.'),
 ('SUBSTITUTE','Use the paired input and output','k = 5 × 14 = 70',
 'Use the paired values five and fourteen. Their product is seventy.'),
 ('CHECK THE RULE','The rule must reproduce the given pair','y = 70/x\nAt x = 5: y = 70/5 = 14',
 'The model y equals seventy over x gives fourteen when x is five. The product stays constant in inverse variation.')],
 g(11,13,4,9),equalities=[('5*14','70'),('70/5','14')]),
authored('evaluation-factored-polynomial-sign','Find the sign of a factored polynomial at an input',
 'For f(x) = (x − 3)(x + 4)(x − 7),\nfind the sign of f(1).', 'Positive',
 'For f of x equals x minus three, times x plus four, times x minus seven, find the sign at x equals one.',[
 ('SUBSTITUTE','Put one into each factor','f(1) = (1 − 3)(1 + 4)(1 − 7)',
 'Substitute one into all three factors.'),
 ('FACTOR SIGNS','Find the sign of each factor','1 − 3 = −2\n1 + 4 = 5\n1 − 7 = −6',
 'The factors are negative two, positive five, and negative six. None is zero.'),
 ('COMBINE SIGNS','Two negative factors give a positive product','Negative × positive × negative = positive',
 'There are two negative factors. An even number of negative factors gives a positive product.'),
 ('CONFIRM','The exact value agrees with the sign','f(1) = (−2)(5)(−6) = 60 > 0',
 'The product is sixty, confirming a positive sign. If any factor were zero, the product would be zero instead.')],
 g(11,4,2,7),equalities=[('(1-3)*(1+4)*(1-7)','60')]),
]
assert round(100*math.exp(-.25*3),1)==47.2
assert abs(math.exp(-.75)-.4723666)<.0000001

def lessons(doc):return make_lessons(SPECS,doc)
