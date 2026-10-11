"""Verified Grade 3 place-value, arithmetic and division methods."""
import json
from pathlib import Path
from card_lessons import make_lessons,draw_card
import generate_sample_videos as video
from early_measurement_lessons import card
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g3-u3-u4/lesson-specs.json').read_text())
def label(d,x,y,s,size=36):d.text((x,y),s,font=video.font(size,True),fill=video.INK,anchor='mm')
def draw(s,d,i,p):
 draw_card(s,d,i,p);vid=s['video_id']
 if vid=='place-six-digit-chart' and i in [1,2]:
  card(d)
  labels=[['Hundred','thousands'],['Ten','thousands'],['Thousands'],['Hundreds'],['Tens'],['Ones']]
  for k,parts in enumerate(labels):
   x=240+k*240;d.rounded_rectangle((x,455,x+230,735),radius=15,fill=video.LIGHT,outline=video.TEAL,width=3)
   for j,part in enumerate(parts):label(d,x+115,500+j*42,part,29)
   label(d,x+115,655,'381506'[k] if i==2 else '?',72)
  label(d,960,800,'381,506: one digit in each place',36)
 if vid=='divide-share-group-meanings' and i in [1,2]:
  card(d);n=4 if i==1 else 7;per=7 if i==1 else 4
  width=330 if n==4 else 195;gap=25;start=(1920-(width+gap)*n+gap)/2
  for k in range(n):
   x=start+k*(width+gap)
   d.rounded_rectangle((x,485,x+width,670),radius=18,outline=video.TEAL,width=4)
   cols=4 if per==7 else 2
   for dot in range(per):
    dx=x+width/2+(dot%cols-(cols-1)/2)*42;dy=535+(dot//cols)*60
    d.ellipse((dx-12,dy-12,dx+12,dy+12),fill=video.TEAL)
   label(d,x+width/2,720,('Child' if i==1 else 'Bag')+' '+str(k+1),28)
  label(d,960,795,'4 children; 7 beads each' if i==1 else '7 bags; 4 beads in each',40)
def lessons(doc):
 result=make_lessons(SPECS,doc)
 for s in SPECS:video.DRAW[s['video_id']]=lambda d,i,p,s=s:draw(s,d,i,p)
 return result
