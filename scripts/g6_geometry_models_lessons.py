import json,math
from pathlib import Path
from card_lessons import make_lessons
import generate_sample_videos as v
from generate_sample_videos import text,TEAL,INK,MUTED
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g6-u8-u10/lesson-specs.json').read_text())
C='#DA9346'
def card(d,lines):
 for i,line in enumerate(lines):text(d,(1345,440+i*80),line,43,TEAL if i==len(lines)-1 else INK,True,anchor='mt')
def grid(d):
 d.rounded_rectangle((145,330,1775,930),radius=35,fill='white')
 def xy(p):return 600+p[0]*31,640-p[1]*31
 for a in range(-9,10):
  x,y=xy((a,a));d.line((x,392,x,888),fill='#E4EAE8',width=2)
  if -8<=a<=8:d.line((321,y,879,y),fill='#E4EAE8',width=2)
  if a%2==0:
   text(d,(x,655),str(a),24,INK,anchor='mt')
   if a:text(d,(585,y),str(a),24,INK,anchor='rm')
 d.line((300,640,905,640),fill=INK,width=3);d.line((600,910,600,365),fill=INK,width=3)
 text(d,(922,638),'x',30,INK,anchor='mm');text(d,(600,350),'y',30,INK,anchor='mm')
 return xy

def point(d,xy,p,label,offset=(12,-20),color=TEAL):
 x,y=xy(p);d.ellipse((x-8,y-8,x+8,y+8),fill=color);text(d,(x+offset[0],y+offset[1]),label,29,color,True)
def coords(vid,d,scene):
 xy=grid(d);lines=[]
 if vid=='coordinate-signed-pairs':
  d.line((*xy((0,0)),*xy((-6,0)),*xy((-6,4))),fill=C,width=5);point(d,xy,(-6,4),'P(−6, 4)');lines=['Left 6: x = −6','Up 4: y = 4','P(−6, 4)']
  if scene==3:point(d,xy,(4,-6),'Q(4, −6)',offset=(-110,20),color=C);lines=['Q: right 4, down 6','P ≠ Q','Order matters']
 elif vid=='coordinate-quadrants-and-axes':
  for p,label in [((5,5),'I'),((-5,5),'II'),((-5,-5),'III'),((5,-5),'IV')]:text(d,xy(p),label,47,'#9AABA7',True,anchor='mm')
  if scene in [1,2]:point(d,xy,(-8,7),'A',offset=(10,-30));lines=['A(−8, 7)','x < 0; y > 0','Quadrant II']
  if scene==3:point(d,xy,(-3,0),'B',offset=(-15,35),color=C);lines=['B(−3, 0)','y = 0','On the x-axis']
 elif vid=='coordinate-signed-movement':
  a=(4,-2);mid=(-3,-2);b=(-3,4);d.line((*xy(a),*xy(mid)),fill=C,width=6)
  if scene>=2:d.line((*xy(mid),*xy(b)),fill=TEAL,width=6);point(d,xy,b,'B(−3, 4)',offset=(-155,-40))
  point(d,xy,a,'A(4, −2)',offset=(10,20));lines=['x = 4 − 7 = −3','y = −2 + 6 = 4','B(−3, 4)']
 elif vid=='coordinate-axis-distance':
  a=(-7,-3);b=(2,-3);c=(2,5);d.line((*xy(a),*xy(b)),fill=TEAL,width=6);d.line((*xy(b),*xy(c)),fill=C,width=6)
  for p,l in [(a,'A'),(b,'B'),(c,'C')]:point(d,xy,p,l)
  lines=['A(−7, −3), B(2, −3)','C(2, 5)','AB = 9; BC = 8']
 elif vid=='coordinate-rectangle-fourth-vertex':
  pts=[(-2,-3),(4,-3),(4,2),(-2,2)];d.line([xy(p) for p in pts[:3]],fill=TEAL,width=6)
  if scene>=2:d.line([xy(p) for p in [pts[2],pts[3],pts[0]]],fill=C,width=6)
  for p,l in zip(pts[:3],['A','B','C']):point(d,xy,p,l)
  if scene>=2:point(d,xy,pts[3],'D',offset=(-40,-30),color=C)
  lines=['Left: x = −2','Top: y = 2','D(−2, 2)']
 elif vid=='coordinate-parallelogram-fourth-vertex':
  pts=[(-2,1),(4,1),(7,6),(1,6)];d.line([xy(p) for p in pts[:3]],fill=TEAL,width=6)
  if scene>=2:d.line([xy(p) for p in [pts[2],pts[3],pts[0]]],fill=C,width=6)
  for p,l in zip(pts[:3],['A','B','C']):point(d,xy,p,l,offset=(12,8))
  if scene>=2:point(d,xy,pts[3],'D',offset=(-35,-30),color=C)
  lines=['B → C: (+3, +5)','A + (+3, +5)','D(1, 6)']
 card(d,lines)
