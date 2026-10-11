import json,math
from pathlib import Path
import generate_sample_videos as v
from generate_sample_videos import text,TEAL,INK
from card_lessons import make_lessons,draw_card
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g12-u3-u4/lesson-specs.json').read_text())
def draw(s,d,scene,p):
 vid=s['video_id'];custom={'complex-midpoint-distance-method','complex-modulus-circle-method','complex-polar-coordinate-method','complex-nth-root-circle-spacing','complex-scale-rotate-multiplication'}
 if scene in [0,4] or vid not in custom:return draw_card(s,d,scene,p)
 d.rounded_rectangle((145,350,1775,850),radius=35,fill='white');gray='#aab5b7';brown='#b76d36'
 def lab(X,Y,t,size=24,col=INK):text(d,(X,Y),t,size,col)
 if vid=='complex-midpoint-distance-method':lo,hi=-6,10
 elif vid=='complex-modulus-circle-method':lo,hi=-19,19
 elif vid=='complex-polar-coordinate-method':lo,hi=-7,7
 elif vid=='complex-nth-root-circle-spacing':lo,hi=-3,3
 else:lo,hi=-11,11
 def xy(x,y):return (280+(x-lo)/(hi-lo)*380,805-(y-lo)/(hi-lo)*380)
 d.line([xy(lo,0),xy(hi,0)],fill=gray,width=2);d.line([xy(0,lo),xy(0,hi)],fill=gray,width=2)
 lab(*xy(hi,0),' Re',20);X,Y=xy(0,hi);lab(X+8,Y-25,'Im',20)
 def line(a,b,col=TEAL):d.line([xy(*a),xy(*b)],fill=col,width=3)
 def dot(x,y,label,col=TEAL,dx=9,dy=-27):
  X,Y=xy(x,y);d.ellipse((X-6,Y-6,X+6,Y+6),fill=col);lab(X+dx,Y+dy,label,22,col)
 def circle(rad):
  X,Y=xy(-rad,rad);U,V=xy(rad,-rad);d.ellipse((X,Y,U,V),outline=gray,width=2)
 if vid=='complex-midpoint-distance-method':
  line((-4,2),(8,7));dot(-4,2,'(−4,2)');dot(8,7,'(8,7)',dx=-75)
  if scene==2:dot(2,4.5,'M=(2,9/2)',brown)
  if scene==3:line((-4,2),(8,2),brown);line((8,2),(8,7),brown);X,Y=xy(2,2);lab(X,Y+12,'12',22,brown);X,Y=xy(8,4);lab(X+10,Y,'5',22,brown)
 elif vid=='complex-modulus-circle-method':
  circle(17);line((0,0),(-8,15));dot(-8,15,'(−8,15)',dx=-45);line((-8,0),(-8,15),brown);line((0,0),(-8,0),brown);lab(295,815,'Circle: radius 17',23)
 elif vid=='complex-polar-coordinate-method':
  circle(6);line((0,0),(-3,3*math.sqrt(3)));dot(-3,3*math.sqrt(3),'(−3,3√3)',dx=-60);lab(330,805,'r=6; θ=2π/3',24)
  X,Y=xy(-1.5,1.5);lab(X,Y,'II',25,brown)
 elif vid=='complex-nth-root-circle-spacing':
  circle(2)
  for xx,yy,label in [(2,0,'2'),(0,2,'2i'),(-2,0,'−2'),(0,-2,'−2i')]:
   line((0,0),(xx,yy));dot(xx,yy,label,dx=10,dy=-25)
  lab(330,810,'Radius 2; spacing π/2',23)
 elif vid=='complex-scale-rotate-multiplication':
  line((0,0),(3,4));line((0,0),(8,-6),brown);dot(3,4,'(3,4)');dot(8,-6,'(8,−6)',brown,dx=-55,dy=14)
  if scene>=2:dot(4,-3,'(4,−3)',dx=-60,dy=-25)
  lab(310,815,'Clockwise π/2, then ×2',23)
 for j,line_ in enumerate(s['displays'][scene].split('\n')):lab(825,510+j*75,line_,28 if len(line_)<52 else 23,TEAL if j==0 else INK)
def lessons(doc):
 out=make_lessons(SPECS,doc)
 for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:draw(s,d,scene,p)
 return out
