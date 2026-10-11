"""Original circle calculations with exact checks and constructed diagrams."""
from math import sin, cos, radians, pi
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons, draw_card, centered_math
import generate_sample_videos as v

SPECS=[
authored('geometry-circumference','Find circumference from radius',
 'A circle has radius 13 cm.\nFind its circumference in terms of pi.','26π centimetres',
 'A circle has radius thirteen centimetres. Find the distance around it, leaving pi in your answer.',[
 ('CHOOSE THE FORMULA','Circumference is the distance around a circle','C = 2πr',
  'Circumference equals two times pi times the radius. Radius goes from the centre to the circle.'),
 ('SUBSTITUTE','Replace r with thirteen','C = 2 × π × 13',
  'Substitute thirteen for the radius. Keep pi as an exact factor.'),
 ('MULTIPLY','Two times thirteen is twenty-six','C = 26π cm',
  'Two times thirteen is twenty-six, so the circumference is twenty-six pi centimetres.'),
 ('CHECK WITH DIAMETER','Diameter is twice the radius','d = 26 cm; C = πd = 26π cm',
  'The diameter is twenty-six centimetres. Multiplying diameter by pi gives the same circumference. Use length units, not square units.')],
 g(10,11,5,7),expression='2*13',value='26'),

authored('geometry-circle-measures-from-circumference','Find radius, diameter and area from circumference',
 'A circle has circumference 30π cm.\nFind its radius, diameter and area.','Radius 15 cm; diameter 30 cm; area 225π cm²',
 'A circle has circumference thirty pi centimetres. Find its radius, diameter, and area.',[
 ('SET UP','Use the circumference formula','2πr = 30π',
  'The formula is two pi r. Set it equal to thirty pi.'),
 ('RECOVER THE RADIUS','Divide both sides by two pi','r = 30π ÷ 2π = 15 cm',
  'Divide both sides by two pi. The pi factors cancel, leaving a radius of fifteen centimetres.'),
 ('FIND THE DIAMETER','Double the radius','d = 2 × 15 = 30 cm',
  'Double the radius to get a diameter of thirty centimetres. Equivalently, divide the circumference by pi.'),
 ('FIND THE AREA','Square the radius, then multiply by pi','A = π × 15² = 225π cm²',
  'For area, square the radius and multiply by pi. Fifteen squared is two hundred twenty-five, so the area is two hundred twenty-five pi square centimetres.')],
 g(7,9,1,2),expression='30/2',value='15',equalities=[('15*2','30'),('15**2','225')]),

authored('geometry-circle-circumference-from-area','Find radius and circumference from area',
 'A circle has area 196π cm².\nFind its radius and circumference.','Radius 14 cm; circumference 28π cm',
 'A circle has area one hundred ninety-six pi square centimetres. Find its radius and circumference.',[
 ('AREA EQUATION','Start with pi times radius squared','πr² = 196π',
  'Use the area formula, pi times radius squared.'),
 ('CANCEL PI','Divide both sides by pi','r² = 196',
  'Dividing both sides by pi gives radius squared equals one hundred ninety-six.'),
 ('TAKE THE POSITIVE ROOT','Radius is a positive length','r = 14 cm, because 14² = 196',
  'Fourteen squared is one hundred ninety-six, so the radius is fourteen centimetres.'),
 ('FIND THE CIRCUMFERENCE','Substitute into two pi r','C = 2π × 14 = 28π cm',
  'Now multiply fourteen by two pi. The circumference is twenty-eight pi centimetres. Area used square units; circumference uses length units.')],
 g(7,9,2,2),expression='2*14',value='28',equalities=[('14**2','196')]),

authored('geometry-circumference-area-scaling','How a circumference multiplier changes area',
 'A circle’s circumference becomes 5 times as large.\nHow many times as large does its area become?','25 times as large',
 'A circle’s circumference becomes five times as large. How many times as large does its area become?',[
 ('RELATE CIRCUMFERENCE AND RADIUS','Two pi is a constant factor','C = 2πr',
  'Circumference is two pi times radius. Because two pi stays constant, radius changes by the same multiplier as circumference.'),
 ('SCALE THE RADIUS','Circumference times five means radius times five','New radius = 5r',
  'Multiplying the circumference by five makes the radius five times as large.'),
 ('SQUARE THE MULTIPLIER','Area uses radius squared','New area = π(5r)² = 25πr²',
  'Area depends on radius squared. Five squared is twenty-five.'),
 ('GENERAL RULE','Square a circumference multiplier to get the area multiplier','Circumference ×k → radius ×k → area ×k²',
  'The new area is twenty-five times the old area. In general, a circumference multiplier of k gives an area multiplier of k squared.')],
 g(7,9,1,4),expression='5**2',value='25',identities=[('(5*r)**2','25*r**2')]),

authored('geometry-circles-arcs','Find arc length using degrees',
 'A circle has radius 14 cm.\nFind the length of its 135° arc, in terms of pi.','21π/2 centimetres',
 'A circle has radius fourteen centimetres. Find the length of its one hundred thirty-five degree arc, in terms of pi.',[
 ('FRACTION OF A TURN','Divide the central angle by three hundred sixty','135/360 = 3/8',
  'One full turn is three hundred sixty degrees. This arc is three eighths of a full circle.'),
 ('WHOLE CIRCUMFERENCE','Use two pi r','C = 2π × 14 = 28π cm',
  'The entire circumference is twenty-eight pi centimetres.'),
 ('TAKE THE SAME FRACTION','Multiply the circumference by three eighths','s = (3/8) × 28π = 21π/2 cm',
  'Take three eighths of twenty-eight pi. The arc length is twenty-one pi over two centimetres.'),
 ('GENERAL FORMULA','Use this formula when the angle is in degrees','s = (θ/360) × 2πr',
  'For degrees, multiply the full circumference by the central angle divided by three hundred sixty. Arc length is a distance, so use length units.')],
 g(10,11,1,6),expression='135/360*2*14',value='21/2',equalities=[('135/360','3/8')]),

authored('geometry-arc-length-radians','Find arc length using radians',
 'A circle has radius 7 cm.\nIts central angle is 5/2 radians. Find the arc length.','35/2 centimetres',
 'A circle has radius seven centimetres. Its central angle is five halves radians. Find the arc length.',[
 ('CHECK THE ANGLE UNIT','The angle is already in radians','s = rθ',
  'When the central angle is in radians, arc length equals radius times angle.'),
 ('SUBSTITUTE','Multiply seven by five halves','s = 7 × (5/2)',
  'Substitute seven for the radius and five halves for the angle.'),
 ('CALCULATE','Multiply the numerator, then divide','s = 35/2 = 17.5 cm',
  'Seven times five is thirty-five. Dividing by two gives seventeen point five centimetres.'),
 ('KEEP THE UNITS STRAIGHT','Radius and arc length use the same length unit','Radians: s = rθ',
  'The arc length is thirty-five halves centimetres. The formula uses radians. If an angle is given in degrees, convert it or use the degree formula.')],
 g(10,11,1,2),expression='7*5/2',value='35/2'),

authored('geometry-sector-area-degrees','Find sector area using degrees',
 'A circle has radius 12 cm.\nFind the area of its 150° sector, in terms of pi.','60π square centimetres',
 'A circle has radius twelve centimetres. Find the area of its one hundred fifty degree sector, in terms of pi.',[
 ('FRACTION OF THE CIRCLE','Divide the central angle by three hundred sixty','150/360 = 5/12',
  'The sector covers five twelfths of the circle, because one hundred fifty divided by three hundred sixty simplifies to five twelfths.'),
 ('WHOLE CIRCLE AREA','Square the radius and multiply by pi','A = π × 12² = 144π cm²',
  'The whole circle has area one hundred forty-four pi square centimetres.'),
 ('TAKE THE FRACTION','Multiply the whole area by five twelfths','Sector area = (5/12) × 144π = 60π cm²',
  'Five twelfths of one hundred forty-four pi is sixty pi square centimetres.'),
 ('GENERAL FORMULA','Area uses pi r squared','Sector area = (θ/360) × πr²',
  'For a central angle in degrees, take that angle over three hundred sixty times the whole circle area. Use square units.')],
 g(10,11,1,7),expression='150/360*12**2',value='60'),

authored('geometry-sector-area-radians','Find sector area using radians',
 'A circle has radius 8 cm.\nFind the area of a sector with angle 3π/4 radians.','24π square centimetres',
 'A circle has radius eight centimetres. Find the area of a sector whose angle is three pi over four radians.',[
 ('CHECK THE UNIT','This angle is in radians','Sector area = (1/2)r²θ',
  'For an angle in radians, sector area equals one half times radius squared times the angle.'),
 ('SUBSTITUTE','Square eight before multiplying','Area = (1/2) × 64 × (3π/4)',
  'Eight squared is sixty-four. Substitute that and three pi over four into the formula.'),
 ('SIMPLIFY','Half of sixty-four is thirty-two','Area = 32 × (3π/4) = 24π cm²',
  'Half of sixty-four is thirty-two. Multiplying by three pi over four gives twenty-four pi square centimetres.'),
 ('CHECK THE FRACTION','A full turn is two pi radians','(3π/4)/(2π) = 3/8\n(3/8) × 64π = 24π cm²',
  'The angle is three eighths of a full turn. Three eighths of the whole circle area also gives twenty-four pi, confirming the answer.')],
 g(10,11,1,4),expression='1/2*8**2*3/4',value='24',equalities=[('(3/4)/2','3/8'),('3/8*64','24')]),
]

