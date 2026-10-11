"""Core counting methods with distinct, independently checked examples."""
from math import factorial
from itertools import permutations
from algebra_lessons import authored
from probability_lessons import enrichment as e
from number_sense_lessons import source
from card_lessons import make_lessons

SPECS=[
authored('counting-product-rule','The multiplication principle of counting',
 'Choose one of 8 shirts, 3 hats, and 2 scarves.\nEvery combination is allowed. How many outfits are possible?','48',
 'Choose one of eight shirts, three hats, and two scarves. Every combination is allowed. How many outfits can you make?',[
 ('FIRST TWO CHOICES','Every shirt pairs with every hat','8 × 3 = 24 shirt-and-hat pairs',
  'For each shirt there are three hat choices. Eight times three gives twenty-four pairs.'),
 ('THIRD CHOICE','Each pair can use either scarf','24 × 2 = 48 outfits',
  'Each pair can be completed with either of the two scarves. Twenty-four times two gives forty-eight outfits.'),
 ('ONE PRODUCT','Use one factor for each stage','8 × 3 × 2 = 48',
  'Write one factor for each choice: eight times three times two.'),
 ('GENERAL RULE','Multiply when every stage has a fixed choice count','a choices, then b choices, then c choices:\na × b × c outcomes',
  'The multiplication principle applies when each earlier choice leaves the stated number of choices at the next stage. Multiply those counts.')],
 source(7,7,4,5),expression='8*3*2',value='48'),

authored('counting-permutations','Selecting distinct ordered roles',
 '13 applicants fill three different roles.\nEach person can hold only one role. Count the assignments.','1716',
 'Thirteen applicants fill three different roles. Each person can hold only one role. How many assignments are possible?',[
 ('FIRST ROLE','Choose any applicant','First role: 13 choices',
  'The first role can go to any of the thirteen applicants.'),
 ('REMAINING ROLES','Remove each person already selected','Second role: 12 choices\nThird role: 11 choices',
  'After one person is selected, twelve remain. After two are selected, eleven remain for the third role.'),
 ('MULTIPLY','Different role assignments count separately','P(13, 3) = 13 × 12 × 11 = 1,716',
  'Multiply thirteen, twelve, and eleven to get one thousand seven hundred sixteen. Swapping people between roles changes the assignment.'),
 ('GENERAL FORMULA','Choose and order r of n distinct objects','P(n, r) = n! / (n − r)!\nNo repetition; order matters.',
  'For r ordered selections from n distinct objects, use n factorial divided by n minus r factorial. This cancels the unused factors.')],
 source(12,8,2,5),expression='13*12*11',value='1716'),

authored('counting-arrangements','Arranging all distinct objects',
 'Nine different flags are placed in a row.\nHow many orders are possible?','362880',
 'Nine different flags are placed in a row. How many different orders are possible?',[
 ('FILL THE POSITIONS','Used flags are no longer available','9 choices, then 8, then 7, …, then 1',
  'There are nine choices for the first position, eight for the next, and so on until one flag remains.'),
 ('FACTORIAL','Multiply all the choice counts','9! = 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1',
  'Multiply all the counts from nine down to one. This product is called nine factorial.'),
 ('EVALUATE','Group the multiplication','9 × 8 × 7 × 6 × 5 = 15,120\n4 × 3 × 2 × 1 = 24\n15,120 × 24 = 362,880',
  'The first five factors give fifteen thousand one hundred twenty. The remaining factors give twenty-four. Their product is three hundred sixty-two thousand eight hundred eighty.'),
 ('GENERAL RULE','Every object is distinct and used once','n distinct objects in a row → n! orders',
  'In general, n distinct objects in a row have n factorial orders. Repeated indistinguishable objects require an adjustment.')],
 source(12,8,2,7),expression='9*8*7*6*5*4*3*2*1',value='362880'),

authored('counting-addition-rule','Adding disjoint choices',
 'Choose exactly one item: 11 bookmarks, 7 badges,\nor 5 stickers. All items are distinct. How many choices?','23',
 'Choose exactly one item from eleven bookmarks, seven badges, or five stickers. All items are distinct. How many choices are there?',[
 ('CLASSIFY','The categories have no shared items','Bookmarks: 11\nBadges: 7\nStickers: 5',
  'These are three disjoint categories. No item belongs to more than one category.'),
 ('ONE CHOICE','Choose from one category, not one from each','Bookmarks OR badges OR stickers',
  'You choose just one item, so the alternatives are combined with or.'),
 ('ADD','Each item is counted once','11 + 7 + 5 = 23',
  'Add eleven, seven, and five. There are twenty-three choices.'),
 ('GENERAL RULE','Disjoint alternatives add','a choices OR b disjoint choices → a + b',
  'The addition principle combines disjoint alternatives. If groups overlap, account for shared items so they are not counted twice.')],
 e('counting-and-classification',1,6),expression='11+7+5',value='23'),

authored('counting-sum-then-product','Add choices within a stage, then multiply',
 'A menu has 6 regular and 2 new sandwiches,\nplus 5 hot and 4 cold drinks. Choose one sandwich and one drink.','72',
 'A menu offers six regular and two new sandwiches, plus five hot and four cold drinks. Choose one sandwich and one drink.',[
 ('SANDWICH CHOICES','Add the two disjoint sandwich groups','6 + 2 = 8 sandwiches',
  'Add the regular and new sandwiches. There are eight sandwich choices.'),
 ('DRINK CHOICES','Add the two disjoint drink groups','5 + 4 = 9 drinks',
  'Add the hot and cold drinks. There are nine drink choices.'),
 ('PAIR THE CHOICES','Every sandwich can pair with every drink','(6 + 2)(5 + 4) = 8 × 9 = 72',
  'Every sandwich can pair with each drink. Multiply eight by nine to get seventy-two meals.'),
 ('ANOTHER COUNT','The four disjoint pairing types agree','6×5 + 6×4 + 2×5 + 2×4\n= 30 + 24 + 10 + 8 = 72',
  'Alternatively, add the four pairing types. Thirty plus twenty-four plus ten plus eight also gives seventy-two.')],
 e('PCF','3HW',5),expression='(6+2)*(5+4)',value='72',equalities=[('6*5+6*4+2*5+2*4','72')]),

authored('counting-product-then-sum','Multiply within a choice, then add alternatives',
 'Choose either an outfit from 7 shirts and 3 hats,\nor one of 9 badges. How many total choices?','30',
 'Choose either an outfit made from seven shirts and three hats, or one of nine badges. How many total choices are possible?',[
 ('COUNT OUTFITS','Each shirt pairs with every hat','7 × 3 = 21 outfits',
  'There are seven times three, or twenty-one, complete outfits.'),
 ('OTHER ALTERNATIVE','A badge is a separate kind of choice','9 badges',
  'The other alternative is one of nine badges. An outfit is not a badge, so these groups do not overlap.'),
 ('ADD','Choose an outfit or a badge','21 + 9 = 30 choices',
  'Add twenty-one outfits and nine badges to get thirty choices.'),
 ('STRUCTURE','And within an option; or between disjoint options','(7 × 3) + 9 = 30',
  'Multiply the choices that form one complete option. Then add the counts of disjoint alternatives.')],
 e('counting-and-classification',3,6),expression='7*3+9',value='30'),

authored('counting-repeated-arrangements','Arranging letters that repeat',
 'How many distinguishable arrangements\ncan be made from the letters in BANANA?','60',
 'How many distinguishable arrangements can be made from the letters in banana?',[
 ('COUNT REPEATS','There are six letters altogether','A: 3 copies; N: 2 copies; B: 1 copy',
  "There are six letters: three A's, two N's, and one B."),
 ('TEMPORARILY LABEL COPIES','Six labelled letters would have 6! orders','6! = 720',
  'If every copy carried a different label, there would be six factorial, or seven hundred twenty, orders.'),
 ('REMOVE DUPLICATE LABELS','Swapping identical copies changes nothing','Each visible order was counted 3! × 2! = 12 times.',
  'Swapping the three A copies or the two N copies leaves the visible word unchanged. Each visible order was counted twelve times.'),
 ('DIVIDE','One count per distinguishable arrangement','6! / (3! × 2!) = 720/12 = 60\nGeneral rule: n! / (a! × b! × …)',
  'Divide seven hundred twenty by twelve to get sixty. In general, divide n factorial by the factorial of each repeated-letter count.')],
 e('PCF',5,7),expression='720/(6*2)',value='60'),

authored('counting-adjacent-distinct-pair','Keeping two people together in a line',
 'Five distinct people line up.\nLina and Omar must be next to each other. Count the lineups.','48',
 'Five distinct people line up. Lina and Omar must stand next to each other. How many lineups are possible?',[
 ('MAKE A BLOCK','Treat the required pair as one object','[Lina, Omar] plus three other people\n= 4 objects',
  'Treat Lina and Omar as a single block. Along with the other three people, there are four objects to arrange.'),
 ('ARRANGE THE OBJECTS','The block may occupy any position','4! = 24 orders',
  'The four objects can be arranged in twenty-four orders.'),
 ('ORDER INSIDE THE BLOCK','The pair can face either way in the lineup','Lina then Omar OR Omar then Lina\n2 orders inside',
  'Inside the block, Lina can come first or Omar can come first. There are two internal orders.'),
 ('MULTIPLY','Combine outside and inside orders','4! × 2 = 24 × 2 = 48',
  'Multiply twenty-four by two to get forty-eight lineups. The block method keeps the pair together without fixing their position.')],
 e('PCF',5,9),expression='24*2',value='48'),
]


def lessons(doc):
    assert factorial(9)==362880
    assert len(set(permutations('BANANA')))==60
    assert sum(abs(p.index('L')-p.index('O'))==1 for p in permutations('LOABC'))==48
    return make_lessons(SPECS,doc)
