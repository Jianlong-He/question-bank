"""Checked examples for required choices, repeated selections and ordered rows."""
from math import comb,factorial
from itertools import permutations
from algebra_lessons import authored
from probability_lessons import enrichment as e
from card_lessons import make_lessons

SPECS=[
authored('counting-fixed-roles','Fix a required role before counting',
 'Eight people fill chair, secretary, and treasurer roles.\nNora must be chair. No person holds two roles. Count assignments.','42',
 'Eight people fill chair, secretary, and treasurer roles. Nora must be chair, and nobody holds two roles. Count the assignments.',[
 ('FIX THE REQUIRED CHOICE','The chair has only one allowed occupant','Chair: Nora\n7 other people remain.',
  'Fix Nora as chair before counting. Seven people remain for the other two roles.'),
 ('FILL THE OTHER ROLES','The two roles are different','Secretary: 7 choices\nTreasurer: 6 choices',
  'There are seven choices for secretary and six remaining choices for treasurer.'),
 ('MULTIPLY','Include the forced choice as a factor of one','1 × 7 × 6 = 42',
  'Multiply one, seven, and six. There are forty-two assignments.'),
 ('GENERALIZE','Remove fixed objects and fixed positions first','Count ordered choices among what remains.\nArrange all m remaining objects: m! orders.',
  'First remove fixed objects and their positions. Count ordered choices among what remains. If all remaining objects are arranged, use the factorial of their number.')],
 e('PeCo',1,10),expression='1*7*6',value='42'),

authored('counting-required-member','A committee with a required member',
 'Choose a committee of 4 from 9 people.\nJules must be included. How many committees are possible?','56',
 'Choose a committee of four from nine people. Jules must be included. How many committees are possible?',[
 ('INCLUDE THE REQUIRED MEMBER','Fill one of the four places first','Jules is included.\n3 places remain; 8 other people are available.',
  'Include Jules first. Three committee places remain, and eight other people are available.'),
 ('CHOOSE THE REST','The remaining members have equal roles','C(8, 3)',
  'Choose three of those eight people. Their order does not matter, so use a combination.'),
 ('EVALUATE','Divide the ordered count by 3!','C(8, 3) = (8 × 7 × 6)/(3 × 2 × 1) = 56',
  'Eight times seven times six, divided by six, gives fifty-six committees.'),
 ('GENERAL RULE','Reduce both the available pool and the required size','Choose r from n, including one specified person:\nC(n − 1, r − 1)',
  'With one specified person required, choose r minus one from n minus one. Reduce both numbers, not just the committee size.')],
 e('PeCo',2,9),expression='8*7*6/(3*2*1)',value='56'),

authored('counting-combination-symmetry','Choosing a set or its complement',
 'Use symmetry to evaluate C(14, 12).','91',
 'Use symmetry to evaluate fourteen choose twelve.',[
 ('COMPLEMENT','Choosing twelve determines which two are left out','14 − 12 = 2',
  'A choice of twelve from fourteen leaves exactly two out. The chosen group determines the omitted pair, and vice versa.'),
 ('SYMMETRY','Count the smaller complementary selection','C(14, 12) = C(14, 2)',
  'This one-to-one correspondence means fourteen choose twelve equals fourteen choose two.'),
 ('CALCULATE','An unordered pair divides the ordered count by two','C(14, 2) = (14 × 13)/2 = 91',
  'Fourteen times thirteen, divided by two, is ninety-one.'),
 ('GENERAL RULE','Chosen and omitted sets determine each other','C(n, r) = C(n, n − r)',
  'In general, n choose r equals n choose n minus r. Use whichever side makes the arithmetic easier.')],
 e('PeCo','3HW',1),expression='14*13/2',value='91'),

authored('counting-pairs-with-repetition','Unordered pairs when matching types are allowed',
 'Select 2 types from 8 tile types. Order does not matter,\nand choosing the same type twice is allowed. Count selections.','36',
 'Select two types from eight tile types. Order does not matter, and you may choose the same type twice. Count the selections.',[
 ('TWO DIFFERENT TYPES','Choose an unordered pair','C(8, 2) = (8 × 7)/2 = 28',
  'First count pairs of different types. Eight choose two is twenty-eight.'),
 ('TWO MATCHING TYPES','Choose the one repeated type','8 matching pairs',
  'For a matching pair, choose which of the eight types is repeated. That gives eight more selections.'),
 ('ADD DISJOINT CASES','Every pair is different-type or matching','28 + 8 = 36',
  'The cases do not overlap and cover every pair. Add twenty-eight and eight to get thirty-six.'),
 ('GENERAL RULE','Do not divide every ordered pair by two','From n types: C(n, 2) + n = n(n + 1)/2',
  'For n types, add n choose two and n. Matching pairs have only one visible order, so dividing every ordered pair by two would undercount.')],
 e('PeCo',3,8),expression='8*7/2+8',value='36'),

authored('counting-two-ordered-rows','Arranging distinct objects in two labelled rows',
 'Put 3 different books on shelves A and B, in order.\nCount arrangements with empty shelves allowed, then with both nonempty.','24; 12',
 'Put three different books on labelled shelves A and B, with order important on each shelf. Count arrangements allowing empty shelves, then requiring both nonempty.',[
 ('ORDER THE BOOKS','Read shelf A, then shelf B','3! = 6 orders\nExample order: X Y Z',
  'First order the three books. There are six orders. Read shelf A followed by shelf B.'),
 ('CHOOSE THE SPLIT','Allow a cut before, between, or after the books','|XYZ   X|YZ   XY|Z   XYZ|\n4 cuts per order',
  'Choose where to split an order. There are four cuts, including before all books or after all books.'),
 ('ALLOW EMPTY SHELVES','Multiply orders by cuts','3! × 4 = 24\nWith n books: (n + 1)n!',
  'Six orders times four cuts gives twenty-four. With n books and empty shelves allowed, use n plus one times n factorial.'),
 ('REQUIRE BOTH NONEMPTY','Use only internal cuts','X|YZ   XY|Z\n3! × 2 = 12\nWith n books: (n − 1)n!',
  'For two nonempty shelves, use only the two internal cuts. Six times two gives twelve. In general, there are n minus one internal cuts.')],
 e('PeCo',4,3),expression='6*4',value='24',equalities=[('6*2','12')]),

authored('counting-nonempty-ordered-rows','Splitting an order into several nonempty rows',
 'Arrange 7 distinct cards in 3 labelled nonempty rows.\nOrder matters within each row. Count arrangements.','75600',
 'Arrange seven distinct cards in three labelled rows. Every row must be nonempty, and order matters within each row. Count the arrangements.',[
 ('ORDER ALL CARDS','Read the rows in label order','7! = 5,040 card orders',
  'First order all seven cards, reading the rows in their label order. There are five thousand forty orders.'),
 ('INTERNAL GAPS','Nonempty rows require dividers between cards','7 cards have 6 internal gaps.\n3 rows need 2 dividers.',
  'Seven cards have six internal gaps. Three rows need two dividers, each in a different gap.'),
 ('CHOOSE DIVIDER LOCATIONS','The chosen gaps determine the row sizes','C(6, 2) = 15',
  'Choose two of the six gaps. There are fifteen ways to choose them.'),
 ('MULTIPLY','Each order and divider choice gives one arrangement','5,040 × 15 = 75,600\nFor n distinct objects, k nonempty labelled rows:\nn! × C(n − 1, k − 1)',
  'Multiply five thousand forty by fifteen to get seventy-five thousand six hundred. In general, multiply n factorial by n minus one choose k minus one.')],
 e('PeCo',4,9),expression='5040*15',value='75600'),

authored('counting-unlabelled-ordered-rows','Removing row labels without overcounting',
 'Split 5 distinct cards into 2 nonempty unlabelled rows.\nOrder within a row matters; swapping whole rows changes nothing.','240',
 'Split five distinct cards into two nonempty rows without labels. Order within each row matters, but swapping the whole rows changes nothing.',[
 ('TEMPORARILY LABEL','First call the rows A and B','5! = 120 orders of the cards',
  'Temporarily label the rows A and B. There are one hundred twenty orders of the five cards.'),
 ('SPLIT INTO NONEMPTY ROWS','Choose one internal gap','4 possible gaps\nLabelled count = 120 × 4 = 480',
  'Choose one of the four internal gaps to split the order. This gives four hundred eighty labelled arrangements.'),
 ('REMOVE THE LABELS','Each unlabelled arrangement appears twice','(row A, row B) and (row B, row A)',
  'Every unlabelled arrangement appears twice, once in each row order. The nonempty rows use distinct cards, so swapping them never leaves the labelled arrangement unchanged.'),
 ('DIVIDE','Count each pair of rows once','480/2 = 240',
  'Divide four hundred eighty by two to get two hundred forty unlabelled arrangements.')],
 e('PeCo','4HW',3),expression='120*4/2',value='240'),

authored('counting-two-rows-insertion','Building two ordered rows by insertion',
 'Insert 3 distinct cards, one at a time, into labelled rows A and B.\nEmpty rows are allowed. Count final arrangements.','24',
 'Insert three distinct cards, one at a time, into labelled rows A and B. Empty rows are allowed. Count the final arrangements.',[
 ('FIRST CARD','Each empty row offers one position','2 positions for the first card',
  'The first card has two possible positions, one in each empty row.'),
 ('COUNT THE GAPS','A row with a cards has a + 1 insertion positions','m cards already placed across both rows:\n(a + 1) + (m − a + 1) = m + 2 positions',
  'A row with a cards has a plus one insertion positions. Across two rows containing m cards, the total is m plus two.'),
 ('INSERT THE NEXT CARDS','The counts depend only on cards already placed','Second card: 3 positions\nThird card: 4 positions',
  'The second card therefore has three positions, and the third has four. This is true even if a row is empty.'),
 ('MULTIPLY','A fixed insertion order counts each result once','2 × 3 × 4 = 24\nFor n cards: 2 × 3 × … × (n + 1) = (n + 1)!',
  'Multiply two, three, and four to get twenty-four. A fixed insertion order gives each final arrangement exactly once. For n cards, the product is n plus one factorial.')],
 e('PeCo','4HW',4),expression='2*3*4',value='24',identities=[('(a+1)+(m-a+1)','m+2')]),

authored('counting-fixed-code-positions','Counting codes with specified positions',
 'A 5-character code uses A, B, C, D with repetition allowed.\nThe first two characters must be AB. How many codes?','64',
 'A five-character code uses A, B, C, and D, with repetition allowed. The first two characters must be A B. How many codes are possible?',[
 ('MARK FIXED POSITIONS','A specified character has one choice','A B _ _ _',
  'Fix the first two characters as A and B. Each fixed position has only one choice.'),
 ('COUNT FREE POSITIONS','Each remaining position may use any letter','Three free positions, 4 choices each',
  'Three positions remain free. Each can use any of the four letters.'),
 ('MULTIPLY','Include one factor for every position','1 × 1 × 4 × 4 × 4 = 64',
  'Multiply one, one, four, four, and four. There are sixty-four codes.'),
 ('GENERAL RULE','Count free positions wherever they occur','m symbols and f free positions → m^f codes\nFixed positions contribute factors of 1.',
  'With m allowed symbols and f free positions, use m to the power f. The free positions need not be adjacent. Fixed positions contribute factors of one.')],
 e('counting-and-classification',4,7),expression='4**3',value='64'),

authored('counting-identical-pair-adjacency','An identical pair together or apart',
 'Arrange the letters of PEPPER.\nCount arrangements with the two Es together, then apart.','20 together; 40 apart',
 'Arrange the letters of pepper. Count arrangements with both E letters together, then with them apart.',[
 ('ALL ARRANGEMENTS','There are three Ps and two Es','All orders = 6!/(3! × 2!) = 60',
  'There are six letters, including three copies of P and two of E. The total number of distinct arrangements is sixty.'),
 ('MAKE AN IDENTICAL BLOCK','Treat EE as one object','[EE], P, P, P, R\n5 objects, with P repeated 3 times',
  'For adjacent E letters, make one E E block. There are five objects, with P still repeated three times.'),
 ('TOGETHER','Identical Es have only one internal order','5!/3! = 120/6 = 20',
  'Five factorial divided by three factorial gives twenty. Do not multiply by two for swapping identical letters.'),
 ('APART','Subtract the adjacent cases from all cases','60 − 20 = 40',
  'Every arrangement has the E letters together or apart. Subtract twenty from sixty to get forty with the E letters apart.')],
 e('PCF',5,10),expression='60-20',value='40',equalities=[('720/(6*2)','60'),('120/6','20')]),
]


def lessons(doc):
    assert comb(8,3)==56 and comb(14,12)==91
    assert comb(8+1,2)==36
    assert factorial(7)*comb(6,2)==75600
    words={''.join(p) for p in permutations('PEPPER')}
    assert len(words)==60 and sum('EE' in w for w in words)==20
    return make_lessons(SPECS,doc)
