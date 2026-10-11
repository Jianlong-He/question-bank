"""Reflections using coordinate rules, fixed points and composition."""
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons,draw_card,centered_math
import generate_sample_videos as v

SPECS=[
authored('geometry-reflection-coordinate-axes','Reflect a point across either coordinate axis',
 'Reflect P(−6, 8) across the x-axis.\nSeparately, reflect the original P across the y-axis.',
 'Across x-axis: (−6, −8); across y-axis: (6, 8)',
 'Reflect negative six, eight across the x-axis. Separately, reflect the original point across the y-axis.',[
 ('X-AXIS','Keep x and change the sign of y','(x, y) → (x, −y)\n(−6, 8) → (−6, −8)',
  'Across the x-axis, keep the horizontal coordinate and reverse the vertical coordinate. The image is negative six, negative eight.'),
 ('Y-AXIS','Keep y and change the sign of x','(x, y) → (−x, y)\n(−6, 8) → (6, 8)',
  'Return to the original point. Across the y-axis, reverse the horizontal coordinate. This image is six, eight.'),
 ('DISTANCE CHECK','The mirror axis is halfway between point and image','Same perpendicular distance on opposite sides',
  'Each point and image are the same perpendicular distance from the mirror axis, on opposite sides.'),
 ('RECOGNIZE THE RULE','Identify the reflected axis from the changed coordinate','Only y changes sign → x-axis\nOnly x changes sign → y-axis',
  'You can also identify the axis from a point and its image. A change in the y sign indicates the x-axis; a change in the x sign indicates the y-axis.')],
 g(6,9,1,7),expression='-8',value='-8',equalities=[('-(-6)','6')]),

authored('geometry-reflection-vertical-line','Reflect a point across a vertical line',
 'Reflect P(11, −4) across the line x = 3.\nFind the image coordinates.',
 '(−5, −4)',
 'Reflect eleven, negative four across the vertical line x equals three. Find the image coordinates.',[
 ('DISTANCE','Measure horizontally to the mirror line','11 − 3 = 8 units',
  'The original point is eight units to the right of the mirror line.'),
 ('OPPOSITE SIDE','Move the same distance to the left','x′ = 3 − 8 = −5',
  'Move eight units to the left of three. The new x-coordinate is negative five.'),
 ('KEEP Y','A vertical mirror keeps the same height','P′ = (−5, −4)',
  'The y-coordinate stays negative four because the mirror is vertical. The image is negative five, negative four.'),
 ('CHECK THE MIDPOINT','The original and image average to the mirror coordinate','(11 + (−5)) ÷ 2 = 3\nGeneral rule: x′ = 2a − x for x = a',
  'The two x-coordinates average to three, the mirror coordinate. In general, reflecting across x equals a gives new x equal to two a minus x.')],
 g(8,6,3,10),expression='2*3-11',value='-5',equalities=[('(11-5)/2','3')]),

authored('geometry-reflection-diagonal-line','Reflect a point across y equals x',
 'Reflect P(−7, 4) across the line y = x.\nFind the image coordinates.',
 '(4, −7)',
 'Reflect negative seven, four across the line y equals x. Find the image coordinates.',[
 ('RULE','Swap the two coordinates','(x, y) → (y, x)',
  'Reflection across y equals x swaps the horizontal and vertical coordinates.'),
 ('APPLY','Move each number with its sign','(−7, 4) → (4, −7)',
  'Move four into the x-position and negative seven into the y-position. Keep each number with its sign.'),
 ('GEOMETRIC CHECK','The midpoint lies on the mirror line','Midpoint = (−1.5, −1.5)',
  'The midpoint is negative one point five in both coordinates, so it lies on y equals x. The joining segment has slope negative one, perpendicular to the mirror.'),
 ('REFLECT AGAIN','Swapping twice returns to the starting point','(4, −7) → (−7, 4)',
  'Swap the coordinates again to recover the original point. The reflected image is four, negative seven.')],
 g(8,6,7,6),expression='(-7+4)/2',value='-1.5',equalities=[('(-7-4)/(4-(-7))','-1')]),

authored('geometry-reflection-fixed-points','Find points that stay fixed under reflection',
 'Which points stay fixed when reflected across y = x?\nA(−7, −7), B(4, −7), C(6, 6)',
 'A and C',
 'Which points stay fixed when reflected across y equals x? A is negative seven, negative seven; B is four, negative seven; C is six, six.',[
 ('FIXED POINTS','A point on the mirror line maps to itself','On y = x, the two coordinates are equal.',
  'Points on the mirror line stay fixed because their perpendicular distance from the line is zero.'),
 ('CHECK A AND C','Their coordinates satisfy y equals x','A: −7 = −7; C: 6 = 6',
  'A and C each have equal coordinates, so they are on the line and remain in place.'),
 ('CHECK B','Swapping unequal coordinates changes the point','B(4, −7) → B′(−7, 4)',
  'B has unequal coordinates. Swapping them gives negative seven, four, which is a different point.'),
 ('CONCLUDE','The fixed points are exactly the points on the mirror','A and C stay fixed.',
  'A and C stay fixed. For any reflection line, points on that line map to themselves; points off it move to the other side.')],
 g(8,6,8,6),expression='-7-(-7)',value='0',equalities=[('6-6','0')]),

authored('geometry-reflection-rigid-properties','Use the measurements preserved by reflection',
 'A triangle has perimeter 29 cm and an angle of 73°.\nIt is reflected. Find the image perimeter and angle.\nAre the two triangles congruent?',
 '29 cm; 73 degrees; yes, congruent',
 'A triangle has perimeter twenty-nine centimetres and an angle of seventy-three degrees. It is reflected. Find those image measurements and decide if the triangles are congruent.',[
 ('LENGTHS','Reflection is a rigid transformation','Corresponding side lengths stay equal.',
  'Reflection preserves distances. Every side in the image has the same length as its corresponding original side.'),
 ('PERIMETER','Equal side lengths give the same total','Image perimeter = 29 cm',
  'Because all the side lengths are unchanged, the perimeter is still twenty-nine centimetres.'),
 ('ANGLES','Angle measures are preserved too','Image angle = 73°',
  'The image angle is still seventy-three degrees. In particular, perpendicular lines remain perpendicular.'),
 ('CONGRUENCE','Same size and shape, even after a sequence of rigid moves','Original and image are congruent.',
  'The triangles have the same size and shape, so they are congruent. Rotations also preserve these measurements, so a sequence of rotations and reflections still gives a congruent image.')],
 g(8,6,1,6),expression='29',value='29',equalities=[('73','73')]),

authored('geometry-reflection-parallel-composition','Combine reflections across parallel lines',
 'Reflect P(−3, 2) across x = −1, then across x = 4.\nFind the final image and the equivalent translation.',
 '(7, 2); translate 10 units right',
 'Reflect negative three, two across x equals negative one, then across x equals four. Find the final image and equivalent translation.',[
 ('FIRST REFLECTION','Use the first mirror line','First x = 2(−1) − (−3) = 1; y = 2',
  'The first reflection sends the x-coordinate to one. The y-coordinate stays two.'),
 ('SECOND REFLECTION','Reflect the first image across the second line','Final x = 2(4) − 1 = 7; y = 2',
  'Reflect this new point across x equals four. The result is seven, two.'),
 ('NET MOVEMENT','Compare the final image with the original','7 − (−3) = 10 → translate 10 units right',
  'The total change is ten units right, with no vertical change. This is a translation.'),
 ('GENERAL RULE','The movement is twice the distance between the lines','Line spacing: 4 − (−1) = 5\nTranslation distance: 2 × 5 = 10',
  'Two reflections across distinct parallel lines give a translation twice their spacing, perpendicular to the lines. Reversing their order reverses its direction.')],
 g(9,16,2,6),expression='2*4-(2*(-1)-(-3))',value='7',equalities=[('7-(-3)','10'),('2*(4-(-1))','10')]),

authored('geometry-reflection-intersecting-composition','Combine reflections across intersecting lines',
 'Two mirror lines meet at O. The second lies 30°\ncounterclockwise from the first. Reflect across the\nfirst, then the second. Describe the combined move.',
 'A 60-degree counterclockwise rotation about O',
 'Two mirror lines meet at O. The second is thirty degrees counterclockwise from the first. Reflect across the first, then the second. Describe the combined move.',[
 ('TRACK A DIRECTION','Use the first mirror as the zero-degree reference','Example ray: 15° → −15° after the first reflection',
  'Track a ray fifteen degrees from the first mirror. Reflecting across that mirror changes its direction to negative fifteen degrees.'),
 ('SECOND MIRROR','Mirror the angle about thirty degrees','New direction = 2(30°) − (−15°) = 75°',
  'Reflect across the second mirror at thirty degrees. Twice thirty minus negative fifteen gives seventy-five degrees.'),
 ('NET TURN','Compare the final and initial directions','75° − 15° = 60° counterclockwise',
  'The direction has turned sixty degrees counterclockwise. Distance from O stays the same, so the move is a rotation about O.'),
 ('GENERAL RULE','Double the directed angle from first mirror to second','Rotation angle = 2θ; center = intersection',
  'The rotation angle is twice the directed angle from the first mirror to the second. Reversing the order reverses the turn.')],
 g(9,16,2,7),expression='2*30-(-15)-15',value='60',identities=[('2*b-(2*a-t)-t','2*(b-a)')]),
]


