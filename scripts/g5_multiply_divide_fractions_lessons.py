import json
from pathlib import Path
from card_lessons import make_lessons,draw_card
import generate_sample_videos as v
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g5-u5-u6/lesson-specs.json').read_text())
def grid(d,rows,cols,shrows,shcols,x,y,cell):
 for r in range(rows):
  for c in range(cols):d.rectangle((x+c*cell,y+r*cell,x+(c+1)*cell,y+(r+1)*cell),fill='#9dd9d1' if r<shrows and c<shcols else 'white',outline=v.INK,width=3)
def draw(s,d,scene,p):
 vid=s['video_id']
 if vid=='multiply-standard-three-by-three':
  d.rounded_rectangle((145,350,1775,875),radius=35,fill='white')
  lines=['    247','  × 386','───────']+(['   1482'] if scene>=1 else [])+(['  19760'] if scene>=2 else [])+(['  74100'] if scene>=3 else [])+(['───────','  95342'] if scene>=4 else [])
  # Fixed-width columns keep every partial product in its place.
  from PIL import ImageFont
  font=ImageFont.truetype('/System/Library/Fonts/Menlo.ttc',45)
  for i,line in enumerate(lines):d.text((1060,375+i*53),line,font=font,fill=v.TEAL if i==len(lines)-1 and scene==4 else v.INK)
  labels=['247 × 386','247 × 6 = 1,482','247 × 80 = 19,760','247 × 300 = 74,100','Sum = 95,342']
  v.text(d,(220,560),labels[scene],43,v.INK)
 elif vid in ['fraction-grid-shaded-fraction','fraction-grid-dimensions']:
  d.rounded_rectangle((145,350,1775,875),radius=35,fill='white')
  shaded=vid=='fraction-grid-shaded-fraction';grid(d,6,9 if shaded else 8,4 if shaded else 0,6 if shaded else 0,225,430,52)
  v.text(d,(225,780),'6 rows × '+('9' if shaded else '8')+' columns',35,v.INK)
  lines=([['Whole: 54 equal cells','Shaded: 4 rows × 6 columns'],['6 × 9 = 54 cells'],['4 × 6 = 24 shaded'],['Shaded / whole = 24/54'],['24/54 = 4/9']][scene] if shaded else [['Whole height: 3 m','Whole width: 7 m'],['Cell height: 3 ÷ 6','= 1/2 m'],['Cell width: 7 ÷ 8','= 7/8 m'],['6 × 1/2 = 3 m'],['8 × 7/8 = 7 m']][scene])
  for i,line in enumerate(lines):v.text(d,(800,510+i*80),line,43,v.TEAL)
 else:draw_card(s,d,scene,p)
def lessons(doc):
 ls=make_lessons(SPECS,doc)
 for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:draw(s,d,scene,p)
 return ls
