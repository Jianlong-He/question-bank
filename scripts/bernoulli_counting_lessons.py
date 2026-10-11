"""Original Bernoulli and repeated-counting examples for the remaining PMF methods."""
from fractions import Fraction as F
from itertools import product
from math import comb
from algebra_lessons import authored
from probability_lessons import enrichment as e
from card_lessons import make_lessons

SPECS=[
authored('pattern-pmf-488f17f2e44d','Recognizing a Bernoulli trial',
 'A parcel is weighed. Compare two records:\nA: its mass in grams; B: whether its mass exceeds 2 kg.\nWhich record is a Bernoulli outcome?','B',
 'A parcel is weighed. We could record its mass in grams, or whether it exceeds two kilograms. Which record gives a Bernoulli outcome?',[
 ('TWO CATEGORIES','Choose a success event and its complement','Success: mass > 2 kg\nFailure: mass ≤ 2 kg',
  'A Bernoulli outcome has two categories. Here, success can mean the mass exceeds two kilograms. Failure means it does not.'),
 ('COMPARE RECORDS','An exact mass has many possible values','A: many numerical values\nB: yes or no',
  'The exact mass has many possible values. The threshold record has only yes and no, so record B is Bernoulli.'),
 ('ENCODE','Use 1 for success and 0 for failure','B: success → 1; failure → 0\nP(1) = p; P(0) = 1 − p',
  'We encode success as one and failure as zero. Their probabilities are p and one minus p.'),
 ('SEQUENCES','Extra assumptions belong to repeated trials','One trial: two categories\nIndependent p-Bernoulli trials: independent, same p',
  'One Bernoulli trial needs two categories. A sequence of independent p Bernoulli trials additionally needs independence and the same success probability.')],
 e('PMF',3,8),identities=[('p+(1-p)','1')]),

authored('pattern-pmf-d93d36d25e19','A specified success and failure sequence',
 'Independent trials succeed with p = 0.35.\nFind P(success, failure, success).','0.079625',
 'Independent trials succeed with probability zero point three five. Find the probability of success, failure, success in that exact order.',[
 ('FAILURE PROBABILITY','Success and failure cover all outcomes','q = 1 − 0.35 = 0.65',
  'Failure has probability one minus zero point three five, which is zero point six five.'),
 ('FOLLOW THE ORDER','Write one factor for each trial','S → F → S\nP(S, F, S) = p × q × p',
  'Follow the requested order. Success contributes p, failure contributes q, and the last success contributes p.'),
 ('MULTIPLY','Use independence','0.35 × 0.65 × 0.35 = 0.079625',
  'Independence lets us multiply. The product is zero point zero seven nine six two five.'),
 ('ONE SPECIFIED ORDER','No combinations factor is needed','s successes, f failures in a fixed order:\nprobability = p^s × (1 − p)^f',
  'For one specified order, multiply the success and failure factors. Do not add a combinations factor unless different orders are also allowed.')],
 e('PMF',3,5),expression='0.35*0.65*0.35',value='0.079625'),

authored('pattern-pmf-ea9fc03d2b5b','Recovering p from repeated successes',
 'Independent trials all have success probability p.\nP(two successes in a row) = 0.49. Find p.','0.7',
 'Independent trials share success probability p. Two successes in a row have probability zero point four nine. Find p.',[
 ('MODEL','Independence gives one factor per success','p × p = p² = 0.49',
  'Multiply p by p for two successes. Therefore p squared equals zero point four nine.'),
 ('TAKE THE ROOT','A probability cannot be negative','p = √0.49 = 0.7',
  'Take the nonnegative square root. P equals zero point seven. The negative root is not a probability.'),
 ('CHECK','Square the result','0.7 × 0.7 = 0.49',
  'Check by multiplying zero point seven by itself. We recover zero point four nine.'),
 ('GENERALIZE','For n consecutive successes, undo the nth power','p^n = a → p is the nonnegative n-th root of a\nThree successes → cube root',
  'With n consecutive successes, p to the nth power equals the given probability. Take the nonnegative nth root; for three successes, use a cube root.')],
 e('PMF',3,10),expression='7/10',value='0.7',equalities=[('0.7**2','0.49')]),

authored('pattern-pmf-d313e72dd673','Counting repeated draws with replacement',
 'A bag contains 7 distinct labelled tokens.\nDraw and replace a token 4 times. Count ordered sequences.','2401',
 'A bag holds seven distinct labelled tokens. Draw a token, replace it, and repeat for four draws. How many ordered sequences are possible?',[
 ('EACH DRAW','Replacement restores all seven choices','Draws 1, 2, 3, 4: 7 choices each',
  'Replacement restores the bag, so every draw has seven choices.'),
 ('MULTIPLICATION PRINCIPLE','Multiply the number of choices at each stage','7 × 7 × 7 × 7 = 7⁴',
  'Use the multiplication principle. Multiply seven choices for each of the four positions.'),
 ('CALCULATE','Group the products','7² = 49\n49 × 49 = 2,401',
  'Seven squared is forty-nine. Forty-nine times forty-nine is two thousand four hundred one.'),
 ('GENERAL RULE','Different orders count as different sequences','m distinct objects, n draws with replacement:\nordered sequences = m^n',
  'In general, n draws with replacement from m distinct objects give m to the nth power ordered sequences. Repetitions are allowed.')],
 e('PMF',5,1),expression='7**4',value='2401',equalities=[('49*49','2401')]),

authored('pattern-pmf-fc49f9797eeb','Filling fixed positions by the counting principle',
 '3 distinct red and 5 distinct blue tokens; replacement.\nCount 5-draw sequences ordered red, red, blue, blue, blue.','1125',
 'Draw with replacement from three distinct red and five distinct blue tokens. Count sequences with red in the first two positions, then three blues.',[
 ('RED POSITIONS','Each red position has three choices','3 × 3 = 3² = 9',
  'Each of the two red positions has three choices. They can be filled in nine ways.'),
 ('BLUE POSITIONS','Each blue position has five choices','5 × 5 × 5 = 5³ = 125',
  'Each of the three blue positions has five choices. They can be filled in one hundred twenty-five ways.'),
 ('MULTIPLY','Combine the choices for all fixed positions','3² × 5³ = 9 × 125 = 1,125',
  'Multiply nine by one hundred twenty-five. There are one thousand one hundred twenty-five sequences in this fixed colour order.'),
 ('IF POSITIONS ARE ALSO CHOSEN','First choose positions, then fill them','Any 2 red positions: C(5, 2) × 3² × 5³\nBoth stages use the multiplication principle.',
  'If the red positions are not fixed, first choose two of the five positions, then fill them. The multiplication principle combines those two stages too.')],
 e('PMF',5,2),expression='3**2*5**3',value='1125'),

authored('probability-binomial-upper-tail','Adding binomial cases for at least',
 'Flip a fair coin 4 independent times.\nFind P(at least 3 heads).','5/16',
 'Flip a fair coin four independent times. Find the probability of at least three heads.',[
 ('LIST THE COUNTS','At least three means three or four','X = 3 or X = 4',
  'At least three means exactly three or exactly four. These cases are disjoint.'),
 ('EXACTLY THREE','Choose the positions of the heads','P(X = 3) = C(4, 3)(1/2)⁴ = 4/16',
  'There are four ways to choose the three head positions. Each sequence has probability one sixteenth, giving four sixteenths.'),
 ('EXACTLY FOUR','All four flips are heads','P(X = 4) = (1/2)⁴ = 1/16',
  'Four heads have only one order, with probability one sixteenth.'),
 ('ADD','Sum the disjoint binomial probabilities','P(X ≥ 3) = 4/16 + 1/16 = 5/16',
  'Add the probabilities to get five sixteenths. For other binomial tails, include every count from the threshold through the total number of trials.')],
 e('PMF','5Rev',2),expression='4/16+1/16',value='5/16'),

authored('probability-not-all-successes','At most one fewer than all trials',
 'A player succeeds independently with p = 0.6.\nIn 3 attempts, find P(at most 2 successes).','0.784',
 'A player succeeds independently with probability zero point six. In three attempts, find the probability of at most two successes.',[
 ('INTERPRET','Allowed counts are zero, one or two','At most 2 out of 3 ↔ not all 3',
  'At most two allows zero, one, or two successes. The only excluded outcome is three successes.'),
 ('OPPOSITE EVENT','All three attempts succeed','P(all 3) = 0.6³',
  'For all three successes, multiply zero point six three times.'),
 ('CALCULATE','Use independence','0.6³ = 0.216',
  'Zero point six cubed is zero point two one six.'),
 ('SUBTRACT FROM ONE','Complementary probabilities total one','P(at most 2) = 1 − 0.216 = 0.784\nIn n trials: P(at most n − 1) = 1 − p^n',
  'Subtract from one to get zero point seven eight four. In n independent trials, at most n minus one successes has probability one minus p to the nth power.')],
 e('PMF',5,9),expression='1-0.6**3',value='0.784'),

authored('counting-binomial-coefficient-nonnegative','Why combination counts are nonnegative',
 'From four labels A, B, C, D, count the 2-label subsets.\nCould a number of subsets be negative?','6; never negative',
 'From labels A, B, C, and D, count the two-label subsets. Could such a count ever be negative?',[
 ('LIST','Each subset is an unordered pair','AB, AC, AD, BC, BD, CD',
  'The subsets are A B, A C, A D, B C, B D, and C D.'),
 ('COUNT','A binomial coefficient counts these subsets','C(4, 2) = 6',
  'There are six subsets. This is what four choose two means.'),
 ('IMPOSSIBLE SELECTION','Zero subsets, never a negative number','Choose 5 from 4 distinct labels: 0 ways',
  'Choosing five distinct labels from only four is impossible. Its count is zero, not a negative number.'),
 ('PROBABILITY CONNECTION','Products of counts remain nonnegative','Subset counts are nonnegative integers.\nDivide by a positive total → nonnegative probability.',
  'Subset counts are nonnegative integers. Multiplying such counts and dividing by a positive total gives a nonnegative probability.')],
 e('PMF',7,10),expression='4*3/(2*1)',value='6'),

authored('counting-inclusive-index-range','Counting terms when an index starts at zero',
 'A sum has one term for each index k = 0, 1, …, 4.\nHow many terms are written?','5',
 'A sum has one term for each index k from zero through four. How many terms are written?',[
 ('LIST THE INDICES','Include both endpoints','0, 1, 2, 3, 4',
  'List zero, one, two, three, and four. Both endpoints are included.'),
 ('COUNT','There is one term for each listed index','5 indices → 5 terms',
  'There are five indices, so the sum has five written terms.'),
 ('INCLUSIVE RULE','Last index minus first index, plus one','4 − 0 + 1 = 5\nFrom 0 through n: n + 1 terms',
  'Subtract the first index from the last, then add one. From zero through n, there are n plus one terms.'),
 ('ZERO-VALUED TERMS','An included term can have value zero','Written terms ≠ necessarily nonzero terms',
  'An included term may have value zero. Counting the written terms does not mean every term is nonzero.')],
 e('PMF','7HW',1),expression='4-0+1',value='5'),

authored('probability-single-trial-failure','Finding a single-trial failure probability',
 'A fair spinner has 9 equal sectors, 4 green.\nSuccess means green. Find the failure probability q.','5/9',
 'A fair spinner has nine equal sectors, four green. Success means green. Find the probability of failure.',[
 ('SUCCESS','Count the favourable sectors','p = 4/9',
  'Four of the nine equally likely sectors are green, so success has probability four ninths.'),
 ('COMPLEMENT','Failure means any result that is not green','q = 1 − p',
  'Failure means not green. Success and failure have probabilities that add to one.'),
 ('SUBTRACT','Use a common denominator','q = 9/9 − 4/9 = 5/9',
  'Write one as nine ninths and subtract four ninths. Failure has probability five ninths.'),
 ('CHECK','Count the non-green sectors directly','9 − 4 = 5 non-green sectors\np + q = 4/9 + 5/9 = 1',
  'There are five non-green sectors out of nine, confirming five ninths. Success plus failure equals one.')],
 e('PMF',3,1),expression='1-4/9',value='5/9')
]


def lessons(doc):
    assert sum(1 for x in product(range(7),repeat=4))==2401
    assert 3**2*5**3==1125
    assert sum(F(comb(4,k),16) for k in [3,4])==F(5,16)
    return make_lessons(SPECS,doc)
