"""Quadrilateral recognition, shape families, trapezoids and the golden ratio."""
from math import sqrt,isclose,hypot
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons,draw_card,centered_math
import generate_sample_videos as v

SPECS=[
authored('geometry-quadrilaterals','Recognize a quadrilateral by counting straight sides',
 'Which drawn shape is a quadrilateral: A, B, or C?', 'Shape B; it has four straight sides',
 'Look at shapes A, B, and C. Which one is a quadrilateral?',[
 ('COUNT A','Follow the straight sides all the way around','Shape A: 3 sides',
  'Follow shape A around its edge. It has three straight sides. This is a triangle.'),
 ('COUNT B','Count every straight side once','Shape B: 4 sides',
  'Shape B has one, two, three, four straight sides. A closed shape with four straight sides is a quadrilateral.'),
 ('COUNT C','Check the whole boundary','Shape C: 6 sides',
  'Shape C has six straight sides. It is a hexagon, so it is not a quadrilateral.'),
 ('CHOOSE','Four straight sides make a quadrilateral','B is the quadrilateral.',
  'Choose B. Squares, rectangles, rhombuses, and trapezoids all have four straight sides. Their side lengths and angles can differ, but each is a quadrilateral.')],
 g(1,3,6,5),expression='1+1+1+1',value='4'),

authored('geometry-quadrilateral-parallel-families','Classify quadrilaterals using parallel sides and right angles',
 'Shape P has two pairs of parallel opposite sides\nand no right angles. Shape R has four right angles\nand sides 5, 9, 5, 9 cm. Classify each.',
 'P is a parallelogram; R is a rectangle and parallelogram, but not a square',
 'Shape P has two pairs of parallel opposite sides and no right angles. Shape R has four right angles and sides five, nine, five, nine centimetres. Classify each.',[
 ('PARALLEL SIDES','Two pairs of parallel opposite sides make a parallelogram','P: parallelogram; not a rectangle',
  'Two pairs of parallel opposite sides make P a parallelogram. With no right angles, it is not a rectangle.'),
 ('RIGHT ANGLES','A rectangle has four right angles','R: rectangle AND parallelogram',
  'R has four right angles, so it is a rectangle. Every rectangle also has two pairs of parallel sides, making it a parallelogram.'),
 ('EQUAL SIDES','A square needs four equal sides as well as right angles','5 ≠ 9, so R is not a square.',
  'R has unequal adjacent sides, so it is not a square. Opposite sides of any rectangle are equal.'),
 ('SHAPE FAMILIES','One shape can satisfy several definitions','Rhombus: four equal sides; also a parallelogram\nSquare: rhombus AND rectangle',
  'A rhombus has four equal sides and is also a parallelogram. A square is both a rhombus and a rectangle. Every one of these is a quadrilateral.')],
 g(3,9,1,4),expression='5+9+5+9',value='28'),

authored('geometry-quadrilateral-trapezoid-legs','Distinguish trapezoids by their nonparallel sides',
 'Two quadrilaterals each have exactly one pair\nof parallel sides. In T, the other two sides are equal.\nIn U, they are unequal. Classify T and U.',
 'T is an isosceles trapezoid; U is a non-isosceles trapezoid',
 'Two quadrilaterals each have exactly one pair of parallel sides. In T, the other two sides are equal. In U, they are unequal. Classify them.',[
 ('PARALLEL PAIR','The parallel sides are called bases','T and U are both trapezoids.',
  'Both have exactly one pair of parallel sides, so both are trapezoids. The parallel sides are called bases.'),
 ('EQUAL LEGS','The nonparallel sides are called legs','T: equal legs → isosceles trapezoid',
  'The two nonparallel sides are the legs. T has equal legs, making it an isosceles trapezoid.'),
 ('UNEQUAL LEGS','Unequal legs do not satisfy the isosceles condition','U: unequal legs → not isosceles',
  'U has unequal legs. It is a trapezoid, but it is not isosceles.'),
 ('CHECK BOTH FEATURES','First parallel sides, then leg lengths','Exactly one parallel pair; then compare the legs.',
  'Check the parallel sides first, then compare the legs. Some courses allow trapezoids to have at least one parallel pair. These two examples have exactly one, so they qualify under either definition.')],
 g(5,16,3,2),expression='1+1',value='2'),

authored('geometry-golden-rectangle-longer-side','Find the longer side of a golden rectangle',
 'A golden rectangle has shorter side 7 cm.\nFind the longer side to the nearest hundredth.',
 '11.33 centimetres',
 'A golden rectangle has shorter side seven centimetres. Find the longer side to the nearest hundredth.',[
 ('GOLDEN RATIO','Longer side divided by shorter side equals phi','φ = (1 + √5)/2 ≈ 1.618033989',
  'For a golden rectangle, the longer side divided by the shorter side equals phi, the golden ratio, about one point six one eight.'),
 ('REARRANGE','Multiply the shorter side by phi','Longer side = 7φ',
  'Multiply the shorter side by phi. Keep the full calculator value until the last step.'),
 ('CALCULATE','Use the full ratio before rounding','7 × (1 + √5)/2 ≈ 11.32623792 cm',
  'Seven times phi is about eleven point three two six two centimetres.'),
 ('ROUND','The thousandths digit is six, so round up','Longer side ≈ 11.33 cm',
  'To round to the nearest hundredth, look at the thousandths digit, six. Round up to eleven point three three centimetres. The longer-to-shorter ratio is still approximately phi.')],
 g(10,8,4,3),expression='1133/100',value='11.33'),
]


