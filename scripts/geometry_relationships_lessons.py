"""Area relationships and inverse formulas, with original checked examples."""
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons,draw_card,centered_math
import generate_sample_videos as v

SPECS=[
authored('geometry-medial-triangle-measures','Perimeter and area of a medial triangle',
 'A triangle has perimeter 54 cm and area 96 cm².\nJoin its side midpoints. Find the new triangle’s\nperimeter and area.','27 centimetres; 24 square centimetres',
 'A triangle has perimeter fifty-four centimetres and area ninety-six square centimetres. Join its side midpoints. Find the new triangle\'s perimeter and area.',[
 ('MIDPOINTS','Each new side is half the matching original side','Length scale factor = 1/2',
  'The midpoint theorem makes each new side half the matching original side. The triangles are similar.'),
 ('PERIMETER','Every side length is halved','54 × 1/2 = 27 cm',
  'Perimeter scales like length. Half of fifty-four is twenty-seven centimetres.'),
 ('AREA','Square the length scale factor','(1/2)² = 1/4\n96 × 1/4 = 24 cm²',
  'Area scales by the square of the length factor. One half squared is one quarter. A quarter of ninety-six is twenty-four square centimetres.'),
 ('COMPARE','Length and area use different scale factors','Perimeter: ×1/2     Area: ×1/4',
  'The medial triangle has perimeter twenty-seven centimetres and area twenty-four square centimetres. Halving lengths quarters area.')],
 g(10,8,3,3),expression='96/4',value='24',equalities=[('54/2','27')]),

authored('geometry-circle-area-scaling','How radius ratios change circle areas',
 'Two circles have radii in the ratio 4:7.\nWhat is their area ratio, in the same order?','16:49',
 'Two circles have radii in the ratio four to seven. What is their area ratio, in the same order?',[
 ('USE THE AREA FORMULA','Circle area is pi times radius squared','Area ratio = π × (radius A)² : π × (radius B)²',
  'Circle area is pi times radius squared. Compare the two radius squares.'),
 ('CANCEL THE COMMON FACTOR','Both areas contain pi','Area ratio = 4² : 7²',
  'The common factor pi cancels, so square both parts of the radius ratio.'),
 ('CALCULATE','Keep the original order','16:49',
  'Four squared is sixteen, and seven squared is forty-nine. The area ratio is sixteen to forty-nine.'),
 ('GENERAL RULE','A radius multiplier is squared for area','Radius ×k → area ×k²',
  'In general, multiplying a radius by k multiplies area by k squared. Use the same rule for a single circle growing or shrinking.')],
 g(10,11,5,10),expression='4**2/7**2',value='16/49'),

authored('geometry-area-semicircle','Area of a semicircle',
 'A semicircle has radius 12 cm.\nFind its exact area in terms of pi.','72π square centimetres',
 'A semicircle has radius twelve centimetres. Find its exact area in terms of pi.',[
 ('WHOLE CIRCLE','Start with pi times radius squared','A = π × 12²',
  'First find the area of the whole circle using pi times radius squared.'),
 ('SQUARE THE RADIUS','Twelve times twelve is one hundred forty-four','Whole circle area = 144π cm²',
  'Twelve squared is one hundred forty-four, so the full circle area is one hundred forty-four pi.'),
 ('TAKE HALF','A semicircle is half a circle','144π ÷ 2 = 72π cm²',
  'Divide by two. The semicircle area is seventy-two pi square centimetres.'),
 ('GENERAL RULE','Keep the one-half factor','Semicircle area = ½πr²',
  'A semicircle has area one half pi r squared. This measures its surface, so use square units.')],
 g(7,9,1,6),expression='12**2/2',value='72'),

authored('geometry-circle-diameter-from-area','Find a circle diameter from area',
 'A circle has area 121π cm². Find its diameter.','22 centimetres',
 'A circle has area one hundred twenty-one pi square centimetres. Find its diameter.',[
 ('AREA EQUATION','Set pi times radius squared equal to the area','πr² = 121π',
  'Use the circle area formula. Pi times radius squared equals one hundred twenty-one pi.'),
 ('DIVIDE BY PI','Cancel the same nonzero factor','r² = 121',
  'Divide both sides by pi. Radius squared equals one hundred twenty-one.'),
 ('POSITIVE SQUARE ROOT','A radius is a positive length','r = 11 cm',
  'Eleven squared is one hundred twenty-one. Take the positive radius of eleven centimetres.'),
 ('DOUBLE THE RADIUS','Diameter runs all the way across the centre','d = 2 × 11 = 22 cm',
  'The diameter is twice the radius, so it is twenty-two centimetres.')],
 g(7,9,2,1),expression='2*11',value='22',equalities=[('11**2','121')]),

authored('geometry-area-isosceles-pythagoras','Isosceles triangle area using Pythagoras',
 'An isosceles triangle has equal sides 26 cm\nand base 20 cm. Find its area.','240 square centimetres',
 'An isosceles triangle has equal sides twenty-six centimetres and base twenty centimetres. Find its area.',[
 ('SPLIT THE BASE','The perpendicular height bisects the base','Half the base = 20 ÷ 2 = 10 cm',
  'Draw the perpendicular height from the top vertex. In an isosceles triangle, it splits the base into two ten-centimetre halves.'),
 ('PYTHAGORAS','Use one right triangle with hypotenuse twenty-six','h² + 10² = 26²\nh² = 676 − 100 = 576',
  'Use Pythagoras on either right triangle. Height squared is twenty-six squared minus ten squared, giving five hundred seventy-six.'),
 ('FIND THE HEIGHT','Take the positive square root','h = 24 cm',
  'Twenty-four squared is five hundred seventy-six, so the height is twenty-four centimetres.'),
 ('USE THE FULL BASE','Area is half of base times height','A = ½ × 20 × 24 = 240 cm²',
  'Use the full twenty-centimetre base for the area. One half times twenty times twenty-four is two hundred forty square centimetres.')],
 g(8,5,5,5),expression='20*24/2',value='240',equalities=[('26**2-10**2','24**2')]),

authored('geometry-square-area-from-perimeter','Find a square area from its perimeter',
 'A square has perimeter 28 cm. Find its area.','49 square centimetres',
 'A square has perimeter twenty-eight centimetres. Find its area.',[
 ('FOUR EQUAL SIDES','The perimeter includes four copies of the side','4 × side = 28',
  'A square has four equal sides, and the perimeter counts all four.'),
 ('FIND ONE SIDE','Divide the perimeter by four','side = 28 ÷ 4 = 7 cm',
  'Divide twenty-eight by four to get a side length of seven centimetres.'),
 ('FIND THE AREA','Multiply the side length by itself','Area = 7 × 7 = 49 cm²',
  'Multiply seven by seven. The area is forty-nine square centimetres.'),
 ('CHECK','Recover the given perimeter','4 × 7 = 28 cm',
  'Four times seven gives the original perimeter of twenty-eight centimetres. Find the side first, then square it for area.')],
 g(3,11,3,10),expression='(28/4)**2',value='49'),

authored('geometry-parallelogram-height-from-area','Find a parallelogram height from area',
 'A parallelogram has area 96 cm² and base 12 cm.\nA student claims its height is 9 cm. Check the claim.','Incorrect; the height is 8 centimetres',
 'A parallelogram has area ninety-six square centimetres and base twelve centimetres. A student claims its height is nine centimetres. Check the claim.',[
 ('TEST THE CLAIM','Multiply the base by the proposed height','12 × 9 = 108 cm²',
  'Test the proposed height. Twelve times nine gives one hundred eight square centimetres.'),
 ('COMPARE','The predicted area must match the given area','108 ≠ 96, so the claim is incorrect.',
  'One hundred eight does not match ninety-six, so the claimed height is incorrect.'),
 ('FIND THE HEIGHT','Divide the area by the base','h = 96 ÷ 12 = 8 cm',
  'Divide the given area by the base. Ninety-six divided by twelve is eight centimetres.'),
 ('CHECK','Use the perpendicular height','12 × 8 = 96 cm²',
  'Twelve times eight gives the correct area. The perpendicular height is eight centimetres.')],
 g(6,8,1,7),expression='96/12',value='8',equalities=[('12*9','108')]),

authored('geometry-area-triangle-missing-dimension','Find a missing triangle base or height',
 'A triangle has area 99 cm² and height 11 cm.\nFind its base.','18 centimetres',
 'A triangle has area ninety-nine square centimetres and perpendicular height eleven centimetres. Find its base.',[
 ('AREA FORMULA','Half of base times height gives area','½ × b × 11 = 99',
  'Set one half times the base times eleven equal to ninety-nine.'),
 ('UNDO THE HALF','Double the given area','b × 11 = 198',
  'Multiply both sides by two. Base times eleven equals one hundred ninety-eight.'),
 ('DIVIDE','Divide by the known dimension','b = 198 ÷ 11 = 18 cm',
  'Divide by eleven. The base is eighteen centimetres.'),
 ('CHECK AND GENERALIZE','Use the same rearrangement for an unknown height','½ × 18 × 11 = 99 cm²\nMissing dimension = 2 × area ÷ known dimension',
  'Check by substituting the base back into the area formula. For either an unknown base or height, double the area and divide by the known dimension.')],
 g(6,8,2,6),expression='2*99/11',value='18'),

authored('geometry-area-trapezoid-missing-dimension','Find a trapezoid base using its area',
 'A trapezoid has area 69 cm² and height 6 cm.\nIts bases are 9 cm and (x + 4) cm. Find x.','10',
 'A trapezoid has area sixty-nine square centimetres and height six centimetres. Its bases are nine centimetres and x plus four centimetres. Find x.',[
 ('FIND THE BASE SUM','Double the area, then divide by height','Base sum = 2 × 69 ÷ 6 = 23 cm',
  'Area is half the base sum times height. Double the area and divide by height to get a base sum of twenty-three centimetres.'),
 ('FIND THE UNKNOWN BASE','Subtract the known base','Unknown base = 23 − 9 = 14 cm',
  'Subtract the known nine-centimetre base. The other base is fourteen centimetres.'),
 ('SOLVE FOR X','The whole base is x plus four','x + 4 = 14\nx = 10',
  'Since x plus four equals fourteen, subtract four to find x equals ten.'),
 ('CHECK','Use the actual base length, fourteen','½ × (9 + 14) × 6 = 69 cm²',
  'Check with the actual base lengths nine and fourteen. The formula gives the original area of sixty-nine square centimetres.')],
 g(6,8,4,9),expression='2*69/6-9-4',value='10',equation=('(9+x+4)*6/2','69','x','10')),

authored('geometry-rectangle-perimeter-equation','Solve a rectangle perimeter equation',
 'A rectangle has width x and length 4x.\nIts perimeter is 70 cm. Find x.','7 centimetres',
 'A rectangle has width x and length four x. Its perimeter is seventy centimetres. Find x.',[
 ('SUBSTITUTE','The boundary includes two lengths and two widths','2 × (4x + x) = 70',
  'Substitute the length and width into twice length plus width.'),
 ('SIMPLIFY','Combine like terms inside the brackets','2 × 5x = 70\n10x = 70',
  'Four x plus x is five x. Multiplying by two gives ten x equals seventy.'),
 ('SOLVE','Divide both sides by ten','x = 70 ÷ 10 = 7 cm',
  'Divide by ten. The width x is seven centimetres.'),
 ('CHECK','The length is four times the width','Length = 28 cm\n2 × (28 + 7) = 70 cm',
  'The length is twenty-eight centimetres. Twice twenty-eight plus seven recovers the perimeter of seventy centimetres.')],
 g(8,2,3,3),expression='70/10',value='7',equation=('2*(4*x+x)','70','x','7')),

authored('geometry-area-two-triangles','Add the areas of two triangles',
 'A shape is split into two triangles without overlap.\nTheir bases are 9 cm and 5 cm; each height is 4 cm.\nFind the total area.','28 square centimetres',
 'A shape is split into two triangles without overlap. Their bases are nine and five centimetres, and each perpendicular height is four centimetres. Find the total area.',[
 ('FIRST TRIANGLE','Use half of base times height','½ × 9 × 4 = 18 cm²',
  'The first triangle has area one half times nine times four, or eighteen square centimetres.'),
 ('SECOND TRIANGLE','Find the second area separately','½ × 5 × 4 = 10 cm²',
  'The second triangle has area ten square centimetres.'),
 ('ADD THE PARTS','The triangles cover the shape without overlap','18 + 10 = 28 cm²',
  'Add the two non-overlapping areas to get twenty-eight square centimetres.'),
 ('GENERAL RULE','Count each part once','Total = triangle one area + triangle two area\nFor two identical triangles: total = 2 × one area',
  'Find each triangle area and add. If the triangles are identical, calculate one area and double it.')],
 g(6,8,4,1),expression='9*4/2+5*4/2',value='28'),

authored('geometry-triangle-equal-height-compare-bases','Compare triangle bases with equal heights',
 'Triangles A and B both have height 5 cm.\nTheir areas are 35 cm² and 25 cm².\nWhich has the longer base?','Triangle A; its base is 14 cm versus 10 cm',
 'Triangles A and B both have perpendicular height five centimetres. Their areas are thirty-five and twenty-five square centimetres. Which has the longer base?',[
 ('REARRANGE','Base is twice the area divided by height','base = 2 × area ÷ height',
  'Rearrange the triangle area formula. Base is twice the area divided by the height.'),
 ('FIND BOTH BASES','The same height is used in both calculations','A: 2 × 35 ÷ 5 = 14 cm\nB: 2 × 25 ÷ 5 = 10 cm',
  'Triangle A has base fourteen centimetres. Triangle B has base ten centimetres.'),
 ('COMPARE','Fourteen is greater than ten','Triangle A has the longer base.',
  'Fourteen is greater than ten, so triangle A has the longer base.'),
 ('GENERAL RULE','Equal heights make area proportional to base','Same height → larger area means longer base',
  'With equal heights, larger area means a longer base. This comparison depends on the heights being equal.')],
 g(6,8,4,11),expression='2*35/5',value='14',equalities=[('2*25/5','10')]),

authored('geometry-perimeter-rectangle-missing-dimension','Find a rectangle side from perimeter',
 'A rectangle has perimeter 46 cm and length 8 cm.\nFind its width.','15 centimetres',
 'A rectangle has perimeter forty-six centimetres and length eight centimetres. Find its width.',[
 ('HALVE THE BOUNDARY','Half the perimeter is one length plus one width','length + width = 46 ÷ 2 = 23 cm',
  'Divide the perimeter by two. One length plus one width is twenty-three centimetres.'),
 ('SUBTRACT THE KNOWN SIDE','The remaining part is the width','width = 23 − 8 = 15 cm',
  'Subtract the known eight-centimetre length. The width is fifteen centimetres.'),
 ('CHECK','Both pairs of opposite sides count','2 × (8 + 15) = 46 cm',
  'Check that twice eight plus fifteen gives the original forty-six-centimetre perimeter.'),
 ('GENERAL RULE','The same formula works with a variable side','Other side = perimeter ÷ 2 − known side\nIf the known side is x: other side = P/2 − x',
  'Subtract the known side from half the perimeter. If that side is called x, the other side is P over two minus x.')],
 g(3,11,2,5),expression='46/2-8',value='15'),
]


