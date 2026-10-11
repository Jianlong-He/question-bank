"""Bounded and general trig equations, with exact solution-set checks."""
from math import pi,sin,cos,tan,sqrt,isclose
from fractions import Fraction as F
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons,draw_card,centered_math
from trig_graph_lessons import graph
import generate_sample_videos as v

SPECS=[
# Keep the existing draft ID stable while narrowing its reviewed teaching method.
authored('trigonometry-right-triangles','Solve sine and cosine zero equations on an interval',
 'Solve sin x = 0 and cos x = 0 separately\non the interval 2π ≤ x ≤ 4π.',
 'Sine: 2π, 3π, 4π; cosine: 5π/2, 7π/2',
 'Solve sine x equals zero and cosine x equals zero separately, from two pi through four pi, including both endpoints.',[
 ('ZERO COORDINATES','Sine reads y; cosine reads x on the unit circle','Sine zeros: x = kπ\nCosine zeros: x = π/2 + kπ; k is an integer',
  'Sine is zero at integer multiples of pi. Cosine is zero at pi over two plus integer multiples of pi.'),
 ('SINE EQUATION','Keep only multiples of pi inside the interval','sin x = 0: x = 2π, 3π, 4π',
  'Within the interval, the sine solutions are two pi, three pi, and four pi.'),
 ('COSINE EQUATION','Keep only the half-integer multiples in the interval','cos x = 0: x = 5π/2, 7π/2',
  'The cosine solutions in this interval are five pi over two and seven pi over two.'),
 ('CHECK ENDPOINTS','Both endpoints are included here','Sine: 2π, 3π, 4π\nCosine: 5π/2, 7π/2',
  'Both endpoints are included, so keep the sine solutions there. With a strict upper bound, four pi would be excluded. Always check the interval symbols.')],
 g(12,2,6,1),expression='2+1/2',value='5/2',equalities=[('3+1/2','7/2')]),

authored('trigonometry-bounded-cosine-two-solutions','Solve a cosine equation in one full turn',
 'Solve cos x = √2/2 for 0 ≤ x < 2π.\nList all solutions in increasing order.',
 'π/4, 7π/4',
 'Solve cosine x equals root two over two, from zero inclusive to two pi exclusive.',[
 ('REFERENCE ANGLE','Recognize the positive reference value','Reference angle = π/4',
  'The reference angle is pi over four, because cosine of forty-five degrees is root two over two.'),
 ('QUADRANTS','Cosine is positive in Quadrants I and IV','x = π/4 or x = 2π − π/4',
  'Cosine is positive in quadrants one and four. Use the reference angle in quadrant one, and subtract it from two pi in quadrant four.'),
 ('SIMPLIFY','Write the two angles in increasing order','x = π/4, 7π/4',
  'Two pi minus pi over four is seven pi over four. The solutions are pi over four and seven pi over four.'),
 ('CHECK THE INTERVAL','Both solutions lie inside the stated bounds','cos(π/4) = cos(7π/4) = √2/2',
  'Both angles satisfy the equation and the interval. At zero and two pi, cosine is one, so neither endpoint adds a solution.')],
 g(12,2,6,2),expression='2-1/4',value='7/4'),

authored('trigonometry-bounded-sine-two-solutions','Solve a sine equation using two quadrants',
 'Solve sin x = −√3/2 for 0 ≤ x < 2π.\nList all solutions in increasing order.',
 '4π/3, 5π/3',
 'Solve sine x equals negative root three over two, from zero inclusive to two pi exclusive.',[
 ('REFERENCE ANGLE','Ignore the sign while finding the acute reference angle','Reference angle = π/3',
  'The positive magnitude root three over two has reference angle pi over three, or sixty degrees.'),
 ('QUADRANTS','Sine is negative below the horizontal axis','Quadrants III and IV',
  'Sine is the vertical coordinate. A negative sine places the solutions in quadrants three and four.'),
 ('BUILD THE ANGLES','Add to pi, or subtract from two pi','x = π + π/3 = 4π/3\nx = 2π − π/3 = 5π/3',
  'In quadrant three, add the reference angle to pi. In quadrant four, subtract it from two pi. This gives four pi over three and five pi over three.'),
 ('CHECK','Both have the required negative sine value','x = 4π/3, 5π/3',
  'Both angles lie in the interval and have sine negative root three over two. Include both solutions, not just the inverse-sine calculator result.')],
 g(12,2,'6HW',5),expression='1+1/3',value='4/3',equalities=[('2-1/3','5/3')]),

authored('trigonometry-bounded-sine-extremum','Solve a sine peak equation over several turns',
 'Solve sin x = 1 for 2π ≤ x < 6π.',
 '5π/2, 9π/2',
 'Solve sine x equals one, from two pi inclusive to six pi exclusive.',[
 ('ONE PEAK PER TURN','Sine equals one at the top of the unit circle','First peak: x = π/2',
  'Sine equals one at the top of the unit circle. The first peak is pi over two.'),
 ('REPEAT','Add whole turns of two pi','x = π/2 + 2kπ; k is an integer',
  'The same peak repeats every two pi. Add integer multiples of two pi to get all candidates.'),
 ('FILTER THE CANDIDATES','Select the candidates in the requested interval','k = 1 → x = 5π/2\nk = 2 → x = 9π/2',
  'In the requested interval, k equals one or two. These give five pi over two and nine pi over two.'),
 ('CHECK THE BOUNDS','The next candidates lie outside the interval','x = 5π/2, 9π/2',
  'Pi over two is below the interval, and thirteen pi over two is above it. The endpoints have sine zero, so there are exactly two solutions.')],
 g(12,2,'6Rev',2),expression='1/2+2',value='5/2',equalities=[('1/2+4','9/2'),('1/2+6','13/2')]),

authored('trigonometry-bounded-tangent-solutions','Solve a tangent equation using its pi period',
 'Solve tan x = √3 for 0 ≤ x < 2π.',
 'π/3, 4π/3',
 'Solve tangent x equals root three, from zero inclusive to two pi exclusive.',[
 ('FIRST SOLUTION','Recognize the sixty-degree tangent value','tan(π/3) = √3',
  'Tangent of pi over three is root three, giving our first solution.'),
 ('PERIOD','Tangent repeats every pi radians','x = π/3 + kπ; k is an integer',
  'Tangent repeats every pi radians. Add integer multiples of pi, rather than two pi, to find every solution.'),
 ('FILTER','Keep candidates in the given interval','k = 0 → π/3\nk = 1 → 4π/3',
  'Within the interval, k can be zero or one. The solutions are pi over three and four pi over three.'),
 ('CHECK','Tangent is defined at both selected angles','x = π/3, 4π/3',
  'Both angles have tangent root three and nonzero cosine. The next candidate is beyond two pi, so the list is complete.')],
 g(12,2,6,5),expression='1/3+1',value='4/3'),

authored('trigonometry-scaled-sine-zero-equation','Solve a sine equation with a multiple-angle input',
 'Solve sin(3x) = 0 for 0 ≤ x ≤ π.',
 '0, π/3, 2π/3, π',
 'Solve sine of three x equals zero, from zero through pi, including both endpoints.',[
 ('CHANGE THE INPUT','Let u equal three x and transform the interval','u = 3x; 0 ≤ u ≤ 3π',
  'Let u equal three x. Multiplying the interval by three gives zero through three pi for u.'),
 ('SOLVE FOR U','Sine is zero at integer multiples of pi','u = 0, π, 2π, 3π',
  'In that expanded interval, sine is zero at zero, pi, two pi, and three pi.'),
 ('RETURN TO X','Divide every candidate by three','x = 0, π/3, 2π/3, π',
  'Divide every candidate by three to return to x. Keep all four solutions.'),
 ('CHECK','Substitution returns the four sine-zero inputs','3x = 0, π, 2π, 3π',
  'Substituting the four x-values gives the four sine-zero inputs again. Both original endpoints are included, so zero and pi stay in the answer.')],
 g(12,2,6,6),expression='3/3',value='1',equalities=[('3*(1/3)','1'),('3*(2/3)','2')]),

authored('trigonometry-general-extremum-family','Write all solutions of a trig extremum equation',
 'Write the general solution of sin(2x) = −1.\nAngles are in radians.',
 'x = 3π/4 + kπ, for any integer k',
 'Write all solutions of sine of two x equals negative one, with angles in radians.',[
 ('ONE CYCLE','The sine input reaches minus one at three pi over two','2x = 3π/2 in one cycle',
  'Sine equals negative one at the bottom of the unit circle. The input angle in one cycle is three pi over two.'),
 ('ALL CYCLES','Add full turns to the input angle','2x = 3π/2 + 2kπ; k is an integer',
  'Add any integer number of full turns to the input: two k pi. This includes positive and negative cycles.'),
 ('ISOLATE X','Divide every term by two','x = 3π/4 + kπ; k is an integer',
  'Divide every term by two. The general solution is three pi over four plus k pi, for any integer k.'),
 ('CHECK','Doubling the answer returns a sine minimum','sin(2x) = sin(3π/2 + 2kπ) = −1',
  'Doubling any angle in this family gives a sine minimum plus full turns. The family is complete because there is one sine minimum per cycle.')],
 g(12,2,6,3),expression='(3/2)/2',value='3/4',equalities=[('2/2','1')]),

authored('trigonometry-general-sine-two-families','Write both general solution families for sine',
 'Write the general solution of sin x = −√2/2.',
 'x = 5π/4 + 2kπ or 7π/4 + 2kπ, k an integer',
 'Write all solutions of sine x equals negative root two over two.',[
 ('REFERENCE AND SIGN','The reference angle is pi over four; sine is negative','Quadrants III and IV; reference angle π/4',
  'The reference angle is pi over four. Negative sine places the angles in quadrants three and four.'),
 ('ONE CYCLE','Find both solutions before adding full turns','x = π + π/4 = 5π/4\nx = 2π − π/4 = 7π/4',
  'In one cycle, the angles are five pi over four and seven pi over four.'),
 ('REPEAT BOTH','Sine repeats every two pi radians','x = 5π/4 + 2kπ or x = 7π/4 + 2kπ\nk is any integer',
  'Add two k pi to each starting angle, with k any integer. Keep both families.'),
 ('CHECK COMPLETENESS','Each full turn has two matching points','Both families are required.',
  'Each full turn has two points with this sine value. One family would miss half the solutions; the two families together cover them all.')],
 g(12,2,6,9),expression='1+1/4',value='5/4',equalities=[('2-1/4','7/4')]),
]


