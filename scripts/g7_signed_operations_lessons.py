import json
from pathlib import Path
from card_lessons import make_lessons,draw_card
import generate_sample_videos as video
from generate_sample_videos import text,centered,TEAL,INK,MUTED
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g7-u3-u4/lesson-specs.json').read_text())
def tile_rows(d,positive,negative,cancel=0):
 for row,(n,symbol,color) in enumerate([(positive,'+',TEAL),(negative,'−','#b8463e')]):
  y=460+row*135;text(d,(190,y+40),'Positive' if row==0 else 'Negative',35,INK,True,'lm')
  for i in range(n):
   x=460+i*120;fill='#e5e6e3' if i<cancel else color
   d.rounded_rectangle((x,y,x+82,y+82),radius=13,fill=fill,outline=color,width=3)
   text(d,(x+41,y+41),symbol,48,color if i<cancel else 'white',True,'mm')
   if i<cancel:d.line((x+8,y+74,x+74,y+8),fill=MUTED,width=3)
  text(d,(1550,y+41),f'{n} tiles',35,INK,True,'lm')
def draw_tiles(spec,d,scene,p):
 if scene==0:return draw_card(spec,d,scene,p)
 d.rounded_rectangle((145,355,1775,880),radius=35,fill='white')
 if spec['video_id']=='integer-zero-pairs-count-value':
  pos,neg,cancel=[(3,3,0),(3,3,3),(5,8,0),(5,8,5)][scene-1]
  title=['3 zero pairs: 6 physical tiles','Each matched pair has value zero','After adding: 5 positive, 8 negative','Five pairs cancel; three negatives remain'][scene-1]
  bottom=['3 × 2 = 6 tiles','3 × (+1 − 1) = 0','5 − 8 = −3','13 physical tiles; represented value −3'][scene-1]
 else:
  pos,neg,cancel=[(7,5,0),(7,2,0),(3,2,0),(3,2,2)][scene-1]
  title=['Starting tiles: value 2','Remove 3 negatives: value rises to 5','Then remove 4 positives: value falls to 1','Two pairs cancel; one positive remains'][scene-1]
  bottom=['7 − 5 = 2','2 − (−3) = 5','5 − 4 = 1','3 − 2 = 1'][scene-1]
 centered(d,390,title,40,INK,True);tile_rows(d,pos,neg,cancel);centered(d,785,bottom,47,TEAL,True)
 if scene==4:centered(d,915,'Check the method, then try your worksheet.',32,MUTED)
def lessons(doc):
 ls=make_lessons(SPECS,doc)
 for s in SPECS:
  if s['video_id'] in ['integer-zero-pairs-count-value','integer-tiles-remove-signed']:video.DRAW[s['video_id']]=lambda d,scene,p,s=s:draw_tiles(s,d,scene,p)
 return ls
