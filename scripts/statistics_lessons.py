"""Checked statistics lessons with original data and purpose-drawn plots."""
from collections import Counter
from fractions import Fraction as F
from math import erf, sqrt, exp
from statistics import median
from algebra_lessons import authored
from number_sense_lessons import source
from card_lessons import make_lessons, draw_card, centered_math
import generate_sample_videos as video


SPECS = [
authored('statistics-mean','Finding the arithmetic mean',
 'Find the mean of 6, 11, 8 and 15.', '10',
 "Let's find the arithmetic mean of six, eleven, eight, and fifteen. Add the values, then divide by how many there are.",[
 ('ADD', 'Find the total', '6 + 11 + 8 + 15 = 40',
  'Six plus eleven plus eight plus fifteen is forty.'),
 ('COUNT', 'Count every data value', 'There are 4 values.',
  'There are four values in this data set.'),
 ('DIVIDE', 'Share the total equally', 'Mean = 40 ÷ 4 = 10',
  'Divide the total, forty, by four. The mean is ten.'),
 ('CHECK', 'Mean times count recovers the total', '10 × 4 = 40',
  'Four equal shares of ten would have the same total as the original values. Ten times four is forty.')],
 source(6,11,4,3),expression='(6+11+8+15)/4',value='10'),

authored('statistics-median','Finding the median',
 'Find the median:\n17, 5, 12, 9, 21, 8', '10.5',
 "Let's find the median of these six numbers. The median describes the middle of the ordered data.",[
 ('ORDER', 'Sort the numbers first', '5, 8, 9, 12, 17, 21',
  'Put the numbers in order: five, eight, nine, twelve, seventeen, twenty-one.'),
 ('FIND THE MIDDLE', 'An even count has two middle positions', '6 values → positions 3 and 4\nMiddle values: 9 and 12',
  'There are six values, an even count. The middle two are in positions three and four: nine and twelve.'),
 ('AVERAGE THE MIDDLE TWO', 'Add and divide by 2', 'Median = (9 + 12)/2 = 10.5',
  'Average those two values. Nine plus twelve, divided by two, is ten point five.'),
 ('CHECK THE RULE', 'The median need not be a data value', 'Even count: average the middle two.\nOdd count: use the one middle value.',
  'The median is ten point five, even though it is not in the list. For an odd number of values, simply use the one middle value.')],
 source(6,11,4,7),expression='(9+12)/2',value='10.5'),

authored('statistics-mode','Finding the mode',
 'Find the mode:\n6, 9, 6, 4, 9, 6, 12', '6',
 "Let's find the mode. It is the value that appears most often.",[
 ('SORT', 'Group equal values together', '4, 6, 6, 6, 9, 9, 12',
  'Sorting makes repeated values easier to see: four, three sixes, two nines, and twelve.'),
 ('COUNT', 'Count each value’s frequency', '4: once     6: three times\n9: twice     12: once',
  'Six appears three times. Nine appears twice. Four and twelve each appear once.'),
 ('CHOOSE', 'Select the greatest frequency', 'Mode = 6',
  'Six occurs most often, so the mode is six. Report the value, not the number of times it appears.'),
 ('TIES', 'A data set can have more than one mode', 'Tie for highest frequency → report both.\nNo repeated values → no mode.',
  'If two values tie for the highest frequency, report both. If no value repeats, report no mode.')],
 source(6,11,2,8),expression='1+3+2+1',value='7'),

authored('statistics-spread','Comparing spread with the range',
 'Which data set has the larger range?\nA: 5, 6, 6, 7, 8    B: 1, 4, 6, 9, 12', 'B; ranges are 3 and 11',
 "Let's compare two data sets using their ranges. Range is the largest value minus the smallest.",[
 ('DATA SET A', 'Subtract A’s smallest value from its largest', 'Range A = 8 − 5 = 3',
  'Set A runs from five to eight. Its range is eight minus five, or three.'),
 ('DATA SET B', 'Subtract B’s smallest value from its largest', 'Range B = 12 − 1 = 11',
  'Set B runs from one to twelve. Its range is twelve minus one, or eleven.'),
 ('COMPARE', 'A larger range means more spread by this measure', '11 > 3 → B has the larger range.',
  'Eleven is greater than three, so set B has more spread when measured by range.'),
 ('INTERPRET', 'Range uses only the two endpoints', 'Range = maximum − minimum',
  'The dot plots show the wider spread in set B. Remember that range only uses the largest and smallest values.')],
 source(6,11,1,2),expression='12-1',value='11',equalities=[('8-5','3')]),

authored('statistics-mean-absolute-deviation','Mean absolute deviation',
 'Find the mean absolute deviation:\n2, 6, 10, 14', '4',
 "Let's find the mean absolute deviation of two, six, ten, and fourteen. It measures the average distance from the mean.",[
 ('MEAN', 'First find the center', '(2 + 6 + 10 + 14)/4 = 8',
  'The total is thirty-two. Divide by four to get a mean of eight.'),
 ('DISTANCES', 'Find each distance from 8', '|2 − 8| = 6     |6 − 8| = 2\n|10 − 8| = 2     |14 − 8| = 6',
  'Find each value’s distance from eight. The distances are six, two, two, and six. Distances are never negative.'),
 ('AVERAGE', 'Find the mean of the distances', 'MAD = (6 + 2 + 2 + 6)/4 = 4',
  'Add the four distances and divide by four. Sixteen divided by four is four.'),
 ('INTERPRET', 'Read MAD as an average distance', 'Mean = 8;   MAD = 4',
  'The data values are, on average, four units away from the mean of eight.')],
 source(6,11,10,8),expression='(6+2+2+6)/4',value='4',equalities=[('(2+6+10+14)/4','8')]),

authored('statistics-missing-value-from-mean','Finding a missing data value',
 'The mean is 14. Find the missing value:\n8, 11, ?, 17, 19', '15',
 "Five numbers have a mean of fourteen. Four of them are eight, eleven, seventeen, and nineteen. Let's find the missing value.",[
 ('REQUIRED TOTAL', 'Multiply the mean by the count', '14 × 5 = 70',
  'The total must be the mean times the number of values. Fourteen times five is seventy.'),
 ('KNOWN TOTAL', 'Add the known values', '8 + 11 + 17 + 19 = 55',
  'Add the four known values. Their total is fifty-five.'),
 ('MISSING PART', 'Subtract from the required total', 'Missing value = 70 − 55 = 15',
  'Subtract fifty-five from seventy. The missing value is fifteen.'),
 ('CHECK', 'Recalculate the mean', '(8 + 11 + 15 + 17 + 19)/5 = 14',
  'Put fifteen back in the list. The total is seventy, and dividing by five gives the required mean of fourteen.')],
 source(6,11,5,3),expression='14*5-(8+11+17+19)',value='15',equalities=[('(8+11+15+17+19)/5','14')]),

authored('statistics-box-plot-summary','Reading a box plot',
 'Read the median, range and IQR\nof this box plot with no outliers.', 'Median = 13; range = 22; IQR = 10',
 "Let's read this box plot, which has no outliers. We want its median, range, and interquartile range.",[
 ('FIVE-NUMBER SUMMARY', 'Read the whiskers and box edges', 'Minimum 4; Q1 8; median 13; Q3 18; maximum 26',
  'The whiskers are at four and twenty-six. The box edges are eight and eighteen, with a median line at thirteen.'),
 ('RANGE', 'Subtract the minimum from the maximum', 'Range = 26 − 4 = 22',
  'The range is twenty-six minus four, which is twenty-two.'),
 ('INTERQUARTILE RANGE', 'Subtract Q1 from Q3', 'IQR = 18 − 8 = 10',
  'The interquartile range is the width of the box. Eighteen minus eight is ten.'),
 ('INTERPRET', 'The box represents the middle half', 'Median = 13; range = 22; IQR = 10',
  'The box runs from eight to eighteen and represents the middle half of the data. The median is thirteen.')],
 source(6,11,'8Rev',5),expression='26-4',value='22',equalities=[('18-8','10')]),

authored('statistics-normal-distribution','Reading a normal distribution',
 'Mean = 92; standard deviation = 7.\nFind the interval within 1 standard deviation.', '85 to 99',
 "A normal distribution has mean ninety-two and standard deviation seven. Let's find the interval within one standard deviation of the mean.",[
 ('CENTER', 'The mean is at the center of the bell', 'Mean = 92',
  'The normal curve is bell-shaped and symmetric about ninety-two. Half the distribution lies on either side of the mean.'),
 ('LOWER END', 'Subtract one standard deviation', '92 − 7 = 85',
  'Subtract seven from the mean. The lower endpoint is eighty-five.'),
 ('UPPER END', 'Add one standard deviation', '92 + 7 = 99',
  'Add seven to the mean. The upper endpoint is ninety-nine.'),
 ('INTERVAL', 'Use both endpoints', '85 ≤ value ≤ 99',
  'The interval is eighty-five to ninety-nine. A larger standard deviation would spread the curve and these endpoints farther apart.')],
 source(11,12,1,6),expression='92-7',value='85',equalities=[('92+7','99')]),

authored('statistics-standard-deviation','The empirical rule',
 'Normal times: mean 60 min, SD 8 min.\nAbout what percent lie from 44 to 76 min?', 'About 95%',
 "Normally distributed times have mean sixty minutes and standard deviation eight minutes. About what percent lie between forty-four and seventy-six?",[
 ('DISTANCE FROM THE MEAN', 'Both endpoints are 16 minutes away', '60 − 44 = 16;   76 − 60 = 16',
  'Both endpoints are sixteen minutes from the mean.'),
 ('COUNT STANDARD DEVIATIONS', 'Divide the distance by the standard deviation', '16 ÷ 8 = 2 standard deviations',
  'Sixteen divided by eight is two, so this interval extends two standard deviations each way.'),
 ('EMPIRICAL RULE', 'Use the normal-distribution percentages', 'Within 1 SD: about 68%\nWithin 2 SD: about 95%\nWithin 3 SD: about 99.7%',
  'For a normal distribution, about sixty-eight percent lies within one standard deviation, ninety-five within two, and ninety-nine point seven within three.'),
 ('ANSWER', 'Choose the two-standard-deviation interval', '44 to 76 minutes → about 95%',
  'Our interval is within two standard deviations, so it contains about ninety-five percent of the times.')],
 source(11,12,1,4),expression='16/8',value='2',equalities=[('60-2*8','44'),('60+2*8','76')]),

authored('statistics-z-scores','Calculating a z-score',
 'Mean = 64; standard deviation = 8.\nFind the z-score of 84.', '2.5',
 "Let's find the z-score of eighty-four when the mean is sixty-four and the standard deviation is eight.",[
 ('FORMULA', 'Measure distance in standard deviations', 'z = (value − mean)/(standard deviation)',
  'Subtract the mean from the value, then divide by the standard deviation.'),
 ('SUBTRACT', 'Find the signed difference from the mean', '84 − 64 = 20',
  'Eighty-four minus sixty-four is positive twenty.'),
 ('DIVIDE', 'Divide by the standard deviation', 'z = 20/8 = 2.5',
  'Twenty divided by eight is two point five. That is the z-score.'),
 ('INTERPRET', 'The sign shows above or below the mean', '84 is 2.5 standard deviations above the mean.',
  'A positive z-score means above the mean. A value below the mean gives a negative score, and a value at the mean gives zero.')],
 source(11,12,'1Rev',5),expression='(84-64)/8',value='2.5'),

authored('statistics-regression','Predictions and residuals',
 'Model: predicted y = 4x + 7.\nAt x = 6, actual y = 35. Find the residual.', 'Prediction = 31; residual = 4',
 "A model predicts y equals four x plus seven. At x equals six, the actual value is thirty-five. Let's find the residual.",[
 ('PREDICT', 'Substitute x into the fitted model', 'Predicted y = 4(6) + 7 = 31',
  'Substitute six into the model. Four times six plus seven gives a prediction of thirty-one.'),
 ('RESIDUAL RULE', 'Actual minus predicted', 'Residual = actual − predicted',
  'A residual is the actual value minus the predicted value. Keep that order.'),
 ('SUBTRACT', 'Calculate the signed difference', 'Residual = 35 − 31 = 4',
  'Thirty-five minus thirty-one is positive four.'),
 ('INTERPRET', 'A positive residual lies above the fitted line', 'The actual value is 4 above the prediction.',
  'The actual observation is four units above the fitted line. A negative residual would mean below the line.')],
 source(8,7,10,3),expression='35-(4*6+7)',value='4',equalities=[('4*6+7','31')]),

authored('statistics-correlation','Reading a scatter plot',
 'Describe the association in this scatter plot.', 'Negative, approximately linear association; it does not establish causation',
 "Let's describe the association in this scatter plot. Look at the overall pattern instead of just one point.",[
 ('DIRECTION', 'Follow the points from left to right', 'As x increases, y tends to decrease.',
  'As x increases, y tends to decrease. The points have an overall downward trend.'),
 ('ASSOCIATION', 'A downward trend is negative', 'Negative association',
  'A downward trend is called a negative association.'),
 ('FORM', 'Look for a straight or curved pattern', 'Approximately linear, with some scatter',
  'These points roughly follow a straight line, with some scatter. The association is approximately linear.'),
 ('LIMIT', 'Association alone does not prove a cause', 'Negative association ≠ proof of causation',
  'This pattern alone does not prove that changing x causes y to change. Other explanations may account for the association.')],
 source(8,7,1,1),expression='216-21*71/6',value='-65/2'),
]


