"""Reviewed fractional arithmetic and measurement plots."""
import json
from pathlib import Path
from card_lessons import make_lessons,draw_card
import generate_sample_videos as video
from early_measurement_lessons import card
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g4-u7-u8/lesson-specs.json').read_text())
def label(d,x,y,t,size=34):d.text((x,y),str(t),font=video.font(size,True),fill=video.INK,anchor='mm')
def plot(d,highlight=None):
 card(d);y=665;x0=360;dx=200
 d.line((x0,y,x0+6*dx,y),fill=video.INK,width=4)
 labels=['2','2 1/4','2 1/2','2 3/4','3','3 1/4','3 1/2']
 for i,t in enumerate(labels):
  x=x0+i*dx;d.line((x,y-15,x,y+15),fill=video.INK,width=4);label(d,x,y+58,t,32)
 for pos,num in [(1,2),(3,1),(4,1),(5,1)]:
  for j in range(num):
   x=x0+pos*dx;yy=y-65-j*85;d.ellipse((x-22,yy-22,x+22,yy+22),fill=video.TEAL)
   if highlight=='threshold' and pos>=3:d.ellipse((x-33,yy-33,x+33,yy+33),outline=video.INK,width=4)
   if highlight=='mode' and pos==1:d.ellipse((x-33,yy-33,x+33,yy+33),outline=video.INK,width=4)
 label(d,960,805,'Ribbon length (metres); each dot = one ribbon',32)
 label(d,960,420,'Five ribbons; scale intervals are 1/4 metre',38)
def draw(s,d,i,p):
 v=s['video_id']
 if v.startswith('fraction-plot-') and (i==0 or (v.endswith('count-mode-threshold') and i in [1,2,3,4])):
  plot(d,'mode' if i in [2,3] else 'threshold' if i==4 else None)
  if i==0:label(d,960,865,'Read the scale and count every dot.',30)
  elif i==2:label(d,960,865,'2 ribbons at 2 1/4 m',32)
  elif i==3:label(d,960,865,'Mode = 2 1/4 m',32)
  elif i==4:label(d,960,865,'At least 2 3/4 m: 3 ribbons',32)
 else:draw_card(s,d,i,p)

def lessons(doc):
 result=make_lessons(SPECS,doc)
 for s in SPECS:video.DRAW[s['video_id']]=lambda d,i,p,s=s:draw(s,d,i,p)
 return result
