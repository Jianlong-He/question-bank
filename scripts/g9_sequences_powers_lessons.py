import json
from pathlib import Path
from card_lessons import make_lessons,draw_card
import generate_sample_videos as v
from generate_sample_videos import text,TEAL,INK,MUTED,font
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g9-u12-u13/lesson-specs.json').read_text())
def draw(s,d,scene,p):
 if s['video_id']!='sequence-discrete-domain' or scene in [0,1]:return draw_card(s,d,scene,p)
 d.rounded_rectangle((145,350,1775,850),radius=35,fill='white')
 pt=lambda x,y:(270+x*100,785-y*27)
 for x in range(1,5):
  d.line([pt(x,0),pt(x,15)],fill='#e2e8e5',width=1);text(d,(pt(x,0)[0],809),str(x),24,MUTED,anchor='mt')
 for y in [0,5,10,15]:
  d.line([pt(0,y),pt(4.5,y)],fill='#e2e8e5',width=1);text(d,(245,pt(0,y)[1]),str(y),23,MUTED,anchor='rm')
 d.line([pt(0,0),pt(4.5,0)],fill=INK,width=3);d.line([pt(0,0),pt(0,15)],fill=INK,width=3)
 for x,y in [(1,7),(2,9),(3,11),(4,13)]:
  a,b=pt(x,y);d.ellipse((a-8,b-8,a+8,b+8),fill=TEAL);text(d,(a+12,b-25),f'({x}, {y})',23,INK)
 text(d,(740,785),'n',26,INK);text(d,(270,360),'a(n)',26,INK)
 for j,line in enumerate(s['displays'][scene].split('\n')):
  size=40
  while d.textlength(line,font=font(size))>850:size-=1
  text(d,(855,530+j*80),line,size,TEAL)
def lessons(doc):
 out=make_lessons(SPECS,doc)
 for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:draw(s,d,scene,p)
 return out
