"""Concrete shape, line and angle examples for elementary geometry."""
from math import sin,cos,radians
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons,draw_card,centered_math
import generate_sample_videos as v

SPECS=[
authored('geometry-count-polygon-features','Count a polygon’s sides, corners and angles',
 'Look at the pentagon.\nHow many sides, corners and inside angles does it have?',
 '5 sides, 5 corners and 5 inside angles',
 'Look at the pentagon. How many sides, corners, and inside angles does it have?',[
 ('SIDES','Follow the boundary once','5 straight sides',
  'Start at the top and follow the boundary once. Count each straight side: one, two, three, four, five.'),
 ('CORNERS','A corner is where two sides meet','5 corners, also called vertices',
  'Count the places where neighbouring sides meet. There are five corners. Corners are also called vertices.'),
 ('ANGLES','Each corner makes one inside angle','5 inside angles',
  'Each corner makes one inside angle, so this shape has five inside angles.'),
 ('CHECK','A polygon has matching counts','5 sides = 5 corners = 5 inside angles',
  'All three counts match. For another polygon, draw it, follow its boundary, and count each side and corner once.')],
 g(2,8,1,6),expression='1+1+1+1+1',value='5'),

authored('geometry-quadrilateral-side-angle-classification','Use sides and angles to classify a quadrilateral',
 'A quadrilateral has four sides of 8 cm each.\nIts angles alternate between 65° and 115°.\nIs it a rhombus, rectangle or square?',
 'Rhombus; not a rectangle or square',
 'A quadrilateral has four sides of eight centimetres each. Its angles alternate between sixty-five and one hundred fifteen degrees. Is it a rhombus, rectangle, or square?',[
 ('EQUAL SIDES','Four equal sides identify a rhombus','8 cm = 8 cm = 8 cm = 8 cm',
  'All four sides are equal, so the quadrilateral is a rhombus.'),
 ('RIGHT ANGLES','A rectangle needs four right angles','65° and 115° are not 90°.',
  'A rectangle needs four right angles. These angles are not ninety degrees, so this is not a rectangle.'),
 ('SQUARE TEST','A square needs both equal sides and right angles','Equal sides alone do not make a square.',
  'A square needs four equal sides and four right angles. This shape fails the right-angle test.'),
 ('CONNECT THE FAMILIES','Check sides and angles separately','Four right angles → rectangle\nFour equal sides AND four right angles → square',
  'Our shape is a rhombus, but not a square. Four right angles make a rectangle. If all four sides are equal too, it is also a square.')],
 g(5,16,3,10),expression='65+115+65+115',value='360'),

authored('geometry-concave-polygon-test','Identify a concave polygon',
 'A pentagon has an inward corner measuring 270°.\nIs the polygon concave or convex?',
 'Concave',
 'A pentagon has an inward corner measuring two hundred seventy degrees. Is the polygon concave or convex?',[
 ('INSIDE THE POLYGON','Measure the angle through the polygon’s interior','Interior angle = 270°',
  'Use the angle inside the polygon. At the inward corner, that is the larger, two hundred seventy degree angle.'),
 ('COMPARE WITH A STRAIGHT ANGLE','A straight angle measures one hundred eighty degrees','270° > 180°',
  'Two hundred seventy is greater than one hundred eighty.'),
 ('NAME THE SHAPE TYPE','One interior angle above one hundred eighty is enough','Concave polygon',
  'A polygon with an interior angle greater than one hundred eighty degrees is concave. It has an inward dent.'),
 ('CONTRAST WITH CONVEX','A convex polygon has no inward corner','Convex: every interior angle is less than 180°.',
  'A convex polygon has every interior angle less than one hundred eighty degrees. The same test works for quadrilaterals and other simple polygons.')],
 g(5,16,2,2),expression='270-180',value='90'),

authored('geometry-intersecting-perpendicular-lines','Distinguish intersecting and perpendicular lines',
 'Two lines cross and form a 72° angle.\nAre they parallel, intersecting, or perpendicular?',
 'Intersecting, but not perpendicular or parallel',
 'Two lines cross and form a seventy-two degree angle. Are they parallel, intersecting, or perpendicular?',[
 ('DO THEY MEET?','Crossing lines are intersecting lines','The lines intersect.',
  'The lines cross, so they are intersecting. Parallel lines in a plane do not meet.'),
 ('CHECK THE ANGLE','Perpendicular lines meet at right angles','Perpendicular requires 90°.',
  'Perpendicular lines meet at right angles. Each angle at their intersection is ninety degrees.'),
 ('COMPARE','Seventy-two is not ninety','72° ≠ 90° → not perpendicular',
  'Seventy-two is not ninety, so these lines are not perpendicular.'),
 ('CONCLUDE','Perpendicular lines are a special kind of intersecting lines','Intersecting; not perpendicular',
  'The best description is intersecting. Every pair of perpendicular lines intersects, but crossing alone does not guarantee a right angle.')],
 g(4,11,3,3),expression='90-72',value='18'),

authored('geometry-halfway-angle','Find an angle halfway between two rays',
 'A turn starts at 0° and ends at 140°.\nWhat angle is exactly halfway through the turn?',
 '70 degrees',
 'A turn starts at zero degrees and ends at one hundred forty degrees. What angle is exactly halfway through the turn?',[
 ('TOTAL TURN','Find the change from start to finish','140° − 0° = 140°',
  'The full change is one hundred forty minus zero, or one hundred forty degrees.'),
 ('HALVE THE CHANGE','Halfway means two equal parts','140° ÷ 2 = 70°',
  'Divide by two to find half the change. Each part is seventy degrees.'),
 ('START AND MOVE HALFWAY','Add the half-turn amount to the starting angle','0° + 70° = 70°',
  'Start at zero and move seventy degrees. The halfway angle is seventy degrees.'),
 ('CHECK BOTH GAPS','The two gaps should be equal','70° − 0° = 70°\n140° − 70° = 70°',
  'The gaps on either side are both seventy degrees, so the angle is exactly halfway.')],
 g(4,12,'1HW',1),expression='(140-0)/2',value='70'),

authored('geometry-angle-increase','Find how much more an angle must open',
 'A door is open at an angle of 37°.\nIt needs to open to 86°. How much more must it turn?',
 '49 degrees',
 'A door is open at an angle of thirty-seven degrees. It needs to open to eighty-six degrees. How much more must it turn?',[
 ('START AND TARGET','Identify the two angle measures','Start: 37°; target: 86°',
  'The door starts at thirty-seven degrees and needs to reach eighty-six.'),
 ('FIND THE DIFFERENCE','Subtract the starting angle from the target','86° − 37°',
  'The extra turn is the target angle minus the starting angle.'),
 ('SUBTRACT','The needed increase is forty-nine degrees','86° − 37° = 49°',
  'Eighty-six minus thirty-seven equals forty-nine degrees.'),
 ('CHECK BY ADDING','Start plus extra turn should reach the target','37° + 49° = 86°',
  'Add forty-nine to the starting angle. We reach eighty-six, so the door needs to open forty-nine degrees more.')],
 g(4,12,3,7),expression='86-37',value='49',equalities=[('37+49','86')]),
]

