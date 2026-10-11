"""Distinct graph, period and unit-circle examples with checked coordinates."""
from math import pi,sin,cos,tan,isclose
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons,draw_card,centered_math
import generate_sample_videos as v

SPECS=[
authored('trigonometry-sine-cosine-range','Find ranges and extrema of sine and cosine graphs',
 'Find the ranges, minimums and maximums of\ny = 3sin x + 2 and y = 4cos x − 3.',
 'First: [−1, 5]; second: [−7, 1]',
 'Find the range, minimum, and maximum of three sine x plus two, and four cosine x minus three.',[
 ('BASE RANGE','Sine and cosine both run from minus one to one','−1 ≤ sin x ≤ 1; −1 ≤ cos x ≤ 1',
  'On the unit circle, both coordinates run from negative one to one. So sine and cosine have that same base range.'),
 ('SCALE AND SHIFT','Multiply the endpoints by three, then add two','−3 ≤ 3sin x ≤ 3\n−1 ≤ 3sin x + 2 ≤ 5',
  'For the sine expression, multiply both endpoints by three, then add two. The range is negative one to five.'),
 ('SECOND FUNCTION','Multiply the endpoints by four, then subtract three','−4 ≤ 4cos x ≤ 4\n−7 ≤ 4cos x − 3 ≤ 1',
  'For the cosine expression, multiply the endpoints by four, then subtract three. The range is negative seven to one.'),
 ('READ THE EXTREMA','The lower endpoint is the minimum','3sin x + 2: minimum −1, maximum 5\n4cos x − 3: minimum −7, maximum 1',
  'The lower endpoint is the minimum, and the upper endpoint is the maximum. Both endpoints are reached by these graphs.')],
 g(11,8,4,5),expression='3*(-1)+2',value='-1',equalities=[('3*1+2','5'),('4*(-1)-3','-7'),('4*1-3','1')]),

authored('trigonometry-sine-cosine-period','Find the period of a sine or cosine function',
 'Find the periods of y = sin(5x) and y = cos(x/7).\nAngles are measured in radians.',
 '2π/5 and 14π',
 'Find the periods of sine of five x, and cosine of x over seven. Angles are in radians.',[
 ('PERIOD RULE','Sine and cosine repeat after an input change of two pi','Period T = 2π/|B| for sin(Bx) or cos(Bx)',
  'Sine and cosine repeat when their input increases by two pi. With coefficient B, the period in x is two pi divided by the absolute value of B.'),
 ('FIRST FUNCTION','The coefficient of x is five','sin(5x): T = 2π/5',
  'For sine of five x, B is five. The period is two pi over five. The graph repeats that distance along the x-axis.'),
 ('SECOND FUNCTION','The coefficient is one seventh, not seven','cos(x/7): B = 1/7\nT = 2π ÷ (1/7) = 14π',
  'For cosine of x over seven, B is one seventh. Dividing by one seventh multiplies by seven, giving fourteen pi.'),
 ('CHECK THE REPEAT','A whole period adds two pi to the input','5 × (2π/5) = 2π\n(1/7) × 14π = 2π',
  'Check by multiplying each period by its coefficient. Both give two pi, one full cycle. Repeating peaks are one period apart.')],
 g(11,8,5,3),expression='2/(1/7)',value='14',equalities=[('5*(2/5)','2'),('(1/7)*14','2')]),

authored('trigonometry-coefficient-from-period','Find a sine model coefficient from its period',
 'A repeating signal has a 20-minute period.\nFind positive B in sin(Bt), with t in minutes\nand the angle Bt in radians.',
 'B = π/10 radians per minute',
 'A signal repeats every twenty minutes. Find positive B in sine of B t, where t is in minutes and the angle is in radians.',[
 ('ONE FULL CYCLE','The input must increase by two pi in twenty minutes','20B = 2π',
  'Over one full cycle, the sine input increases by two pi radians. Twenty minutes times B must equal two pi.'),
 ('SOLVE FOR B','Divide by the period','B = 2π/20 = π/10',
  'Divide both sides by twenty. B equals pi over ten radians per minute.'),
 ('WRITE THE MODEL','Keep time units consistent','sin(πt/10), where t is in minutes',
  'The model is sine of pi t over ten. Keep t in minutes, because the coefficient was found using a period in minutes.'),
 ('CHECK','Recover the period from the coefficient','T = 2π ÷ (π/10) = 20 minutes',
  'Check with two pi divided by B. The result is twenty minutes, matching the required repeat time.')],
 g(11,8,6,4),expression='2/20',value='1/10',equalities=[('2/(1/10)','20')]),

authored('trigonometry-cardinal-unit-circle','Read sine and cosine at a unit-circle axis point',
 'Find sin(3π/2) and cos(3π/2)\nusing the unit circle.',
 'sin(3π/2) = −1; cos(3π/2) = 0',
 'Use the unit circle to find sine and cosine of three pi over two radians.',[
 ('LOCATE THE ANGLE','Three pi over two is a three-quarter turn','3π/2 = 270°',
  'Start on the positive x-axis and turn counterclockwise. Three pi over two is two hundred seventy degrees, pointing straight down.'),
 ('READ THE POINT','The bottom of the unit circle has coordinates zero, minus one','(x, y) = (0, −1)',
  'The unit circle has radius one. Its bottom point has coordinates zero, negative one.'),
 ('MATCH COORDINATES','Cosine is x; sine is y','(cos θ, sin θ) = (x, y)\ncos(3π/2) = 0; sin(3π/2) = −1',
  'Cosine is the horizontal coordinate, x. Sine is the vertical coordinate, y. So cosine is zero and sine is negative one.'),
 ('KEEP THE ORDER','Find the point first, then read the requested coordinate','sin(3π/2) = −1\ncos(3π/2) = 0',
  'For any axis angle, locate its point first. Read y for sine and x for cosine, keeping the signs.')],
 g(11,8,4,8),expression='3/2*180',value='270'),

authored('trigonometry-sine-cosine-intersection','Find where sine and cosine agree in an interval',
 'Solve sin x = cos x for π < x < 3π/2.',
 'x = 5π/4',
 'Find where sine x equals cosine x, between pi and three pi over two radians.',[
 ('DIVIDE BY COSINE','Cosine is nonzero inside this interval','sin x / cos x = 1 → tan x = 1',
  'Cosine is nonzero inside the given interval, so divide both sides by cosine. This gives tangent x equals one.'),
 ('REFERENCE ANGLE','Equal opposite and adjacent magnitudes give pi over four','Reference angle = π/4',
  'Tangent has magnitude one when the opposite and adjacent lengths match. The reference angle is pi over four.'),
 ('CHOOSE THE QUADRANT','The interval lies in Quadrant III','x = π + π/4 = 5π/4',
  'The interval lies in quadrant three. Add the reference angle to pi, giving five pi over four.'),
 ('CHECK','Both values are negative root two over two','sin(5π/4) = cos(5π/4) = −√2/2',
  'At five pi over four, both sine and cosine are negative root two over two. They match, and the angle lies inside the interval.')],
 g(11,8,4,7),expression='1+1/4',value='5/4'),

authored('trigonometry-tangent-first-asymptote','Find the first positive tangent asymptote',
 'Find the first positive vertical asymptote\nof y = tan(3x), with x in radians.',
 'x = π/6',
 'Find the first positive vertical asymptote of y equals tangent of three x, with x in radians.',[
 ('QUOTIENT','Tangent is undefined when its cosine denominator is zero','tan(3x) = sin(3x)/cos(3x)',
  'Tangent is sine divided by cosine. Its vertical asymptotes occur where the cosine denominator is zero.'),
 ('FIRST POSITIVE ZERO','The first positive cosine zero occurs at input pi over two','3x = π/2',
  'The first positive input where cosine is zero is pi over two. The input here is three x.'),
 ('SOLVE','Divide the input angle by three','x = (π/2)/3 = π/6',
  'Set three x equal to pi over two, then divide by three. The first positive asymptote is x equals pi over six.'),
 ('CHECK THE DENOMINATOR','The graph approaches the line but has no value there','cos(3 × π/6) = cos(π/2) = 0',
  'At this x-value the cosine denominator is zero. The graph approaches the vertical line, but tangent is undefined on it.')],
 g(11,8,4,10),expression='(1/2)/3',value='1/6'),

authored('trigonometry-cosine-starting-extremum','Decide whether a cosine graph starts at a maximum',
 'For y = −2cos x + 5, find y at x = 0.\nIs this a maximum or a minimum?',
 'y = 3, a minimum',
 'For y equals negative two cosine x plus five, find y when x is zero, and decide whether it is a maximum or minimum.',[
 ('EVALUATE COSINE','Cosine at zero is one','y(0) = −2(1) + 5 = 3',
  'Cosine of zero is one. Substitute it: negative two times one plus five is three.'),
 ('FIND THE RANGE','Multiplying by negative two reverses the endpoints','−1 ≤ cos x ≤ 1\n−2 ≤ −2cos x ≤ 2',
  'Cosine ranges from negative one to one. Multiplying by negative two reverses which input gives each endpoint, while the new range is negative two to two.'),
 ('SHIFT THE RANGE','Add five to both endpoints','3 ≤ −2cos x + 5 ≤ 7',
  'Add five to both endpoints. The graph ranges from three to seven.'),
 ('CLASSIFY','The starting value is the lower endpoint','At x = 0, y = 3: a minimum',
  'The starting value, three, is the lower endpoint, so it is a minimum. The negative coefficient flipped the original cosine maximum into a minimum.')],
 g(12,2,1,8),expression='-2*1+5',value='3',equalities=[('-2*(-1)+5','7')]),
]


