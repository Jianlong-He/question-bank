"""Shared dilation methods with fresh numerical examples and exact checks."""
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons,draw_card,centered_math
import generate_sample_videos as v

SPECS=[
authored('geometry-dilation-image-length','Find a length after dilation',
 'A segment is 13 cm long. A dilation has\nscale factor 0.7. Find the image length.','9.1 cm',
 'A segment is thirteen centimetres long. A dilation has scale factor zero point seven. Find the image length.',[
 ('RULE','Multiply the original length by the scale factor','Image length = k × original length',
  'The scale factor tells us what to multiply each length by. This applies to sides, radii, altitudes, and distances from the center.'),
 ('SUBSTITUTE','Use the factor in the stated direction','Image length = 0.7 × 13',
  'We are going from the original to the image, so multiply thirteen by zero point seven.'),
 ('CALCULATE','Seven tenths of thirteen','Image length = 9.1 cm',
  'Seven tenths of thirteen is nine point one centimetres.'),
 ('CHECK','A positive factor below one makes lengths smaller','9.1 < 13; 9.1 ÷ 13 = 0.7',
  'The factor is between zero and one, so the image should be shorter. Dividing the new length by thirteen recovers the scale factor.')],
 g(7,8,1,1),expression='13*0.7',value='9.1',equalities=[('9.1/13','0.7')]),

authored('geometry-dilation-length-ratio','Find a scale factor from corresponding lengths',
 'An original side is 22 cm. Its corresponding\nimage side is 33 cm. Find the scale factor.','1.5',
 'An original side is twenty-two centimetres, and its corresponding image side is thirty-three centimetres. Find the scale factor.',[
 ('DIRECTION','Put the destination length on top','k = image length ÷ original length',
  'Use image length divided by original length. Make sure both measurements use the same units.'),
 ('SUBSTITUTE','The image is thirty-three centimetres','k = 33 ÷ 22',
  'The image length goes on top, so divide thirty-three by twenty-two.'),
 ('SIMPLIFY','Reduce the ratio','k = 3/2 = 1.5',
  'The fraction reduces to three halves, or one point five.'),
 ('CHECK','Multiply the original by the factor','22 × 1.5 = 33',
  'Multiplying twenty-two by one point five gives thirty-three. Reversing the direction would use the reciprocal, two thirds.')],
 g(7,8,1,3),expression='33/22',value='1.5',equalities=[('22*1.5','33')]),

authored('geometry-dilation-origin-coordinates','Dilate a point about the origin',
 'Dilate P(−8, 6) about the origin\nwith scale factor 3/4. Find P′.','(−6, 4.5)',
 'Dilate the point negative eight, six about the origin with scale factor three quarters. Find its image.',[
 ('COORDINATE RULE','Multiply both coordinates by the scale factor','(x, y) → (kx, ky)',
  'For a dilation centered at the origin, multiply both coordinates by the same scale factor.'),
 ('X-COORDINATE','Keep the sign when multiplying','x′ = (3/4)(−8) = −6',
  'Three quarters of negative eight is negative six.'),
 ('Y-COORDINATE','Apply the same factor to y','y′ = (3/4)(6) = 4.5',
  'Three quarters of six is four point five. Even if the question asks for only one coordinate, the rule applies to both.'),
 ('CHECK','The image stays on the ray from the origin','P′ = (−6, 4.5)',
  'The image is negative six, four point five. A positive factor below one moves it closer to the origin on the same ray.')],
 g(8,6,9,1),expression='(3/4)*(-8)',value='-6',equalities=[('(3/4)*6','4.5')]),

authored('geometry-dilation-coordinate-factor','Find a dilation factor from a point and its image',
 'A dilation about the origin sends\nP(−4, 10) to P′(−6, 15). Find k.','1.5',
 'A dilation about the origin sends negative four, ten to negative six, fifteen. Find the scale factor.',[
 ('COMPARE X','Divide the image coordinate by the original','k = −6 ÷ (−4)',
  'Divide the image x-coordinate by the original x-coordinate. Negative six divided by negative four is positive one point five.'),
 ('CHECK Y','Both nonzero coordinates must give the same factor','15 ÷ 10 = 1.5',
  'Check the y-coordinates too. Fifteen divided by ten also gives one point five.'),
 ('VERIFY THE POINT','Multiply both original coordinates','1.5(−4, 10) = (−6, 15)',
  'Multiplying both original coordinates by one point five reproduces the image.'),
 ('ZERO COORDINATES','Do not divide by zero','k = 1.5; use a nonzero original coordinate',
  'Use a nonzero original coordinate to find the factor. A zero coordinate remains zero. The origin maps to itself and cannot determine the factor alone.')],
 g(8,6,10,3),expression='(-6)/(-4)',value='1.5',equalities=[('15/10','1.5')]),

authored('geometry-dilation-perimeter','Scale a perimeter by the length factor',
 'A polygon has perimeter 26 cm. It is dilated\nwith scale factor 1.2. Find its new perimeter.','31.2 cm',
 'A polygon has perimeter twenty-six centimetres. It is dilated with scale factor one point two. Find its new perimeter.',[
 ('ADD THE SIDES','Perimeter is a sum of lengths','P = a + b + c + …',
  'Perimeter is the sum of all side lengths.'),
 ('SCALE EVERY SIDE','Factor the same multiplier out of the sum','P′ = ka + kb + kc + … = kP',
  'Every side is multiplied by the same factor. Factoring it out shows that the whole perimeter uses that factor too.'),
 ('CALCULATE','Multiply the original perimeter','P′ = 1.2 × 26 = 31.2 cm',
  'Multiply twenty-six by one point two. The new perimeter is thirty-one point two centimetres.'),
 ('CHECK','Perimeter uses the length factor','31.2 ÷ 26 = 1.2',
  'The ratio of new perimeter to old perimeter is one point two. Use the length factor for perimeter; square the factor only for area.')],
 g(8,6,10,4),expression='26*1.2',value='31.2',identities=[('k*a+k*b+k*c','k*(a+b+c)')]),

authored('geometry-dilation-angle-preservation','Find an angle after dilation',
 'A triangle has an 83° angle. It is dilated\nwith scale factor 2.2. Find the image angle.','83 degrees',
 'A triangle has an eighty-three degree angle. It is dilated with scale factor two point two. Find the image angle.',[
 ('RECOGNIZE','Dilation scales lengths uniformly','Every length is multiplied by 2.2',
  'Dilation multiplies every length by the same factor, so the shape stays similar.'),
 ('ANGLE RULE','Corresponding angles stay equal','Image angle = original angle',
  'Uniform scaling preserves corresponding angles. An angle measures the opening between two rays, not the lengths along them.'),
 ('ANSWER','Keep the original angle measure','Image angle = 83°',
  'The image angle is still eighty-three degrees. Do not multiply the angle by the scale factor.'),
 ('CHECK','The same rule applies to a reduction','Enlargement or reduction: angles are preserved',
  'A reduction also keeps corresponding angles equal. For any positive scale factor, the size may change while the angles stay the same.')],
 g(8,6,10,2),expression='83',value='83'),

authored('geometry-dilation-enlargement-reduction','Classify a dilation from its positive scale factor',
 'One dilation uses k = 0.65. Another uses k = 2.2.\nClassify each as an enlargement or reduction.',
 '0.65: reduction; 2.2: enlargement',
 'One dilation uses factor zero point six five. Another uses two point two. Classify each as an enlargement or reduction.',[
 ('COMPARE WITH ONE','Use positive scale factors','0 < k < 1: reduction\nk > 1: enlargement',
  'A positive factor below one reduces lengths. A factor greater than one enlarges them.'),
 ('FIRST FACTOR','Try an original length of seven','0.65 × 7 = 4.55 → reduction',
  'Zero point six five times seven is four point five five. The shorter result confirms a reduction.'),
 ('SECOND FACTOR','Use the same original length','2.2 × 7 = 15.4 → enlargement',
  'Two point two times seven is fifteen point four. The longer result confirms an enlargement.'),
 ('SPECIAL CASE','Multiplying by one changes nothing','k = 1: identity dilation',
  'With factor one, every point stays where it was. That is the identity dilation. These size changes using one uniform factor are called dilations.')],
 g(9,15,4,4),expression='0.65*7',value='4.55',equalities=[('2.2*7','15.4'),('1*7','7')]),

authored('geometry-dilation-similarity-congruence','Distinguish similarity and congruence after dilation',
 'A triangle has sides 7, 9, and 11 cm.\nDilate it by k = 1.8. Is it similar, congruent, or both?',
 'Similar, but not congruent',
 'A triangle has sides seven, nine, and eleven centimetres. Dilate it by factor one point eight. Is the image similar, congruent, or both?',[
 ('LENGTHS','Multiply every side by the same factor','Image sides: 12.6, 16.2, 19.8 cm',
  'The new sides are twelve point six, sixteen point two, and nineteen point eight centimetres.'),
 ('SIMILARITY','Equal angles and proportional corresponding lengths','Same shape → similar',
  'Corresponding angles stay equal and the sides are proportional, so the triangles are similar.'),
 ('CONGRUENCE','Congruent figures also have equal corresponding lengths','Different size → not congruent; not rigid',
  'Their lengths differ, so they are not congruent. This dilation is not rigid, because rigid transformations preserve distances and angles.'),
 ('FACTOR ONE','For positive k, congruence occurs when k equals one','k = 1: identical image; similar AND congruent',
  'With factor one, every point stays fixed. This identity dilation gives both similarity and congruence. For positive factors other than one, nonzero side lengths change.')],
 g(8,6,10,10),expression='7*1.8',value='12.6',equalities=[('9*1.8','16.2'),('11*1.8','19.8')]),

authored('geometry-dilation-center-line','Track the center and a line through it',
 'A dilation centered at O(0, 0) has k = 2.5.\nA(2, 0) lies on the x-axis. Find O′ and A′,\nand describe the image of the entire x-axis.',
 'O′ = (0, 0); A′ = (5, 0); the x-axis maps to itself',
 'A dilation centered at the origin has factor two point five. A is two, zero. Find both images and describe the image of the entire x-axis.',[
 ('CENTER','Zero distance from the center stays zero','O′ = (2.5 × 0, 2.5 × 0) = (0, 0)',
  'The center is zero distance from itself. Multiplying zero by the factor leaves the center fixed.'),
 ('OTHER POINT','Points on the line can move','A′ = (2.5 × 2, 2.5 × 0) = (5, 0)',
  'A moves from two, zero to five, zero, still on the x-axis.'),
 ('WHOLE LINE','Every point remains on this line','(t, 0) → (2.5t, 0)',
  'Every point on this line has zero y-coordinate. Scaling keeps that coordinate zero, and the images cover the entire line.'),
 ('GENERAL RULE','Separate a fixed line from fixed individual points','A line through the center maps to itself.',
  'For a nonzero scale factor, any line through the center maps to itself as a set. Individual points usually move, but the center always stays fixed.')],
 g(9,16,2,4),expression='2.5*2',value='5',equalities=[('2.5*0','0')]),

authored('geometry-dilation-area','Scale an area using the square of the length factor',
 'A shape has area 75 cm². Every length is scaled\nby 0.6. Find the area factor and the new area.',
 'Area factor 0.36; new area 27 cm²',
 'A shape has area seventy-five square centimetres. Every length is scaled by zero point six. Find the area factor and the new area.',[
 ('TWO DIMENSIONS','Both dimensions contribute a factor','Area factor = k²',
  'Area uses two length dimensions. Scaling both by k multiplies area by k squared. This applies to planar areas and surface areas.'),
 ('SQUARE THE FACTOR','Use the length factor twice','0.6² = 0.6 × 0.6 = 0.36',
  'Square zero point six to get zero point three six.'),
 ('SCALE THE AREA','Multiply the original area by the area factor','75 × 0.36 = 27 cm²',
  'Multiply seventy-five by zero point three six. The new area is twenty-seven square centimetres.'),
 ('CHECK','The area ratio equals the square of the length ratio','27 ÷ 75 = 0.36 = 0.6²',
  'The area ratio is zero point three six. For a triangle, both base and height scale; for a solid, each surface patch follows the same square rule.')],
 g(7,8,'4HW',5),expression='75*0.6**2',value='27',identities=[('(k*x)*(k*y)','k**2*x*y')]),

authored('geometry-dilation-volume','Scale volume using the cube of the length factor',
 'A cube has side length 5 cm. Every length\nis scaled by 0.4. Find the volume factor\nand the new volume.',
 'Volume factor 0.064; new volume 8 cm³',
 'A cube has side length five centimetres. Every length is scaled by zero point four. Find the volume factor and the new volume.',[
 ('THREE DIMENSIONS','Use the factor once for each length dimension','Volume factor = k³',
  'Volume uses three length dimensions. Multiply three copies of the length factor.'),
 ('CUBE THE FACTOR','Multiply zero point four three times','0.4³ = 0.064',
  'Zero point four cubed is zero point zero six four. This is the image to original volume ratio.'),
 ('SCALE THE VOLUME','The original cube has volume five cubed','Original: 5³ = 125 cm³\nImage: 125 × 0.064 = 8 cm³',
  'The original volume is one hundred twenty-five cubic centimetres. Multiplying by the volume factor gives eight cubic centimetres.'),
 ('CHECK WITH LENGTHS','The new cube side is two centimetres','New side: 5 × 0.4 = 2 cm\nNew volume: 2³ = 8 cm³',
  'The new side is two centimetres, whose cube is eight. For similar solids, lengths scale by k, surface areas by k squared, and volumes by k cubed.')],
 g(10,10,1,3),expression='125*0.4**3',value='8',equalities=[('5*0.4','2'),('2**3','8')],identities=[('(k*x)*(k*y)*(k*z)','k**3*x*y*z')]),

authored('geometry-dilation-length-from-area','Find a length scale factor from an area ratio',
 'Two similar triangles have areas 18 cm² and 288 cm².\nFind the length scale factor from small to large.',
 '4',
 'Two similar triangles have areas eighteen and two hundred eighty-eight square centimetres. Find the length scale factor from small to large.',[
 ('AREA RATIO','Divide destination area by starting area','Area ratio = 288 ÷ 18 = 16',
  'We are going from small to large, so divide two hundred eighty-eight by eighteen. The area ratio is sixteen.'),
 ('RELATE THE FACTORS','The area ratio is the length factor squared','k² = 16',
  'For similar shapes, the area ratio is k squared. Sixteen is the area factor, not the length factor.'),
 ('TAKE THE ROOT','Use the positive square root for lengths','k = √16 = 4',
  'Take the positive square root. The length scale factor is four.'),
 ('CHECK','Square the length factor to recover the area factor','4² × 18 = 288 cm²',
  'Four squared times eighteen is two hundred eighty-eight, which checks the larger area. The reverse length factor would be one quarter.')],
 g(10,8,'2Rev',3),expression='288/18',value='16',equalities=[('4**2','16'),('4**2*18','288')]),
]


