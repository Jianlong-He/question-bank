import json,math
from pathlib import Path
from card_lessons import make_lessons,draw_card
import generate_sample_videos as video
from generate_sample_videos import text,TEAL,INK,MUTED,font
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g8-u5/lesson-specs.json').read_text())
def diagram(s,d,scene,p):
 vid=s['video_id']
 if scene not in [1,2,3] or vid not in ['geometry-isosceles-vertex-angle','geometry-circle-radius-diameter','geometry-space-diagonal-box','geometry-coordinate-diagonal-distance']:return draw_card(s,d,scene,p)
 d.rounded_rectangle((145,360,1775,840),radius=35,fill='white')
 if vid=='geometry-isosceles-vertex-angle':
  a,b,c=(340,730),(740,730),(540,730-200*math.tan(math.radians(47)))
  d.polygon([a,b,c],fill='#e1f2ed',outline=TEAL,width=5)
  for edge in [(a,c),(b,c)]:
   (x,y),(u,v)=edge;mx,my=(x+u)/2,(y+v)/2;dx,dy=u-x,v-y;L=math.hypot(dx,dy);d.line((mx-dy/L*12,my+dx/L*12,mx+dy/L*12,my-dx/L*12),fill=INK,width=4)
  text(d,(345,750),'47°',32,INK);text(d,(700,750),'47°',32,INK);text(d,(515,c[1]-50),'x',36,TEAL)
 elif vid=='geometry-circle-radius-diameter':
  cx,cy,r=540,610,160;d.ellipse((cx-r,cy-r,cx+r,cy+r),outline=TEAL,width=5);d.line((cx-r,cy,cx+r,cy),fill=INK,width=4);d.ellipse((cx-6,cy-6,cx+6,cy+6),fill=INK);d.line((cx,cy,cx+r,cy),fill='#bc6828',width=8);text(d,(410,650),'Diameter = 23 cm',30,INK);text(d,(580,563),'r',36,'#bc6828')
 elif vid=='geometry-coordinate-diagonal-distance':
  cx,cy,k=490,550,27
  def pt(x,y):return(cx+x*k,cy-y*k)
  for x in range(-6,9):d.line([pt(x,-5),pt(x,4)],fill='#e4e9ec',width=1)
  for y in range(-5,5):d.line([pt(-6,y),pt(8,y)],fill='#e4e9ec',width=1)
  d.line([pt(-6,0),pt(8,0)],fill=INK,width=2);d.line([pt(0,-5),pt(0,4)],fill=INK,width=2)
  a,b,c=pt(-5,-4),pt(7,1),pt(7,-4);d.line([a,c,b],fill='#bc6828',width=5);d.line([a,b],fill=TEAL,width=6)
  for x,y in [a,b]:d.ellipse((x-6,y-6,x+6,y+6),fill=TEAL)
  text(d,(a[0]-40,a[1]+18),'A(−5,−4)',27,INK);text(d,(b[0]-60,b[1]-46),'B(7,1)',27,INK);text(d,(480,685),'12 units',27,'#bc6828');text(d,(700,578),'5 units',26,'#bc6828');text(d,(335,772),'Grid step = 1 unit',27,MUTED)
  d.line((c[0]-17,c[1],c[0]-17,c[1]-17,c[0],c[1]-17),fill=INK,width=2)
 else:
  A,B,C,D=(310,715),(610,715),(765,610),(465,610);top=lambda p:(p[0],p[1]-155)
  for poly in [[A,B,C,D,A],[top(A),top(B),top(C),top(D),top(A)]]:d.line(poly,fill=TEAL,width=4)
  for q in [A,B,C,D]:d.line([q,top(q)],fill=TEAL,width=4)
  d.line([A,C],fill='#bc6828',width=4);d.line([A,top(C)],fill='#c03b39',width=6)
  text(d,(418,744),'12 cm',29,INK);text(d,(685,675),'4 cm',29,INK);text(d,(780,508),'3 cm',29,INK);text(d,(380,500),'Space diagonal d',28,'#c03b39');text(d,(370,795),'Schematic: not to scale',24,MUTED)
 lines=s['displays'][scene].split('\n')
 for j,line in enumerate(lines):
  size=40
  while d.textlength(line,font=font(size))>790:size-=1
  text(d,(900,510+j*90),line,size,TEAL if j==len(lines)-1 else INK)
def lessons(doc):
 result=make_lessons(SPECS,doc)
 for s in SPECS:video.DRAW[s['video_id']]=lambda d,scene,p,s=s:diagram(s,d,scene,p)
 return result
