import json,math
from pathlib import Path
from card_lessons import make_lessons,draw_card
import generate_sample_videos as v
from generate_sample_videos import text,TEAL,INK,font
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g10-u3/lesson-specs.json').read_text())
BROWN='#b76d36';GRAY='#aab5b7'
GRAPHS={
'quadratic-opening-width':(-3,3,-10,6,lambda x:-3*x*x),
'quadratic-vertex-form-features':(-7,1,-5,10,lambda x:-2*(x+3)**2+7),
'quadratic-write-transformations':(-3,8,-15,10,lambda x:-2*(x-4)**2+6),
'quadratic-factored-axis-vertex':(-6,8,-15,60,lambda x:-2*(x+4)*(x-6)),
'quadratic-fixed-perimeter-area':(0,28,0,220,lambda x:x*(28-x)),
'quadratic-projectile-vertex':(0,11,0,160,lambda x:-5*x*x+50*x+15),
'quadratic-standard-form-vertex':(-7,1,-10,15,lambda x:2*x*x+12*x+11),
'quadratic-three-forms-features':(-7,9,-45,25,lambda x:x*x-2*x-35),
'quadratic-discriminant-root-count':(-3,5,-6,12,lambda x:x*x-2*x-3),
}
def draw(s,d,scene,p):
 vid=s['video_id']
 if scene in [0,4] or (vid not in GRAPHS and vid not in ['geometry-square-base-symbolic-volume','quadratic-area-positive-root']):return draw_card(s,d,scene,p)
 d.rounded_rectangle((145,350,1775,850),radius=35,fill='white')
 if vid in GRAPHS:
  xmin,xmax,ymin,ymax,fun=GRAPHS[vid]
  def pt(x,y):return (250+(x-xmin)/(xmax-xmin)*510,790-(y-ymin)/(ymax-ymin)*370)
  def line(a,b,color=GRAY,width=2):d.line([pt(*a),pt(*b)],fill=color,width=width)
  def dot(x,y,label,dx=10,dy=-28):
   u,w=pt(x,y);d.ellipse((u-6,w-6,u+6,w+6),fill=INK);text(d,(u+dx,w+dy),label,22,INK)
  for i in range(6):
   xx=xmin+(xmax-xmin)*i/5;yy=ymin+(ymax-ymin)*i/5
   line((xx,ymin),(xx,ymax),'#edf0ee',1);line((xmin,yy),(xmax,yy),'#edf0ee',1)
  line((xmin,0),(xmax,0));line((0,ymin),(0,ymax))
  text(d,(pt(xmax,0)[0]+10,pt(xmax,0)[1]-12),'t' if vid=='quadratic-projectile-vertex' else 'x',22,INK)
  text(d,(pt(0,ymax)[0]-10,pt(0,ymax)[1]-28),'h' if vid=='quadratic-projectile-vertex' else ('A' if vid=='quadratic-fixed-perimeter-area' else 'y'),22,INK)
  def plot(f,color=TEAL):
   points=[]
   for j in range(501):
    xx=xmin+(xmax-xmin)*j/500;yy=f(xx)
    if ymin<=yy<=ymax:points.append(pt(xx,yy))
    else:
     if len(points)>1:d.line(points,fill=color,width=4)
     points=[]
   if len(points)>1:d.line(points,fill=color,width=4)
  if vid=='quadratic-opening-width':
   plot(lambda x:x*x,GRAY);plot(fun);plot(lambda x:.5*x*x,BROWN)
   text(d,(225,815),'Gray: x²   Teal: −3x²   Brown: 0.5x²',23,INK)
  elif vid=='quadratic-write-transformations':
   h=0 if scene==1 else 4;k=6 if scene==3 else 0
   plot(lambda x:-2*(x-h)**2+k);dot(h,k,f'({h}, {k})')
  elif vid=='quadratic-discriminant-root-count':
   c=[-3,1,5][scene-1];plot(lambda x:x*x-2*x+c)
   if scene==1:dot(-1,0,'−1',-30,10);dot(3,0,'3',10,10)
   elif scene==2:dot(1,0,'(1, 0)',10,10)
   else:dot(1,4,'(1, 4)')
  else:
   plot(fun)
   h,k={'quadratic-vertex-form-features':(-3,7),'quadratic-factored-axis-vertex':(1,50),'quadratic-fixed-perimeter-area':(14,196),'quadratic-projectile-vertex':(5,140),'quadratic-standard-form-vertex':(-3,-7),'quadratic-three-forms-features':(1,-36)}[vid]
   line((h,ymin),(h,ymax),BROWN,2);dot(h,k,f'({h}, {k})')
   if vid in ['quadratic-factored-axis-vertex','quadratic-three-forms-features']:
    for r in ([-4,6] if vid=='quadratic-factored-axis-vertex' else [-5,7]):dot(r,0,str(r),8,10)
 elif vid=='geometry-square-base-symbolic-volume':
  front=[(280,550),(570,550),(570,740),(280,740)];back=[(380,450),(670,450),(670,640),(380,640)]
  d.polygon(front,fill='#e1f0ed',outline=TEAL,width=4);d.polygon([front[0],back[0],back[1],front[1]],fill='#c5e1db',outline=TEAL,width=4);d.polygon([front[1],back[1],back[2],front[2]],fill='#a9cec5',outline=TEAL,width=4)
  text(d,(410,755),'x',36,INK);text(d,(622,692),'x',36,INK);text(d,(165,623),'x + 3',30,INK);text(d,(275,805),'Square base; diagram not to scale',23,INK)
 else:
  d.rectangle((270,460,730,730),fill='#e1f0ed',outline=TEAL,width=5);text(d,(465,750),'x + 6',35,INK);text(d,(210,580),'x',35,INK);text(d,(390,570),'Area = 72',36,TEAL)
 for j,t in enumerate(s['displays'][scene].split('\n')):
  size=39
  while d.textlength(t,font=font(size))>850:size-=1
  text(d,(865,495+j*82),t,size,TEAL)
def lessons(doc):
 out=make_lessons(SPECS,doc)
 for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:draw(s,d,scene,p)
 return out
