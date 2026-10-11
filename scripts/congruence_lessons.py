"""Distinct congruence methods, checked examples and explanatory diagrams."""
from math import sqrt,sin,cos,radians,hypot,isclose
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons,draw_card,centered_math
import generate_sample_videos as v

SPECS=[
authored('geometry-congruence','Compare segments and angles for congruence',
 'Two segments each measure 7.5 cm.\nTwo angles measure 43° and 47°.\nWhich pair is congruent?', 'The segments are congruent; the angles are not',
 'Two segments each measure seven point five centimetres. Two angles measure forty-three and forty-seven degrees. Which pair is congruent?',[
 ('SEGMENTS','Compare lengths using the same unit','7.5 cm = 7.5 cm',
  'Segments are congruent exactly when their lengths are equal. Both lengths are seven point five centimetres.'),
 ('POSITION','Turning or moving a segment does not change its length','The segment pair is congruent.',
  'The segments are congruent even if they point in different directions or sit in different places.'),
 ('ANGLES','Compare angle measures','43° ≠ 47°',
  'Angles are congruent exactly when their measures are equal. Forty-three and forty-seven are different.'),
 ('CONCLUSION','Match the measurement to the kind of object','Segments: equal length\nAngles: equal measure',
  'The segments are congruent, but these angles are not. Compare segment lengths and angle measures, rather than how large the drawings appear.')],
 g(9,17,1,3),expression='47-43',value='4'),

authored('geometry-congruence-corresponding-parts','Match corresponding parts of congruent triangles',
 'Triangle PQR is congruent to triangle UVW.\nPQ = x + 6 cm, UV = 19 cm, and angle R = 67°.\nFind x and angle W.', 'x = 13; angle W = 67 degrees',
 'Triangle P Q R is congruent to triangle U V W. P Q is x plus six centimetres, U V is nineteen, and angle R is sixty-seven degrees. Find x and angle W.',[
 ('MATCH THE ORDER','The congruence statement fixes the vertex pairs','P ↔ U     Q ↔ V     R ↔ W',
  'Match letters by their positions in the statement. P matches U, Q matches V, and R matches W.'),
 ('MATCH THE SIDE','Corresponding parts of congruent triangles are congruent','PQ ↔ UV, so x + 6 = 19',
  'P Q matches U V, so their lengths are equal. Set x plus six equal to nineteen.'),
 ('SOLVE','Subtract six from both sides','x = 19 − 6 = 13\nCheck: 13 + 6 = 19',
  'Subtract six to get x equals thirteen. Adding six back gives nineteen, as required.'),
 ('MATCH THE ANGLE','CPCTC justifies equality of corresponding parts','Angle W = angle R = 67°',
  'R matches W, so angle W is sixty-seven degrees. The justification is corresponding parts of congruent triangles are congruent, abbreviated C P C T C.')],
 g(9,17,2,9),equation=('x+6','19','x','13'),equalities=[('13+6','19')]),

authored('geometry-congruence-sss','Prove triangle congruence using SSS',
 'Two triangles each have side lengths 6, 8, and 11 cm.\nDoes this prove they are congruent?', 'Yes, by SSS',
 'Two triangles each have side lengths six, eight, and eleven centimetres. Does this prove that they are congruent?',[
 ('MATCH SIDES','Match each side to an equal side in the other triangle','6 ↔ 6     8 ↔ 8     11 ↔ 11',
  'There are three pairs of equal corresponding sides: six, eight, and eleven.'),
 ('COUNT THE FACTS','All three side pairs match','Side • Side • Side',
  'Three side lengths determine a triangle up to turning, sliding, or reflecting it.'),
 ('NAME THE CRITERION','SSS means side-side-side','The triangles are congruent by SSS.',
  'The criterion is side-side-side, or S S S. The triangles have the same shape and size.'),
 ('DISTINGUISH SIMILARITY','Congruence needs equal lengths, not just equal ratios','Equal side pairs → SSS congruence',
  'Equal ratios alone would establish similarity. For S S S congruence, the three corresponding side lengths themselves must be equal.')],
 g(9,17,1,5),expression='6+8-11',value='3'),

authored('geometry-congruence-sas','Prove triangle congruence using SAS',
 'Each of two triangles has sides 6 cm and 10 cm\nwith a 48° angle between them.\nWhich congruence criterion applies?', 'SAS',
 'Each of two triangles has sides six and ten centimetres with a forty-eight degree angle between them. Which congruence criterion applies?',[
 ('MATCH THE SIDES','Two corresponding side pairs are equal','6 cm ↔ 6 cm; 10 cm ↔ 10 cm',
  'The six-centimetre sides match, and the ten-centimetre sides match.'),
 ('CHECK THE ANGLE','The included angle lies between the two given sides','Included angle: 48° in both triangles',
  'The forty-eight degree angle is formed by those two sides. This is the included angle.'),
 ('NAME THE CRITERION','Side, included angle, side','SAS congruence',
  'Two equal side pairs and their equal included angles establish side-angle-side congruence.'),
 ('POSITION MATTERS','Check which sides actually form the given angle','The matched angle must be BETWEEN the sides.',
  'Always check the position of the angle. An angle away from the meeting point of the two given sides does not give the same S A S guarantee.')],
 g(9,17,2,5),expression='48',value='48'),

authored('geometry-congruence-asa','Prove triangle congruence using ASA',
 'In two triangles, matching angles are 42° and 73°.\nThe side joining those angle vertices is 9 cm in each.\nWhich congruence criterion applies?', 'ASA',
 'In two triangles, matching angles are forty-two and seventy-three degrees. The side joining those angle vertices is nine centimetres in each. Which criterion applies?',[
 ('MATCH TWO ANGLES','Both pairs of corresponding angles agree','42° ↔ 42°; 73° ↔ 73°',
  'The two angle pairs match. We also need a matching side to fix the size.'),
 ('LOCATE THE SIDE','The given side connects the two given angle vertices','The 9 cm side is the included side.',
  'The nine-centimetre side lies between the two given angles. It is the included side.'),
 ('NAME THE CRITERION','Angle, included side, angle','ASA congruence',
  'Two equal angles and their equal included side give angle-side-angle congruence, or A S A.'),
 ('WHY THE SIDE MATTERS','Equal angles alone determine shape, not size','Two angles alone → AA similarity\nAdd the equal included side → ASA congruence',
  'Two angles alone give angle-angle similarity. Adding the equal included side fixes the size and proves congruence.')],
 g(9,17,1,7),expression='180-42-73',value='65'),

authored('geometry-congruence-aas','Prove triangle congruence using AAS',
 'Two triangles have matching angles of 42° and 73°.\nIn each, the side opposite the 42° angle is 9 cm.\nWhich congruence criterion applies?', 'AAS',
 'Two triangles have matching angles of forty-two and seventy-three degrees. In each, the side opposite forty-two degrees is nine centimetres. Which criterion applies?',[
 ('MATCH TWO ANGLES','Both corresponding angle pairs are equal','42° ↔ 42°; 73° ↔ 73°',
  'Both angle pairs match, and a pair of corresponding sides also matches.'),
 ('LOCATE THE SIDE','The known side is opposite one of the given angles','9 cm: a nonincluded side',
  'The nine-centimetre side is opposite forty-two degrees. It is not the side between the two given angles.'),
 ('NAME THE CRITERION','Two angles and a corresponding nonincluded side','AAS congruence',
  'This is angle-angle-side congruence, or A A S.'),
 ('WHY IT WORKS','The third angles must match too','Third angle = 180° − 42° − 73° = 65°',
  'Each third angle is sixty-five degrees. Now the known side lies between two matching angles, so the result also follows from A S A.')],
 g(9,17,1,8),expression='180-42-73',value='65'),

authored('geometry-congruence-ssa-ambiguity','Show why SSA can give two different triangles',
 'Let angle A = 30°, AC = 10 cm and BC = 7 cm.\nB lies on the horizontal ray from A.\nMust these data determine one triangle?', 'No; there are two possible triangles',
 'Let angle A be thirty degrees, A C ten centimetres, and B C seven. B lies on the horizontal ray from A. Must these data determine one triangle?',[
 ('FIX TWO FEATURES','Draw the 30° ray and locate C ten centimetres from A','A and C are fixed; B lies on the baseline ray.',
  'Draw the thirty-degree angle and place C ten centimetres from A. B must lie on the horizontal ray.'),
 ('USE THE OTHER SIDE','B must also be seven centimetres from C','Draw a circle centred at C with radius 7 cm.',
  'A circle centred at C with radius seven shows every possible position for B.'),
 ('TWO INTERSECTIONS','Both marked positions lie on the required ray','B1 and B2 give different lengths AB.',
  'The circle crosses the ray twice. Both choices satisfy the given data, but their third side lengths are different.'),
 ('CONCLUSION','The angle is not included between the two given sides','SSA does not guarantee congruence.',
  'These are two noncongruent triangles with the same side-side-angle data. S S A therefore does not guarantee congruence in general. Some special data can still give just one triangle.')],
 g(9,17,1,9),expression='10*0.5',value='5'),

authored('geometry-congruence-parallelogram-diagonal','Prove the triangles across a parallelogram diagonal congruent',
 'PQRS is a parallelogram with diagonal PR.\nExplain why triangles PQR and RSP are congruent.',
 'Alternate interior angles and shared PR give ASA',
 'P Q R S is a parallelogram with diagonal P R. Explain why triangles P Q R and R S P are congruent.',[
 ('FIRST ANGLE PAIR','PQ is parallel to RS; PR is a transversal','Angle QPR = angle SRP',
  'P Q is parallel to R S. The diagonal makes equal alternate interior angles with these parallel sides.'),
 ('SECOND ANGLE PAIR','QR is parallel to SP; PR is a transversal','Angle QRP = angle SPR',
  'Q R is parallel to S P. The diagonal gives a second pair of equal alternate interior angles.'),
 ('SHARED SIDE','Both triangles contain the same diagonal','PR = RP',
  'The diagonal is the same segment in both triangles. It lies between the two matching angle pairs.'),
 ('CONCLUDE','Two angles and their included side agree','PQR and RSP are congruent by ASA',
  'The triangles are congruent by angle-side-angle. Match P with R, Q with S, and R with P when writing the statement.')],
 g(9,17,4,4),expression='1',value='1'),

authored('geometry-congruence-rigid-area','Use area preservation under rigid transformations',
 'A 7 cm by 11 cm rectangle is reflected,\nthen rotated. Find its final area.\nIs it congruent to the original?', '77 square centimetres; yes',
 'A seven by eleven centimetre rectangle is reflected, then rotated. Find its final area and decide whether it is congruent to the original.',[
 ('ORIGINAL AREA','Multiply perpendicular side lengths','Area = 7 × 11 = 77 cm²',
  'The rectangle covers seven times eleven, or seventy-seven square centimetres.'),
 ('RIGID MOVES','Reflections and rotations keep lengths and angles','The image is still a 7 cm by 11 cm rectangle.',
  'Reflection and rotation preserve lengths and angles. The image is still a rectangle with the same side lengths.'),
 ('FINAL AREA','Moving the figure does not change how much it covers','Final area = 77 cm²',
  'Its area remains seventy-seven square centimetres. Position and direction can change, but size and shape do not.'),
 ('GENERAL RULE','A sequence of rigid transformations gives a congruent image','Translations, rotations, reflections:\nlengths, angles and area are preserved.',
  'Any sequence of translations, rotations, and reflections preserves area as well as lengths and angles. The original and final figures are congruent.')],
 g(9,16,1,3),expression='7*11',value='77'),

authored('geometry-congruence-hypotenuse-leg','Prove right-triangle congruence using HL',
 'Two right triangles each have a hypotenuse of 17 cm\nand a leg of 8 cm. Must they be congruent?',
 'Yes, by HL; each other leg is 15 cm',
 'Two right triangles each have a hypotenuse of seventeen centimetres and a leg of eight centimetres. Must they be congruent?',[
 ('CHECK RIGHT ANGLES','HL applies specifically to right triangles','Both triangles have a 90° angle.',
  'First check that both triangles are right triangles. The hypotenuse is the side opposite the right angle.'),
 ('MATCH THE GIVEN SIDES','Equal hypotenuses and one equal leg pair','Hypotenuses: 17 cm; matching legs: 8 cm',
  'The hypotenuses match at seventeen centimetres, and one pair of legs matches at eight.'),
 ('NAME THE CRITERION','Hypotenuse-leg congruence','The triangles are congruent by HL.',
  'This proves hypotenuse-leg congruence, abbreviated H L.'),
 ('WHY IT WORKS','Pythagoras fixes the remaining leg in both triangles','Other leg² = 17² − 8² = 225\nOther leg = 15 cm',
  'Pythagoras gives the other leg squared as seventeen squared minus eight squared, or two hundred twenty-five. Each remaining leg is fifteen, so all three sides match.')],
 g(9,17,1,10),expression='17**2-8**2',value='225',equalities=[('15**2','225')]),

authored('geometry-angle-bisector-halves','Find the two equal angles made by a bisector',
 'Ray BD bisects angle ABC, which measures 78°.\nFind angles ABD and DBC.', '39 degrees each',
 'Ray B D bisects angle A B C, which measures seventy-eight degrees. Find the two smaller angles.',[
 ('BISECTOR','Bisect means divide into two equal parts','Angle ABD = angle DBC',
  'An angle bisector divides the original angle into two equal angles.'),
 ('TOTAL','The two smaller angles make the whole angle','x + x = 78°',
  'Let each smaller angle be x. Together they add to seventy-eight degrees.'),
 ('HALVE','Divide the original measure by two','x = 78° ÷ 2 = 39°',
  'Divide seventy-eight by two. Each smaller angle is thirty-nine degrees.'),
 ('CHECK','Equal parts must add back to the original measure','39° + 39° = 78°',
  'The two equal thirty-nine degree angles add back to seventy-eight. Whenever a ray bisects an angle, halve the original measure.')],
 g(9,17,5,9),expression='78/2',value='39',equalities=[('39+39','78')]),

authored('number-theory-congruence-difference','Check modular congruence using a difference',
 'Is 59 congruent to 11 modulo 8?', 'Yes; 59 − 11 = 48 is divisible by 8',
 'Is fifty-nine congruent to eleven modulo eight?',[
 ('MEANING','Modulo eight, congruent integers have the same remainder','59 ≡ 11 (mod 8)?',
  'Modular congruence means that two integers leave the same remainder when divided by the modulus.'),
 ('SUBTRACT','The difference must be divisible by the modulus','59 − 11 = 48',
  'Subtract eleven from fifty-nine. The difference is forty-eight.'),
 ('TEST DIVISIBILITY','Check for a whole-number quotient','48 ÷ 8 = 6',
  'Forty-eight divided by eight is six, a whole number. The difference is divisible by eight.'),
 ('CONFIRM','Both integers leave remainder three','59 = 7 × 8 + 3\n11 = 1 × 8 + 3',
  'Both numbers leave remainder three, so they are congruent modulo eight. In general, a is congruent to b modulo m exactly when m divides a minus b.')],
 ('worksheets/enrichment/number-theory 1/U1modular-arithmetic/E-NT1U1W1-1.csv','8'),
 expression='59-11',value='48',equalities=[('48/8','6'),('59%8','11%8')]),
]