def white_card(d):
    d.rounded_rectangle((145,360,1775,840),radius=35,fill='white')


def draw_scatter(spec,d,scene,p):
    white_card(d)
    x0,y0=550,735; sx,sy=112,18
    d.line((x0,y0,x0+7*sx,y0),fill=video.INK,width=4)
    d.line((x0,y0,x0,y0-18*sy),fill=video.INK,width=4)
    for x in range(1,7):
        video.text(d,(x0+x*sx,y0+12),str(x),27,video.MUTED,anchor='mt')
    for y in [0,4,8,12,16]:
        video.text(d,(x0-20,y0-y*sy),str(y),27,video.MUTED,anchor='rm')
    for x,y in zip(range(1,7),[16,14,15,10,9,7]):
        px,py=x0+x*sx,y0-y*sy
        d.ellipse((px-11,py-11,px+11,py+11),fill=video.TEAL)
    video.text(d,(x0+7*sx+28,y0),'x',30,video.INK,anchor='lm')
    video.text(d,(x0,y0-18*sy-25),'y',30,video.INK,anchor='mm')
    if scene in [1,2,3]:d.line((x0+sx,y0-16*sy,x0+6*sx,y0-7*sy),fill='#c58b37',width=4)
    label=['Six paired observations','Overall trend: downward','Negative association','Approximately linear','Association does not establish causation'][scene]
    video.centered(d,900,label,39,video.TEAL,True)


