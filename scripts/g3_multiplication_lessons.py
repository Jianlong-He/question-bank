"""Early multiplication methods with independently checked examples."""
import json
from pathlib import Path
from card_lessons import make_lessons,draw_card
import generate_sample_videos as video
from early_measurement_lessons import card
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g3-u1-u2/lesson-specs.json').read_text())
def label(d,x,y,s,size=34):d.text((x,y),s,font=video.font(size,True),fill=video.INK,anchor='mm')
def dots(d,x,y,rows,cols,gap=36):
 for r in range(rows):
  for c in range(cols):d.ellipse((x+c*gap-10,y+r*gap-10,x+c*gap+10,y+r*gap+10),fill=video.TEAL)
def draw(s,d,i,p):
 draw_card(s,d,i,p);vid=s['video_id']
 if vid=='multiply-write-groups-addition' and i<3:
  card(d)
  for k in range(5):
   x=335+k*290;d.rounded_rectangle((x-25,460,x+145,645),radius=18,outline=video.INK,width=3);dots(d,x+12,505,3,3, 40);label(d,x+60,705,f'Group {k+1}',28)
  label(d,960,790,'5 equal groups; 9 dots in each group',38)
 if vid=='multiply-zero-one-early' and i<3:
  card(d);label(d,600,440,'0 trays',40);label(d,1310,440,'1 full tray',40)
  d.rounded_rectangle((1100,495,1510,670),radius=15,outline=video.INK,width=4);dots(d,1195,540,1,4,55);dots(d,1220,610,1,3,55)
  label(d,600,745,'0 beads');label(d,1310,745,'7 beads')
 if vid=='multiply-square-facts-early' and i<3:
  card(d);dots(d,700,460,7,7,48);label(d,1230,565,'7 rows',40);label(d,1230,650,'7 dots in each row',33);label(d,960,820,'Count all seven rows.',30)
def lessons(doc):
 assert [n for n in range(1,19) if 18%n==0]==[1,2,3,6,9,18]
 assert [n for n in range(1,26) if 25%n==0]==[1,5,25]
 result=make_lessons(SPECS,doc)
 for s in SPECS:video.DRAW[s['video_id']]=lambda d,i,p,s=s:draw(s,d,i,p)
 return result