def label(d,pt,name,dx=0,dy=0):v.text(d,(pt[0]+dx,pt[1]+dy),name,29,v.INK,True,anchor='mm')

def triangle(d,pts,names='ABC'):
    d.polygon(pts,fill='#D0E8E2',outline=v.TEAL,width=4)
    for pt,n,offset in zip(pts,names,[(-22,22),(22,22),(0,-25)]):label(d,pt,n,*offset)

def criteria_points(kind):
    if kind=='sss':return [(0,0),(11,0),((6**2+11**2-8**2)/22,sqrt(6**2-((6**2+11**2-8**2)/22)**2))]
    if kind=='sas':return [(0,0),(10,0),(6*cos(radians(48)),6*sin(radians(48)))]
    base=9 if kind=='asa' else 9*sin(radians(65))/sin(radians(42))
    ac=base*sin(radians(73))/sin(radians(65))
    return [(0,0),(base,0),(ac*cos(radians(42)),ac*sin(radians(42)))]


def diagram(spec,d,scene,p):
    vid=spec['video_id'];kind=vid.removeprefix('geometry-congruence-')
    if kind in ('sss','sas','asa','aas') and scene in (1,2):
        raw=criteria_points(kind)
        for x,names in [(500,'ABC'),(1110,'DEF')]:
            pts=[(x+xx*32,750-yy*32) for xx,yy in raw];triangle(d,pts,names)
            a,b,c=pts
            if kind in ('sss','sas'):
                label(d,((a[0]+b[0])/2,780),'11 cm' if kind=='sss' else '10 cm')
                label(d,((a[0]+c[0])/2-30,(a[1]+c[1])/2),'6 cm')
                if kind=='sss':label(d,((b[0]+c[0])/2+37,(b[1]+c[1])/2),'8 cm')
                else:label(d,(a[0]+60,a[1]-27),'48°')
            else:
                label(d,(a[0]+58,a[1]-22),'42°');label(d,(b[0]-38,b[1]-31),'73°')
                if kind=='asa':label(d,((a[0]+b[0])/2,785),'9 cm')
                else:label(d,((b[0]+c[0])/2+40,(b[1]+c[1])/2),'9 cm')
        centered_math(d,865,spec['displays'][scene],42,v.TEAL)
    elif kind=='ssa-ambiguity' and scene in (1,2,3):
        A=(550,760);C=(550+5*sqrt(3)*42,550);B1=(550+(5*sqrt(3)-sqrt(24))*42,760);B2=(550+(5*sqrt(3)+sqrt(24))*42,760)
        d.line((A[0],760,1350,760),fill=v.INK,width=4);d.line((*A,*C),fill=v.TEAL,width=5)
        label(d,A,'A',-25,24);label(d,C,'C',0,-25);label(d,(635,735),'30°');label(d,((A[0]+C[0])/2-32,(A[1]+C[1])/2-18),'10 cm')
        if scene>=2:
            # Only the lower arc is needed to show both baseline intersections.
            d.arc((C[0]-294,C[1]-294,C[0]+294,C[1]+294),0,180,fill='#B66F4E',width=3)
        if scene==3:
            for B,n in [(B1,'B1'),(B2,'B2')]:
                d.line((*C,*B),fill='#B66F4E',width=4);label(d,B,n,0,30)
                label(d,((C[0]+B[0])/2+20,(C[1]+B[1])/2),'7 cm')
        centered_math(d,925,spec['displays'][scene],39,v.TEAL)
    elif kind=='parallelogram-diagonal' and scene in (1,2,3):
        P,Q,R,S=(610,730),(1140,730),(1310,430),(780,430)
        d.polygon([P,Q,R,S],fill='#D0E8E2',outline=v.TEAL,width=5);d.line((*P,*R),fill='#B66F4E',width=5)
        for pt,n in zip([P,Q,R,S],'PQRS'):label(d,pt,n,-15,28 if n in 'PQ' else -25)
        centered_math(d,830,'PQ parallel to RS; QR parallel to SP',38,v.INK)
        centered_math(d,900,spec['displays'][scene],42,v.TEAL)
    elif kind=='hypotenuse-leg' and scene in (1,2):
        for x,names in [(460,'ABC'),(1090,'DEF')]:
            pts=[(x,745),(x+390,745),(x,537)];triangle(d,pts,names)
            d.line((x+18,745,x+18,727,x,727),fill=v.INK,width=3)
            label(d,(x-44,641),'8 cm');label(d,(x+220,623),'17 cm')
        centered_math(d,875,spec['displays'][scene],42,v.TEAL)
    elif vid=='geometry-angle-bisector-halves' and scene in (1,2,3):
        B=(670,775)
        def ray(a,r):return (B[0]+r*cos(radians(a)),B[1]-r*sin(radians(a)))
        for a,name in [(0,'A'),(39,'D'),(78,'C')]:
            endpoint=ray(a,390);d.line((*B,*endpoint),fill='#B66F4E' if a==39 else v.TEAL,width=5);label(d,endpoint,name,17,-12)
        label(d,B,'B',-23,22)
        for a in (19.5,58.5):label(d,ray(a,175),'39°' if scene==3 else 'x')
        centered_math(d,875,spec['displays'][scene],43,v.TEAL)
    else:draw_card(spec,d,scene,p)


def lessons(doc):
    for kind in ('sss','sas','asa','aas'):
        a,b,c=criteria_points(kind)
        lengths=[hypot(x[0]-y[0],x[1]-y[1]) for x,y in [(a,b),(b,c),(a,c)]]
        if kind=='sss':assert all(isclose(x,y) for x,y in zip(lengths,[11,8,6]))
        if kind=='sas':assert isclose(lengths[0],10) and isclose(lengths[2],6)
        if kind=='asa':assert isclose(lengths[0],9)
        if kind=='aas':assert isclose(lengths[1],9)
    c=(5*sqrt(3),5);b1=5*sqrt(3)-sqrt(24);b2=5*sqrt(3)+sqrt(24)
    assert 0<b1<b2 and isclose(hypot(*c),10)
    assert all(isclose(hypot(b-c[0],c[1]),7) for b in (b1,b2))
    batch=make_lessons(SPECS,doc)
    for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:diagram(s,d,scene,p)
    return batch
