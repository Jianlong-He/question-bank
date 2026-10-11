"""Finite waiting times, geometric trials, hypergeometric sampling and counts."""
from fractions import Fraction as F
from itertools import combinations
from math import comb, prod
from algebra_lessons import authored
from probability_lessons import enrichment
from number_sense_lessons import source
from card_lessons import make_lessons

SPECS=[
authored('probability-first-success','First success without replacement',
 '5 red and 4 blue balls; no replacement.\nFind P(first red on draw 3).','5/42',
 "A bag has five red and four blue balls. Draw without replacement. Let's find the probability that the first red ball appears on draw three.",[
 ('REQUIRED ORDER','First red on draw 3 means two blues first','Blue → blue → red',
  'The required order is blue, blue, then red. A red on either earlier draw would not count.'),
 ('UPDATE COUNTS','Remove each drawn blue ball','First blue: 4/9\nSecond blue: 3/8\nThen red: 5/7',
  'The first blue has probability four ninths. The next blue has probability three eighths. Then five reds remain among seven balls.'),
 ('MULTIPLY','Multiply the conditional probabilities','(4/9) × (3/8) × (5/7) = 60/504',
  'Multiply four ninths, three eighths, and five sevenths. The product is sixty over five hundred four.'),
 ('SIMPLIFY','The waiting time fixes the order','60/504 = 5/42',
  'Simplify to five forty-seconds. Do not multiply by rearrangements: the first red must be in the third position.')],
 enrichment('PMF',1,3),expression='4/9*3/8*5/7',value='5/42'),

authored('probability-first-success-first','A first success on the first draw',
 '6 red and 5 blue balls. X is the draw of the first red.\nFind p(1) = P(X = 1).','6/11',
 "A bag contains six red and five blue balls. X is the draw on which the first red appears. Let's find p of one.",[
 ('READ THE NOTATION','p(1) is a probability, not a ball count','p(1) = P(first red on draw 1)',
  'P of one means the probability that the first red appears on the first draw.'),
 ('COUNT','No earlier draw has changed the bag','6 red + 5 blue = 11 balls',
  'Before the first draw, all eleven balls are present. Six are red.'),
 ('DIVIDE','Choose uniformly from the original bag','p(1) = 6/11',
  'The probability of red on that first draw is six elevenths.'),
 ('FIRST DRAW ONLY','Replacement after a draw cannot change the first draw','P(X = 1) = 6/11',
  'Whether later balls are replaced does not affect this first-draw probability. There are no previous failures to include.')],
 enrichment('PMF',1,1),expression='6/(6+5)',value='6/11'),

authored('probability-first-success-support','The latest possible first success',
 '2 red and 5 blue balls; no replacement.\nWhat is the latest draw on which the first red can appear?','6',
 "A bag has two red and five blue balls. Draw without replacement until the first red. What is the latest possible draw for that first red?",[
 ('DELAY SUCCESS','Draw every blue ball before any red','Blue → blue → blue → blue → blue',
  'To delay the first red as long as possible, draw all five blue balls first.'),
 ('NEXT DRAW','After five blues, only red balls remain','Draw 6 must be red.',
  'After those five draws, only the two red balls remain. Draw six must be red.'),
 ('COUNT','Maximum failures before success, plus one','Largest X = 5 + 1 = 6',
  'The largest possible waiting time is the number of blue balls plus one. That is six.'),
 ('SUPPORT','A red can also appear earlier','Possible X: 1, 2, 3, 4, 5, 6',
  'The first red can appear on any draw from one through six. Seven is impossible, because a red must already have appeared by draw six.')],
 enrichment('PMF',1,6),expression='5+1',value='6'),

authored('probability-first-success-total','A complete waiting-time distribution',
 '2 red and 2 blue balls; no replacement.\nX is the draw of the first red. Find p(1) + p(2) + p(3).','1',
 "A bag has two red and two blue balls. Draw without replacement. Let's add the probabilities of the first red appearing on draws one, two, or three.",[
 ('FIRST DRAW','Red immediately','p(1) = 2/4 = 1/2',
  'A red immediately has probability two fourths, or one half.'),
 ('SECOND DRAW','One blue, then red','p(2) = (2/4) × (2/3) = 1/3',
  'For the second draw, get blue then red. Two fourths times two thirds is one third.'),
 ('THIRD DRAW','Two blues, then a guaranteed red','p(3) = (2/4) × (1/3) × (2/2) = 1/6',
  'For the third draw, get both blues first, then red. This has probability one sixth.'),
 ('ADD ALL CASES','These disjoint cases cover every possibility','1/2 + 1/3 + 1/6 = 1',
  'The three probabilities add to one. They cover every possible first-red position without overlapping.')],
 enrichment('PMF',1,5),expression='1/2+1/3+1/6',value='1',equalities=[('2/4*2/3','1/3'),('2/4*1/3*2/2','1/6')]),

authored('pattern-pmf-90d35baa0439','Geometric first success',
 'Independent attempts succeed with probability 0.4.\nFind P(first success on attempt 5).','0.05184',
 "Independent attempts each succeed with probability zero point four. Let's find the probability that the first success is on attempt five.",[
 ('REQUIRED SEQUENCE','Four failures, then one success','Failure probability = 1 − 0.4 = 0.6\nF → F → F → F → S',
  'The first four attempts must fail, and the fifth must succeed. A failure has probability zero point six.'),
 ('MULTIPLY','Independence lets us multiply','P(X = 5) = 0.6⁴ × 0.4',
  'Multiply four failure probabilities by one success probability. That is zero point six to the fourth power, times zero point four.'),
 ('CALCULATE','There is only one allowed order','0.6⁴ × 0.4 = 0.1296 × 0.4 = 0.05184',
  'The result is zero point zero five one eight four. There is no combinations factor because the success must be last.'),
 ('GENERAL RULE','Count k − 1 failures before success','P(X = k) = (1 − p)ᵏ⁻¹ × p',
  'In general, use k minus one failures followed by one success. This geometric rule needs independent trials with a constant success probability.')],
 enrichment('PMF',2,3),expression='0.6**4*0.4',value='0.05184'),

authored('pattern-pmf-4be2809cd266','Geometric tails and cumulative probabilities',
 'Independent attempts succeed with probability 0.4.\nFind P(X > 4) and P(X ≤ 4), where X is the first success.','0.1296 and 0.8704',
 "Attempts succeed independently with probability zero point four. X is the first success. Let's find the probability of waiting more than four attempts, and at most four.",[
 ('MORE THAN FOUR','All first four attempts must fail','P(X > 4) = 0.6⁴',
  'More than four means the first four attempts all fail. Each failure has probability zero point six.'),
 ('TAIL PROBABILITY','No success factor is needed yet','P(X > 4) = 0.1296',
  'Raise zero point six to the fourth power to get zero point one two nine six. We do not require a success on attempt five.'),
 ('AT MOST FOUR','Use the complementary event','P(X ≤ 4) = 1 − 0.1296 = 0.8704',
  'At most four is the complement. Subtract from one to get zero point eight seven zero four.'),
 ('GENERAL RULES','Separate an exact time from a waiting-time interval','P(X > t) = (1 − p)ᵗ\nP(X ≤ t) = 1 − (1 − p)ᵗ',
  'For more than t attempts, use t failures. For a success by attempt t, subtract that tail probability from one.')],
 enrichment('PMF',2,8),expression='0.6**4',value='0.1296',equalities=[('1-0.6**4','0.8704')]),

authored('pattern-pmf-bfe65fc756d0','Sampling without replacement using combinations',
 '6 red and 7 blue balls; choose 4 uniformly.\nFind P(exactly 2 red), without replacement.','63/143',
 "Choose four balls uniformly from six red and seven blue balls, without replacement. Let's find the probability of exactly two reds.",[
 ('COUNT ALL SAMPLES','Order does not matter','Total = C(13, 4) = 715',
  'There are thirteen balls. Choosing four without regard to order gives thirteen choose four, or seven hundred fifteen possible samples.'),
 ('COUNT FAVOURABLE SAMPLES','Two red requires two blue as well','C(6, 2) × C(7, 2) = 15 × 21 = 315',
  'Choose two of the six reds and two of the seven blues. Fifteen times twenty-one gives three hundred fifteen favourable samples.'),
 ('DIVIDE','All four-ball samples are equally likely','P(exactly 2 red) = 315/715 = 63/143',
  'Divide three hundred fifteen by seven hundred fifteen. This simplifies to sixty-three over one hundred forty-three.'),
 ('GENERAL FORM','Use the sample size in both colour counts','P(X = k) = C(m, k) C(N − m, n − k) / C(N, n)\nN = total; m = red; n = drawn; k = red drawn',
  'This is the hypergeometric rule: choose the required successes and failures, then divide by the number of all samples.')],
 enrichment('PMF',6,1),expression='15*21/715',value='63/143'),

authored('probability-expected-count','Predicting an expected count',
 'An event has probability 0.35 on each of 160 trials.\nHow many occurrences are expected?','56',
 "An event has probability zero point three five on each of one hundred sixty trials. How many occurrences should we expect?",[
 ('IDENTIFY','Read the number of trials and the probability','n = 160; p = 0.35',
  'There are one hundred sixty trials, each with probability zero point three five for the event.'),
 ('RULE','Expected count is trials times probability','Expected count = n × p',
  'Multiply the number of trials by the probability of the event.'),
 ('CALCULATE','Multiply the two given values','160 × 0.35 = 56',
  'One hundred sixty times zero point three five is fifty-six.'),
 ('INTERPRET','An average prediction is not a guarantee','Expected occurrences: 56\nAn actual set of trials may differ.',
  'We expect fifty-six occurrences on average. An actual set of trials can have more or fewer; fifty-six is not guaranteed.')],
 source(10,13,1,8),expression='160*0.35',value='56'),
]


def lessons(doc):
    assert F(4,9)*F(3,8)*F(5,7)==F(5,42)
    assert [2/(4-k) for k in range(3)]==[.5,2/3,1]
    # Enumerate uniformly shuffled colour positions to check finite waiting times.
    waits=[min(red)+1 for red in combinations(range(4),2)]
    assert [F(waits.count(k),len(waits)) for k in range(1,4)]==[F(1,2),F(1,3),F(1,6)]
    assert max(min(red)+1 for red in combinations(range(7),2))==6
    assert comb(13,4)==715 and comb(6,2)==15 and comb(7,2)==21
    assert sum(comb(6,k)*comb(7,4-k) for k in range(5))==comb(13,4)
    assert sum(F(3,5)**(k-1)*F(2,5) for k in range(1,5))==1-F(3,5)**4
    return make_lessons(SPECS,doc)
