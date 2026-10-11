"""Original illustrated examples for circle angles and related constructions."""
from math import sin,cos,radians,hypot
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons,draw_card,centered_math
import generate_sample_videos as v

SPECS=[
authored('geometry-circle-fraction-from-degrees','Find a circle fraction from its central angle',
 'A sector has central angle 150°.\nWhat fraction of the circle does it cover?','5/12 of the circle',
 'A sector has central angle one hundred fifty degrees. What fraction of the circle does it cover?',[
 ('THE WHOLE','A complete circle is one full turn','Full turn = 360°',
  'A full turn is three hundred sixty degrees. Compare the sector angle with that whole.'),
 ('PART OVER WHOLE','Put the sector angle over three hundred sixty','Fraction = 150/360',
  'Put one hundred fifty over three hundred sixty.'),
 ('SIMPLIFY','Divide numerator and denominator by thirty','150/360 = 5/12',
  'Both numbers divide by thirty, so the fraction simplifies to five twelfths.'),
 ('SAME FRACTION','The sector and its arc occupy the same fraction','Sector: 5/12 of circle area\nArc: 5/12 of circumference',
  'The sector is five twelfths of the circle’s area. Its arc also makes up five twelfths of the circumference.')],
 g(10,11,1,5),expression='150/360',value='5/12'),

authored('geometry-degrees-from-turn-fraction','Find degrees in a fraction of a turn',
 'A turn covers 2/5 of a full circle.\nHow many degrees is the turn?','144 degrees',
 'A turn covers two fifths of a full circle. How many degrees is the turn?',[
 ('START WITH THE WHOLE','One complete turn has three hundred sixty degrees','Full turn = 360°',
  'One full turn has three hundred sixty degrees.'),
 ('FIND ONE PART','Split the full turn into five equal parts','360° ÷ 5 = 72°',
  'Divide by five to find one fifth. Each equal part measures seventy-two degrees.'),
 ('TAKE TWO PARTS','Two fifths uses two of those equal parts','72° × 2 = 144°',
  'Two fifths uses two parts. Twice seventy-two is one hundred forty-four degrees.'),
 ('CHECK','Five equal parts still make a full turn','5 × 72° = 360°\n2/5 turn = 144°',
  'Five parts of seventy-two make three hundred sixty. Our two-part turn measures one hundred forty-four degrees.')],
 g(4,12,1,2),expression='360/5*2',value='144',equalities=[('5*72','360')]),

authored('geometry-radians-from-arc-length','Find a radian angle from arc length and radius',
 'A circle has radius 15 cm and arc length 10π cm.\nFind the arc’s central angle in radians.','2π/3 radians',
 'A circle has radius fifteen centimetres and an arc of length ten pi centimetres. Find the central angle in radians.',[
 ('RADIANS COMPARE TWO LENGTHS','Divide arc length by radius','θ = s/r',
  'An angle in radians is the arc length divided by the radius. Use the same length unit for both.'),
 ('SUBSTITUTE','Put ten pi over fifteen','θ = 10π/15',
  'Divide ten pi by fifteen.'),
 ('SIMPLIFY','Divide numerator and denominator by five','θ = 2π/3 radians',
  'The fraction simplifies to two pi over three radians.'),
 ('UNDERSTAND ONE RADIAN','An arc as long as the radius gives one radian','If s = r, then θ = r/r = 1 radian.',
  'One radian means the arc length equals the radius. Here the arc spans two pi over three radius lengths, so that is its angle in radians.')],
 g(10,11,6,7),expression='10/15',value='2/3',equalities=[('15*(2/3)','10')]),

authored('geometry-radians-from-turn-fraction','Convert a fraction of a turn to radians',
 'An arc is 3/10 of the circumference.\nFind its central angle in radians.','3π/5 radians',
 'An arc is three tenths of the circumference. Find its central angle in radians.',[
 ('ONE FULL TURN','A full circle measures two pi radians','Full turn = 2π radians',
  'A full circle measures two pi radians.'),
 ('USE THE FRACTION','Take three tenths of the full turn','θ = (3/10) × 2π',
  'Take three tenths of two pi, because the angle occupies the same fraction of a turn as the arc.'),
 ('SIMPLIFY','Multiply, then reduce the fraction','θ = 6π/10 = 3π/5 radians',
  'Three times two is six. Six tenths simplifies to three fifths, giving three pi over five radians.'),
 ('CHECK THE FRACTION','Divide the angle by one full turn','(3π/5)/(2π) = 3/10',
  'Divide our angle by two pi. We recover three tenths, which matches the original fraction.')],
 g(10,11,7,10),expression='3/10*2',value='3/5',equalities=[('(3/5)/2','3/10')]),

authored('geometry-central-angle-minor-arc','Relate a central angle to its minor arc',
 'A circle has a central angle of 88°.\nFind the measures of its minor and major arcs.','Minor arc 88°; major arc 272°',
 'A circle has a central angle of eighty-eight degrees. Find the measures of its minor and major arcs.',[
 ('LOCATE THE VERTEX','A central angle has its vertex at the centre','Central angle = 88°',
  'The angle’s vertex is at the centre. Its two radii cut off the minor arc.'),
 ('MATCH THE MINOR ARC','Its degree measure equals the central angle','Minor arc = 88°',
  'The minor arc has the same degree measure as the central angle: eighty-eight degrees.'),
 ('FIND THE REST','Subtract the minor arc from a full circle','Major arc = 360° − 88° = 272°',
  'The remaining major arc is three hundred sixty minus eighty-eight, or two hundred seventy-two degrees.'),
 ('CHECK','Both arcs together make one complete circle','88° + 272° = 360°',
  'The two arcs total three hundred sixty degrees. These are angle measures. An arc’s length would also depend on the radius.')],
 g(10,11,6,2),expression='360-88',value='272',equalities=[('88+272','360')]),

authored('geometry-regular-polygon-central-angle','Find equal central angles in an inscribed polygon',
 'Nine equally spaced points lie on a circle.\nJoin neighbouring points. Name the regular polygon\nand find the angle at the centre between neighbours.',
 'Regular nonagon; central angle 40°',
 'Nine equally spaced points lie on a circle. Join neighbouring points. Name the regular polygon and find the angle at the centre between neighbours.',[
 ('COUNT THE EQUAL SECTORS','Nine vertices make nine equal central angles','Number of sectors = 9',
  'Nine equally spaced vertices divide the full turn into nine equal sectors.'),
 ('DIVIDE A FULL TURN','Each central angle gets an equal share','360° ÷ 9 = 40°',
  'Divide three hundred sixty degrees by nine. Each central angle measures forty degrees.'),
 ('NAME THE POLYGON','It has nine equal sides and equal angles','9 sides → regular nonagon',
  'Joining the points makes a regular nine-sided polygon, called a nonagon. Equal central angles create equal chords.'),
 ('REVERSE THE METHOD','Recover the side count from the central angle','Number of sides = 360° ÷ 40° = 9',
  'To work backwards, divide three hundred sixty by the central angle. That gives the side count, which identifies the regular polygon.')],
 g(10,11,4,2),expression='360/9',value='40',equalities=[('360/40','9')]),

authored('geometry-perpendicular-bisector-property','Use the perpendicular bisector of a segment',
 'A is at (−6, 0), B at (6, 0), and P at (0, 8).\nExplain why P is on the perpendicular bisector\nof AB and compare distances PA and PB.',
 'The bisector is x = 0; PA = PB = 10 units',
 'A is at negative six, zero. B is at six, zero, and P is at zero, eight. Explain why P is on the perpendicular bisector of A B, and compare P A with P B.',[
 ('BISECT THE SEGMENT','The midpoint is halfway between the endpoints','Midpoint M = (0, 0)',
  'The midpoint is zero, zero. It lies six units from each endpoint.'),
 ('MAKE A RIGHT ANGLE','The vertical line through M is perpendicular to AB','Perpendicular bisector: x = 0',
  'A B is horizontal. The vertical line through its midpoint crosses it at ninety degrees, so it is the perpendicular bisector. P lies on that line.'),
 ('COMPARE THE DISTANCES','The two right triangles have matching legs','PA² = PB² = 6² + 8² = 100\nPA = PB = 10 units',
  'Both right triangles have legs six and eight. Each sloping distance is ten units.'),
 ('THE PROPERTY','Every point on the perpendicular bisector is equally far from A and B','PA = PB',
  'Any point on a segment’s perpendicular bisector is equally far from the two endpoints. The bisector crosses the segment at its midpoint.')],
 g(9,17,6,4),expression='6**2+8**2',value='100',equalities=[('10**2','100')]),

authored('geometry-arc-angle-proportionality','Compare arc lengths when the radius stays fixed',
 'In one circle, central angles measure 40° and 120°.\nHow does the longer arc’s length compare\nwith the shorter arc’s length?','The longer arc is 3 times as long',
 'In one circle, central angles measure forty degrees and one hundred twenty degrees. How does the longer arc compare with the shorter arc?',[
 ('KEEP THE RADIUS FIXED','Both arcs belong to the same circle','s = (θ/360) × 2πr',
  'Both arcs have the same radius. The arc-length formula multiplies the angle by the same constant in both cases.'),
 ('COMPARE THE ANGLES','Divide the larger angle by the smaller angle','120° ÷ 40° = 3',
  'One hundred twenty is three times forty.'),
 ('USE THE SAME MULTIPLIER','Arc length scales directly with central angle','Longer arc = 3 × shorter arc',
  'The longer arc is therefore three times as long. At a fixed radius, multiplying the angle multiplies arc length by the same amount.'),
 ('EQUAL ARCS','The relationship also works backwards','Same radius and equal arc lengths\n→ equal central angles',
  'The relationship works backwards too. In the same circle, equal arc lengths must have equal central angles.')],
 g(10,11,1,9),expression='120/40',value='3'),
]