def diagram(spec,d,scene,p):
    vid=spec['video_id']
    if scene not in (1,2,3) and not (scene==0 and vid=='geometry-count-polygon-features'):
        draw_card(spec,d,scene,p);return
    if vid=='geometry-count-polygon-features':
        pts=[(960+190*cos(radians(-90+72*i)),570+190*sin(radians(-90+72*i))) for i in range(5)]
        d.polygon(pts,fill='#D0E8E2',outline=v.TEAL,width=5)
        if scene in (1,2,3):
            for i,(x,y) in enumerate(pts):
                if scene==1:
                    nx,ny=pts[(i+1)%5];x,y=(x+nx)/2,(y+ny)/2
                dx,dy=x-960,y-570;mag=(dx*dx+dy*dy)**.5
                v.text(d,(x+dx/mag*26,y+dy/mag*26),str(i+1),30,v.INK,True,anchor='mm')
        if scene==0:
            centered_math(d,820,'Count the sides, corners and inside angles.',42,v.TEAL);return
    elif vid=='geometry-quadrilateral-side-angle-classification':
        a=240;dx=a*cos(radians(65));dy=a*sin(radians(65));x,y=760,730
        pts=[(x,y),(x+a,y),(x+a+dx,y-dy),(x+dx,y-dy)]
        d.polygon(pts,fill='#D0E8E2',outline=v.TEAL,width=4)
        v.text(d,(x+55,y-27),'65°',30,v.INK,True,anchor='mm')
        v.text(d,(x+a-25,y-50),'115°',30,v.INK,True,anchor='mm')
        v.text(d,(960,420),'four sides of 8 cm',32,v.INK,True,anchor='mm')
    elif vid=='geometry-concave-polygon-test':
        pts=[(760,740),(1160,740),(1160,390),(960,590),(760,390)]
        d.polygon(pts,fill='#D0E8E2',outline=v.TEAL,width=4)
        d.arc((905,535,1015,645),315,585,fill='#B66F4E',width=4)
        v.text(d,(960,690),'270° inside',32,v.INK,True,anchor='mm')
    else:
        cx,cy,R=880,690,280
        if vid=='geometry-intersecting-perpendicular-lines':
            cx,cy,R=960,555,210
            d.line((cx-R,cy,cx+R,cy),fill=v.TEAL,width=5)
            dx,dy=R*cos(radians(72)),R*sin(radians(72))
            d.line((cx-dx,cy+dy,cx+dx,cy-dy),fill=v.TEAL,width=5)
            v.text(d,(cx+115,cy-80),'72°',34,v.INK,True,anchor='mm')
        else:
            angles=[0,70,140] if vid=='geometry-halfway-angle' else [0,37,86]
            for i,a in enumerate(angles):
                end=(cx+R*cos(radians(a)),cy-R*sin(radians(a)))
                d.line((cx,cy,*end),fill='#B66F4E' if i==1 else v.TEAL,width=4)
                v.text(d,(cx+(R+40)*cos(radians(a)),cy-(R+40)*sin(radians(a))),f'{a}°',30,v.INK,True,anchor='mm')
    for i,line in enumerate(spec['displays'][scene].split('\n')):centered_math(d,845+i*58,line,40,v.TEAL)

def lessons(doc):
    assert 65+115==180 and 270>180 and 72!=90
    batch=make_lessons(SPECS,doc)
    for spec in SPECS:v.DRAW[spec['video_id']]=lambda d,scene,p,s=spec:diagram(s,d,scene,p)
    return batch
