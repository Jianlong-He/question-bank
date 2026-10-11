"""Original examples for triangle classification and angle validity."""
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons,draw_card,centered_math
from angle_equation_lessons import triangle_points
import generate_sample_videos as v

SPECS=[
authored('geometry-triangle-classify-from-angles','Classify a triangle using its angles',
 'A triangle has angles 34°, 34° and 112°.\nClassify it by its angles and by its sides.',
 'Obtuse and isosceles',
 'A triangle has angles thirty-four, thirty-four, and one hundred twelve degrees. Classify it by its angles and by its sides.',[
 ('CHECK THE TOTAL','The three angles must add to one hundred eighty','34° + 34° + 112° = 180°',
  'First check that the angles total one hundred eighty. They do.'),
 ('CLASSIFY BY ANGLES','Compare the largest angle with ninety degrees','112° > 90° → obtuse triangle',
  'One angle exceeds ninety, so the triangle is obtuse. A right triangle has a ninety-degree angle. An acute triangle has all three angles below ninety.'),
 ('CLASSIFY BY SIDES','Equal angles have equal opposite sides','Two equal angles → two equal sides → isosceles',
  'Two angles are equal, so their opposite sides are equal. The triangle is isosceles.'),
 ('KEEP BOTH DESCRIPTIONS','Angle type and side type answer different questions','Obtuse and isosceles\nThree equal sides: equilateral; all different: scalene',
  'Our triangle is both obtuse and isosceles. Three equal angles give three equal sides, called equilateral. Three different angles give three different sides, called scalene.')],
 g(4,11,4,1),expression='34+34+112',value='180'),

authored('geometry-missing-angle-and-classification','Find a missing angle and classify the triangle',
 'Two angles of a triangle are 41° and 47°.\nFind the third angle, then classify the triangle\nas acute, right or obtuse.',
 '92 degrees; obtuse',
 'Two angles of a triangle are forty-one and forty-seven degrees. Find the third angle, then classify the triangle as acute, right, or obtuse.',[
 ('ADD THE KNOWN ANGLES','Start with the two given measures','41° + 47° = 88°',
  'Add the two known angles to get eighty-eight degrees.'),
 ('SUBTRACT FROM THE TOTAL','A triangle has one hundred eighty degrees','Third angle = 180° − 88° = 92°',
  'Subtract eighty-eight from one hundred eighty. The missing angle is ninety-two degrees.'),
 ('CLASSIFY','An angle greater than ninety makes the triangle obtuse','92° > 90° → obtuse',
  'Ninety-two is greater than ninety, so the triangle is obtuse. Check all three angles, including the one you just found.'),
 ('CHECK AND COMPARE','Use the largest angle to choose the type','41° + 47° + 92° = 180°\nLargest: below 90° acute; 90° right; above 90° obtuse',
  'The angles total one hundred eighty. If the largest were below ninety, the triangle would be acute. If it were exactly ninety, the triangle would be right.')],
 g(4,11,4,5),expression='180-41-47',value='92',equalities=[('41+47+92','180')]),

authored('geometry-equilateral-angle-classification','Classify an equilateral triangle by its angles',
 'A triangle has three sides, each 11 cm long.\nFind every angle and classify it by angles.',
 'Each angle is 60 degrees; acute triangle',
 'A triangle has three sides, each eleven centimetres long. Find every angle and classify it by angles.',[
 ('EQUAL SIDES','All three equal sides make an equilateral triangle','11 cm, 11 cm, 11 cm → equilateral',
  'All three sides are equal, so this is an equilateral triangle.'),
 ('EQUAL ANGLES','Equal sides have equal opposite angles','Three equal angles share 180°.',
  'The three opposite angles are equal too. They share a total of one hundred eighty degrees.'),
 ('DIVIDE EQUALLY','Divide the triangle total by three','180° ÷ 3 = 60° each',
  'Divide one hundred eighty by three. Each angle is sixty degrees.'),
 ('CLASSIFY BY ANGLES','Every angle is smaller than a right angle','60° < 90° → acute triangle',
  'All three angles are below ninety, so the triangle is acute. The side length does not change these angles. Equal angles also imply equal opposite sides.')],
 g(5,16,'1HW',5),expression='180/3',value='60'),

authored('geometry-triangle-angle-validity','Check whether given angles can form a triangle',
 'Can a triangle have angles of 102° and 91°?\nExplain using the angle total.',
 'No; the two angles already exceed 180 degrees',
 'Can a triangle have angles of one hundred two and ninety-one degrees? Explain using the angle total.',[
 ('THE REQUIREMENT','All three interior angles total one hundred eighty','A + B + C = 180°',
  'A triangle’s three interior angles must total one hundred eighty degrees, and each angle must be positive.'),
 ('ADD THE TWO ANGLES','Check how much of the total is already used','102° + 91° = 193°',
  'The two given angles already add to one hundred ninety-three degrees.'),
 ('FIND WHAT WOULD REMAIN','A negative third angle cannot belong to a triangle','180° − 193° = −13°',
  'Subtracting from one hundred eighty would leave negative thirteen degrees. That is impossible for an interior triangle angle.'),
 ('CONCLUDE','Two obtuse angles cannot fit in one triangle','No such triangle exists.',
  'So no such triangle exists. In particular, a triangle cannot contain two obtuse angles, because they would already exceed one hundred eighty degrees.')],
 g(9,17,'3Rev',4),expression='180-102-91',value='-13'),

authored('geometry-angle-type-benchmarks','Name an angle using benchmark measures',
 'An angle measures 125°.\nIs it acute, right, obtuse or straight?',
 'Obtuse',
 'An angle measures one hundred twenty-five degrees. Is it acute, right, obtuse, or straight?',[
 ('RIGHT ANGLE','A quarter turn measures ninety degrees','Right angle = 90°',
  'A right angle measures ninety degrees. A smaller positive angle is acute.'),
 ('STRAIGHT ANGLE','Opposite rays form a half turn','Straight angle = 180°',
  'Opposite rays form a straight angle, which is one hundred eighty degrees.'),
 ('COMPARE','One hundred twenty-five is between the two benchmarks','90° < 125° < 180°',
  'One hundred twenty-five is greater than ninety and less than one hundred eighty.'),
 ('NAME THE ANGLE','An angle between ninety and one hundred eighty is obtuse','125° → obtuse angle',
  'That makes it obtuse. Use ninety for a right angle and one hundred eighty for a straight angle when comparing other measures.')],
 g(4,11,2,7),expression='125-90',value='35'),
]

