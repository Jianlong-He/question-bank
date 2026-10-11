"""Inverse lengths, measurement relationships, rings and composed area functions."""
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons,draw_card,centered_math
import generate_sample_videos as v

SPECS=[
authored('geometry-area-square-missing-dimension','Find a square’s side and perimeter from its area',
 'A square has area 64 cm².\nFind its side length and then its perimeter.',
 'Side: 8 cm; perimeter: 32 cm',
 'A square has area sixty-four square centimetres. Find its side length and then its perimeter.',[
 ('EQUAL SIDES','Area is one side multiplied by itself','side × side = 64',
  'All sides of a square are equal. Its area is one side multiplied by itself.'),
 ('FIND THE SIDE','Which number times itself gives sixty-four?','8 × 8 = 64\nSide length = 8 cm',
  'Eight times eight equals sixty-four, so each side is eight centimetres long.'),
 ('FIND THE PERIMETER','Add four equal side lengths','4 × 8 = 32 cm',
  'Perimeter measures the distance around all four sides. Four times eight gives thirty-two centimetres.'),
 ('CHECK THE UNITS','Area and side lengths use different units','Area: 64 cm²\nSide: 8 cm     Perimeter: 32 cm',
  'Area uses square units. Side length and perimeter use length units. Find the side first, then use it to calculate perimeter.')],
 g(3,10,3,10),expression='8**2',value='64',equalities=[('4*8','32')]),

authored('geometry-perimeter-from-area-rectangle','Find perimeter from rectangle area and one side',
 'A rectangle has area 72 cm² and length 9 cm.\nFind its perimeter.','34 centimetres',
 'A rectangle has area seventy-two square centimetres and length nine centimetres. Find its perimeter.',[
 ('FIND THE OTHER SIDE','Area equals length times width','9 × width = 72',
  'Find the width first. Length times width gives area, so nine times the width equals seventy-two.'),
 ('DIVIDE','Divide area by the known side','Width = 72 ÷ 9 = 8 cm',
  'Divide seventy-two by nine. The width is eight centimetres.'),
 ('ADD ALL FOUR SIDES','Use two lengths and two widths','Perimeter = 9 + 8 + 9 + 8 = 34 cm',
  'Now add all four sides: nine, eight, nine, and eight. The perimeter is thirty-four centimetres.'),
 ('CHECK BOTH MEASUREMENTS','Multiply for area; add for perimeter','Area: 9 × 8 = 72 cm²\nPerimeter: 2 × (9 + 8) = 34 cm',
  'Check that the two side lengths multiply to the given area. Then add them twice to get the perimeter.')],
 g(3,11,3,6),expression='2*(9+72/9)',value='34'),

authored('geometry-perimeter-triangle-missing-dimension','Find one missing triangle side from perimeter',
 'A triangle has perimeter 47 cm.\nTwo sides are 14 cm and 18 cm.\nFind the third side.','15 centimetres',
 'A triangle has perimeter forty-seven centimetres. Two sides measure fourteen and eighteen centimetres. Find the third side.',[
 ('THE TOTAL','Perimeter includes all three sides','14 + 18 + missing side = 47',
  'Perimeter is the total of all three sides. The two known sides and the missing one must add to forty-seven.'),
 ('ADD THE KNOWN SIDES','Find how much of the perimeter is already used','14 + 18 = 32 cm',
  'Fourteen plus eighteen equals thirty-two centimetres.'),
 ('SUBTRACT','Take the known total from the perimeter','47 − 32 = 15 cm',
  'Subtract thirty-two from forty-seven. The remaining side is fifteen centimetres.'),
 ('CHECK','All three sides should recover the perimeter','14 + 18 + 15 = 47 cm',
  'Check by adding all three sides. Fourteen plus eighteen plus fifteen is forty-seven, matching the perimeter.')],
 g(3,11,2,3),expression='47-(14+18)',value='15',equalities=[('14+18+15','47')]),

authored('geometry-perimeter-two-equal-missing-sides','Find two equal sides from a triangle’s perimeter',
 'A triangle has perimeter 62 m.\nOne side is 18 m; the other two sides are equal.\nFind each equal side.','22 metres each',
 'A triangle has perimeter sixty-two metres. One side is eighteen metres, and the other two sides are equal. Find each equal side.',[
 ('REMOVE THE KNOWN SIDE','Find the length left for both equal sides','62 − 18 = 44 m',
  'Subtract the known side from the perimeter. That leaves forty-four metres for both equal sides together.'),
 ('SHARE EQUALLY','The two remaining sides have the same length','44 ÷ 2 = 22 m',
  'Since the two sides are equal, divide forty-four by two. Each is twenty-two metres long.'),
 ('CHECK THE PERIMETER','Include the known side and both equal sides','18 + 22 + 22 = 62 m',
  'Add eighteen, twenty-two, and twenty-two. Their total is sixty-two metres.'),
 ('KEEP BOTH STEPS','Subtract first, then divide by two','Each equal side = (perimeter − known side) ÷ 2',
  'Subtract the known side first. The remainder belongs to two sides, so divide it by two to find just one of them.')],
 g(3,11,2,9),expression='(62-18)/2',value='22',equalities=[('18+22+22','62')]),

authored('geometry-parallelogram-base-from-area','Find a parallelogram base from its area',
 'A parallelogram has area 80 cm²\nand perpendicular height 8 cm. Find its base.',
 '10 centimetres',
 'A parallelogram has area eighty square centimetres and perpendicular height eight centimetres. Find its base.',[
 ('USE THE AREA FORMULA','Area equals base times perpendicular height','A = b × h',
  'For a parallelogram, area equals base times perpendicular height.'),
 ('SUBSTITUTE','The base is the missing factor','80 = b × 8',
  'Substitute eighty for area and eight for height. The base is the missing factor.'),
 ('DIVIDE','Divide area by height','b = 80 ÷ 8 = 10 cm',
  'Divide eighty by eight. The base is ten centimetres.'),
 ('CHECK','Base times height must give the original area','10 × 8 = 80 cm²',
  'Check by multiplying ten by eight. This gives the original area of eighty square centimetres. The base length uses centimetres.')],
 g(6,8,1,6),expression='80/8',value='10'),

authored('geometry-parallelogram-rearrangement','Explain parallelogram area by rearranging pieces',
 'A parallelogram has base 10 cm and height 4 cm.\nExplain why it has the same area as\na 10 cm by 4 cm rectangle.','Both areas are 40 square centimetres',
 'A parallelogram has base ten centimetres and perpendicular height four centimetres. Explain why it has the same area as a ten by four centimetre rectangle.',[
 ('CUT A TRIANGLE','Cut along a perpendicular height near one end','Separate the triangular end piece.',
  'Cut off the triangular piece near one end, following a perpendicular height.'),
 ('MOVE THE PIECE','Slide the triangle to the other end','Same pieces, with no gaps or overlaps.',
  'Slide that triangle to the other end. It fills the empty corner, without leaving a gap or overlapping the other piece.'),
 ('A RECTANGLE','The base and height stay the same','Rectangle area = 10 × 4 = 40 cm²',
  'The pieces now form a rectangle with the same base and height. Its area is ten times four, or forty square centimetres.'),
 ('AREA IS PRESERVED','Moving pieces does not change their total area','Parallelogram area = base × height = 40 cm²',
  'No area was added or removed, so the parallelogram has the same area. That is why base times perpendicular height works.')],
 g(6,8,1,9),expression='10*4',value='40'),
]

