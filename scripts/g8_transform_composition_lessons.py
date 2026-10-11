import json
from pathlib import Path
from card_lessons import make_lessons,draw_card
import generate_sample_videos as video
from generate_sample_videos import text,TEAL,INK,MUTED,font
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g8-u6/lesson-specs.json').read_text())
def diagram(s,d,scene,p):
 if s['video_id']!='geometry-rigid-orientation' or scene not in [1,2,3]:return draw_card(s,d,scene,p)
 d.rounded_rectangle((145,340,1775,865),radius=35,fill='white')
 cx,cy,k=560,750,55
 def pt(x,y):return(cx+k*x,cy-k*y)
 for x in range(-5,6):d.line([pt(x,0),pt(x,5)],fill='#e4e9ec',width=1)
 for y in range(0,6):d.line([pt(-5,y),pt(5,y)],fill='#e4e9ec',width=1)
 d.line([pt(-5,0),pt(5,0)],fill=INK,width=2);d.line([pt(0,0),pt(0,5)],fill='#b66f4e',width=4)
 text(d,(550,780),'0',24,INK);text(d,(575,430),'y-axis mirror',26,'#b66f4e');text(d,(270,820),'Grid step = 1 unit',25,MUTED)
 for pts,names,color in [([(1,1),(4,1),(1,3)],['A','B','C'],TEAL),([(-1,1),(-4,1),(-1,3)],["A′","B′","C′"],'#8b55a1')]:
  d.polygon([pt(*q) for q in pts],outline=color,width=5)
  for (x,y),name in zip(pts,names):
   xx,yy=pt(x,y);d.ellipse((xx-5,yy-5,xx+5,yy+5),fill=color);text(d,(xx+(8 if x>0 else -43),yy-32),name,27,color)
  # An arrow on AB establishes the traversal order without implying an open path.
  a,b=pt(*pts[0]),pt(*pts[1]);mx,my=(a[0]+b[0])/2,a[1];sgn=1 if b[0]>a[0] else -1;d.polygon([(mx+sgn*12,my),(mx-sgn*8,my-9),(mx-sgn*8,my+9)],fill=color)
 for j,line in enumerate(s['displays'][scene].split('\n')):
  size=39
  while d.textlength(line,font=font(size))>800:size-=1
  text(d,(890,530+j*90),line,size,TEAL)
 text(d,(905,765),'Original: CCW    Image: CW',30,INK)
def lessons(doc):
 result=make_lessons(SPECS,doc)
 for s in SPECS:video.DRAW[s['video_id']]=lambda d,scene,p,s=s:diagram(s,d,scene,p)
 return result
