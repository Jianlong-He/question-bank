"""Analogous coordinate correspondence and compass construction demonstrations."""
from math import sin,cos,radians,hypot,isclose,atan2,degrees
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons,draw_card,centered_math
import generate_sample_videos as v

SPECS=[
authored('geometry-translation-angle-correspondence','Match vertices and angles after a translation',
 'Translate P(1, 1), Q(4, 1), R(2, 3) by (5, −2).\nFind Q′ and the angle that corresponds to angle Q.',
 'Q′ = (9, −1); angle Q corresponds to angle Q′',
 'Translate triangle P Q R five units right and two down. Find the image of Q, and the angle corresponding to angle Q.',[
 ('TRANSLATION RULE','Add five to x; subtract two from y','(x, y) → (x + 5, y − 2)',
  'A translation applies the same change to every vertex: add five to x, and subtract two from y.'),
 ('TRACK Q','Apply the rule to Q, keeping its label','Q(4, 1) → Q′(4 + 5, 1 − 2) = Q′(9, −1)',
  'Q starts at four, one. Four plus five is nine, and one minus two is negative one. So Q prime is nine, negative one.'),
 ('MATCH VERTICES','Each original vertex has its own image','P → P′; Q → Q′; R → R′',
  'Keep the vertex pairs together. P maps to P prime, Q to Q prime, and R to R prime.'),
 ('MATCH ANGLES','Match the vertices where the angles are formed','Angle Q ↔ angle Q′\nQ′ = (9, −1)',
  'An angle corresponds to the angle at its image vertex. Therefore angle Q corresponds to angle Q prime. A translation also preserves its measure.')],
 g(9,16,1,5),expression='4+5',value='9',equalities=[('1-2','-1'),('1+5','6'),('2+5','7'),('3-2','1')]),

authored('geometry-copy-angle-compass','Copy an angle with a compass',
 'Copy a given 55° angle at a new vertex P\nusing a compass and a straightedge.',
 'The copied angle at P is 55 degrees',
 'Copy a given fifty-five degree angle at a new vertex P, using only a compass and a straightedge.',[
 ('FIRST ARC','Mark where an arc crosses both original rays','Centre O: arc crosses the rays at A and B.',
  'Centre the compass at O and draw an arc across both rays. Name the two intersections A and B.'),
 ('SAME RADIUS','Keep the compass width unchanged for the new arc','Centre P: same radius; baseline intersection Q.',
  'Draw a baseline from P. Without changing the compass width, draw the same-radius arc at P. It meets the baseline at Q.'),
 ('TRANSFER THE SPAN','Now set the compass to the distance from A to B','Centre Q, radius AB: mark R on the new arc.',
  'Now set the compass to the distance from A to B. Centre it at Q and mark R where this arc crosses the new vertex arc.'),
 ('JOIN THE POINTS','Draw ray PR to complete the copied angle','Equal radii and equal chord spans → equal angles\nAngle QPR = 55°',
  'Draw ray P R. Equal radii and equal chord spans give equal angles, so angle Q P R is fifty-five degrees.')],
 g(9,17,6,2),expression='55',value='55'),

authored('geometry-construct-parallel-corresponding-angle','Construct a parallel line by copying an angle',
 'A transversal meets line L at A, making a 68° angle.\nPoint P lies on the transversal above L.\nConstruct a line through P parallel to L.',
 'Copy the 68-degree corresponding angle at P',
 'A transversal meets line L at sixty-eight degrees. Point P lies above the line on the transversal. Construct a parallel line through P.',[
 ('EXTEND THE TRANSVERSAL','Continue the line from A through P','Use the same transversal at both intersections.',
  'Extend the transversal beyond P. We will use it as one arm of the copied angle.'),
 ('COPY THE ANGLE','Use the corresponding position at P','Copy 68° between the upper ray and a rightward ray.',
  'With compass and straightedge, copy the sixty-eight degree angle at P in the corresponding position: between the upper transversal ray and a rightward ray.'),
 ('DRAW THE NEW LINE','Extend the new ray through P in both directions','The two marked corresponding angles are both 68°.',
  'Extend the new ray through P in both directions. The marked corresponding angles are equal.'),
 ('JUSTIFY','Equal corresponding angles imply parallel lines','New line through P is parallel to line L',
  'By the converse of the corresponding-angle theorem, equal corresponding angles make the two lines parallel. This proves the construction works.')],
 g(9,17,6,3),expression='68-68',value='0'),
]


def point(origin,length,angle):
    return origin[0]+length*cos(radians(angle)),origin[1]-length*sin(radians(angle))


def dot(d,pt,label,dx=0,dy=26):
    x,y=pt;d.ellipse((x-5,y-5,x+5,y+5),fill=v.INK)
    v.text(d,(x+dx,y+dy),label,30,v.INK,True,anchor='mm')


def arc(d,pt,r,start,end,color=v.TEAL):
    x,y=pt;d.arc((x-r,y-r,x+r,y+r),start,end,fill=color,width=4)


