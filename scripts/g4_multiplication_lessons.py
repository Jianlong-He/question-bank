"""Verified Grade4 multiplicative comparisons, grids, columns and area."""
import json
from pathlib import Path
from card_lessons import make_lessons,draw_card
import generate_sample_videos as video
from early_measurement_lessons import card
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g4-u3-u4/lesson-specs.json').read_text())
def label(d,x,y,t,size=36):d.text((x,y),str(t),font=video.font(size,True),fill=video.INK,anchor='mm')
def grid(d,showparts=True):
 xs=[610,1010,1410];ys=[470,625,780]
 for x in xs:d.line((x,ys[0],x,ys[-1]),fill=video.TEAL,width=4)
 for y in ys:d.line((xs[0],y,xs[-1],y),fill=video.TEAL,width=4)
 label(d,810,420,'30');label(d,1210,420,'2')
 label(d,515,550,'40' if showparts else '?');label(d,515,700,'7' if showparts else '?')
 for x,y,t in [(810,550,1200),(1210,550,80),(810,700,210),(1210,700,14)]:label(d,x,y,t,48)
 label(d,960,830,'Area grid shown schematically; not to scale.',30)
def draw(s,d,i,p):
 draw_card(s,d,i,p);vid=s['video_id']
 if vid=='multiply-area-grid-missing-factor' and i in [1,2,3]:card(d);grid(d,i>1)
 elif vid=='multiply-single-digit-carry-columns' and i in [1,2,3,4]:
  card(d);xs=[580,770,960,1150,1340]
  for x,t in zip(xs,['10,000','1000','100','10','1']):label(d,x,400,t,30)
  for x,t in zip(xs,'03627'):label(d,x,535,t,56)
  label(d,430,630,'×',48);label(d,1340,630,'4',56)
  if i<4:
   k,n={1:(3,2),2:(2,1),3:(1,2)}[i];label(d,xs[k],460,f'+{n}',34)
  d.line((450,685,1440,685),fill=video.INK,width=4)
  for x,t in zip(xs,{1:'    8',2:'   08',3:'  508',4:'14508'}[i]):label(d,x,745,t,56)
  label(d,960,830,'Small + value: carry into the next column.',30)
 elif vid=='geometry-area-place-parts' and i in [1,2,3]:
  card(d);xs=[450,1000,1300,1530];ys=[510,735]
  for k,(left,right) in enumerate(zip(xs,xs[1:])):
   d.rectangle((left,ys[0],right,ys[1]),fill=video.LIGHT,outline=video.TEAL,width=4);label(d,(left+right)/2,450,['100 m','40 m','3 m'][k],36)
   if i>1:label(d,(left+right)/2,620,['600 m²','240 m²','18 m²'][k],36)
  label(d,350,620,'6 m',36);label(d,960,825,'Place-value strips shown schematically; not to scale.',30)
def lessons(doc):
 result=make_lessons(SPECS,doc)
 for s in SPECS:video.DRAW[s['video_id']]=lambda d,i,p,s=s:draw(s,d,i,p)
 return result
