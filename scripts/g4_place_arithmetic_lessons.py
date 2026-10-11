"""Reviewed place-value and large-number arithmetic lessons."""
import json
from pathlib import Path
from card_lessons import make_lessons,draw_card
import generate_sample_videos as video
from early_measurement_lessons import card
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g4-u1-u2/lesson-specs.json').read_text())
def label(d,x,y,t,size=36):d.text((x,y),t,font=video.font(size,True),fill=video.INK,anchor='mm')
def draw(s,d,i,p):
 draw_card(s,d,i,p);vid=s['video_id']
 if vid=='add-large-place-columns' and i in [1,2,3,4]:
  card(d)
  for k,t in enumerate(['100k','10k','1k','100','10','1']):label(d,610+k*150,400,t,30)
  for y,number in [(505,'027864'),(615,'395728')]:
   for k,t in enumerate(number):label(d,610+k*150,y,t,56)
  label(d,420,615,'+',56);d.line((450,675,1500,675),fill=video.INK,width=4)
  shown={1:'     2',2:'   592',3:' 23592',4:'423592'}[i]
  for k,t in enumerate(shown):label(d,610+k*150,740,t,56)
  label(d,960,845,'Work right to left; carry each extra ten to the next column.',30)
 elif vid=='subtract-large-through-zero' and i in [2,3]:
  card(d)
  for k,t in enumerate(['100k','10k','1k','100','10','1']):label(d,570+k*155,415,t,30)
  for y,values in [(525,[5,9,9,11,9,14]),(630,[2,7,8,5,6,9])]:
   for k,t in enumerate(values):label(d,570+k*155,y,str(t),52)
  label(d,390,630,'−',54);d.line((420,685,1475,685),fill=video.INK,width=4)
  if i==3:
   for k,t in enumerate('321635'):label(d,570+k*155,745,t,52)
  label(d,960,845,'Regrouped top row still represents 600,204.',34)
def lessons(doc):
 result=make_lessons(SPECS,doc)
 for s in SPECS:video.DRAW[s['video_id']]=lambda d,i,p,s=s:draw(s,d,i,p)
 return result
