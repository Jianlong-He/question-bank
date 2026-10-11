import json,math
from pathlib import Path
from card_lessons import make_lessons,draw_card
import generate_sample_videos as v
from generate_sample_videos import text,TEAL,INK,font
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g9-u18/lesson-specs.json').read_text())
def draw(s,d,scene,p):
 vid=s['video_id'];custom=['geometry-coordinate-midpoint-inverse','geometry-coordinate-segment-ratio','geometry-coordinate-centroid-median','geometry-circle-equation-center-radius','geometry-circle-point-position']
 if vid not in custom or scene in [0,4]:return draw_card(s,d,scene,p)
 d.rounded_rectangle((145,350,1775,850),radius=35,fill='white')
 def pt(x,y):return (490+(x-cx)*scale,610-(y-cy)*scale)
 def line(a,b,color=TEAL,width=4):d.line([pt(*a),pt(*b)],fill=color,width=width)
 def dot(xy,label,dx=8,dy=-30):
  a,b=pt(*xy);d.ellipse((a-5,b-5,a+5,b+5),fill=INK);text(d,(a+dx,b+dy),label,24,INK)
 if vid=='geometry-coordinate-midpoint-inverse':
  cx,cy,scale=2,2,25;A=(-6,5);B=(10,-1);M=(2,2)
  line(A,B);dot(A,'A(−6, 5)',-15,-42);dot(B,'B(10, −1)',-40,15);dot(M,'M(2, 2)',0,-40)
 elif vid=='geometry-coordinate-segment-ratio':
  cx,cy,scale=8,8.5,21;A=(-2,1);B=(18,16);P=(10,10)
  line(A,B);dot(A,'A(−2, 1)',-15,15);dot(B,'B(18, 16)',-70,-38);dot(P,'P(10, 10)',10,0)
  for j in [1,2,4]:dot((-2+4*j,1+3*j),'',0,0)
  text(d,(235,420),'AP:PB = 3:2',28,TEAL)
 elif vid=='geometry-coordinate-centroid-median':
  cx,cy,scale=1,4.5,32;A=(1,9);B=(-5,0);C=(7,0);G=(1,3);M=(1,0)
  for u,w in [(A,B),(B,C),(C,A)]:line(u,w)
  line(A,M,'#b76d36',3)
  for u,t,dx,dy in [(A,'A(1, 9)',10,-35),(B,'B(−5, 0)',-35,20),(C,'C(7, 0)',-40,20),(G,'G(1, 3)',14,-10),(M,'M',-12,20)]:dot(u,t,dx,dy)
 else:
  if vid=='geometry-circle-equation-center-radius':cx,cy,scale=-4,6,19;center=(-4,6);r=9;points=[((-4,6),'C(−4, 6)',-50,20),((5,6),'(5, 6)',-20,-40)]
  else:cx,cy,scale=0,0,13;center=(0,0);r=13;points=[((3,4),'P',-28,5),((5,12),'Q',-25,-40),((8,12),'R',14,-10)]
  a,b=pt(*center);rr=r*scale;d.ellipse((a-rr,b-rr,a+rr,b+rr),outline=TEAL,width=4)
  if vid.endswith('radius'):line(center,(5,6),'#b76d36');text(d,(a+70,b+18),'r = 9',24,TEAL)
  else:
   line((-15,0),(15,0),'#aab5b7',2);line((0,-15),(0,15),'#aab5b7',2);dot((0,0),'O',-25,10)
  for u,t,dx,dy in points:dot(u,t,dx,dy)
 for j,line_text in enumerate(s['displays'][scene].split('\n')):
  size=39
  while d.textlength(line_text,font=font(size))>850:size-=1
  text(d,(865,520+j*82),line_text,size,TEAL)
def lessons(doc):
 out=make_lessons(SPECS,doc)
 for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:draw(s,d,scene,p)
 return out