def point(cx,cy,R,a):return (cx+R*cos(radians(a)),cy+R*sin(radians(a)))

def diagram(spec,d,scene,p):
    vid=spec['video_id']
    if scene not in (1,2,3):draw_card(spec,d,scene,p);return
    cx,cy,R=960,560,190;box=(cx-R,cy-R,cx+R,cy+R)
    if vid=='geometry-perpendicular-bisector-property':
        A=(720,720);B=(1200,720);M=(960,720);P=(960,400)
        d.line((*A,*B),fill=v.TEAL,width=5)
        d.line((960,340,960,775),fill='#B66F4E',width=4)
        d.line((*A,*P,*B),fill=v.TEAL,width=4)
        d.line((960,700,980,700,980,720),fill=v.INK,width=3)
        for label,pt,dx,dy in [('A (−6, 0)',A,-50,35),('B (6, 0)',B,50,35),('M (0, 0)',M,0,70),('P (0, 8)',P,80,-25)]:
            d.ellipse((pt[0]-4,pt[1]-4,pt[0]+4,pt[1]+4),fill=v.INK);v.text(d,(pt[0]+dx,pt[1]+dy),label,29,v.INK,True,anchor='mm')
    else:
        d.ellipse(box,fill='white',outline=v.TEAL,width=4)
        if vid=='geometry-regular-polygon-central-angle':
            pts=[point(cx,cy,R,-90+40*i) for i in range(9)]
            for pt in pts:d.line((cx,cy,*pt),fill='#AECBC3',width=3)
            d.polygon(pts,outline=v.TEAL,width=4)
            v.text(d,(cx,cy+R+32),'9 equal central angles',30,v.INK,True,anchor='mm')
        elif vid=='geometry-arc-angle-proportionality':
            for angle,col in [(120,'#B66F4E'),(40,v.TEAL)]:
                d.arc(box,-90,-90+angle,fill=col,width=9 if angle==120 else 5)
                pt=point(cx,cy,R,-90+angle);d.line((cx,cy,*pt),fill=col,width=3)
            d.line((cx,cy,cx,cy-R),fill=v.TEAL,width=3)
            v.text(d,(cx,cy+R+32),'40° and 120°, same radius',30,v.INK,True,anchor='mm')
        else:
            angle,label={
             'geometry-circle-fraction-from-degrees':(150,'150° sector'),
             'geometry-degrees-from-turn-fraction':(144,'2 of 5 equal sectors'),
             'geometry-radians-from-arc-length':(120,'r = 15 cm; arc = 10π cm'),
             'geometry-radians-from-turn-fraction':(108,'3 of 10 equal sectors'),
             'geometry-central-angle-minor-arc':(88,'Central angle = 88°'),
            }[vid]
            d.pieslice(box,-90,-90+angle,fill='#D0E8E2',outline=v.TEAL,width=3)
            if vid in ('geometry-degrees-from-turn-fraction','geometry-radians-from-turn-fraction'):
                count=5 if vid=='geometry-degrees-from-turn-fraction' else 10
                for i in range(count):d.line((cx,cy,*point(cx,cy,R,-90+360*i/count)),fill=v.TEAL,width=2)
            d.arc(box,-90,-90+angle,fill='#B66F4E',width=7)
            v.text(d,(cx,cy+R+32),label,30,v.INK,True,anchor='mm')
        d.ellipse((cx-4,cy-4,cx+4,cy+4),fill=v.INK)
    for i,line in enumerate(spec['displays'][scene].split('\n')):centered_math(d,835+i*63,line,42,v.TEAL)

def lessons(doc):
    assert hypot(6,8)==10
    assert 9*40==360 and 5*72==360 and 10*36==360
    batch=make_lessons(SPECS,doc)
    for spec in SPECS:v.DRAW[spec['video_id']]=lambda d,scene,p,s=spec:diagram(s,d,scene,p)
    return batch