def diagram(spec,d,scene,p):
    vid=spec['video_id']
    if scene not in (1,2,3) or vid in ('trigonometry-general-extremum-family','trigonometry-general-sine-two-families'):
        draw_card(spec,d,scene,p);return
    orange='#B66F4E'
    if vid=='trigonometry-right-triangles':
        graph(d,[(sin,v.TEAL),(cos,orange)],2*pi,4*pi,-1.3,1.3,[(2*pi,'2π'),(2.5*pi,'5π/2'),(3*pi,'3π'),(3.5*pi,'7π/2'),(4*pi,'4π')],[(-1,'−1'),(0,'0'),(1,'1')])
        v.text(d,(1450,410),'sin x',28,v.TEAL,True);v.text(d,(1450,455),'cos x',28,orange,True)
    elif vid=='trigonometry-bounded-cosine-two-solutions':
        graph(d,[(cos,v.TEAL),(lambda x:sqrt(2)/2,orange)],0,2*pi,-1.3,1.3,[(0,'0'),(pi/4,'π/4'),(pi,'π'),(7*pi/4,'7π/4'),(2*pi,'2π')],[(-1,'−1'),(0,'0'),(sqrt(2)/2,'√2/2')])
    elif vid=='trigonometry-bounded-sine-two-solutions':
        graph(d,[(sin,v.TEAL),(lambda x:-sqrt(3)/2,orange)],0,2*pi,-1.3,1.3,[(0,'0'),(pi,'π'),(4*pi/3,'4π/3'),(5*pi/3,'5π/3'),(2*pi,'2π')],[(-sqrt(3)/2,'−√3/2'),(0,'0'),(1,'1')])
    elif vid=='trigonometry-bounded-sine-extremum':
        graph(d,[(sin,v.TEAL),(lambda x:1,orange)],2*pi,6*pi,-1.3,1.3,[(2*pi,'2π'),(2.5*pi,'5π/2'),(4.5*pi,'9π/2'),(6*pi,'6π')],[(-1,'−1'),(0,'0'),(1,'1')])
    elif vid=='trigonometry-bounded-tangent-solutions':
        graph(d,[(lambda x:tan(x) if abs(cos(x))>1e-6 else None,v.TEAL),(lambda x:sqrt(3),orange)],0,2*pi,-3,3,[(0,'0'),(pi/3,'π/3'),(pi,'π'),(4*pi/3,'4π/3'),(2*pi,'2π')],[(-2,'−2'),(0,'0'),(sqrt(3),'√3')])
    else:
        graph(d,[(lambda x:sin(3*x),v.TEAL)],0,pi,-1.3,1.3,[(0,'0'),(pi/3,'π/3'),(2*pi/3,'2π/3'),(pi,'π')],[(-1,'−1'),(0,'0'),(1,'1')])
        v.text(d,(1450,410),'sin(3x)',28,v.TEAL,True)
    for i,line in enumerate(spec['displays'][scene].split('\n')):centered_math(d,855+i*56,line,38,v.TEAL)


