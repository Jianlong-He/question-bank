import json,math
from pathlib import Path
from card_lessons import make_lessons,draw_card
import generate_sample_videos as v
from generate_sample_videos import text,TEAL,INK
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g11-u13/lesson-specs.json').read_text())
BROWN='#b76d36';GRAY='#aab5b7'
def draw(s,d,scene,p):
 vid=s['video_id'];custom={'rational-reciprocal-parent-reflection','rational-shifted-reciprocal-asymptotes','rational-horizontal-degree-rules','rational-intercepts-and-factors','rational-hole-pole-distinction','rational-cross-horizontal-asymptote','rational-shared-cost-model'}
 if scene in [0,4] or vid not in custom:return draw_card(s,d,scene,p)
 d.rounded_rectangle((145,350,1775,850),radius=35,fill='white')
 def lab(X,Y,t,size=25,col=INK):text(d,(X,Y),t,size,col)
 def ln(points,col=TEAL,width=4):d.line(points,fill=col,width=width)
 def setup(x0,x1,y0,y1):
  def xy(x,y):return (245+(x-x0)/(x1-x0)*535,780-(y-y0)/(y1-y0)*325)
  if y0<=0<=y1:ln([xy(x0,0),xy(x1,0)],GRAY,2)
  if x0<=0<=x1:ln([xy(0,y0),xy(0,y1)],GRAY,2)
  lab(785,783,'x',22);lab(212,438,'y',22)
  return xy
 def curve(fn,bounds,xy,col=TEAL):
  x0,x1,y0,y1=bounds;pts=[]
  for i in range(901):
   x=x0+(x1-x0)*i/900
   try:y=fn(x)
   except (ValueError,ZeroDivisionError):y=float('nan')
   if math.isfinite(y) and y0<=y<=y1:pts.append(xy(x,y))
   else:
    if len(pts)>1:ln(pts,col)
    pts=[]
  if len(pts)>1:ln(pts,col)
 def vertical(x,bounds,xy,label):
  X,Y=xy(x,bounds[2]);top=xy(x,bounds[3])[1]
  for yy in range(int(top),int(Y),18):ln([(X,yy),(X,min(yy+9,Y))],BROWN,2)
  lab(X-25,795,label,23,BROWN)
 def horizontal(y,bounds,xy,label):
  X,Y=xy(bounds[0],y);right=xy(bounds[1],y)[0]
  for xx in range(int(X),int(right),18):ln([(xx,Y),(min(xx+9,right),Y)],BROWN,2)
  lab(250,Y-30,label,22,BROWN)
 def dot(xy,x,y,label,dy=-33,hole=False):
  X,Y=xy(x,y);d.ellipse((X-7,Y-7,X+7,Y+7),fill='white' if hole else INK,outline=TEAL if hole else INK,width=3);lab(X+10,Y+dy,label,22)
 if vid=='rational-reciprocal-parent-reflection':
  b=(-6,6,-6,6);xy=setup(*b);fn=(lambda x:1/x) if scene<3 else (lambda x:-4/x);curve(fn,b,xy);lab(260,405,'y=1/x' if scene<3 else 'y=−4/x',28)
  if scene<3:dot(xy,2,.5,'(2,1/2)');dot(xy,-2,-.5,'(−2,−1/2)',12)
  else:dot(xy,2,-2,'(2,−2)',12);dot(xy,-2,2,'(−2,2)')
  lab(620,465,'I',24);lab(275,465,'II',24);lab(275,742,'III',24);lab(620,742,'IV',24)
 elif vid=='rational-shifted-reciprocal-asymptotes':
  b=(-10,2,-13,1);xy=setup(*b);curve(lambda x:3/(x+4)-6,b,xy);vertical(-4,b,xy,'−4');horizontal(-6,b,xy,'y=−6');dot(xy,-5,-9,'(−5,−9)',12);dot(xy,-3,-3,'(−3,−3)');lab(250,405,'f(x)=3/(x+4)−6',27)
 elif vid=='rational-horizontal-degree-rules':
  if scene==1:b=(-10,10,-.2,.8);fn=lambda x:5/(x*x+9);label='A=5/(x²+9)';H=0
  elif scene==2:b=(-8,8,-4,11);fn=lambda x:(7*x+2)/(2*x-1);label='B=(7x+2)/(2x−1)';H=3.5
  else:b=(-8,8,-12,10);fn=lambda x:(x*x+3)/(x+2);label='C=(x²+3)/(x+2)';H=None
  xy=setup(*b);curve(fn,b,xy);lab(250,405,label,26)
  if H is not None:horizontal(H,b,xy,'y='+str(H))
  else:curve(lambda x:x-2,b,xy,BROWN);lab(255,810,'Brown: slant line y=x−2',24)
 elif vid=='rational-intercepts-and-factors':
  b=(-10,10,-5,5);xy=setup(*b);curve(lambda x:(x+6)/(x-4),b,xy);vertical(4,b,xy,'4');dot(xy,-6,0,'(−6,0)');dot(xy,0,-1.5,'(0,−3/2)',12);lab(250,405,'f(x)=(x+6)/(x−4)',26)
 elif vid=='rational-hole-pole-distinction':
  b=(-7,10,-3,3);xy=setup(*b);curve(lambda x:(x+2)/((x-6)*(x+3)),b,xy);vertical(-3,b,xy,'−3');vertical(6,b,xy,'6');dot(xy,4,-3/7,'hole (4,−3/7)',-45,True);lab(250,405,'Reduced curve with original hole',25)
 elif vid=='rational-cross-horizontal-asymptote':
  b=(-10,10,2.6,3.4);xy=setup(*b);curve(lambda x:3+x/(x*x+4),b,xy);horizontal(3,b,xy,'y=3');dot(xy,0,3,'(0,3)',16);lab(250,405,'f(x)=3+x/(x²+4)',26);lab(250,815,'Below for x<0; above for x>0',24)
 elif vid=='rational-shared-cost-model':
  b=(0,28,0,90);xy=setup(*b)
  for n in range(2,29):
   X,Y=xy(n,168/n);d.ellipse((X-4,Y-4,X+4,Y+4),fill=TEAL)
  dot(xy,7,24,'(7,24)',-35);dot(xy,14,12,'(14,12)',-35);lab(250,405,'S(n)=168/n; positive integer n',25);lab(250,815,'n: people; S: dollars per person',24)
 for j,line in enumerate(s['displays'][scene].split('\n')):lab(920,505+j*76,line,29 if len(line)<47 else 24,TEAL if j==0 else INK)
def lessons(doc):
 out=make_lessons(SPECS,doc)
 for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:draw(s,d,scene,p)
 return out
