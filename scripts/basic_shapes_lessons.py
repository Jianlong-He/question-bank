"""Original direct area/perimeter examples with correctly scaled shape diagrams."""
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons, draw_card, centered_math
import generate_sample_videos as v

SPECS=[
authored('geometry-area-square','Area of a square',
 'A square has side length 9 cm. Find its area.','81 square centimetres',
 'A square has side length nine centimetres. Find its area.',[
 ('EQUAL SIDES','The length and width are both nine centimetres','Area = 9 × 9',
  'A square has equal sides, so its length and width are both nine centimetres.'),
 ('COUNT THE SQUARES','Nine rows, with nine unit squares in each row','9 × 9 = 81',
  'Nine rows of nine unit squares contain eighty-one squares.'),
 ('AREA UNITS','Each unit square covers one square centimetre','Area = 81 cm²',
  'The area is eighty-one square centimetres.'),
 ('GENERAL RULE','Multiply the side length by itself','A = s × s = s²',
  'For any square, multiply its side length by itself. This is s squared. Use square units for area.')],
 g(3,10,3,3),expression='9**2',value='81'),

authored('geometry-perimeter-square','Perimeter of a square',
 'A square has side length 2 cm. Find its perimeter.','8 centimetres',
 'A square has side length two centimetres. Find its perimeter.',[
 ('BOUNDARY','Perimeter is the distance around the outside','Four sides, each 2 cm long',
  'Perimeter measures the outside boundary. A square has four equal sides.'),
 ('ADD ALL SIDES','Walk around the whole boundary','2 + 2 + 2 + 2',
  'Add the length of all four sides: two plus two plus two plus two.'),
 ('MULTIPLY','Four equal sides means four times the side length','4 × 2 = 8 cm',
  'Four times two is eight centimetres. That is the perimeter.'),
 ('GENERAL RULE','The perimeter is four times the side length','P = 4s     so P/s = 4',
  'For side length s, the perimeter is four times s. For a positive side length, perimeter divided by side length is always four.')],
 g(3,11,1,3),expression='4*2',value='8'),

authored('geometry-perimeter-rectangle','Perimeter of a rectangle',
 'A rectangle is 9 m long and 6 m wide.\nFind its perimeter.','30 metres',
 'A rectangle is nine metres long and six metres wide. Find its perimeter.',[
 ('OPPOSITE SIDES','Both long sides are nine; both short sides are six','9 m, 6 m, 9 m, 6 m',
  'Opposite sides of a rectangle are equal. The four sides are nine, six, nine, and six metres.'),
 ('ADD ALL SIDES','Perimeter counts the outside boundary','9 + 6 + 9 + 6 = 30',
  'Add all four sides. Nine plus six plus nine plus six is thirty.'),
 ('SHORTER CALCULATION','Double one length plus one width','2 × (9 + 6) = 2 × 15 = 30 m',
  'You can also add one length and one width, then double the sum.'),
 ('GENERAL RULE','Use length units for a boundary','P = 2 × (length + width)',
  'The perimeter is thirty metres. In general, double the sum of length and width. Perimeter uses length units.')],
 g(3,11,1,2),expression='2*(9+6)',value='30'),

authored('geometry-perimeter-triangle','Perimeter of a triangle',
 'A triangle has sides 3 cm, 4 cm, and 5 cm.\nFind its perimeter.','12 centimetres',
 'A triangle has sides three, four, and five centimetres. Find its perimeter.',[
 ('THREE SIDES','Perimeter follows the entire outside boundary','P = 3 + 4 + 5',
  'A triangle has three sides. Add all three side lengths to find the distance around it.'),
 ('ADD','Combine the side lengths','3 + 4 + 5 = 12',
  'Three plus four is seven. Seven plus five is twelve.'),
 ('STATE THE PERIMETER','A boundary uses length units','Perimeter = 12 cm',
  'The perimeter is twelve centimetres.'),
 ('EQUAL-SIDE CASE','For an equilateral triangle, all three sides match','If each side is s: P = s + s + s = 3s\nThen P/s = 3',
  'If all three sides equal s, the perimeter is three times s. For positive s, the ratio of perimeter to side length is three.')],
 g(3,11,1,5),expression='3+4+5',value='12'),

authored('geometry-area-parallelogram','Area of a parallelogram',
 'A parallelogram has base 17 cm, perpendicular height 5 cm,\n and slanted side 13 cm. Find its area.','85 square centimetres',
 'A parallelogram has base seventeen centimetres, perpendicular height five centimetres, and slanted side thirteen centimetres. Find its area.',[
 ('CHOOSE THE HEIGHT','Use the perpendicular distance between parallel bases','Base: 17 cm     Height: 5 cm',
  'Use the perpendicular height of five centimetres. The slanted side is not the height.'),
 ('MULTIPLY','Parallelogram area is base times height','A = 17 × 5',
  'Multiply the base by the perpendicular height: seventeen times five.'),
 ('CALCULATE','Area uses square units','17 × 5 = 85 cm²',
  'The area is eighty-five square centimetres.'),
 ('WHY THIS WORKS','Rearranging a corner makes a rectangle','A = base × perpendicular height',
  'Cutting off a triangular corner and moving it makes a rectangle with the same base and height. Area stays the same.')],
 g(6,8,1,3),expression='17*5',value='85'),

authored('geometry-area-triangle','Area of a triangle',
 'A triangle has base 14 cm and perpendicular height 9 cm.\nFind its area.','63 square centimetres',
 'A triangle has base fourteen centimetres and perpendicular height nine centimetres. Find its area.',[
 ('BASE AND HEIGHT','Height meets the base at a right angle','Base: 14 cm     Height: 9 cm',
  'Use the given base and its perpendicular height.'),
 ('MULTIPLY FIRST','Base times height gives the matching parallelogram area','14 × 9 = 126 cm²',
  'Fourteen times nine is one hundred twenty-six square centimetres. That is the area of a parallelogram with this base and height.'),
 ('TAKE HALF','A triangle has half that area','A = 126 ÷ 2 = 63 cm²',
  'A triangle takes half that area. Divide by two to get sixty-three square centimetres.'),
 ('GENERAL RULE','Two copies form the matching parallelogram','Triangle: A = ½ × base × height\nMatching parallelogram: 2 × triangle area',
  'Use one half times base times perpendicular height. Two copies of the triangle form a parallelogram, so its area is twice the triangle area.')],
 g(6,8,2,1),expression='14*9/2',value='63'),

authored('geometry-area-trapezoid','Area of a trapezoid',
 'A trapezoid has parallel bases 9 cm and 17 cm,\nwith perpendicular height 7 cm. Find its area.','91 square centimetres',
 'A trapezoid has parallel bases nine and seventeen centimetres, with perpendicular height seven centimetres. Find its area.',[
 ('USE BOTH BASES','Add the parallel side lengths','9 + 17 = 26 cm',
  'Add the lengths of the two parallel bases: nine plus seventeen is twenty-six.'),
 ('AVERAGE THE BASES','Divide their sum by two','26 ÷ 2 = 13 cm',
  'Divide by two. The average base length is thirteen centimetres.'),
 ('MULTIPLY BY HEIGHT','Use the perpendicular height','A = 13 × 7 = 91 cm²',
  'Multiply thirteen by the perpendicular height of seven. The area is ninety-one square centimetres.'),
 ('TWO TRIANGLES','A diagonal splits the trapezoid into two triangles','½ × 9 × 7 + ½ × 17 × 7 = 91\nA = ½ × (base one + base two) × height',
  'A diagonal gives two triangles with these bases and the same height. Adding their areas produces the same formula.')],
 g(6,8,4,3),expression='(9+17)*7/2',value='91',equalities=[('9*7/2+17*7/2','91')]),

authored('geometry-area-circle','Area of a circle from radius or diameter',
 'A circle has diameter 34 cm.\nFind its exact area in terms of pi.','289π square centimetres',
 'A circle has diameter thirty-four centimetres. Find its exact area in terms of pi.',[
 ('FIND THE RADIUS','The radius is half the diameter','r = 34 ÷ 2 = 17 cm',
  'The radius is half the diameter. Thirty-four divided by two is seventeen centimetres.'),
 ('AREA FORMULA','Square the radius, then multiply by pi','A = πr² = π × 17²',
  'Use pi times radius squared. Substitute seventeen for the radius.'),
 ('CALCULATE EXACTLY','Keep pi in the answer','17² = 289\nA = 289π cm²',
  'Seventeen squared is two hundred eighty-nine, so the exact area is two hundred eighty-nine pi square centimetres.'),
 ('CHECK THE INPUT','The formula uses radius, not diameter','Given radius: use it directly.\nGiven diameter: divide by two first.',
  'If the radius is already given, use it directly. If the diameter is given, halve it first. Keep pi when an exact answer is requested.')],
 g(7,9,2,5),expression='(34/2)**2',value='289'),
]