SPECS += [
authored('measurement-area-value-equal-price','Compare area when prices are equal',
 'Two garden plots cost the same amount.\nPlot A covers 600 m²; Plot B covers 850 m².\nBased on area alone, which gives more land for the money?',
 'Plot B; it gives 250 square metres more',
 'Two garden plots cost the same amount. Plot A covers six hundred square metres and plot B covers eight hundred fifty. Based on area alone, which gives more land for the money?',[
 ('SAME COST','Both plots have the same total price','Equal prices → compare the areas.',
  'Because both plots cost the same amount, compare how much land each price buys.'),
 ('COMPARE AREAS','Both areas use square metres','850 > 600',
  'Eight hundred fifty is greater than six hundred. Plot B gives more land.'),
 ('FIND THE DIFFERENCE','Subtract to find the extra area','850 − 600 = 250 m²',
  'Subtract six hundred from eight hundred fifty. Plot B provides two hundred fifty extra square metres.'),
 ('STATE THE COMPARISON','More area for the same total cost','Plot B gives more area for the money.',
  'Based on area alone, plot B gives more for the same price. If prices differ, comparing areas alone would not settle the question.')],
 g(3,10,4,9),expression='850-600',value='250'),

authored('geometry-volume-rectangular-prism-coordinates','Find prism volume from a given base area',
 'A rectangular prism has base area 28 cm²\nand height 6 cm. Find its volume.','168 cubic centimetres',
 'A rectangular prism has base area twenty-eight square centimetres and height six centimetres. Find its volume.',[
 ('RECOGNIZE THE GIVEN AREA','Length times width has already been calculated','Base area B = 28 cm²',
  'The base area is already given. It represents length times width, so you do not need separate base side lengths.'),
 ('USE BASE AREA TIMES HEIGHT','Extend the base through the prism’s height','V = B × h = 28 × 6',
  'Multiply the base area by the perpendicular height. Use twenty-eight times six.'),
 ('CALCULATE','Twenty-eight times six is one hundred sixty-eight','V = 168 cm³',
  'Twenty-eight times six equals one hundred sixty-eight cubic centimetres.'),
 ('CHECK THE UNITS','Square units times length units give cubic units','cm² × cm = cm³\nV = Bh',
  'Square centimetres times centimetres gives cubic centimetres. Whenever a prism’s base area is given, multiply it by the height.')],
 g(5,11,2,5),expression='28*6',value='168'),

authored('geometry-area-triangle-side-equation','Solve for a variable in a triangle’s base',
 'A triangle has base (x + 5) cm and height 8 cm.\nIts area is 52 cm². Find x.','x = 8',
 'A triangle has base x plus five centimetres and perpendicular height eight centimetres. Its area is fifty-two square centimetres. Find x.',[
 ('WRITE THE AREA EQUATION','Use half of base times height','(1/2) × (x + 5) × 8 = 52',
  'Write half of the base times the height equal to fifty-two.'),
 ('SIMPLIFY AND DIVIDE','Half of eight is four','4(x + 5) = 52\nx + 5 = 13',
  'Half of eight is four. Divide both sides by four to get x plus five equals thirteen.'),
 ('FIND THE VARIABLE','Subtract five from both sides','x = 13 − 5 = 8',
  'Subtract five from thirteen. The value of x is eight.'),
 ('CHECK THE ACTUAL BASE','The base is x plus five, not just x','Base = 8 + 5 = 13 cm\n(1/2) × 13 × 8 = 52 cm²',
  'The actual base is thirteen centimetres. Half of thirteen times eight gives fifty-two, so the area checks.')],
 g(6,8,2,9),equation=('(1/2)*(x+5)*8','52','x','8'),equalities=[('(1/2)*13*8','52')]),

authored('geometry-area-circle-coordinates','Find the area of a circular ring',
 'A ring has outer radius 11 cm and inner radius 5 cm.\nFind the outer circle area, inner circle area\nand ring area, in terms of pi.',
 'Outer: 121π cm²; inner: 25π cm²; ring: 96π cm²',
 'A ring has outer radius eleven centimetres and inner radius five centimetres. Find the outer circle area, inner circle area, and ring area, in terms of pi.',[
 ('OUTER CIRCLE','Use pi times the outer radius squared','Outer area = π × 11² = 121π cm²',
  'The outer circle has area pi times eleven squared, or one hundred twenty-one pi.'),
 ('INNER CIRCLE','Use pi times the inner radius squared','Inner area = π × 5² = 25π cm²',
  'The inner circle has area pi times five squared, or twenty-five pi.'),
 ('SUBTRACT THE HOLE','The inner circle is not part of the ring','Ring area = 121π − 25π = 96π cm²',
  'Subtract the inner circle from the outer circle. One hundred twenty-one pi minus twenty-five pi equals ninety-six pi.'),
 ('GENERAL RULE','Square the radii before subtracting','Ring area = π(R² − r²)\nR = outer radius; r = inner radius',
  'Square each radius first, then subtract the areas. Use pi times outer radius squared minus inner radius squared.')],
 g(7,9,3,10),expression='11**2-5**2',value='96',equalities=[('11**2','121'),('5**2','25')]),

authored('geometry-area-general-coordinates','Evaluate a composition of radius and area functions',
 'r(t) = t + 3 and A(r) = πr².\nFind A(r(4)).','49π',
 'The radius function is r of t equals t plus three, and the area function is A of r equals pi r squared. Find A of r of four.',[
 ('START INSIDE','Evaluate the inner function first','r(4) = 4 + 3 = 7',
  'Start with the inner function. Substitute four for t. The radius is four plus three, or seven.'),
 ('USE THAT OUTPUT','Seven becomes the input to the area function','A(r(4)) = A(7)',
  'Take that output, seven, and use it as the input to the area function.'),
 ('EVALUATE THE AREA','Substitute seven for the radius','A(7) = π × 7² = 49π',
  'Substitute seven for the radius. Pi times seven squared is forty-nine pi.'),
 ('FOLLOW THE ORDER','Input to radius, then radius to area','4 → 7 → 49π',
  'Follow the functions from the inside out: four becomes radius seven, then seven becomes area forty-nine pi.')],
 g(12,1,2,2),expression='(4+3)**2',value='49'),

authored('functions-compose-square-area','Write a composed area function',
 'A square’s side length is s(t) = 5t, with t > 0.\nIts area function is A(s) = s².\nWrite A(s(t)) in terms of t.','25t²',
 'A square’s side length is s of t equals five t, with t positive. Its area function is A of s equals s squared. Write the composed area function in terms of t.',[
 ('IDENTIFY THE INNER FUNCTION','The side expression is five t','s(t) = 5t',
  'The inner function gives the side length as five t.'),
 ('SUBSTITUTE THE ENTIRE EXPRESSION','Replace s in the area rule','A(s(t)) = (5t)²',
  'Replace s in the area rule with the whole expression five t. Put parentheses around it before squaring.'),
 ('SQUARE BOTH FACTORS','Five squared is twenty-five','(5t)² = 5² × t² = 25t²',
  'Square both factors. Five squared is twenty-five, so the composed function is twenty-five t squared.'),
 ('CHECK WITH A VALUE','At t = 2, the side is ten','s(2) = 10 → area = 100\n25 × 2² = 100',
  'Check with t equal to two. The side is ten and the area is one hundred. The composed formula gives the same result.')],
 g(12,1,'2Rev',2),identities=[('(5*t)**2','25*t**2')],equalities=[('(5*2)**2','25*2**2')]),
]


