"""Fresh examples for enrichment unions, complements, and double counting."""
from fractions import Fraction as F
from itertools import combinations_with_replacement
from algebra_lessons import authored
from probability_lessons import enrichment
from card_lessons import make_lessons

def e(w,q):return enrichment('conditional-probability',w,q)
SPECS=[
authored('probability-exclusive-sets','Decide whether events are mutually exclusive',
 'A fair spinner has numbers 1 to 8.\nA = {1,2,3} and B = {6,7}.\nAre A and B mutually exclusive? Find P(A or B).','Yes; 5/8',
 'A fair spinner has numbers one to eight. A contains one, two, and three. B contains six and seven. Are they mutually exclusive, and what is the probability of A or B?',[
 ('LOOK FOR AN OVERLAP','Can one outcome belong to both events?','A = {1,2,3}     B = {6,7}\nNo common outcome',
 'Compare the sets. They have no common outcome, so they cannot happen together. They are mutually exclusive.'),
 ('COUNT THE UNION','Or includes any outcome in either set','A or B = {1,2,3,6,7}\n5 favourable outcomes out of 8',
 'Their union has five outcomes. None has been counted twice.'),
 ('ADD DISJOINT PROBABILITIES','There is no overlap to subtract','P(A or B) = 3/8 + 2/8 = 5/8',
 'Add three eighths and two eighths to get five eighths.'),
 ('COMPARE AN OVERLAPPING PAIR','One shared outcome is enough to rule out exclusivity','If C = {3,4}, then A and C share 3.\nA and C are not mutually exclusive.',
 'For comparison, let C contain three and four. A and C share three, so that pair is not mutually exclusive.')],e(3,1),expression='3/8+2/8',value='5/8'),
authored('probability-domino-union','Count a union in an unordered domino set',
 'A double-four set has one tile for each unordered\npair from 0 to 4, including doubles. Choose a tile uniformly.\nFind P(the tile contains 1 or 3).','3/5',
 'A double-four domino set has one tile for each unordered pair from zero to four, including doubles. Find the probability that a uniformly chosen tile contains one or three.',[
 ('COUNT ALL TILES','Reversing a tile does not make a new tile','5 doubles + C(5,2) different pairs\n= 5 + 10 = 15 tiles',
 'There are five doubles and ten pairs of different numbers, making fifteen tiles.'),
 ('COUNT EACH EVENT','Each target pairs with every number from zero to four','5 tiles contain 1.\n5 tiles contain 3.',
 'Five tiles contain one, and five contain three. Each target can pair with any of the five numbers.'),
 ('REMOVE THE OVERLAP','The tile with one and three belongs to both groups','5 + 5 − 1 = 9 favourable tiles',
 'The one-three tile was counted twice. Subtract it once, leaving nine favourable tiles.'),
 ('DIVIDE','Use the number of tiles as the denominator','P(contains 1 or 3) = 9/15 = 3/5',
 'Divide by the fifteen equally likely tiles. The probability is three fifths. Count tiles, not orientations.')],e(3,3),expression='(5+5-1)/15',value='3/5'),
authored('probability-card-union','Count overlapping card categories',
 'Draw one card from a standard 52-card deck.\nWhat is the probability it is red or a face card?','8/13',
 'Draw one card from a standard fifty-two-card deck. What is the probability it is red or a face card?',[
 ('COUNT THE CATEGORIES','Face cards are jacks, queens, and kings','Red cards: 2 suits × 13 = 26\nFace cards: 4 suits × 3 = 12',
 'Two red suits give twenty-six red cards. Jacks, queens, and kings give twelve face cards.'),
 ('COUNT THE INTERSECTION','Find cards belonging to both categories','Red face cards: 2 suits × 3 = 6',
 'Each red suit has three face cards. Six cards belong to both categories.'),
 ('ADD, THEN SUBTRACT ONCE','Or includes the overlap, counted once','26 + 12 − 6 = 32\nP(red or face) = 32/52 = 8/13',
 'Add twenty-six and twelve, then subtract the six counted twice. Thirty-two out of fifty-two simplifies to eight thirteenths.'),
 ('ADAPT THE CATEGORY COUNTS','For other unions, count the shared cards again','One suit: 13 cards. One rank: 4 cards.\nA suit and a rank share exactly 1 card.',
 'For a suit and a single rank, use thirteen and four, with one shared card. Always count the overlap for the categories given.')],e(3,4),expression='(26+12-6)/52',value='8/13'),
authored('counting-two-set-union-neither','Count two overlapping groups and neither',
 'Of 90 students, 47 join coding, 38 join robotics,\nand 16 join both. How many join at least one?\nHow many join neither?','69 at least one; 21 neither',
 'Of ninety students, forty-seven join coding, thirty-eight join robotics, and sixteen join both. How many join at least one, and how many join neither?',[
 ('ADD THE GROUP COUNTS','The students in both groups are counted twice','47 + 38 = 85',
 'Adding the two group counts gives eighty-five, but this counts each student in both groups twice.'),
 ('REMOVE ONE COPY OF THE OVERLAP','At least one includes both','At least one = 47 + 38 − 16 = 69',
 'Subtract sixteen once. Sixty-nine students join at least one group.'),
 ('TAKE THE COMPLEMENT','Everyone else joins neither group','Neither = 90 − 69 = 21',
 'Subtract sixty-nine from the full group of ninety. Twenty-one students join neither.'),
 ('CHECK DISJOINT REGIONS','Every student belongs to one region','Coding only: 31     Both: 16\nRobotics only: 22     Neither: 21\n31 + 16 + 22 + 21 = 90',
 'Check the separate regions: thirty-one coding only, sixteen both, twenty-two robotics only, and twenty-one neither. They total ninety.')],e(3,5),expression='47+38-16',value='69',equalities=[('90-69','21'),('31+16+22+21','90')]),
authored('probability-three-set-union','Three overlapping groups: union and neither',
 'Among 100 people: A has 42, B has 35, C has 30.\nThe pairwise overlaps AB, AC, BC are 15, 12, 10;\nall three overlap in 5. Find the union and neither.','75 in union; 25 neither',
 'Among one hundred people, groups A, B, and C have forty-two, thirty-five, and thirty members. Pairwise overlaps are fifteen, twelve, and ten, including five in all three. Find the union and neither.',[
 ('ADD THE SINGLES','Begin with all three group counts','42 + 35 + 30 = 107',
 'Start by adding all three group counts. The total is one hundred seven.'),
 ('SUBTRACT PAIRWISE OVERLAPS','Then restore the triple overlap once','107 − 15 − 12 − 10 + 5 = 75',
 'Subtract the three pairwise overlaps, then add back the triple overlap. The union has seventy-five people.'),
 ('WHY ADD THE TRIPLE BACK?','Track one person belonging to all three','Counted 3 times, subtracted 3 times:\n3 − 3 + 1 = 1',
 'Someone in all three was added three times and subtracted three times. Adding once more counts that person exactly once.'),
 ('COMPLEMENT AND PROBABILITY','Divide by the total for probabilities','Neither: 100 − 75 = 25\nP(at least one) = 75/100 = 0.75\nP(neither) = 25/100 = 0.25',
 'Twenty-five belong to none. For probabilities, divide the union or neither count by one hundred. The same inclusion-exclusion rule also works directly with probabilities.')],e(3,6),expression='42+35+30-15-12-10+5',value='75'),
authored('probability-two-multiples-union','Probability of either of two divisibility conditions',
 'Choose an integer uniformly from 1 through 80.\nFind P(divisible by 6 or by 9).','17/80',
 'Choose an integer uniformly from one through eighty. Find the probability it is divisible by six or by nine.',[
 ('COUNT EACH SET','Count whole multiples within the range','Multiples of 6: 13, ending at 78\nMultiples of 9: 8, ending at 72',
 'There are thirteen multiples of six and eight multiples of nine. Ignore any incomplete group beyond the upper limit.'),
 ('FIND THE OVERLAP','A number divisible by both is a multiple of the LCM','LCM(6,9) = 18\nShared multiples: 18, 36, 54, 72',
 'The shared numbers are multiples of the least common multiple, eighteen. There are four within the range.'),
 ('COUNT THE UNION','Subtract the shared count once','13 + 8 − 4 = 17',
 'Add thirteen and eight, then subtract four. Seventeen integers satisfy at least one condition.'),
 ('DIVIDE BY ALL OUTCOMES','The original range contains eighty integers','P(divisible by 6 or 9) = 17/80',
 'Divide seventeen by eighty. For a range starting at one, count multiples by dividing the upper limit and taking only the whole-number part.')],e('3HW',4),expression='(13+8-4)/80',value='17/80'),
authored('probability-three-multiples-union','Three divisibility conditions using inclusion-exclusion',
 'Choose an integer uniformly from 1 through 72.\nFind P(divisible by 4, 6, or 9).','7/18',
 'Choose an integer uniformly from one through seventy-two. Find the probability it is divisible by four, six, or nine.',[
 ('COUNT SINGLES','Divide by each divisor to count its multiples','4: 18 multiples     6: 12 multiples\n9: 8 multiples',
 'There are eighteen multiples of four, twelve of six, and eight of nine.'),
 ('COUNT INTERSECTIONS','Use the least common multiple for every overlap','LCM(4,6) = 12 → 6 multiples\nLCM(4,9) = 36 → 2 multiples\nLCM(6,9) = 18 → 4 multiples',
 'The pairwise least common multiples are twelve, thirty-six, and eighteen. Their counts are six, two, and four.'),
 ('RESTORE THE TRIPLE','All three conditions require a multiple of thirty-six','LCM(4,6,9) = 36 → 2 multiples\n18 + 12 + 8 − 6 − 2 − 4 + 2 = 28',
 'All three conditions require a multiple of thirty-six. Add that count back after subtracting the pairwise counts. The union contains twenty-eight numbers.'),
 ('CONVERT TO PROBABILITY','Divide the union count by the full range','28/72 = 7/18',
 'Divide twenty-eight by seventy-two to get seven eighteenths. Adding the triple overlap back makes every qualifying number count once.')],e('3Rev',4),expression='(18+12+8-6-2-4+2)/72',value='7/18'),
authored('probability-exactly-one-of-two','Probability that exactly one of two events occurs',
 'P(A) = 0.62, P(B) = 0.39, and P(both) = 0.18.\nFind P(exactly one of A and B).','0.65',
 'A has probability zero point six two, B has zero point three nine, and both has probability zero point one eight. Find the probability that exactly one occurs.',[
 ('REMOVE BOTH FROM A','Keep only outcomes in A but not B','P(A only) = 0.62 − 0.18 = 0.44',
 'Subtract the overlap from A. A only has probability zero point four four.'),
 ('REMOVE BOTH FROM B','Keep only outcomes in B but not A','P(B only) = 0.39 − 0.18 = 0.21',
 'Subtract the same overlap from B. B only has probability zero point two one.'),
 ('ADD THE EXCLUSIVE PARTS','A only and B only cannot occur together','P(exactly one) = 0.44 + 0.21 = 0.65',
 'Add the two exclusive parts. The answer is zero point six five.'),
 ('GENERAL RULE','The overlap must be removed from both counts','P(exactly one) = P(A) + P(B) − 2P(both)',
 'The general rule subtracts twice the overlap. Exactly one excludes outcomes where both events occur.')],e(3,9),expression='.62+.39-2*.18',value='.65'),
authored('probability-fixed-membership-count','Use double counting to find participation',
 'Each participant joins exactly two of four workshops.\nOthers join none. Workshop participation rates are\n0.18, 0.26, 0.22, 0.14. Find P(joining none).','0.60',
 'Each participant joins exactly two of four workshops, and everyone else joins none. The workshop participation rates are eighteen, twenty-six, twenty-two, and fourteen percent. Find the probability of joining none.',[
 ('ADD ALL MEMBERSHIPS','A participant appears in two workshop counts','0.18 + 0.26 + 0.22 + 0.14 = 0.80',
 'The participation rates sum to zero point eight. This counts workshop memberships, with each participant counted twice.'),
 ('COUNT PEOPLE ONCE','Divide by the fixed number of workshops per participant','P(participating) = 0.80/2 = 0.40',
 'Divide by two because every participant joins exactly two workshops. Forty percent participate.'),
 ('FIND THE COMPLEMENT','Everyone else participates in none','P(none) = 1 − 0.40 = 0.60',
 'Subtract forty percent from one hundred percent. Sixty percent join none.'),
 ('CHECK THE ASSUMPTION','The same participation count must apply to everyone','Exactly k memberships each:\nparticipation rate = sum of membership rates / k',
 'This shortcut depends on each participant having the same number of memberships. Divide by that fixed count, then take the complement.')],e(3,8),expression='1-(.18+.26+.22+.14)/2',value='.60'),
]

def lessons(doc):
 tiles=list(combinations_with_replacement(range(5),2))
 assert len(tiles)==15 and sum(1 in t or 3 in t for t in tiles)==9
 assert sum(n%6==0 or n%9==0 for n in range(1,81))==17
 assert sum(any(n%k==0 for k in [4,6,9]) for n in range(1,73))==28
 # The eight disjoint regions are all nonnegative and total one hundred.
 assert sum([20,15,13,10,7,5,5,25])==100
 return make_lessons(SPECS,doc)
