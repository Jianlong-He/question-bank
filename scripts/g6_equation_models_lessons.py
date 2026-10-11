import json
from pathlib import Path
from card_lessons import make_lessons
import generate_sample_videos as v
from generate_sample_videos import text,centered,TEAL,INK,MUTED
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g6-u7/lesson-specs.json').read_text())
def graph(d,scene,p):
 d.rounded_rectangle((145,360,1775,860),radius=35,fill='white')
 x0,y0,sx,sy=260,800,84,11
 for x in range(9):
  xx=x0+x*sx;d.line((xx,425,xx,y0),fill='#DDE4E3',width=2);text(d,(xx,817),str(x),27,INK,anchor='mt')
 for y in range(0,33,4):
  yy=y0-y*sy;d.line((x0,yy,x0+8*sx,yy),fill='#DDE4E3',width=2);text(d,(x0-18,yy),str(y),27,INK,anchor='rm')
 d.line((x0,y0,x0+8*sx+25,y0),fill=INK,width=4);d.line((x0,y0,x0,400),fill=INK,width=4)
 text(d,(960,795),'x',34,INK);text(d,(243,383),'y',34,INK)
 d.line((x0,y0,x0+8*sx,y0-32*sy),fill=TEAL,width=7)
 if scene in [2,3]:
  x,y=(5,20) if scene==2 else (7,28);xx,yy=x0+x*sx,y0-y*sy
  d.line((xx,y0,xx,yy,x0,yy),fill='#DA9346',width=5)
  d.ellipse((xx-10,yy-10,xx+10,yy+10),fill='#DA9346')
 lines={1:['y = 4x','(0, 0), (1, 4), (2, 8)','x scale: 1 per step','y scale: 4 per step'],2:['Start at x = 5','Up to the line','Across: y = 20'],3:['Start at y = 28','Across to the line','Down: x = 7']}[scene]
 for i,line in enumerate(lines):text(d,(1360,455+i*82),line,43,TEAL if i==len(lines)-1 else INK,True,anchor='mt')
def numberline(d,scene,p):
 d.rounded_rectangle((145,360,1775,860),radius=35,fill='white')
 boundary=14 if scene==1 else -2;center=960;y=620;step=150
 centered(d,410,'x > 14' if scene==1 else 'x ≤ −2',70,INK,True)
 d.line((280,y,1640,y),fill=INK,width=4)
 for i in range(-4,5):
  xx=center+i*step;d.line((xx,y-14,xx,y+14),fill=INK,width=3);text(d,(xx,y+30),str(boundary+i),35,INK,anchor='mt')
 end=1640 if scene==1 else 280;direction=1 if scene==1 else -1
 d.line((center,y,end,y),fill=TEAL,width=12);d.polygon([(end,y),(end-direction*30,y-18),(end-direction*30,y+18)],fill=TEAL)
 d.ellipse((center-16,y-16,center+16,y+16),fill='white' if scene==1 else TEAL,outline=TEAL,width=6)
 centered(d,750,'Open: 14 excluded; shade right' if scene==1 else 'Filled: −2 included; shade left',45,TEAL,True)
def lessons(doc):
 ls=make_lessons(SPECS,doc)
 for lesson in ls:
  vid=lesson['video_id'];original=v.DRAW[vid]
  if vid=='proportion-read-line':v.DRAW[vid]=lambda d,scene,p,old=original:graph(d,scene,p) if scene in [1,2,3] else old(d,scene,p)
  if vid=='inequality-number-line-boundaries':v.DRAW[vid]=lambda d,scene,p,old=original:numberline(d,scene,p) if scene in [1,2] else old(d,scene,p)
 return ls
