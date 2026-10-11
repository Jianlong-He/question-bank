"""Checked, analogous angle calculations and angle equations."""
from math import sin,cos,radians
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons,draw_card,centered_math
import generate_sample_videos as v

SPECS=[
authored('geometry-angle-relationships','Find a supplementary angle',
 'Two adjacent angles form a straight line.\nOne measures 137°. Find the other angle.','43 degrees',
 'Two adjacent angles form a straight line. One measures one hundred thirty-seven degrees. Find the other angle.',[
 ('STRAIGHT ANGLE','A straight angle measures one hundred eighty degrees','137° + x = 180°',
  'The angles form a straight angle, so they add to one hundred eighty degrees. Such angles are supplementary.'),
 ('SUBTRACT','Remove the known angle from the total','x = 180° − 137°',
  'Subtract the known angle from one hundred eighty.'),
 ('CALCULATE','The remaining angle is forty-three degrees','x = 43°',
  'One hundred eighty minus one hundred thirty-seven is forty-three degrees.'),
 ('CHECK','The pair must add to one hundred eighty','137° + 43° = 180°',
  'Check the sum. Any angle supplementary to one hundred thirty-seven degrees has measure forty-three degrees.')],
 g(7,9,3,5),expression='180-137',value='43'),

authored('geometry-complementary-angle-equation','Solve an equation for complementary angles',
 'Complementary angles measure (2x + 7)° and (3x + 18)°.\nFind x and both angle measures.','x = 13; angles 33° and 57°',
 'Complementary angles measure two x plus seven degrees and three x plus eighteen degrees. Find x and both angles.',[
 ('SET THE TOTAL','Complementary angles add to ninety degrees','(2x + 7) + (3x + 18) = 90',
  'Complementary angles add to ninety, so add the two expressions and set the result equal to ninety.'),
 ('COMBINE LIKE TERMS','Collect the x terms and the constants','5x + 25 = 90',
  'Two x plus three x is five x. Seven plus eighteen is twenty-five.'),
 ('SOLVE','Subtract twenty-five, then divide by five','5x = 65 → x = 13',
  'Subtract twenty-five to get five x equals sixty-five. Divide by five, giving x equals thirteen.'),
 ('FIND THE ANGLES','Substitute x back into each expression','2(13) + 7 = 33°; 3(13) + 18 = 57°\n33° + 57° = 90°',
  'Substitute thirteen. The angles are thirty-three and fifty-seven degrees, and their sum is ninety.')],
 g(7,9,1,8),equation=('2*x+7+3*x+18','90','x','13'),equalities=[('2*13+7','33'),('3*13+18','57'),('33+57','90')]),

authored('geometry-supplementary-angle-equation','Solve an equation for supplementary angles',
 'Supplementary angles measure (4x + 8)° and (2x − 2)°.\nFind x and both angle measures.','x = 29; angles 124° and 56°',
 'Supplementary angles measure four x plus eight degrees and two x minus two degrees. Find x and both angles.',[
 ('SET THE TOTAL','Supplementary angles add to one hundred eighty','(4x + 8) + (2x − 2) = 180',
  'Add the two angle expressions and set their sum equal to one hundred eighty.'),
 ('COMBINE LIKE TERMS','Add the variable terms and constants','6x + 6 = 180',
  'Four x plus two x is six x. Eight minus two is six.'),
 ('SOLVE','Subtract six, then divide by six','6x = 174 → x = 29',
  'Subtract six from both sides, then divide by six. The value of x is twenty-nine.'),
 ('FIND AND CHECK THE ANGLES','x is not itself either angle measure','4(29) + 8 = 124°; 2(29) − 2 = 56°\n124° + 56° = 180°',
  'Substitute twenty-nine into both expressions. The angles are one hundred twenty-four and fifty-six degrees, which add to one hundred eighty.')],
 g(7,9,1,7),equation=('4*x+8+2*x-2','180','x','29'),equalities=[('4*29+8','124'),('2*29-2','56'),('124+56','180')]),

authored('geometry-vertical-angle-equation-one-side','Solve a vertical-angle equation with one expression',
 'Opposite angles at intersecting lines measure\n(7x − 9)° and 96°. Find x.','x = 15',
 'Opposite angles at intersecting lines measure seven x minus nine degrees and ninety-six degrees. Find x.',[
 ('VERTICAL ANGLES','Opposite angles at an intersection are equal','7x − 9 = 96',
  'These opposite angles are called vertical angles. They are equal, so set seven x minus nine equal to ninety-six.'),
 ('UNDO SUBTRACTION','Add nine to both sides','7x = 105',
  'Add nine to both sides, giving seven x equals one hundred five.'),
 ('DIVIDE','Divide both sides by seven','x = 15',
  'Divide by seven. The value of x is fifteen.'),
 ('CHECK','Both angle measures must agree','7(15) − 9 = 105 − 9 = 96°',
  'Substituting fifteen gives ninety-six degrees, matching the opposite angle.')],
 g(7,9,1,9),equation=('7*x-9','96','x','15'),equalities=[('7*15-9','96')]),

authored('geometry-vertical-angle-equation-both-sides','Solve a vertical-angle equation with two expressions',
 'Vertical angles measure (8x + 3)° and (5x + 48)°.\nFind x and their common angle measure.','x = 15; both angles 123°',
 'Vertical angles measure eight x plus three degrees and five x plus forty-eight degrees. Find x and their common measure.',[
 ('EQUAL ANGLES','Vertical angles have equal measures','8x + 3 = 5x + 48',
  'Set the two expressions equal because vertical angles have the same measure.'),
 ('COLLECT THE VARIABLES','Subtract five x from both sides','3x + 3 = 48',
  'Subtract five x from both sides, leaving three x plus three equals forty-eight.'),
 ('SOLVE','Subtract three, then divide by three','3x = 45 → x = 15',
  'Subtract three, then divide by three. This gives x equals fifteen.'),
 ('CHECK BOTH EXPRESSIONS','Substitute fifteen into each angle','8(15) + 3 = 123°\n5(15) + 48 = 123°',
  'Both expressions give one hundred twenty-three degrees. That confirms the equation and the angle measure.')],
 g(8,5,2,4),equation=('8*x+3','5*x+48','x','15'),equalities=[('8*15+3','123'),('5*15+48','123')]),

authored('geometry-complementary-angle-ratio','Divide complementary angles in a ratio',
 'Complementary angles are in the ratio 4:11.\nFind the smaller and larger angles.','24° and 66°',
 'Complementary angles are in the ratio four to eleven. Find the smaller and larger angles.',[
 ('COUNT THE PARTS','Complementary angles share ninety degrees','4 + 11 = 15 equal parts',
  'The total is ninety degrees. The ratio uses four plus eleven, or fifteen equal parts.'),
 ('FIND ONE PART','Divide the total by fifteen','90° ÷ 15 = 6° per part',
  'Divide ninety by fifteen. Each ratio part represents six degrees.'),
 ('SCALE BOTH PARTS','Multiply by four and by eleven','Smaller = 4 × 6° = 24°\nLarger = 11 × 6° = 66°',
  'Four parts give twenty-four degrees. Eleven parts give sixty-six degrees.'),
 ('CHECK','Check both the total and the ratio','24° + 66° = 90°\n24:66 = 4:11',
  'The angles add to ninety, and their ratio simplifies to four to eleven. Both conditions are satisfied.')],
 g(7,9,1,10),expression='90/(4+11)',value='6',equalities=[('4*6','24'),('11*6','66'),('24+66','90'),('24/66','4/11')]),

authored('geometry-supplementary-angle-multiple','Find supplementary angles when one is a multiple',
 'Two angles are supplementary.\nThe larger is 7 times the smaller. Find both angles.','22.5° and 157.5°',
 'Two angles are supplementary. The larger is seven times the smaller. Find both angles.',[
 ('CHOOSE A VARIABLE','Let x be the smaller angle','Smaller = x; larger = 7x',
  'Let the smaller angle be x. Then the larger angle is seven x.'),
 ('USE THE TOTAL','Their sum is one hundred eighty','x + 7x = 180 → 8x = 180',
  'Add them and set the sum equal to one hundred eighty. That gives eight x equals one hundred eighty.'),
 ('SOLVE','Divide by eight','x = 22.5°\n7x = 157.5°',
  'Divide by eight to get twenty-two point five degrees. Multiply by seven for the larger angle, one hundred fifty-seven point five degrees.'),
 ('CHECK','The angle measures add to a straight angle','22.5° + 157.5° = 180°',
  'The two angles add to one hundred eighty, and the larger is seven times the smaller.')],
 g(7,9,3,4),equation=('x+7*x','180','x','22.5'),equalities=[('7*22.5','157.5'),('22.5+157.5','180')]),

authored('geometry-supplementary-angle-difference','Find supplementary angles from their difference',
 'Two angles are supplementary.\nThe larger is 54° more than the smaller. Find both.','63° and 117°',
 'Two angles are supplementary. The larger is fifty-four degrees more than the smaller. Find both angles.',[
 ('WRITE BOTH ANGLES','Let x be the smaller angle','Smaller = x; larger = x + 54',
  'Let the smaller angle be x, so the larger is x plus fifty-four.'),
 ('USE THEIR SUM','Supplementary angles total one hundred eighty','x + (x + 54) = 180\n2x + 54 = 180',
  'Add the two expressions and set the total equal to one hundred eighty.'),
 ('SOLVE','Subtract fifty-four, then divide by two','2x = 126 → x = 63°',
  'Subtract fifty-four and divide by two. The smaller angle is sixty-three degrees.'),
 ('FIND AND CHECK THE LARGER ANGLE','Add the difference to the smaller angle','63° + 54° = 117°\n63° + 117° = 180°',
  'Add fifty-four to get the larger angle, one hundred seventeen degrees. Together they make one hundred eighty degrees.')],
 g(7,9,2,8),equation=('x+x+54','180','x','63'),equalities=[('63+54','117'),('63+117','180')]),

authored('geometry-complementary-angle-word-equation','Translate a complementary-angle word problem',
 'Two angles are complementary. The larger is 24°\nless than twice the smaller. Find both angles.','38° and 52°',
 'Two angles are complementary. The larger is twenty-four degrees less than twice the smaller. Find both angles.',[
 ('TRANSLATE','Let x be the smaller angle','Smaller = x; larger = 2x − 24',
  'Let the smaller angle be x. Twice it is two x. Twenty-four less means subtract twenty-four.'),
 ('ADD TO NINETY','Complementary angles have a total of ninety','x + (2x − 24) = 90\n3x − 24 = 90',
  'Add the two angles and set the sum equal to ninety.'),
 ('SOLVE','Add twenty-four, then divide by three','3x = 114 → x = 38°',
  'Add twenty-four and divide by three. The smaller angle is thirty-eight degrees.'),
 ('CHECK THE OTHER ANGLE','Use the original description','2(38°) − 24° = 52°\n38° + 52° = 90°',
  'Twice thirty-eight minus twenty-four is fifty-two degrees. It is larger, and the two angles add to ninety.')],
 g(7,9,5,1),equation=('x+2*x-24','90','x','38'),equalities=[('2*38-24','52'),('38+52','90')]),

authored('geometry-triangle-angle-equation','Solve a triangle angle-sum equation',
 'Triangle angles are A = (2x + 7)°, B = (3x − 9)°,\nand C = (x + 14)°. Find x and angle C.','x = 28; angle C = 42°',
 'A triangle has angles two x plus seven, three x minus nine, and x plus fourteen degrees. Find x and the third angle, C.',[
 ('ANGLE SUM','The three interior angles add to one hundred eighty','(2x + 7) + (3x − 9) + (x + 14) = 180',
  'Add the three angle expressions and set their sum equal to one hundred eighty degrees.'),
 ('COMBINE AND SOLVE','Collect the terms, then isolate x','6x + 12 = 180\n6x = 168 → x = 28',
  'Combine like terms to get six x plus twelve equals one hundred eighty. Subtract twelve and divide by six, giving x equals twenty-eight.'),
 ('ANSWER THE REQUESTED ANGLE','Substitute x into angle C','C = 28 + 14 = 42°',
  'The question asks for angle C, so substitute twenty-eight into x plus fourteen. Angle C is forty-two degrees.'),
 ('CHECK ALL THREE','Their measures should total one hundred eighty','A = 63°; B = 75°; C = 42°\n63° + 75° + 42° = 180°',
  'The other angles are sixty-three and seventy-five degrees. All three total one hundred eighty, as required.')],
 g(8,5,2,10),equation=('2*x+7+3*x-9+x+14','180','x','28'),equalities=[('2*28+7','63'),('3*28-9','75'),('28+14','42'),('63+75+42','180')]),

authored('geometry-angle-measure-triangle-sum','Find a missing triangle angle',
 'Two angles of a triangle measure 46° and 73°.\nFind the third angle.','61 degrees',
 'Two angles of a triangle measure forty-six and seventy-three degrees. Find the third angle.',[
 ('TOTAL','A triangle’s interior angles sum to one hundred eighty','46° + 73° + x = 180°',
  'The three interior angles of a triangle always add to one hundred eighty degrees.'),
 ('ADD THE KNOWN ANGLES','Combine forty-six and seventy-three','46° + 73° = 119°',
  'First add the two known angles. Forty-six plus seventy-three equals one hundred nineteen degrees.'),
 ('SUBTRACT','Find what remains of the total','x = 180° − 119° = 61°',
  'Subtract one hundred nineteen from one hundred eighty. The third angle is sixty-one degrees.'),
 ('CHECK','All three angles must be positive and total one hundred eighty','46° + 73° + 61° = 180°',
  'The three positive angles add to one hundred eighty degrees, so the answer checks.')],
 g(7,9,3,7),expression='180-46-73',value='61'),

authored('geometry-isosceles-base-angles','Find the equal base angles of an isosceles triangle',
 'An isosceles triangle has vertex angle 76°\nbetween its two equal sides. Find each base angle.','52 degrees each',
 'An isosceles triangle has a seventy-six degree angle between its two equal sides. Find each base angle.',[
 ('EQUAL SIDES','The angles opposite the equal sides are equal','Base angles: x and x',
  'The two equal sides have equal opposite angles. Call each base angle x.'),
 ('REMOVE THE VERTEX ANGLE','The three angles total one hundred eighty','180° − 76° = 104°',
  'Subtract the vertex angle from one hundred eighty. One hundred four degrees remain for the two base angles.'),
 ('SHARE EQUALLY','Divide the remaining angle sum by two','104° ÷ 2 = 52°',
  'Divide by two. Each base angle is fifty-two degrees.'),
 ('CHECK','The equal angles and vertex angle make the full total','52° + 52° + 76° = 180°',
  'The two fifty-two degree angles and the seventy-six degree angle add to one hundred eighty.')],
 g(7,9,5,4),expression='(180-76)/2',value='52',equalities=[('52+52+76','180')]),

authored('geometry-equilateral-angle-equation','Use equal angles in an equilateral triangle',
 'One angle of an equilateral triangle is (5x − 15)°.\nFind x.','x = 15',
 'One angle of an equilateral triangle is five x minus fifteen degrees. Find x.',[
 ('THREE EQUAL ANGLES','An equilateral triangle has three equal angles','Each angle = 180° ÷ 3 = 60°',
  'All three angles are equal. Divide one hundred eighty by three, so each angle is sixty degrees.'),
 ('WRITE AN EQUATION','Set the given angle equal to sixty','5x − 15 = 60',
  'The given expression must equal sixty degrees.'),
 ('SOLVE','Add fifteen, then divide by five','5x = 75 → x = 15',
  'Add fifteen to both sides, then divide by five. The value of x is fifteen.'),
 ('CHECK','The expression gives sixty degrees','5(15) − 15 = 60°\n60° + 60° + 60° = 180°',
  'Substituting fifteen gives sixty degrees. Three sixty-degree angles make the required triangle total.')],
 g(8,5,3,6),equation=('5*x-15','60','x','15'),equalities=[('180/3','60'),('5*15-15','60')]),
]

