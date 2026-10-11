import json
from pathlib import Path
import generate_sample_videos as v
from generate_sample_videos import text,TEAL,INK
from card_lessons import make_lessons,draw_card
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g12-u8-u9/lesson-specs.json').read_text())
def draw(s,d,scene,p):
 vid=s['video_id']
 if vid=='probability-distribution-event-sums' and scene in [1,2,3]:
  d.rounded_rectangle((145,350,1775,850),radius=35,fill='white')
  vals=[0,2,4,6];ps=[.15,.25,.35,.25]
  d.line([(240,750),(760,750)],fill=INK,width=2)
  text(d,(225,415),'Probability of each value',27,INK)
  for j,(x,prob) in enumerate(zip(vals,ps)):
   X=265+j*125;col=TEAL if scene==1 or x>=4 else '#b8c9cb';Y=750-prob*650
   d.rectangle((X,Y,X+80,750),fill=col);text(d,(X+10,Y-38),f'{prob:.2f}',25,INK);text(d,(X+28,765),str(x),27,INK)
  text(d,(780,773),'X',24,INK)
  lines={1:['All four probabilities sum to 1.','Each bar belongs to one X value.'],2:['X≥4 selects the bars at 4 and 6.','These two events are disjoint.'],3:['P(X≥4)=0.35+0.25=0.60','Add probabilities, not X values.']}[scene]
  for j,t in enumerate(lines):text(d,(885,515+j*80),t,34 if j==0 else 29,TEAL if j==0 else INK)
 elif vid=='binomial-pascal-row-method' and scene in [1,2,3]:
  d.rounded_rectangle((145,350,1775,850),radius=35,fill='white')
  row5=[1,5,10,10,5,1];row6=[1,6,15,20,15,6,1]
  text(d,(270,470),'Row 5',30,INK);text(d,(270,670),'Row 6',30,INK)
  for j,n in enumerate(row5):text(d,(610+j*140,470),str(n),48,INK)
  for j,n in enumerate(row6):
   if scene==1 and j not in [0,6]:t='?'
   else:t=str(n)
   text(d,(540+j*140,670),t,48,TEAL)
  if scene>=2:
   for j in range(1,6):
    X=560+j*140;d.line([(X-65,535),(X,635)],fill='#afbdbe',width=2);d.line([(X+75,535),(X,635)],fill='#afbdbe',width=2)
  text(d,(565,795),'Each interior entry adds the two above it.',32,INK)
 else:draw_card(s,d,scene,p)
def lessons(doc):
 out=make_lessons(SPECS,doc)
 for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:draw(s,d,scene,p)
 return out
