"""Reviewed division, factor and repeating-pattern lessons."""
import json,math
from pathlib import Path
from card_lessons import make_lessons,draw_card
import generate_sample_videos as video
from early_measurement_lessons import card
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g4-u5-u6/lesson-specs.json').read_text())
def label(d,x,y,t,size=36):d.text((x,y),str(t),font=video.font(size,True),fill=video.INK,anchor='mm')
def drawshape(d,x,y,k):
 if k==0:d.ellipse((x-50,y-50,x+50,y+50),fill=video.TEAL)
 if k==1:d.polygon([(x,y-60),(x-65,y+50),(x+65,y+50)],fill=video.TEAL)
 if k==2:d.rectangle((x-50,y-50,x+50,y+50),fill=video.TEAL)
 if k==3:
  pts=[(x+(60 if j%2==0 else 26)*math.cos(-math.pi/2+j*math.pi/5),y+(60 if j%2==0 else 26)*math.sin(-math.pi/2+j*math.pi/5)) for j in range(10)];d.polygon(pts,fill=video.TEAL)
def draw(s,d,i,p):
 draw_card(s,d,i,p);vid=s['video_id']
 if vid=='divide-small-quotient-remainder' and i in [2,3]:
  card(d)
  for row in range(2):
   for col in range(3):
    x=260+col*465;y=420+row*185;d.rounded_rectangle((x,y,x+360,y+140),radius=16,outline=video.TEAL,width=3)
    for j in range(7):
     xx=x+55+(j%4)*80;yy=y+45+(j//4)*52;d.ellipse((xx-13,yy-13,xx+13,yy+13),fill=video.TEAL)
  label(d,1580,565,'Left',34);d.ellipse((1567,612,1593,638),fill=video.TEAL);label(d,960,815,'6 equal trays × 7 beads; 1 bead left over',34)
 elif vid=='story-nested-groups-total-share' and i in [1,2,3]:
  card(d)
  for k in range(7):
   x=250+k*205;d.rectangle((x,455,x+170,715),outline=video.TEAL,width=3)
   for j in range(1,4):d.line((x,455+j*65,x+170,455+j*65),fill=video.TEAL,width=2)
   if i>1:
    for j in range(4):label(d,x+85,486+j*65,'18',30)
  label(d,960,780,'7 cases × 4 shelves = 28 shelves',36)
  label(d,960,840,'18 books per shelf; 504 books total' if i>1 else 'Each box is one case; each row is one shelf.',30)
 elif vid=='pattern-repeating-cycles' and i==1:
  card(d)
  for k,t in enumerate(['Thursday','Friday','Saturday','Sunday']):
   x=440+k*340;label(d,x,560,t,42)
   if k<3:label(d,x+170,560,'→',40)
  label(d,960,720,'38 = 5 complete weeks + 3 extra days',38)
 elif vid=='pattern-repeating-cycles' and i in [2,3]:
  card(d);names=['Circle','Triangle','Square','Star'];chosen=1 if i==2 else 3
  for k in range(4):
   x=440+k*340;drawshape(d,x,555,k);label(d,x,670,names[k],34);label(d,x,430,k+1,34)
   if k==chosen:d.rounded_rectangle((x-140,390,x+140,715),radius=20,outline=video.TEAL,width=5)
  label(d,960,810,'Item 30: remainder 2 → Triangle' if i==2 else 'Item 28: remainder 0 → last item, Star',36)
def lessons(doc):
 result=make_lessons(SPECS,doc)
 for s in SPECS:video.DRAW[s['video_id']]=lambda d,i,p,s=s:draw(s,d,i,p)
 return result
