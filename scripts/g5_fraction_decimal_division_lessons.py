import json
from pathlib import Path
from card_lessons import make_lessons,draw_card
import generate_sample_videos as v
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g5-u7-u9/lesson-specs.json').read_text())
def draw(s,d,scene,p):
 vid=s['video_id']
 if vid=='fraction-unit-divide-model':
  d.rounded_rectangle((145,350,1775,875),radius=35,fill='white');x=260;y=450;cw=105;ch=80
  for c in range(3):
   for r in range(4):
    color='#9dd9d1' if c==0 else 'white'
    if c==0 and r==0 and scene>=2:color='#f0c077'
    d.rectangle((x+c*cw,y+r*ch,x+(c+1)*cw,y+(r+1)*ch),fill=color)
  for c in range(4):d.line((x+c*cw,y,x+c*cw,y+4*ch),fill=v.INK,width=4)
  d.line((x,y,x+3*cw,y),fill=v.INK,width=4);d.line((x,y+4*ch,x+3*cw,y+4*ch),fill=v.INK,width=4)
  if scene>=2:
   for r in range(1,4):d.line((x,y+r*ch,x+3*cw,y+r*ch),fill=v.INK,width=3)
  lines=[['Select 1 of 3 equal columns','Divide that third into 4 shares'],['Selected column = 1/3'],['3 × 4 = 12 equal cells'],['One share = 1/12'],['4 × 1/12 = 1/3']][scene]
  for i,line in enumerate(lines):v.text(d,(700,510+i*85),line,44,v.TEAL)
 elif vid=='fraction-whole-divide-unit-model':
  d.rounded_rectangle((145,350,1775,875),radius=35,fill='white')
  for row in range(5):
   for c in range(4):d.rectangle((250+c*90,405+row*85,250+(c+1)*90,465+row*85),fill='#9dd9d1',outline=v.INK,width=3)
  lines=[['5 wholes; each split into fourths'],['1 whole = 4 quarter-pieces'],['5 × 4 = 20 pieces'],['5 ÷ 1/4 = 20'],['20 pieces × 1/4 = 5 wholes']][scene]
  for i,line in enumerate(lines):v.text(d,(730,550+i*85),line,43,v.TEAL)
 else:draw_card(s,d,scene,p)
def lessons(doc):
 ls=make_lessons(SPECS,doc)
 for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:draw(s,d,scene,p)
 return ls