def draw_range(spec,d,scene,p):
    white_card(d)
    for label,values,y in [('A',[5,6,6,7,8],505),('B',[1,4,6,9,12],730)]:
        video.text(d,(245,y-35),label,54,video.TEAL,True)
        x0=450;scale=90
        d.line((x0,y,x0+13*scale,y),fill=video.INK,width=3)
        for x in range(14):video.text(d,(x0+x*scale,y+12),str(x),25,video.MUTED,anchor='mt')
        counts=Counter()
        for x in values:
            py=y-28-counts[x]*30;counts[x]+=1;px=x0+x*scale
            d.ellipse((px-10,py-10,px+10,py+10),fill=video.TEAL)
    labels=['Compare the two ranges','Range A = 8 − 5 = 3','Range B = 12 − 1 = 11','B has the larger range: 11 > 3','Range = maximum − minimum']
    video.centered(d,900,labels[scene],40,video.TEAL,True)


def draw_box(spec,d,scene,p):
    white_card(d)
    x=lambda n:300+n*50
    y=570
    d.line((x(4),y,x(26),y),fill=video.INK,width=5)
    d.line((x(4),y-42,x(4),y+42),fill=video.INK,width=5)
    d.line((x(26),y-42,x(26),y+42),fill=video.INK,width=5)
    d.rectangle((x(8),y-70,x(18),y+70),fill='#d6eeeb',outline=video.TEAL,width=5)
    d.line((x(13),y-70,x(13),y+70),fill=video.TEAL,width=7)
    for n,label in [(4,'min'),(8,'Q1'),(13,'median'),(18,'Q3'),(26,'max')]:
        video.text(d,(x(n),y-125),label,30,video.MUTED,anchor='mt')
        video.text(d,(x(n),y+92),str(n),38,video.INK,True,anchor='mt')
    labels=['Find the median, range and IQR','Five-number summary: 4, 8, 13, 18, 26','Range = 26 − 4 = 22','IQR = 18 − 8 = 10','The box represents the middle half of the data.']
    video.centered(d,900,labels[scene],38,video.TEAL,True)