def diagram(spec,d,scene,p):
    vid=spec['video_id']
    if vid=='geometry-dilation-origin-coordinates' and scene in (1,4):
        left,top,step=650,380,48
        def xy(x,y):return left+(x+9)*step,top+(7-y)*step
        for x in range(-9,2):d.line([xy(x,0),xy(x,7)],fill='#E4E9E8',width=2)
        for y in range(8):d.line([xy(-9,y),xy(1,y)],fill='#E4E9E8',width=2)
        d.line([xy(-9,0),xy(1,0)],fill=v.INK,width=3);d.line([xy(0,0),xy(0,7)],fill=v.INK,width=3)
        d.line([xy(0,0),xy(-8,6)],fill='#A8BEB9',width=4)
        v.text(d,xy(1.3,0),'x',28,v.INK,True);v.text(d,xy(0.3,7.3),'y',28,v.INK,True)
        for x,y,label in [(-8,6,'P(−8, 6)'),(-6,4.5,'P′(−6, 4.5)'),(0,0,'O')]:
            X,Y=xy(x,y);d.ellipse((X-7,Y-7,X+7,Y+7),fill=v.TEAL)
            v.text(d,(X+16,Y-25 if y==6 else Y+14),label,30,v.TEAL,True)
        centered_math(d,780,'(−8, 6) × 3/4 = (−6, 4.5)',48,v.TEAL)
        centered_math(d,870,'Scale BOTH coordinates about the origin.',36,v.INK)
    elif vid=='geometry-dilation-center-line' and scene in (1,2,3):
        y=550;d.line((400,y,1540,y),fill=v.INK,width=4)
        for x,label in [(650,'O = O′'),(850,'A'),(1150,'A′')]:
            d.ellipse((x-8,y-8,x+8,y+8),fill=v.TEAL);v.text(d,(x-35,y-65),label,38,v.TEAL,True)
        for x,label in [(650,'0'),(850,'2'),(1150,'5')]:v.text(d,(x-10,y+22),label,32,v.INK,True)
        centered_math(d,710,'x-axis → x-axis; A moves, O stays fixed',40,v.TEAL)
        centered_math(d,815,spec['displays'][scene],42,v.INK)
    else:draw_card(spec,d,scene,p)


def lessons(doc):
    batch=make_lessons(SPECS,doc)
    assert 7+9>11 and 0<.65<1<2.2
    for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:diagram(s,d,scene,p)
    return batch
