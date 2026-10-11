"""Percentage growth, decay, factor interpretation and weighted mixtures."""
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons

SPECS=[
authored('percent-exponential-growth-model','Build and evaluate a repeated percentage-growth model',
 'An amount starts at 1500 and grows by 7% each year.\nWrite a model for t years and find the amount\nafter two years.', 'A(t) = 1500(1.07)^t; after two years: 1717.35',
 'An amount starts at fifteen hundred and grows by seven percent each year. Write a model for t years and find the amount after two years.',[
 ('YEARLY MULTIPLIER','Keep one hundred percent and add seven percent','1 + 0.07 = 1.07',
  'Seven percent is zero point zero seven. Add one to keep the original amount, giving a yearly multiplier of one point zero seven.'),
 ('REPEATED MULTIPLICATION','Apply the same multiplier once per year','A(t) = 1500(1.07)^t',
  'After t years, multiply fifteen hundred by one point zero seven to the power t.'),
 ('EVALUATE','Two years means two applications of the multiplier','Year 1: 1500 × 1.07 = 1605\nYear 2: 1605 × 1.07 = 1717.35',
  'After one year the amount is sixteen hundred five. Multiply again for the second year to get one thousand seven hundred seventeen point three five.'),
 ('INTERPRET','Each percentage applies to the updated amount','Initial value × (1 + rate)^number of periods',
  'The second increase uses the updated amount. Repeated percentage growth compounds. The model uses the initial value, the growth multiplier, and the number of periods.')],
 g(10,7,2,6),expression='1500*1.07**2',value='1717.35',equalities=[('1500*1.07','1605')]),

authored('percent-exponential-decay-model','Build and evaluate a repeated percentage-decay model',
 'A machine is worth $18,000 and loses 9%\nof its current value each year. Write its value model\nand find its value after two years.',
 'V(t) = 18000(0.91)^t; after two years: $14905.80',
 'A machine is worth eighteen thousand dollars and loses nine percent of its current value each year. Write its value model and find its value after two years.',[
 ('WHAT REMAINS','Subtract the lost fraction from one','1 − 0.09 = 0.91',
  'If nine percent is lost, ninety-one percent remains. The yearly multiplier is zero point nine one.'),
 ('MODEL','Apply the remaining fraction once per year','V(t) = 18000(0.91)^t',
  'Multiply eighteen thousand by zero point nine one to the power t, where t is the number of years.'),
 ('EVALUATE','Apply the multiplier twice','Year 1: $16,380\nYear 2: $16,380 × 0.91 = $14,905.80',
  'After one year the value is sixteen thousand three hundred eighty. After two years it is fourteen thousand nine hundred five dollars and eighty cents.'),
 ('GEOMETRIC PATTERN','The ratio is constant; the dollar decrease is not','Each new value = previous value × 0.91',
  'The values form a geometric pattern because each is multiplied by the same factor. Do not subtract nine percent of the original value every year.')],
 g(10,7,1,5),expression='18000*0.91**2',value='14905.8',equalities=[('18000*0.91','16380')]),

authored('percent-read-exponential-factor','Read percentage change from an exponential factor',
 'A(t) = 750(1.14)^t and B(t) = 600(0.73)^t.\nFor each model, find the percentage of the previous\namount retained and the percentage change per period.',
 'A: 114% retained, 14% growth; B: 73% retained, 27% decay',
 'Two models have multipliers one point one four and zero point seven three. For each, find the percentage of the previous amount retained and the percentage change per period.',[
 ('READ THE FACTOR','The number raised to t is the multiplier each period','A: 1.14; B: 0.73',
  'Read the number raised to t. The starting values, seven hundred fifty and six hundred, do not determine the percentage rate.'),
 ('GROWTH FACTOR','One point one four means one hundred fourteen percent','114% of previous amount → 14% increase',
  'One point one four keeps one hundred fourteen percent of the previous amount. Subtract the original hundred percent to get fourteen percent growth.'),
 ('DECAY FACTOR','Zero point seven three means seventy-three percent','73% remains → 100% − 73% = 27% decrease',
  'Zero point seven three leaves seventy-three percent. The missing twenty-seven percent is the decrease.'),
 ('KEEP THE TWO MEANINGS APART','The amount remaining differs from the amount gained or lost','Multiplier b → 100b% of previous amount\nPercent change = 100(b − 1)%',
  'Distinguish the percentage retained from the percentage change. Subtract one from the multiplier, then multiply by one hundred. A negative change indicates decay.')],
 g(10,7,3,9),expression='(1.14-1)*100',value='14',equalities=[('(1-0.73)*100','27'),('0.73*100','73')]),

authored('percent-mixture-concentration','Find the concentration of a mixture',
 'Mix 3 L of a 15% solution with 5 L of a 55% solution.\nAssume the volumes add.\nWhat is the resulting concentration?', '40 percent',
 'Mix three litres of a fifteen percent solution with five litres of a fifty-five percent solution. Assume the volumes add. What is the resulting concentration?',[
 ('FIRST SOLUTION','Multiply its volume by its concentration','3 × 0.15 = 0.45 L of solute',
  'The first solution contains three times zero point one five, or zero point four five litres of solute.'),
 ('SECOND SOLUTION','Compute the solute amount separately','5 × 0.55 = 2.75 L of solute',
  'The second contains five times zero point five five, or two point seven five litres of solute.'),
 ('COMBINE AMOUNTS','Add solute volumes and total solution volumes','Solute: 0.45 + 2.75 = 3.20 L\nSolution: 3 + 5 = 8 L',
  'Together there are three point two litres of solute in eight litres of solution.'),
 ('DIVIDE','Concentration is solute divided by total solution','3.20 ÷ 8 = 0.40 = 40%',
  'Divide three point two by eight to get forty percent. Weight each concentration by its volume; a simple average of the two percentages would be wrong when the volumes differ.')],
 g(12,4,2,3),expression='(3*0.15+5*0.55)/(3+5)*100',value='40',equalities=[('3*0.15','0.45'),('5*0.55','2.75')]),

authored('percent-mixture-unknown-volume','Find an unknown volume in a mixture',
 'Mix 25% and 65% solutions to make 20 L\nof a 41% solution. Assume volumes add.\nHow many litres of the 65% solution are needed?', '8 litres',
 'Mix twenty-five percent and sixty-five percent solutions to make twenty litres of a forty-one percent solution. Assume volumes add. How much of the stronger solution is needed?',[
 ('DEFINE VOLUMES','Let x be litres of the stronger solution','65% solution: x L\n25% solution: (20 − x) L',
  'Call the stronger volume x. The weaker volume is twenty minus x.'),
 ('BALANCE SOLUTE','The solute amounts must add to the final solute amount','0.65x + 0.25(20 − x) = 0.41 × 20',
  'Multiply each volume by its concentration. Their sum equals forty-one percent of twenty litres.'),
 ('SOLVE','Expand, combine terms, and isolate x','0.40x + 5 = 8.2\n0.40x = 3.2 → x = 8 L',
  'Combining terms gives zero point four x plus five equals eight point two. Subtract five and divide by zero point four. We need eight litres.'),
 ('CHECK','Use twelve litres of weaker solution and eight of stronger','0.25 × 12 + 0.65 × 8 = 8.2 L\n8.2 ÷ 20 = 41%',
  'Eight litres of stronger solution leaves twelve litres of weaker solution. They contain eight point two litres of solute in twenty litres total, confirming forty-one percent.')],
 g(9,6,5,9),equation=('0.65*x+0.25*(20-x)','0.41*20','x','8'),equalities=[('0.25*12+0.65*8','8.2'),('8.2/20','0.41')]),
]


def lessons(doc):return make_lessons(SPECS,doc)
