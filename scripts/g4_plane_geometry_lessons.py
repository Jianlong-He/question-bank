"""Elementary geometry diagrams with exact authored angles and counts."""
import json,math,itertools
from pathlib import Path
from card_lessons import make_lessons,draw_card
from early_measurement_lessons import card
import generate_sample_videos as v
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g4-u11-u13/lesson-specs.json').read_text())
def text(d,x,y,t,size=34,color=None):d.text((x,y),str(t),font=v.font(size,True),fill=color or v.INK,anchor='mm')
def dot(d,p,label,dy=38):
 x,y=p;d.ellipse((x-8,y-8,x+8,y+8),fill=v.INK);text(d,x,y+dy,label,30)
def arrow(d,a,b,color=None,width=5):
 color=color or v.TEAL;d.line((a,b),fill=color,width=width);x,y=b;ang=math.atan2(y-a[1],x-a[0]);d.polygon([b,(x-18*math.cos(ang-.45),y-18*math.sin(ang-.45)),(x-18*math.cos(ang+.45),y-18*math.sin(ang+.45))],fill=color)
def point(c,r,a):return(c[0]+r*math.cos(math.radians(a)),c[1]-r*math.sin(math.radians(a)))
def ray(d,c,r,a,color=None):arrow(d,c,point(c,r,a),color)
def arc(d,c,r,a,b,color=None):d.line([point(c,r,t) for t in range(round(a),round(b)+1)],fill=color or '#D28C25',width=5)
def angle(d,c,r,a,label=None):
 ray(d,c,r,0);ray(d,c,r,a);arc(d,c,60,0,a)
 if label:text(d,c[0]+r*.3,c[1]+45,label,36)
def protractor(d,c,r,a,show=False):
 for t in range(181):
  d.line((point(c,r-(18 if t%10==0 else 11 if t%5==0 else 5),t),point(c,r,t)),fill=v.INK,width=2)
  if t%10==0:
   x,y=point(c,r-44,t);text(d,x,y,t,22)
   x,y=point(c,r+24,t);text(d,x,y,180-t,21,'#7A7A7A')
 d.line((point(c,r,180),point(c,r,0)),fill=v.INK,width=3);angle(d,c,r+40,a)
 if show:text(d,c[0],c[1]+75,f'{a}° from the right-hand zero',34)
def triangle(d,c,lengths,scale=24):
 left,right,base=lengths;x=(left*left+base*base-right*right)/(2*base);h=math.sqrt(left*left-x*x)
 a=(c[0]-base*scale/2,c[1]+h*scale/2);b=(a[0]+base*scale,a[1]);top=(a[0]+x*scale,a[1]-h*scale)
 d.polygon([a,b,top],outline=v.TEAL,width=5)
 for p,q,n in [(a,b,base),(a,top,left),(b,top,right)]:text(d,(p[0]+q[0])/2,(p[1]+q[1])/2+(-25 if p!=a or q!=b else 30),str(n)+' cm',28)