def polygon(d,pts,title):
    d.polygon(pts,fill='#D0E8E2',outline=v.TEAL,width=5)
    v.text(d,(sum(x for x,y in pts)/len(pts),max(y for x,y in pts)+42),title,35,v.INK,True,anchor='mm')


def diagram(s,d,scene,p):
    vid=s['video_id']
    if vid=='geometry-quadrilaterals':
        shapes=[[(330,740),(620,740),(475,445)],[(800,740),(1120,740),(1060,510),(865,510)],[(1370,495),(1510,495),(1590,620),(1510,745),(1370,745),(1290,620)]]
        for name,pts in zip('ABC',shapes):polygon(d,pts,name)
        if scene>0:
            centered_math(d,875,s['displays'][scene],48,v.TEAL)
            active=scene-1 if scene in (1,2,3) else 1
            pts=shapes[active]
            for i in range(len(pts)):
                a,b=pts[i],pts[(i+1)%len(pts)];x,y=(a[0]+b[0])/2,(a[1]+b[1])/2
                d.ellipse((x-20,y-20,x+20,y+20),fill=v.TEAL);v.text(d,(x,y),str(i+1),26,'white',True,anchor='mm')
    elif vid=='geometry-quadrilateral-parallel-families' and scene in (0,1,2,3):
        polygon(d,[(370,710),(770,710),(885,500),(485,500)],'P')
        polygon(d,[(1120,710),(1498,710),(1498,500),(1120,500)],'R')
        for x,y,dx,dy in [(1120,710,1,-1),(1498,710,-1,-1),(1498,500,-1,1),(1120,500,1,1)]:
            d.line((x+15*dx,y,x+15*dx,y+15*dy,x,y+15*dy),fill=v.INK,width=3)
        v.text(d,(1309,465),'9 cm',29,v.INK,True,anchor='mm');v.text(d,(1546,605),'5 cm',29,v.INK,True,anchor='mm')
        if scene==0:
            centered_math(d,850,'P: two parallel pairs; no right angles',39,v.INK)
            centered_math(d,910,'R: four right angles; sides 5 and 9 cm',39,v.TEAL)
        else:centered_math(d,885,s['displays'][scene],43,v.TEAL)
    elif vid=='geometry-quadrilateral-trapezoid-legs' and scene in (0,1,2,3):
        t=[(380,735),(820,735),(730,495),(470,495)];u=[(1090,735),(1530,735),(1490,495),(1180,495)]
        for pts,name in [(t,'T'),(u,'U')]:
            polygon(d,pts,name)
            for a,b in [(pts[0],pts[3]),(pts[1],pts[2])]:
                d.line((*a,*b),fill='#B66F4E',width=6)
        for x in (425,775):d.line((x-12,615,x+12,615),fill=v.INK,width=4)
        if scene==0:
            centered_math(d,860,'Both: exactly one pair of parallel sides',39,v.INK)
            centered_math(d,918,'T: equal legs; U: unequal legs',42,v.TEAL)
        else:centered_math(d,888,s['displays'][scene],43,v.TEAL)
    else:draw_card(s,d,scene,p)


def lessons(doc):
    phi=(1+sqrt(5))/2;assert round(7*phi,2)==11.33 and isclose(phi**2,phi+1)
    assert isclose(hypot(90,240),hypot(-90,240)) and not isclose(hypot(90,240),hypot(-40,240))
    batch=make_lessons(SPECS,doc)
    for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:diagram(s,d,scene,p)
    return batch
