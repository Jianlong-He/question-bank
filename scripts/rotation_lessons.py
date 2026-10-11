"""Rotations with explicit centers and independently checked coordinates."""
from math import pi,sin,cos,isclose
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons,draw_card,centered_math
from reflection_lessons import axes,point
from symmetry_lessons import OCTAGON
from trig_graph_lessons import graph
import generate_sample_videos as v

SPECS=[
authored('geometry-rotation-quarter-ccw','Rotate a point ninety degrees counterclockwise',
 'Rotate P(−8, 3) by 90° counterclockwise\nabout the origin. Find P′.', '(−3, −8)',
 'Rotate negative eight, three ninety degrees counterclockwise about the origin. Find the image point.',[
 ('RULE','A quarter-turn swaps coordinates and changes one sign','(x, y) → (−y, x)',
  'For a ninety degree counterclockwise turn about the origin, the new x is negative old y, and the new y is old x.'),
 ('SUBSTITUTE','Move each original value into its new position','x′ = −3; y′ = −8',
  'The original y is three, so the new x is negative three. The original x is negative eight, so the new y is negative eight.'),
 ('LOCATE THE IMAGE','Quadrant II turns into Quadrant III','P′ = (−3, −8)',
  'The image is negative three, negative eight. The point moves from quadrant two to quadrant three, consistent with a counterclockwise quarter-turn.'),
 ('CHECK','Rotation preserves distance from the origin','(−8)² + 3² = (−3)² + (−8)² = 73',
  'The squared distance from the origin stays seventy-three. You can recognize this same coordinate rule when asked to identify the rotation from a point and its image.')],
 g(8,6,2,7),expression='(-8)**2+3**2',value='73',equalities=[('(-3)**2+(-8)**2','73')]),

authored('geometry-rotation-quarter-cw','Rotate a point clockwise or three quarters counterclockwise',
 'Rotate Q(−7, −4) by 90° clockwise\nabout the origin. Find Q′.', '(−4, 7)',
 'Rotate negative seven, negative four ninety degrees clockwise about the origin. Find its image.',[
 ('EQUIVALENT TURN','Ninety clockwise equals two hundred seventy counterclockwise','90° CW = 270° CCW, about the same center',
  'A ninety degree clockwise turn ends at the same position as a two hundred seventy degree counterclockwise turn about the same center.'),
 ('RULE','Swap the coordinates and negate the original x','(x, y) → (y, −x)',
  'The new x is the original y. The new y is the negative of the original x.'),
 ('SUBSTITUTE','Negating a negative gives a positive','Q′ = (−4, −(−7)) = (−4, 7)',
  'The image is negative four, positive seven. Keep track of the double negative.'),
 ('CHECK','Quadrant III turns clockwise into Quadrant II','(−7)² + (−4)² = (−4)² + 7² = 65',
  'The point moves from quadrant three to quadrant two. Its distance from the origin stays the same. This rule also identifies a clockwise quarter-turn from matching coordinates.')],
 g(8,6,3,7),expression='(-7)**2+(-4)**2',value='65',equalities=[('(-4)**2+7**2','65')]),

authored('geometry-rotation-half-turn','Rotate a point one hundred eighty degrees',
 'Rotate R(−6, 9) by 180° about the origin.\nFind R′.', '(6, −9)',
 'Rotate negative six, nine one hundred eighty degrees about the origin. Find the image point.',[
 ('HALF-TURN','The image is directly opposite across the origin','(x, y) → (−x, −y)',
  'A half-turn sends a point to the opposite side of the origin, the same distance away. Both coordinate signs reverse.'),
 ('SUBSTITUTE','Negate both coordinates','R′ = (−(−6), −9) = (6, −9)',
  'Negative six becomes positive six, and nine becomes negative nine.'),
 ('CENTER CHECK','The origin is the midpoint of point and image','Midpoint = ((−6 + 6)/2, (9 − 9)/2) = (0, 0)',
  'The midpoint of the original and image is the origin, which checks the center of the half-turn.'),
 ('DIRECTION','Either direction gives the same half-turn','180° clockwise = 180° counterclockwise',
  'A half-turn ends at the same place in either direction. If a coordinate mapping reverses both signs, it describes this rotation about the origin.')],
 g(8,6,1,9),expression='(-6+6)/2',value='0',equalities=[('(9-9)/2','0')]),

authored('geometry-rotation-equivalent-directions','Find an equivalent turn in the opposite direction',
 'A figure turns 150° clockwise about O.\nWhat counterclockwise turn less than 360°\nhas the same final position?', '210 degrees counterclockwise',
 'A figure turns one hundred fifty degrees clockwise about O. What counterclockwise turn less than one full revolution gives the same final position?',[
 ('FULL TURN','One complete revolution is three hundred sixty degrees','Full turn = 360°',
  'One full revolution is three hundred sixty degrees.'),
 ('OTHER WAY AROUND','Subtract the given angle from a full turn','360° − 150°',
  'Going the opposite way covers the rest of the revolution. Subtract one hundred fifty from three hundred sixty.'),
 ('CALCULATE','Keep the new direction in the answer','210° counterclockwise about O',
  'The equivalent turn is two hundred ten degrees counterclockwise about the same center.'),
 ('CHECK','The two path lengths complete a full revolution','150° + 210° = 360°',
  'The two angles add to a full turn. The paths differ, but they end at the same position. Always specify both direction and center.')],
 g(8,6,8,3),expression='360-150',value='210',equalities=[('150+210','360')]),

authored('geometry-rotation-regular-polygon','Find the smallest rotational symmetry angle',
 'What is the smallest positive turn that maps\na regular octagon onto itself about its center?', '45 degrees',
 'What is the smallest positive turn that maps a regular octagon onto itself about its center?',[
 ('COUNT POSITIONS','There are eight equally spaced vertices','8 matching positions in one full turn',
  'A regular octagon has eight equally spaced vertices. A rotation to the next vertex makes the whole shape match.'),
 ('DIVIDE THE TURN','Split a full turn into eight equal parts','360° ÷ 8',
  'Divide three hundred sixty degrees by eight.'),
 ('RESULT','One vertex step is the smallest positive matching turn','Smallest angle = 45°',
  'The smallest angle is forty-five degrees. A smaller positive turn would place each vertex between vertices, so the outline would not match.'),
 ('GENERAL RULE','Use the number of sides for a regular polygon','Regular n-gon: smallest turn = 360°/n',
  'For a regular polygon with n sides, divide a full turn by n. Larger matching rotations are multiples of this angle, but the question asks for the smallest.')],
 g(9,16,3,4),expression='360/8',value='45'),

authored('geometry-rotation-odd-function','Recognize half-turn symmetry of an odd function',
 'For f(x) = 2x³ − x, show that the graph\nhas half-turn symmetry. Find its center.', 'The origin, (0, 0)',
 'For f of x equals two x cubed minus x, show that its graph has half-turn symmetry and find the center.',[
 ('SUBSTITUTE NEGATIVE X','Replace every x by negative x','f(−x) = 2(−x)³ − (−x)',
  'Replace every x by negative x, keeping parentheses around the input.'),
 ('SIMPLIFY','Factor out a minus sign','f(−x) = −2x³ + x = −f(x)',
  'The result is negative two x cubed plus x. That is the negative of the original function, so this function is odd.'),
 ('PAIR GRAPH POINTS','Negating both coordinates gives another graph point','(x, f(x)) → (−x, −f(x))',
  'For every point on the graph, the point with both signs reversed is also on the graph.'),
 ('INTERPRET','Negating both coordinates is a half-turn about the origin','Center of half-turn symmetry: (0, 0)',
  'Reversing both coordinate signs is a one hundred eighty degree rotation about the origin. That proves the graph has half-turn symmetry centered at zero, zero.')],
 g(11,6,2,7),identities=[('2*(-x)**3-(-x)','-(2*x**3-x)')]),

authored('geometry-rotation-center-angle','Identify the center and angle of a rotation',
 'A point moves from A to B along a 120°\ncounterclockwise arc centered at O.\nName the transformation, its center, and its angle.',
 'Rotation about O through 120 degrees counterclockwise',
 'A point moves from A to B along a one hundred twenty degree counterclockwise arc centered at O. Name the transformation, its center, and its angle.',[
 ('FIXED CENTER','The turning point O remains fixed','Center = O',
  'The motion turns around O. This fixed turning point is called the center of rotation.'),
 ('DISTANCE','A rotation keeps the distance to the center','OA = OB',
  'The point stays the same distance from O throughout the turn, so O A and O B are equal.'),
 ('ANGLE','Measure the turn at the center','Angle AOB = 120° counterclockwise',
  'Read the directed angle from the original ray O A to the image ray O B. Here it is one hundred twenty degrees counterclockwise.'),
 ('DESCRIBE THE MOVE','Include center, angle, and direction','Rotation: center O; 120° counterclockwise',
  'The transformation is a rotation about O through one hundred twenty degrees counterclockwise. A center, angle, and direction specify a rotation.')],
 g(9,15,1,2),expression='360/3',value='120'),

authored('geometry-rotation-parallelogram','Check half-turn symmetry using opposite vertices',
 'A quadrilateral has vertices (−4, −2), (2, −2),\n(4, 2), and (−2, 2), in order. Does a half-turn\nabout the origin map it onto itself?', 'Yes',
 'A quadrilateral has vertices negative four, negative two; two, negative two; four, two; and negative two, two. Does a half-turn about the origin map it onto itself?',[
 ('OPPOSITE PAIRS','Apply the half-turn rule to one opposite pair','(−4, −2) → (4, 2)',
  'A half-turn reverses both signs. The first vertex maps to the opposite vertex, four, two.'),
 ('OTHER PAIR','Check the remaining two vertices','(2, −2) → (−2, 2)',
  'The second vertex maps to negative two, two. The other pair also exchanges places.'),
 ('WHOLE OUTLINE','Corresponding sides exchange and the outline matches','Every vertex and side returns to the same outline.',
  'Both opposite pairs exchange, and every side maps to the opposite side. The whole outline matches, so the answer is yes.'),
 ('PARALLELOGRAM RULE','The diagonals bisect each other at the turning center','Half-turn center = intersection of the diagonals',
  'This is a parallelogram. Its diagonals share a midpoint, the origin here. Every parallelogram has half-turn symmetry about the intersection of its diagonals.')],
 g(9,16,3,5),expression='(-4+4)/2',value='0',equalities=[('(-2+2)/2','0'),('(2-2)/2','0')]),
]


