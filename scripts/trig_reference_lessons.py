"""Reference-angle, sign and inverse-composition examples."""
from math import pi,sin,cos,tan,asin,atan,sqrt,isclose
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons,draw_card,centered_math
import generate_sample_videos as v

SPECS=[
authored('trigonometry-reference-angle-sine','Find an exact sine with a reference angle',
 'Find sin(7π/6) exactly.', '−1/2',
 'Find sine of seven pi over six exactly.',[
 ('LOCATE','Seven pi over six lies in Quadrant III','7π/6 = π + π/6',
  'Seven pi over six is pi plus pi over six, so it lies in quadrant three.'),
 ('REFERENCE ANGLE','Measure the acute angle to the x-axis','Reference angle = π/6 = 30°',
  'Its reference angle is pi over six, or thirty degrees. A thirty-sixty-ninety triangle has opposite-to-hypotenuse ratio one half for the thirty-degree angle.'),
 ('APPLY THE SIGN','Sine is the vertical coordinate','Quadrant III: y < 0 → sine is negative',
  'Sine is the vertical coordinate. In quadrant three, that coordinate is negative, so use negative one half.'),
 ('EXACT ANSWER','Use the reference magnitude and the quadrant sign','sin(7π/6) = −1/2',
  'The exact answer is negative one half. Find the reference-angle magnitude first, then attach the sign from the quadrant.')],
 g(12,2,3,1),expression='7/6-1',value='1/6'),

authored('trigonometry-reference-angle-cosine','Find an exact cosine with a reference angle',
 'Find cos(11π/6) exactly.', '√3/2',
 'Find cosine of eleven pi over six exactly.',[
 ('LOCATE','Eleven pi over six lies in Quadrant IV','11π/6 = 2π − π/6',
  'Eleven pi over six is one sixth of pi short of a full turn. It lies in quadrant four.'),
 ('REFERENCE ANGLE','Use the acute angle to the positive x-axis','Reference angle = π/6 = 30°',
  'The reference angle is thirty degrees. In a thirty-sixty-ninety triangle, adjacent over hypotenuse for thirty degrees is root three over two.'),
 ('APPLY THE SIGN','Cosine is the horizontal coordinate','Quadrant IV: x > 0 → cosine is positive',
  'Cosine is the horizontal coordinate. In quadrant four it is positive, so keep the positive reference value.'),
 ('EXACT ANSWER','Keep the radical form instead of rounding','cos(11π/6) = √3/2',
  'The exact answer is root three over two. Use the acute reference angle for the magnitude and the quadrant for the sign.')],
 g(12,2,3,2),expression='2-11/6',value='1/6'),

authored('trigonometry-reference-angle-tangent','Find an exact tangent with a reference angle',
 'Find tan(4π/3) exactly.', '√3',
 'Find tangent of four pi over three exactly.',[
 ('LOCATE','Four pi over three lies in Quadrant III','4π/3 = π + π/3',
  'Four pi over three equals pi plus pi over three, placing it in quadrant three.'),
 ('REFERENCE ANGLE','Use the sixty-degree special triangle','Reference angle = π/3 = 60°\nOpposite/adjacent = √3/1',
  'The reference angle is sixty degrees. Its special triangle has opposite-to-adjacent ratio root three over one.'),
 ('APPLY THE SIGN','Tangent is y divided by x','Quadrant III: y < 0 and x < 0 → y/x > 0',
  'On the unit circle, tangent is y divided by x. Both coordinates are negative in quadrant three, so their quotient is positive.'),
 ('EXACT ANSWER','A negative divided by a negative is positive','tan(4π/3) = √3',
  'The exact answer is positive root three. Reference angles give the magnitude; the signs of y and x determine the sign of tangent.')],
 g(12,2,3,3),expression='4/3-1',value='1/3'),

authored('trigonometry-pi-shift-reflection-signs','Use pi-shift and reflection identities',
 'Let θ = π/4. Find sin(π + θ) and cos(π − θ).',
 'Both equal −√2/2',
 'Let theta equal pi over four. Find sine of pi plus theta, and cosine of pi minus theta.',[
 ('START WITH THETA','The forty-five-degree unit-circle coordinates match','At θ = π/4: (x, y) = (√2/2, √2/2)',
  'At pi over four, both unit-circle coordinates are root two over two.'),
 ('ADD PI','A half-turn changes both coordinate signs','sin(π + θ) = −sin θ\nsin(5π/4) = −√2/2',
  'Adding pi makes a half-turn. Both coordinates change sign. Sine reads y, so sine of pi plus theta is negative sine theta.'),
 ('SUBTRACT FROM PI','Reflect across the vertical axis','cos(π − θ) = −cos θ\ncos(3π/4) = −√2/2',
  'Pi minus theta reflects the original point across the vertical axis. The x-coordinate changes sign. Cosine reads x, so its value is negative cosine theta.'),
 ('COMPARE','Different transformations give the same value here','sin(5π/4) = cos(3π/4) = −√2/2',
  'Both answers are negative root two over two. The half-turn explains the sine identity; the reflection explains the cosine identity.')],
 g(12,2,3,6),expression='1+1/4',value='5/4',equalities=[('1-1/4','3/4')]),

authored('trigonometry-arcsine-sine-principal-value','Evaluate arcsine of sine using the principal range',
 'Evaluate arcsin(sin(5π/6)).', 'π/6',
 'Evaluate inverse sine of sine of five pi over six.',[
 ('INNER FUNCTION','Find the sine value first','sin(5π/6) = 1/2',
  'Start inside. Five pi over six is in quadrant two, with reference angle pi over six. Its sine is one half.'),
 ('PRINCIPAL RANGE','Arcsine returns an angle from minus pi over two to pi over two','−π/2 ≤ arcsin(u) ≤ π/2',
  'Arcsine returns only angles between negative pi over two and positive pi over two. The original angle is outside this range.'),
 ('FIND THE RETURNED ANGLE','Choose the angle in that range with sine one half','arcsin(1/2) = π/6',
  'Within the principal range, the angle with sine one half is pi over six.'),
 ('CHECK THE ORDER','The composition need not return the original angle','arcsin(sin(5π/6)) = π/6',
  'The answer is pi over six. Inverse sine of sine does not always return the original angle; it returns the matching angle in the principal range.')],
 g(12,2,4,7),expression='1-5/6',value='1/6'),

authored('trigonometry-tangent-arctangent-composition','Simplify tangent of an arctangent',
 'Simplify tan(arctan(7/3)).', '7/3',
 'Simplify tangent of inverse tangent of seven thirds.',[
 ('NAME THE ANGLE','Let theta be the angle returned by arctangent','θ = arctan(7/3)',
  'Call the returned angle theta. Arctangent returns an angle strictly between negative pi over two and positive pi over two.'),
 ('INVERSE DEFINITION','That angle has tangent seven thirds','tan θ = 7/3',
  'By definition, theta is the angle whose tangent is seven thirds.'),
 ('APPLY TANGENT','Substitute theta back into the expression','tan(arctan(7/3)) = tan θ = 7/3',
  'Applying tangent recovers the original ratio, so the expression equals seven thirds.'),
 ('GENERAL RULE','This order works for every real input','tan(arctan u) = u for every real u',
  'Tangent of arctangent returns the input for every real number. Keep track of which function is on the outside when using inverse compositions.')],
 g(12,2,4,8),expression='7/3',value='7/3'),
]


