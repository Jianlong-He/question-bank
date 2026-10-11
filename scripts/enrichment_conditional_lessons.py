"""Fresh enrichment examples for conditional and complementary probability."""
from fractions import Fraction as F
from itertools import product
from math import comb
from algebra_lessons import authored
from probability_lessons import enrichment
from card_lessons import make_lessons

def e(w,q):return enrichment('conditional-probability',w,q)
SPECS=[
authored('probability-committee-given-members','Committee probability with known members',
 'Choose 5 of 12 students uniformly.\nGiven that Kai and Nia are chosen,\nwhat is the probability that Eli is chosen?','3/10',
 'Five of twelve students are chosen uniformly. Given that Kai and Nia are chosen, what is the probability that Eli is chosen?',[
 ('FIX THE KNOWN MEMBERS','Remove known members and their occupied places','Open places: 5 − 2 = 3\nAvailable students: 12 − 2 = 10',
 'Fix the two known members first. Three places remain among ten available students.'),
 ('USE SYMMETRY','Each available student has the same chance','P(Eli chosen | Kai and Nia chosen) = 3/10',
 'Each available student has the same chance of taking one of the three open places. Eli has probability three tenths.'),
 ('CHECK BY COUNTING','Count committees inside the given condition','All completions: C(10,3) = 120\nWith Eli: C(9,2) = 36\n36/120 = 3/10',
 'Alternatively, there are one hundred twenty completions. Thirty-six include Eli, giving the same fraction.'),
 ('GENERAL METHOD','Apply the condition before calculating','r open places among n available people → r/n',
 'After fixing every known member, divide open places by available people. This uses uniform selection.')],e(1,6),expression='3/10',value='3/10',equalities=[('36/120','3/10')]),
authored('probability-nested-events','Multiply probabilities for nested events',
 'A battery has probability 0.90 of lasting over 10 hours.\nGiven that it lasts over 10 hours, its chance\nof lasting over 18 hours is 0.70. Find P(over 18 hours).','0.63',
 'A battery has a ninety percent chance of lasting over ten hours. Given that it does, its chance of lasting over eighteen hours is seventy percent. Find the chance of lasting over eighteen hours.',[
 ('NAME THE EVENTS','The longer lifetime implies the shorter one','A: over 10 hours\nB: over 18 hours\nB is contained in A',
 'Call the shorter lifetime event A and the longer event B. Every B outcome also belongs to A.'),
 ('MULTIPLICATION RULE','Use the conditional probability supplied','P(B) = P(A) × P(B | A)',
 'Multiply the probability of reaching ten hours by the conditional probability of reaching eighteen hours.'),
 ('CALCULATE','Multiply the two probabilities','0.90 × 0.70 = 0.63',
 'Zero point nine times zero point seven is zero point six three.'),
 ('INTERPRET','The stricter event cannot be more likely','P(over 18 hours) = 63%',
 'The answer is sixty-three percent. No independence assumption is needed because the second probability is already conditional.')],e(1,8),expression='.90*.70',value='.63'),
authored('probability-ordered-roll-comparison','Compare two ordered die rolls',
 'Roll a fair four-sided die numbered 1 to 4 twice.\nWhat is the probability that the second roll\nis strictly less than the first?','3/8',
 'Roll a fair four-sided die numbered one to four twice. What is the probability that the second roll is strictly less than the first?',[
 ('ORDER MATTERS','First and second rolls form an ordered pair','4 × 4 = 16 equally likely outcomes',
 'The two rolls form an ordered pair. There are sixteen equally likely outcomes.'),
 ('COUNT BY FIRST ROLL','Count smaller possible second rolls','First roll:         1   2   3   4\nSmaller choices:  0   1   2   3',
 'For first rolls one, two, three, and four, there are zero, one, two, and three smaller second rolls.'),
 ('ADD AND DIVIDE','Strictly less excludes equal rolls','(0 + 1 + 2 + 3)/16 = 6/16 = 3/8',
 'Add the favourable counts and divide by sixteen. The probability is three eighths.'),
 ('SYMMETRY CHECK','Remove ties, then split the remaining outcomes','4 ties; 16 − 4 = 12 unequal outcomes\nHalf have second < first: 12/2 = 6',
 'As a check, remove the four ties. Exactly half the twelve unequal outcomes have the second roll smaller.')],e(1,10),expression='6/16',value='3/8'),
authored('probability-not-divisible','Probability of avoiding a multiple',
 'Choose an integer uniformly from 1 through 42.\nWhat is the probability it is not divisible by 6?','5/6',
 'Choose an integer uniformly from one through forty-two. What is the probability that it is not divisible by six?',[
 ('COUNT THE COMPLEMENT','List the multiples within the allowed range','6, 12, 18, 24, 30, 36, 42\n7 multiples',
 'First count the multiples of six. There are seven, ending at forty-two.'),
 ('DIVISIBLE PROBABILITY','All forty-two integers are equally likely','P(divisible by 6) = 7/42 = 1/6',
 'Seven of the forty-two equally likely integers are divisible by six. That probability is one sixth.'),
 ('SUBTRACT FROM ONE','Divisible and not divisible are complements','P(not divisible by 6) = 1 − 1/6 = 5/6',
 'Subtract one sixth from one. The probability of not being divisible by six is five sixths.'),
 ('CHECK THE COUNT','The favourable outcomes are the remaining integers','42 − 7 = 35\n35/42 = 5/6',
 'There are thirty-five favourable integers. Count multiples only within the stated range, then divide by the total number of possible integers.')],e(2,5),expression='1-7/42',value='5/6'),
authored('probability-dice-sum-complement','A dice sum threshold using the complement',
 'Roll two distinguishable fair six-sided dice.\nWhat is the probability that their sum is at least 6?','13/18',
 'Roll two distinguishable fair six-sided dice. What is the probability that their sum is at least six?',[
 ('CHOOSE THE OPPOSITE','The complement of at least six is below six','Excluded sums: 2, 3, 4, 5',
 'The opposite event is a sum below six. That means sums two, three, four, or five.'),
 ('COUNT ORDERED PAIRS','Different dice orders count separately','Sum:                  2   3   4   5\nNumber of pairs:  1   2   3   4\nExcluded total = 10',
 'Those sums occur in one, two, three, and four ordered ways. That gives ten excluded outcomes.'),
 ('SUBTRACT AND DIVIDE','Two six-sided dice give thirty-six outcomes','(36 − 10)/36 = 26/36 = 13/18',
 'Subtract ten from thirty-six, then divide by thirty-six. The probability is thirteen eighteenths.'),
 ('CHECK THE BOUNDARY','At least includes the boundary value','Sum 6 is included; only smaller sums are excluded.',
 'Keep outcomes with sum six. At least includes equality, so only sums below six belong in the complement.')],e(2,4),expression='(36-10)/36',value='13/18'),
authored('probability-conditional-complement','Complements inside a given condition',
 'P(A | B) = 0.46 and P(B) > 0.\nFind P(not A | B).','0.54',
 'The probability of A given B is zero point four six, and B has positive probability. Find the probability of not A given B.',[
 ('KEEP THE CONDITION','We consider only outcomes where B occurs','Within B: A or not A',
 'Keep B as the condition. Within those outcomes, either A happens or A does not happen.'),
 ('COMPLEMENTS ADD TO ONE','The condition stays the same on both terms','P(A | B) + P(not A | B) = 1',
 'These two conditional probabilities add to one. Both use the same condition B.'),
 ('SUBTRACT','Remove the given probability from one','P(not A | B) = 1 − 0.46 = 0.54',
 'Subtract zero point four six from one. The answer is zero point five four.'),
 ('INTERPRET','This is still conditional probability','Among outcomes satisfying B, 54% do not satisfy A.',
 'Among outcomes satisfying B, fifty-four percent do not satisfy A. We have not removed or reversed the condition.')],e(2,7),expression='1-.46',value='.54'),
]

def lessons(doc):
 assert F(comb(9,2),comb(10,3))==F(3,10)
 assert sum(b<a for a,b in product(range(1,5),repeat=2))==6
 assert sum(a+b>=6 for a,b in product(range(1,7),repeat=2))==26
 assert sum(n%6!=0 for n in range(1,43))==35
 return make_lessons(SPECS,doc)
