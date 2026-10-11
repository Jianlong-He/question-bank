"""Verified Grade3 time, measurement and fractional-scale lessons."""
import json
from pathlib import Path
from card_lessons import make_lessons,draw_card
import generate_sample_videos as video
from early_measurement_lessons import card,clock
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g3-u12-u14/lesson-specs.json').read_text())
def label(d,x,y,t,size=36):d.text((x,y),t,font=video.font(size,True),fill=video.INK,anchor='mm')
def scale(d,y,start,parts,offset,unit):
 x=420;w=1050;d.line((x,y,x+w,y),fill=video.INK,width=5)
 for k in range(parts+1):
  xx=x+k*w/parts;hh=24 if k in [0,parts] else 15;d.line((xx,y-hh,xx,y+hh),fill=video.INK,width=3)
  if k in [0,parts]:label(d,xx,y+65,f'{start+k//parts} {unit}',36)
 xx=x+offset*w/parts;d.ellipse((xx-12,y-12,xx+12,y+12),fill=video.TEAL)
 label(d,960,y-70,f'{parts} equal intervals; point {offset} marks past {start}',34)
def draw(s,d,i,p):
 draw_card(s,d,i,p);vid=s['video_id']
 if vid=='time-read-minutes-hour-boundary' and i in [0,1,2,3]:
  card(d);clock(d,11,35)
  label(d,1320,525,'Hour: 11',40);label(d,1320,625,'7 × 5 = 35 minutes',34)
  if i==3:label(d,1320,730,'11:35',58)
 elif vid=='time-elapsed-hours-minutes' and i in [1,2,3]:
  card(d);label(d,960,425,'Time jumps (not to scale)',32);xs=[330,675,1150,1570];times=['2:38','3:00','5:00','5:12'];spans=['22 minutes','2 hours','12 minutes']
  for j in range(3):
   d.line((xs[j],590,xs[j+1],590),fill=video.TEAL,width=6);label(d,(xs[j]+xs[j+1])/2,520,spans[j],32)
  for x,t in zip(xs,times):d.ellipse((x-8,582,x+8,598),fill=video.INK);label(d,x,660,t,42)
  if i==3:label(d,960,780,'22 + 12 = 34 minutes; total: 2 h 34 min',36)
 elif vid=='measurement-volume-container-count' and i in [2,3]:
  card(d)
  for k in range(5):
   x=310+k*270;d.rectangle((x,490,x+220,710),fill=video.LIGHT,outline=video.TEAL,width=4);label(d,x+110,605,'400 mL',34)
  label(d,960,800,'5 × 400 mL = 2000 mL = 2 L',40)
 elif vid=='measurement-volume-partial-container' and i==3:
  card(d);x=740;y=450;w=360;h=330
  d.rectangle((x,y+h*2/3,x+w,y+h),fill=video.LIGHT)
  d.rectangle((x,y,x+w,y+h),outline=video.TEAL,width=4)
  for k in [1,2]:d.line((x,y+h*k/3,x+w,y+h*k/3),fill=video.TEAL,width=2)
  label(d,1300,525,'Full cup: 30 mL',38);label(d,1300,685,'Extra: 10 mL',38);label(d,960,840,'10/30 = 1/3 cup',40)
 elif vid=='measurement-fractional-scale-reading' and i in [1,2,3]:
  card(d)
  if i in [1,2]:scale(d,590,4,4,3,'cm');label(d,960,790,'4 + 3/4 = 4.75 cm',40)
  else:scale(d,590,2,5,4,'m');label(d,960,790,'2 + 4/5 = 2.8 m',40)
def lessons(doc):
 result=make_lessons(SPECS,doc)
 for s in SPECS:video.DRAW[s['video_id']]=lambda d,i,p,s=s:draw(s,d,i,p)
 return result