def diagram(spec,d,scene,p):
    vid=spec['video_id']
    if vid=='geometry-parallelogram-rearrangement' and scene in (1,2,3):
        x,y,s=660,420,50
        # Cut the left triangle and translate it exactly one base length to the right.
        d.polygon([(x+2*s,y+4*s),(x+10*s,y+4*s),(x+12*s,y),(x+2*s,y)],fill='#D0E8E2',outline=v.TEAL,width=4)
        dx=10*s if scene==3 else 0
        d.polygon([(x+dx,y+4*s),(x+dx+2*s,y+4*s),(x+dx+2*s,y)],fill='#F1DBB9',outline=v.TEAL,width=4)
        if scene==2:
            d.line((x+s,y-50,x+11*s,y-50),fill=v.TEAL,width=5)
            d.polygon([(x+11*s,y-50),(x+11*s-18,y-63),(x+11*s-18,y-37)],fill=v.TEAL)
        v.text(d,(x+(7 if scene==3 else 5)*s,y+4*s+45),'10 cm',38,v.INK,True,anchor='mm')
        d.line((x+12*s+40,y,x+12*s+40,y+4*s),fill=v.TEAL,width=3)
        v.text(d,(x+12*s+100,y+2*s),'4 cm',36,v.INK,True,anchor='mm')
        centered_math(d,805,spec['displays'][scene],43,v.TEAL)
        return
    if vid=='geometry-area-circle-coordinates' and scene in (1,2,3):
        cx,cy,scale=960,555,20;R=11*scale;r=5*scale
        d.ellipse((cx-R,cy-R,cx+R,cy+R),fill='#D0E8E2',outline=v.TEAL,width=4)
        if scene>=2:d.ellipse((cx-r,cy-r,cx+r,cy+r),fill=v.BG,outline=v.TEAL,width=4)
        d.line((cx,cy,cx+R,cy),fill=v.INK,width=3)
        v.text(d,(cx+R*0.72,cy+33),'11 cm',30,v.INK,True,anchor='mm')
        if scene>=2:
            d.line((cx,cy,cx,cy-r),fill=v.INK,width=3)
            v.text(d,(cx-44,cy-r/2),'5 cm',28,v.INK,True,anchor='mm')
        centered_math(d,825,spec['displays'][scene],44,v.TEAL)
        return
    draw_card(spec,d,scene,p)


def lessons(doc):
    assert 14+15>18 and 18+22>22 and 2*22>18
    batch=make_lessons(SPECS,doc)
    for spec in SPECS:v.DRAW[spec['video_id']]=lambda d,scene,p,s=spec:diagram(s,d,scene,p)
    return batch