def circle_diagram(spec,d,scene,p):
    vid=spec['video_id']
    if scene not in (1,2,3) or vid=='geometry-circumference-area-scaling':
        draw_card(spec,d,scene,p);return
    cx,cy,R=960,560,190
    box=(cx-R,cy-R,cx+R,cy+R)
    info={
      'geometry-circumference':(360,'r = 13 cm'),
      'geometry-circle-measures-from-circumference':(360,'C = 30π cm'),
      'geometry-circle-circumference-from-area':(360,'A = 196π cm²'),
      'geometry-circles-arcs':(135,'r = 14 cm'),
      'geometry-arc-length-radians':(5/2*180/pi,'r = 7 cm'),
      'geometry-sector-area-degrees':(150,'r = 12 cm'),
      'geometry-sector-area-radians':(135,'r = 8 cm'),
    }
    angle,label=info[vid]
    d.ellipse(box,fill='white',outline=v.TEAL,width=4)
    if angle<360:
        if 'sector' in vid:d.pieslice(box,-90,-90+angle,fill='#D0E8E2')
        for a in [-90,-90+angle]:
            end=(cx+R*cos(radians(a)),cy+R*sin(radians(a)))
            d.line((cx,cy,*end),fill=v.TEAL,width=4)
        d.arc(box,-90,-90+angle,fill='#B66F4E',width=7)
        theta={'geometry-arc-length-radians':'5/2 rad','geometry-sector-area-radians':'3π/4 rad'}.get(vid,f'{angle}°')
        v.text(d,(cx+75,cy-70),theta,30,v.INK,True,anchor='mm')
    else:
        d.line((cx,cy,cx+R,cy),fill=v.TEAL,width=4)
    d.ellipse((cx-4,cy-4,cx+4,cy+4),fill=v.INK)
    v.text(d,(cx,cy+R+32),label,32,v.INK,True,anchor='mm')
    for i,line in enumerate(spec['displays'][scene].split('\n')):centered_math(d,830+i*62,line,44,v.TEAL)

def lessons(doc):
    batch=make_lessons(SPECS,doc)
    for spec in SPECS:v.DRAW[spec['video_id']]=lambda d,scene,p,s=spec:circle_diagram(s,d,scene,p)
    return batch