def graph(d,curves,xmin,xmax,ymin,ymax,xticks,yticks,xlabel='x'):
    left,right,top,bottom=550,1370,380,760
    def xy(x,y):return left+(x-xmin)/(xmax-xmin)*(right-left),bottom-(y-ymin)/(ymax-ymin)*(bottom-top)
    for yy,label in yticks:
        Y=xy(xmin,yy)[1];d.line((left,Y,right,Y),fill='#D8E2DD',width=2)
        v.text(d,(left-22,Y),label,26,v.MUTED,anchor='rm')
    axisY=xy(xmin,0)[1] if ymin<=0<=ymax else bottom
    d.line((left,axisY,right,axisY),fill=v.INK,width=3)
    if xmin<=0<=xmax:
        X=xy(0,ymin)[0];d.line((X,top,X,bottom),fill=v.INK,width=3)
    for x,label in xticks:
        X=xy(x,ymin)[0];v.text(d,(X,bottom+25),label,26,v.INK,anchor='mm')
    v.text(d,(right+70,bottom+25),xlabel,26,v.INK,anchor='lm')
    for fn,color in curves:
        pts=[]
        for i in range(1001):
            x=xmin+(xmax-xmin)*i/1000;y=fn(x)
            if y is None or not ymin<=y<=ymax:
                if len(pts)>1:d.line(pts,fill=color,width=4)
                pts=[];continue
            pts.append(xy(x,y))
        if len(pts)>1:d.line(pts,fill=color,width=4)
    return xy


