import json
from pathlib import Path
from card_lessons import make_lessons,draw_card
import generate_sample_videos as v
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g5-u1-u2/lesson-specs.json').read_text())
def draw_steps(d,scene,p):
 s=next(x for x in SPECS if x['video_id']=='decimal-number-line-small-steps')
 if scene not in (1,2):return draw_card(s,d,scene,p)
 d.rounded_rectangle((130,355,1790,845),radius=30,fill='white')
 left,right,y=300,1620,620;dx=(right-left)/5
 d.line((left,y,right,y),fill=v.INK,width=5)
 for i in range(6):
  x=left+i*dx;d.line((x,y-15,x,y+15),fill=v.INK,width=3)
  d.text((x,y+65),f'3.{510+i}',font=v.font(38,True),fill=v.TEAL if i==4 and scene==2 else v.INK,anchor='mm')
  if scene==2 and 0<i<=4:
   d.line((x-dx+12,y-95,x-12,y-95),fill=v.TEAL,width=4);d.polygon([(x-12,y-95),(x-30,y-104),(x-30,y-86)],fill=v.TEAL)
   d.text((x-dx/2,y-125),str(i),font=v.font(28,True),fill=v.TEAL,anchor='mm')
 if scene==2:d.ellipse((left+4*dx-10,y-10,left+4*dx+10,y+10),fill=v.TEAL)
 v.centered(d,410,'Each equal interval = 0.001',43,v.INK,True)
 v.centered(d,765,'Start at 3.510; count four intervals to reach 3.514' if scene==2 else 'Count intervals, not the starting tick',38,v.TEAL,True)
def lessons(doc):
 result=make_lessons(SPECS,doc);v.DRAW['decimal-number-line-small-steps']=draw_steps;return result
