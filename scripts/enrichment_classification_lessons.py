"""Counting classification, forbidden cases, and arithmetic structures."""
from itertools import product
from algebra_lessons import authored
from probability_lessons import enrichment
from card_lessons import make_lessons

def e(w,q):return enrichment('counting-and-classification',w,q)
SPECS=[
authored('counting-square-four-products','Expand a numerical square and recognise its four products',
 'Use 11 = 5 + 6 to calculate 11 × 11\nby extended distribution. Then rewrite the\nfour partial products as one square.','121',
 'Use eleven equals five plus six to calculate eleven times eleven by extended distribution. Then rewrite the four partial products as one square.',[
 ('SPLIT BOTH FACTORS','Each factor has the same two parts','11 × 11 = (5 + 6)(5 + 6)',
 'Write both elevens as five plus six.'),
 ('PAIR EVERY PART','Every term in one factor multiplies each term in the other','5×5 + 5×6 + 6×5 + 6×6',
 'Multiply five by five and six, then six by five and six. There are four partial products.'),
 ('ADD','The middle products are separate contributions','25 + 30 + 30 + 36 = 121',
 'Add twenty-five, thirty, thirty, and thirty-six. The result is one hundred twenty-one.'),
 ('REVERSE THE PROCESS','Group the four terms to recover the square','5(5 + 6) + 6(5 + 6)\n= (5 + 6)(5 + 6) = 11²',
 'Going backwards, group the first two terms and the last two. Factor out the shared sum. The four products become eleven squared.')],e(1,7),expression='11*11',value='121',equalities=[('5*5+5*6+6*5+6*6','121')]),
authored('arithmetic-split-regroup-factors','Split factors to make a convenient product',
 'Use commutation and convenient grouping\nto calculate 24 × 35.','840',
 'Use commutation and convenient grouping to calculate twenty-four times thirty-five.',[
 ('FACTOR THE NUMBERS','Choose factors that will make friendly pairs','24 × 35 = (6 × 4)(7 × 5)',
 'Split twenty-four into six times four, and thirty-five into seven times five.'),
 ('REORDER AND REGROUP','Changing factor order and grouping preserves the product','6 × 4 × 7 × 5 = (6 × 7)(4 × 5)',
 'Reorder the factors so six pairs with seven and four pairs with five.'),
 ('MULTIPLY FRIENDLY PAIRS','Work with forty-two times twenty','42 × 20 = 840',
 'The pairs give forty-two and twenty. Their product is eight hundred forty.'),
 ('CHECK THE FACTORS','Every original factor must appear exactly once','Commutation changes order.\nAssociation changes grouping.\nNeither changes the product.',
 'Keep every factor exactly once. Commutation changes their order, and association changes their grouping, while preserving the product.')],e(1,9),expression='24*35',value='840',equalities=[('6*4*7*5','42*20')]),
authored('counting-fixed-row-table','Count one row and the whole choice table',
 'A choice table has 4 rows for a first choice\nand 3 columns for a second choice.\nHow many entries are in one row, and in the whole table?','3 in one row; 12 total',
 'A choice table has four rows for a first choice and three columns for a second choice. Count the entries in one row, and in the whole table.',[
 ('FIX THE FIRST CHOICE','One row keeps the first choice unchanged','Row A: (A,1), (A,2), (A,3)',
 'In one row, the first choice is fixed. The second choice can be one, two, or three.'),
 ('COUNT THAT ROW','There is one entry for each column','One row has 3 entries.',
 'There are three entries in that row, one for each column.'),
 ('COUNT ALL ROWS','Each of the four rows has three entries','4 × 3 = 12 entries in the whole table',
 'The entire table has four rows of three, so there are twelve entries.'),
 ('DISTINGUISH THE REQUESTS','One row and all rows use different counts','Fixed row → number of columns\nWhole table → rows × columns',
 'For one fixed row, count columns only. For the whole table, multiply rows by columns.')],e(3,2),expression='4*3',value='12'),
authored('counting-forbidden-role-pair','Count ordered roles excluding a forbidden pair',
 'Choose a captain and assistant from 9 children.\nAri and Ren refuse to serve together.\nHow many valid assignments are possible?','70',
 'Choose a captain and assistant from nine children. Ari and Ren refuse to serve together. How many valid assignments are possible?',[
 ('COUNT WITHOUT RESTRICTIONS','Roles differ and one person cannot fill both','9 × 8 = 72 assignments',
 'Choose any of nine captains, then any of eight other assistants. There are seventy-two unrestricted assignments.'),
 ('LIST FORBIDDEN ASSIGNMENTS','The pair can occupy the roles in either order','Captain Ari, assistant Ren\nCaptain Ren, assistant Ari',
 'Exactly two assignments put the forbidden pair together: Ari then Ren, or Ren then Ari.'),
 ('SUBTRACT','Every other assignment is allowed','72 − 2 = 70',
 'Subtract these two assignments. Seventy valid assignments remain.'),
 ('CHECK BY CASES','Split according to the captain','Captain Ari or Ren: 2 × 7 = 14\nOther captain: 7 × 8 = 56\n14 + 56 = 70',
 'As a check, a captain from the pair has seven assistant choices. Each of seven other captains has eight. Fourteen plus fifty-six is seventy.')],e(2,10),expression='9*8-2',value='70'),
authored('counting-two-digit-comparison','Classify two-digit numbers by their tens digit',
 'Use only digits 0 through 5 to form two-digit numbers.\nCount those with tens > ones,\nthen those with tens < ones.','15 greater; 10 smaller',
 'Use only digits zero through five to form two-digit numbers. Count those with tens greater than ones, then those with tens smaller than ones.',[
 ('CHOOSE THE TENS DIGIT','A two-digit number cannot start with zero','Tens digit: 1, 2, 3, 4, or 5',
 'The tens digit must be one through five. Zero cannot start a two-digit number.'),
 ('TENS GREATER','For tens digit t, the ones can be zero through t minus one','Tens:    1   2   3   4   5\nChoices: 1   2   3   4   5\nTotal = 15',
 'For tens digits one through five, the smaller ones digits give one, two, three, four, and five choices. Add to get fifteen.'),
 ('TENS SMALLER','Count allowed digits strictly above the tens digit','Tens:    1   2   3   4   5\nChoices: 4   3   2   1   0\nTotal = 10',
 'For the reverse inequality, the choice counts are four, three, two, one, and zero. There are ten numbers.'),
 ('CHECK THE PARTITION','Equal digits form a third category','15 greater + 10 smaller + 5 equal\n= 30 = 5 tens choices × 6 ones choices',
 'The five equal-digit numbers complete the count. Together the three categories give all thirty allowed two-digit numbers.')],e(3,8),expression='1+2+3+4+5',value='15',equalities=[('4+3+2+1','10'),('15+10+5','5*6')]),
authored('counting-labelled-dice-boundaries','Count dice thresholds by disjoint cases',
 'Roll labelled blue and red dice, each numbered 1 to 7.\nCount outcomes with sum at least 11,\nthen outcomes with product at least 21.','10 sum; 15 product',
 'Roll labelled blue and red dice, each numbered one to seven. Count outcomes with sum at least eleven, then outcomes with product at least twenty-one.',[
 ('LABEL THE OUTCOMES','Blue and red values form ordered pairs','(blue, red): (4,7) differs from (7,4).',
 'The dice are labelled, so swapping unequal values gives another outcome.'),
 ('COUNT SUM CASES','Fix blue and count qualifying red values','Blue 4, 5, 6, 7 → 1, 2, 3, 4 choices\n1 + 2 + 3 + 4 = 10',
 'For blue four, five, six, and seven, there are one, two, three, and four qualifying red values. Add to get ten.'),
 ('COUNT PRODUCT CASES','Include products equal to twenty-one','Blue 3, 4, 5, 6, 7 → 1, 2, 3, 4, 5 choices\n1 + 2 + 3 + 4 + 5 = 15',
 'For products at least twenty-one, blue three through seven allow one through five choices. Their sum is fifteen.'),
 ('READ THE BOUNDARY','Strictly greater and at least are different conditions','At least includes equality.\nStrictly greater excludes equality.',
 'Check the boundary in each question. At least includes equality. Strictly greater excludes it. Count each blue-value case once.')],e(3,9),expression='1+2+3+4',value='10',equalities=[('1+2+3+4+5','15')]),
authored('counting-avoid-short-word','Count codes avoiding a forbidden consecutive word',
 'Five-character codes use S, U, N, A, B, with repeats allowed.\nHow many do not contain the consecutive word SUN?','3050',
 'Five-character codes use the letters S, U, N, A, and B, with repeats allowed. How many do not contain the consecutive word SUN?',[
 ('COUNT ALL CODES','Every position has five choices','5⁵ = 3,125',
 'There are five choices for each of five positions, giving three thousand one hundred twenty-five codes.'),
 ('PLACE THE FORBIDDEN WORD','Three starting positions leave two free letters','SUNxx, xSUNx, xxSUN\nEach form: 5² = 25 codes',
 'SUN can start in three positions. Each placement fixes three letters and leaves two free, giving twenty-five codes.'),
 ('CHECK FOR DOUBLE COUNTING','Two copies cannot fit or overlap in a five-letter code','SUN has no matching prefix and suffix.\nTwo disjoint copies would need 6 positions.',
 'These cases cannot overlap. SUN has no matching prefix and suffix, and two separate copies would need six positions.'),
 ('SUBTRACT FORBIDDEN CODES','Only subtract separate cases directly','3,125 − 3 × 25 = 3,050',
 'Subtract three times twenty-five from the total. Three thousand fifty codes remain. Longer codes or self-overlapping words need additional overlap checks.')],e(4,10),expression='5**5-3*5**2',value='3050'),
]

def lessons(doc):
 assert sum('SUN' not in ''.join(t) for t in product('SUNAB',repeat=5))==3050
 assert sum(a+b>=11 for a,b in product(range(1,8),repeat=2))==10
 assert sum(a*b>=21 for a,b in product(range(1,8),repeat=2))==15
 return make_lessons(SPECS,doc)
