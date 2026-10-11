"""Original right-triangle, sine-law, side-name and radian examples."""
from math import tan,sin,cos,radians,sqrt,isclose
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons,draw_card,centered_math
from angle_equation_lessons import triangle_points
import generate_sample_videos as v

SPECS=[
authored('trigonometry-rise-from-horizontal-distance','Find a rise using tangent',
 'A sight line makes a 37° angle above horizontal.\nThe horizontal distance is 18 m.\nFind the rise to the nearest tenth of a metre.',
 '13.6 metres',
 'A sight line makes a thirty-seven degree angle above horizontal. The horizontal distance is eighteen metres. Find the rise to the nearest tenth.',[
 ('LABEL THE SIDES','The rise is opposite; eighteen metres is adjacent','tan 37° = rise/18',
  'Relative to the given angle, the rise is the opposite side and the horizontal distance is adjacent. Tangent compares opposite to adjacent.'),
 ('ISOLATE THE RISE','Multiply both sides by eighteen','Rise = 18 × tan 37°',
  'Multiply both sides by eighteen to isolate the rise.'),
 ('USE DEGREE MODE','Keep calculator precision until the last step','tan 37° ≈ 0.753554\nRise ≈ 13.563973 m',
  'Set your calculator to degrees. Eighteen times tangent of thirty-seven degrees is about thirteen point five six four metres.'),
 ('ROUND','The hundredths digit rounds the tenths upward','Rise ≈ 13.6 m',
  'Round once at the end. To the nearest tenth, the rise is thirteen point six metres. The rise is measured from the horizontal sight-line level.')],
 g(10,9,3,9),expression='18*0.75355405',value='13.5639729'),

authored('geometry-pythagorean-converse-angle','Identify a right angle from three side lengths',
 'A triangle has side lengths 20 cm, 21 cm and 29 cm.\nFind the angle opposite the 29 cm side.',
 '90 degrees',
 'A triangle has side lengths twenty, twenty-one, and twenty-nine centimetres. Find the angle opposite the twenty-nine centimetre side.',[
 ('LONGEST SIDE','Compare the longest side with the other two','Longest side = 29 cm',
  'The longest side is twenty-nine. Test whether its square equals the sum of the other two squares.'),
 ('SQUARE THE SHORTER SIDES','Add their squares','20² + 21² = 400 + 441 = 841',
  'Twenty squared plus twenty-one squared is four hundred plus four hundred forty-one, or eight hundred forty-one.'),
 ('COMPARE WITH THE LONGEST','The squares match exactly','29² = 841 = 20² + 21²',
  'Twenty-nine squared is also eight hundred forty-one. The squares match exactly.'),
 ('USE THE CONVERSE','The triangle is right-angled opposite its longest side','Angle opposite 29 cm = 90°',
  'By the converse of the Pythagorean theorem, this is a right triangle. Its ninety-degree angle is opposite the longest side.')],
 g(11,8,1,8),expression='20**2+21**2',value='841',equalities=[('29**2','841')]),

authored('trigonometry-sine-law-known-pair','Choose and use the sine law with an opposite pair',
 'In triangle ABC, A = 30°, B = 45° and side a = 9 cm.\nFind side b, to the nearest tenth of a centimetre.',
 '12.7 centimetres',
 'In triangle A B C, angle A is thirty degrees, angle B is forty-five degrees, and side a is nine centimetres. Find side b to the nearest tenth.',[
 ('MATCH OPPOSITE PAIRS','Side a is opposite A; side b is opposite B','a/sin A = b/sin B',
  'We know a side and its opposite angle, so the sine law is useful. Keep each side paired with its opposite angle.'),
 ('SUBSTITUTE','Use the known pair and the requested side','9/sin 30° = b/sin 45°',
  'Pair nine with sine of thirty degrees, and b with sine of forty-five degrees.'),
 ('ISOLATE THE SIDE','Multiply by sine of forty-five degrees','b = 9 × sin 45° / sin 30°\nb = 9√2 ≈ 12.727922 cm',
  'Multiply by sine of forty-five. Using the exact special-angle values gives nine root two, about twelve point seven two eight centimetres.'),
 ('ROUND AND CHECK','A larger angle faces a longer side','b ≈ 12.7 cm; 45° > 30°, so b > a',
  'The answer is twelve point seven centimetres. Since forty-five degrees is larger than thirty, its opposite side should be longer than nine, and it is.')],
 g(11,8,1,10),expression='9**2*2',value='162'),

authored('geometry-opposite-side-and-angle-names','Identify an angle opposite a side',
 'Triangle ABC has AB = 7 cm, AC = 10 cm and BC = 12 cm.\nWhich angle is opposite the longest side?\nWhat lowercase letter names that side?',
 'Angle A; side a = BC',
 'Triangle A B C has A B equal to seven centimetres, A C equal to ten, and B C equal to twelve. Which angle is opposite the longest side, and what lowercase letter names that side?',[
 ('COMPARE LENGTHS','Twelve is the largest side length','BC = 12 cm is the longest side.',
  'Compare the three lengths. Twelve is the largest, so B C is the longest side.'),
 ('FIND THE UNUSED VERTEX','The opposite vertex is not an endpoint of the side','BC has endpoints B and C → opposite vertex A',
  'Side B C touches vertices B and C. The remaining vertex, A, lies opposite it.'),
 ('NAME THE ANGLE','The angle at the opposite vertex faces the side','Angle A is opposite BC.',
  'The angle at A faces side B C, so angle A is the required angle.'),
 ('LOWERCASE SIDE NAMES','Use the lowercase letter of the opposite angle','a opposite A; b opposite B; c opposite C\nHere, a = BC = 12 cm.',
  'A lowercase side letter matches its opposite uppercase angle. So B C is side a. Similarly, side b is opposite B, and side c is opposite C.')],
 g(11,8,'1Rev',1),expression='12-10',value='2'),

authored('trigonometry-radian-angle-quadrant','Locate a radian angle in a quadrant',
 'In standard position, which quadrant contains\nthe terminal side of angle 11π/6?',
 'Quadrant IV',
 'In standard position, which quadrant contains the terminal side of eleven pi over six radians?',[
 ('START ON THE POSITIVE X-AXIS','Positive angles turn counterclockwise','π radians = 180°',
  'Start on the positive x-axis and turn counterclockwise for a positive angle. Pi radians equals one hundred eighty degrees.'),
 ('CONVERT','Multiply by one hundred eighty over pi','(11π/6) × (180°/π) = 330°',
  'Multiply by one hundred eighty over pi. The pi factors cancel, giving three hundred thirty degrees.'),
 ('LOCATE THE ANGLE','Between 270° and 360°','270° < 330° < 360°',
  'Three hundred thirty degrees is between two hundred seventy and three hundred sixty.'),
 ('NAME THE QUADRANT','The terminal ray points right and down','Quadrant IV',
  'That places the terminal side in quadrant four, where x is positive and y is negative.')],
 g(11,8,2,10),expression='11/6*180',value='330'),
]

