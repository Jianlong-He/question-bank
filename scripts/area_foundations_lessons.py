"""Simple area/whole concepts and finding a derived parallelogram height."""
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons,draw_card,centered_math
import generate_sample_videos as v

SPECS=[
authored('geometry-whole-area-from-halves','Find the whole area from two equal halves',
 'A rectangle is split into two equal halves.\nEach half covers 6 little squares.\nHow many little squares does the whole rectangle cover?','12 little squares',
 'A rectangle is split into two equal halves. Each half covers six little squares. How many little squares does the whole rectangle cover?',[
 ('ONE HALF','Count the squares in one half','One half: 6 squares',
  'One half covers six little squares.'),
 ('THE OTHER HALF','Equal halves cover equal areas','Other half: 6 squares',
  'The other half is equal, so it also covers six little squares.'),
 ('PUT THE HALVES TOGETHER','Add the two equal parts','6 + 6 = 12 squares',
  'Put the two halves together. Six plus six is twelve.'),
 ('THE WHOLE','Two halves make one whole','Whole rectangle: 12 little squares',
  'The whole rectangle covers twelve little squares. To find a whole from one of two equal halves, add that half twice.')],
 g(1,3,7,10),expression='6+6',value='12'),

authored('geometry-area-unit-square-count-compare','Measure and compare area with unit squares',
 'Shape A covers 11 unit squares. Shape B covers 14.\nThe unit squares are the same size.\nFind each area and decide which shape covers more space.','A: 11 square units; B: 14 square units; B is larger',
 'Shape A covers eleven unit squares, and shape B covers fourteen. The unit squares are the same size. Find each area and decide which shape covers more space.',[
 ('ONE UNIT','A unit square covers one square unit','1 unit square → 1 square unit of area',
  'Each unit square covers one square unit of area.'),
 ('COUNT THE COVERING SQUARES','No gaps or overlaps','Area A = 11 square units\nArea B = 14 square units',
  'Count squares covering each shape without gaps or overlaps. A has area eleven square units; B has area fourteen.'),
 ('COMPARE','More equal-size squares means more area','14 > 11, so Shape B covers more space.',
  'Fourteen is greater than eleven, so shape B covers more space.'),
 ('USE MATCHING UNITS','The measuring squares must be the same size','Area = number of covering unit squares',
  'Always compare using the same size unit square. With square-metre tiles, the count gives the area in square metres.')],
 g(3,10,1,8),expression='14-11',value='3'),

authored('fractions-whole-number-denominator-one','Write a whole number as a fraction',
 'Six whole circles are shaded.\nWrite the shaded amount as a number\nand as a fraction with denominator 1.','6 and 6/1',
 'Six whole circles are shaded. Write the shaded amount as a number and as a fraction with denominator one.',[
 ('COUNT WHOLES','Each circle is one complete whole','6 whole circles',
  'There are six complete circles, so the shaded amount is six wholes.'),
 ('ONE PART PER WHOLE','Denominator one means each part is an entire whole','Each whole has 1 whole-size part.',
  'A denominator of one means each part is one whole.'),
 ('COUNT THE PARTS','Six whole-size parts give a numerator of six','6 wholes = 6/1',
  'There are six whole-size parts, so the numerator is six. The fraction is six over one.'),
 ('CHECK','Dividing by one preserves the number','6 ÷ 1 = 6\nIn general: n = n/1',
  'Six divided by one equals six. Any whole number can be written over one without changing its value.')],
 g(3,5,4,2),expression='6/1',value='6'),

authored('geometry-parallelogram-derived-height','Find area when height is half the base',
 'A parallelogram has base 18 cm.\nIts perpendicular height is half the base. Find its area.','162 square centimetres',
 'A parallelogram has base eighteen centimetres. Its perpendicular height is half the base. Find its area.',[
 ('FIND THE HEIGHT','Half the base means divide its length by two','h = 18 ÷ 2 = 9 cm',
  'First find the height. Half of eighteen is nine centimetres.'),
 ('USE THE AREA FORMULA','Multiply base by perpendicular height','A = 18 × 9',
  'The area formula is base times perpendicular height. Substitute eighteen and nine.'),
 ('CALCULATE','Multiply the two lengths','18 × 9 = 162 cm²',
  'Eighteen times nine is one hundred sixty-two square centimetres.'),
 ('KEEP THE TWO STEPS','The height must be found before the area','Find the height from the relationship.\nThen use A = base × height.',
  'Use the stated relationship to find the missing height first. Then calculate the parallelogram area using that height.')],
 g(6,8,1,10),expression='18*(18/2)',value='162'),
]


def squares(d,x,y,rows,size=55,color='#D0E8E2'):
    for r,cols in enumerate(rows):
        for c in range(cols):d.rectangle((x+c*size,y+r*size,x+(c+1)*size,y+(r+1)*size),fill=color,outline=v.TEAL,width=3)


def diagram(spec,d,scene,p):
    vid=spec['video_id']
    if vid=='geometry-whole-area-from-halves' and scene in (1,2,3):
        squares(d,710,410,[2,2,2],85)
        if scene in (2,3):squares(d,880,410,[2,2,2],85,'#F1DBB9')
        v.text(d,(795,715),'6',44,v.INK,True,anchor='mm')
        if scene in (2,3):v.text(d,(965,715),'6',44,v.INK,True,anchor='mm')
        centered_math(d,810,spec['displays'][scene],54,v.TEAL);return
    if vid=='geometry-area-unit-square-count-compare' and scene in (1,2):
        squares(d,540,450,[3,3,5]);squares(d,1080,450,[4,5,5],55,'#F1DBB9')
        v.text(d,(600,660),'Shape A: 11',40,v.INK,True);v.text(d,(1140,660),'Shape B: 14',40,v.INK,True)
        for i,line in enumerate(spec['displays'][scene].split('\n')):centered_math(d,755+i*64,line,44,v.TEAL)
        return
    if vid=='fractions-whole-number-denominator-one' and scene in (1,2):
        for r in range(2):
            for c in range(3):
                x,y=640+c*220,380+r*200;d.ellipse((x,y,x+150,y+150),fill='#D0E8E2',outline=v.TEAL,width=4)
        centered_math(d,835,spec['displays'][scene],45,v.TEAL);return
    draw_card(spec,d,scene,p)


def lessons(doc):
    assert sum([3,3,5])==11 and sum([4,5,5])==14
    result=make_lessons(SPECS,doc)
    for spec in SPECS:v.DRAW[spec['video_id']]=lambda d,scene,p,s=spec:diagram(s,d,scene,p)
    return result
