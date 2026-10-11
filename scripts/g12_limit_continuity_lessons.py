import json,math
from pathlib import Path
import generate_sample_videos as v
from generate_sample_videos import text,TEAL,INK
from card_lessons import make_lessons,draw_card
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g12-u10/lesson-specs.json').read_text())
def draw(s,d,scene,p):
 vid=s['video_id'];custom={'limit-approach-versus-point','limit-one-sided-agreement','limit-squeeze-method','limit-infinite-signs'}
 if vid not in custom or scene not in [1,2,3]:return draw_card(s,d,scene,p)
 d.rounded_rectangle((145,350,1775,850),radius=35,fill='white');brown='#b76d36';gray='#abbcbd'
 bounds={'limit-approach-versus-point':(0,7,-4,16),'limit-one-sided-agreement':(0,6,0,12),'limit-squeeze-method':(0,4,-1,9),'limit-infinite-signs':(0,8,-15,15)}
 xmin,xmax,ymin,ymax=bounds[vid]
 def xy(x,y):return (265+(x-xmin)/(xmax-xmin)*490,795-(y-ymin)/(ymax-ymin)*355)
 def line(a,b,col=gray,w=2):d.line([xy(*a),xy(*b)],fill=col,width=w)
 def lab(x,y,t,dx=5,dy=-23,col=INK):X,Y=xy(x,y);text(d,(X+dx,Y+dy),t,23,col)
 def dot(x,y,t='',open=True,col=TEAL,dx=7,dy=-23):
  X,Y=xy(x,y);d.ellipse((X-6,Y-6,X+6,Y+6),fill='white' if open else col,outline=col,width=3)
  if t:lab(x,y,t,dx,dy,col)
 line((xmin,0),(xmax,0));line((xmin,ymin),(xmin,ymax));lab(xmax,0,'x',dy=2);lab(xmin,ymax,'y',dy=-25)
 def curve(fn,a,b,col=TEAL):
  part=[]
  for j in range(401):
   x=a+(b-a)*j/400;y=fn(x)
   if ymin<=y<=ymax:part.append(xy(x,y))
   else:
    if len(part)>1:d.line(part,fill=col,width=3)
    part=[]
  if len(part)>1:d.line(part,fill=col,width=3)
 if vid=='limit-approach-versus-point':
  curve(lambda x:2*x+1,xmin,xmax);dot(4,9,'(4,9)',dy=-30);dot(4,-2,'f(4)=−2',False,brown,dy=7);lab(4,0,'4',dy=6)
  ts={1:['Nearby values follow y=2x+1.','The open point is at height 9.'],2:['Left and right approach 9.','lim x→4 f(x)=9'],3:['Filled point: f(4)=−2','The limit remains 9.']}[scene]
 elif vid=='limit-one-sided-agreement':
  curve(lambda x:x+2,0,3);curve(lambda x:x+5,3,6,brown);dot(3,5,'left: 5',col=TEAL,dx=-80,dy=-30);dot(3,8,'right: 8',col=brown);dot(3,1,'f(3)=1',False,INK,dy=5)
  ts={1:['x→3− uses x<3.','Left rule x+2 approaches 5.'],2:['x→3+ uses x>3.','Right rule x+5 approaches 8.'],3:['The heights 5 and 8 differ.','No two-sided limit.']}[scene]
 elif vid=='limit-squeeze-method':
  curve(lambda x:4-(x-2)**2,0,4,brown);curve(lambda x:4+(x-2)**2,0,4);dot(2,4,'(2,4)',False,INK,dy=-30)
  ts={1:['Lower bound: 4−(x−2)² → 4','Shown in brown.'],2:['Upper bound: 4+(x−2)² → 4','Shown in teal.'],3:['Both bounds meet at height 4.','Any trapped f approaches 4.']}[scene]
 elif vid=='limit-infinite-signs':
  line((5,ymin),(5,ymax),brown);lab(5,ymax,'x=5',dy=-27,col=brown)
  fn=(lambda x:2/(x-5)) if scene<3 else (lambda x:-3/(x-5)**2)
  curve(fn,0,4.999);curve(fn,5.001,8)
  ts={1:['A: x→5− gives −∞','Negative small denominator.'],2:['A: x→5+ gives +∞','Positive small denominator.'],3:['B: both sides tend to −∞','Squared denominator stays positive.']}[scene]
 for j,t in enumerate(ts):text(d,(850,500+j*85),t,37 if j==0 else 30,TEAL if j==0 else INK)
def lessons(doc):
 out=make_lessons(SPECS,doc)
 for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:draw(s,d,scene,p)
 return out
