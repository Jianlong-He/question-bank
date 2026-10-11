import json,math
from pathlib import Path
from card_lessons import make_lessons,draw_card
import generate_sample_videos as v
from generate_sample_videos import text,TEAL,INK,MUTED,font
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g9-u16-u17/lesson-specs.json').read_text())
BROWN='#b76d36'
def draw(s,d,scene,p):
 vid=s['video_id'];custom=['geometry-parallelogram-side-diagonal-properties','geometry-rhombus-perpendicular-diagonals','geometry-rhombus-diagonal-area','geometry-circle-equal-radii','geometry-construction-classical-tools','geometry-construct-perpendicular-bisector','geometry-construct-perpendicular-off-line','geometry-angle-bisector-equal-distances','geometry-proof-reflexive-side']
 if vid not in custom or scene in [0,4]:return draw_card(s,d,scene,p)
 d.rounded_rectangle((145,350,1775,850),radius=35,fill='white')
 def line(a,b,c=TEAL,w=4):d.line([a,b],fill=c,width=w)
 def dot(pt,label,dx=8,dy=-25):
  x,y=pt;d.ellipse((x-5,y-5,x+5,y+5),fill=INK);text(d,(x+dx,y+dy),label,25,INK)
 def circle(c,r,color=BROWN):d.ellipse((c[0]-r,c[1]-r,c[0]+r,c[1]+r),outline=color,width=3)
 if vid=='geometry-parallelogram-side-diagonal-properties':
  pts=[(260,720),(580,720),(740,440),(420,440)];P,Q,R,T=pts
  d.polygon(pts,outline=TEAL,width=5)
  for pt,lab in zip(pts,'PQRS'):dot(pt,lab)
  if scene>=2:line(P,R,BROWN);line(Q,T,BROWN);dot((500,580),'M')
  text(d,(405,742),'14 cm',27,TEAL);text(d,(532,400),'RS = 14 cm',27,TEAL)
  if scene>=2:text(d,(265,795),'PR = 26 cm',25,INK)
 elif vid in ['geometry-rhombus-perpendicular-diagonals','geometry-rhombus-diagonal-area']:
  # Horizontal diagonal 12 units, vertical diagonal 18 units, equal scale 24 px/unit.
  P,Q,R,T=(500,384),(644,600),(500,816),(356,600);O=(500,600)
  d.polygon([P,Q,R,T],outline=TEAL,width=5);line(P,R,BROWN);line(Q,T,BROWN)
  for pt,lab in zip([P,Q,R,T,O],['P','Q','R','S','O']):dot(pt,lab)
  if vid.endswith('area'):
   text(d,(668,645),'12 cm',24,INK);text(d,(250,590),'18 cm',24,INK)
   text(d,(518,680),'9',25,TEAL);text(d,(560,620),'6',25,TEAL)
  elif scene>=2:
   d.polygon([P,O,Q],fill='#d5ebe4');d.polygon([R,O,Q],fill='#f4e1ce');d.polygon([P,Q,R,T],outline=TEAL,width=5);line(P,R,BROWN);line(Q,T,BROWN)
   for pt,lab in zip([P,Q,R,T,O],['P','Q','R','S','O']):dot(pt,lab)
  if vid.endswith('area') or scene>=3:d.line([(500,582),(518,582),(518,600)],fill=INK,width=3)
 elif vid=='geometry-proof-reflexive-side':
  J,L,K,M=(310,640),(690,640),(455,410),(580,790)
  d.polygon([J,K,L],outline=TEAL,width=4);d.polygon([J,M,L],outline=TEAL,width=4);line(J,L,BROWN,7)
  for pt,lab in [(J,'J'),(L,'L'),(K,'K'),(M,'M')]:dot(pt,lab)
  text(d,(405,665),'Shared segment JL',26,BROWN)
 elif vid in ['geometry-circle-equal-radii','geometry-construction-classical-tools']:
  O=(485,600);r=170;A=(655,600);B=(400,600-170*math.sqrt(3)/2)
  circle(O,r,TEAL);dot(O,'O');dot(A,'A');line(O,A,BROWN)
  if vid=='geometry-circle-equal-radii':
   dot(B,'B',-23,-28);line(O,B,BROWN);text(d,(530,620),'3x + 1',25,INK);text(d,(375,510),'16',25,INK)
  elif scene>=3:line((250,600),(760,600),BROWN)
  else:text(d,(470,625),'radius OA',26,INK)
 elif vid=='geometry-construct-perpendicular-bisector':
  A=(360,600);B=(640,600);P=(500,600);rad=196;h=math.sqrt(24)*28;C=(500,600-h);D=(500,600+h)
  line((220,600),(780,600),INK);dot(A,'A');dot(B,'B');dot(P,'P',8,12);circle(A,rad);circle(B,rad)
  text(d,(450,810),'AB = 10 cm',25,INK)
  if scene>=2:dot(C,'C');dot(D,'D')
  if scene>=3:line((500,385),(500,790),TEAL);d.line([(500,582),(518,582),(518,600)],fill=INK,width=3)
 elif vid=='geometry-construct-perpendicular-off-line':
  P=(500,520);Q=(500,740);rad=160;dx=math.sqrt(rad*rad-110*110);A=(500-dx,630);B=(500+dx,630)
  line((220,630),(780,630),INK);text(d,(760,647),'L',25,INK);circle(P,rad);dot(P,'P');dot(A,'A',-20,12);dot(B,'B',8,12)
  if scene>=2:line(P,A,TEAL);line(P,B,TEAL)
  if scene>=3:
   # Equal-radius arc portions centered at A/B pass through Q, their lower intersection.
   for pt in [A,B]:
    cx,cy=pt;d.arc((cx-rad,cy-rad,cx+rad,cy+rad),start=15,end=165,fill=TEAL,width=3)
   dot(Q,'Q');line(P,Q,TEAL)
 elif vid=='geometry-angle-bisector-equal-distances':
  O=(280,610);P=(580,610);theta=math.radians(40);feet=[]
  for sign,lab in [(-1,'A'),(1,'B')]:
   end=(O[0]+330*math.cos(theta),O[1]+sign*330*math.sin(theta));line(O,end,INK);dot(end,lab)
   t=300*math.cos(theta);foot=(O[0]+t*math.cos(theta),O[1]+sign*t*math.sin(theta));feet.append(foot)
  line(O,P,TEAL);dot(O,'O',-25,10);dot(P,'P');d.arc((O[0]-65,O[1]-65,O[0]+65,O[1]+65),start=320,end=360,fill=BROWN,width=3);d.arc((O[0]-65,O[1]-65,O[0]+65,O[1]+65),start=0,end=40,fill=BROWN,width=3)
  text(d,(350,574),'40°',23,BROWN);text(d,(350,638),'40°',23,BROWN)
  if scene>=2:
   for F,lab in zip(feet,['X','Y']):
    line(P,F,BROWN);dot(F,lab,-26,0)
    # Right-angle marker using unit vectors toward O and toward P.
    norm1=math.dist(F,O);norm2=math.dist(F,P);u=((O[0]-F[0])/norm1*16,(O[1]-F[1])/norm1*16);w=((P[0]-F[0])/norm2*16,(P[1]-F[1])/norm2*16)
    d.line([(F[0]+u[0],F[1]+u[1]),(F[0]+u[0]+w[0],F[1]+u[1]+w[1]),(F[0]+w[0],F[1]+w[1])],fill=INK,width=3)
   text(d,(530,520),'6 cm',26,BROWN);text(d,(530,710),'6 cm',26,BROWN)
 for j,line_text in enumerate(s['displays'][scene].split('\n')):
  size=39
  while d.textlength(line_text,font=font(size))>850:size-=1
  text(d,(865,520+j*82),line_text,size,TEAL)
def lessons(doc):
 out=make_lessons(SPECS,doc)
 for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:draw(s,d,scene,p)
 return out
