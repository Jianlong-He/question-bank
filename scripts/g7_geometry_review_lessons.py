import json,math
from pathlib import Path
from card_lessons import make_lessons,draw_card,centered_math
import generate_sample_videos as v
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g7-u9/lesson-specs.json').read_text())
def draw(s,d,i,p):
 vid=s['video_id']
 if i not in [1,2,3] or vid not in ['geometry-area-quarter-circle','geometry-intersection-angle-pairs']:return draw_card(s,d,i,p)
 cx,cy,r=960,570,195
 if vid=='geometry-area-quarter-circle':
  box=(cx-r,cy-r,cx+r,cy+r);d.ellipse(box,fill='white',outline=v.TEAL,width=4);d.pieslice(box,-90,0,fill='#D0E8E2',outline=v.TEAL,width=4)
  d.line((cx-r,cy,cx+r,cy),fill=v.TEAL,width=3);d.line((cx,cy-r,cx,cy+r),fill=v.TEAL,width=3)
  v.text(d,(cx+r/2,cy+20),'14 cm',30,v.INK,True,anchor='mt');v.text(d,(cx+85,cy-105),'¼',48,v.INK,True,anchor='mm')
 else:
  def xy(a,rad):return cx+rad*math.cos(math.radians(a)),cy-rad*math.sin(math.radians(a))
  for a in [0,127]:d.line((*xy(a,260),*xy(a+180,260)),fill=v.TEAL,width=5)
  for a,label in [(63.5,'127°'),(153.5,'y' if i<3 else '53°'),(243.5,'x' if i<2 else '127°')]:v.text(d,xy(a,135),label,37,v.INK,True,anchor='mm')
 for n,line in enumerate(s['displays'][i].split('\n')):centered_math(d,825+65*n,line,40,v.TEAL)
def lessons(doc):
 out=make_lessons(SPECS,doc)
 for s in SPECS:v.DRAW[s['video_id']]=lambda d,i,p,s=s:draw(s,d,i,p)
 return out