def triangle_points(A,B):
    # A at left and B at right; sine rule gives AC when AB is one unit.
    C=180-A-B;ac=sin(radians(B))/sin(radians(C))
    return [(0,0),(1,0),(ac*cos(radians(A)),ac*sin(radians(A)))]

def diagram(spec,d,scene,p):
    vid=spec['video_id']
    if scene!=1 or vid not in ('geometry-angle-measure-triangle-sum','geometry-isosceles-base-angles','geometry-angle-relationships'):
        draw_card(spec,d,scene,p);return
    if vid=='geometry-angle-relationships':
        cx,cy=960,680;R=280
        d.line((cx-R,cy,cx+R,cy),fill=v.TEAL,width=5)
        d.line((cx,cy,cx+R*cos(radians(137)),cy-R*sin(radians(137))),fill=v.TEAL,width=5)
        d.arc((cx-85,cy-85,cx+85,cy+85),223,360,fill='#B66F4E',width=4)
        v.text(d,(cx+20,cy-130),'137°',36,v.INK,True,anchor='mm');v.text(d,(cx-160,cy-55),'x',36,v.INK,True,anchor='mm')
    else:
        angles=[46,73,61] if vid=='geometry-angle-measure-triangle-sum' else [52,52,76]
        pts=triangle_points(*angles[:2]);scale=450
        coords=[(730+x*scale,750-y*scale) for x,y in pts]
        d.polygon(coords,fill='#D0E8E2',outline=v.TEAL,width=4)
        labels=['46°','73°','x'] if vid=='geometry-angle-measure-triangle-sum' else ['x','x','76°']
        for (x,y),label,(dx,dy) in zip(coords,labels,[(-25,25),(25,25),(0,-30)]):v.text(d,(x+dx,y+dy),label,34,v.INK,True,anchor='mm')
        if vid=='geometry-isosceles-base-angles':
            for k in (0,1):
                a,b=coords[k],coords[2];mx,my=(a[0]+b[0])/2,(a[1]+b[1])/2
                dx,dy=b[0]-a[0],b[1]-a[1];length=(dx*dx+dy*dy)**.5
                d.line((mx-dy/length*12,my+dx/length*12,mx+dy/length*12,my-dx/length*12),fill=v.INK,width=4)
    for i,line in enumerate(spec['displays'][scene].split('\n')):centered_math(d,845+i*60,line,42,v.TEAL)

def lessons(doc):
    batch=make_lessons(SPECS,doc)
    for spec in SPECS:v.DRAW[spec['video_id']]=lambda d,scene,p,s=spec:diagram(s,d,scene,p)
    return batch
