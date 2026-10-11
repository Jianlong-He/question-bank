import json,math
from pathlib import Path
from card_lessons import make_lessons,draw_card
import generate_sample_videos as v
from generate_sample_videos import text,TEAL,INK,font
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g11-u4-u6/lesson-specs.json').read_text())
BROWN='#b76d36';GRAY='#aab5b7'
def draw(s,d,scene,p):
 vid=s['video_id'];custom={'polynomial-sign-intervals','polynomial-multiplicity-graph','logarithm-basic-inverse-graph','logarithm-shift-domain-asymptote','exponential-shift-asymptote','function-translate-points','function-reflect-input-output','function-vertical-scale','function-horizontal-scale','function-combined-point-map'}
 if scene in [0,4] or vid not in custom:return draw_card(s,d,scene,p)
 d.rounded_rectangle((145,350,1775,850),radius=35,fill='white')
 def lab(X,Y,t,size=26,col=INK):text(d,(X,Y),t,size,col)
 def ln(points,col=TEAL,width=4):d.line(points,fill=col,width=width)
 def xy_setup(xmin,xmax,ymin,ymax):
  def xy(x,y):return (240+(x-xmin)/(xmax-xmin)*530,780-(y-ymin)/(ymax-ymin)*360)
  if ymin<=0<=ymax:ln([xy(xmin,0),xy(xmax,0)],GRAY,2)
  if xmin<=0<=xmax:ln([xy(0,ymin),xy(0,ymax)],GRAY,2)
  return xy
 def curve(fn,xmin,xmax,ymin,ymax,xy,col=TEAL):
  points=[]
  for i in range(501):
   x=xmin+(xmax-xmin)*i/500
   try:y=fn(x)
   except (ValueError,ZeroDivisionError):y=float('nan')
   if math.isfinite(y) and ymin<=y<=ymax:points.append(xy(x,y))
   else:
    if len(points)>1:ln(points,col)
    points=[]
  if len(points)>1:ln(points,col)
 def dot(xy,x,y,label,dy=12,col=INK):
  X,Y=xy(x,y);d.ellipse((X-5,Y-5,X+5,Y+5),fill=col);lab(X+8,Y+dy,label,22,col)
 if vid=='polynomial-sign-intervals':
  X=lambda n:250+(n+9)/20*500
  ln([(X(-9),610),(X(11),610)],GRAY,3)
  for n in [-5,7]:d.ellipse((X(n)-6,604,X(n)+6,616),outline=INK,width=2);lab(X(n)-12,640,str(n))
  for n,t in [(-7,'+'),(1,'−'),(9,'+')]:lab(X(n)-10,525,t,42)
  if scene==3:
   ln([(X(-5),610),(X(7),610)],TEAL,8)
   for n in [-5,7]:d.ellipse((X(n)-8,602,X(n)+8,618),fill=TEAL)
  lab(295,445,'Product sign on each interval',26);lab(310,725,'Zeros: −5 and 7',26)
 elif vid=='polynomial-multiplicity-graph':
  xy=xy_setup(-6,5,-600,600);curve(lambda x:(x+4)**2*(x-3)**3,-6,5,-600,600,xy)
  dot(xy,-4,0,'−4: touches',15);dot(xy,3,0,'3: crosses',15);lab(260,365,'f(x)=(x+4)²(x−3)³',27);lab(245,797,'Vertical window: −600 to 600',23)
 elif vid=='logarithm-basic-inverse-graph':
  xy=xy_setup(-2,6,-3,6);curve(lambda x:5**x,-2,6,-3,6,xy);curve(lambda x:math.log(x,5),-2,6,-3,6,xy,BROWN)
  ln([xy(-2,-2),xy(6,6)],GRAY,2);dot(xy,1,0,'(1,0)',14,BROWN);lab(280,360,'5^x',25,TEAL);lab(510,360,'log base 5 (x)',25,BROWN);lab(295,800,'Gray diagonal: y=x',23)
 elif vid=='logarithm-shift-domain-asymptote':
  xy=xy_setup(-7,2,-5,2);curve(lambda x:math.log(x+6,4)-2,-7,2,-5,2,xy)
  ln([xy(-6,-5),xy(-6,2)],BROWN,2);dot(xy,-5,-2,'(−5,−2)',14);lab(250,365,'Vertical asymptote x=−6',25,BROWN)
 elif vid=='exponential-shift-asymptote':
  xy=xy_setup(-4,2,0,18);curve(lambda x:3**x+8,-4,2,0,18,xy)
  ln([xy(-4,8),xy(2,8)],BROWN,2);dot(xy,0,9,'(0,9)',-30);lab(250,365,'Horizontal asymptote y=8',25,BROWN)
 else:
  data={'function-translate-points':((-2,7),(-10,1),(-13,2,-1,10),'Shift left 8, down 6'),
   'function-reflect-input-output':((4,-7),(4,7) if scene<3 else (-4,-7),(-8,8,-10,10),'Outside −: negate y' if scene<3 else 'Inside −: negate x'),
   'function-vertical-scale':((-3,10),(-3,50) if scene==1 else (-3,4),(-7,2,-3,60),'Stretch ×5' if scene==1 else 'Compress ×0.4'),
   'function-horizontal-scale':((15,-2),(3,-2) if scene<3 else (90,-2),(-5,105,-5,2),'Horizontal factor 1/5' if scene<3 else 'Horizontal factor 6'),
   'function-combined-point-map':((2,-3),(-3,-3) if scene==1 else (-3,9) if scene==2 else (-3,16),(-7,6,-7,22),'Track each operation in order')}
  A,B,bounds,caption=data[vid];xy=xy_setup(*bounds);ln([xy(*A),xy(*B)],BROWN,3);dot(xy,*A,str(A),-32);dot(xy,*B,str(B),10,TEAL);lab(250,365,caption,26);lab(240,800,'Original point → image point',23)
 for j,t in enumerate(s['displays'][scene].split('\n')):
  size=38
  while d.textlength(t,font=font(size))>850:size-=1
  text(d,(865,445+j*90),t,size,TEAL)
def lessons(doc):
 out=make_lessons(SPECS,doc)
 for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:draw(s,d,scene,p)
 return out
