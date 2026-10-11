"""Original probability examples with exact fractions and enumerated checks."""
from fractions import Fraction as F
from math import comb
from algebra_lessons import authored
from number_sense_lessons import source
from card_lessons import make_lessons


def enrichment(topic, worksheet, qid):
    unit = {'counting-and-classification': 1, 'PCF': 2, 'PeCo': 3,
            'conditional-probability': 4, 'PMF': 5}[topic]
    return (f'worksheets/enrichment/counting-and-probability 1/U{unit}{topic}/E-CP1U{unit}W{worksheet}.csv',str(qid))


SPECS = [
authored('probability-equally-likely','Equally likely outcomes',
 'A spinner has 12 equal sections.\n5 are purple. Find P(purple).', '5/12',
 "A fair spinner has twelve equal sections, five of them purple. Let's find the probability of purple.",[
 ('COUNT ALL OUTCOMES','Each equal section is equally likely','Total sections = 12',
  'There are twelve equally likely sections. This is the denominator.'),
 ('COUNT FAVOURABLE OUTCOMES','Count the sections that meet the condition','Purple sections = 5',
  'Five sections are purple. This is the numerator.'),
 ('DIVIDE','Favourable outcomes divided by all outcomes','P(purple) = 5/12',
  'Divide five by twelve. The probability of purple is five twelfths.'),
 ('CHECK','Use this counting rule for equally likely outcomes','0 ≤ 5/12 ≤ 1',
  'Five twelfths is between zero and one. Counting outcomes this way works because all twelve sections are equally likely.')],
 source(7,7,2,3),expression='5/12',value='5/12'),

authored('probability-experimental','Experimental probability',
 'An event occurs 17 times in 64 trials.\nEstimate its probability to 3 decimal places.', '0.266',
 "An event occurs seventeen times in sixty-four trials. Let's estimate its probability to three decimal places.",[
 ('OBSERVE','Use the recorded outcomes','Occurrences = 17; trials = 64',
  'Experimental probability uses recorded results. We observed seventeen occurrences out of sixty-four trials.'),
 ('DIVIDE','Occurrences divided by trials','17/64 = 0.265625',
  'Divide seventeen by sixty-four. The result is zero point two six five six two five.'),
 ('ROUND','The fourth decimal digit is 6','0.265625 → 0.266',
  'Keep three decimal places. The next digit is six, so round the five up to six. The estimate is zero point two six six.'),
 ('INTERPRET','An estimate from this set of observations','Experimental probability ≈ 0.266',
  'This is an estimate from the observations. A new set of trials can give a different result.')],
 source(7,7,2,6),expression='17/64',value='0.265625'),

authored('probability-independent','Independent events',
 'Independent events A and B have\nP(A) = 0.65 and P(B) = 0.40. Find P(both).', '0.26',
 "Independent events A and B have probabilities zero point six five and zero point four. Let's find the probability that both occur.",[
 ('INDEPENDENCE','One event does not change the other’s probability','P(B given A) = P(B)',
  'Independence means knowing that A occurred does not change the probability of B.'),
 ('MULTIPLY','Use the multiplication rule for independent events','P(A and B) = P(A) × P(B)',
  'For independent events, multiply their probabilities to find the probability of both.'),
 ('SUBSTITUTE','Multiply the two given values','0.65 × 0.40 = 0.26',
  'Zero point six five times zero point four is zero point two six.'),
 ('INTERPRET','Both events occur together','P(both) = 0.26 = 26%',
  'The probability of both events is twenty-six percent. The multiplication rule extends to several mutually independent events.')],
 source(12,8,'1Rev',3),expression='0.65*0.40',value='0.26'),

authored('probability-without-replacement','Drawing without replacement',
 'A bag has 7 yellow and 4 blue balls.\nDraw 2 without replacement. Find P(both yellow).', '21/55',
 "A bag has seven yellow and four blue balls. Two are drawn without replacement. Let's find the probability that both are yellow.",[
 ('FIRST DRAW','Start with all 11 balls','P(first yellow) = 7/11',
  'There are eleven balls, and seven are yellow. The first probability is seven elevenths.'),
 ('SECOND DRAW','Assume the first ball was yellow','6 yellow among 10 remaining\nP(second yellow given first yellow) = 6/10',
  'After a yellow ball is removed, six yellow balls remain among ten balls. The second probability is six tenths.'),
 ('MULTIPLY','Multiply along this sequence','(7/11) × (6/10) = 42/110',
  'Multiply the first probability by the conditional second probability. This gives forty-two over one hundred ten.'),
 ('SIMPLIFY','Both the numerator and denominator changed','42/110 = 21/55',
  'Simplify to twenty-one fifty-fifths. Without replacement, update the remaining counts before each draw.')],
 source(7,7,5,4),expression='7/11*6/10',value='21/55'),

authored('probability-sample-space','Counting a compound sample space',
 'Flip a coin and spin a 7-section spinner.\nHow many possible ordered outcomes are there?', '14',
 "Flip a coin and spin a spinner with seven sections numbered one through seven. How many ordered outcomes are possible?",[
 ('FIRST CHOICE','List the coin outcomes','Heads or tails: 2 possibilities',
  'The coin has two possible outcomes: heads or tails.'),
 ('SECOND CHOICE','Each coin result can pair with every section','For heads: H1, H2, H3, H4, H5, H6, H7\nFor tails: T1, T2, T3, T4, T5, T6, T7',
  'Each coin result pairs with seven spinner results. There are seven heads pairs and seven tails pairs.'),
 ('MULTIPLY','Count every ordered pair once','2 × 7 = 14 outcomes',
  'Multiply two by seven. There are fourteen ordered outcomes in the sample space.'),
 ('EXTEND','Multiply the available choices at each stage','If all 14 pairs are equally likely:\nP(one specified pair) = 1/14',
  'If all fourteen pairs are equally likely, any one specified pair has probability one fourteenth. Counting and probability are connected.')],
 source(7,7,3,1),expression='2*7',value='14'),

authored('probability-addition-rule','The probability addition rule',
 'P(A) = 0.45; P(B) = 0.32; P(both) = 0.14.\nFind P(A or B).', '0.63',
 "Event A has probability zero point four five, B has zero point three two, and both have zero point one four. Let's find A or B.",[
 ('INCLUDE EITHER EVENT','Or includes the overlap','P(A or B) = P(A) + P(B) − P(both)',
  'Or includes A, B, or both. Add the two probabilities, then subtract their overlap once.'),
 ('ADD','This counts the overlap twice','0.45 + 0.32 = 0.77',
  'First add zero point four five and zero point three two. The total is zero point seven seven.'),
 ('REMOVE THE EXTRA OVERLAP','Subtract the intersection once','0.77 − 0.14 = 0.63',
  'Subtract the overlap, zero point one four. The probability is zero point six three.'),
 ('SPECIAL CASE','Mutually exclusive events have no overlap','P(A or B) = 0.63\nNo overlap → simply add.',
  'Our answer is sixty-three percent. Mutually exclusive events have zero overlap, so their probabilities simply add.')],
 source(10,13,4,2),expression='0.45+0.32-0.14',value='0.63'),

authored('probability-complements','At least one: use the complement',
 'Flip a fair coin 6 independent times.\nFind P(at least one head).', '63/64',
 "A fair coin is flipped six independent times. Let's find the probability of at least one head.",[
 ('OPPOSITE EVENT','No heads means six tails','At least one head ↔ not all tails',
  'The opposite of at least one head is no heads at all. That means six tails.'),
 ('CALCULATE THE OPPOSITE','Multiply the six independent probabilities','P(all tails) = (1/2)⁶ = 1/64',
  'Each tail has probability one half. Six independent tails have probability one half to the sixth power, or one sixty-fourth.'),
 ('SUBTRACT FROM ONE','Complementary probabilities add to 1','P(at least one head) = 1 − 1/64',
  'An event and its complement have probabilities that add to one. Subtract one sixty-fourth from one.'),
 ('ANSWER','Write 1 as 64/64','64/64 − 1/64 = 63/64',
  'The answer is sixty-three sixty-fourths. Using the opposite event avoids listing every sequence with a head.')],
 enrichment('conditional-probability',2,3),expression='1-(1/2)**6',value='63/64'),

authored('probability-conditional','Conditional probability',
 'A fair spinner is numbered 1 to 12.\nGiven a result greater than 5, find P(even).', '4/7',
 "A fair spinner is numbered one through twelve. Given that its result is greater than five, what is the probability that it is even?",[
 ('RESTRICT','Keep only outcomes satisfying the condition','Possible now: 6, 7, 8, 9, 10, 11, 12',
  'The condition rules out one through five. Seven equally likely results remain: six through twelve.'),
 ('COUNT SUCCESSES','Count the even results within that smaller set','Even results: 6, 8, 10, 12',
  'Four of the remaining results are even: six, eight, ten, and twelve.'),
 ('DIVIDE','Use the restricted total as the denominator','P(even given greater than 5) = 4/7',
  'Divide four by seven. Use the restricted total of seven, because the condition is already known.'),
 ('GENERAL RULE','Count only within the given condition','P(A given B) = P(A and B)/P(B)\nP(B) must be positive.',
  'In general, divide the probability of both events by the probability of the given event. That denominator must be positive.')],
 enrichment('conditional-probability',1,2),expression='4/7',value='4/7'),

authored('probability-discrete-distribution','Completing a probability distribution',
 'X: 0, 1, 2, 3\nP(X): 0.12, 0.28, ?, 0.35. Find P(X = 2).', '0.25',
 "A distribution has probabilities zero point one two, zero point two eight, an unknown, and zero point three five. Let's find the missing probability.",[
 ('CHECK THE RULES','Probabilities are nonnegative and sum to 1','Every probability ≥ 0\nAll probabilities together = 1',
  'A probability distribution has no negative probabilities, and all its probabilities add to one.'),
 ('ADD THE KNOWN VALUES','Calculate the probability already assigned','0.12 + 0.28 + 0.35 = 0.75',
  'The known probabilities add to zero point seven five.'),
 ('SUBTRACT','Use the remaining probability','P(X = 2) = 1 − 0.75 = 0.25',
  'Subtract from one. The missing probability, at X equals two, is zero point two five.'),
 ('VERIFY BOTH RULES','Check nonnegativity and the total','0.12 + 0.28 + 0.25 + 0.35 = 1',
  'All four probabilities are nonnegative and their sum is one. Both distribution rules are satisfied.')],
 enrichment('PMF',1,8),expression='1-(0.12+0.28+0.35)',value='0.25',equalities=[('0.12+0.28+0.25+0.35','1')]),

authored('probability-expected-value','Expected value',
 'X: −3, 2, 8\nProbabilities: 0.40, 0.35, 0.25. Find E(X).', '1.5',
 "A random variable takes values negative three, two, and eight, with probabilities point four, point three five, and point two five. Let's find its expected value.",[
 ('WEIGHT EACH OUTCOME','Multiply each value by its probability','E(X) = sum of value × probability',
  'Expected value is a weighted average. Multiply each value by its probability, then add the products.'),
 ('CALCULATE PRODUCTS','Keep the sign of each value','−3 × 0.40 = −1.20\n2 × 0.35 = 0.70;   8 × 0.25 = 2',
  'The products are negative one point two, zero point seven, and two.'),
 ('ADD','Combine the weighted values','E(X) = −1.20 + 0.70 + 2 = 1.50',
  'Adding gives one point five.'),
 ('INTERPRET','A long-run average, not a guaranteed result','Expected value = 1.5\nPossible outcomes: −3, 2, 8',
  'Over many repetitions, the average tends toward one point five. Expected value need not be one of the possible outcomes.')],
 source(12,8,5,10),expression='-3*0.40+2*0.35+8*0.25',value='1.5',equalities=[('0.40+0.35+0.25','1')]),

authored('probability-binomial','Exactly k successes',
 '5 independent shots; success probability 0.7 each.\nFind P(exactly 3 successes).', '0.3087',
 "Five independent shots each succeed with probability zero point seven. Let's find the probability of exactly three successes.",[
 ('CHECK THE MODEL','Fixed trials, two outcomes, constant probability','n = 5; k = 3; p = 0.7; failure = 0.3',
  'This is binomial: five fixed trials, success or failure, independence, and the same success probability each time.'),
 ('ONE ORDER','Three successes and two failures','0.7³ × 0.3² = 0.03087',
  'One particular order of three successes and two failures has probability zero point seven cubed times zero point three squared.'),
 ('COUNT THE ORDERS','Choose which 3 of the 5 trials succeed','C(5, 3) = (5 × 4 × 3)/(3 × 2 × 1) = 10',
  'Choose three of five positions. Five times four times three, divided by three times two times one, gives ten possible orders.'),
 ('MULTIPLY','Include all ten possible orders','P(X = 3) = 10 × 0.03087 = 0.3087',
  'Multiply by ten. The probability of exactly three successes is zero point three zero eight seven.')],
 source(11,11,1,5),expression='10*0.7**3*0.3**2',value='0.3087',equalities=[('0.7**3*0.3**2','0.03087')]),
]


def lessons(doc):
    assert comb(5,3)==10
    assert sum(comb(5,k)*F(7,10)**k*F(3,10)**(5-k) for k in range(6))==1
    restricted=[x for x in range(1,13) if x>5]
    assert F(sum(x%2==0 for x in restricted),len(restricted))==F(4,7)
    assert len([(coin,spin) for coin in 'HT' for spin in range(1,8)])==14
    assert round(F(17,64),3)==F(266,1000)
    return make_lessons(SPECS,doc)