def draw_normal(spec,d,scene,p):
    # One standard normal shape; transform the tick labels to the given units.
    if spec['video_id']=='statistics-standard-deviation' and scene==3:
        draw_card(spec,d,scene,p);return
    white_card(d)
    empirical=spec['video_id']=='statistics-standard-deviation'
    mean,sd,bound=(60,8,2) if empirical else (92,7,1)
    x=lambda z:960+z*180
    y=lambda z:730-270*exp(-z*z/2)
    z_values=[-3.5+i*.025 for i in range(281)]
    shaded=[z for z in z_values if -bound<=z<=bound]
    d.polygon([(x(-bound),730)]+[(x(z),y(z)) for z in shaded]+[(x(bound),730)],fill='#d6eeeb')
    d.line([(x(z),y(z)) for z in z_values],fill=video.TEAL,width=5)
    d.line((x(-3.5),730,x(3.5),730),fill=video.INK,width=3)
    for z in range(-3,4):
        px=x(z);d.line((px,730,px,742),fill=video.INK,width=3)
        video.text(d,(px,758),str(mean+z*sd),30,video.INK,anchor='mt')
    d.line((x(0),730,x(0),y(0)),fill='#c58b37',width=3)
    if empirical:
        labels=['Mean 60; standard deviation 8','44 and 76 are 16 minutes from the mean','16 ÷ 8 = 2 standard deviations','','Within 2 standard deviations: about 95%']
    else:
        labels=['One standard deviation each side of 92','A symmetric bell, centered at 92','Lower endpoint: 92 − 7 = 85','Upper endpoint: 92 + 7 = 99','Interval: 85 to 99']
    video.centered(d,900,labels[scene],39,video.TEAL,True)


def lessons(doc):
    assert F(sum([6,11,8,15]),4)==10
    assert median([17,5,12,9,21,8])==10.5
    assert Counter([6,9,6,4,9,6,12]).most_common(1)==[(6,3)]
    data=[2,6,10,14];mean=F(sum(data),len(data))
    assert mean==8 and sum(abs(F(v)-mean) for v in data)/len(data)==4
    assert round(erf(1/sqrt(2))*100)==68
    assert round(erf(2/sqrt(2))*100)==95
    assert round(erf(3/sqrt(2))*100,1)==99.7
    assert sum(x*y for x,y in zip(range(1,7),[16,14,15,10,9,7]))-F(21*71,6)<0
    result=make_lessons(SPECS,doc)
    custom={'statistics-correlation':draw_scatter,'statistics-spread':draw_range,
            'statistics-box-plot-summary':draw_box,'statistics-normal-distribution':draw_normal,
            'statistics-standard-deviation':draw_normal}
    for spec in SPECS:
        if spec['video_id'] in custom:
            video.DRAW[spec['video_id']]=lambda d,scene,p,s=spec,fn=custom[spec['video_id']]:fn(s,d,scene,p)
    return result
