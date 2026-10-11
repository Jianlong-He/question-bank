"""Visual fold tests using new letter and shape examples."""
from math import sin,cos,pi,isclose
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons,draw_card,centered_math
import generate_sample_videos as v

SPECS=[
authored('geometry-symmetry-block-letters','Find symmetry lines in drawn block letters',
 'Count the lines of symmetry in the three\nblock letters shown: I, V, and F.',
 'I: 2; V: 1; F: 0',
 'Count the lines of symmetry in the three block letters shown: I, V, and F. Use the drawings, since different fonts can change symmetry.',[
 ('LETTER I','A symmetry line gives exactly matching reflected halves','I: 2 lines — vertical and horizontal',
  'The block I matches across its vertical center line and its horizontal center line. It has two lines of symmetry.'),
 ('LETTER V','Test the vertical line and the horizontal line','V: 1 line — vertical',
  'The V matches across the vertical line. A horizontal reflection would put its point at the top, so that line fails. There is exactly one line.'),
 ('LETTER F','A rough resemblance is not an exact match','F: 0 lines',
  'The F has no matching reflection. Its unequal top and middle arms also prevent a horizontal match.'),
 ('COUNT CAREFULLY','Count every valid mirror line, not just vertical ones','I: 2     V: 1     F: 0',
  'The counts are two, one, and zero. Distinguish having a vertical line from having only one line in total. Always inspect the exact letter drawing.')],
 g(4,11,6,2),expression='1+1',value='2'),

authored('geometry-symmetry-regular-polygons','Count symmetry lines of a regular polygon',
 'How many lines of symmetry does a regular octagon\nhave? Explain how to locate them.',
 '8 lines: 4 through opposite vertices and 4 through side midpoints',
 'How many lines of symmetry does a regular octagon have? Explain how to locate them.',[
 ('REGULAR SHAPE','All eight sides and all eight angles are equal','Regular octagon: 8 equal sides',
  'Regular means that all sides and all angles are equal. That condition makes the repeated folds line up.'),
 ('VERTEX LINES','Join pairs of opposite vertices','4 lines through opposite vertices',
  'Four symmetry lines join opposite pairs of vertices. Each produces matching reflected halves.'),
 ('SIDE LINES','Join midpoints of opposite sides','4 more lines through opposite side midpoints',
  'Four more symmetry lines pass through opposite side midpoints. Count each whole line once.'),
 ('GENERAL RULE','A regular n-sided polygon has n symmetry lines','4 + 4 = 8; regular n-gon → n lines',
  'There are eight lines in total. A regular polygon with n sides has n symmetry lines. This also lets you identify the side count from the symmetry count.')],
 g(4,11,6,5),expression='4+4',value='8'),

authored('geometry-symmetry-fold-test','Test whether a line is an axis of symmetry',
 'Count the lines of symmetry of the drawn\nisosceles trapezoid. Its parallel bases\nhave different lengths.',
 '1 line, through the midpoints of the two bases',
 'Count the lines of symmetry of this isosceles trapezoid. Its two parallel bases have different lengths.',[
 ('MIRROR TEST','Every point must reflect onto the same shape','A matching fold line is a line of symmetry.',
  'A line of symmetry is a mirror line that maps the whole shape onto itself. Matching just part of the outline is not enough.'),
 ('VERTICAL LINE','Left and right vertices exchange in matching pairs','The vertical center line works.',
  'The vertical center line pairs each left vertex with a right vertex. Folding there makes the halves coincide.'),
 ('REJECT OTHER LINES','Check the whole outline, not just the center','Horizontal: unequal bases do not match.\nDiagonals: vertices and angles do not match.',
  'The horizontal line fails because the bases have different lengths. The diagonals fail too. Passing through a center does not by itself make a symmetry line.'),
 ('COUNT','Keep only lines that pass the exact mirror test','Exactly 1 line of symmetry',
  'Only the vertical line works. On another polygon, test candidate lines through vertices or side midpoints, keeping only exact matches. A shape may have none, one, or several.')],
 g(9,16,3,1),expression='3-2',value='1'),

authored('geometry-symmetry-circular-ring','Reason about infinitely many symmetry lines',
 'A circular ring has concentric boundaries\nwith radii 2 cm and 5 cm. How many\nlines of symmetry does the ring have?',
 'Infinitely many: every line through the common center',
 'A circular ring has concentric boundaries with radii two and five centimetres. How many lines of symmetry does the ring have?',[
 ('ONE MIRROR','Try a line through the common center','Both circular boundaries match after reflection.',
  'A line through the center reflects each circular boundary onto itself. The ring between them also matches.'),
 ('TURN THE LINE','Its direction can change by any angle','Every center line gives a matching fold.',
  'Turn the line to any angle through the same center. The reflection still preserves each point’s distance from the center, so the ring still matches.'),
 ('COUNT DIRECTIONS','There is no finite list of possible directions','Infinitely many lines of symmetry',
  'There are infinitely many possible directions. Each gives a line of symmetry, so the count is infinite.'),
 ('CHECK THE LOCATION','An off-center line moves the common center','The symmetry lines pass through the center.',
  'An off-center mirror would move the ring’s center, so it would not map the ring onto itself. Its symmetry lines are exactly the lines through the common center.')],
 g(9,16,'3Rev',2),expression='5-2',value='3'),
]

