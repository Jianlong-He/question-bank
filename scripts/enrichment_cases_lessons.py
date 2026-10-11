"""Counting constraints verified by exhaustive finite enumeration."""
from itertools import product,combinations_with_replacement,permutations
from math import prod,comb,factorial
from algebra_lessons import authored
from probability_lessons import enrichment as e
from card_lessons import make_lessons

SPECS=[
authored('counting-all-equal-choices','Count choices when everyone must match',
 'Four friends each choose a number from 1 to 7.\nHow many ordered choices have all four numbers equal?','7',
 'Four friends each choose a number from one to seven. How many ordered choices have all four numbers equal?',[
 ('CHOOSE THE SHARED VALUE','There are seven possible common numbers','Shared value: 1, 2, 3, 4, 5, 6, or 7',
  'Choose the number they will all share. There are seven possible values.'),
 ('THE REST ARE FORCED','Once one value is chosen, nobody has another choice','7 × 1 × 1 × 1',
  'Once the first value is chosen, every other friend must match it. Each remaining choice is forced.'),
 ('COUNT','Each shared value gives one ordered outcome','(1,1,1,1), (2,2,2,2), …, (7,7,7,7)\nTotal = 7',
  'There is one matching outcome for each number, giving seven ordered outcomes.'),
 ('GENERAL RULE','Count the possible shared values','m allowed values → m all-equal outcomes',
  'With m allowed values, there are m all-equal outcomes. Multiplying independent choices would ignore the matching constraint.')],
 e('PCF',6,3),expression='7*1*1*1',value='7'),

authored('counting-triples-fixed-product','Count ordered triples with a fixed product',
 'Three friends each choose a number from 1 to 4.\nHow many ordered triples have product exactly 12?','9',
 'Three friends each choose a number from one to four. How many ordered triples have product exactly twelve?',[
 ('SORT FIRST','List triples in nondecreasing order','Only (1,3,4) and (2,2,3) have product 12.',
  'List sorted triples first. With smallest value one, the other values must be three and four. With smallest value two, they must be two and three.'),
 ('CHECK COMPLETENESS','A smallest value of three is already too large','3 × 3 × 3 = 27 > 12',
  'If the smallest value were at least three, the product would be at least twenty-seven. There are no more cases.'),
 ('COUNT DISTINCT ORDERS','Repeated values reduce the number of orders','(1,3,4): 3! = 6\n(2,2,3): 3!/2! = 3',
  'Three distinct values have six orders. The triple with two twos has three orders because exchanging the twos changes nothing.'),
 ('ADD DISJOINT CASES','Every ordered triple belongs to exactly one sorted case','6 + 3 = 9',
  'Add the two disjoint cases. There are nine ordered triples.')],
 e('PCF',6,6),expression='6+3',value='9',equalities=[('1*3*4','12'),('2*2*3','12')]),

authored('counting-triples-product-threshold','Count ordered triples above a product threshold',
 'Three friends each choose a number from 1 to 4.\nHow many ordered triples have product greater than 24?','11',
 'Three friends each choose a number from one to four. How many ordered triples have product greater than twenty-four?',[
 ('SORT AND TEST','List only nondecreasing triples that pass','(2,4,4), (3,3,3), (3,3,4), (3,4,4), (4,4,4)',
  'Use sorted triples to avoid duplicate cases. No triple starting with one works. Starting with two, only two four four works. The remaining four triples start with three or four.'),
 ('COUNT EACH CASE','All equal: one order. Two equal: three orders.','(2,4,4): 3     (3,3,3): 1\n(3,3,4): 3     (3,4,4): 3     (4,4,4): 1',
  'An all-equal triple has one order. A triple with exactly two equal values has three orders.'),
 ('ADD','Sorted cases do not overlap','3 + 1 + 3 + 3 + 1 = 11',
  'Add the order counts to get eleven.'),
 ('RESPECT THE BOUNDARY','Greater than excludes equality','(2,3,4) has product 24, so it is excluded.',
  'The inequality is strict. For example, two three four has product exactly twenty-four, so it is excluded.')],
 e('PCF',6,7),expression='3+1+3+3+1',value='11'),

authored('counting-dice-consecutive-runs','Count dice that form a consecutive run',
 'Roll three distinguishable six-sided dice.\nHow many outcomes show three consecutive values,\nin any order?','24',
 'Roll three distinguishable six-sided dice. How many outcomes show three consecutive values, in any order?',[
 ('CHOOSE THE RUN','List every allowed set of consecutive values','{1,2,3}, {2,3,4}, {3,4,5}, {4,5,6}',
  'There are four possible sets of consecutive values, starting at one, two, three, or four.'),
 ('ASSIGN VALUES TO DICE','All three values in a run are distinct','3! = 3 × 2 × 1 = 6 orders',
  'For each set, its three distinct values can be assigned to the three distinguishable dice in six orders.'),
 ('MULTIPLY','Four disjoint sets, six orders each','4 × 6 = 24',
  'Multiply four runs by six orders. There are twenty-four outcomes.'),
 ('CHECK THE MODEL','Dice labels make different orders distinct','Choose a run, then permute its values.',
  'Each ordered outcome belongs to just one run. Dice labels make different orders distinct, so both counting stages are necessary.')],
 e('PCF',6,8),expression='4*6',value='24'),

authored('counting-exact-target-positions','Count codes with an exact number of target digits',
 'A four-character code uses digits 0 through 5.\nRepetition and leading zero are allowed.\nHow many codes contain exactly two 5s?','150',
 'A four-character code uses digits zero through five. Repetition and leading zero are allowed. How many codes contain exactly two fives?',[
 ('CHOOSE POSITIONS','Choose which two positions contain five','C(4,2) = 6',
  'Choose two of the four positions for the fives. There are six choices.'),
 ('FILL THE OTHER POSITIONS','Each remaining digit must not be five','Digits allowed there: 0, 1, 2, 3, 4\n5 × 5 = 25',
  'The other two positions must avoid five. Each has five choices, giving twenty-five completions.'),
 ('MULTIPLY','The selected positions contain fixed digits','6 × 25 = 150',
  'Multiply six position choices by twenty-five completions. The two fives themselves require no further choices.'),
 ('CHECK EXACTLY','Do not allow another five in the remaining positions','Exactly two 5s → 150 codes',
  'There are one hundred fifty codes. Keeping five out of the other positions ensures exactly two fives.')],
 e('PCF','6Rev',4),expression='6*5**2',value='150'),

authored('counting-codes-at-least-one-target','Count codes containing at least one target digit',
 'A four-character code uses digits 0 through 5.\nRepetition and leading zero are allowed.\nHow many codes contain at least one 3?','671',
 'A four-character code uses digits zero through five. Repetition and leading zero are allowed. How many codes contain at least one three?',[
 ('ALL CODES','Every position has six choices','6⁴ = 1,296',
  'There are six choices in each of four positions, giving one thousand two hundred ninety-six total codes.'),
 ('NONE OF THE TARGET','Avoid three in every position','5⁴ = 625',
  'If a code contains no three, each position has only five choices. That gives six hundred twenty-five codes.'),
 ('SUBTRACT THE COMPLEMENT','Remove codes with no threes','1,296 − 625 = 671',
  'Subtract codes with no threes from all codes. The result is six hundred seventy-one.'),
 ('GENERAL RULE','At least one includes every positive count','At least one = all − none',
  'This subtraction includes codes with one, two, three, or four threes, each exactly once.')],
 e('PCF',6,10),expression='6**4-5**4',value='671'),

authored('counting-exactly-one-empty-shelf','Arrange books with exactly one empty shelf',
 'Five different books go on two labelled shelves.\nExactly one shelf must be empty; book order matters.\nHow many arrangements are possible?','240',
 'Five different books go on two labelled shelves. Exactly one shelf must be empty, and book order matters. How many arrangements are possible?',[
 ('CHOOSE THE USED SHELF','All five books must go on the other shelf','2 choices for the nonempty shelf',
  'Exactly one empty shelf means all five books go together on the other shelf. Choose which shelf is used.'),
 ('ORDER THE BOOKS','The five books are all distinct','5! = 5 × 4 × 3 × 2 × 1 = 120',
  'The five different books can be ordered in one hundred twenty ways.'),
 ('MULTIPLY','Shelf choice and book order both matter','2 × 120 = 240',
  'Multiply two shelf choices by one hundred twenty orders to get two hundred forty arrangements.'),
 ('CHECK THE RESTRICTION','Splitting the books would leave neither shelf empty','Choose one used shelf, then order all books there.',
  'Do not split books between the shelves. That would violate the requirement that one shelf is empty.')],
 e('PeCo','4HW',2),expression='2*120',value='240'),

authored('counting-pascal-identity','Use Pascal’s identity for combination counts',
 'Use C(9,3) = 84 and C(9,2) = 36\nto find C(10,3).','120',
 'Use nine choose three equals eighty-four, and nine choose two equals thirty-six, to find ten choose three.',[
 ('SPLIT BY ONE PERSON','A three-person group either includes or excludes Alex','Exclude Alex: choose 3 of the other 9.\nInclude Alex: choose 2 of the other 9.',
  'Single out Alex. A three-person group either excludes Alex, choosing three others, or includes Alex, choosing two others.'),
 ('ADD THE TWO CASES','The cases are disjoint and cover every group','C(10,3) = C(9,3) + C(9,2)',
  'These cases do not overlap, and together they cover every group. Add their counts.'),
 ('CALCULATE','Use the two given counts','84 + 36 = 120',
  'Eighty-four plus thirty-six is one hundred twenty.'),
 ('PASCAL’S IDENTITY','Combine neighbours in the same row','C(n,k) + C(n,k−1) = C(n+1,k)',
  'Pascal\'s identity adds neighbouring combination counts. Increase n by one and keep the larger selection size k.')],
 e('PeCo',3,4),expression='84+36',value='120'),

authored('counting-permutation-overcount-factor','How often ordered selections count each group',
 'P(14,6) counts ordered selections of six objects.\nHow many times is each unordered six-object group counted?','720 times',
 'Fourteen permute six counts ordered selections of six objects. How many times is each unordered six-object group counted?',[
 ('FIX ONE GROUP','Its six distinct members are already chosen','Same six members; different possible orders',
  'Fix one group of six objects. We are counting its possible orders, not choosing its members again.'),
 ('COUNT THE ORDERS','Each order represents the same unordered group','6! = 6 × 5 × 4 × 3 × 2 × 1',
  'Six distinct objects have six factorial orders.'),
 ('EVALUATE','Multiply the descending factors','6! = 720',
  'Six factorial is seven hundred twenty. Every unordered group appears seven hundred twenty times in the ordered count.'),
 ('REMOVE OVERCOUNTING','Divide by the number of orders per group','C(n,k) = P(n,k)/k!\nConversely: P(n,k) = C(n,k) × k!',
  'Divide an ordered count by k factorial to count unordered groups. Multiply by k factorial to reverse the conversion.')],
 e('PeCo',1,6),expression='6*5*4*3*2*1',value='720'),

authored('pattern-pcf-1c8d6c2baaec','Count stacked boxes across several shelves',
 'Five shelves each hold boxes stacked 2 wide,\n5 deep, and 3 high. How many boxes are there in all?','150 boxes',
 'Five shelves each hold boxes stacked two wide, five deep, and three high. How many boxes are there in all?',[
 ('ONE LAYER','Width times depth counts boxes in one layer','2 × 5 = 10 boxes',
  'One layer has two times five, or ten boxes.'),
 ('ONE SHELF','Multiply by the number of layers','10 × 3 = 30 boxes',
  'Three layers make thirty boxes on one shelf.'),
 ('ALL SHELVES','Each of the five shelves holds thirty boxes','5 × 30 = 150 boxes',
  'Five shelves with thirty boxes each contain one hundred fifty boxes.'),
 ('CHECK THE FACTORS','Count each level of grouping once','5 shelves × 2 wide × 5 deep × 3 high = 150',
  'The four factors represent shelves, width, depth, and height. Include each grouping level exactly once.')],
 e('PCF',1,9),expression='5*2*5*3',value='150'),

authored('counting-two-category-selections','Choose required numbers from two categories',
 'Choose 2 science books from 8 and 3 history books from 6.\nAll books are distinct, and order does not matter.\nHow many selections are possible?','560',
 'Choose two science books from eight and three history books from six. All books are distinct, and order does not matter. How many selections are possible?',[
 ('SCIENCE CHOICES','Choose an unordered pair','C(8,2) = 8 × 7 ÷ 2 = 28',
  'Choose two science books from eight. Eight choose two is twenty-eight.'),
 ('HISTORY CHOICES','Choose an unordered group of three','C(6,3) = 6 × 5 × 4 ÷ (3 × 2 × 1) = 20',
  'Choose three history books from six. Six choose three is twenty.'),
 ('MULTIPLY','Every science choice pairs with every history choice','28 × 20 = 560',
  'Every science pair can go with every history group. Multiply twenty-eight by twenty to get five hundred sixty selections.'),
 ('GENERAL RULE','Respect the required count in each category','C(8,2) × C(6,3), rather than C(14,5)',
  'Choosing any five of all fourteen books would include wrong category counts. Choose within each category, then multiply.')],
 e('PeCo',2,10),expression='28*20',value='560'),
]


def lessons(doc):
    triples=list(product(range(1,5),repeat=3))
    assert sum(prod(t)==12 for t in triples)==9
    assert [t for t in combinations_with_replacement(range(1,5),3) if prod(t)==12]==[(1,3,4),(2,2,3)]
    above={t:len(set(permutations(t))) for t in combinations_with_replacement(range(1,5),3) if prod(t)>24}
    assert above=={(2,4,4):3,(3,3,3):1,(3,3,4):3,(3,4,4):3,(4,4,4):1}
    assert sum(prod(t)>24 for t in triples)==sum(above.values())==11
    assert sum(len(set(t))==3 and max(t)-min(t)==2 for t in product(range(1,7),repeat=3))==24
    codes=list(product(range(6),repeat=4))
    assert sum(t.count(5)==2 for t in codes)==150
    assert sum(3 in t for t in codes)==671
    assert sum(len(set(t))==1 for t in product(range(1,8),repeat=4))==7
    assert comb(9,3)==84 and comb(9,2)==36 and comb(10,3)==120
    assert factorial(6)==720 and 2*factorial(5)==240
    assert comb(8,2)*comb(6,3)==560
    return make_lessons(SPECS,doc)
