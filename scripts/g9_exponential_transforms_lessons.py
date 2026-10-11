import json,math
from pathlib import Path
from card_lessons import make_lessons,draw_card
import generate_sample_videos as v
from generate_sample_videos import text,TEAL,INK,MUTED,font
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g9-u14-u15/lesson-specs.json').read_text())
def draw(s,d,scene,p):
 vid=s['video_id']
 if vid not in ['exponential-graph-growth-decay','exponential-sign-reflection','geometry-rotation-same-center-composition'] or scene in [0,4]:return draw_card(s,d,scene,p)
 d.rounded_rectangle((145,350,1775,850),radius=35,fill='white');brown='#b76d36'
 if vid=='geometry-rotation-same-center-composition':
  cx,cy=495,650;radius=180
  def pt(angle,r=radius):return (cx+r*math.cos(math.radians(angle)),cy-r*math.sin(math.radians(angle)))
  d.ellipse((cx-5,cy-5,cx+5,cy+5),fill=INK);text(d,(cx+7,cy+14),'O',25,INK)
  angles=[0]+([60] if scene>=2 else [])+([180] if scene>=3 else [])
  for a in angles:
   end=pt(a);d.line([(cx,cy),end],fill=TEAL if a!=60 else brown,width=4);d.ellipse((end[0]-6,end[1]-6,end[0]+6,end[1]+6),fill=TEAL);text(d,(end[0]+10,end[1]-22),{0:'Start',60:'After 60°',180:'After 180°'}[a],24,INK)
  for lo,hi,r,color in [(0,60,95,brown),(60,180,120,TEAL)][:max(0,scene-1)]:
   ps=[pt(lo+(hi-lo)*i/80,r) for i in range(81)];d.line(ps,fill=color,width=4)
   tip=ps[-1];prev=ps[-5];ang=math.atan2(tip[1]-prev[1],tip[0]-prev[0]);d.polygon([tip,(tip[0]-13*math.cos(ang-.5),tip[1]-13*math.sin(ang-.5)),(tip[0]-13*math.cos(ang+.5),tip[1]-13*math.sin(ang+.5))],fill=color)
   mid=pt((lo+hi)/2,r+22);text(d,mid,str(hi-lo)+'°',23,color,anchor='mm')
 else:
  signed=vid=='exponential-sign-reflection';xmin,xmax=(-1,1.5) if signed else (-2,2);ymin,ymax=(-42,42) if signed else (0,17)
  pt=lambda x,y:(260+(x-xmin)/(xmax-xmin)*500,800-(y-ymin)/(ymax-ymin)*420)
  xticks=[-1,0,1] if signed else [-2,-1,0,1,2];yticks=[-40,-20,0,20,40] if signed else [0,1,4,8,12,16]
  for xx in xticks:
   d.line([pt(xx,ymin),pt(xx,ymax)],fill='#e2e8e5',width=1);text(d,(pt(xx,0)[0],pt(xx,0)[1]+12),str(xx),21,MUTED,anchor='mt')
  for yy in yticks:
   d.line([pt(xmin,yy),pt(xmax,yy)],fill='#e2e8e5',width=1);text(d,(240,pt(0,yy)[1]),str(yy),21,MUTED,anchor='rm')
  d.line([pt(xmin,0),pt(xmax,0)],fill=INK,width=3);d.line([pt(0,ymin),pt(0,ymax)],fill=INK,width=3)
  fs=[(lambda x:5*4**x,TEAL,'f(x) = 5 × 4^x'),(lambda x:-5*4**x,brown,'h(x) = −5 × 4^x')] if signed else [(lambda x:4**x,TEAL,'f(x) = 4^x'),(lambda x:4**(-x),brown,'g(x) = (1/4)^x')]
  for j,(fn,color,label) in enumerate(fs):
   points=[pt(xmin+(xmax-xmin)*i/250,fn(xmin+(xmax-xmin)*i/250)) for i in range(251)];d.line(points,fill=color,width=5);text(d,(265,370+j*30),label,24,color)
  text(d,(780,pt(0,0)[1]),'x',24,INK)
 for j,line in enumerate(s['displays'][scene].split('\n')):
  size=38
  while d.textlength(line,font=font(size))>855:size-=1
  text(d,(860,525+j*80),line,size,TEAL)
def lessons(doc):
 out=make_lessons(SPECS,doc)
 for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:draw(s,d,scene,p)
 return out
