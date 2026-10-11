"""Verified geometry and measurement lesson diagrams."""
import json,math
from pathlib import Path
from card_lessons import make_lessons,draw_card
import generate_sample_videos as video
from early_measurement_lessons import card
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g3-u9-u11/lesson-specs.json').read_text())
def label(d,x,y,s,size=36):d.text((x,y),s,font=video.font(size,True),fill=video.INK,anchor='mm')
def polygon(d,labels=False):
 pts=[(960+240*math.cos(math.pi/3*n),600+240*math.sin(math.pi/3*n)) for n in range(6)]
 d.polygon(pts,fill=video.LIGHT,outline=video.TEAL,width=5)
 for i,(x,y) in enumerate(pts):
  if i==0:d.ellipse((x-8,y-8,x+8,y+8),fill=video.INK)
  a,b=pts[i],pts[(i+1)%6];cx=(a[0]+b[0])/2;cy=(a[1]+b[1])/2
  label(d,960+(cx-960)*1.22,600+(cy-600)*1.22,'7 cm' if labels else str(i+1),30)
def draw(s,d,i,p):
 draw_card(s,d,i,p);vid=s['video_id']
 if vid=='geometry-parallel-lines-early' and i in [0,1,2,3]:
  card(d)
  for x,t in [(570,'P'),(1350,'Q')]:label(d,x,425,t,45)
  for y in [550,700]:
   d.line((280,y,860,y),fill=video.TEAL,width=6)
   d.polygon([(280,y),(300,y-12),(300,y+12)],fill=video.TEAL);d.polygon([(860,y),(840,y-12),(840,y+12)],fill=video.TEAL)
  d.line((1080,515,1630,755),fill=video.INK,width=6);d.line((1080,755,1630,515),fill=video.INK,width=6)
  label(d,570,825,'Never meet',36);label(d,1350,825,'Meet at one point',36)
 elif vid in ['geometry-polygon-names-early','geometry-perimeter-equal-sides-early'] and i in [0,1,2]:
  if vid=='geometry-polygon-names-early' and i==2:return
  card(d);polygon(d,vid=='geometry-perimeter-equal-sides-early')
 elif vid=='measurement-square-unit-definition' and i in [0,1,2]:
  card(d)
  for k in range(3):
   x=600+k*240;d.rectangle((x,510,x+240,750),fill=video.LIGHT,outline=video.TEAL,width=4)
   label(d,x+120,625,'1 sq ft',36)
  label(d,720,470,'1 ft',36);label(d,520,630,'1 ft',36)
  label(d,960,815,'3 equal tiles cover 3 square feet',38)
 elif vid=='measurement-square-decimetre-conversion' and i in [1,2]:
  card(d)
  for r in range(10):
   for c in range(10):d.rectangle((750+c*32,465+r*32,782+c*32,497+r*32),fill=video.LIGHT,outline=video.TEAL,width=2)
  label(d,910,415,'1 dm = 10 cm',36);label(d,1205,625,'10 rows',36);label(d,910,835,'10 × 10 = 100 square cm',38)
 elif vid=='geometry-perimeter-many-sides-early' and i in [0,1]:
  card(d);pts=[(680,450),(1240,450),(1240,810),(890,810),(890,570),(680,570)]
  d.polygon(pts,fill=video.LIGHT,outline=video.TEAL,width=5)
  for x,y,t in [(960,415,'8 cm'),(1320,630,'6 cm'),(1070,850,'5 cm'),(970,685,'4 cm'),(785,610,'3 cm'),(595,510,'2 cm')]:label(d,x,y,t,32)
def lessons(doc):
 result=make_lessons(SPECS,doc)
 for s in SPECS:video.DRAW[s['video_id']]=lambda d,i,p,s=s:draw(s,d,i,p)
 return result
