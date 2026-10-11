import json,math
from pathlib import Path
import generate_sample_videos as v
from generate_sample_videos import text,TEAL,INK
from card_lessons import make_lessons,draw_card
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g12-u5-u7/lesson-specs.json').read_text())
def draw(s,d,scene,p):
 vid=s['video_id'];custom={'ellipse-center-axes-method','ellipse-foci-eccentricity-method','hyperbola-center-vertices-method','hyperbola-focus-asymptote-method','vector-read-components-method','vector-magnitude-distance-method','vector-scalar-multiply-method','vector-add-subtract-method','vector-direction-quadrant-method','vector-magnitude-angle-components','vector-collinear-forces-method','vector-motion-distance-method'}
 if scene in [0,4] or vid not in custom:return draw_card(s,d,scene,p)
 d.rounded_rectangle((145,350,1775,850),radius=35,fill='white');gray='#adb9ba';brown='#b76d36'
 def lab(X,Y,t,size=22,col=INK):text(d,(X,Y),t,size,col)
 bounds={
 'ellipse-center-axes-method':(-10,8,-7,9),'ellipse-foci-eccentricity-method':(-15,15,-10,10),
 'hyperbola-center-vertices-method':(-8,10,-11,7),'hyperbola-focus-asymptote-method':(-16,16,-16,16),
 'vector-read-components-method':(-10,4,-4,11),'vector-magnitude-distance-method':(-11,5,-7,13),
 'vector-scalar-multiply-method':(-7,11,-9,6),'vector-add-subtract-method':(-4,12,-4,12),
 'vector-direction-quadrant-method':(-8,18,-3,19),'vector-magnitude-angle-components':(-16,16,-16,16),
 'vector-collinear-forces-method':(-9,21,-9,9),'vector-motion-distance-method':(-3,20,-3,20)}
 xmin,xmax,ymin,ymax=bounds[vid]
 if vid=='vector-add-subtract-method' and scene==3:xmin,xmax,ymin,ymax=-5,7,-12,4
 scale=min(430/(xmax-xmin),355/(ymax-ymin));ox=260+(430-(xmax-xmin)*scale)/2;oy=805-(355-(ymax-ymin)*scale)/2
 def xy(x,y):return(ox+(x-xmin)*scale,oy-(y-ymin)*scale)
 d.line([xy(xmin,0),xy(xmax,0)],fill=gray,width=2);d.line([xy(0,ymin),xy(0,ymax)],fill=gray,width=2)
 X,Y=xy(xmax,0);lab(X+6,Y,'x',18);X,Y=xy(0,ymax);lab(X+6,Y-20,'y',18)
 def line(a,b,col=TEAL,width=3):d.line([xy(*a),xy(*b)],fill=col,width=width)
 def arrow(a,b,col=TEAL):
  line(a,b,col);X,Y=xy(*b);U,V=xy(*a);ang=math.atan2(Y-V,X-U)
  for delta in [-.45,.45]:d.line([(X,Y),(X-12*math.cos(ang+delta),Y-12*math.sin(ang+delta))],fill=col,width=3)
 def dot(x,y,t='',col=TEAL,dx=7,dy=-24):
  X,Y=xy(x,y);d.ellipse((X-5,Y-5,X+5,Y+5),fill=col)
  if t:lab(X+dx,Y+dy,t,19,col)
 def ellipse(h,k,a,b):
  X,Y=xy(h-a,k+b);U,V=xy(h+a,k-b);d.ellipse((X,Y,U,V),outline=TEAL,width=3)
 def curve(points,col=TEAL):
  good=[]
  for x,y in points:
   if xmin<=x<=xmax and ymin<=y<=ymax:good.append(xy(x,y))
   else:
    if len(good)>1:d.line(good,fill=col,width=3)
    good=[]
  if len(good)>1:d.line(good,fill=col,width=3)
 if vid=='ellipse-center-axes-method':
  ellipse(-1,2,7,4);dot(-1,2,'C',brown);dot(-8,2,'(−8,2)',dx=-15,dy=8);dot(6,2,'(6,2)',dx=-30,dy=8)
  if scene>=2:dot(-1,-2,'(−1,−2)',dy=7);dot(-1,6,'(−1,6)',dx=-30)
 elif vid=='ellipse-foci-eccentricity-method':
  ellipse(0,0,13,5);dot(-12,0,'F1',brown,dx=-20,dy=8);dot(12,0,'F2',brown,dx=-10,dy=8);dot(13,0,'V',dx=0,dy=-25)
 elif vid=='hyperbola-center-vertices-method':
  for sign in [-1,1]:curve([(1+xx,-2+sign*4*math.sqrt(1+xx*xx/9)) for xx in [j/20 for j in range(-180,181)]])
  dot(1,-2,'C',brown);dot(1,-6,'(1,−6)',dy=5);dot(1,2,'(1,2)')
 elif vid=='hyperbola-focus-asymptote-method':
  for sign in [-1,1]:curve([(sign*5*math.sqrt(1+yy*yy/144),yy) for yy in [j/10 for j in range(-160,161)]])
  curve([(x,12*x/5) for x in [j/10 for j in range(-160,161)]],gray);curve([(x,-12*x/5) for x in [j/10 for j in range(-160,161)]],gray)
  dot(-13,0,'−13',brown,dx=-18,dy=8);dot(13,0,'13',brown,dy=8);dot(5,0,'5',dy=-25)
 elif vid=='vector-read-components-method':
  arrow((0,0),(-7,9));line((0,0),(-7,0),brown);line((-7,0),(-7,9),brown);dot(-7,9,'(−7,9)',dx=-15)
 elif vid=='vector-magnitude-distance-method':
  arrow((1,-4),(-7,11));dot(1,-4,'A(1,−4)',dx=-10,dy=7);dot(-7,11,'B(−7,11)',dx=-20);line((1,-4),(-7,-4),brown);line((-7,-4),(-7,11),brown)
 elif vid=='vector-scalar-multiply-method':
  arrow((0,0),(-4,3));arrow((0,0),(8,-6),brown);dot(-4,3,'v=(−4,3)',dx=-30);dot(8,-6,'−2v=(8,−6)',dx=-100,dy=8)
 elif vid=='vector-add-subtract-method':
  if scene==3:
   arrow((0,0),(4,-1));arrow((0,0),(-2,-9));line((4,-1),(2,-10),gray);line((-2,-9),(2,-10),gray);arrow((0,0),(2,-10),brown);dot(4,-1,'u');dot(-2,-9,'−v',dx=-25);dot(2,-10,'u−v',brown,dy=8)
  else:
   arrow((0,0),(4,-1));arrow((0,0),(2,9));line((4,-1),(6,8),gray);line((2,9),(6,8),gray);arrow((0,0),(6,8),brown);dot(4,-1,'u',dy=8);dot(2,9,'v');dot(6,8,'u+v',brown)
 elif vid=='vector-direction-quadrant-method':
  arrow((0,0),(-5,5));arrow((0,0),(8,15),brown);dot(-5,5,'v',dx=-20);dot(8,15,'w',brown)
 elif vid=='vector-magnitude-angle-components':
  arrow((0,0),(-7,7*math.sqrt(3)));line((0,0),(-7,0),brown);line((-7,0),(-7,7*math.sqrt(3)),brown);dot(-7,7*math.sqrt(3),'(−7,7√3)',dx=-40);lab(300,815,'θ=120°; r=14',22)
 elif vid=='vector-collinear-forces-method':
  arrow((0,4),(18,4));arrow((0,0),(-7,0),brown);arrow((0,-4),(11,-4));lab(320,815,'18 east − 7 west → 11 east',20)
 elif vid=='vector-motion-distance-method':
  arrow((0,0),(8,0));arrow((8,0),(8,15));arrow((0,0),(8,15),brown);dot(8,0,'8',dy=7);dot(8,15,'(8,15)',dx=8);lab(300,815,'Resultant length 17',22)
 for j,z in enumerate(s['displays'][scene].split('\n')):lab(825,505+j*72,z,27 if len(z)<54 else 22,TEAL if j==0 else INK)
def lessons(doc):
 out=make_lessons(SPECS,doc)
 for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:draw(s,d,scene,p)
 return out
