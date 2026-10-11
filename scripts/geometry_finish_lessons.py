"""Original examples for geometric halves, pyramid sections/nets and line slopes."""
from math import isclose
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons,draw_card,centered_math
import generate_sample_videos as v

SPECS=[
authored('geometry-rectangle-halving-cuts','Compare two ways to cut a rectangle into halves',
 'Cut one rectangular card along a diagonal.\nCut another across the middle.\nWhich cuts make two equal halves?', 'Both cuts make two equal halves',
 'Cut one rectangular card along a diagonal. Cut another across the middle. Which cuts make two equal halves?',[
 ('WHAT IS A HALF?','Two halves must be equal parts of one whole','Same amount in each part',
  'Halves are two equal parts of one whole. Each part must contain the same amount of the card.'),
 ('DIAGONAL CUT','Join two opposite corners','Two matching triangles',
  'The diagonal cut makes two matching triangles. Turn one around, and it fits exactly over the other. They are equal halves.'),
 ('MIDDLE CUT','Join the midpoints of opposite sides','Two matching rectangles',
  'A straight cut across the middle makes two matching rectangles. These are equal halves too.'),
 ('BOTH WORK','The halves can have different shapes in different cuts','Diagonal or middle cut → two equal halves',
  'Both cuts work. The same two cuts also halve a square. Look for two equal parts, not just two pieces of any size.')],
 g(1,3,7,5),expression='1/2+1/2',value='1'),

authored('fractions-count-halves-in-wholes','Count halves in several whole shapes',
 'Three equal rectangular cards are each cut in half.\nHow many half-cards are there altogether?', '6 half-cards',
 'Three equal rectangular cards are each cut in half. How many half-cards are there altogether?',[
 ('ONE WHOLE','Each whole card makes two halves','1 card → 2 halves',
  'One whole card makes two equal halves.'),
 ('THREE WHOLES','Count two halves for each of the three cards','2 + 2 + 2',
  'There are three cards. Count two halves for the first, two for the second, and two for the third.'),
 ('ADD OR MULTIPLY','Three groups of two give six','3 × 2 = 6 halves',
  'Three groups of two make six. There are six half-cards altogether.'),
 ('CHECK','Pair the halves to rebuild the original cards','6 halves = 3 whole cards',
  'Pair the six halves to rebuild three whole cards. To count halves in whole shapes, multiply the number of wholes by two.')],
 g(3,5,4,5),expression='3*2',value='6',equalities=[('6/2','3')]),

authored('geometry-pyramid-parallel-section','Identify a pyramid section parallel to its base',
 'A square pyramid has base side 9 cm and height 12 cm.\nSlice parallel to its base, 4 cm above the base.\nName the section and find its side length.', 'A square with side 6 cm',
 'A square pyramid has base side nine centimetres and height twelve. Slice parallel to its base, four centimetres above the base. Name the section and find its side length.',[
 ('PARALLEL SECTION','A parallel slice has the same shape as the base','Square base → square section',
  'A slice parallel to a pyramid’s base, between the base and the apex, is a scaled copy of the base. Here the section is a square.'),
 ('HEIGHT FROM THE APEX','Compare distances measured from the apex','12 − 4 = 8 cm',
  'The slice lies eight centimetres below the apex. Measure both heights from the same apex.'),
 ('SCALE THE SIDE','Use the height ratio for corresponding lengths','Side = 9 × (8/12) = 6 cm',
  'The small pyramid’s height is eight twelfths of the full height. Multiply the base side nine by eight twelfths to get six.'),
 ('RESULT','Shape stays the same while size changes','Square section; side 6 cm',
  'The section is a square with side six centimetres. A different parallel slice changes the size but retains the square shape, except at the apex itself.')],
 g(10,10,'1Rev',2),expression='9*(12-4)/12',value='6'),

authored('geometry-square-pyramid-net-faces','Check the faces needed for a square-pyramid net',
 'A proposed net has one square and two triangles.\nDoes it have enough faces for a closed square pyramid?\nHow many triangular faces are missing?', 'No; two triangular faces are missing',
 'A proposed net has one square and two triangles. Does it have enough faces for a closed square pyramid? How many triangular faces are missing?',[
 ('BASE','The square base has four edges','1 square base; 4 base edges',
  'The square is the base. Count its four edges.'),
 ('SIDE FACES','Each base edge meets one triangular side face','4 triangular side faces are needed.',
  'Each base edge needs a triangle rising to the apex. A square pyramid therefore has four triangular side faces.'),
 ('COMPARE COUNTS','Subtract the number supplied from the number needed','4 − 2 = 2 triangles missing',
  'Only two triangles were supplied. Four minus two leaves two triangular faces missing, so the proposed net cannot close the pyramid.'),
 ('CHECK A COMPLETE NET','Correct counts are necessary; sizes and layout must also fit','1 square + 4 triangles = 5 faces',
  'A complete square-pyramid net has one square and four triangles. Their edge lengths and arrangement must also fit when folded; face counts alone do not guarantee a valid net.')],
 g(6,10,5,8),expression='4-2',value='2',equalities=[('1+4','5')]),

authored('geometry-square-inscribed-circle-radius','Find the radius of a circle inscribed in a square',
 'A circle is inscribed in a square of side 14 cm.\nFind the circle’s radius.', '7 centimetres',
 'A circle is inscribed in a square of side fourteen centimetres. Find the circle’s radius.',[
 ('INSCRIBED','The circle touches all four sides from inside','The circle fits exactly between opposite sides.',
  'Inscribed means the circle lies inside the square and touches all four sides.'),
 ('DIAMETER','Across the centre, the circle spans the square’s width','Diameter = 14 cm',
  'A diameter runs across the centre between opposite contact points. Its length equals the square’s side, fourteen centimetres.'),
 ('HALVE','The radius is half the diameter','Radius = 14 ÷ 2 = 7 cm',
  'Divide the diameter by two. The radius is seven centimetres.'),
 ('CHECK','Two radii span the square','2 × 7 = 14 cm',
  'Two seven-centimetre radii span the square’s width. Use half the side length, not half the diagonal.')],
 g(9,17,5,8),expression='14/2',value='7',equalities=[('2*7','14')]),

authored('linear-perpendicular-slope-product','Test perpendicular lines using their slopes',
 'Two lines have slopes 7/9 and −9/7.\nAre they perpendicular? Explain.', 'Yes; their slopes multiply to −1',
 'Two lines have slopes seven ninths and negative nine sevenths. Are they perpendicular?',[
 ('SLOPE TEST','For two nonvertical lines, multiply their slopes','Perpendicular exactly when m1 × m2 = −1',
  'For two nonvertical lines, the slopes multiply to negative one exactly when the lines are perpendicular.'),
 ('MULTIPLY','Multiply numerators and denominators','(7/9) × (−9/7) = −63/63',
  'Multiply seven by negative nine on top, and nine by seven underneath.'),
 ('SIMPLIFY','A product of negative one passes the test','−63/63 = −1 → perpendicular',
  'Negative sixty-three over sixty-three equals negative one. The lines are perpendicular, meeting at a right angle.'),
 ('NEGATIVE RECIPROCALS','Invert the nonzero slope and change its sign','7/9 → −9/7\nHorizontal and vertical lines are also perpendicular.',
  'These slopes are negative reciprocals. Invert a nonzero slope and change its sign. Handle horizontal and vertical lines separately: they are perpendicular, a horizontal slope is zero, and a vertical slope is undefined.')],
 g(9,18,3,10),expression='(7/9)*(-9/7)',value='-1'),

authored('linear-perpendicular-slope-from-equation','Find a perpendicular slope from a line equation',
 'Find the slope of a line perpendicular to\n4x + 7y = 21.', '7/4',
 'Find the slope of a line perpendicular to four x plus seven y equals twenty-one.',[
 ('ISOLATE THE Y TERM','Subtract four x from both sides','7y = −4x + 21',
  'First find the original line’s slope. Subtract four x from both sides.'),
 ('SLOPE-INTERCEPT FORM','Divide every term by seven','y = (−4/7)x + 3',
  'Divide every term by seven. The equation is y equals negative four sevenths x plus three.'),
 ('READ AND INVERT','The coefficient of x in y = mx + b is the slope','Original slope: −4/7\nPerpendicular slope: 7/4',
  'In y equals m x plus b, the coefficient of x is the slope. It is negative four sevenths. Invert it and change its sign to get seven quarters.'),
 ('CHECK','Nonvertical perpendicular slopes multiply to negative one','(−4/7) × (7/4) = −1',
  'Their product is negative one, confirming the result. If the original equation is already in slope-intercept form, read its x coefficient directly before taking the negative reciprocal.')],
 g(9,18,5,10),expression='(-4/7)*(7/4)',value='-1',identities=[('7*((-4/7)*x+3)','21-4*x')]),
]


