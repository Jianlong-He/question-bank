import json,math
from pathlib import Path
from card_lessons import make_lessons,draw_card
import generate_sample_videos as v
from generate_sample_videos import text,TEAL,INK,font
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g10-u4-u6/lesson-specs.json').read_text())
BROWN='#b76d36';GRAY='#aab5b7'
def draw(s,d,scene,p):
 vid=s['video_id']
 if scene in [0,4] or vid not in ['complex-parts-plane','complex-unit-power-cycle','complex-conjugate-sum-product','irrational-integer-root-interval','real-number-rational-partition']:return draw_card(s,d,scene,p)
 d.rounded_rectangle((145,350,1775,850),radius=35,fill='white')
 if vid=='real-number-rational-partition':
  d.rounded_rectangle((210,415,800,790),radius=20,fill='#e1f0ed',outline=TEAL,width=3);text(d,(405,435),'REAL',35,INK)
  for left,title,vals in [(230,'Rational',['−12 = −12/1','7/9']),(520,'Irrational',['√23'])]:
   d.rounded_rectangle((left,500,left+260,750),radius=15,fill='white',outline=GRAY,width=2);text(d,(left+30,520),title,27,TEAL)
   for j,val in enumerate(vals):text(d,(left+30,590+j*65),val,30,INK)
 elif vid=='irrational-integer-root-interval':
  def xpos(x):return 240+(x-4)*510
  d.line([(240,640),(750,640)],fill=INK,width=4)
  for x,label in [(4,'4'),(5,'5')]:
   d.line([(xpos(x),628),(xpos(x),652)],fill=INK,width=4);text(d,(xpos(x)-7,665),label,30,INK)
  u=xpos(math.sqrt(18));d.ellipse((u-8,632,u+8,648),fill=TEAL);text(d,(u-20,590),'√18',34,TEAL)
  text(d,(280,470),'16 < 18 < 25',34,INK);text(d,(280,735),'4 < √18 < 5',34,TEAL)
 else:
  bounds=(-7,7,-7,8) if vid=='complex-parts-plane' else (-7,3,-6,6) if vid=='complex-conjugate-sum-product' else (-1.7,1.7,-1.7,1.7)
  xmin,xmax,ymin,ymax=bounds
  def pt(x,y):return (270+(x-xmin)/(xmax-xmin)*430,790-(y-ymin)/(ymax-ymin)*350)
  def line(a,b,color=GRAY,width=2):d.line([pt(*a),pt(*b)],fill=color,width=width)
  line((xmin,0),(xmax,0));line((0,ymin),(0,ymax));text(d,(pt(xmax,0)[0]+12,pt(xmax,0)[1]-10),'Real',23,INK);text(d,(pt(0,ymax)[0]-30,pt(0,ymax)[1]-30),'Imaginary',23,INK)
  def dot(x,y,label,dx=10,dy=-30,color=TEAL):
   u,w=pt(x,y);d.ellipse((u-8,w-8,u+8,w+8),fill=color);text(d,(u+dx,w+dy),label,28,color)
  if vid=='complex-parts-plane':
   line((-5,0),(-5,6),BROWN,2);line((0,6),(-5,6),BROWN,2);dot(-5,6,'(−5, 6)');text(d,(pt(-5,0)[0]-10,pt(-5,0)[1]+15),'−5',25,INK);text(d,(pt(0,6)[0]+12,pt(0,6)[1]-10),'6',25,INK)
  elif vid=='complex-conjugate-sum-product':
   dot(-5,-4,'−5 − 4i',10,15);dot(-5,4,'−5 + 4i',10,-35,color=BROWN);line((-5,-4),(-5,4),GRAY,2)
  else:
   u1,w1=pt(-1,1);u2,w2=pt(1,-1);d.ellipse((u1,w1,u2,w2),outline=GRAY,width=2)
   dot(1,0,'1',10,15);dot(0,1,'i',12,-22);dot(-1,0,'−1',-42,15);dot(0,-1,'−i',12,10)
   text(d,(265,815),'Multiply by i: quarter-turn counterclockwise',22,INK)
 for j,t in enumerate(s['displays'][scene].split('\n')):
  size=39
  while d.textlength(t,font=font(size))>850:size-=1
  text(d,(865,495+j*82),t,size,TEAL)
def lessons(doc):
 out=make_lessons(SPECS,doc)
 for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:draw(s,d,scene,p)
 return out
