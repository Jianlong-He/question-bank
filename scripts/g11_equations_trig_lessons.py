import json,math
from pathlib import Path
from card_lessons import make_lessons,draw_card
import generate_sample_videos as v
from generate_sample_videos import text,TEAL,INK
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g11-u7-u8/lesson-specs.json').read_text())
BROWN='#b76d36';GRAY='#aab5b7'
def draw(s,d,scene,p):
 vid=s['video_id'];custom={'systems-parabola-line-intersections','systems-horizontal-curve-intersections','systems-intersection-solution-count','systems-difference-zero-graph','systems-viewing-window','systems-break-even-model','trigonometry-cosine-law-sas','trigonometry-tangent-period','trigonometry-amplitude-midline','trigonometry-extrema-cycle-model'}
 if scene in [0,4] or vid not in custom:return draw_card(s,d,scene,p)
 d.rounded_rectangle((145,350,1775,850),radius=35,fill='white')
 def lab(X,Y,t,size=25,col=INK):text(d,(X,Y),t,size,col)
 def ln(points,col=TEAL,width=4):d.line(points,fill=col,width=width)
 def setup(x0,x1,y0,y1):
  def xy(x,y):return (240+(x-x0)/(x1-x0)*530,780-(y-y0)/(y1-y0)*330)
  if y0<=0<=y1:ln([xy(x0,0),xy(x1,0)],GRAY,2)
  if x0<=0<=x1:ln([xy(0,y0),xy(0,y1)],GRAY,2)
  lab(740,795,'x',21);lab(200,415,'y',21)
  return xy
 def curve(fn,bounds,xy,col=TEAL):
  x0,x1,y0,y1=bounds;pts=[]
  for i in range(601):
   x=x0+(x1-x0)*i/600
   try:y=fn(x)
   except (ValueError,ZeroDivisionError):y=float('nan')
   if math.isfinite(y) and y0<=y<=y1:pts.append(xy(x,y))
   else:
    if len(pts)>1:ln(pts,col)
    pts=[]
  if len(pts)>1:ln(pts,col)
 def dot(xy,x,y,label,dy=10):
  X,Y=xy(x,y);d.ellipse((X-5,Y-5,X+5,Y+5),fill=INK);lab(X+6,Y+dy,label,20)
 if vid=='systems-parabola-line-intersections':
  bounds=(-4,7,-3,40);xy=setup(*bounds);curve(lambda x:x*x,bounds,xy);curve(lambda x:3*x+10,bounds,xy,BROWN);dot(xy,-2,4,'(−2,4)');dot(xy,5,25,'(5,25)');lab(250,405,'Teal: y=x²; brown: y=3x+10',23)
 elif vid=='systems-horizontal-curve-intersections':
  if scene<3:
   bounds=(-6,6,-10,25);xy=setup(*bounds);curve(lambda x:x*x-7,bounds,xy);curve(lambda x:9,bounds,xy,BROWN);dot(xy,-4,9,'(−4,9)',-32);dot(xy,4,9,'(4,9)',-32);lab(250,405,'y=x²−7 and y=9',24)
  else:
   bounds=(-12,12,-12,12);xy=lambda x,y:(500+13*x,615-13*y);ln([xy(-12,0),xy(12,0)],GRAY,2);ln([xy(0,-12),xy(0,12)],GRAY,2);pts=[xy(10*math.cos(t*math.pi/180),10*math.sin(t*math.pi/180)) for t in range(361)];ln(pts);curve(lambda x:6,bounds,xy,BROWN);dot(xy,-8,6,'(−8,6)',-32);dot(xy,8,6,'(8,6)',-32);lab(250,405,'x²+y²=100; y=6',24)
 elif vid=='systems-intersection-solution-count':
  bounds=(-3,7,0,20);xy=setup(*bounds);curve(lambda x:(x-2)**2+4,bounds,xy);height={1:3,2:4,3:13}[scene];curve(lambda x:height,bounds,xy,BROWN);lab(250,405,f'y=(x−2)²+4; line y={height}',23)
  if scene==2:dot(xy,2,4,'(2,4)',-30)
  if scene==3:dot(xy,-1,13,'(−1,13)',-30);dot(xy,5,13,'(5,13)',-30)
 elif vid=='systems-difference-zero-graph':
  bounds=(-5,5,-11,16);xy=setup(*bounds)
  if scene<3:curve(lambda x:x*x-9,bounds,xy);dot(xy,-3,0,'(−3,0)',-30);dot(xy,3,0,'(3,0)',-30);lab(250,405,'Difference h(x)=x²−9',24)
  else:curve(lambda x:x*x-3,bounds,xy);curve(lambda x:6,bounds,xy,BROWN);dot(xy,-3,6,'(−3,6)',-30);dot(xy,3,6,'(3,6)',-30);lab(250,405,'Original functions f and g',24)
 elif vid=='systems-viewing-window':
  bounds=((0,8,0,40) if scene==1 else (-8,8,0,40));xy=setup(*bounds);curve(lambda x:x*x,bounds,xy);curve(lambda x:36,bounds,xy,BROWN);dot(xy,6,36,'(6,36)',-30)
  if scene>1:dot(xy,-6,36,'(−6,36)',-30)
  lab(250,405,'Window: '+('0≤x≤8' if scene==1 else '−8≤x≤8'),24)
 elif vid=='systems-break-even-model':
  bounds=(0,20,0,340);xy=setup(*bounds);curve(lambda x:9*x+84,bounds,xy,BROWN);curve(lambda x:16*x,bounds,xy);dot(xy,12,192,'(12,192)',-30);lab(250,405,'Teal: revenue; brown: cost',24);lab(280,820,'x: units sold; y: dollars',23)
 elif vid=='trigonometry-cosine-law-sas':
  # Triangle with a=8, b=11 and included C=60 degrees.
  C=(300,775);B=(604,775);A=(300+418*.5,775-418*math.sin(math.pi/3))
  ln([C,B,A,C]);lab(C[0]-30,C[1]-15,'C',24);lab(B[0]+10,B[1]-15,'B',24);lab(A[0]-20,A[1]-35,'A',24);lab(430,785,'a=8',24);lab(310,560,'b=11',24);lab(580,560,'c',24);lab(335,730,'60°',24)
 elif vid=='trigonometry-tangent-period':
  bounds=(-math.pi/4,math.pi/4,-4,4);xy=setup(*bounds);curve(lambda x:math.tan(4*x),bounds,xy)
  for a,label in [(-math.pi/8,'−π/8'),(math.pi/8,'π/8')]:ln([xy(a,-4),xy(a,4)],BROWN,2);lab(xy(a,0)[0]-20,795,label,22)
  lab(250,405,'y=tan(4x); x in radians',24);lab(330,820,'Asymptote spacing = π/4',23)
 elif vid=='trigonometry-amplitude-midline':
  bounds=(0,8*math.pi,-5,11);xy=setup(*bounds);curve(lambda x:-6*math.sin(x/4)+3,bounds,xy);curve(lambda x:3,bounds,xy,BROWN);dot(xy,2*math.pi,-3,'(2π,−3)',-32);dot(xy,6*math.pi,9,'(6π,9)',10);lab(250,405,'y=−6sin(x/4)+3',24);lab(250,820,'One cycle: 0 to 8π radians',23)
 elif vid=='trigonometry-extrema-cycle-model':
  bounds=(0,20,0,20);xy=setup(*bounds);curve(lambda x:11+6*math.cos(math.pi*x/5),bounds,xy);curve(lambda x:11,bounds,xy,BROWN);dot(xy,5,5,'5 m',-28);dot(xy,10,17,'17 m',10);lab(250,405,'One possible phase of the depth model',22);lab(260,820,'Time (h): peaks at 0, 10 and 20',23)
 for j,line in enumerate(s['displays'][scene].split('\n')):lab(920,510+j*72,line,30,TEAL if j==0 else INK)
def lessons(doc):
 out=make_lessons(SPECS,doc)
 for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:draw(s,d,scene,p)
 return out