def net(d,scene):
 d.rounded_rectangle((145,340,1775,920),radius=35,fill='white');a=65;t=a/math.sqrt(2);x=455;y=520
 for i in range(8):d.rectangle((260+i*a,y,260+(i+1)*a,y+100),fill='#E5F1ED',outline=TEAL,width=3)
 for sign,yy in [(-1,y),(1,y+100)]:
  pts=[(x,yy),(x+a,yy),(x+a+t,yy+sign*t),(x+a+t,yy+sign*(t+a)),(x+a,yy+sign*(2*t+a)),(x,yy+sign*(2*t+a)),(x-t,yy+sign*(t+a)),(x-t,yy+sign*t)]
  d.polygon(pts,fill='#FFEACD',outline=INK,width=3)
 text(d,(520,855),'2 octagons + 8 rectangles',37,INK,True,anchor='mm')
 card(d,['Octagonal prism','Faces: 2 + 8 = 10','Edges: 8 + 8 + 8 = 24','Vertices: 8 + 8 = 16'])
def pyramid(d,scene):
 d.rounded_rectangle((145,340,1775,920),radius=35,fill='white');pts=[(570+240*math.cos(2*math.pi*i/5-math.pi/2),740+95*math.sin(2*math.pi*i/5-math.pi/2)) for i in range(5)];ap=(570,390)
 d.polygon(pts,fill='#E5F1ED',outline=TEAL,width=4)
 for p in pts:d.line((*ap,*p),fill=INK,width=4);d.ellipse((p[0]-6,p[1]-6,p[0]+6,p[1]+6),fill=C)
 d.ellipse((ap[0]-7,ap[1]-7,ap[0]+7,ap[1]+7),fill=C)
 text(d,(560,860),'Pentagonal base: 5 sides',36,INK,True,anchor='mm');card(d,['1 base + 5 triangles','6 faces','5 base + 5 apex edges','10 edges; 6 vertices'])
def missingnet(d,scene):
 d.rounded_rectangle((145,340,1775,930),radius=35,fill='white');x=270;y=470;unit=14;h=140
 for i,a in enumerate([9,10,9,10]):
  xx=x+sum([9,10,9,10][:i])*unit;d.rectangle((xx,y,xx+a*unit,y+h),fill='#E5F1ED',outline=TEAL,width=4);text(d,(xx+a*unit/2,y+h/2),str(a) if i%2==0 or scene>=2 else 'w',40,INK,True,anchor='mm')
 x2=x+9*unit;d.rectangle((x2,y-9*unit,x2+10*unit,y),outline=TEAL,width=4);d.rectangle((x2,y+h,x2+10*unit,y+h+9*unit),outline=TEAL,width=4)
 d.line((x,y+h+170,x+38*unit,y+h+170),fill=INK,width=3);text(d,(x+19*unit,y+h+190),'38 cm total',36,INK,True,anchor='mt');text(d,(x-25,y+h/2),'14 cm',32,INK,True,anchor='rm')
 card(d,['9 + w + 9 + w = 38','w = (38 − 18)/2 = 10','Dimensions: 14, 9, 10'])
def lessons(doc):
 ls=make_lessons(SPECS,doc)
 for l in ls:
  vid=l['video_id'];old=v.DRAW[vid]
  if vid.startswith('coordinate-'):v.DRAW[vid]=lambda d,s,p,vid=vid,old=old:coords(vid,d,s) if s in [1,2,3] else old(d,s,p)
  if vid=='solid-prism-faces-edges-net':v.DRAW[vid]=lambda d,s,p,old=old:net(d,s) if s in [1,2,3] else old(d,s,p)
  if vid=='solid-pyramid-faces-edges':v.DRAW[vid]=lambda d,s,p,old=old:pyramid(d,s) if s in [1,2,3] else old(d,s,p)
  if vid=='solid-net-missing-dimension-area':v.DRAW[vid]=lambda d,s,p,old=old:missingnet(d,s) if s in [1,2] else old(d,s,p)
 return ls
