"""Numerical examples for tangent geometry, with true circle/line diagrams."""
from math import sqrt,hypot,isclose
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons,draw_card,centered_math
import generate_sample_videos as v

SPECS=[
authored('geometry-tangent-radius-distance','Use the perpendicular radius at a tangent',
 'A circle has centre O and radius 13 cm.\nLine L is tangent at T. Find the angle between OT and L,\nand the shortest distance from O to L.',
 '90 degrees; 13 centimetres',
 'A circle has radius thirteen centimetres. Line L is tangent at T. Find the angle between the radius and the tangent, and the shortest distance from the centre to the line.',[
 ('JOIN THE CENTRE','Draw the radius to the point of contact','OT = 13 cm',
  'Join the centre O to the point of contact T. This segment is a radius, so its length is thirteen centimetres.'),
 ('TANGENT PROPERTY','The tangent is perpendicular to the radius at T','Angle between OT and L = 90°',
  'A tangent is perpendicular to the radius at the point of contact. The angle is ninety degrees.'),
 ('SHORTEST DISTANCE','Measure perpendicular to the line','Distance from O to L = OT = 13 cm',
  'Distance from a point to a line means the perpendicular distance. Here that segment is O T, so the distance is thirteen centimetres.'),
 ('CONSTRUCTION RULE','Draw the perpendicular through the contact point','To draw L: construct a perpendicular to OT at T.',
  'This also gives a construction method: draw the radius, then construct a line through T perpendicular to that radius.')],
 g(10,11,3,8),expression='13',value='13'),

authored('geometry-equal-tangent-segments-equation','Use equal tangent segments to solve for a length',
 'PA and PB are tangent segments from the same point P.\nPA = 3x + 2 cm and PB = 5x − 12 cm.\nFind x and the length of each tangent segment.',
 'x = 7; PA = PB = 23 centimetres',
 'Two tangents from point P have lengths three x plus two and five x minus twelve centimetres. Find x and both lengths.',[
 ('EQUAL TANGENTS','Tangents from the same outside point have equal lengths','PA = PB → 3x + 2 = 5x − 12',
  'Tangent segments from the same external point have equal lengths. Set the two expressions equal.'),
 ('SOLVE','Collect the x terms and constants','3x + 14 = 5x\n14 = 2x → x = 7',
  'Add twelve to both sides, then subtract three x. Fourteen equals two x, so x equals seven.'),
 ('SUBSTITUTE','Use x = seven in both length expressions','PA = 3(7) + 2 = 23 cm\nPB = 5(7) − 12 = 23 cm',
  'Substitute seven into both expressions. Each gives twenty-three centimetres.'),
 ('CHECK','Equal positive lengths satisfy the tangent property','x = 7; PA = PB = 23 cm',
  'The lengths are equal and positive, as required. Remember that equal tangents must start at the same external point.')],
 g(10,11,3,4),equation=('3*x+2','5*x-12','x','7'),equalities=[('3*7+2','23'),('5*7-12','23')]),

authored('geometry-tangent-external-distance','Find centre-to-point distance using a tangent',
 'PT is tangent to a circle at T.\nThe radius OT is 9 cm and PT = 40 cm.\nFind OP, from the centre to the external point.',
 '41 centimetres',
 'A tangent segment P T is forty centimetres, and the radius O T is nine centimetres. Find the distance from the centre O to point P.',[
 ('RIGHT ANGLE','The radius and tangent meet at ninety degrees','OT is perpendicular to PT',
  'The radius to the contact point is perpendicular to the tangent, so O T P is a right triangle.'),
 ('HYPOTENUSE','OP is opposite the right angle','OP² = OT² + PT²',
  'O P is opposite the right angle. It is the hypotenuse, so add the squares of the other two sides.'),
 ('CALCULATE','Square and add before taking the root','OP² = 9² + 40² = 81 + 1600 = 1681',
  'Nine squared plus forty squared is eighty-one plus sixteen hundred, or one thousand six hundred eighty-one.'),
 ('TAKE THE POSITIVE ROOT','A distance must be positive','OP = √1681 = 41 cm',
  'The positive square root is forty-one. The centre-to-point distance is forty-one centimetres, longer than either leg.')],
 g(10,11,3,6),expression='9**2+40**2',value='1681',equalities=[('41**2','1681')]),

authored('geometry-tangent-missing-radius','Find a radius from a tangent and external distance',
 'PT is tangent to a circle at T.\nOP = 37 cm and PT = 35 cm, where O is the centre.\nFind the radius OT.',
 '12 centimetres',
 'Point P is thirty-seven centimetres from a circle centre. A tangent from P has length thirty-five centimetres. Find the radius to its point of contact.',[
 ('RIGHT TRIANGLE','The radius is perpendicular to the tangent','OT² + PT² = OP²',
  'The radius and tangent meet at ninety degrees. The centre-to-point segment O P is the hypotenuse.'),
 ('ISOLATE THE LEG','Subtract the known leg squared','OT² = 37² − 35²',
  'The missing radius is a leg. Subtract the tangent length squared from the hypotenuse squared.'),
 ('CALCULATE','Keep the squares in the correct order','OT² = 1369 − 1225 = 144',
  'Thirty-seven squared minus thirty-five squared is one thousand three hundred sixty-nine minus one thousand two hundred twenty-five, giving one hundred forty-four.'),
 ('TAKE THE ROOT','Use the positive root for a length','OT = √144 = 12 cm',
  'The positive square root of one hundred forty-four is twelve. The radius is twelve centimetres.')],
 g(10,11,'3Rev',4),expression='37**2-35**2',value='144',equalities=[('12**2','144')]),

authored('geometry-tangent-versus-secant-intersections','Distinguish tangents from secants by intersections',
 'For the circle x² + y² = 25, classify the lines\ny = 3 and y = 5 as secants or tangents.',
 'y = 3 is a secant; y = 5 is a tangent',
 'A circle has equation x squared plus y squared equals twenty-five. Classify the lines y equals three and y equals five as secants or tangents.',[
 ('TEST THE FIRST LINE','Substitute y = three in the circle equation','x² + 3² = 25 → x² = 16 → x = ±4',
  'For y equals three, x squared is sixteen, so x can be four or negative four.'),
 ('TWO INTERSECTIONS','A secant crosses at two distinct points','(−4, 3) and (4, 3) → y = 3 is a secant',
  'There are two distinct intersection points. That makes this line a secant.'),
 ('TEST THE SECOND LINE','Substitute y = five','x² + 5² = 25 → x² = 0 → x = 0',
  'For y equals five, x squared is zero. There is just one intersection, at zero, five.'),
 ('ONE POINT OF CONTACT','A tangent meets the circle at exactly one point','(0, 5) only → y = 5 is a tangent',
  'One point of contact makes this line a tangent. A line meeting a circle at two distinct points is a secant, not a tangent.')],
 g(10,11,3,9),expression='25-3**2',value='16',equalities=[('25-5**2','0'),('4**2+3**2','25'),('(-4)**2+3**2','25')]),
]


