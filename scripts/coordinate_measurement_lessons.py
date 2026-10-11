"""Coordinate grids and checked coordinate-derived lengths, areas and costs."""
from fractions import Fraction
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons,draw_card,math_runs,math_width
import generate_sample_videos as v

SPECS=[
authored('geometry-area-rectangle-coordinates','Find rectangle area from coordinates',
 'A rectangle has vertices (−4, −3), (5, −3),\n(5, 3) and (−4, 3). Find its area.',
 '54 square units',
 'A rectangle has opposite corners at negative four, negative three, and five, three, as shown by the listed vertices. Find its area.',[
 ('HORIZONTAL LENGTH','Subtract the left x-coordinate from the right','Width = 5 − (−4) = 9',
  'For the width, subtract the left x-coordinate from the right. Five minus negative four is nine units.'),
 ('VERTICAL LENGTH','Subtract the bottom y-coordinate from the top','Height = 3 − (−3) = 6',
  'For the height, subtract the bottom y-coordinate from the top. Three minus negative three is six units.'),
 ('MULTIPLY','Area is width times height','Area = 9 × 6 = 54 square units',
  'Multiply nine by six. The area is fifty-four square units.'),
 ('CHECK THE DISTANCES','Count intervals between coordinates','Coordinate difference → side length\nWidth × height → area',
  'Count the intervals between coordinates. Subtracting a negative adds its distance across zero. Multiply the two side lengths for area.')],
 g(6,9,2,6),expression='(5-(-4))*(3-(-3))',value='54'),

authored('geometry-perimeter-rectangle-coordinates','Find coordinate perimeter and fencing cost',
 'A garden has corners (−5, −2), (4, −2),\n(4, 5) and (−5, 5). Fence costs $2 per unit.\nFind its perimeter and the fencing cost.',
 'Perimeter: 32 units; cost: $64',
 'A rectangular garden has opposite corners at negative five, negative two, and four, five. Fence costs two dollars per unit. Find its perimeter and fencing cost.',[
 ('WIDTH','Find the horizontal coordinate difference','Width = 4 − (−5) = 9',
  'The width is four minus negative five, or nine units.'),
 ('HEIGHT','Find the vertical coordinate difference','Height = 5 − (−2) = 7',
  'The height is five minus negative two, or seven units.'),
 ('PERIMETER','Count two widths and two heights','P = 2 × (9 + 7) = 32 units',
  'The perimeter includes two widths and two heights. Twice the sum of nine and seven is thirty-two units.'),
 ('COST','Multiply the perimeter by the price per unit','Cost = 32 × $2 = $64',
  'For the fencing cost, multiply the perimeter by two dollars per unit. The total is sixty-four dollars.')],
 g(6,9,2,7),expression='2*((4-(-5))+(5-(-2)))',value='32',equalities=[('32*2','64')]),

authored('geometry-area-square-coordinates','Find square area from neighbouring coordinates',
 'Two neighbouring corners of a square are\nA(−4, 2) and B(3, 2). Find its area.',
 '49 square units',
 'Two neighbouring corners of a square are A at negative four, two, and B at three, two. Find the square’s area.',[
 ('SAME Y-COORDINATE','The known side is horizontal','A(−4, 2)     B(3, 2)',
  'Both points have y-coordinate two, so the side joining them is horizontal.'),
 ('FIND THE SIDE LENGTH','Subtract the x-coordinates','Side = 3 − (−4) = 7',
  'Subtract negative four from three. The side length is seven units.'),
 ('SQUARE THE LENGTH','A square has equal side lengths','Area = 7 × 7 = 49 square units',
  'A square has equal side lengths, so multiply seven by seven. Its area is forty-nine square units.'),
 ('CHECK THE GIVEN PAIR','Neighbouring corners define a side','Area = side²\nA diagonal needs a different calculation.',
  'Check that the given corners are neighbours. Their distance is a side length. Opposite corners would define a diagonal instead.')],
 g(6,9,'2Rev',5),expression='(3-(-4))**2',value='49'),

authored('geometry-area-parallelogram-coordinates','Find parallelogram area from coordinates',
 'A parallelogram has vertices (−4, −2), (3, −2),\n(6, 4) and (−1, 4). Find its area.',
 '42 square units',
 'The parallelogram has the four listed vertices. Its base runs horizontally from negative four to three, and its top is at y equals four. Find its area.',[
 ('BASE LENGTH','Use the horizontal bottom edge','Base = 3 − (−4) = 7',
  'The horizontal base runs from x equals negative four to x equals three, a length of seven units.'),
 ('PERPENDICULAR HEIGHT','Measure vertically between the parallel edges','Height = 4 − (−2) = 6',
  'The height is the vertical separation between y equals negative two and y equals four, which is six units.'),
 ('BASE TIMES HEIGHT','Multiply the two perpendicular measurements','Area = 7 × 6 = 42 square units',
  'Multiply the base, seven, by the perpendicular height, six. The area is forty-two square units.'),
 ('USE THE VERTICAL SEPARATION','A slanted side is not the height','Horizontal base → vertical height\nArea = base × perpendicular height',
  'The slanted side is not the height. With a horizontal base, use the vertical coordinate difference as the perpendicular height.')],
 g(6,9,3,7),expression='(3-(-4))*(4-(-2))',value='42'),

authored('geometry-area-triangle-coordinates','Find right-triangle area from coordinates',
 'A triangle has vertices (−2, −1), (5, −1)\nand (5, 5). Find its area.',
 '21 square units',
 'A triangle has vertices at negative two, negative one; five, negative one; and five, five. Find its area.',[
 ('HORIZONTAL BASE','The bottom two points share a y-coordinate','Base = 5 − (−2) = 7',
  'The horizontal base runs from negative two to five, so its length is seven units.'),
 ('VERTICAL HEIGHT','The right-hand points share an x-coordinate','Height = 5 − (−1) = 6',
  'The vertical side rises from negative one to five. Its length is six units, perpendicular to the base.'),
 ('TAKE HALF','Triangle area is half of base times height','Area = (1/2) × 7 × 6 = 21',
  'Take half of seven times six. Half of forty-two is twenty-one square units.'),
 ('PICTURE THE MATCHING RECTANGLE','The triangle covers half a seven-by-six rectangle','Rectangle: 42 square units\nTriangle: 21 square units',
  'A matching seven-by-six rectangle has area forty-two. This right triangle covers exactly half of it, confirming twenty-one.')],
 g(6,9,2,9),expression='(1/2)*(5-(-2))*(5-(-1))',value='21'),

authored('geometry-rectangle-missing-side-coordinate-area','Find a missing rectangle side using coordinates and area',
 'One side of a rectangle joins (−5, 1) and (2, 1).\nThe rectangle has area 56 square units.\nFind the length of the other side.',
 '8 units',
 'One side of a rectangle joins negative five, one, and two, one. Its area is fifty-six square units. Find the other side length.',[
 ('KNOWN SIDE','Use the horizontal coordinate difference','Known side = 2 − (−5) = 7',
  'The two points share a y-coordinate, so subtract their x-coordinates. The known side is seven units.'),
 ('USE THE AREA','The two side lengths multiply to fifty-six','7 × missing side = 56',
  'The area is fifty-six, so seven times the missing side must equal fifty-six.'),
 ('DIVIDE','Divide area by the known side','Missing side = 56 ÷ 7 = 8 units',
  'Divide fifty-six by seven. The other side is eight units long.'),
 ('CHECK AND GENERALIZE','Use y-coordinate differences for a vertical side','7 × 8 = 56 square units\nMissing side = area ÷ known side',
  'Seven times eight recovers the given area. If the known side is vertical, use its y-coordinate difference before dividing the area.')],
 g(6,9,3,9),expression='56/(2-(-5))',value='8'),
]