# Explicit filled polygon shapes avoid relying on a font's incidental symmetry.
LETTERS={
 'I':[(-1,-2),(1,-2),(1,-1.5),(.3,-1.5),(.3,1.5),(1,1.5),(1,2),(-1,2),(-1,1.5),(-.3,1.5),(-.3,-1.5),(-1,-1.5)],
 'V':[(-1,2),(-.45,2),(0,-.8),(.45,2),(1,2),(.25,-2),(-.25,-2)],
 'F':[(-1,-2),(-.4,-2),(-.4,-.1),(.5,-.1),(.5,.5),(-.4,.5),(-.4,1.4),(1,1.4),(1,2),(-1,2)],
}
TRAPEZOID=[(-3,-2),(3,-2),(2,2),(-2,2)]
OCTAGON=[(cos(i*pi/4),sin(i*pi/4)) for i in range(8)]


def dashed(d,a,b,color,width=4):
    for i in range(0,24,2):
        p=(a[0]+(b[0]-a[0])*i/24,a[1]+(b[1]-a[1])*i/24)
        q=(a[0]+(b[0]-a[0])*(i+1)/24,a[1]+(b[1]-a[1])*(i+1)/24)
        d.line((p,q),fill=color,width=width)


def letter(d,name,cx,cy=590,scale=78,mirrors=False):
    d.polygon([(cx+x*scale,cy-y*scale) for x,y in LETTERS[name]],fill=v.TEAL)
    if mirrors and name in ('I','V'):dashed(d,(cx,cy-205),(cx,cy+205),'#B66F4E')
    if mirrors and name=='I':dashed(d,(cx-145,cy),(cx+145,cy),'#B66F4E')


def diagram(spec,d,scene,p):
    vid=spec['video_id'];orange='#B66F4E'
    if vid=='geometry-symmetry-block-letters' and scene<4:
        if scene==0:
            for name,cx in zip('IVF',[560,960,1360]):letter(d,name,cx)
            centered_math(d,855,'Count the symmetry lines of each drawn letter.',40,v.INK)
        else:
            name='IVF'[scene-1];letter(d,name,960,mirrors=True)
            centered_math(d,870,spec['displays'][scene],44,v.INK)
    elif vid=='geometry-symmetry-regular-polygons':
        cx,cy,r=960,590,200
        d.polygon([(cx+r*x,cy-r*y) for x,y in OCTAGON],fill='#D4E8E1',outline=v.TEAL,width=5)
        angles=[]
        if scene in (1,2,4):angles+=[i*pi/4 for i in range(4)]
        if scene in (3,4):angles+=[pi/8+i*pi/4 for i in range(4)]
        for a in angles:dashed(d,(cx-230*cos(a),cy+230*sin(a)),(cx+230*cos(a),cy-230*sin(a)),orange)
        label='Regular octagon: how many symmetry lines?' if scene==0 else spec['displays'][scene]
        centered_math(d,870,label,42,v.INK)
    elif vid=='geometry-symmetry-fold-test':
        xy=lambda x,y:(960+90*x,590-70*y)
        d.polygon([xy(x,y) for x,y in TRAPEZOID],fill='#D4E8E1',outline=v.TEAL,width=5)
        if scene in (1,2,4):dashed(d,xy(0,-2.7),xy(0,2.7),orange)
        if scene==3:
            dashed(d,xy(-3.5,0),xy(3.5,0),orange)
            dashed(d,xy(-3,-2),xy(2,2),orange)
            dashed(d,xy(3,-2),xy(-2,2),orange)
        label='Isosceles trapezoid: how many symmetry lines?' if scene==0 else spec['displays'][scene]
        for i,line in enumerate(label.split('\n')):centered_math(d,830+i*58,line,40,v.INK)
    elif vid=='geometry-symmetry-circular-ring':
        cx,cy=960,580
        d.ellipse((cx-210,cy-210,cx+210,cy+210),fill='#D4E8E1',outline=v.TEAL,width=5)
        d.ellipse((cx-84,cy-84,cx+84,cy+84),fill=v.BG,outline=v.TEAL,width=4)
        angles=[0] if scene==1 else [i*pi/8 for i in range(8)] if scene in (2,3) else []
        for a in angles:dashed(d,(cx-240*cos(a),cy+240*sin(a)),(cx+240*cos(a),cy-240*sin(a)),orange)
        if scene==4:dashed(d,(cx+130,cy-240),(cx+130,cy+240),orange)
        d.ellipse((cx-5,cy-5,cx+5,cy+5),fill=v.INK)
        label='Concentric ring, radii 2 cm and 5 cm' if scene==0 else 'This off-center line FAILS the mirror test.' if scene==4 else spec['displays'][scene]
        centered_math(d,870,label,42,v.INK)
    else:draw_card(spec,d,scene,p)


def symmetry_axes(points):
    # Candidate axes of a centered polygon: vertex directions and edge-midpoint directions.
    candidates=[]
    for a,b in zip(points,points[1:]+points[:1]):
        candidates.extend([a,((a[0]+b[0])/2,(a[1]+b[1])/2)])
    found=[]
    for x,y in candidates:
        norm=x*x+y*y
        if norm<1e-12:continue
        ux,uy=x/norm**.5,y/norm**.5
        reflected=[(2*(px*ux+py*uy)*ux-px,2*(px*ux+py*uy)*uy-py) for px,py in points]
        if all(any(abs(rx-px)<1e-8 and abs(ry-py)<1e-8 for px,py in points) for rx,ry in reflected):
            if not any(abs(ux*vy-uy*vx)<1e-8 for vx,vy in found):found.append((ux,uy))
    return found


def lessons(doc):
    assert len(symmetry_axes(OCTAGON))==8
    assert len(symmetry_axes(TRAPEZOID))==1
    assert len(symmetry_axes(LETTERS['I']))==2
    assert len(symmetry_axes(LETTERS['V']))==1
    assert len(symmetry_axes(LETTERS['F']))==0
    batch=make_lessons(SPECS,doc)
    for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:diagram(s,d,scene,p)
    return batch
