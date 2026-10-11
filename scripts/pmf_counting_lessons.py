"""Checked PMF, combination, factorial and expected-net-gain examples."""
from fractions import Fraction as F
from math import comb,factorial
from algebra_lessons import authored
from probability_lessons import enrichment
from number_sense_lessons import source
from card_lessons import make_lessons

SPECS=[
authored('probability-pmf-normalization','Normalizing a probability mass function',
 'p(k) = ck for k = 1, 2, 3, 4, 5, 6; zero otherwise.\nFind c so this is a probability mass function.','1/21',
 "A probability mass function is c times k for k from one through six, and zero elsewhere. Let's find c.",[
 ('TOTAL PROBABILITY','Add every possible probability','c + 2c + 3c + 4c + 5c + 6c = 1',
  'The probabilities must add to one. Add c, two c, three c, four c, five c, and six c.'),
 ('COLLECT','Add the coefficients','(1 + 2 + 3 + 4 + 5 + 6)c = 21c',
  'The coefficients add to twenty-one, so the total is twenty-one c.'),
 ('SOLVE','Set the total equal to 1','21c = 1 → c = 1/21',
  'Set twenty-one c equal to one. Divide by twenty-one to get c equals one twenty-first.'),
 ('CHECK BOTH RULES','All probabilities are nonnegative','p(k) = k/21\n(1 + 2 + 3 + 4 + 5 + 6)/21 = 1',
  'Every resulting probability is nonnegative, and their sum is one. Both requirements are satisfied.')],
 enrichment('PMF',1,9),expression='1/(1+2+3+4+5+6)',value='1/21',equation=('21*c','1','c','1/21')),

authored('probability-geometric-ratio','Successive geometric probabilities',
 'Independent trials succeed with probability 0.45.\nX is the first success. Find P(X = 2)/P(X = 1).','0.55',
 "Independent trials succeed with probability zero point four five. X is the first success. Let's compare the probabilities for attempts two and one.",[
 ('FIRST ATTEMPT','Success immediately','P(X = 1) = 0.45',
  'A success immediately has probability zero point four five.'),
 ('SECOND ATTEMPT','One failure, then success','P(X = 2) = 0.55 × 0.45 = 0.2475',
  'For the second attempt, fail once then succeed. Zero point five five times zero point four five is zero point two four seven five.'),
 ('DIVIDE','The common success factor cancels','0.2475/0.45 = 0.55',
  'Divide by zero point four five. The ratio is zero point five five, the failure probability.'),
 ('GENERALIZE','Every extra failure adds a factor of 1 − p','For 0 < p < 1 and k ≥ 2:\nP(X = k)/P(X = k − 1) = 1 − p\nGiven ratio r: p = 1 − r\nLargest probability: k = 1',
  'Each extra failure adds a factor of one minus p. Given the ratio r, recover p as one minus r. For p between zero and one, the probabilities decrease, so the largest is at attempt one.')],
 enrichment('PMF','2HW',5),expression='(0.55*0.45)/0.45',value='0.55'),

authored('pattern-pmf-2e87e898b750','Recovering a geometric success probability',
 'X is geometric and P(X > 2) = 0.36.\nFind the success probability p.','0.4',
 "X is the attempt of the first success in independent trials. The probability that X is greater than two is zero point three six. Let's find p.",[
 ('TRANSLATE','More than two means two failures','P(X > 2) = (1 − p)² = 0.36',
  'More than two means both first attempts fail. Their probability is one minus p, squared.'),
 ('TAKE A ROOT','The failure probability is nonnegative','1 − p = √0.36 = 0.6',
  'Take the nonnegative square root. The failure probability, one minus p, is zero point six.'),
 ('SOLVE','Success and failure probabilities add to 1','p = 1 − 0.6 = 0.4',
  'Subtract from one. The success probability is zero point four.'),
 ('CHECK AND EXTEND','Use the corresponding root for other waiting times','(1 − 0.4)² = 0.36\nFor P(X > t), take the nonnegative t-th root first.',
  'Check: zero point six squared is zero point three six. For a tail beyond t attempts, take the nonnegative t-th root before subtracting from one.')],
 enrichment('PMF',4,7),expression='1-0.6',value='0.4',equalities=[('(1-0.4)**2','0.36')]),

authored('probability-geometric-disjoint-times','Adding distinct first-success times',
 'Independent trials succeed with probability 1/4.\nFind P(first success on attempt 2 or 3).','21/64',
 "Independent trials succeed with probability one fourth. Let's find the probability that the first success is on attempt two or attempt three.",[
 ('ATTEMPT TWO','One failure, then success','P(X = 2) = (3/4)(1/4) = 3/16',
  'For attempt two, one failure precedes a success. Three fourths times one fourth is three sixteenths.'),
 ('ATTEMPT THREE','Two failures, then success','P(X = 3) = (3/4)²(1/4) = 9/64',
  'For attempt three, two failures precede success. The probability is nine sixty-fourths.'),
 ('ADD DISJOINT CASES','The first success cannot be at both times','P(X = 2 or X = 3) = 3/16 + 9/64',
  'The first success cannot occur at both times in one run. These cases do not overlap, so add their probabilities.'),
 ('COMMON DENOMINATOR','Convert sixteenths to sixty-fourths','12/64 + 9/64 = 21/64',
  'Three sixteenths is twelve sixty-fourths. Adding nine sixty-fourths gives twenty-one sixty-fourths.')],
 enrichment('PMF',4,5),expression='3/4*1/4+(3/4)**2*1/4',value='21/64'),

authored('pattern-pmf-803aa2d4d578','Counting the same selections two ways',
 'Choose 2 balls from 3 red and 5 blue balls.\nVerify the total by counting each possible number of reds.','28',
 "Choose two balls from three red and five blue balls. Let's count the selections two ways to see the hypergeometric identity.",[
 ('DIRECT COUNT','Choose any 2 of the 8 balls','C(8, 2) = 28',
  'Ignoring colour, there are eight choose two, or twenty-eight selections.'),
 ('SPLIT BY RED COUNT','The cases have 0, 1 or 2 reds','0 red: C(3, 0)C(5, 2) = 10\n1 red: C(3, 1)C(5, 1) = 15\n2 red: C(3, 2)C(5, 0) = 3',
  'With zero reds there are ten selections, with one red there are fifteen, and with two reds there are three.'),
 ('ADD','Every selection belongs to exactly one case','10 + 15 + 3 = 28',
  'The disjoint cases cover all selections. Ten plus fifteen plus three equals twenty-eight, matching the direct count.'),
 ('GENERAL IDENTITY','Sum over k = 0, 1, …, n','Σ C(m, k)C(N − m, n − k) = C(N, n)\nDivide by C(N, n) → total probability = 1',
  'In general, sum over the possible success counts. The sum equals N choose n. Dividing both sides by that total shows why the hypergeometric probabilities add to one.')],
 enrichment('PMF','7Rev',4),expression='10+15+3',value='28'),

authored('probability-hypergeometric-complement','At least one in a sample',
 '12 tickets include 3 winners. Choose 4 uniformly.\nFind P(at least one winning ticket).','41/55',
 "Twelve tickets include three winners. Choose four tickets uniformly without replacement. Let's find the probability of at least one winner.",[
 ('OPPOSITE EVENT','No winners means all four tickets lose','9 losing tickets; choose 4 of them.',
  'The opposite event is no winners. All four tickets must come from the nine losing tickets.'),
 ('COUNT SAMPLES','Use combinations because order does not matter','No-winner samples: C(9, 4) = 126\nAll samples: C(12, 4) = 495',
  'There are nine choose four, or one hundred twenty-six, no-winner samples. There are twelve choose four, or four hundred ninety-five, samples altogether.'),
 ('PROBABILITY OF NONE','Divide favourable samples by all samples','P(no winners) = 126/495 = 14/55',
  'The probability of no winners is one hundred twenty-six over four hundred ninety-five, or fourteen fifty-fifths.'),
 ('COMPLEMENT','Subtract from 1','P(at least one winner) = 1 − 14/55 = 41/55',
  'Subtract from one. The probability of at least one winner is forty-one fifty-fifths.')],
 enrichment('PMF',6,9),expression='1-126/495',value='41/55'),

authored('counting-combinations','Choosing an unordered committee',
 'Choose a committee of 4 from 16 people.\nHow many different committees are possible?','1820',
 "Choose a committee of four from sixteen people. Everyone has the same role, so only membership matters. How many committees are possible?",[
 ('ORDERED SELECTIONS','Temporarily count four distinct positions','16 × 15 × 14 × 13 = 43,680',
  'First count ordered selections: sixteen times fifteen times fourteen times thirteen gives forty-three thousand six hundred eighty.'),
 ('REMOVE DUPLICATE ORDERS','Each committee has 4! different orders','4! = 4 × 3 × 2 × 1 = 24',
  'The same four people can be ordered in twenty-four ways. Each committee was counted that many times.'),
 ('DIVIDE','Count each committee once','C(16, 4) = 43,680/24 = 1,820',
  'Divide by twenty-four to get one thousand eight hundred twenty committees.'),
 ('GENERAL RULE','Use combinations when order does not matter','C(n, r) = n! / [r!(n − r)!]',
  'The combination formula divides the ordered count by r factorial. Use it for a set of r distinct objects when order does not matter.')],
 enrichment('PMF',6,2),expression='16*15*14*13/(4*3*2*1)',value='1820'),

authored('counting-factorials','Evaluating a factorial',
 'Evaluate 8!.','40320',
 "Let's evaluate eight factorial. The exclamation mark tells us to multiply all the positive whole numbers from eight down to one.",[
 ('EXPAND','Include each positive integer down to 1','8! = 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1',
  'Write eight times seven times six times five times four times three times two times one.'),
 ('GROUP THE PRODUCTS','Calculate smaller products','8 × 7 = 56; 6 × 5 = 30; 4 × 3 × 2 × 1 = 24',
  'Group the products: eight times seven is fifty-six, six times five is thirty, and the remaining factors make twenty-four.'),
 ('MULTIPLY','Combine the products','56 × 30 × 24 = 40,320',
  'Fifty-six times thirty times twenty-four equals forty thousand three hundred twenty.'),
 ('RULE','Factorial multiplies, rather than adds','8! = 40,320\nBy definition: 0! = 1',
  'Eight factorial is forty thousand three hundred twenty. The special definition zero factorial equals one keeps factorial formulas consistent.')],
 source(12,8,2,1),expression='8*7*6*5*4*3*2*1',value='40320'),

authored('pattern-probability-and-combinatorics-748de98e98f6','Expected net gain',
 'Expected payout: $3.75. Cost to play: $5.50.\nFind the player’s expected net gain.','-$1.75',
 "A game's expected payout is three dollars seventy-five, and it costs five dollars fifty to play. Let's find the player's expected net gain.",[
 ('ACCOUNT FOR THE COST','Payout alone is not net gain','Expected net gain = expected payout − cost',
  'Subtract the cost to play from the expected payout.'),
 ('SUBTRACT','Keep the player’s point of view','$3.75 − $5.50 = −$1.75',
  'Three dollars seventy-five minus five dollars fifty is negative one dollar seventy-five.'),
 ('INTERPRET THE SIGN','A negative expectation means an average loss','Expected loss = $1.75 per play',
  'The negative sign means an expected loss of one dollar seventy-five per play. It does not mean every play loses exactly that amount.'),
 ('OVER MANY PLAYS','Expected net gains add','20 plays: 20 × (−$1.75) = −$35',
  'Over twenty plays with the same cost and expected payout, the expected net total is negative thirty-five dollars.')],
 source(12,8,'5HW',5),expression='3.75-5.50',value='-1.75',equalities=[('20*(3.75-5.50)','-35')]),
]


def lessons(doc):
    assert sum(F(k,21) for k in range(1,7))==1
    assert F(6,10)**2==F(36,100)
    assert comb(8,2)==sum(comb(3,k)*comb(5,2-k) for k in range(3))==28
    assert [comb(3,k)*comb(5,2-k) for k in range(3)]==[10,15,3]
    assert comb(9,4)==126 and comb(12,4)==495
    assert comb(16,4)==1820 and factorial(8)==40320
    return make_lessons(SPECS,doc)