GRIDS={
 'geometry-area-rectangle-coordinates':([(-4,-3),(5,-3),(5,3),(-4,3)],54),
 'geometry-perimeter-rectangle-coordinates':([(-5,-2),(4,-2),(4,5),(-5,5)],63),
 'geometry-area-square-coordinates':([(-4,2),(3,2),(3,9),(-4,9)],49),
 'geometry-area-parallelogram-coordinates':([(-4,-2),(3,-2),(6,4),(-1,4)],42),
 'geometry-area-triangle-coordinates':([(-2,-1),(5,-1),(5,5)],21),
 'geometry-rectangle-missing-side-coordinate-area':([(-5,1),(2,1)],None),
}


def right_math(d,y,line,size=42):
    while math_width(d,line,size)>720 and size>26:size-=1
    x=1420-math_width(d,line,size)/2
    for part,font,raised in math_runs(line,size):
        d.text((x,y+size*(.42 if raised else .9)),part,font=font,fill=v.TEAL,anchor='ls')
        x+=d.textlength(part,font=font)


def diagram(spec,d,scene,p):
    vid=spec['video_id']
    if scene not in (1,2) or (vid=='geometry-rectangle-missing-side-coordinate-area' and scene!=1):
        draw_card(spec,d,scene,p);return
    pts,_=GRIDS[vid]
    xmin=min(0,min(x for x,y in pts))-2;xmax=max(0,max(x for x,y in pts))+2
    ymin=min(0,min(y for x,y in pts))-2;ymax=max(0,max(y for x,y in pts))+2
    scale=min(610/(xmax-xmin),405/(ymax-ymin))
    left=560-scale*(xmax-xmin)/2;top=385
    def xy(x,y):return left+(x-xmin)*scale,top+(ymax-y)*scale
    for x in range(xmin,xmax+1):d.line((*xy(x,ymin),*xy(x,ymax)),fill='#D9DEDB',width=1)
    for y in range(ymin,ymax+1):d.line((*xy(xmin,y),*xy(xmax,y)),fill='#D9DEDB',width=1)
    for ends in [(xy(xmin,0),xy(xmax,0)),(xy(0,ymin),xy(0,ymax))]:d.line((*ends[0],*ends[1]),fill=v.MUTED,width=2)
    v.text(d,xy(xmax,0),'x',24,v.INK,True,anchor='ls');v.text(d,xy(0,ymax),'y',24,v.INK,True,anchor='lb')
    pixels=[xy(x,y) for x,y in pts]
    if len(pts)>2:d.polygon(pixels,fill='#D0E8E2',outline=v.TEAL,width=4)
    else:d.line((*pixels[0],*pixels[1]),fill=v.TEAL,width=5)
    # Redraw axes above the fill, so negative-coordinate distances remain visible.
    for ends in [(xy(xmin,0),xy(xmax,0)),(xy(0,ymin),xy(0,ymax))]:d.line((*ends[0],*ends[1]),fill='#A8B7B1',width=2)
    for x in range(xmin+1,xmax):
        px,py=xy(x,0);d.line((px,py-4,px,py+4),fill=v.MUTED,width=2)
        if x%2==0:v.text(d,(px,py+11),str(x),20,v.MUTED,anchor='mt')
    for y in range(ymin+1,ymax):
        px,py=xy(0,y);d.line((px-4,py,px+4,py),fill=v.MUTED,width=2)
        if y%2==0 and y!=0:v.text(d,(px-9,py),str(y),20,v.MUTED,anchor='rm')
    for i,((x,y),(px,py)) in enumerate(zip(pts,pixels)):
        d.ellipse((px-5,py-5,px+5,py+5),fill=v.INK)
        if vid=='geometry-area-square-coordinates' and i>=2:continue
        # Place vertex labels beyond the shape's top/bottom, away from axis tick labels.
        bottom=y==min(q[1] for q in pts)
        label=f'({x}, {y})'
        v.text(d,(px,py+(27 if bottom else -25)),label,27,v.INK,True,anchor='mm')
    if vid=='geometry-area-parallelogram-coordinates' and scene==2:
        a,b=xy(3,-2),xy(3,4);d.line((*a,*b),fill='#BB795B',width=4)
    for i,line in enumerate(spec['displays'][scene].split('\n')):right_math(d,490+i*85,line)
    if vid.endswith('square-coordinates'):right_math(d,650,'A square extends above this side.',30)
    return


def lessons(doc):
    for pts,expected in GRIDS.values():
        if expected is not None:
            area=abs(sum(x*pts[(i+1)%len(pts)][1]-y*pts[(i+1)%len(pts)][0] for i,(x,y) in enumerate(pts)))/2
            assert area==expected,(pts,area,expected)
    batch=make_lessons(SPECS,doc)
    for spec in SPECS:v.DRAW[spec['video_id']]=lambda d,scene,p,s=spec:diagram(s,d,scene,p)
    return batch
