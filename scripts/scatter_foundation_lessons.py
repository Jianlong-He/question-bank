"""Original plotted examples for scatter-plot vocabulary and interpretation."""
from statistics import correlation
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons
import generate_sample_videos as video

POS=[(1,2),(2,4),(3,4.5),(4,7),(5,8),(6,10)]
CURVE=[(x,1+(x-4)**2/2) for x in range(1,8)]
CLUSTER=[(4.6,5.1),(4.8,4.7),(5,5),(5.2,5.3),(5.3,4.8),(4.7,5.4),(1,2),(2,8),(8,2),(8.5,8)]
CLOUD=[(1,3),(1.3,7.2),(1.8,5.1),(2.5,1.5),(2.8,8.3),(3.4,4),(3.6,6.3),(4.3,2.3),(4.7,8.8),(5.1,5.1),(5.8,1.7),(6,7.3),(6.5,3.5),(7.1,8.5),(7.5,5.8),(8.1,1.8),(8.7,4.2),(9,7)]
STRONG=[(x,1+.6*x+e) for x,e in zip(range(1,10),[.1,-.1,.15,-.15,0,.15,-.1,.1,-.05])]
OUTLIERS=[(1,2),(2,3),(3,3.5),(4,5),(5,5.5),(6,7),(7,8),(4,9)]
assert correlation(*zip(*POS))>.98
assert abs(correlation(*zip(*CURVE)))<1e-12
assert abs(correlation(*zip(*CLOUD)))<.1
assert correlation(*zip(*STRONG))>.99
assert sum(4.5<=x<=5.5 and 4.5<=y<=5.5 for x,y in CLUSTER)==6
assert OUTLIERS[-1][1]-(OUTLIERS[-1][0]+1)==4

