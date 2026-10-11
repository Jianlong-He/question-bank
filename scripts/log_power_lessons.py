"""Logarithm power expansion with its real-domain conditions stated explicitly."""
from math import log,isclose
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons
SPECS=[
authored('expand-logarithm-power','Bring an exponent in a logarithm down as a multiplier',
 'Expand log base 3 (u⁹), where u > 0.', '9 log base 3 (u)',
 'Expand the base-three logarithm of u to the ninth power, where u is positive.',[
 ('CHECK THE DOMAIN','The base is positive and not one; the argument is positive','Base: 3 > 0 and 3 ≠ 1\nu > 0, so u⁹ > 0',
 'Three is a valid logarithm base because it is positive and not one. A positive u makes the logarithm argument positive.'),
 ('APPLY THE POWER RULE','An exponent on the argument becomes a coefficient','log base 3 (u⁹) = 9 log base 3 (u)',
 'The power rule moves the exponent nine in front as a multiplier. The answer is nine times the base-three logarithm of u.'),
 ('WHY IT WORKS','Let the logarithm of u equal t','u = 3ᵗ, so u⁹ = 3⁹ᵗ\nlog base 3 (u⁹) = 9t',
 'If the base-three logarithm of u is t, then u equals three to the t. Raising u to the ninth power multiplies that exponent by nine, so its logarithm is nine t.'),
 ('NUMERICAL CHECK','For u equal to three, both forms equal nine','u = 3: log base 3 (3⁹) = 9\n9 log base 3 (3) = 9 × 1 = 9',
 'Check with u equal to three. Both forms give nine. Keep the logarithm base unchanged; the exponent becomes a multiplier, not part of the base.')],
 g(11,5,3,3),equalities=[('3**9','19683'),('9*1','9')]),
]
for b in [.5,2,3,10]:
 for u in [.25,.7,1,2,5,9]:assert isclose(log(u**9,b),9*log(u,b),rel_tol=1e-12,abs_tol=1e-12)
def lessons(doc):return make_lessons(SPECS,doc)