def roots(offsets,period,low,high,closed=False):
    return sorted({a+k*period for a in offsets for k in range(-20,21) if low<=a+k*period and (a+k*period<=high if closed else a+k*period<high)})


def lessons(doc):
    # Root locations are rational multiples of pi; verify endpoint filtering exactly.
    assert roots([F(0)],F(1),F(2),F(4),True)==[F(2),F(3),F(4)]
    assert roots([F(1,2)],F(1),F(2),F(4),True)==[F(5,2),F(7,2)]
    assert roots([F(1,4),F(7,4)],F(2),F(0),F(2))==[F(1,4),F(7,4)]
    assert roots([F(4,3),F(5,3)],F(2),F(0),F(2))==[F(4,3),F(5,3)]
    assert roots([F(1,2)],F(2),F(2),F(6))==[F(5,2),F(9,2)]
    assert roots([F(1,3)],F(1),F(0),F(2))==[F(1,3),F(4,3)]
    assert roots([F(0)],F(1,3),F(0),F(1),True)==[F(0),F(1,3),F(2,3),F(1)]
    for r in (1/4,7/4):assert isclose(cos(r*pi),sqrt(2)/2)
    for r in (4/3,5/3):assert isclose(sin(r*pi),-sqrt(3)/2)
    for k in range(-10,11):
        assert isclose(sin(2*(3*pi/4+k*pi)),-1,abs_tol=1e-12)
        for r in (5/4,7/4):assert isclose(sin(r*pi+2*k*pi),-sqrt(2)/2,abs_tol=1e-12)
    batch=make_lessons(SPECS,doc)
    for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:diagram(s,d,scene,p)
    return batch
