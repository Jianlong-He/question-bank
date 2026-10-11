"""Circle scaling, triangle exterior angles and parallel-line relationships."""
from math import sin,cos,tan,radians,acos,degrees,isclose,hypot
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons,draw_card,centered_math
from angle_equation_lessons import triangle_points
import generate_sample_videos as v

SPECS=[
authored('geometry-cyclic-quadrilateral-opposite-angle','Find opposite angles in a cyclic quadrilateral',
 'All four vertices of quadrilateral ABCD lie on a circle.\nAngle A is 107°. Find the opposite angle C.','73 degrees',
 'All four vertices of quadrilateral A B C D lie on a circle. Angle A is one hundred seven degrees. Find the opposite angle C.',[
 ('CYCLIC QUADRILATERAL','All four vertices lie on one circle','A + C = 180°',
  'A quadrilateral with all four vertices on one circle is cyclic. Its opposite angles add to one hundred eighty degrees.'),
 ('SUBSTITUTE','A and C are opposite, not adjacent','107° + C = 180°',
  'A and C are opposite angles, so substitute one hundred seven for A.'),
 ('SUBTRACT','Remove the known angle from one hundred eighty','C = 180° − 107° = 73°',
  'Subtract one hundred seven from one hundred eighty. Angle C is seventy-three degrees.'),
 ('CHECK','Opposite angles are supplementary','107° + 73° = 180°',
  'The two opposite angles add to one hundred eighty, which checks the cyclic-quadrilateral rule.')],
 g(10,11,2,7),expression='180-107',value='73'),

authored('geometry-circle-fixed-angle-radius-scaling','Scale arc length and sector area with radius',
 'A sector keeps the same central angle.\nIts radius becomes 3 times as large.\nHow do arc length and sector area change?',
 'Arc length becomes 3 times as large; sector area becomes 9 times as large',
 'A sector keeps the same central angle, but its radius becomes three times as large. How do arc length and sector area change?',[
 ('FIX THE ANGLE','Only the radius changes','New radius = 3r; same angle θ',
  'The central angle stays fixed, so the sector remains the same fraction of its circle.'),
 ('ARC LENGTH','Arc length contains one radius factor','s = rθ → new arc length = 3rθ = 3s',
  'Using radians, arc length is radius times angle. Tripling the radius triples the arc length.'),
 ('SECTOR AREA','Area contains radius squared','A = (1/2)r²θ\nNew area = (1/2)(3r)²θ = 9A',
  'Sector area uses radius squared. Three squared is nine, so the area becomes nine times as large.'),
 ('GENERAL RULE','Length scales once; area scales with the square','Radius ×k, fixed angle:\narc length ×k; sector area ×k²',
  'At a fixed angle, multiply arc length by the radius multiplier, and multiply sector area by its square.')],
 g(10,11,1,10),expression='3**2',value='9',identities=[('(3*r)**2','9*r**2')]),

authored('geometry-complementary-angle-multiple','Find complementary angles when one is a multiple',
 'Two angles are complementary.\nThe larger is 5 times the smaller. Find both.','15° and 75°',
 'Two angles are complementary. The larger is five times the smaller. Find both angles.',[
 ('CHOOSE A VARIABLE','Let x represent the smaller angle','Smaller = x; larger = 5x',
  'Let the smaller angle be x. The larger is five x.'),
 ('ADD TO NINETY','Complementary angles total ninety degrees','x + 5x = 90 → 6x = 90',
  'The two angles add to ninety degrees. Combining them gives six x equals ninety.'),
 ('FIND BOTH ANGLES','Divide by six, then multiply by five','x = 15°; 5x = 75°',
  'Divide by six. The smaller angle is fifteen degrees, and the larger is five times fifteen, or seventy-five degrees.'),
 ('CHECK','Check the sum and the multiplier','15° + 75° = 90°\n75° = 5 × 15°',
  'The angles add to ninety, and seventy-five is five times fifteen. Both conditions hold.')],
 g(7,9,3,3),equation=('x+5*x','90','x','15'),equalities=[('5*15','75'),('15+75','90')]),

authored('geometry-triangle-exterior-angle','Find a remote interior angle from an exterior angle',
 'A triangle has an exterior angle of 143°.\nOne remote interior angle is 58°.\nFind the other remote interior angle.','85 degrees',
 'A triangle has an exterior angle of one hundred forty-three degrees. One remote interior angle is fifty-eight degrees. Find the other remote interior angle.',[
 ('EXTERIOR ANGLE RULE','Use the two interior angles away from the exterior vertex','Exterior angle = sum of remote interior angles',
  'An exterior angle equals the sum of the two interior angles away from its vertex. These are the remote interior angles.'),
 ('WRITE THE EQUATION','The remote angles add to one hundred forty-three','58° + x = 143°',
  'Fifty-eight plus the missing angle must equal one hundred forty-three.'),
 ('SUBTRACT','Subtract the known remote angle','x = 143° − 58° = 85°',
  'Subtract fifty-eight to get eighty-five degrees.'),
 ('CHECK USING THE TRIANGLE','The adjacent interior angle is supplementary to the exterior','Adjacent angle = 180° − 143° = 37°\n58° + 85° + 37° = 180°',
  'The interior angle beside the exterior angle is thirty-seven degrees. All three triangle angles now add to one hundred eighty.')],
 g(8,5,1,7),expression='143-58',value='85',equalities=[('180-143','37'),('58+85+37','180')]),

authored('geometry-parallel-corresponding-angles','Use corresponding angles on parallel lines',
 'A transversal crosses two parallel lines.\nThe upper-right angle at the first intersection is 64°.\nFind the upper-right angle at the second intersection.','64 degrees',
 'A transversal crosses two parallel lines. The upper-right angle at the first intersection is sixty-four degrees. Find the upper-right angle at the second intersection.',[
 ('MATCH POSITIONS','Look in the same corner at each intersection','Upper-right ↔ upper-right',
  'Look at the same corner at each intersection. These angles are in corresponding positions.'),
 ('CHECK PARALLEL LINES','Corresponding angles are equal when the lines are parallel','Corresponding angle = 64°',
  'Because the two lines are parallel, their corresponding angles are equal.'),
 ('TRANSFER THE MEASURE','The second upper-right angle has the same measure','x = 64°',
  'The second upper-right angle is also sixty-four degrees.'),
 ('RECOGNIZE THE PATTERN','The position stays the same at both crossings','Parallel lines → equal corresponding angles',
  'Corresponding means the same relative position. Check both the matching corners and the parallel-line condition.')],
 g(8,5,2,1),expression='64',value='64'),

authored('geometry-parallel-alternate-angles','Use alternate angles on parallel lines',
 'Two parallel lines are cut by a transversal.\nOne interior angle is 117°.\nFind the alternate interior angle.','117 degrees',
 'Two parallel lines are cut by a transversal. One interior angle is one hundred seventeen degrees. Find the alternate interior angle.',[
 ('INSIDE THE PARALLEL LINES','Interior angles lie between the two lines','Choose the angle inside the strip.',
  'Interior angles lie in the strip between the parallel lines.'),
 ('OPPOSITE SIDES OF THE TRANSVERSAL','Alternate angles switch sides','Alternate interior angles are equal.',
  'Alternate interior angles sit on opposite sides of the transversal. When the lines are parallel, these angles are equal.'),
 ('USE EQUALITY','Keep the given angle measure','x = 117°',
  'The other alternate interior angle is one hundred seventeen degrees.'),
 ('EXTERIOR PAIRS','The same equality holds for alternate exterior angles','Parallel lines:\nalternate interior equal; alternate exterior equal',
  'Alternate exterior angles lie outside the parallel lines on opposite sides of the transversal. They are equal too.')],
 g(8,5,1,6),expression='117',value='117'),

authored('geometry-parallel-same-side-interior','Find a same-side interior angle on parallel lines',
 'A transversal crosses two parallel lines.\nOne interior angle is 71°. Find its same-side\ninterior partner at the other intersection.','109 degrees',
 'A transversal crosses two parallel lines. One interior angle is seventy-one degrees. Find its same-side interior partner at the other intersection.',[
 ('LOCATE THE PAIR','Both angles are inside and on the same side of the transversal','Same-side interior angles',
  'Both angles lie between the parallel lines, on the same side of the transversal.'),
 ('USE THE SUM','For parallel lines, this pair is supplementary','71° + x = 180°',
  'Same-side interior angles add to one hundred eighty degrees when the lines are parallel.'),
 ('SUBTRACT','Subtract seventy-one from one hundred eighty','x = 180° − 71° = 109°',
  'Subtract seventy-one. The partner angle is one hundred nine degrees.'),
 ('CHECK','Their sum must be one hundred eighty','71° + 109° = 180°',
  'The angles add to one hundred eighty. Same-side interior angles use a sum, unlike equal corresponding or alternate pairs.')],
 g(8,5,'3Rev',5),expression='180-71',value='109'),
]

