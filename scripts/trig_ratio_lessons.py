"""Short, numerically distinct right-triangle ratio and identity examples."""
from math import atan,degrees,isclose,sqrt
from fractions import Fraction
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons,draw_card,centered_math
import generate_sample_videos as v

SPECS=[
authored('trigonometry-three-side-ratios','Find sine, cosine and tangent from side lengths',
 'For acute angle θ in a right triangle:\nopposite = 40, adjacent = 42, hypotenuse = 58.\nFind sin θ, cos θ and tan θ in simplest form.',
 'sin θ = 20/29; cos θ = 21/29; tan θ = 20/21',
 'A right triangle has opposite side forty, adjacent side forty-two, and hypotenuse fifty-eight, relative to angle theta. Find its three trigonometric ratios.',[
 ('SINE','Opposite divided by hypotenuse','sin θ = 40/58 = 20/29',
  'Sine is opposite over hypotenuse: forty over fifty-eight. Divide top and bottom by two to get twenty over twenty-nine.'),
 ('COSINE','Adjacent divided by hypotenuse','cos θ = 42/58 = 21/29',
  'Cosine is adjacent over hypotenuse: forty-two over fifty-eight, which simplifies to twenty-one over twenty-nine.'),
 ('TANGENT','Opposite divided by adjacent','tan θ = 40/42 = 20/21',
  'Tangent is opposite over adjacent: forty over forty-two, or twenty over twenty-one. It does not use the hypotenuse.'),
 ('CHECK THE SIDES','Always label sides relative to the given angle','sin: opposite/hypotenuse\ncos: adjacent/hypotenuse\ntan: opposite/adjacent',
  'First identify the hypotenuse opposite the right angle. Then label opposite and adjacent relative to the given acute angle, and choose the matching ratio.')],
 g(10,9,3,4),expression='40/58',value='20/29',equalities=[('42/58','21/29'),('40/42','20/21'),('40**2+42**2','58**2')]),

authored('trigonometry-inverse-tangent-acute-angle','Find an acute angle using inverse tangent',
 'An acute angle θ has tan θ = 7/9.\nFind θ to the nearest tenth of a degree.',
 '37.9 degrees',
 'An acute angle has tangent seven ninths. Find the angle to the nearest tenth of a degree.',[
 ('RECOGNIZE THE UNKNOWN','The ratio is known; the angle is missing','tan θ = 7/9',
  'We know the tangent ratio and want the acute angle that produces it.'),
 ('USE THE INVERSE','Inverse tangent returns an angle','θ = arctan(7/9)',
  'Use inverse tangent, also called arctangent. This is not the reciprocal of tangent.'),
 ('DEGREE MODE','Enter the full fraction before rounding','θ ≈ 37.874984°',
  'In degree mode, enter inverse tangent of seven divided by nine. The result is about thirty-seven point eight seven five degrees.'),
 ('ROUND','Round once, to the requested precision','θ ≈ 37.9°',
  'Round to the nearest tenth: thirty-seven point nine degrees. It lies between zero and ninety, as an acute angle should.')],
 g(10,9,3,7),expression='7/9',value='7/9'),

authored('trigonometry-find-other-acute-ratio','Find cosine from sine for an acute angle',
 'If sin θ = 9/41 and θ is acute, find cos θ.',
 '40/41',
 'If sine theta is nine over forty-one and theta is acute, find cosine theta.',[
 ('USE THE IDENTITY','Sine squared plus cosine squared equals one','sin² θ + cos² θ = 1',
  'Use the Pythagorean identity: sine squared plus cosine squared equals one.'),
 ('ISOLATE THE MISSING SQUARE','Subtract the known square from one','cos² θ = 1 − (9/41)²\n= 1681/1681 − 81/1681 = 1600/1681',
  'Cosine squared equals one minus nine over forty-one squared. With a common denominator, that is sixteen hundred over one thousand six hundred eighty-one.'),
 ('TAKE THE POSITIVE ROOT','Cosine is positive for an acute angle','cos θ = √(1600/1681) = 40/41',
  'Take the square root. Since theta is acute, cosine is positive, so choose forty over forty-one.'),
 ('CHECK','The same method works when cosine is given','(9/41)² + (40/41)² = 1',
  'Squaring and adding the two ratios gives one. If cosine were given instead, isolate sine squared and take the positive root for an acute angle.')],
 g(11,8,3,2),expression='1-(9/41)**2',value='1600/1681',equalities=[('(40/41)**2','1600/1681'),('(9/41)**2+(40/41)**2','1')]),

authored('trigonometry-verify-squared-sum','Verify the sine and cosine squared-sum identity',
 'If sin θ = 16/65 and cos θ = 63/65,\nverify sin² θ + cos² θ.',
 '1',
 'Sine theta is sixteen over sixty-five, and cosine theta is sixty-three over sixty-five. Verify their squared sum.',[
 ('SQUARE EACH RATIO','Square the numerator and denominator','sin² θ = 256/4225\ncos² θ = 3969/4225',
  'Square each entire fraction. Both results have the same denominator: four thousand two hundred twenty-five.'),
 ('ADD THE FRACTIONS','Keep the common denominator','(256 + 3969)/4225 = 4225/4225',
  'Add the numerators while keeping that denominator. Two hundred fifty-six plus three thousand nine hundred sixty-nine is four thousand two hundred twenty-five.'),
 ('SIMPLIFY','A nonzero number divided by itself is one','4225/4225 = 1',
  'The numerator and denominator are equal, so the result is one.'),
 ('GENERALIZE','This identity holds for every real angle','sin² θ + cos² θ = 1',
  'This verifies the Pythagorean identity for the given ratios. The identity also lets you evaluate the squared sum at any angle without calculating each ratio.')],
 g(11,8,3,4),expression='(16/65)**2+(63/65)**2',value='1',equalities=[('16**2','256'),('63**2','3969'),('65**2','4225')]),

authored('trigonometry-rearrange-pythagorean-identity','Simplify using the Pythagorean identity',
 'Simplify 5 − sin² θ using cosine.\nThen simplify 7 − cos² θ using sine.',
 '4 + cos² θ; 6 + sin² θ',
 'Simplify five minus sine squared theta using cosine. Then simplify seven minus cosine squared theta using sine.',[
 ('REARRANGE','Isolate each squared ratio in the identity','1 − sin² θ = cos² θ\n1 − cos² θ = sin² θ',
  'Start from sine squared plus cosine squared equals one. Subtract either square to isolate the other.'),
 ('FIRST EXPRESSION','Split five into four plus one','5 − sin² θ = 4 + (1 − sin² θ)\n= 4 + cos² θ',
  'Write five as four plus one. Replace one minus sine squared by cosine squared, leaving four plus cosine squared.'),
 ('SECOND EXPRESSION','Split seven into six plus one','7 − cos² θ = 6 + (1 − cos² θ)\n= 6 + sin² θ',
  'Similarly, write seven as six plus one. Replace one minus cosine squared by sine squared.'),
 ('CHECK THE PATTERN','Replace a complete one-minus-square group','5 − sin² θ = 4 + cos² θ\n7 − cos² θ = 6 + sin² θ',
  'Look for a complete one-minus-square group. The identity replaces that whole group with the other squared ratio.')],
 g(11,8,3,5),identities=[('5-s','4+(1-s)'),('7-c','6+(1-c)')]),

authored('trigonometry-tangent-from-sine-cosine','Find tangent from sine and cosine',
 'If sin θ = 11/61 and cos θ = 60/61,\nfind tan θ.',
 '11/60',
 'Sine theta is eleven over sixty-one, and cosine theta is sixty over sixty-one. Find tangent theta.',[
 ('QUOTIENT IDENTITY','Divide sine by cosine when cosine is nonzero','tan θ = sin θ / cos θ',
  'Tangent equals sine divided by cosine. The given cosine is nonzero, so this quotient is defined.'),
 ('SUBSTITUTE','Keep each ratio as a complete fraction','tan θ = (11/61) ÷ (60/61)',
  'Substitute the two ratios, keeping the entire cosine fraction as the divisor.'),
 ('MULTIPLY BY THE RECIPROCAL','Invert the divisor, then multiply','tan θ = (11/61) × (61/60)',
  'To divide by sixty over sixty-one, multiply by its reciprocal: sixty-one over sixty.'),
 ('CANCEL','The matching hypotenuse factors cancel','tan θ = 11/60',
  'Cancel the sixty-one factors. Tangent is eleven over sixty, the opposite side divided by the adjacent side.')],
 g(11,8,3,10),expression='(11/61)/(60/61)',value='11/60',equalities=[('11**2+60**2','61**2')]),
]