SPECS=[
authored('scatter-positive-linear','Recognize a positive linear association',
 'Describe the pattern in these six plotted observations.', 'Positive, approximately linear association',
 'Describe the pattern in these six plotted observations. Look at direction and form separately.',[
 ('DIRECTION','Follow the points as x increases','',
 'From left to right, the points generally rise. Larger values of x go with larger values of y.'),
 ('SIGN','An upward trend is a positive association','',
 'This is a positive association. In a context, that means the second quantity tends to increase as the first increases.'),
 ('FORM','The points roughly follow a straight path','',
 'A straight line roughly describes the pattern, so the association is approximately linear. The dots do not need to lie perfectly on a line.'),
 ('INTERPRET','Positive describes direction; linear describes form','',
 'Our answer is positive and approximately linear. A gentle upward slope is still positive. The pattern describes a tendency, not a guarantee for every observation.')],
 g(8,7,1,3),equalities=[('10-2','8')]),
authored('scatter-nonlinear-curve','Recognize a curved association',
 'Can one straight line describe this U-shaped pattern?', 'No; the association is nonlinear',
 'Can one straight line describe this U-shaped scatter pattern?',[
 ('FOLLOW THE POINTS','The values first fall and then rise','',
 'As x increases, y first falls and then rises. The points form a clear curve.'),
 ('COMPARE WITH A LINE','A single straight line misses the shape','',
 'One straight line cannot follow both sides of this pattern. A horizontal line would miss the low middle and high ends.'),
 ('NAME THE FORM','A curved association is nonlinear','',
 'This is a nonlinear association. Nonlinear means the relationship does not have a straight-line form.'),
 ('AVOID A COMMON MISTAKE','No overall straight trend does not mean no relationship','',
 'The curved pattern still shows an association. Having no overall upward or downward straight trend is different from having no visible relationship.')],
 g(8,7,1,5),equalities=[('1+(1-4)**2/2','5.5'),('1+(4-4)**2/2','1'),('1+(7-4)**2/2','5.5')]),
authored('scatter-identify-cluster','Identify a cluster of nearby observations',
 'What do we call the tightly packed group near (5, 5)?', 'A cluster',
 'What do we call the tightly packed group near five, five in this scatter plot?',[
 ('LOOK FOR DENSITY','Several points occupy a small region','',
 'Six of the observations are close together near five, five. Other points lie farther away.'),
 ('NAME THE GROUP','A dense group of nearby points is a cluster','',
 'A group of observations packed close together is called a cluster.'),
 ('KEEP BOTH COORDINATES','The clustered observations have similar x and y values','',
 'These observations have similar values on both axes. Each dot still represents its own paired observation.'),
 ('DISTINGUISH FEATURES','A cluster describes a group, not one isolated point','',
 'A cluster is a dense group. One point far from the main pattern would instead be an outlier. Describe what the dots show before guessing why the group exists.')],
 g(8,7,1,4),equalities=[('6+4','10')]),
authored('scatter-random-cloud','Recognize a plot with no clear visible association',
 'Describe the association in this scattered cloud of points.', 'No clear visible association',
 'Describe the association in this scattered cloud of points.',[
 ('SCAN LEFT TO RIGHT','High and low values appear across the plot','',
 'High and low y values appear at both small and large x values. There is no consistent rising or falling trend.'),
 ('CHECK FOR A CURVE','Look for a curved pattern as well as a straight one','',
 'Also check for a curve. Here the observations form a scattered cloud without an obvious curved path.'),
 ('STATE THE EVIDENCE','There is no clear visible association in this sample','',
 'The appropriate description is no clear visible association. Knowing x does not reveal a clear pattern for y in this sample.'),
 ('LIMIT THE CLAIM','A sample plot does not prove absolute independence','',
 'This describes the evidence in the plot. It does not prove the variables are independent in every setting. Also, zero linear correlation alone would not rule out a curved relationship.')],
 g(8,7,3,3),equalities=[('9-1','8')]),
authored('scatter-axes-and-coordinates','Interpret the axes and a paired observation',
 'A trip plot uses hours on x and kilometres on y.\nWhat does the point (3, 180) mean?', 'After 3 hours, the recorded distance is 180 km',
 'A trip plot uses hours on the x axis and kilometres on the y axis. What does the point three, one hundred eighty mean?',[
 ('READ X FIRST','The horizontal coordinate gives the time','',
 'Read the first coordinate on the horizontal axis. Three means three hours. The explanatory or input variable usually goes on this axis.'),
 ('READ Y SECOND','The vertical coordinate gives the distance','',
 'Read the second coordinate on the vertical axis. One hundred eighty means one hundred eighty kilometres. The response variable usually goes here.'),
 ('COMBINE THE PAIR','One dot records two values for the same observation','',
 'Together, the dot records a distance of one hundred eighty kilometres at three hours. Keep the axis labels and units with their coordinates.'),
 ('CHECK THE ORDER','An ordered pair always gives x before y','',
 'The point is time first, distance second. Reversing the coordinates would describe a different point, so always check the axis labels.')],
 g(8,7,2,2),equalities=[('180/60','3')]),
authored('scatter-strength-tightness','Judge linear strength by closeness to a line',
 'This plot has a gentle upward slope.\nIs the linear association strong or weak?', 'Strong positive linear association',
 'This plot has a gentle upward slope. Is the linear association strong or weak?',[
 ('CHECK SCATTER','The observations stay very close to a straight line','',
 'The dots stay very close to a straight line, with little scatter around it.'),
 ('NAME STRENGTH','Close alignment indicates a strong linear association','',
 'That close alignment means the linear association is strong. A broad cloud around a line would indicate a weaker linear pattern.'),
 ('SEPARATE DIRECTION','The rising line makes the direction positive','',
 'The line rises, so its direction is positive. Strength and direction describe different features.'),
 ('SEPARATE STEEPNESS','A gentle or steep line can have a strong association','',
 'Our answer is strong and positive. Strength depends on how closely the points follow a line, not how steep the line looks. Changing axis scales changes apparent steepness.')],
 g(8,7,5,6),equalities=[('1+.6*9','6.4'),('1+.6*1','1.6')]),
authored('scatter-identify-outlier','Identify a point far from the overall pattern',
 'Which point lies far from the main rising pattern?', 'The point (4, 9) is an outlier',
 'Which point lies far from the main rising pattern in this plot?',[
 ('FIND THE MAIN PATTERN','Most points rise along a roughly straight path','',
 'Most observations form an upward pattern. Near x equals four, that pattern has y around five.'),
 ('SPOT THE EXCEPTION','One observation lies well above its neighbours','',
 'The point four, nine lies well above the nearby pattern. It is separated vertically from the other observations.'),
 ('NAME THE FEATURE','A point far from the overall pattern is an outlier','',
 'We call this point an outlier because it is far from the main pattern.'),
 ('INVESTIGATE BEFORE REMOVING','An unusual observation is not automatically an error','',
 'An outlier might be a recording error or a valid unusual observation. Check its context before deciding what to do with it; do not automatically delete it.')],
 g(9,9,1,10),equalities=[('9-5','4')]),
]

# Plot geometry keeps room for explanatory labels beside the graph.
def axes(d,xmax=10,ymax=10,xlabel='x',ylabel='y'):
    x0,y0=330,780;w,h=810,370
    xy=lambda x,y:(x0+x/xmax*w,y0-y/ymax*h)
    for i in range(6):
        xx=xmax*i/5;yy=ymax*i/5;px,py=xy(xx,yy)
        d.line((px,y0,px,y0-h),fill='#e2e7e4',width=2)
        d.line((x0,py,x0+w,py),fill='#e2e7e4',width=2)
        video.text(d,(px,y0+14),f'{xx:g}',26,video.MUTED,anchor='mt')
        video.text(d,(x0-20,py),f'{yy:g}',26,video.MUTED,anchor='rm')
    d.line((x0,y0,x0+w,y0),fill=video.INK,width=4)
    d.line((x0,y0,x0,y0-h),fill=video.INK,width=4)
    video.text(d,(x0+w/2,y0+58),xlabel,31,video.INK,anchor='mt')
    video.text(d,(x0,y0-h-45),ylabel,31,video.INK,anchor='lm')
    return xy