def diagram(spec,d,scene,p):
    vid=spec['video_id']
    if scene!=1:return draw_card(spec,d,scene,p)
    if vid=='geometry-medial-triangle-measures':
        a,b,c=(680,760),(1240,760),(900,400)
        d.polygon([a,b,c],fill='#D0E8E2',outline=v.TEAL,width=4)
        mids=[((u[0]+w[0])/2,(u[1]+w[1])/2) for u,w in [(a,b),(b,c),(c,a)]]
        d.polygon(mids,fill='#F1DBB9',outline=v.TEAL,width=5)
        for x,y in mids:d.ellipse((x-7,y-7,x+7,y+7),fill=v.INK)
    elif vid=='geometry-area-isosceles-pythagoras':
        x,y,s=730,800,16
        d.polygon([(x,y),(x+20*s,y),(x+10*s,y-24*s)],fill='#D0E8E2',outline=v.TEAL,width=4)
        d.line((x+10*s,y,x+10*s,y-24*s),fill=v.INK,width=3)
        d.line((x+10*s,y-15,x+10*s+15,y-15,x+10*s+15,y),fill=v.INK,width=3)
        v.text(d,(x-85,y-210),'26 cm',36,v.INK,True);v.text(d,(x+20*s-5,y-210),'26 cm',36,v.INK,True)
        v.text(d,(x+20,y+12),'10 cm',32,v.INK,True);v.text(d,(x+180,y+12),'10 cm',32,v.INK,True)
        v.text(d,(x+10*s+20,y-250),'h',40,v.INK,True)
    elif vid=='geometry-area-semicircle':
        d.pieslice((720,420,1200,900),180,360,fill='#D0E8E2',outline=v.TEAL,width=4)
        d.line((960,660,1200,660),fill=v.INK,width=4)
        d.ellipse((953,653,967,667),fill=v.INK)
        v.text(d,(1020,600),'12 cm',40,v.INK,True)
    else:return draw_card(spec,d,scene,p)
    centered_math(d,890,spec['displays'][scene],43,v.TEAL)


def lessons(doc):
    assert 10**2+24**2==26**2
    result=make_lessons(SPECS,doc)
    for spec in SPECS:v.DRAW[spec['video_id']]=lambda d,scene,p,s=spec:diagram(s,d,scene,p)
    return result
