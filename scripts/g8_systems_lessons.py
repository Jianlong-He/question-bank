import json
from pathlib import Path
from card_lessons import make_lessons,draw_card
import generate_sample_videos as video
from generate_sample_videos import text,TEAL,INK
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g8-u4/lesson-specs.json').read_text())
def graph_intersection(s,d,scene,p):
 if scene in [0,4]:return draw_card(s,d,scene,p)
 d.rounded_rectangle((145,360,1775,840),radius=35,fill='white')
 cx,cy,scale=555,595,40
 def pt(x,y):return (cx+x*scale,cy-y*scale)
 for k in range(-5,6):
  d.line([pt(k,-5),pt(k,5)],fill='#e5e9ed',width=2);d.line([pt(-5,k),pt(5,k)],fill='#e5e9ed',width=2)
  if k:
   text(d,(cx+k*scale-9,cy+8),str(k),20,INK)
   text(d,(cx+8,cy-k*scale-12),str(k),20,INK)
 d.line([pt(-5,0),pt(5,0)],fill=INK,width=3);d.line([pt(0,-5),pt(0,5)],fill=INK,width=3)
 text(d,(cx+211,cy-8),'x',26,INK);text(d,(cx+6,cy-235),'y',26,INK)
 d.line([pt(-5,-1),pt(1,5)],fill=TEAL,width=6)
 d.line([pt(-3,5),pt(5,-3)],fill='#bc6828',width=6)
 x,y=pt(-1,3)
 if scene>=2:
  for yy in range(int(y),int(cy),12):d.line((x,yy,x,min(yy+6,cy)),fill='#c03b39',width=3)
  for xx in range(int(x),int(cx),12):d.line((xx,y,min(xx+6,cx),y),fill='#c03b39',width=3)
 d.ellipse((x-9,y-9,x+9,y+9),fill='#c03b39')
 text(d,(850,410),'y = x + 4',36,TEAL);text(d,(1250,410),'y = −x + 2',36,'#bc6828')
 for j,line in enumerate(s['displays'][scene].split('\n')):text(d,(850,530+j*68),line,38,INK)
 text(d,(850,705),'Each grid step is 1 unit.',30,TEAL)
def lessons(doc):
 result=make_lessons(SPECS,doc)
 s=next(s for s in SPECS if s['video_id']=='systems-read-intersection')
 video.DRAW[s['video_id']]=lambda d,scene,p:graph_intersection(s,d,scene,p)
 return result
