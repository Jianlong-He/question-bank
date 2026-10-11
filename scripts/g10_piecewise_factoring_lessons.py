import json,math
from pathlib import Path
from card_lessons import make_lessons,draw_card
import generate_sample_videos as v
from generate_sample_videos import text,TEAL,INK,font
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g10-u1-u2/lesson-specs.json').read_text())
BROWN='#b76d36';GRAY='#aab5b7'
def draw(s,d,scene,p):
 vid=s['video_id'];custom=['absolute-value-vertex-symmetry-extrema','absolute-value-write-transformations','absolute-value-reflection-width','piecewise-select-rule-evaluate','piecewise-domain-range-constants','piecewise-open-closed-endpoints']
 if vid not in custom or scene in [0,4]:return draw_card(s,d,scene,p)
 d.rounded_rectangle((145,350,1775,850),radius=35,fill='white')
 bounds=(-3,7,-6,10)
 if vid=='absolute-value-write-transformations':bounds=(-10,4,-11,3)
 if vid=='absolute-value-reflection-width':bounds=(-3,3,-9,5)
 xmin,xmax,ymin,ymax=bounds
 def pt(x,y):return (250+(x-xmin)/(xmax-xmin)*510,790-(y-ymin)/(ymax-ymin)*370)
 def line(a,b,color=TEAL,width=4):d.line([pt(*a),pt(*b)],fill=color,width=width)
 def dot(a,label='',open=False,dx=12,dy=-23):
  u,w=pt(*a);d.ellipse((u-7,w-7,u+7,w+7),outline=INK,fill='white' if open else INK,width=3)
  if label:text(d,(u+dx,w+dy),label,23,INK)
 for k in range(math.ceil(xmin),math.floor(xmax)+1):
  if k%2==0:line((k,ymin),(k,ymax),'#edf0ee',1)
 for k in range(math.ceil(ymin),math.floor(ymax)+1):
  if k%2==0:line((xmin,k),(xmax,k),'#edf0ee',1)
 line((xmin,0),(xmax,0),GRAY,2);line((0,ymin),(0,ymax),GRAY,2)
 text(d,(pt(xmax,0)[0]+12,pt(xmax,0)[1]-10),'x',22,INK);text(d,(pt(0,ymax)[0]-8,pt(0,ymax)[1]-25),'y',22,INK)
 for k in range(math.ceil(xmin),math.floor(xmax)+1):
  if k%2==0 and k!=0:text(d,(pt(k,0)[0]-8,pt(k,0)[1]+8),str(k),16,INK)
 for k in range(math.ceil(ymin),math.floor(ymax)+1):
  if k%2==0 and k!=0:text(d,(pt(0,k)[0]-27,pt(0,k)[1]-10),str(k),16,INK)
 def plot(fun,lo=xmin,hi=xmax,color=TEAL):
  points=[]
  for j in range(401):
   x=lo+(hi-lo)*j/400;y=fun(x)
   if ymin<=y<=ymax:points.append(pt(x,y))
   elif len(points)>1:d.line(points,fill=color,width=4);points=[]
  if len(points)>1:d.line(points,fill=color,width=4)
 if vid=='absolute-value-vertex-symmetry-extrema':
  plot(lambda x:-3*abs(x-2)+8);line((2,ymin),(2,ymax),BROWN,2);dot((2,8),'(2, 8)',15,-25)
  if scene>=2:dot((1,5));dot((3,5))
 elif vid=='absolute-value-write-transformations':
  h=0 if scene==1 else -5;k=-3 if scene==3 else 0
  plot(lambda x:-abs(x-h)+k);dot((h,k),f'({h}, {k})',15,-30)
 elif vid=='absolute-value-reflection-width':
  plot(lambda x:abs(x),color=GRAY);plot(lambda x:-4*abs(x),color=TEAL);plot(lambda x:.5*abs(x),color=BROWN)
  text(d,(230,810),'Parent: gray   −4|x|: teal   0.5|x|: brown',21,INK)
 elif vid=='piecewise-select-rule-evaluate':
  plot(lambda x:x+4,hi=3);plot(lambda x:2*x-5,lo=3,color=BROWN);dot((3,7),'(3, 7)',open=True);dot((3,1),'(3, 1)',dy=12);dot((-2,2),'(−2, 2)',dx=-40,dy=-33)
 elif vid=='piecewise-domain-range-constants':
  plot(lambda x:-4,hi=2);plot(lambda x:7,lo=2,color=BROWN);dot((2,-4),'(2, −4)',open=True);dot((2,7),'(2, 7)')
 elif vid=='piecewise-open-closed-endpoints':
  plot(lambda x:x+1,hi=4);plot(lambda x:2,lo=4,color=BROWN);dot((4,5),'(4, 5)',open=True);dot((4,2),'(4, 2)',dy=16)
 for j,t in enumerate(s['displays'][scene].split('\n')):
  size=39
  while d.textlength(t,font=font(size))>850:size-=1
  text(d,(865,495+j*82),t,size,TEAL)
def lessons(doc):
 out=make_lessons(SPECS,doc)
 for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:draw(s,d,scene,p)
 return out
