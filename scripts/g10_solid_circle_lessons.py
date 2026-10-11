import json,math
from pathlib import Path
from card_lessons import make_lessons,draw_card
import generate_sample_videos as v
from generate_sample_videos import text,TEAL,INK,font
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g10-u10-u11/lesson-specs.json').read_text())
BROWN='#b76d36';GRAY='#aab5b7'
def draw(s,d,scene,p):
 vid=s['video_id']
 if scene in [0,4] or vid in ['measurement-area-population-density','angle-degrees-radians-conversion']:return draw_card(s,d,scene,p)
 d.rounded_rectangle((145,350,1775,850),radius=35,fill='white')
 def line(pts,col=TEAL,w=4):d.line(pts,fill=col,width=w)
 def label(pt,val,dx=0,dy=0,size=26):text(d,(pt[0]+dx,pt[1]+dy),val,size,INK)
 def dot(pt,name,dx=10,dy=-25):d.ellipse((pt[0]-5,pt[1]-5,pt[0]+5,pt[1]+5),fill=INK);label(pt,name,dx,dy)
 def circle(cx=500,cy=615,R=175):d.ellipse((cx-R,cy-R,cx+R,cy+R),outline=TEAL,width=4)
 def point(a,cx=500,cy=615,R=175):return(cx+R*math.cos(math.radians(a)),cy-R*math.sin(math.radians(a)))
 def arc(a,b,cx=500,cy=615,R=175,col=BROWN):line([point(a+(b-a)*j/120,cx,cy,R) for j in range(121)],col,6)
 if vid=='geometry-solid-parallel-cross-sections':
  if scene==1:
   front=[(320,720),(560,720),(560,480),(320,480)];back=[(x+110,y-50) for x,y in front];line(front+[front[0]]);line(back+[back[0]])
   for a,b in zip(front,back):line([a,b],GRAY,2)
   P=[(320,620),(560,620),(670,570),(430,570)];d.polygon(P,fill='#f2e1c7');line(P+[P[0]],BROWN);label((430,735),'8');label((335,810),'Square shown in perspective')
  elif scene==2:
   d.ellipse((345,425,655,515),outline=TEAL,width=3);d.ellipse((345,715,655,805),outline=TEAL,width=3);line([(345,470),(345,760)]);line([(655,470),(655,760)])
   d.ellipse((345,570,655,660),fill='#f2e1c7',outline=BROWN,width=4);line([(500,615),(655,615)],INK,3);label((550,580),'r = 7');label((335,820),'Circular slice shown in perspective',size=23)
  else:
   cx,cy,R=480,610,175;circle(cx,cy,R);depth=R*5/13;half=R*12/13;O=(cx,cy);M=(cx,cy+depth);A=(cx+half,cy+depth)
   line([(cx-half,cy+depth),A],BROWN);line([O,M,A,O],GRAY,3);dot(O,'O',-25,-30);label(((O[0]+A[0])/2,(O[1]+A[1])/2),'13',5,-25);label((cx,cy+depth/2),'5',-30,0);label((cx+half/2,cy+depth),'12',-10,15);label((315,810),'Sphere meridian; slice radius = 12',size=24)
 elif vid=='geometry-inscribed-angles-shared-arc':
  circle();A=point(-62);B=point(62);C=point(170);D=point(230)
  for V,col in [(C,TEAL),(D,GRAY)]:line([A,V,B],col,3)
  arc(-62,62)
  for P,n,dx,dy in [(A,'A',10,10),(B,'B',10,-30),(C,'C',-30,-25),(D,'D',-25,10)]:dot(P,n,dx,dy)
  label((698,600),'124°');label(C,'62°',30,-5);label(D,'62°',10,-45)
 elif vid=='geometry-perpendicular-radius-chord-bisector':
  circle(480,610,180);O=(480,610);M=(480,718);A=(336,718);B=(624,718);line([A,O,B,A]);line([O,M],BROWN);line([(480,703),(495,703),(495,718)],GRAY,2)
  for P,n,dx,dy in [(O,'O',-20,-30),(M,'M',-10,38),(A,'A',-25,10),(B,'B',10,10)]:dot(P,n,dx,dy)
  label((390,640),'10');label((552,640),'10');label((485,660),'6');label((400,733),'8');label((545,733),'8')
 elif vid=='geometry-two-tangents-exterior-angle':
  cx,cy,R=455,610,145;circle(cx,cy,R);A=point(63,cx,cy,R);B=point(-63,cx,cy,R);O=(cx,cy);P=(cx+R/math.cos(math.radians(63)),cy)
  line([A,P,B],BROWN);line([A,O,B],GRAY,3);arc(-63,63,cx,cy,R)
  for pt,n,dx,dy in [(A,'A',0,-30),(B,'B',0,12),(O,'O',-25,-15),(P,'P',10,-15)]:dot(pt,n,dx,dy)
  label((485,596),'126°');label((695,596),'54°');label((275,815),'OA and OB are perpendicular to tangents',size=23)
 elif vid=='geometry-circumcircle-perpendicular-bisectors':
  def xy(x,y):return(320+x*40,760-y*40)
  circle(*xy(4,3),200);A=xy(0,0);B=xy(8,0);C=xy(0,6);O=xy(4,3);line([A,B,C,A]);line([xy(4,-1),xy(4,8)],BROWN,2);line([xy(-1,3),xy(9,3)],GRAY,2)
  for P,n,dx,dy in [(A,'A (0, 0)',-55,12),(B,'B (8, 0)',-20,12),(C,'C (0, 6)',-70,-30),(O,'O (4, 3)',10,-25)]:dot(P,n,dx,dy)
  line([O,A],GRAY,2);label((385,700),'r = 5');label((508,430),'x = 4');label((710,640),'y = 3')
 elif vid=='geometry-compass-hexagon-construction':
  circle();P=[point(j*60) for j in range(6)];line(P+[P[0]],BROWN)
  for j,pt in enumerate(P):line([(500,615),pt],GRAY,2);dot(pt,str(j+1),12 if j in [0,1,5] else -25,-25 if j in [1,2] else 10)
  label((555,595),'9');label((425,575),'60°');label((310,820),'Keep compass opening equal to the radius.',size=23)
 elif vid=='geometry-all-circles-similar':
  circle(505,610,150);d.ellipse((442.5,547.5,567.5,672.5),outline=BROWN,width=4);dot((505,610),'(4, 3)',-20,20);line([(505,610),(655,610)],TEAL,3);line([(505,610),(505,547.5)],BROWN,3);label((580,620),'12');label((512,560),'5');label((290,420),'After translating to the common center',size=24);label((350,810),'Dilation factor = 12/5')
 elif vid=='geometry-adjacent-arcs-semicircle-equation':
  circle();A=point(180);B=point(0);M=point(61);line([A,B],GRAY,2);line([(500,615),M],GRAY,2);arc(0,61);arc(61,180,col=TEAL)
  for P,n in [(A,'A'),(B,'B'),(M,'M')]:dot(P,n,10,-30)
  label((360,440),'119° = 2x + 13');label((640,470),'61° = x + 8');label((335,810),'Adjacent upper arcs total 180°')
 for j,t in enumerate(s['displays'][scene].split('\n')):
  size=38
  while d.textlength(t,font=font(size))>850:size-=1
  text(d,(865,465+j*80),t,size,TEAL)
def lessons(doc):
 out=make_lessons(SPECS,doc)
 for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:draw(s,d,scene,p)
 return out