def cyclic_points():return [(cos(radians(a)),sin(radians(a))) for a in [0,70,180,284]]
def diagram(spec,d,scene,p):
    vid=spec['video_id']
    special=vid in {'geometry-cyclic-quadrilateral-opposite-angle','geometry-triangle-exterior-angle','geometry-parallel-corresponding-angles','geometry-parallel-alternate-angles','geometry-parallel-same-side-interior'}
    if scene not in (1,2,3) or not special:draw_card(spec,d,scene,p);return
    if vid=='geometry-cyclic-quadrilateral-opposite-angle':
        cx,cy,R=960,570,185;pts=[(cx+x*R,cy+y*R) for x,y in cyclic_points()]
        d.ellipse((cx-R,cy-R,cx+R,cy+R),outline=v.TEAL,width=4);d.polygon(pts,fill='#D0E8E2',outline=v.TEAL,width=3)
        for label,(x,y),(dx,dy) in zip('ABCD',pts,[(25,0),(15,25),(-25,0),(0,-25)]):v.text(d,(x+dx,y+dy),label,32,v.INK,True,anchor='mm')
        v.text(d,(cx+R-60,cy),'107°',31,v.INK,True,anchor='mm');v.text(d,(cx-R+40,cy),'x',32,v.INK,True,anchor='mm')
    elif vid=='geometry-triangle-exterior-angle':
        pts=[(710+x*420,730-y*420) for x,y in triangle_points(58,37)]
        d.polygon(pts,fill='#D0E8E2',outline=v.TEAL,width=4)
        B=pts[1];d.line((*B,B[0]+190,B[1]),fill=v.TEAL,width=4)
        for text,pt,dx,dy in [('58°',pts[0],25,-22),('x',pts[2],0,-30),('143°',B,75,-55)]:v.text(d,(pt[0]+dx,pt[1]+dy),text,34,v.INK,True,anchor='mm')
        d.arc((B[0]-65,B[1]-65,B[0]+65,B[1]+65),217,360,fill='#B66F4E',width=4)
    else:
        theta={'geometry-parallel-corresponding-angles':64,'geometry-parallel-alternate-angles':63,'geometry-parallel-same-side-interior':71}[vid]
        y1,y2,x1=430,690,1030;x2=x1-(y2-y1)/tan(radians(theta))
        for y in [y1,y2]:
            d.line((610,y,1310,y),fill=v.TEAL,width=4)
            # Matching chevrons mark the parallel lines.
            d.line((640,y-9,654,y,640,y+9),fill=v.TEAL,width=3)
        def xx(y):return x1-(y-y1)/tan(radians(theta))
        d.line((xx(340),340,xx(775),775),fill='#B66F4E',width=4)
        if vid=='geometry-parallel-corresponding-angles':labels=[(x1+70,y1-40,'64°'),(x2+70,y2-40,'x')]
        elif vid=='geometry-parallel-alternate-angles':labels=[(x1+65,y1+50,'117°'),(x2-70,y2-45,'x')]
        else:labels=[(x1-70,y1+45,'71°'),(x2-70,y2-45,'x')]
        for x,y,label in labels:v.text(d,(x,y),label,34,v.INK,True,anchor='mm')
    for i,line in enumerate(spec['displays'][scene].split('\n')):centered_math(d,840+i*60,line,40,v.TEAL)

def lessons(doc):
    pts=cyclic_points()
    for i,want in [(0,107),(2,73)]:
        a,b,c=pts[(i-1)%4],pts[i],pts[(i+1)%4]
        u=(a[0]-b[0],a[1]-b[1]);w=(c[0]-b[0],c[1]-b[1])
        angle=degrees(acos((u[0]*w[0]+u[1]*w[1])/(hypot(*u)*hypot(*w))))
        assert isclose(angle,want,abs_tol=1e-8)
    batch=make_lessons(SPECS,doc)
    for spec in SPECS:v.DRAW[spec['video_id']]=lambda d,scene,p,s=spec:diagram(s,d,scene,p)
    return batch