def caption(d,s,scene,y=905):
    for i,line in enumerate(s['displays'][scene].split('\n')):centered_math(d,y+i*53,line,40,v.TEAL)


def diagram(s,d,scene,p):
    vid=s['video_id'];orange='#B66F4E';fill='#D0E8E2'
    if vid=='geometry-rectangle-halving-cuts' and scene in (0,1,2,3):
        for x in (440,1090):
            d.rectangle((x,455,x+390,715),fill=fill,outline=v.TEAL,width=5)
            if x==440:
                d.polygon([(x,455),(x+390,715),(x,715)],fill='#F1D8C9');d.line((x,455,x+390,715),fill=orange,width=5)
            else:
                d.rectangle((x,585,x+390,715),fill='#F1D8C9');d.line((x,585,x+390,585),fill=orange,width=5)
            d.rectangle((x,455,x+390,715),outline=v.TEAL,width=5)
        centered_math(d,800,'Diagonal cut                              Middle cut',40,v.INK)
        if scene:caption(d,s,scene)
    elif vid=='fractions-count-halves-in-wholes' and scene in (0,1,2,3):
        for i in range(3):
            x=370+i*420;d.rectangle((x,480,x+320,710),fill=fill,outline=v.TEAL,width=5);d.line((x+160,480,x+160,710),fill=orange,width=5)
            for j in range(2):v.text(d,(x+80+j*160,590),str(i*2+j+1) if scene==3 else '1/2',42,v.INK,True,anchor='mm')
        if scene:caption(d,s,scene)
    elif vid=='geometry-pyramid-parallel-section' and scene in (1,2,3):
        apex=(920,360);base=[(570,705),(1030,800),(1370,640),(910,545)]
        section=[(apex[0]+(x-apex[0])*2/3,apex[1]+(y-apex[1])*2/3) for x,y in base]
        d.polygon(base,outline=v.MUTED,width=3)
        for pt in base:d.line((*apex,*pt),fill=v.TEAL,width=4)
        d.polygon(section,fill=fill,outline=orange,width=5)
        v.text(d,(490,740),'base: 9 cm',30,v.INK,True)
        v.text(d,(1260,450),'parallel slice',30,v.INK,True)
        v.text(d,(1260,500),'4 cm above base',28,v.MUTED)
        v.text(d,(1260,550),'8 cm below apex',28,v.MUTED)
        caption(d,s,scene)
    elif vid=='geometry-square-pyramid-net-faces' and scene in (1,2,3,4):
        x,y,a,h=870,500,180,190
        d.rectangle((x,y,x+a,y+a),fill=fill,outline=v.TEAL,width=4)
        triangles=[[(x,y),(x+a,y),(x+a/2,y-h)],[(x+a,y),(x+a,y+a),(x+a+h,y+a/2)],[(x,y+a),(x+a,y+a),(x+a/2,y+a+h)],[(x,y),(x,y+a),(x-h,y+a/2)]]
        for i,pts in enumerate(triangles):
            d.polygon(pts,fill='#F1D8C9' if i<2 or scene==4 else None,outline=orange if i<2 or scene==4 else '#BDC8C1',width=4)
            cx=sum(p[0] for p in pts)/3;cy=sum(p[1] for p in pts)/3
            v.text(d,(cx,cy),str(i+1) if scene==4 else ('face' if i<2 else 'missing'),24,v.INK,True,anchor='mm')
        caption(d,s,scene,925)
    elif vid=='geometry-square-inscribed-circle-radius' and scene in (1,2,3):
        x,y,a=735,385,430;cx,cy=x+a/2,y+a/2
        d.rectangle((x,y,x+a,y+a),outline=v.INK,width=4);d.ellipse((x,y,x+a,y+a),fill=fill,outline=v.TEAL,width=5)
        d.line((x,cy,x+a,cy),fill=orange,width=4);d.ellipse((cx-5,cy-5,cx+5,cy+5),fill=v.INK)
        v.text(d,(cx,y-30),'14 cm',31,v.INK,True,anchor='mm')
        if scene==3:v.text(d,(cx+a/4,cy-30),'7 cm',34,v.INK,True,anchor='mm')
        caption(d,s,scene)
    else:draw_card(s,d,scene,p)


def lessons(doc):
    # Projection preserves parallel edges of the pyramid section; base is a parallelogram
    # in the oblique drawing. Its represented 3D section is a square scaled by 2/3.
    base=[(570,705),(1030,800),(1370,640),(910,545)]
    assert tuple(base[0][i]+base[2][i] for i in (0,1))==tuple(base[1][i]+base[3][i] for i in (0,1))
    assert isclose(9*8/12,6)
    batch=make_lessons(SPECS,doc)
    for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:diagram(s,d,scene,p)
    return batch
