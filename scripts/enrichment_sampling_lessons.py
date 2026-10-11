"""Sampling and conditional counting examples for enrichment."""
from fractions import Fraction as F
from itertools import product
from math import comb,prod
from algebra_lessons import authored
from probability_lessons import enrichment
from card_lessons import make_lessons

def e(w,q):return enrichment('conditional-probability',w,q)
SPECS=[
authored('probability-mixed-sampling-stages','Combine independent and dependent sampling stages',
 'Spin a fair spinner numbered 1 to 5, then independently\ndraw two cards without replacement from a 52-card deck.\nFind P(spinner above 3 and both cards red).','5/51',
 'Spin a fair spinner numbered one to five, then independently draw two cards without replacement. Find the probability the spinner is above three and both cards are red.',[
 ('SPINNER STAGE','Four and five satisfy the spinner condition','P(above 3) = 2/5',
 'Two of the five spinner outcomes are above three. That probability is two fifths.'),
 ('FIRST CARD','Two of the four suits are red','P(first red) = 26/52 = 1/2',
 'There are twenty-six red cards among fifty-two. The first red probability is one half.'),
 ('SECOND CARD','Update the deck after a red card is removed','P(second red | first red) = 25/51',
 'After removing a red card, twenty-five red cards remain among fifty-one cards.'),
 ('MULTIPLY ALONG THE PATH','Only the spinner stage is independent of the card draws','(2/5) × (26/52) × (25/51) = 5/51',
 'Multiply the three probabilities to get five fifty-firsts. Use a conditional probability for the second card because there is no replacement.')],e(4,3),expression='(2/5)*(26/52)*(25/51)',value='5/51'),
authored('probability-three-colours-replacement','Three different colours with replacement',
 'A bag has 2 red, 3 blue, and 4 green balls.\nDraw three times with replacement.\nFind P(all three recorded colours are different).','16/81',
 'A bag has two red, three blue, and four green balls. Draw three times with replacement. Find the probability that all three recorded colours are different.',[
 ('ONE ORDER','Start with red, then blue, then green','P(R,B,G) = (2/9)(3/9)(4/9) = 24/729',
 'For red, blue, then green, multiply two ninths, three ninths, and four ninths. Replacement keeps the denominators at nine.'),
 ('COUNT COLOUR ORDERS','Each colour must appear once','RBG, RGB, BRG, BGR, GRB, GBR\n3! = 6 orders',
 'All three different means each colour appears once. The three colours have six possible orders.'),
 ('ADD EQUAL DISJOINT CASES','Each order has the same product','6 × 24/729 = 144/729 = 16/81',
 'Each order has the same probability, and the orders are disjoint. Multiply by six and simplify to sixteen eighty-firsts.'),
 ('CHECK THE MODEL','Balls are equally likely, but colours need not be','Use colour counts / total balls at each draw.',
 'Do not assume the colours are equally likely. Use their different ball counts. Replacement makes the successive draws independent.')],e(4,7),expression='6*2*3*4/9**3',value='16/81'),
authored('probability-birthday-complement','A shared birthday using the complement',
 'Eight people have independent birthdays, each uniform\namong 365 days. Ignore leap day. Find P(at least two\nshare a birthday), rounded to four decimal places.','0.0743',
 'Eight people have independent birthdays uniformly spread over three hundred sixty-five days, ignoring leap day. Find the chance that at least two share a birthday, to four decimal places.',[
 ('USE ALL DIFFERENT','The complement is that nobody shares a birthday','Shared birthday = complement of all different',
 'Use the complement: all eight birthdays are different.'),
 ('COUNT SUCCESSIVE CHOICES','Keep the denominator fixed at three hundred sixty-five','P(all different)\n= (365 × 364 × … × 358)/365⁸',
 'The first birthday can be anything. Each later person must avoid the previous birthdays. The allowed counts decrease from three hundred sixty-five to three hundred fifty-eight.'),
 ('SUBTRACT','Keep full precision until the final rounding','P(shared) = 1 − P(all different)\n≈ 0.0743353',
 'Multiply the eight fractions, then subtract from one. Keep full precision until the final rounding.'),
 ('ROUND','Use four digits after the decimal point','P(at least two share) ≈ 0.0743',
 'The answer rounds to zero point zero seven four three. At least two includes any shared pair or larger group.')],e(4,8),expression='1-(365*364*363*362*361*360*359*358)/365**8',value=str(1-prod(F(365-i,365) for i in range(8)))),
authored('probability-distinct-repeated-draws','All different in independent repeated selections',
 'A three-character code uses digits 0 through 6.\nEvery code is equally likely; repetition and leading zero\nare allowed. Find P(all three digits are different).','30/49',
 'A three-character code uses digits zero through six. Every code is equally likely, including leading zero and repeats. Find the probability all three digits are different.',[
 ('FIRST DIGIT','Any of the seven digits is allowed','First digit: 7/7',
 'The first digit can be any of the seven possibilities.'),
 ('AVOID PREVIOUS DIGITS','Selection still comes from all seven digits each time','Second differs: 6/7\nThird differs from both: 5/7',
 'The second must avoid one previous digit, giving six sevenths. The third must avoid two, giving five sevenths.'),
 ('MULTIPLY CONDITIONAL CHANCES','The denominator stays fixed for each selection','(7/7)(6/7)(5/7) = 210/343 = 30/49',
 'Multiply these conditional chances. The probability is thirty forty-ninths.'),
 ('GENERAL PATTERN','For k selections from m equally likely values','P(all different)\n= m(m−1)…(m−k+1) / m^k, for k ≤ m',
 'For k selections from m values, the favourable choices decrease by one at each step. The total choices remain m at every step.')],e('4HW',5),expression='7*6*5/7**3',value='30/49'),
authored('probability-specified-pair-selected','Two specified people in a chosen group',
 'Choose 4 winners uniformly from 18 students,\nwithout replacement. Find the probability that\nZoe and Max are both winners.','2/51',
 'Choose four winners uniformly from eighteen students, without replacement. Find the probability that Zoe and Max are both winners.',[
 ('FIRST SPECIFIED PERSON','Four of eighteen winner positions are available','P(Zoe wins) = 4/18',
 'Zoe has probability four eighteenths of being selected.'),
 ('CONDITION ON THAT SELECTION','One winner place and one student are now removed','P(Max wins | Zoe wins) = 3/17',
 'Given that Zoe wins, three winner places remain among seventeen other students. Max has probability three seventeenths.'),
 ('MULTIPLY','Both people must be selected','(4/18)(3/17) = 12/306 = 2/51',
 'Multiply to get two fifty-firsts.'),
 ('GROUP INTERPRETATION','The same rule applies to a particular team','Two named people in a group of size r from n:\n(r/n) × ((r−1)/(n−1))',
 'This also works for two named people on a particular team. Use that team size for the selected group size, not the number of teams.')],e(4,10),expression='4/18*3/17',value='2/51'),
authored('probability-bayes-hidden-type','Update a hidden type after observing repeated outcomes',
 'A device is type A with probability 0.30, otherwise B.\nType A flashes red independently with chance 0.40 per trial;\nB never flashes red. After two nonred trials, find P(type A).','27/202',
 'A device has a thirty percent chance of being type A. Type A independently flashes red with probability zero point four per trial; type B never does. After two nonred trials, find the chance of type A.',[
 ('LIKELIHOODS','Compute the observed result under each type','P(two nonred | A) = 0.60² = 0.36\nP(two nonred | B) = 1',
 'Under A, two nonred results have probability zero point three six. Under B, they are certain.'),
 ('WEIGHT BY THE PRIOR','Count the two disjoint ways to observe nonred','A and nonred: 0.30 × 0.36 = 0.108\nB and nonred: 0.70 × 1 = 0.70',
 'Multiply each likelihood by its type probability. The two joint probabilities are zero point one zero eight and zero point seven.'),
 ('TOTAL OBSERVED PROBABILITY','Add across both possible device types','P(two nonred) = 0.108 + 0.70 = 0.808',
 'Add them to find the probability of the observed result: zero point eight zero eight.'),
 ('BAYES UPDATE','Divide the desired joint probability by the observed total','P(A | two nonred) = 0.108/0.808 = 27/202',
 'Divide the A joint probability by the observed total. The updated probability is twenty-seven over two hundred two.')],e(6,5),expression='.30*.60**2/(.30*.60**2+.70)',value='27/202'),
authored('probability-condition-distinct-values','Condition on a number of distinct values',
 'Roll four independent fair six-sided dice.\nGiven that at least three distinct values appear,\nfind P(exactly three distinct values).','2/3',
 'Roll four independent fair six-sided dice. Given that at least three distinct values appear, find the probability that exactly three appear.',[
 ('EXACTLY THREE VALUES','One value repeats and the other two appear once','Choose values: C(6,3) = 20\nChoose the repeated value: 3\nArrange: 4!/2! = 12',
 'Choose three values, then which one repeats. The four results have twelve distinct orders because one value is repeated.'),
 ('COUNT BOTH ALLOWED CASES','At least three means exactly three or exactly four','Exactly three: 20 × 3 × 12 = 720\nExactly four: 6 × 5 × 4 × 3 = 360',
 'Exactly three gives seven hundred twenty ordered outcomes. Exactly four gives three hundred sixty.'),
 ('RESTRICT THE DENOMINATOR','Only outcomes satisfying the condition remain','P(exactly three | at least three)\n= 720/(720 + 360) = 2/3',
 'Use only these two cases in the denominator. Seven hundred twenty over one thousand eighty is two thirds.'),
 ('CHECK THE CONDITION','Exclude outcomes with only one or two values','Conditional count = favourable / allowed',
 'Do not divide by all possible dice outcomes. The given condition excludes rolls with fewer than three distinct values.')],e(6,10),expression='720/(720+360)',value='2/3'),
]

def lessons(doc):
 assert round(1-prod(F(365-i,365) for i in range(8)),4)==F('0.0743')
 assert sum(len(set(t))==3 for t in product(range(6),repeat=4))==720
 assert sum(len(set(t))==4 for t in product(range(6),repeat=4))==360
 assert F(comb(16,2),comb(18,4))==F(2,51)
 return make_lessons(SPECS,doc)