def draw_translation(spec,d,scene):
    # One coordinate unit has equal horizontal and vertical size.
    def xy(x,y):return 570+x*70,650-y*70
    for x in range(11):
        d.line((*xy(x,-2),*xy(x,4)),fill='#D7E2DB',width=2)
        if x:v.text(d,xy(x,-.35),str(x),22,v.MUTED,anchor='mm')
    for y in range(-2,5):
        d.line((*xy(0,y),*xy(10,y)),fill='#D7E2DB',width=2)
        v.text(d,(xy(0,y)[0]-25,xy(0,y)[1]),str(y),22,v.MUTED,anchor='mm')
    d.line((*xy(0,0),*xy(10.35,0)),fill=v.INK,width=3)
    d.line((*xy(0,-2.1),*xy(0,4.15)),fill=v.INK,width=3)
    v.text(d,xy(10.6,0),'x',26,v.INK,anchor='mm');v.text(d,xy(0,4.4),'y',26,v.INK,anchor='mm')
    original=[(1,1),(4,1),(2,3)];shifted=[(x+5,y-2) for x,y in original]
    for pts,color,labels in [(original,v.TEAL,['P','Q','R']),(shifted,'#B66F4E',['P′','Q′','R′'])]:
        d.polygon([xy(*p) for p in pts],outline=color,width=4)
        for pt,label in zip(pts,labels):dot(d,xy(*pt),label,dy=-24 if label.startswith('R') else 23)
    if scene>=2:
        a=xy(4,1);b=xy(9,-1);d.line((*a,*b),fill='#B66F4E',width=3)
        # Arrowhead follows the translation vector.
        dx,dy=b[0]-a[0],b[1]-a[1];norm=hypot(dx,dy);ux,uy=dx/norm,dy/norm
        d.polygon([b,(b[0]-17*ux+7*uy,b[1]-17*uy-7*ux),(b[0]-17*ux-7*uy,b[1]-17*uy+7*ux)],fill='#B66F4E')
    for i,line in enumerate(spec['displays'][scene].split('\n')):centered_math(d,855+i*55,line,39,v.TEAL)


def draw_copy(spec,d,scene):
    O=(550,660);P=(1200,660);radius=140
    A=point(O,radius,0);B=point(O,radius,55);Q=point(P,radius,0);R=point(P,radius,55)
    span=hypot(B[0]-A[0],B[1]-A[1])
    for a in (0,55):d.line((*O,*point(O,255,a)),fill=v.INK,width=4)
    d.line((*P,*point(P,255,0)),fill=v.INK,width=4)
    dot(d,O,'O',-20,24);dot(d,P,'P',-20,24)
    arc(d,O,radius,290,10);dot(d,A,'A',10,27);dot(d,B,'B',-13,-25)
    v.text(d,(O[0]+75,O[1]-33),'55°',29,v.INK,True,anchor='mm')
    if scene>=2:
        arc(d,P,radius,290,10);dot(d,Q,'Q',10,27)
    if scene>=3:
        d.line((*A,*B),fill='#B66F4E',width=3)
        arc(d,Q,span,208,285,'#B66F4E')
        d.line((*Q,*R),fill='#B66F4E',width=3);dot(d,R,'R',-12,-25)
    if scene==4:
        d.line((*P,*point(P,255,55)),fill=v.TEAL,width=5)
        v.text(d,(P[0]+75,P[1]-33),'55°',29,v.TEAL,True,anchor='mm')
    for i,line in enumerate(spec['displays'][scene].split('\n')):centered_math(d,835+i*60,line,39,v.TEAL)


def draw_parallel(spec,d,scene):
    A=(790,750);P=point(A,330,68);top=point(P,100,68)
    d.line((550,A[1],1390,A[1]),fill=v.INK,width=4)
    d.line((*point(A,-35,68),*top),fill=v.INK,width=4)
    dot(d,A,'A',-26,24);dot(d,P,'P',-25,15)
    v.text(d,(1430,A[1]),'L',32,v.INK,True,anchor='mm')
    arc(d,A,76,292,360);v.text(d,(A[0]+98,A[1]-55),'68°',30,v.INK,True,anchor='mm')
    if scene>=2:
        d.line((P[0] if scene==2 else 550,P[1],1390,P[1]),fill=v.TEAL,width=5)
        arc(d,P,65,292,360);v.text(d,(P[0]+94,P[1]-46),'68°',30,v.TEAL,True,anchor='mm')
    for i,line in enumerate(spec['displays'][scene].split('\n')):centered_math(d,850+i*57,line,39,v.TEAL)


def diagram(spec,d,scene,p):
    if scene==0:draw_card(spec,d,scene,p)
    elif spec['video_id']=='geometry-translation-angle-correspondence':
        if scene==4:draw_card(spec,d,scene,p)
        else:draw_translation(spec,d,scene)
    elif spec['video_id']=='geometry-copy-angle-compass':draw_copy(spec,d,scene)
    else:draw_parallel(spec,d,scene)


def lessons(doc):
    # Verify the copied radius, transferred chord and reconstructed angle.
    O=(550,660);P=(1200,660);A=point(O,140,0);B=point(O,140,55);Q=point(P,140,0);R=point(P,140,55)
    assert isclose(hypot(B[0]-O[0],B[1]-O[1]),140)
    assert isclose(hypot(R[0]-P[0],R[1]-P[1]),140)
    assert isclose(hypot(B[0]-A[0],B[1]-A[1]),hypot(R[0]-Q[0],R[1]-Q[1]))
    assert isclose(degrees(atan2(P[1]-R[1],R[0]-P[0])),55)
    newP=point((790,750),330,68)
    assert isclose(degrees(atan2(750-newP[1],newP[0]-790)),68)
    batch=make_lessons(SPECS,doc)
    for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:diagram(s,d,scene,p)
    return batch
