"""Original numeric illustrations of area, similarity and inscribed-angle arguments.

Teaching facts checked against sources recorded in videos/lesson-source-references.txt.
All diagrams are constructed here, not copied from source illustrations.
"""
from math import tan,sin,cos,radians,hypot,isclose
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons,draw_card,centered_math
import generate_sample_videos as v

SPECS=[
authored('geometry-pythagorean-area-argument','Use area comparison in a Pythagorean arrangement',
 'Four right triangles, each with legs 4 cm and 7 cm,\nsurround a central square inside an 11 cm square.\nFind the central square’s area by comparing areas.',
 '65 square centimetres',
 'Four right triangles, each with legs four and seven centimetres, surround a central square inside an eleven centimetre square. Find the central area by comparing areas.',[
 ('THE OUTER SQUARE','Its side is four plus seven','Outer area = 11² = 121 cm²',
  'The outer square has side eleven, so its area is one hundred twenty-one square centimetres.'),
 ('THE FOUR TRIANGLES','Find one triangle’s area, then multiply by four','4 × [(1/2) × 4 × 7] = 56 cm²',
  'Each triangle has area fourteen. All four together cover fifty-six square centimetres.'),
 ('THE CENTRAL SQUARE','Subtract the triangles from the whole','Central area = 121 − 56 = 65 cm²',
  'Subtract fifty-six from one hundred twenty-one. The central square covers sixty-five square centimetres.'),
 ('THE GENERAL ARGUMENT','The same area comparison works with legs a and b','c = hypotenuse; central square area = c²\nc² = (a + b)² − 4(ab/2) = a² + b²',
  'Each central side is a hypotenuse, c. For legs a and b, subtracting triangle areas gives c squared equals a squared plus b squared. Garfield’s and Bhaskara’s proofs also compare areas.')],
 g(10,9,1,8),expression='11**2-4*(1/2)*4*7',value='65',identities=[('(a+b)**2-4*(a*b/2)','a**2+b**2')]),

authored('geometry-right-triangle-altitude-similarity','Use an altitude to create similar right triangles',
 'Triangle ABC is right-angled at C, and angle A is 35°.\nDraw altitude CD to hypotenuse AB.\nFind the angles in the two smaller triangles.',
 'Each smaller triangle has angles 35°, 55° and 90°',
 'Triangle A B C is right-angled at C, and angle A is thirty-five degrees. Draw altitude C D to the hypotenuse. Find the angles in the two smaller triangles.',[
 ('DRAW THE ALTITUDE','CD meets the hypotenuse at a right angle','CD is perpendicular to AB.',
  'Draw C D from the right-angle vertex perpendicular to the hypotenuse. Both smaller triangles have a right angle at D.'),
 ('FIND THE OTHER ORIGINAL ANGLE','A triangle’s angles total one hundred eighty degrees','Angle B = 180° − 90° − 35° = 55°',
  'The original angle at B is one hundred eighty minus ninety minus thirty-five, giving fifty-five degrees.'),
 ('COMPARE THE SMALL TRIANGLES','Each keeps one of the original acute angles','ACD: 35°, 55°, 90°\nBCD: 55°, 35°, 90°',
  'The first small triangle keeps angle A. The other keeps angle B. Their remaining acute angles are fifty-five and thirty-five degrees.'),
 ('USE AA SIMILARITY','Their corresponding angles match','Both smaller triangles are similar\nto the original triangle by AA.',
  'Both small triangles have the same angles as the original, so they are similar by angle-angle. This altitude construction starts a similarity proof of Pythagoras.')],
 g(10,9,1,9),expression='180-90-35',value='55',equalities=[('35+55+90','180')]),

authored('geometry-inscribed-angle-diameter-test','Use an inscribed angle to test for a diameter',
 'A, B and C lie on a circle.\nArc AB not containing C measures 144°.\nFind angle ACB. Is chord AB a diameter?',
 'Angle ACB = 72°; AB is not a diameter',
 'A, B, and C lie on a circle. The arc A B that does not contain C measures one hundred forty-four degrees. Find angle A C B and decide whether A B is a diameter.',[
 ('THE INTERCEPTED ARC','Use the arc between A and B away from C','Intercepted arc = 144°',
  'Use the arc between A and B that is away from C. Its measure is one hundred forty-four degrees.'),
 ('HALVE THE ARC','An inscribed angle is half its intercepted arc','Angle ACB = 144° ÷ 2 = 72°',
  'An inscribed angle is half the measure of its intercepted arc. The angle is seventy-two degrees.'),
 ('TEST THE CHORD','A diameter would intercept a semicircle','72° is not 90°, so AB is not a diameter.',
  'A diameter would intercept a semicircle and give a ninety-degree inscribed angle. Seventy-two is not ninety, so A B is not a diameter.'),
 ('THE RIGHT-ANGLE CASE','A right angle intercepts a one-hundred-eighty-degree arc','90° × 2 = 180°\nThen the opposite chord is a diameter.',
  'Conversely, a ninety-degree inscribed angle intercepts one hundred eighty degrees. Its opposite chord is then a diameter.')],
 g(10,11,2,10),expression='144/2',value='72',equalities=[('90*2','180')]),
]