def axes(d,limit=10):
    cx,cy,scale=955,600,24
    def xy(x,y):return cx+scale*x,cy-scale*y
    for a in range(-limit,limit+1,2):
        d.line([xy(a,-limit),xy(a,limit)],fill='#E2E8E5',width=1)
        d.line([xy(-limit,a),xy(limit,a)],fill='#E2E8E5',width=1)
    d.line([xy(-limit,0),xy(limit,0)],fill=v.INK,width=2)
    d.line([xy(0,-limit),xy(0,limit)],fill=v.INK,width=2)
    v.text(d,xy(limit+.5,0),'x',25,v.INK,True);v.text(d,xy(.4,limit+.5),'y',25,v.INK,True)
    return xy


def point(d,xy,x,y,label,offset=(12,10)):
    X,Y=xy(x,y);d.ellipse((X-7,Y-7,X+7,Y+7),fill=v.TEAL)
    v.text(d,(X+offset[0],Y+offset[1]),label,29,v.TEAL,True)


def diagram(spec,d,scene,p):
    vid=spec['video_id']
    if vid=='geometry-reflection-coordinate-axes' and scene in (1,2):
        xy=axes(d)
        target=(-6,-8) if scene==1 else (6,8)
        a,b=((-10,0),(10,0)) if scene==1 else ((0,-10),(0,10))
        d.line([xy(*a),xy(*b)],fill='#B66F4E',width=5)
        d.line([xy(-6,8),xy(*target)],fill='#A8BEB9',width=4)
        point(d,xy,-6,8,'P(−6, 8)',(-180,-20))
        point(d,xy,*target,'P′'+ ('(−6, −8)' if scene==1 else '(6, 8)'),(12,-15))
        centered_math(d,890,spec['displays'][scene].split('\n')[0],43,v.TEAL)
    elif vid=='geometry-reflection-vertical-line' and scene in (1,2,3):
        xy=lambda x,y:(730+x*35,540-y*20)
        d.line([xy(3,-10),xy(3,7)],fill='#B66F4E',width=5)
        v.text(d,xy(3.4,7),'x = 3',31,'#B66F4E',True)
        d.line([xy(-5,-4),xy(11,-4)],fill='#A8BEB9',width=4)
        point(d,xy,11,-4,'P(11, −4)',(15,-12));point(d,xy,-5,-4,'P′(−5, −4)',(-160,-12))
        v.text(d,xy(-1,0),'8 units',31,v.INK,True);v.text(d,xy(6,0),'8 units',31,v.INK,True)
        centered_math(d,840,spec['displays'][scene],44,v.TEAL)
    elif vid=='geometry-reflection-diagonal-line' and scene in (1,3):
        xy=axes(d,9)
        d.line([xy(-9,-9),xy(9,9)],fill='#B66F4E',width=4)
        v.text(d,xy(9,9),'y = x',29,'#B66F4E',True)
        d.line([xy(-7,4),xy(4,-7)],fill='#A8BEB9',width=3)
        point(d,xy,-7,4,'P(−7, 4)',(-170,-10));point(d,xy,4,-7,'P′(4, −7)')
        if scene==3:point(d,xy,-1.5,-1.5,'M(−1.5, −1.5)',(-240,25))
        centered_math(d,890,spec['displays'][scene],43,v.TEAL)
    else:draw_card(spec,d,scene,p)


def lessons(doc):
    # Independently check that midpoint/difference vectors satisfy mirror geometry.
    assert ((-7+4)/2,(4-7)/2)==(-1.5,-1.5)
    assert (4-(-7))+(-7-4)==0
    batch=make_lessons(SPECS,doc)
    for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:diagram(s,d,scene,p)
    return batch