def diagram(spec,d,scene,p):
    if scene not in (1,2,3):draw_card(spec,d,scene,p);return
    vid=spec['video_id'];orange='#B66F4E'
    if vid=='trigonometry-sine-cosine-range':
        fn,lo,hi,title=(sin,-1,1,'y = sin x') if scene==1 else ((lambda x:3*sin(x)+2),-1,5,'y = 3sin x + 2') if scene==2 else ((lambda x:4*cos(x)-3),-7,1,'y = 4cos x − 3')
        graph(d,[(fn,v.TEAL)],0,2*pi,lo-1,hi+1,[(0,'0'),(pi,'π'),(2*pi,'2π')],[(lo,str(lo)),(hi,str(hi))])
        v.text(d,(1410,410),title,28,v.TEAL,True)
    elif vid=='trigonometry-sine-cosine-period':
        b=1/7 if scene==3 else 5;T=2*pi/b
        graph(d,[(lambda x:cos(b*x) if scene==3 else sin(b*x),v.TEAL)],0,2*T,-1.3,1.3,[(0,'0'),(T,'14π' if scene==3 else '2π/5'),(2*T,'28π' if scene==3 else '4π/5')],[(-1,'−1'),(1,'1')])
        v.text(d,(1410,410),'y = cos(x/7)' if scene==3 else 'y = sin(5x)',28,v.TEAL,True)
    elif vid=='trigonometry-coefficient-from-period':
        graph(d,[(lambda t:sin(pi*t/10),v.TEAL)],0,40,-1.3,1.3,[(t,str(t)) for t in (0,10,20,30,40)],[(-1,'−1'),(1,'1')],xlabel='t (min)')
    elif vid=='trigonometry-cardinal-unit-circle':
        cx,cy,R=960,555,185
        d.ellipse((cx-R,cy-R,cx+R,cy+R),outline=v.TEAL,width=4)
        d.line((cx-R-40,cy,cx+R+40,cy),fill=v.INK,width=3);d.line((cx,cy-R-35,cx,cy+R+35),fill=v.INK,width=3)
        for pt,label in [((cx+R+60,cy),'x'),((cx+25,cy-R-35),'y'),((cx+100,cy+R+20),'(0, −1)')]:v.text(d,pt,label,30,v.INK,True,anchor='mm')
        d.line((cx,cy,cx,cy+R),fill=orange,width=6);d.ellipse((cx-6,cy+R-6,cx+6,cy+R+6),fill=orange)
        pts=[(cx+100*cos(i*pi/180),cy-100*sin(i*pi/180)) for i in range(271)];d.line(pts,fill=orange,width=4)
        ex,ey=pts[-1];d.polygon([(ex,ey),(ex-15,ey-7),(ex-15,ey+7)],fill=orange)
        v.text(d,(cx-260,cy-120),'270°',30,v.INK,True,anchor='mm')
    elif vid=='trigonometry-sine-cosine-intersection':
        xy=graph(d,[(sin,v.TEAL),(cos,orange)],pi,1.5*pi,-1.2,.2,[(pi,'π'),(1.25*pi,'5π/4'),(1.5*pi,'3π/2')],[(-1,'−1'),(0,'0')])
        x,y=xy(1.25*pi,sin(1.25*pi));d.ellipse((x-7,y-7,x+7,y+7),fill=v.INK)
        v.text(d,(1420,410),'sin x',30,v.TEAL,True);v.text(d,(1420,455),'cos x',30,orange,True)
    elif vid=='trigonometry-tangent-first-asymptote':
        xy=graph(d,[(lambda x:tan(3*x) if abs(cos(3*x))>1e-6 else None,v.TEAL)],0,pi/3,-3,3,[(0,'0'),(pi/6,'π/6'),(pi/3,'π/3')],[(-2,'−2'),(0,'0'),(2,'2')])
        X=xy(pi/6,0)[0]
        for y in range(380,755,22):d.line((X,y,X,y+11),fill=orange,width=3)
        v.text(d,(1410,410),'y = tan(3x)',29,v.TEAL,True)
    else:
        xy=graph(d,[(lambda x:-2*cos(x)+5,v.TEAL)],0,2*pi,0,8,[(0,'0'),(pi,'π'),(2*pi,'2π')],[(0,'0'),(3,'3'),(5,'5'),(7,'7')])
        X,Y=xy(0,3);d.ellipse((X-6,Y-6,X+6,Y+6),fill=orange)
    for i,line in enumerate(spec['displays'][scene].split('\n')):centered_math(d,855+i*56,line,38,v.TEAL)


def lessons(doc):
    assert isclose(sin(1.25*pi),cos(1.25*pi)) and pi<1.25*pi<1.5*pi
    assert abs(cos(3*pi/6))<1e-12 and isclose(sin(3*pi/2),-1) and abs(cos(3*pi/2))<1e-12
    for x in (.11,.73,1.2):
        assert isclose(sin(5*(x+2*pi/5)),sin(5*x),abs_tol=1e-12)
        assert isclose(cos((x+14*pi)/7),cos(x/7),abs_tol=1e-12)
        assert isclose(sin(pi*(x+20)/10),sin(pi*x/10),abs_tol=1e-12)
    batch=make_lessons(SPECS,doc)
    for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:diagram(s,d,scene,p)
    return batch