def dot(d,pt,label,dx=0,dy=25):
    x,y=pt;d.ellipse((x-5,y-5,x+5,y+5),fill=v.INK);v.text(d,(x+dx,y+dy),label,31,v.INK,True,anchor='mm')


def diagram(spec,d,scene,p):
    if scene not in (1,2,3):draw_card(spec,d,scene,p);return
    vid=spec['video_id']
    if vid=='geometry-tangent-radius-distance':
        O=(940,555);R=175;T=(940,730)
        d.ellipse((O[0]-R,O[1]-R,O[0]+R,O[1]+R),outline=v.TEAL,width=4)
        d.line((610,T[1],1320,T[1]),fill=v.INK,width=4);d.line((*O,*T),fill=v.TEAL,width=4)
        d.line((T[0],T[1]-20,T[0]+20,T[1]-20,T[0]+20,T[1]),fill=v.INK,width=3)
        dot(d,O,'O',-26,0);dot(d,T,'T',0,29)
        v.text(d,(1008,642),'13 cm',31,v.INK,True,anchor='mm');v.text(d,(1350,730),'L',31,v.INK,True,anchor='mm')
    elif vid=='geometry-equal-tangent-segments-equation':
        O=(800,585);R=165;P=(1200,585);ox=R*R/400;oy=sqrt(R*R-ox*ox)
        A=(O[0]+ox,O[1]-oy);B=(O[0]+ox,O[1]+oy)
        d.ellipse((O[0]-R,O[1]-R,O[0]+R,O[1]+R),outline=v.TEAL,width=4)
        for pt,label in [(A,'A'),(B,'B')]:d.line((*P,*pt),fill=v.INK,width=4);dot(d,pt,label,-15,-28 if label=='A' else 28)
        dot(d,P,'P',27,0)
        v.text(d,(1040,466),'3x + 2',32,v.INK,True,anchor='mm');v.text(d,(1040,708),'5x − 12',32,v.INK,True,anchor='mm')
    elif vid in ('geometry-tangent-external-distance','geometry-tangent-missing-radius'):
        radius,tangent,distance=(9,40,41) if vid=='geometry-tangent-external-distance' else (12,35,37)
        s=10;O=(740,650);T=(740,650-radius*s);P=(740+tangent*s,T[1])
        d.ellipse((O[0]-radius*s,O[1]-radius*s,O[0]+radius*s,O[1]+radius*s),outline=v.TEAL,width=4)
        d.polygon([O,T,P],outline=v.INK,width=4)
        d.line((T[0],T[1]+18,T[0]+18,T[1]+18,T[0]+18,T[1]),fill=v.INK,width=3)
        dot(d,O,'O',-24,24);dot(d,T,'T',-26,-18);dot(d,P,'P',25,0)
        v.text(d,(O[0]-radius*s-100,(O[1]+T[1])/2),'OT = 9 cm' if radius==9 else 'OT = ?',30,v.INK,True,anchor='mm')
        v.text(d,((T[0]+P[0])/2,T[1]-30),f'{tangent} cm',31,v.INK,True,anchor='mm')
        v.text(d,((O[0]+P[0])/2+35,(O[1]+P[1])/2+40),'OP = ?' if radius==9 else '37 cm',31,v.INK,True,anchor='mm')
    else:
        def xy(x,y):return 960+x*31,625-y*31
        d.ellipse((*xy(-5,5),*xy(5,-5)),outline=v.TEAL,width=4)
        d.line((*xy(-7,0),*xy(7,0)),fill='#BCCEC6',width=2);d.line((*xy(0,-5.7),*xy(0,6.5)),fill='#BCCEC6',width=2)
        d.line((*xy(-7,3),*xy(7,3)),fill='#B66F4E',width=4)
        for x in (-4,4):dot(d,xy(x,3),f'({x}, 3)',-85 if x<0 else 85,27)
        v.text(d,xy(8.4,3),'y = 3',30,'#B66F4E',True,anchor='mm')
        if scene>=3:
            d.line((*xy(-7,5),*xy(7,5)),fill=v.INK,width=4);dot(d,xy(0,5),'(0, 5)',0,-27)
            v.text(d,xy(8.4,5),'y = 5',30,v.INK,True,anchor='mm')
    for i,line in enumerate(spec['displays'][scene].split('\n')):centered_math(d,835+i*60,line,39,v.TEAL)


def lessons(doc):
    # Radius vectors at the two drawn contact points are perpendicular to tangents.
    R=165;ox=R*R/400;oy=sqrt(R*R-ox*ox)
    assert isclose(ox*(400-ox)-oy*oy,0,abs_tol=1e-8)
    assert isclose(hypot(400-ox,oy),hypot(400-ox,-oy))
    assert 9**2+40**2==41**2 and 12**2+35**2==37**2
    batch=make_lessons(SPECS,doc)
    for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:diagram(s,d,scene,p)
    return batch
