"""Core percentage methods with fresh examples and explicit reference wholes."""
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons,draw_card,centered_math
import generate_sample_videos as v

SPECS=[
authored('percent-hundred-grid','Read and show percentages on a hundred-square grid',
 'A 10 by 10 grid has 61 shaded squares.\nWhat percent is shaded?', '61 percent',
 'A ten by ten grid has sixty-one shaded squares. What percent is shaded?',[
 ('THE WHOLE','There are one hundred equal squares','10 × 10 = 100 squares',
  'The whole grid contains one hundred equal squares. Percent means out of one hundred.'),
 ('COUNT THE PART','Each square is one hundredth of this whole','61 shaded out of 100',
  'Sixty-one squares are shaded. Each square is one hundredth of the whole grid.'),
 ('WRITE THE PERCENT','Use the shaded count when the whole has one hundred parts','61/100 = 61%',
  'Sixty-one out of one hundred is sixty-one percent.'),
 ('REVERSE THE METHOD','To show a percent, shade that many of the hundred squares','61% ↔ 61 shaded squares',
  'The method works both ways. To show sixty-one percent, shade sixty-one of the hundred equal squares. Always check the total number of parts first.')],
 g(6,3,2,1),expression='61/100*100',value='61'),

authored('percent-problems','Find a percentage from a part and a whole',
 'A club has 20 members. Of these, 13 walk to the club.\nWhat percent of the members walk?', '65 percent',
 'A club has twenty members. Thirteen walk to the club. What percent of the members walk?',[
 ('CHOOSE THE WHOLE','Use the complete group named in the question','Part = 13; whole = 20',
  'The complete group is twenty members. The part we are counting is thirteen walkers.'),
 ('WRITE THE FRACTION','Divide the part by the whole','13/20 = 0.65',
  'Write thirteen over twenty, then divide. The result is zero point six five.'),
 ('CONVERT TO PERCENT','Multiply the fraction or decimal by one hundred','0.65 × 100% = 65%',
  'Multiply by one hundred percent. Sixty-five percent of the members walk.'),
 ('CHECK','The answer is more than half but less than the whole','Percent = (part ÷ whole) × 100%',
  'Thirteen is more than half of twenty but less than twenty, so sixty-five percent is reasonable. Use the same rule for shaded parts, fractions, or a specified subgroup.')],
 g(6,3,3,1),expression='13/20*100',value='65'),

authored('percent-of-quantity','Find a given percentage of a quantity',
 'Find 18% of 350.', '63',
 'Find eighteen percent of three hundred fifty.',[
 ('CONVERT','Percent means divide by one hundred','18% = 18/100 = 0.18',
  'Convert eighteen percent to a decimal by dividing by one hundred. It becomes zero point one eight.'),
 ('MULTIPLY','Of tells us to multiply by the whole quantity','0.18 × 350',
  'Multiply that decimal by the whole quantity, three hundred fifty.'),
 ('CALCULATE','Multiply before interpreting the result','0.18 × 350 = 63',
  'Zero point one eight times three hundred fifty is sixty-three.'),
 ('CHECK','Compare with easy nearby percentages','10% = 35; 20% = 70\n18% of 350 = 63',
  'Ten percent is thirty-five and twenty percent is seventy. Our answer sixty-three falls between them. This same multiplication finds a tip amount or a percentage of a group.')],
 g(6,3,4,1),expression='0.18*350',value='63',equalities=[('0.1*350','35'),('0.2*350','70')]),

authored('percent-less-than-one','Calculate a percentage smaller than one percent',
 'Find 0.6% of 750.', '4.5',
 'Find zero point six percent of seven hundred fifty.',[
 ('DIVIDE BY ONE HUNDRED','The percent sign still means out of one hundred','0.6% = 0.6/100 = 0.006',
  'Divide zero point six by one hundred. The decimal multiplier is zero point zero zero six, not zero point six.'),
 ('MULTIPLY','Apply the decimal multiplier to the whole','750 × 0.006',
  'Multiply seven hundred fifty by zero point zero zero six.'),
 ('CALCULATE','Six thousandths of seven hundred fifty','750 × 0.006 = 4.5',
  'The result is four point five.'),
 ('CHECK AGAINST ONE PERCENT','A rate below one percent gives less than one hundredth','1% of 750 = 7.5\n0.6% gives 4.5, which is smaller.',
  'One percent of seven hundred fifty is seven point five. Zero point six percent must be smaller, and four point five passes that check.')],
 g(6,3,5,2),expression='750*0.006',value='4.5',equalities=[('750*0.01','7.5')]),

authored('percent-find-whole','Find the whole when a part and percentage are known',
 '72 completed tasks represent 45% of a project.\nHow many tasks are in the whole project?', '160 tasks',
 'Seventy-two completed tasks represent forty-five percent of a project. How many tasks are in the whole project?',[
 ('NAME THE UNKNOWN','Let W be the whole number of tasks','45% of W = 72',
  'The whole is unknown. Call it W. Forty-five percent of W equals seventy-two.'),
 ('CONVERT','Write the percent as a decimal','0.45 × W = 72',
  'Forty-five percent is zero point four five. So zero point four five times W equals seventy-two.'),
 ('DIVIDE','Undo multiplication by the percentage','W = 72 ÷ 0.45 = 160',
  'Divide seventy-two by zero point four five to get one hundred sixty tasks.'),
 ('CHECK','The stated percentage of the answer must recover the known part','0.45 × 160 = 72',
  'Forty-five percent of one hundred sixty is seventy-two, which checks. The rule is whole equals known part divided by the percent written as a decimal. It also works with rates above one hundred percent.')],
 g(6,3,3,10),expression='72/0.45',value='160',equalities=[('0.45*160','72')]),

authored('percent-compare-groups','Compare percentages for groups of different sizes',
 'Team A wins 22 of 40 games. Team B wins 21 of 35.\nWhich team has the higher winning percentage?', 'Team B: 60%, compared with Team A: 55%',
 'Team A wins twenty-two of forty games. Team B wins twenty-one of thirty-five. Which team has the higher winning percentage?',[
 ('TEAM A','Use Team A’s total as its denominator','22/40 × 100% = 55%',
  'Team A’s rate is twenty-two divided by forty, or fifty-five percent.'),
 ('TEAM B','Use Team B’s own total as its denominator','21/35 × 100% = 60%',
  'Team B’s rate is twenty-one divided by thirty-five, or sixty percent.'),
 ('COMPARE RATES','Compare the percentages rather than the raw wins','60% > 55%',
  'Sixty percent exceeds fifty-five percent, so Team B has the higher winning percentage.'),
 ('EXPLAIN','Different group sizes make raw counts misleading','Team B wins a larger share of its games.',
  'Team A has more wins, but also played more games. Team B won a larger share. Always divide each part by its own whole before comparing percentages.')],
 g(6,3,3,9),expression='22/40*100',value='55',equalities=[('21/35*100','60')]),

authored('percent-wholes-and-hundredths','Represent percentages greater than one hundred',
 'One hundred-square grid represents one whole.\nA model shades 2 full grids and 63 squares on a third.\nWhat percentage of one whole does this represent?', '263 percent',
 'One hundred-square grid represents one whole. A model shades two full grids and sixty-three squares on a third. What percentage of one whole does this represent?',[
 ('REFERENCE WHOLE','One grid, not all the grids together, is one hundred percent','1 grid = 100%',
  'Set the reference whole first. Here, one grid represents one hundred percent.'),
 ('FULL GRIDS','Each full grid contributes another one hundred percent','2 × 100% = 200%',
  'Two full grids contribute two hundred percent.'),
 ('EXTRA PART','Add the extra hundredths of one grid','200% + 63% = 263%',
  'The extra sixty-three squares are sixty-three percent of one grid. Add them to get two hundred sixty-three percent.'),
 ('REVERSE IT','Split a percentage into hundreds and leftover hundredths','263% = 2 wholes + 63/100 of a whole',
  'To draw two hundred sixty-three percent, reverse the steps: shade two full grids, then sixty-three squares. Percentages can exceed one hundred when the amount exceeds the reference whole.')],
 g(6,3,2,9),expression='2*100+63',value='263'),

authored('percent-ratio-above-one-hundred','Find a percentage when the part exceeds the reference amount',
 'A target is 80 pages. A reader finishes 116 pages.\nWhat percent of the target did the reader finish?', '145 percent',
 'A target is eighty pages. A reader finishes one hundred sixteen pages. What percent of the target did the reader finish?',[
 ('REFERENCE AMOUNT','The target is the whole used for this comparison','100% means 80 pages.',
  'The eighty-page target is our reference amount. It represents one hundred percent.'),
 ('DIVIDE','Compare actual progress with the reference target','116 ÷ 80 = 1.45',
  'Divide one hundred sixteen by eighty. The result is one point four five.'),
 ('CONVERT','Multiply the ratio by one hundred percent','1.45 × 100% = 145%',
  'Multiply by one hundred percent. The reader completed one hundred forty-five percent of the target.'),
 ('INTERPRET','Percentage of the target and percentage above it differ','145% of the target = 45% above the target',
  'More than the full target means more than one hundred percent. One hundred forty-five percent of the target is forty-five percent above it, not one hundred forty-five percent above it.')],
 g(6,3,5,8),expression='116/80*100',value='145',equalities=[('(116-80)/80*100','45')]),

authored('percent-reverse-increase','Recover an original amount after a percentage increase',
 'A price increases by 35% and becomes $81.\nWhat was the original price?', '60 dollars',
 'A price increases by thirty-five percent and becomes eighty-one dollars. What was the original price?',[
 ('NEW AMOUNT','Keep the original hundred percent and add the increase','100% + 35% = 135% of the original',
  'After the increase, the new price is one hundred thirty-five percent of the original.'),
 ('MULTIPLIER','Let P be the original price','1.35 × P = 81',
  'Convert one hundred thirty-five percent to one point three five. Multiply the original P by that factor to get eighty-one.'),
 ('UNDO THE INCREASE','Divide by the full multiplier','P = 81 ÷ 1.35 = $60',
  'Divide eighty-one by one point three five. The original price was sixty dollars.'),
 ('CHECK','Calculate the increase using the original price','35% of $60 = $21\n$60 + $21 = $81',
  'Thirty-five percent of sixty is twenty-one, and sixty plus twenty-one is eighty-one. Use the original as the percentage base when checking.')],
 g(7,2,2,8),expression='81/1.35',value='60',equalities=[('0.35*60','21'),('60+21','81')]),

authored('percent-tip-and-total','Calculate a tip and the final bill',
 'A meal costs $46 before the tip. Add a 15% tip.\nFind the tip and the final bill.', 'Tip $6.90; final bill $52.90',
 'A meal costs forty-six dollars before the tip. Add a fifteen percent tip. Find the tip and the final bill.',[
 ('DECIMAL RATE','Divide the tip percentage by one hundred','15% = 0.15',
  'Fifteen percent is zero point one five.'),
 ('TIP AMOUNT','Multiply the original bill by the tip rate','Tip = $46 × 0.15 = $6.90',
  'Multiply forty-six by zero point one five. The tip is six dollars and ninety cents.'),
 ('ADD THE TIP','The final bill includes the meal and tip','Total = $46 + $6.90 = $52.90',
  'Add the tip to the original bill. The total is fifty-two dollars and ninety cents.'),
 ('CHECK THE QUESTION','Report both requested amounts, with money to two decimal places','Tip: $6.90; total: $52.90',
  'The tip and final total are different amounts. Report the tip as six ninety and the full bill as fifty-two ninety, with two decimal places for money.')],
 g(7,2,3,9),expression='46*0.15',value='6.9',equalities=[('46+6.9','52.9')]),

authored('percent-fixed-rate-time-intervals','Accumulate a fixed percentage over time intervals',
 'A worker completes 14% of one job every 8 minutes\nat a constant rate. What fraction of the job is done\nin 40 minutes? Give a decimal.', '0.7 of the job',
 'A worker completes fourteen percent of one job every eight minutes at a constant rate. What fraction is done in forty minutes? Give a decimal.',[
 ('COUNT INTERVALS','Divide elapsed time by time per interval','40 ÷ 8 = 5 intervals',
  'Forty minutes contains five eight-minute intervals.'),
 ('FIX THE BASE','Each interval completes the same share of the original job','14% = 0.14 of the job per interval',
  'Each interval completes zero point one four of the same original job. The reference whole stays fixed.'),
 ('MULTIPLY','Add equal progress for all five intervals','5 × 0.14 = 0.70',
  'Multiply five by zero point one four to get zero point seven zero.'),
 ('REPORT','The requested form is a decimal fraction of the job','0.7 of the job, or 70%',
  'The worker has completed zero point seven of the job, equivalent to seventy percent. This is a fixed rate; percentages of a changing amount would require a different model.')],
 g(7,2,3,7),expression='40/8*0.14',value='0.7'),
]


def grid(d,x,y,shaded,cell=26):
    for i in range(100):
        xx=x+(i%10)*cell;yy=y+(i//10)*cell
        d.rectangle((xx,yy,xx+cell,yy+cell),fill=v.TEAL if i<shaded else 'white',outline='#82968C',width=1)


def diagram(s,d,scene,p):
    if s['video_id']=='percent-hundred-grid' and scene in (1,2,3):
        grid(d,760,390,61,39)
        centered_math(d,845,'6 full rows + 1 square = 61 shaded squares',37,v.INK)
        centered_math(d,910,s['displays'][scene],43,v.TEAL)
    elif s['video_id']=='percent-wholes-and-hundredths' and scene in (1,2,3):
        for i,n in enumerate((100,100,63)):grid(d,420+i*400,440,n,28)
        centered_math(d,805,'Each grid = one whole = 100%',40,v.INK)
        centered_math(d,900,s['displays'][scene],43,v.TEAL)
    else:draw_card(s,d,scene,p)


def lessons(doc):
    batch=make_lessons(SPECS,doc)
    for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:diagram(s,d,scene,p)
    return batch
