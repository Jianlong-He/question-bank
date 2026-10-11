"""Exact-value trigonometry examples with arithmetic and identity checks."""
from math import pi,sin,cos,tan,asin,sqrt,isclose,degrees,radians
from fractions import Fraction
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons

SPECS=[
authored('trigonometry-acute-inverse-sine','Find an acute angle from its sine',
 'An acute angle θ has sin θ = √2/2.\nFind θ in degrees.', '45 degrees',
 'An acute angle has sine root two over two. Find the angle in degrees.',[
 ('RECOGNIZE THE RATIO','Use a right isosceles triangle','Legs: 1, 1; hypotenuse: √2',
  'A right isosceles triangle with legs one and one has hypotenuse root two.'),
 ('COMPUTE ITS SINE','Opposite over hypotenuse gives the known ratio','sin 45° = 1/√2 = √2/2',
  'Each acute angle is forty-five degrees. Its sine is one over root two, which equals root two over two.'),
 ('USE THE ACUTE CONDITION','Only the first-quadrant angle is wanted','0° < θ < 90° → θ = 45°',
  'The question asks for an acute angle, so we choose the first-quadrant angle: forty-five degrees.'),
 ('INVERSE CHECK','Use degree mode if checking on a calculator','arcsin(√2/2) = 45°',
  'In degree mode, inverse sine of root two over two confirms forty-five degrees. Other sine solutions are excluded by the acute-angle condition.')],
 g(12,2,1,7),expression='(180-90)/2',value='45',equalities=[('1**2+1**2','2')]),

authored('trigonometry-sine-angle-addition-exact','Find an exact sine using angle addition',
 'Find sin 105° exactly.\nWrite the result using fractional exponents.',
 '(6^(1/2) + 2^(1/2))/4',
 'Find sine of one hundred five degrees exactly, then write the answer using fractional exponents.',[
 ('SPLIT THE ANGLE','Use two special angles','105° = 60° + 45°',
  'Split one hundred five degrees into sixty plus forty-five, whose sine and cosine values are known.'),
 ('ADDITION IDENTITY','Sine of a sum uses two products added together','sin(A + B) = sin A cos B + cos A sin B',
  'Use sine A cosine B plus cosine A sine B. Sine of a sum is not the sum of the sines.'),
 ('SUBSTITUTE','Keep the exact radical values','sin 105° = (√3/2)(√2/2) + (1/2)(√2/2)\n= (√6 + √2)/4',
  'Substitute the special-angle values. The two products are root six over four and root two over four. Add their numerators.'),
 ('FRACTIONAL EXPONENTS','A square root is a power of one half','sin 105° = (6^(1/2) + 2^(1/2))/4',
  'Replace each square root by a power of one half. The result is six to the one half plus two to the one half, all over four.')],
 g(12,2,2,6),expression='60+45',value='105',equalities=[('2*2','4'),('3*2','6')]),

authored('trigonometry-cosine-angle-addition-exact','Find an exact cosine using angle addition',
 'Find cos 105° exactly.\nWrite the result using fractional exponents.',
 '(2^(1/2) − 6^(1/2))/4',
 'Find cosine of one hundred five degrees exactly, then write the answer using fractional exponents.',[
 ('SPLIT THE ANGLE','Use sixty degrees plus forty-five degrees','105° = 60° + 45°',
  'Write one hundred five as sixty plus forty-five degrees.'),
 ('ADDITION IDENTITY','Cosine of a sum has a subtraction','cos(A + B) = cos A cos B − sin A sin B',
  'Cosine of a sum is cosine A cosine B minus sine A sine B. Keep the subtraction sign.'),
 ('SUBSTITUTE','Combine the two exact products','cos 105° = (1/2)(√2/2) − (√3/2)(√2/2)\n= (√2 − √6)/4',
  'Substitute the special-angle values. This gives root two over four minus root six over four.'),
 ('CHECK THE SIGN','Cosine is negative in Quadrant II','cos 105° = (2^(1/2) − 6^(1/2))/4',
  'Write the roots as powers of one half. The numerator is negative, matching cosine in quadrant two.')],
 g(12,2,2,7),expression='60+45',value='105',equalities=[('2*2','4'),('3*2','6')]),

authored('trigonometry-tangent-angle-addition-exact','Find an exact tangent using angle addition',
 'Find tan 105° exactly using the angle-addition identity.',
 '−2 − √3',
 'Find tangent of one hundred five degrees exactly, using the angle-addition identity.',[
 ('ADDITION IDENTITY','Use sixty plus forty-five degrees','tan(A + B) = (tan A + tan B)/(1 − tan A tan B)',
  'Use sixty plus forty-five. Tangent of a sum is the sum of the tangents divided by one minus their product.'),
 ('SUBSTITUTE','Tangent of sixty is root three; tangent of forty-five is one','tan 105° = (√3 + 1)/(1 − √3)',
  'Substitute root three and one. The numerator is root three plus one; the denominator is one minus root three.'),
 ('RATIONALIZE','Multiply top and bottom by one plus root three','[(√3 + 1)(1 + √3)]/[(1 − √3)(1 + √3)]\n= (4 + 2√3)/(1 − 3)',
  'Multiply top and bottom by one plus root three. The numerator becomes four plus two root three, and the denominator is negative two.'),
 ('SIMPLIFY','Divide both numerator terms by minus two','tan 105° = −2 − √3 = −2 − 3^(1/2)',
  'Divide by negative two. The exact answer is negative two minus root three, which has the correct negative sign in quadrant two.')],
 g(12,2,2,8),expression='1-3',value='-2',identities=[('(s+1)*(1+s)','s**2+2*s+1'),('(1-s)*(1+s)','1-s**2')]),

authored('trigonometry-cosine-double-angle-forms','Use the three cosine double-angle forms',
 'Given sin x = 7/25 and cos x = 24/25,\nfind cos(2x) and check it with the other two forms.',
 '527/625',
 'Sine x is seven over twenty-five, and cosine x is twenty-four over twenty-five. Find cosine of two x and check it with the other forms.',[
 ('FIRST FORM','Subtract sine squared from cosine squared','cos(2x) = cos² x − sin² x',
  'Start with cosine squared minus sine squared. This is the cosine double-angle identity.'),
 ('SUBSTITUTE','Use a common denominator','cos(2x) = (24/25)² − (7/25)²\n= (576 − 49)/625 = 527/625',
  'Square the two ratios and subtract. Five hundred seventy-six minus forty-nine is five hundred twenty-seven, over six hundred twenty-five.'),
 ('COSINE-ONLY FORM','Replace sine squared by one minus cosine squared','cos(2x) = 2cos² x − 1\n= 2(576/625) − 1 = 527/625',
  'Replacing sine squared by one minus cosine squared gives twice cosine squared minus one. Substitution gives the same result.'),
 ('SINE-ONLY FORM','Replace cosine squared by one minus sine squared','cos(2x) = 1 − 2sin² x\n= 1 − 2(49/625) = 527/625',
  'Replacing cosine squared gives one minus twice sine squared. All three forms agree: five hundred twenty-seven over six hundred twenty-five.')],
 g(12,2,2,10),expression='(24/25)**2-(7/25)**2',value='527/625',equalities=[('2*(24/25)**2-1','527/625'),('1-2*(7/25)**2','527/625'),('7**2+24**2','25**2')],identities=[('c-(1-c)','2*c-1'),('(1-s)-s','1-2*s')]),

authored('trigonometry-sine-double-angle-evaluate','Evaluate sine of a doubled angle',
 'Given sin x = 7/25 and cos x = 24/25, find sin(2x).',
 '336/625',
 'Sine x is seven over twenty-five, and cosine x is twenty-four over twenty-five. Find sine of two x.',[
 ('DOUBLE-ANGLE IDENTITY','Multiply twice the sine by the cosine','sin(2x) = 2sin x cos x',
  'Use the sine double-angle identity: twice sine x times cosine x.'),
 ('SUBSTITUTE','Keep both ratios in the product','sin(2x) = 2 × (7/25) × (24/25)',
  'Replace sine and cosine with their given fractions. Keep the factor of two.'),
 ('MULTIPLY','Multiply numerators and denominators','sin(2x) = (2 × 7 × 24)/(25 × 25)\n= 336/625',
  'Two times seven times twenty-four is three hundred thirty-six. Twenty-five squared is six hundred twenty-five.'),
 ('CHECK','The result must lie between minus one and one','sin(2x) = 336/625 = 0.5376',
  'The fraction is already in simplest form and equals zero point five three seven six, within the allowed sine range.')],
 g(12,2,'2Rev',3),expression='2*(7/25)*(24/25)',value='336/625',equalities=[('336/625','.5376')]),

authored('complex-polar-to-rectangular-axis-angle','Convert a polar complex number to rectangular form',
 'Write 5(cos(3π/2) + i sin(3π/2))\nin rectangular form a + bi.',
 '−5i',
 'Write five times cosine of three pi over two, plus i times sine of three pi over two, in rectangular form.',[
 ('RECTANGULAR PARTS','The cosine term is real; the sine term is imaginary','a = r cos θ; b = r sin θ',
  'In polar form, r cosine theta gives the real part. R sine theta gives the coefficient of i.'),
 ('UNIT-CIRCLE VALUES','Three pi over two points straight down','cos(3π/2) = 0; sin(3π/2) = −1',
  'Three pi over two points straight down on the unit circle. Its cosine is zero and its sine is negative one.'),
 ('MULTIPLY BY THE MODULUS','Multiply both coordinates by five','a = 5 × 0 = 0\nb = 5 × (−1) = −5',
  'Multiply both coordinates by five. The real part is zero and the imaginary coefficient is negative five.'),
 ('COMBINE','Keep i attached to the imaginary coefficient','a + bi = 0 − 5i = −5i',
  'Combine the parts: zero minus five i, or simply negative five i. Its distance from the origin is five, matching the modulus.')],
 g(12,3,3,5),expression='5*(-1)',value='-5',equalities=[('5*0','0')]),
]


def lessons(doc):
    assert isclose(degrees(asin(sqrt(2)/2)),45)
    assert isclose(sin(radians(105)),(sqrt(6)+sqrt(2))/4)
    assert isclose(cos(radians(105)),(sqrt(2)-sqrt(6))/4)
    assert isclose(tan(radians(105)),-2-sqrt(3))
    assert isclose((sqrt(3)+1)/(1-sqrt(3)),-2-sqrt(3))
    assert Fraction(7,25)**2+Fraction(24,25)**2==1
    assert abs(5*cos(3*pi/2))<1e-12 and isclose(5*sin(3*pi/2),-5)
    return make_lessons(SPECS,doc)