def diagram(spec,d,scene,p):
    vid=spec['video_id']
    if scene not in (1,2,3) or vid=='geometry-triangle-angle-validity':draw_card(spec,d,scene,p);return
    if vid=='geometry-angle-type-benchmarks':
        from math import sin,cos,radians
        angle=[90,180,125][scene-1];cx,cy,R=900,680,270
        d.line((cx,cy,cx+R,cy),fill=v.TEAL,width=5)
        d.line((cx,cy,cx+R*cos(radians(angle)),cy-R*sin(radians(angle))),fill=v.TEAL,width=5)
        d.arc((cx-85,cy-85,cx+85,cy+85),360-angle,360,fill='#B66F4E',width=4)
        v.text(d,(cx+(100 if angle==90 else 30),cy-130),f'{angle}°',36,v.INK,True,anchor='mm')
    else:
        angles={'geometry-triangle-classify-from-angles':[34,34,112],
                'geometry-missing-angle-and-classification':[41,47,92],
                'geometry-equilateral-angle-classification':[60,60,60]}[vid]
        scale=420 if vid=='geometry-equilateral-angle-classification' else 500
        pts=[(960-scale/2+x*scale,755-y*scale) for x,y in triangle_points(*angles[:2])]
        d.polygon(pts,fill='#D0E8E2',outline=v.TEAL,width=4)
        labels=[f'{a}°' for a in angles]
        if vid=='geometry-missing-angle-and-classification' and scene==1:labels[2]='?'
        if vid=='geometry-equilateral-angle-classification' and scene<3:labels=['?','?','?']
        for (x,y),label,(dx,dy) in zip(pts,labels,[(-20,28),(20,28),(0,-30)]):v.text(d,(x+dx,y+dy),label,33,v.INK,True,anchor='mm')
        if vid=='geometry-equilateral-angle-classification':
            v.text(d,(960,640),'all sides 11 cm',30,v.INK,True,anchor='mm')
    for i,line in enumerate(spec['displays'][scene].split('\n')):centered_math(d,845+i*60,line,40,v.TEAL)

def lessons(doc):
    assert 112>90 and 34==34 and 180-41-47==92 and 92>90
    assert 3*60==180 and 60<90 and 102+91>180 and 90<125<180
    batch=make_lessons(SPECS,doc)
    for spec in SPECS:v.DRAW[spec['video_id']]=lambda d,scene,p,s=spec:diagram(s,d,scene,p)
    return batch