def diagram(spec,d,scene,p):
    vid=spec['video_id']
    if scene not in (1,2,3):draw_card(spec,d,scene,p);return
    if vid=='trigonometry-rise-from-horizontal-distance':
        x,y,s=710,750,26;rise=18*tan(radians(37));pts=[(x,y),(x+18*s,y),(x+18*s,y-rise*s)]
        d.polygon(pts,fill='#D0E8E2',outline=v.TEAL,width=4)
        d.line((x+18*s-20,y,x+18*s-20,y-20,x+18*s,y-20),fill=v.INK,width=3)
        for pt,label in [((x+9*s,y+30),'18 m'),((x+18*s+55,y-rise*s/2),'rise'),((x+95,y-28),'37°')]:v.text(d,pt,label,31,v.INK,True,anchor='mm')
    elif vid=='geometry-pythagorean-converse-angle':
        x,y,s=750,760,17;pts=[(x,y),(x+21*s,y),(x,y-20*s)]
        d.polygon(pts,fill='#D0E8E2',outline=v.TEAL,width=4)
        for pt,label in [((x+10.5*s,y+30),'21 cm'),((x-60,y-10*s),'20 cm'),((x+10.5*s+50,y-10*s-25),'29 cm'),((x+35,y-32),'?')]:v.text(d,pt,label,31,v.INK,True,anchor='mm')
    elif vid=='trigonometry-sine-law-known-pair':
        pts=[(710+x*500,745-y*500) for x,y in triangle_points(30,45)];a,b,c=pts
        d.polygon(pts,fill='#D0E8E2',outline=v.TEAL,width=4)
        for label,pt,dx,dy in [('A: 30°',a,0,30),('B: 45°',b,0,30),('C',c,0,-28)]:v.text(d,(pt[0]+dx,pt[1]+dy),label,31,v.INK,True,anchor='mm')
        v.text(d,((b[0]+c[0])/2+55,(b[1]+c[1])/2-10),'a = 9 cm',30,v.INK,True,anchor='mm')
        v.text(d,((a[0]+c[0])/2-40,(a[1]+c[1])/2-30),'b = ?',30,v.INK,True,anchor='mm')
    elif vid=='geometry-opposite-side-and-angle-names':
        # B=(0,0), C=(12,0), AB=7 and AC=10 determine A.
        ax=(7**2+12**2-10**2)/24;ay=sqrt(7**2-ax**2);s=37
        B=(730,745);C=(730+12*s,745);A=(730+ax*s,745-ay*s)
        d.polygon([A,B,C],fill='#D0E8E2',outline=v.TEAL,width=4)
        for label,pt,dx,dy in [('A',A,0,-28),('B',B,-25,20),('C',C,25,20)]:v.text(d,(pt[0]+dx,pt[1]+dy),label,33,v.INK,True,anchor='mm')
        for a,b,label,dx,dy in [(A,B,'7 cm',-45,0),(A,C,'10 cm',30,-20),(B,C,'12 cm',0,38)]:v.text(d,((a[0]+b[0])/2+dx,(a[1]+b[1])/2+dy),label,30,v.INK,True,anchor='mm')
    else:
        cx,cy,R=960,560,190
        d.ellipse((cx-R,cy-R,cx+R,cy+R),outline='#AECBC3',width=3)
        d.line((cx-R-50,cy,cx+R+50,cy),fill=v.INK,width=3);d.line((cx,cy-R-45,cx,cy+R+45),fill=v.INK,width=3)
        for a,label in [(0,'0°'),(90,'90°'),(180,'180°'),(270,'270°')]:
            dx,dy=(0,27) if a in (0,180) else (33,0)
            v.text(d,(cx+(R+30)*cos(radians(a))+dx,cy-(R+30)*sin(radians(a))+dy),label,27,v.INK,True,anchor='mm')
        end=(cx+R*cos(radians(330)),cy-R*sin(radians(330)));d.line((cx,cy,*end),fill=v.TEAL,width=5)
        points=[(cx+100*cos(radians(a)),cy-100*sin(radians(a))) for a in range(331)]
        d.line(points,fill='#B66F4E',width=4)
        ex,ey=points[-1];tx,ty=-sin(radians(330)),-cos(radians(330))
        d.polygon([(ex,ey),(ex-tx*16-ty*7,ey-ty*16+tx*7),(ex-tx*16+ty*7,ey-ty*16-tx*7)],fill='#B66F4E')
        v.text(d,(end[0]+35,end[1]+28),'330°',30,v.INK,True,anchor='mm')
    for i,line in enumerate(spec['displays'][scene].split('\n')):centered_math(d,845+i*58,line,40,v.TEAL)

def lessons(doc):
    assert round(18*tan(radians(37)),1)==13.6
    assert isclose(18*tan(radians(37)),13.5639729,abs_tol=1e-7)
    assert isclose(9*sin(radians(45))/sin(radians(30)),9*sqrt(2))
    assert round(9*sqrt(2),1)==12.7
    assert 7+10>12 and 20+21>29 and cos(radians(330))>0 and sin(radians(330))<0
    batch=make_lessons(SPECS,doc)
    for spec in SPECS:v.DRAW[spec['video_id']]=lambda d,scene,p,s=spec:diagram(s,d,scene,p)
    return batch
