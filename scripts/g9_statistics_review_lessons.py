import json
from pathlib import Path
from card_lessons import make_lessons,draw_card
import generate_sample_videos as v
from generate_sample_videos import text,font,INK,TEAL,MUTED
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g9-u9-u11/lesson-specs.json').read_text())
def diagram(s,d,scene,p):
 vid=s['video_id']
 if vid=='statistics-histogram-uniform-gap' and scene in [1,2,3]:
  d.rounded_rectangle((145,345,1775,870),radius=35,fill='white')
  for j,counts in enumerate([[5,5,5,5],[4,0,7,3]]):
   x0=285+j*700;y0=725;bw=105;scale=38
   text(d,(x0+210,385),'A: uniform' if j==0 else 'B: gap in second bin',34,TEAL,anchor='mm')
   for y in [0,2,4,6,8]:
    d.line((x0,y0-y*scale,x0+4*bw,y0-y*scale),fill='#e0e8e4',width=1);text(d,(x0-18,y0-y*scale),str(y),24,MUTED,anchor='rm')
   for k,n in enumerate(counts):
    if n:d.rectangle((x0+k*bw,y0-n*scale,x0+(k+1)*bw,y0),fill='#aad8cd',outline=TEAL,width=3)
    text(d,(x0+(k+.5)*bw,y0-n*scale-18),str(n),28,INK,anchor='mm');text(d,(x0+(k+.5)*bw,y0+25),f'{k*10}–{(k+1)*10}',25,MUTED,anchor='mm')
   d.line((x0,y0,x0+4*bw,y0),fill=INK,width=2)
  text(d,(960,805),'Frequency counts in equal-width bins; intervals include left endpoint only',28,INK,anchor='mm')
 elif vid=='statistics-fit-balance-heuristic' and scene in [1,2,3]:
  d.rounded_rectangle((145,345,1775,870),radius=35,fill='white')
  table=[['x','Observed y','Predicted y','Residuals'],['0','3, 3, 0','2','+1, +1, −2'],['1','4, 4, 1','3','+1, +1, −2']]
  x0=245;y0=395;cw=355;ch=100
  for i,row in enumerate(table):
   for j,t in enumerate(row):
    b=(x0+j*cw,y0+i*ch,x0+(j+1)*cw,y0+(i+1)*ch);d.rectangle(b,fill='#e8f4ef' if i==0 else 'white',outline='#becbc6',width=2);text(d,((b[0]+b[2])/2,(b[1]+b[3])/2),t,32,TEAL if i==0 else INK,anchor='mm')
  text(d,(960,765),'4 observations above; 2 below; signed residual sum = 0',35,TEAL,anchor='mm')
 else:return draw_card(s,d,scene,p)
def lessons(doc):
 out=make_lessons(SPECS,doc)
 for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:diagram(s,d,scene,p)
 return out