def draw(s,d,i,p):
 vid=s['video_id']
 if i==4:draw_card(s,d,i,p);return
 card(d)
 if vid=='geometry-primitives-endpoints':
  for y,label in [(430,'Point'),(540,'Segment'),(650,'Ray'),(760,'Line')]:text(d,280,y,label)
  dot(d,(620,430),'P');d.line((620,540,1390,540),fill=v.TEAL,width=5);dot(d,(620,540),'J');dot(d,(1390,540),'K')
  arrow(d,(620,650),(1490,650));dot(d,(620,650),'U');dot(d,(1170,650),'V')
  arrow(d,(1000,760),(1490,760));arrow(d,(1000,760),(510,760));dot(d,(760,760),'R');dot(d,(1250,760),'S')
 elif vid=='geometry-ray-name-order':
  arrow(d,(550,510),(1470,510));dot(d,(550,510),'U');dot(d,(1170,510),'V');text(d,280,510,'Ray UV')
  arrow(d,(1170,710),(380,710));dot(d,(550,710),'U');dot(d,(1170,710),'V');text(d,1520,710,'Ray VU')
 elif vid=='geometry-count-point-pairs':
  pts=[point((960,595),205,90-k*72) for k in range(5)]
  for a,b in itertools.combinations(range(5),2):
   color=v.TEAL if i==0 or i==3 or (i==1 and a==0) or(i==2 and a in [1,2]) else '#D3D8D7';d.line((pts[a],pts[b]),fill=color,width=5)
  for k,z in enumerate(pts):
   x,y=point((960,595),242,90-k*72);dot(d,z,'',0);text(d,x,y,chr(65+k))
 elif vid=='geometry-segment-midpoint-length':
  d.line((430,560,1490,560),fill=v.TEAL,width=6)
  for x,l in [(430,'P'),(960,'N'),(1490,'Q')]:dot(d,(x,560),l)
  for x in [695,1225]:d.line((x-10,545,x+10,575),fill=v.INK,width=4)
  text(d,960,440,'PQ = 18 cm');text(d,695,670,'?' if i<2 else '9 cm');text(d,1225,670,'?' if i<2 else '9 cm');text(d,960,790,'N is the midpoint')
 elif vid=='geometry-angle-name-vertex':
  c=(780,730);ray(d,c,580,0);ray(d,c,400,65);arc(d,c,100,0,65);dot(d,c,'N');dot(d,point(c,330,65),'M',-35);dot(d,point(c,460,0),'P');text(d,1470,470,'MNP / NMP / MPN',32)
 elif vid=='geometry-angle-opening-compare':
  angle(d,(430,740),390,55,'A: 55°');angle(d,(1390,700),230,105,'B: 105°')
 elif vid=='geometry-parallel-perpendicular-pairs':
  for j,y in enumerate([460,585,710]):
   d.line((470,y,1450,y),fill=v.TEAL if i!=2 else '#B9C7C5',width=5);text(d,365,y,'H'+str(j+1),28)
  for j,x in enumerate([750,1150]):
   d.line((x,400,x,780),fill=v.TEAL if i!=1 else '#B9C7C5',width=5);text(d,x,825,'V'+str(j+1),28)
 elif vid=='geometry-perpendicular-parallel-transfer':
  for y,l in [(490,'L'),(710,'M')]:
   d.line((480,y,1470,y),fill=v.TEAL,width=6);text(d,360,y,l);d.line((960,y-30,990,y-30,990,y),fill=v.INK,width=4)
  d.line((960,390,960,800),fill=v.INK,width=5);text(d,960,835,'T');text(d,1100,450,'90°');text(d,1100,670,'?' if i<3 else '90°')
 elif vid=='geometry-triangle-side-length-types':
  for c,ls,l in [((430,605),(6,8,9),'A'),((960,605),(4,4,6),'B'),((1470,605),(5,5,5),'C')]:triangle(d,c,ls,29);text(d,c[0],790,l,38)
 elif vid=='geometry-protractor-read-scales':
  if i in [0,1]:protractor(d,(580,720),240,65);protractor(d,(1360,720),240,155);text(d,580,820,'A');text(d,1360,820,'B')
  else:protractor(d,(960,735),295,65 if i==2 else 155,True)
 elif vid=='geometry-reflex-protractor':
  c=(960,600);r=210
  for t in range(360):
   d.line((point(c,r-(15 if t%10==0 else 5),t),point(c,r,t)),fill=v.INK,width=2)
   if t%30==0:x,y=point(c,r+30,t);text(d,x,y,t,22)
  ray(d,c,r+65,0);ray(d,c,r+65,235);arc(d,c,80,0,235);text(d,1450,480,'counterclockwise',28)
  if i>=1:text(d,1460,620,'235° reflex',36)
  if i>=3:text(d,1460,710,'125° smaller',36)
 elif vid=='geometry-dial-clockwise-turn':
  c=(960,590);r=195;d.ellipse((765,395,1155,785),outline=v.INK,width=3)
  for k,l in enumerate('ABCDEFGH'):
   x,y=point(c,r+40,90-k*45);text(d,x,y,l,36)
  ray(d,c,r-20,0 if i<3 else -135);text(d,1480,450,'Start: C',34)
  if i>=2:text(d,1470,650,'3 clockwise gaps',30)
 elif vid=='geometry-adjacent-angle-parts':
  if i<3:
   c=(1050,730)
   for a,l in [(125,'K'),(77,'L'),(0,'P')]:ray(d,c,300,a);x,y=point(c,340,a);text(d,x,y,l,32)
   dot(d,c,'N');arc(d,c,80,77,125);arc(d,c,150,0,125);text(d,535,500,'Whole KNP: 125°',34);text(d,535,600,'Part KNL: 48°',34)
   if i==2:text(d,535,700,'LNP: 77°',34)
  else:
   c=(1140,750)
   for a in [0,35,82,110]:ray(d,c,300,a)
   for a,b,label in [(0,35,'35°'),(35,82,'47°'),(82,110,'28°')]:arc(d,c,90,a,b);x,y=point(c,160,(a+b)/2);text(d,x,y,label,28)
   text(d,550,570,'28° + 47° + 35°',38);text(d,550,660,'110° total',40)
 elif vid=='geometry-symmetry-rectangle-square':
  for x,w,h,l in [(560,420,252,'6 × 10 rectangle'),(1370,330,330,'7 × 7 square')]:
   y=600;d.rectangle((x-w/2,y-h/2,x+w/2,y+h/2),outline=v.TEAL,width=5);text(d,x,820,l,32)
   if i>=1:
    d.line((x,y-h/2-25,x,y+h/2+25),fill='#D28C25',width=4);d.line((x-w/2-25,y,x+w/2+25,y),fill='#D28C25',width=4)
   if (x==560 and i==2)or(x==1370 and i==3):
    color='#D95555' if x==560 else '#D28C25';d.line((x-w/2,y-h/2,x+w/2,y+h/2),fill=color,width=4);d.line((x-w/2,y+h/2,x+w/2,y-h/2),fill=color,width=4)
 else:draw_card(s,d,i,p)
def lessons(doc):
 result=make_lessons(SPECS,doc)
 for s in SPECS:v.DRAW[s['video_id']]=lambda d,i,p,s=s:draw(s,d,i,p)
 return result
