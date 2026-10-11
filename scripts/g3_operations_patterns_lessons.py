"""Verified Grade3 operations, story structure, patterns and parity."""
import json
from pathlib import Path
from card_lessons import make_lessons,draw_card
import generate_sample_videos as video
from early_measurement_lessons import card
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g3-u7-u8/lesson-specs.json').read_text())
def label(d,x,y,s,size=36):d.text((x,y),s,font=video.font(size,True),fill=video.INK,anchor='mm')
def draw(s,d,i,p):
 draw_card(s,d,i,p);vid=s['video_id']
 if vid=='story-remaining-then-divide-early' and i==1:
  card(d);x=330;y=525;width=1260
  split=x+width*18/74
  d.rectangle((x,y,split,y+100),fill='#BAC7C7');d.rectangle((split,y,x+width,y+100),fill=video.TEAL)
  label(d,960,430,'Whole book: 74 pages',42);label(d,(x+split)/2,680,'18 read',34);label(d,(split+x+width)/2,680,'56 pages left',40)
  label(d,960,785,'74 − 18 = 56 pages',42)
 elif vid=='story-total-then-share-early' and i in [1,2,3]:
  card(d);groups=5 if i==1 else 10;per=8 if i==1 else 4
  for j in range(groups):
   x=295+(j%5)*285;y=450+(j//5)*150
   d.rounded_rectangle((x,y,x+230,y+125),radius=12,outline=video.TEAL,width=3)
   for n in range(per):
    dx=x+55+(n%4)*40;dy=y+40+(n//4)*45
    d.ellipse((dx-10,dy-10,dx+10,dy+10),fill=video.TEAL)
  label(d,960,795,'5 bags × 8 marbles = 40 marbles' if i==1 else '10 children × 4 marbles = 40 marbles',38)
 elif vid=='story-cups-to-tables-early' and i in [2,3]:
  card(d)
  for t in range(3):
   x=255+t*485;d.rounded_rectangle((x,440,x+445,730),radius=20,fill=video.LIGHT,outline=video.TEAL,width=3)
   label(d,x+222,475,f'Table {t+1}',32)
   for c in range(3):
    cx=x+20+c*140;d.rectangle((cx,520,cx+125,680),fill='white',outline=video.INK,width=2)
    for n in range(7):
     dx=cx+25+(n%3)*38;dy=552+(n//3)*44;d.ellipse((dx-7,dy-7,dx+7,dy+7),fill=video.TEAL)
   label(d,x+222,707,'3 cups, 7 pencils each',27)
  label(d,960,795,'Each table: 3 × 7 = 21 pencils',40)
 elif vid=='pattern-square-numbers-early' and i==2:
  card(d)
  for r in range(7):
   for c in range(7):
    x=820+c*42;y=450+r*42;d.ellipse((x-9,y-9,x+9,y+9),fill=video.TEAL)
  label(d,960,790,'7 rows × 7 dots = 49 dots',42)
def lessons(doc):
 result=make_lessons(SPECS,doc)
 for s in SPECS:video.DRAW[s['video_id']]=lambda d,i,p,s=s:draw(s,d,i,p)
 return result
