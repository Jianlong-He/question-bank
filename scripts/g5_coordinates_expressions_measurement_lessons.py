import json
from pathlib import Path
from card_lessons import make_lessons,draw_card
import generate_sample_videos as v
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g5-u12-u14/lesson-specs.json').read_text())
def graph(d,xmax=10,ymax=10,xstep=1,ystep=1,xlabel='x',ylabel='y'):
 left,bottom,w,h=250,820,530,420
 def xy(x,y):return (left+x/xmax*w,bottom-y/ymax*h)
 for i in range(round(xmax/xstep)+1):
  x=i*xstep;px,_=xy(x,0);d.line((px,bottom,px,bottom-h),fill='#d9e4e1',width=2)
  if i% (1 if xmax<=10 else 2)==0:v.text(d,(px,bottom+10),str(int(x)) if x.is_integer() else str(x),24,v.INK,False,'mt')
 for i in range(round(ymax/ystep)+1):
  y=i*ystep;_,py=xy(0,y);d.line((left,py,left+w,py),fill='#d9e4e1',width=2)
  if ymax<=10 or i%5==0:v.text(d,(left-15,py),str(int(y)),24,v.INK,False,'rm')
 v.arrow(d,(left,bottom),(left+w+25,bottom),v.INK,4);v.arrow(d,(left,bottom),(left,bottom-h-25),v.INK,4)
 v.text(d,(left+w/2,bottom+48),xlabel,28,v.INK,True,'mt');v.text(d,(left,bottom-h-40),ylabel,27,v.INK,True,'lb')
 return xy

def dot(d,xy,x,y,label,color=v.TEAL):
 px,py=xy(x,y);d.ellipse((px-9,py-9,px+9,py+9),fill=color);v.text(d,(px+15,py-18),label,30,color,True)
def right(d,s):
 lines=[]
 for part in s.split('\n'):lines+=v.wrap(d,part,44,760)
 y=585-len(lines)*31
 for line in lines:v.text(d,(940,y),line,44,v.TEAL,True);y+=62

def draw(s,d,scene,p):
 vid=s['video_id']
 if vid not in ['coordinate-grid-basics','coordinate-grid-movement','coordinate-context-plot','coordinate-table-line-types'] or (vid=='coordinate-table-line-types' and scene in [0,4]):return draw_card(s,d,scene,p)
 d.rounded_rectangle((145,345,1775,930),radius=35,fill='white')
 if vid=='coordinate-context-plot':
  xy=graph(d,4,50,.5,2,'Time (hours)','Volume (litres)')
  for x,y,l,c in [(1.5,24,'P','#8b42a3'),(3,36,'Q','#cb7816'),(0,12,'R',v.TEAL)]:dot(d,xy,x,y,l,c)
  if scene==2:
   d.line((xy(1.5,0),xy(1.5,24),xy(0,24)),fill='#8b42a3',width=3)
 elif vid=='coordinate-grid-basics':
  xy=graph(d,xstep=1.0,ystep=1.0)
  if scene>=2:v.arrow(d,xy(0,0),xy(6,0),'#cb7816',6)
  if scene>=3:v.arrow(d,xy(6,0),xy(6,3),v.TEAL,6);dot(d,xy,6,3,'P')
  if scene==4:dot(d,xy,3,6,'Q','#8b42a3')
 elif vid=='coordinate-grid-movement':
  xy=graph(d,xstep=1.0,ystep=1.0);dot(d,xy,3,2,'A');dot(d,xy,8,6,'B','#8b42a3')
  if scene>=2:v.arrow(d,xy(3,2),xy(8,2),'#cb7816',6)
  if scene>=3:v.arrow(d,xy(8,2),xy(8,6),'#cb7816',6)
 else:
  xy=graph(d,xstep=1.0,ystep=1.0)
  pts=[(4,2),(4,5),(4,9)] if scene==1 else [(2,3),(4,3),(7,3)] if scene==2 else [(1,2),(2,4),(3,8)]
  if scene==1:d.line((xy(4,0),xy(4,10)),fill=v.TEAL,width=4)
  elif scene==2:d.line((xy(0,3),xy(10,3)),fill=v.TEAL,width=4)
  else:d.line([xy(*pt) for pt in pts],fill='#cb7816',width=4)
  for x,y in pts:dot(d,xy,x,y,'')
 right(d,s['displays'][scene])
 if scene==4:v.centered(d,955,'Check the method, then try your worksheet.',30,v.MUTED)
def lessons(doc):
 ls=make_lessons(SPECS,doc)
 for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:draw(s,d,scene,p)
 return ls