def diagram(spec,d,scene,p):
    vid=spec['video_id']
    if scene not in (1,2,3) or vid in ('trigonometry-arcsine-sine-principal-value','trigonometry-tangent-arctangent-composition'):
        draw_card(spec,d,scene,p);return
    theta,label,coord={
      'trigonometry-reference-angle-sine':(7*pi/6,'θ = 7π/6','(−√3/2, −1/2)'),
      'trigonometry-reference-angle-cosine':(11*pi/6,'θ = 11π/6','(√3/2, −1/2)'),
      'trigonometry-reference-angle-tangent':(4*pi/3,'θ = 4π/3','(−1/2, −√3/2)'),
      'trigonometry-pi-shift-reflection-signs':((pi/4,5*pi/4,3*pi/4)[scene-1],('θ = π/4','π + θ = 5π/4','π − θ = 3π/4')[scene-1],('(√2/2, √2/2)','(−√2/2, −√2/2)','(−√2/2, √2/2)')[scene-1])}[vid]
    cx,cy,R=930,560,170
    d.ellipse((cx-R,cy-R,cx+R,cy+R),outline='#AAC8BD',width=3)
    d.line((cx-R-35,cy,cx+R+35,cy),fill=v.INK,width=3);d.line((cx,cy-R-35,cx,cy+R+35),fill=v.INK,width=3)
    x,y=cx+R*cos(theta),cy-R*sin(theta)
    d.line((cx,cy,x,y),fill=v.TEAL,width=5);d.line((x,y,x,cy,cx,cy),fill='#B66F4E',width=3)
    d.ellipse((x-6,y-6,x+6,y+6),fill=v.TEAL)
    v.text(d,(cx+R+50,cy),'x',28,v.INK,True,anchor='mm');v.text(d,(cx+25,cy-R-35),'y',28,v.INK,True,anchor='mm')
    v.text(d,(1210,440),label,33,v.INK,True)
    v.text(d,(cx,cy+R+54),coord,32,v.INK,True,anchor='mm')
    for i,line in enumerate(spec['displays'][scene].split('\n')):centered_math(d,855+i*56,line,39,v.TEAL)


def lessons(doc):
    assert isclose(sin(7*pi/6),-.5) and isclose(cos(11*pi/6),sqrt(3)/2)
    assert isclose(tan(4*pi/3),sqrt(3))
    assert isclose(sin(5*pi/4),-sqrt(2)/2) and isclose(cos(3*pi/4),-sqrt(2)/2)
    assert isclose(asin(sin(5*pi/6)),pi/6) and isclose(tan(atan(7/3)),7/3)
    batch=make_lessons(SPECS,doc)
    for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:diagram(s,d,scene,p)
    return batch