def diagram(spec,d,scene,p):
    if spec['video_id']!='trigonometry-three-side-ratios' or scene not in (1,2,3):draw_card(spec,d,scene,p);return
    x,y,s=730,750,9
    d.polygon([(x,y),(x+42*s,y),(x+42*s,y-40*s)],fill='#D0E8E2',outline=v.TEAL,width=4)
    d.line((x+42*s-20,y,x+42*s-20,y-20,x+42*s,y-20),fill=v.INK,width=3)
    for pt,label in [((x+21*s,y+35),'adjacent: 42'),((x+42*s+105,y-20*s),'opposite: 40'),((x+21*s-110,y-20*s-60),'hypotenuse: 58'),((x+80,y-27),'θ')]:v.text(d,pt,label,30,v.INK,True,anchor='mm')
    centered_math(d,865,spec['displays'][scene],45,v.TEAL)


def lessons(doc):
    assert round(degrees(atan(7/9)),1)==37.9
    assert isclose(degrees(atan(7/9)),37.874984,abs_tol=1e-6)
    assert Fraction(9,41)**2+Fraction(40,41)**2==1
    assert isclose(sqrt(1600/1681),40/41)
    batch=make_lessons(SPECS,doc)
    for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:diagram(s,d,scene,p)
    return batch
