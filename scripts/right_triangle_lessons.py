"""Distinct right-triangle calculations and area models."""
from math import sqrt
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons,draw_card,centered_math
import generate_sample_videos as v

SPECS=[
authored('geometry-pythagorean','Find the hypotenuse with the Pythagorean theorem',
 'A right triangle has legs 33 cm and 56 cm.\nFind its hypotenuse.','65 centimetres',
 'A right triangle has legs thirty-three centimetres and fifty-six centimetres. Find its hypotenuse.',[
 ('IDENTIFY THE SIDES','The hypotenuse is opposite the right angle','a² + b² = c²\n33² + 56² = c²',
  'The hypotenuse is opposite the right angle. Use a squared plus b squared equals c squared, with thirty-three and fifty-six as the legs.'),
 ('SQUARE AND ADD','Add the squares of the two legs','1089 + 3136 = 4225\nc² = 4225',
  'Square both legs. One thousand eighty-nine plus three thousand one hundred thirty-six equals four thousand two hundred twenty-five.'),
 ('TAKE THE POSITIVE ROOT','A length must be positive','c = √4225 = 65 cm',
  'Take the positive square root. The hypotenuse is sixty-five centimetres.'),
 ('CHECK','The hypotenuse is the longest side','65² = 4225\n65 > 56 and 65 > 33',
  'Sixty-five squared equals the sum of the leg squares. The hypotenuse is also longer than either leg, as expected.')],
 g(10,9,1,2),expression='33**2+56**2',value='4225',equalities=[('65**2','4225')]),

authored('geometry-pythagorean-missing-leg','Find a missing leg of a right triangle',
 'A right triangle has hypotenuse 53 cm\nand one leg 28 cm. Find the other leg.','45 centimetres',
 'A right triangle has hypotenuse fifty-three centimetres and one leg twenty-eight centimetres. Find the other leg.',[
 ('WRITE THE EQUATION','The hypotenuse stays alone on one side','28² + b² = 53²',
  'Put the hypotenuse squared on its own side of the equation. Twenty-eight squared plus b squared equals fifty-three squared.'),
 ('SUBTRACT THE KNOWN SQUARE','Subtract because a leg is missing','b² = 53² − 28²\nb² = 2809 − 784 = 2025',
  'Subtract the known leg’s square from the hypotenuse’s square. Two thousand eight hundred nine minus seven hundred eighty-four is two thousand twenty-five.'),
 ('TAKE THE POSITIVE ROOT','Find the side length, not its square','b = √2025 = 45 cm',
  'Take the positive square root. The missing leg is forty-five centimetres.'),
 ('CHECK','Both leg squares should add to the hypotenuse square','28² + 45² = 784 + 2025 = 2809\n2809 = 53²',
  'Check by adding the two leg squares. Their sum equals fifty-three squared, so forty-five is correct.')],
 g(10,9,1,3),expression='53**2-28**2',value='2025',equalities=[('45**2','2025'),('28**2+45**2','53**2')]),

authored('geometry-triangle-30-60-90','Use the 30-60-90 triangle side ratios',
 'A 30-60-90 triangle has short leg 7 cm.\nFind its long leg and hypotenuse.',
 'Long leg: 7√3 cm; hypotenuse: 14 cm',
 'A thirty-sixty-ninety triangle has short leg seven centimetres. Find its long leg and hypotenuse.',[
 ('THE SIDE RATIO','Match each side to its opposite angle','Short : long : hypotenuse = 1 : √3 : 2',
  'The sides opposite thirty, sixty, and ninety degrees have ratio one to square root of three to two.'),
 ('HYPOTENUSE','Double the short leg','Hypotenuse = 2 × 7 = 14 cm',
  'Double the short leg. Two times seven gives a hypotenuse of fourteen centimetres.'),
 ('LONG LEG','Multiply the short leg by square root of three','Long leg = 7√3 cm',
  'Multiply the short leg by square root of three. The long leg is seven root three centimetres.'),
 ('REVERSE THE PROCESS','If the hypotenuse is given, halve it first','Short = hypotenuse ÷ 2\nLong = short × √3',
  'When the hypotenuse is given instead, divide it by two to find the short leg. Then multiply that short leg by square root of three.')],
 g(10,9,2,2),expression='2*7',value='14',equalities=[('7**2+(7**2)*3','14**2')]),

authored('geometry-triangle-45-45-90-hypotenuse','Find the hypotenuse of a 45-45-90 triangle',
 'A 45-45-90 triangle has one leg 6 cm.\nFind its hypotenuse.','6√2 centimetres',
 'A forty-five-forty-five-ninety triangle has one leg six centimetres. Find its hypotenuse.',[
 ('EQUAL LEGS','Equal acute angles give equal opposite legs','Both legs = 6 cm',
  'The two acute angles are equal, so the two legs are equal. Both legs are six centimetres.'),
 ('USE PYTHAGORAS','Add the two equal leg squares','c² = 6² + 6² = 72',
  'Use the Pythagorean theorem. Six squared plus six squared equals seventy-two.'),
 ('SIMPLIFY THE ROOT','Separate the perfect-square factor','c = √72 = √(36 × 2) = 6√2 cm',
  'Take the square root of seventy-two. Factor out thirty-six to get six root two centimetres.'),
 ('REMEMBER THE RATIO','Leg, leg and hypotenuse have ratio one, one, root two','1 : 1 : √2\nHypotenuse = leg × √2',
  'The side ratio is one to one to root two. Multiply either leg by square root of two to find the hypotenuse.')],
 g(10,9,2,5),expression='6**2+6**2',value='72',equalities=[('36*2','72')]),

authored('geometry-triangle-45-45-90-leg','Find the legs of a 45-45-90 triangle',
 'A 45-45-90 triangle has hypotenuse 18 cm.\nFind either leg.','9√2 centimetres',
 'A forty-five-forty-five-ninety triangle has hypotenuse eighteen centimetres. Find either leg.',[
 ('SIDE RATIO','Each leg is the hypotenuse divided by root two','Leg : leg : hypotenuse = 1 : 1 : √2',
  'The side ratio is one to one to root two. To recover a leg, divide the hypotenuse by square root of two.'),
 ('SUBSTITUTE','Use the given hypotenuse','Leg = 18/√2',
  'Substitute eighteen for the hypotenuse. Each leg is eighteen divided by square root of two.'),
 ('SIMPLIFY','Multiply numerator and denominator by root two','18/√2 = 18√2/2 = 9√2 cm',
  'Multiply the numerator and denominator by root two. The denominator becomes two, and the result simplifies to nine root two.'),
 ('CHECK BOTH LEGS','Their squares must add to eighteen squared','2 × (9√2)² = 2 × 162 = 324\n18² = 324',
  'Each leg squared is one hundred sixty-two. Twice that is three hundred twenty-four, which equals eighteen squared.')],
 g(10,9,2,6),expression='18**2/2',value='162',equalities=[('9**2*2','162'),('2*162','18**2')]),

authored('geometry-right-triangle-area-equation','Write an area equation from two algebraic legs',
 'A right triangle has legs x cm and (x + 5) cm.\nIts area is 42 cm². Write an equation for x.',
 'x(x + 5)/2 = 42',
 'A right triangle has legs x centimetres and x plus five centimetres. Its area is forty-two square centimetres. Write an equation for x.',[
 ('PERPENDICULAR LEGS','The two legs can be used as base and height','Base = x\nHeight = x + 5',
  'The two legs meet at a right angle, so they can serve as the base and perpendicular height.'),
 ('USE TRIANGLE AREA','Take half of base times height','A = (1/2)x(x + 5)',
  'Triangle area is half of base times height. Multiply x by x plus five, then divide by two.'),
 ('SET EQUAL TO THE AREA','Use the given area of forty-two','x(x + 5)/2 = 42',
  'Set that expression equal to forty-two. This is the required equation.'),
 ('AN EQUIVALENT FORM','Double both sides, then expand','x(x + 5) = 84\nx² + 5x − 84 = 0',
  'You can also double both sides, expand, and move everything to one side. The equivalent equation is x squared plus five x minus eighty-four equals zero.')],
 g(10,3,5,1),identities=[('x*(x+5)-84','x**2+5*x-84')],equalities=[('7*(7+5)/2','42')]),
]