def right_angle(d,x,y,size=16):
    d.line((x,y-size,x+size,y-size,x+size,y),fill=v.INK,width=3)


def diagram(spec,d,scene,p):
    vid=spec['video_id']
    if scene!=1:return draw_card(spec,d,scene,p)
    if vid in {'geometry-area-square','geometry-perimeter-square'}:
        x,y,s=780,385,38
        d.rectangle((x,y,x+9*s,y+9*s),fill='#D0E8E2',outline=v.TEAL,width=5)
        if vid=='geometry-area-square':
            for k in range(1,9):
                d.line((x+k*s,y,x+k*s,y+9*s),fill=v.TEAL,width=2)
                d.line((x,y+k*s,x+9*s,y+k*s),fill=v.TEAL,width=2)
        label='9 cm' if vid=='geometry-area-square' else '2 cm'
        v.text(d,(x+130,y+9*s+20),label,42,v.INK,True)
        v.text(d,(x+9*s+30,y+130),label,42,v.INK,True)
    elif vid=='geometry-perimeter-rectangle':
        x,y=665,405;w,h=9*60,6*60
        d.rectangle((x,y,x+w,y+h),fill='#D0E8E2',outline=v.TEAL,width=5)
        v.text(d,(x+210,y-55),'9 m',42,v.INK,True);v.text(d,(x+210,y+h+15),'9 m',42,v.INK,True)
        v.text(d,(x-100,y+140),'6 m',42,v.INK,True);v.text(d,(x+w+25,y+140),'6 m',42,v.INK,True)
    elif vid=='geometry-perimeter-triangle':
        d.polygon([(720,730),(1080,730),(720,460)],fill='#D0E8E2',outline=v.TEAL,width=5)
        v.text(d,(610,580),'3 cm',42,v.INK,True);v.text(d,(860,750),'4 cm',42,v.INK,True)
        v.text(d,(940,540),'5 cm',42,v.INK,True)
    elif vid=='geometry-area-parallelogram':
        x,y,s=520,700,30
        d.polygon([(x,y),(x+17*s,y),(x+29*s,y-5*s),(x+12*s,y-5*s)],fill='#D0E8E2',outline=v.TEAL,width=4)
        d.line((x+12*s,y,x+12*s,y-5*s),fill=v.INK,width=3);right_angle(d,x+12*s,y)
        v.text(d,(x+190,y+20),'17 cm',40,v.INK,True)
        v.text(d,(x+12*s+20,y-110),'5 cm',40,v.INK,True)
        v.text(d,(x+70,y-235),'13 cm slanted side',35,v.INK,True)
        d.line((x+180,y-185,x+180,y-80),fill=v.MUTED,width=2)
    elif vid=='geometry-area-triangle':
        x,y,s=620,760,40
        d.polygon([(x,y),(x+14*s,y),(x+4*s,y-9*s)],fill='#D0E8E2',outline=v.TEAL,width=5)
        d.line((x+4*s,y,x+4*s,y-9*s),fill=v.INK,width=3);right_angle(d,x+4*s,y)
        v.text(d,(x+4*s+25,y-200),'9 cm',42,v.INK,True)
        v.text(d,(x+230,y+18),'14 cm',42,v.INK,True)
    elif vid=='geometry-area-trapezoid':
        x,y,s=580,750,40
        d.polygon([(x,y),(x+17*s,y),(x+13*s,y-7*s),(x+4*s,y-7*s)],fill='#D0E8E2',outline=v.TEAL,width=5)
        d.line((x+4*s,y,x+4*s,y-7*s),fill=v.INK,width=3);right_angle(d,x+4*s,y)
        v.text(d,(x+6.5*s,y-7*s-55),'9 cm',42,v.INK,True)
        v.text(d,(x+6.5*s,y+15),'17 cm',42,v.INK,True)
        v.text(d,(x+4*s+25,y-160),'7 cm',42,v.INK,True)
    elif vid=='geometry-area-circle':
        x,y,r=940,585,190
        d.ellipse((x-r,y-r,x+r,y+r),fill='#D0E8E2',outline=v.TEAL,width=5)
        d.line((x-r,y,x+r,y),fill=v.INK,width=3)
        d.ellipse((x-5,y-5,x+5,y+5),fill=v.INK)
        v.text(d,(x-68,y+25),'34 cm',42,v.INK,True)
        v.text(d,(x+15,y-60),'17 cm',40,v.TEAL,True)
    else:return draw_card(spec,d,scene,p)
    for i,line in enumerate(spec['displays'][scene].split('\n')):centered_math(d,850+i*60,line,44,v.TEAL)


def lessons(doc):
    # Diagram proportions: 3-4-5 triangle and parallelogram slanted side 13.
    assert 3**2+4**2==5**2 and 12**2+5**2==13**2
    result=make_lessons(SPECS,doc)
    for spec in SPECS:v.DRAW[spec['video_id']]=lambda d,scene,p,s=spec:diagram(s,d,scene,p)
    return result
