import json
from pathlib import Path
from collections import Counter
from card_lessons import make_lessons,draw_card
import generate_sample_videos as v
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g7-u7-u8/lesson-specs.json').read_text())
def ranges(spec,d,scene,p):
 if scene not in [0,1,2]:return draw_card(spec,d,scene,p)
 d.rounded_rectangle((145,360,1775,840),radius=35,fill='white')
 for label,values,y in [('A',[3,5,5,6,9],525),('B',[1,4,7,10,12],745)]:
  v.text(d,(245,y-45),label,54,v.TEAL,True)
  x0=450;scale=90;d.line((x0,y,x0+13*scale,y),fill=v.INK,width=3)
  for x in range(14):v.text(d,(x0+x*scale,y+12),str(x),25,v.MUTED,anchor='mt');d.line((x0+x*scale,y,x0+x*scale,y+7),fill=v.INK,width=2)
  c=Counter()
  for x in values:
   py=y-28-c[x]*30;c[x]+=1;px=x0+x*scale;d.ellipse((px-10,py-10,px+10,py+10),fill=v.TEAL)
 v.centered(d,895,['Each dot is one observation. Compare the ranges.','Range A = 9 − 3 = 6','Range B = 12 − 1 = 11'][scene],40,v.TEAL,True)
def lessons(doc):
 out=make_lessons(SPECS,doc)
 s=next(s for s in SPECS if s['video_id']=='statistics-difference-ranges');v.DRAW[s['video_id']]=lambda d,scene,p:ranges(s,d,scene,p)
 return out
