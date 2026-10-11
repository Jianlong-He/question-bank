"""Concrete analogous examples explaining coprimality and Euclidean stopping rules."""
from math import gcd
from algebra_lessons import authored
from number_theory_lessons import source as e
from card_lessons import make_lessons
SPECS=[
authored('gcf-coprime-fraction','Use a GCD of one to recognize a simplest fraction',
 'Are 14 and 25 coprime? Can 14/25 be reduced?', 'Coprime; 14/25 is already in simplest form',
 'Are fourteen and twenty-five coprime, and can fourteen twenty-fifths be reduced?',[
 ('LIST FACTORS','Look for a shared divisor','14: 1, 2, 7, 14\n25: 1, 5, 25',
 'The factors of fourteen are one, two, seven, and fourteen. The factors of twenty-five are one, five, and twenty-five.'),
 ('FIND THE GCD','Their only common positive factor is one','gcd(14, 25) = 1',
 'Only one appears in both lists, so the greatest common divisor is one.'),
 ('NAME THE RELATIONSHIP','Coprime numbers need not be prime individually','14 and 25 are coprime',
 'Numbers with greatest common divisor one are called coprime, or relatively prime. Neither number needs to be prime by itself.'),
 ('APPLY TO THE FRACTION','There is no common factor above one to cancel','14/25 is in simplest form',
 'A fraction reduces by dividing its numerator and denominator by a common factor above one. There is none here, so fourteen twenty-fifths is already in simplest form.')],
 e('Euclidean-division',1,3),equalities=[('14','2*7'),('25','5*5')]),
authored('gcf-distinct-primes','Explain why two distinct primes have GCD one',
 'Find the GCD of the distinct primes 13 and 19.\nExplain using their factors.', '1',
 'Find the greatest common divisor of the distinct primes thirteen and nineteen. Explain using their factors.',[
 ('FIRST PRIME','A prime has exactly two positive factors','Factors of 13: 1 and 13',
 'A prime has exactly two positive factors: one and itself. For thirteen, those are one and thirteen.'),
 ('SECOND PRIME','The second prime is different','Factors of 19: 1 and 19',
 'For nineteen, the factors are one and nineteen.'),
 ('INTERSECT','The two prime factors are unequal','Common positive factor: 1',
 'Because the primes are different, neither prime is a factor in the other list. The only shared factor is one.'),
 ('GENERALIZE','Distinctness is the key condition','gcd(13, 19) = 1\ngcd(13, 13) = 13',
 'The greatest common divisor is one. The same reasoning applies to any two distinct primes. If the primes were equal, their greatest common divisor would be that prime instead.')],
 e('prime-factorization',2,5),equalities=[('13/13','1'),('19/19','1')]),
authored('gcf-normalize-both-numbers','Divide both numbers by their GCD to remove shared factors',
 'The GCD of 84 and 126 is 42.\nCompare dividing both numbers by 42 with dividing only 84.', 'Both: gcd(2,3)=1; only the first: gcd(2,126)=2',
 'The greatest common divisor of eighty-four and one hundred twenty-six is forty-two. Compare dividing both numbers by it with dividing only the first number.',[
 ('DIVIDE BOTH','Remove the entire common factor from each number','84 ÷ 42 = 2; 126 ÷ 42 = 3',
 'Dividing both numbers by forty-two leaves two and three.'),
 ('CHECK WHAT REMAINS','The remaining numbers are coprime','gcd(2, 3) = 1',
 'Two and three are coprime. Any further shared factor would mean forty-two was not the greatest common divisor originally.'),
 ('DIVIDE ONLY ONE','Leaving the second number unchanged can retain a factor','gcd(84 ÷ 42, 126)\n= gcd(2, 126) = 2',
 'Dividing only the first number leaves two and one hundred twenty-six. They still share a factor of two.'),
 ('CONCLUSION','To guarantee coprime results, divide both numbers','84/42 = 2; 126/42 = 3\nThe remaining numbers are coprime',
 'Remove the greatest common divisor from both numbers to guarantee coprime results. Changing only one number does not give that guarantee.')],
 e('Euclidean-division',4,5),equalities=[('84/42','2'),('126/42','3')]),
authored('gcf-remainder-one','Use a remainder of one to prove two numbers are coprime',
 'Find gcd(38,39) and gcd(43,14)\nusing remainders.', 'Both GCDs are 1',
 'Find the greatest common divisors of thirty-eight and thirty-nine, and of forty-three and fourteen, using remainders.',[
 ('CONSECUTIVE NUMBERS','Their difference is one','39 = 1 × 38 + 1',
 'Thirty-nine is one more than thirty-eight. Dividing leaves remainder one.'),
 ('COMMON DIVISOR ARGUMENT','A shared divisor must divide their difference','Any common divisor divides 39 − 38 = 1\ngcd(38,39) = 1',
 'Any number dividing both must divide their difference, one. The only positive divisor of one is one.'),
 ('ANOTHER REMAINDER OF ONE','The quotient need not be one','43 = 3 × 14 + 1',
 'Forty-three is three times fourteen plus one. The same argument works even though the quotient is three.'),
 ('USE THE RULE','A shared divisor also divides the remainder','gcd(43,14) = gcd(14,1) = 1',
 'A common divisor must divide forty-three minus three times fourteen, which is one. A remainder of one proves that the numbers are coprime.')],
 e('Euclidean-division',1,6),equalities=[('39-38','1'),('43-3*14','1')]),
authored('gcf-zero-remainder','Recognize the GCD when division leaves no remainder',
 'Find gcd(96,24). Explain why a zero remainder ends the process.', '24',
 'Find the greatest common divisor of ninety-six and twenty-four. Explain why a zero remainder ends the process.',[
 ('DIVIDE','Twenty-four divides ninety-six exactly','96 = 4 × 24 + 0',
 'Ninety-six is four times twenty-four, with remainder zero.'),
 ('COMMON FACTOR','The divisor divides both original numbers','24 divides 96 and 24',
 'Twenty-four divides ninety-six, and it also divides itself, so it is a common factor.'),
 ('GREATEST','A positive divisor of twenty-four cannot exceed twenty-four','No common positive factor can be larger than 24',
 'Every common factor must divide twenty-four. No positive divisor of twenty-four is larger than twenty-four itself.'),
 ('STOP','At an exact division, use the current divisor','gcd(96,24) = 24',
 'Therefore twenty-four is the greatest common divisor. In the Euclidean algorithm, a zero remainder means stop and use the divisor from that final step.')],
 e('Euclidean-division',1,7),equalities=[('4*24','96')]),
authored('gcf-linear-combination-one','Use an integer combination equal to one to establish GCD one',
 'Since 5 × 17 − 3 × 28 = 1,\nwhat can you conclude about gcd(17,28)?', 'The GCD is 1',
 'Since five times seventeen minus three times twenty-eight equals one, what can you conclude about the greatest common divisor of seventeen and twenty-eight?',[
 ('CHECK THE IDENTITY','Both coefficients are integers','5 × 17 − 3 × 28 = 85 − 84 = 1',
 'Check the identity. Eighty-five minus eighty-four equals one.'),
 ('TAKE A COMMON DIVISOR','It divides every integer multiple of each number','d divides 17 and 28\nso d divides 5 × 17 and 3 × 28',
 'Let d be any common positive divisor. It divides each integer multiple of seventeen and twenty-eight.'),
 ('SUBTRACT','It must also divide the difference','d divides 5 × 17 − 3 × 28 = 1',
 'A divisor of both terms also divides their difference, so d must divide one.'),
 ('CONCLUDE','One has only one positive divisor','d = 1\ngcd(17,28) = 1',
 'The only possible common positive divisor is one. This argument works whenever an integer linear combination of two numbers equals one.')],
 e('Euclidean-division',3,2),equalities=[('5*17-3*28','1')]),
]
def lessons(doc):return make_lessons(SPECS,doc)
assert gcd(14,25)==gcd(13,19)==gcd(38,39)==gcd(43,14)==gcd(17,28)==1
assert gcd(84,126)==42 and gcd(2,126)==2 and gcd(96,24)==24