DIAGRAMS={
 'geometry-pythagorean':(56,33,'56 cm','33 cm','c'),
 'geometry-pythagorean-missing-leg':(45,28,'b','28 cm','53 cm'),
 'geometry-triangle-30-60-90':(7,7*sqrt(3),'7 cm','long leg','hypotenuse'),
 'geometry-triangle-45-45-90-hypotenuse':(6,6,'6 cm','6 cm','c'),
 'geometry-triangle-45-45-90-leg':(1,1,'x','x','18 cm'),
}


def diagram(spec,d,scene,p):
    vid=spec['video_id']
    if vid in DIAGRAMS and scene==1:
        a,b,al,bl,cl=DIAGRAMS[vid];scale=min(410/a,280/b)
        x,y=720,705;ax,by=a*scale,b*scale
        d.polygon([(x,y),(x+ax,y),(x,y-by)],fill='#D0E8E2',outline=v.TEAL,width=4)
        d.line((x+22,y,x+22,y-22,x,y-22),fill=v.INK,width=3)
        v.text(d,(x+ax/2,y+40),al,35,v.INK,True,anchor='mm')
        v.text(d,(x-90,y-by/2),bl,34,v.INK,True,anchor='mm')
        v.text(d,(x+ax/2+80,y-by/2-45),cl,34,v.INK,True,anchor='mm')
        if '30-60-90' in vid:
            v.text(d,(x+30,y-by-35),'30°',30,v.INK,True,anchor='mm')
            v.text(d,(x+ax+48,y-15),'60°',30,v.INK,True,anchor='mm')
        elif '45-45-90' in vid:
            v.text(d,(x+30,y-by-35),'45°',30,v.INK,True,anchor='mm')
            v.text(d,(x+ax+48,y-15),'45°',30,v.INK,True,anchor='mm')
        for i,line in enumerate(spec['displays'][scene].split('\n')):centered_math(d,810+i*65,line,42,v.TEAL)
        return
    draw_card(spec,d,scene,p)


def lessons(doc):
    batch=make_lessons(SPECS,doc)
    for spec in SPECS:v.DRAW[spec['video_id']]=lambda d,scene,p,s=spec:diagram(s,d,scene,p)
    return batch
