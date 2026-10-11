"""Fraction products and decimal-place diagrams, checked against analogous examples."""
import json
from pathlib import Path
from card_lessons import make_lessons,draw_card
import generate_sample_videos as v
from early_measurement_lessons import card
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g4-u9-u10/lesson-specs.json').read_text())
def text(d,x,y,t,size=34):d.text((x,y),str(t),font=v.font(size,True),fill=v.INK,anchor='mm')
def axis(d,y,left,right,point,name):
 x=300;dx=128;d.line((x,y,x+10*dx,y),fill=v.INK,width=4)
 for i in range(11):d.line((x+i*dx,y-15,x+i*dx,y+15),fill=v.INK,width=4)
 text(d,x,y+55,left);text(d,x+10*dx,y+55,right)
 px=x+point*dx;d.ellipse((px-20,y-20,px+20,y+20),fill=v.TEAL);text(d,px,y-58,name,38)
def grids(d):
 card(d)
 for k in range(3):
  x=290+k*460;y=415;s=34
  for row in range(10):
   for col in range(10):
    filled=k<2 or col*10+row<37
    d.rectangle((x+col*s,y+row*s,x+(col+1)*s,y+(row+1)*s),fill=v.TEAL if filled else 'white',outline=v.INK,width=2)
  text(d,x+170,800,'1 whole' if k<2 else '37/100',34)
def draw(s,d,i,p):
 vid=s['video_id']
 if vid=='decimal-fraction-scale-reading' and i in [0,1,2,3]:
  card(d)
  if i==0:
   axis(d,500,'2','3',6,'A');axis(d,700,'4.3','4.4',7,'B')
  elif i in [1,2]:
   axis(d,540,'2','3',6,'A');text(d,960,720,'10 equal steps: each step = 0.1',38)
   if i==2:text(d,960,790,'A = 2 + 6/10 = 2.6 = 2 3/5',38)
  else:
   axis(d,540,'4.3','4.4',7,'B');text(d,960,720,'0.1 ÷ 10 = 0.01 per step',38)
 elif vid=='decimal-shaded-place-grids' and i in [0,1,2]:grids(d)
 else:draw_card(s,d,i,p)
def lessons(doc):
 result=make_lessons(SPECS,doc)
 for s in SPECS:v.DRAW[s['video_id']]=lambda d,i,p,s=s:draw(s,d,i,p)
 return result