def diagram(spec,d,scene,p):
    vid=spec['video_id'];orange='#B66F4E'
    if vid in ('geometry-rotation-quarter-ccw','geometry-rotation-quarter-cw','geometry-rotation-half-turn') and scene in (1,3):
        xy=axes(d)
        a,b= {'geometry-rotation-quarter-ccw':((-8,3),(-3,-8)), 'geometry-rotation-quarter-cw':((-7,-4),(-4,7)), 'geometry-rotation-half-turn':((-6,9),(6,-9))}[vid]
        for pt in [a,b]:d.line([xy(0,0),xy(*pt)],fill='#A8BEB9',width=4)
        name='Q' if vid.endswith('quarter-cw') else 'R' if vid.endswith('half-turn') else 'P'
        point(d,xy,*a,f'{name}{a}',(-190,-30));point(d,xy,*b,f'{name}′{b}',(12,-15))
        label={'geometry-rotation-quarter-ccw':'90° CCW: (x, y) → (−y, x)','geometry-rotation-quarter-cw':'90° CW: (x, y) → (y, −x)','geometry-rotation-half-turn':'180°: (x, y) → (−x, −y)'}[vid]
        centered_math(d,900,label,42,v.TEAL)
    elif vid=='geometry-rotation-regular-polygon' and scene in (0,1,2,3):
        cx,cy,r=960,585,205
        xy=lambda x,y:(cx+r*x,cy-r*y)
        d.polygon([xy(x,y) for x,y in OCTAGON],fill='#D4E8E1',outline=v.TEAL,width=4)
        for a in [i*pi/4 for i in range(8)]:d.line([(cx,cy),xy(cos(a),sin(a))],fill='#A8BEB9',width=2)
        v.text(d,(cx+75,cy-45),'45°' if scene>=2 else '?',35,orange,True)
        centered_math(d,870,'360° ÷ 8 = 45°' if scene>=2 else 'Eight equal vertex steps fill one full turn.',44,v.TEAL)
    elif vid=='geometry-rotation-odd-function' and scene in (3,4):
        graph(d,[(lambda x:2*x**3-x,v.TEAL)],-1.5,1.5,-6,6,[(-1,'−1'),(0,'0'),(1,'1')],[(-5,'−5'),(0,'0'),(5,'5')])
        centered_math(d,860,'(x, y) → (−x, −y); center (0, 0)',42,v.TEAL)
    elif vid=='geometry-rotation-center-angle' and scene>0:
        cx,cy,r=950,650,230
        a=(cx+r,cy);b=(cx+r*cos(2*pi/3),cy-r*sin(2*pi/3))
        d.line([(cx,cy),a],fill=v.TEAL,width=4);d.line([(cx,cy),b],fill=v.TEAL,width=4)
        curve=[(cx+100*cos(t*2*pi/180),cy-100*sin(t*2*pi/180)) for t in range(61)]
        d.line(curve,fill=orange,width=4)
        X,Y=curve[-1];d.polygon([(X,Y),(X+15,Y-3),(X+7,Y+12)],fill=orange)
        for pt,label in [((cx,cy),'O'),(a,'A'),(b,'B')]:v.text(d,(pt[0]+12,pt[1]+12),label,38,v.TEAL,True)
        v.text(d,(cx+75,cy-100),'120° CCW',32,orange,True)
        centered_math(d,870,spec['displays'][scene],42,v.INK)
    elif vid=='geometry-rotation-parallelogram' and scene in (1,2,3):
        xy=lambda x,y:(950+80*x,570-70*y)
        pts=[(-4,-2),(2,-2),(4,2),(-2,2)]
        d.polygon([xy(*pt) for pt in pts],fill='#D4E8E1',outline=v.TEAL,width=4)
        for a,b in [(pts[0],pts[2]),(pts[1],pts[3])]:d.line([xy(*a),xy(*b)],fill=orange,width=3)
        for x,y in pts:point(d,xy,x,y,f'({x}, {y})',(10,-40 if y>0 else 12))
        v.text(d,(960,580),'O',30,v.INK,True)
        centered_math(d,855,spec['displays'][scene],40,v.TEAL)
    else:draw_card(spec,d,scene,p)


def lessons(doc):
    for x,y in [(-8,3),(-7,-4),(-6,9)]:
        for a,expected in [(pi/2,(-y,x)),(-pi/2,(y,-x)),(pi,(-x,-y))]:
            got=(x*cos(a)-y*sin(a),x*sin(a)+y*cos(a))
            assert all(isclose(u,w,abs_tol=1e-10) for u,w in zip(got,expected))
    batch=make_lessons(SPECS,doc)
    for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:diagram(s,d,scene,p)
    return batch