PLOT_DATA={
 'scatter-positive-linear':(POS,['Six paired observations','Overall direction: upward','Positive association','Approximately linear','Direction and form are separate']),
 'scatter-nonlinear-curve':(CURVE,['A clear curved pattern','First down, then up','A straight line misses the shape','Nonlinear association','Curved pattern ≠ no association']),
 'scatter-identify-cluster':(CLUSTER,['Look for the dense group','Six points close together','Cluster near (5, 5)','Similar values on both axes','A cluster contains multiple points']),
 'scatter-random-cloud':(CLOUD,['Inspect the whole cloud','No consistent direction','No obvious curved path','No clear visible association','Describe the evidence in this sample']),
 'scatter-strength-tightness':(STRONG,['Gentle slope; points close together','Very little scatter around the line','Strong linear association','Positive direction','Strength is not steepness']),
 'scatter-identify-outlier':(OUTLIERS,['Find the unusual point','Most points follow a rising pattern','(4, 9) lies well above the pattern','Outlier at (4, 9)','Investigate unusual observations']),
 'scatter-axes-and-coordinates':([(3,180)],['Hours on x; kilometres on y','x = 3 hours','y = 180 kilometres','At 3 hours: 180 kilometres','Ordered pair: (x, y)'])}


def draw_plot(spec,d,scene,p):
    vid=spec['video_id'];points,labels=PLOT_DATA[vid]
    d.rounded_rectangle((145,330,1775,870),radius=35,fill='white')
    pair=vid=='scatter-axes-and-coordinates'
    xy=axes(d,6 if pair else 10,300 if pair else 10,'Time (hours)' if pair else 'x','Distance (km)' if pair else 'y')
    if vid=='scatter-positive-linear' and scene>=1:
        d.line([xy(1,2),xy(6,10)],fill=video.GOLD,width=4)
    if vid=='scatter-nonlinear-curve' and scene>=1:
        curve=[xy(1+i*.05,1+((1+i*.05)-4)**2/2) for i in range(121)]
        d.line(curve,fill=video.GOLD,width=4)
        if scene==2:d.line([xy(1,3),xy(7,3)],fill='#a6afb2',width=3)
    if vid=='scatter-strength-tightness' and scene>=1:
        d.line([xy(1,1.6),xy(9,6.4)],fill=video.GOLD,width=4)
    if vid=='scatter-identify-cluster' and scene>=1:
        a=xy(4.3,5.8);b=xy(5.7,4.3)
        d.ellipse((*a,*b),outline=video.GOLD,width=4)
    if vid=='scatter-identify-outlier' and scene>=1:
        d.line([xy(1,2),xy(7,8)],fill=video.GOLD,width=4)
    if pair and scene>=1:
        px,py=xy(3,180);base=xy(3,0);left=xy(0,180)
        d.line([base,(px,py)],fill=video.GOLD,width=3)
        if scene>=2:d.line([left,(px,py)],fill=video.GOLD,width=3)
    for i,(x,y) in enumerate(points):
        px,py=xy(x,y);special=vid=='scatter-identify-outlier' and i==len(points)-1 and scene>=2
        d.ellipse((px-9,py-9,px+9,py+9),fill=video.GOLD if special else video.TEAL)
        if special:video.text(d,(px+20,py-12),'(4, 9)',30,video.INK,True)
    if pair:
        px,py=xy(3,180);video.text(d,(px+20,py-40),'(3, 180)',31,video.TEAL,True)
    right={
      'scatter-positive-linear':['Direction?\nForm?','x increases\ny tends to increase','Positive','Straight overall path\nSome scatter','Positive\nApproximately linear'],
      'scatter-nonlinear-curve':['One straight line?','Direction changes','Curve fits better','Nonlinear','A relationship\ncan be curved'],
      'scatter-identify-cluster':['Dense group?','6 nearby points','A cluster','Near (5, 5)','Group of points'],
      'scatter-random-cloud':['Look for a pattern','High and low values\nacross the plot','Check curves too','No clear association','Evidence from\nthis sample'],
      'scatter-strength-tightness':['Strong or weak?','Close to the line','Strong','Positive','Closeness to line\nNOT steepness'],
      'scatter-identify-outlier':['Which point differs?','Rising main pattern','High y at x = 4','An outlier','Check the context'],
      'scatter-axes-and-coordinates':['What does\n(3, 180) mean?','First: x\nTime: 3 hours','Second: y\nDistance: 180 km','One paired\nobservation','x first\ny second']}
    for i,line in enumerate(right[vid][scene].split('\n')):
        assert d.textlength(line,font=video.font(37,True))<535,(vid,line)
        video.text(d,(1195,495+i*60),line,37,video.INK,True)
    assert d.textlength(labels[scene],font=video.font(39,True))<1680
    video.centered(d,925,labels[scene],39,video.TEAL,True)


def lessons(doc):
    result=make_lessons(SPECS,doc)
    for s in SPECS:video.DRAW[s['video_id']]=lambda d,scene,p,s=s:draw_plot(s,d,scene,p)
    return result