def altitude_points():
    a,b=8,8*tan(radians(35));t=a*a/(a*a+b*b)
    return (a,0),(0,b),(0,0),(a*(1-t),b*t)


def diagram(spec,d,scene,p):
    vid=spec['video_id']
    if scene not in (1,2,3):draw_card(spec,d,scene,p);return
    if vid=='geometry-pythagorean-area-argument':
        x,y,s=770,370,34
        def pts(coords):return [(x+a*s,y+b*s) for a,b in coords]
        d.rectangle((x,y,x+11*s,y+11*s),fill='white',outline=v.TEAL,width=4)
        for tri in [[(0,0),(4,0),(0,7)],[(11,0),(11,4),(4,0)],[(11,11),(7,11),(11,4)],[(0,11),(0,7),(7,11)]]:
            d.polygon(pts(tri),fill='#D0E8E2',outline=v.TEAL,width=3)
        v.text(d,(x+2*s,y-25),'4 cm',29,v.INK,True,anchor='mm')
        v.text(d,(x+7.5*s,y-25),'7 cm',29,v.INK,True,anchor='mm')
        v.text(d,(x+5.5*s,y+11*s+28),'11 cm',30,v.INK,True,anchor='mm')
        v.text(d,(x+5.5*s,y+5.5*s),'central square',28,v.INK,True,anchor='mm')
    elif vid=='geometry-right-triangle-altitude-similarity':
        A,B,C,D=altitude_points();x,y,s=700,735,52
        def screen(pt):return (x+s*pt[0],y-s*pt[1])
        aa,bb,cc,dd=map(screen,[A,B,C,D])
        d.polygon([aa,dd,cc],fill='#D0E8E2',outline=v.TEAL,width=3)
        d.polygon([bb,dd,cc],fill='#F1DBB9',outline=v.TEAL,width=3)
        d.line((*cc,*dd),fill=v.INK,width=4)
        d.line((cc[0]+22,cc[1],cc[0]+22,cc[1]-22,cc[0],cc[1]-22),fill=v.INK,width=3)
        u=((aa[0]-dd[0])/hypot(aa[0]-dd[0],aa[1]-dd[1]),(aa[1]-dd[1])/hypot(aa[0]-dd[0],aa[1]-dd[1]))
        w=((cc[0]-dd[0])/hypot(cc[0]-dd[0],cc[1]-dd[1]),(cc[1]-dd[1])/hypot(cc[0]-dd[0],cc[1]-dd[1]))
        marker=[(dd[0]+u[0]*18,dd[1]+u[1]*18),(dd[0]+(u[0]+w[0])*18,dd[1]+(u[1]+w[1])*18),(dd[0]+w[0]*18,dd[1]+w[1]*18)]
        d.line(marker,fill=v.INK,width=3)
        for label,pt,dx,dy in [('A',aa,25,18),('B',bb,-20,-25),('C',cc,-25,20),('D',dd,18,-27)]:v.text(d,(pt[0]+dx,pt[1]+dy),label,34,v.INK,True,anchor='mm')
        v.text(d,(aa[0]-90,aa[1]-22),'35°',30,v.INK,True,anchor='mm')
    elif vid=='geometry-inscribed-angle-diameter-test':
        cx,cy,R=960,555,190;box=(cx-R,cy-R,cx+R,cy+R)
        A=(cx+R*cos(radians(162)),cy+R*sin(radians(162)))
        B=(cx+R*cos(radians(18)),cy+R*sin(radians(18)))
        C=(cx,cy-R)
        d.ellipse(box,outline=v.TEAL,width=4);d.polygon([A,B,C],fill='#D0E8E2',outline=v.TEAL,width=3)
        d.arc(box,18,162,fill='#B66F4E',width=7)
        for label,pt,dx,dy in [('A',A,-25,20),('B',B,25,20),('C',C,0,-27)]:v.text(d,(pt[0]+dx,pt[1]+dy),label,32,v.INK,True,anchor='mm')
        d.ellipse((cx-4,cy-4,cx+4,cy+4),fill=v.INK);v.text(d,(cx-20,cy),'O',28,v.INK,True,anchor='mm')
        v.text(d,(cx,cy+R+25),'144° arc',30,'#B66F4E',True,anchor='mm')
    for i,line in enumerate(spec['displays'][scene].split('\n')):centered_math(d,825+i*65,line,42,v.TEAL)


def lessons(doc):
    # Verify the constructed central quadrilateral is a square of area65.
    pts=[(4,0),(11,4),(7,11),(0,7)]
    edges=[(pts[(i+1)%4][0]-x,pts[(i+1)%4][1]-y) for i,(x,y) in enumerate(pts)]
    assert all(x*x+y*y==65 for x,y in edges)
    assert all(edges[i][0]*edges[(i+1)%4][0]+edges[i][1]*edges[(i+1)%4][1]==0 for i in range(4))
    A,B,C,D=altitude_points()
    assert isclose((B[0]-A[0])*D[0]+(B[1]-A[1])*D[1],0,abs_tol=1e-10)
    batch=make_lessons(SPECS,doc)
    for spec in SPECS:v.DRAW[spec['video_id']]=lambda d,scene,p,s=spec:diagram(s,d,scene,p)
    return batch
