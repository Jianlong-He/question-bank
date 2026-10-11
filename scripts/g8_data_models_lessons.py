import json
from pathlib import Path
from card_lessons import make_lessons,draw_card
import generate_sample_videos as v
from generate_sample_videos import text,TEAL,INK,MUTED,font
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g8-u7/lesson-specs.json').read_text())
FIT=[(1,4),(2,3),(3,9),(4,7),(5,12),(6,13)]
assert sum(y-(2*x+1) for x,y in FIT)==0 and sum(x*(y-(2*x+1)) for x,y in FIT)==0

def diagram(s,d,scene,p):
 vid=s['video_id']
 if vid=='statistics-two-way-counts' and scene in [1,2]:
  d.rounded_rectangle((145,340,1775,865),radius=35,fill='white')
  table=[['Travel mode','Lunch: Yes','Lunch: No','Total'],['Cycle','17','23','40'],['Walk','11','29','40'],['Total','28','52','80']]
  x0,y0,cw,ch=305,400,325,83
  for i,row in enumerate(table):
   for j,t in enumerate(row):
    box=(x0+j*cw,y0+i*ch,x0+(j+1)*cw,y0+(i+1)*ch);d.rectangle(box,fill='#d8efea' if (i==1 and j==1 and scene==2) else '#edf3f1' if i==0 or j==0 else 'white',outline='#becbc6',width=2);text(d,(box[0]+cw/2,box[1]+ch/2),t,32,TEAL if i==0 or j==0 else INK,anchor='mm')
  text(d,(960,800),s['displays'][scene],35,TEAL,anchor='mm')
 elif vid=='statistics-best-fit-meaning' and scene in [1,2,3]:
  d.rounded_rectangle((145,340,1775,875),radius=35,fill='white')
  x0,y0,sx,sy=285,780,78,24
  pt=lambda x,y:(x0+sx*x,y0-sy*y)
  for x in range(8):
   d.line([pt(x,0),pt(x,16)],fill='#e0e8e4',width=1);text(d,(pt(x,0)[0],798),str(x),23,MUTED,anchor='mt')
  for y in range(0,17,4):
   d.line([pt(0,y),pt(7,y)],fill='#e0e8e4',width=1);text(d,(260,pt(0,y)[1]),str(y),23,MUTED,anchor='rm')
  d.line([pt(0,0),pt(7,0)],fill=INK,width=2);d.line([pt(0,0),pt(0,16)],fill=INK,width=2);d.line([pt(0,1),pt(7,15)],fill='#bc7e33',width=4)
  for x,y in FIT:
   a,b=pt(x,y);d.ellipse((a-7,b-7,a+7,b+7),fill=TEAL)
  d.line([pt(3,7),pt(3,9)],fill='#bb4455',width=6);text(d,(pt(3,9)[0]-70,pt(3,9)[1]-35),'(3, 9)',27,TEAL);text(d,(pt(3,7)[0]+12,pt(3,7)[1]+5),'(3, 7)',27,'#bc7e33');text(d,(350,365),'Fitted line: y = 2x + 1',28,INK)
  for j,line in enumerate(s['displays'][scene].split('\n')):
   size=39
   while d.textlength(line,font=font(size))>820:size-=1
   text(d,(875,520+j*90),line,size,TEAL)
  text(d,(875,720),'Vertical gap at x = 3: +2',31,'#bb4455')
 else:return draw_card(s,d,scene,p)
def lessons(doc):
 out=make_lessons(SPECS,doc)
 for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:diagram(s,d,scene,p)
 return out
