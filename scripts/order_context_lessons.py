"""Context questions recovered from the broad comparison draft group."""
from algebra_lessons import authored
from number_sense_lessons import source as g
from number_theory_lessons import source as e
from card_lessons import make_lessons,draw_card
from math import gcd
import generate_sample_videos as v
DICE=('worksheets/enrichment/counting-and-probability 1/U1counting-and-classification/E-CP1U1W3Rev.csv','4')
SPECS=[
authored('order-histogram-threshold','Choose a histogram to count values above a boundary',
 'Data use intervals of width 20. Which display helps count values above 60:\na histogram, box plot or pie chart?', 'Histogram; the example has 8 values above 60',
 'Data are grouped into intervals of width twenty. Which display helps count values above sixty: a histogram, box plot, or pie chart?',[
 ('CHOOSE THE DISPLAY','A histogram shows frequencies in numerical intervals','Histogram: counts in intervals\nBox plot: quartiles\nPie chart: category proportions',
 'A histogram shows how many values fall in each numerical interval. A box plot summarizes quartiles, while a pie chart shows category proportions.'),
 ('READ THE INTERVALS','The example intervals end at forty, sixty, eighty and one hundred','20 < value ≤ 40: 4\n40 < value ≤ 60: 7\n60 < value ≤ 80: 5; 80 < value ≤ 100: 3',
 'Read each bar as an interval count. Here the two intervals above sixty have frequencies five and three.'),
 ('ADD THE RELEVANT FREQUENCIES','The endpoint convention excludes sixty itself','Values above 60: 5 + 3 = 8',
 'Add five and three to get eight values above sixty. Values equal to sixty belong in the previous interval and are excluded.'),
 ('CHECK THE BOUNDARY','Exact counting needs a suitable interval boundary','A cutoff inside a bar needs more detailed data.',
 'If a cutoff falls inside a bar, that bar alone cannot tell the exact count. Check the interval boundaries and which endpoints are included.')],
 g(6,11,11,4),equalities=[('5+3','8'),('4+7+5+3','19')]),
authored('order-less-than-phrasing','Translate less-than phrases in the correct order',
 'Write expressions for y less than 18\nand 7 less than x + 5.', '18 − y; (x + 5) − 7',
 'Write expressions for y less than eighteen, and seven less than x plus five.',[
 ('FIND THE STARTING AMOUNT','What comes after less than is the starting quantity','y less than 18: start with 18',
 'For y less than eighteen, start with eighteen. The phrase tells us to remove y from that amount.'),
 ('SUBTRACT WHAT IS REMOVED','Keep the subtraction order','y less than 18 → 18 − y',
 'The expression is eighteen minus y. Y minus eighteen would describe eighteen less than y.'),
 ('KEEP A COMPOUND START TOGETHER','The whole starting amount is x plus five','7 less than x + 5 → (x + 5) − 7',
 'For the second phrase, start with the whole quantity x plus five, then subtract seven. Parentheses keep that starting amount together.'),
 ('CHECK WITH A NUMBER','Let x and y both equal ten','18 − 10 = 8\n(10 + 5) − 7 = 8',
 'Try ten for each variable. Ten less than eighteen is eight. Seven less than fifteen is also eight. Substitution checks the meaning.')],
 g(6,6,5,8),equalities=[('18-10','8'),('(10+5)-7','8')]),
authored('order-gcf-identical-packs','Find the greatest number of identical packs',
 'Pack 32 markers and 48 pencils into identical packs with no leftovers.\nWhat is the greatest number of packs?', '16 packs; 2 markers and 3 pencils in each',
 'Pack thirty-two markers and forty-eight pencils into identical packs with no leftovers. Find the greatest number of packs.',[
 ('MODEL THE COUNT','The pack count must divide both totals','Pack count divides both 32 and 48.',
 'Each pack must have the same number of markers and the same number of pencils. The number of packs must divide both totals exactly.'),
 ('FIND COMMON FACTORS','Keep factors shared by both totals','Common factors: 1, 2, 4, 8, 16',
 'The common factors of thirty-two and forty-eight are one, two, four, eight, and sixteen.'),
 ('CHOOSE THE GREATEST','The largest common factor gives the most packs','GCF(32, 48) = 16',
 'Choose sixteen, the greatest common factor. That is the greatest possible number of identical packs.'),
 ('CHECK THE CONTENTS','Divide each supply by the pack count','32 ÷ 16 = 2 markers\n48 ÷ 16 = 3 pencils per pack',
 'Each pack gets two markers and three pencils. Sixteen such packs use every item with no leftovers.')],
 g(6,6,9,8),equalities=[('32/16','2'),('48/16','3')]),
authored('order-gcf-group-size','Find the largest equal group size without mixing types',
 'Shelf 84 science books and 126 art books, with equal counts per shelf.\nKeep types separate. What is the largest count per shelf?', '42 books per shelf',
 'Shelf eighty-four science books and one hundred twenty-six art books. Keep types separate, with an equal number on every shelf. Find the largest count per shelf.',[
 ('IDENTIFY WHAT IS MAXIMIZED','The unknown is books per shelf, not shelf count','Books per shelf must divide 84 and 126.',
 'Here the unknown is the number of books on each shelf. It must divide both totals so neither type has leftovers.'),
 ('FACTOR BOTH TOTALS','Use shared prime factors','84 = 2² × 3 × 7\n126 = 2 × 3² × 7',
 'Factor each total. Eighty-four has two squared, three, and seven. One hundred twenty-six has two, three squared, and seven.'),
 ('TAKE THE COMMON PART','Use the smaller exponent of each shared prime','GCF = 2 × 3 × 7 = 42',
 'Use one two, one three, and one seven. Their product is forty-two, the largest common divisor.'),
 ('CHECK THE SHELVES','Each shelf holds forty-two books of one type','84 ÷ 42 = 2 science shelves\n126 ÷ 42 = 3 art shelves',
 'Forty-two books per shelf gives two science shelves and three art shelves. The types stay separate and all books are used.')],
 e('prime-factorization',6,7),equalities=[('2**2*3*7','84'),('2*3**2*7','126'),('84/42','2'),('126/42','3')]),
authored('order-at-least-constraints','Write separate at-least constraints',
 'An order needs at least 7 pens p and at least 9 notebooks n.\nWrite both constraints.', 'p ≥ 7 and n ≥ 9, with whole-number counts',
 'An order needs at least seven pens, called p, and at least nine notebooks, called n. Write both constraints.',[
 ('TRANSLATE AT LEAST','The minimum is included','At least 7 → 7 or more',
 'At least means the stated minimum is allowed, along with larger values.'),
 ('WRITE THE FIRST CONSTRAINT','Compare pens with their own minimum','p ≥ 7',
 'For pens, write p greater than or equal to seven.'),
 ('WRITE THE SECOND CONSTRAINT','Keep the notebook requirement separate','n ≥ 9',
 'For notebooks, write n greater than or equal to nine. Both conditions must hold.'),
 ('CHECK THE BOUNDARIES','Counts are whole numbers and the minimum works','p = 7 and n = 9 satisfy both.\np = 6 fails, even if n is large.',
 'Seven pens and nine notebooks meet the order. Six pens would fail even with extra notebooks. Use whole-number counts for these objects.')],
 g(9,7,4,9),equalities=[('7-7','0'),('9-9','0')]),
authored('order-dice-threshold-count','Count labelled-dice outcomes above a threshold',
 'Roll a blue and a red six-sided die.\nCount outcomes with sum > 8, then outcomes with product > 18.', '10 sum outcomes; 8 product outcomes',
 'Roll a blue and a red six-sided die. Count outcomes with sum greater than eight, then product greater than eighteen.',[
 ('KEEP THE DICE LABELS','An outcome is an ordered blue-red pair','(blue, red): (3, 6) differs from (6, 3).',
 'The dice have different labels. Swapping the values usually gives a different outcome, so count ordered pairs.'),
 ('COUNT SUM CASES','Fix blue and count red values that qualify','Blue 3, 4, 5, 6 → 1, 2, 3, 4 red choices\nTotal: 1 + 2 + 3 + 4 = 10',
 'For sums above eight, blue values three, four, five, and six allow one, two, three, and four red choices. Add them to get ten.'),
 ('COUNT PRODUCT CASES','Use the strict product condition','Blue 4: red 5, 6\nBlue 5 or 6: red 4, 5, 6\nTotal: 2 + 3 + 3 = 8',
 'For products above eighteen, blue four allows red five or six. Blue five and six each allow red four, five, or six. That gives eight.'),
 ('CHECK COMPLETENESS','Lower blue values cannot reach the thresholds','Sum: 10 outcomes\nProduct: 8 outcomes',
 'The remaining blue values cannot pass the corresponding threshold. Equality does not qualify because both conditions say greater than.')],
 DICE,equalities=[('1+2+3+4','10'),('2+3+3','8')]),
authored('order-crt-two-remainders','Find the smallest count with two prescribed remainders',
 'A positive number of tokens leaves remainder 1 in groups of 4\nand remainder 2 in groups of 7. Find the smallest count.', '9',
 'A positive token count leaves remainder one in groups of four and remainder two in groups of seven. Find the smallest count.',[
 ('WRITE BOTH CONDITIONS','Each grouping gives a remainder condition','x = 4a + 1\nx = 7b + 2',
 'The count must be one more than a multiple of four and two more than a multiple of seven.'),
 ('LIST ONE SET OF CANDIDATES','Start at the smallest positive candidate','Remainder 2 modulo 7: 2, 9, 16, 23, …',
 'List positive counts leaving remainder two after division by seven. Start with two, then add seven each time.'),
 ('TEST THE OTHER CONDITION','The first match is the smallest','2 leaves remainder 2 modulo 4: no.\n9 = 4 × 2 + 1: yes.',
 'Two fails the groups-of-four condition. Nine leaves remainder one, so it is the first match.'),
 ('CHECK BOTH','Verify the original grouping statements','9 = 4 × 2 + 1\n9 = 7 × 1 + 2',
 'Nine satisfies both remainders. Because the smaller candidate failed, nine is the smallest positive count.')],
 e('CRT',4,5),equalities=[('9%4','1'),('9%7','2'),('2%4','2')]),
authored('order-crt-three-remainders','Combine three remainder conditions systematically',
 'Find the smallest positive x with remainders 1, 2 and 1\nwhen divided by 4, 5 and 7, respectively.', '57',
 'Find the smallest positive number with remainder one on division by four, remainder two on division by five, and remainder one on division by seven.',[
 ('START WITH ONE CONDITION','List values leaving remainder two modulo five','2, 7, 12, 17, 22, …',
 'Begin with the remainder-two condition for division by five. The candidates increase by five.'),
 ('COMBINE TWO CONDITIONS','Keep candidates also leaving remainder one modulo four','First match: 17\nCombined candidates: 17 + 20t, for whole t ≥ 0',
 'Seventeen is the first candidate leaving remainder one modulo four. The two conditions repeat every twenty, so list seventeen plus twenty t.'),
 ('TEST THE THIRD CONDITION','Check these candidates in increasing order','17 mod 7 = 3\n37 mod 7 = 2\n57 mod 7 = 1',
 'Test division by seven. Seventeen leaves three, thirty-seven leaves two, and fifty-seven leaves one. The first match is fifty-seven.'),
 ('CHECK ALL THREE','Verify every original remainder','57 = 4 × 14 + 1\n57 = 5 × 11 + 2\n57 = 7 × 8 + 1',
 'Check fifty-seven against all three divisors. Every remainder matches, and our increasing candidate list proves it is the smallest positive solution.')],
 e('CRT',4,7),equalities=[('17%4','1'),('17%5','2'),('17%7','3'),('37%7','2'),('57%4','1'),('57%5','2'),('57%7','1')]),
]
def draw_context(spec,d,scene,p):
 if spec['video_id']=='order-histogram-threshold' and scene==2:
  left=420;bottom=790;bw=240;scale=44
  for i,f in enumerate([4,7,5,3]):
   x=left+i*bw;top=bottom-f*scale
   d.rectangle((x,top,x+bw,bottom),fill=v.TEAL if i>=2 else '#A9BABD',outline=v.INK,width=3)
   v.text(d,(x+bw/2,top-38),str(f),35,v.INK,True,anchor='mm')
  for f in range(0,9,2):v.text(d,(left-40,bottom-f*scale),str(f),30,v.MUTED,anchor='rm')
  for i,n in enumerate([20,40,60,80,100]):v.text(d,(left+i*bw,bottom+35),str(n),32,v.INK,anchor='mm')
  d.line((left+2*bw,405,left+2*bw,bottom),fill='#CF6944',width=5)
  v.text(d,(200,360),'Frequency',34,v.INK,True)
  v.centered(d,855,'Value; left endpoint excluded, right endpoint included',32,v.MUTED)
 else:draw_card(spec,d,scene,p)
def lessons(doc):
 assert gcd(32,48)==16 and gcd(84,126)==42
 assert sum(b+r>8 for b in range(1,7) for r in range(1,7))==10
 assert sum(b*r>18 for b in range(1,7) for r in range(1,7))==8
 assert next(x for x in range(1,100) if x%4==1 and x%7==2)==9
 assert next(x for x in range(1,200) if x%4==1 and x%5==2 and x%7==1)==57
 L=make_lessons(SPECS,doc)
 for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:draw_context(s,d,scene,p)
 return L
