import json,math
from pathlib import Path
from card_lessons import make_lessons,draw_card
import generate_sample_videos as v
from generate_sample_videos import text,TEAL,INK,MUTED,font
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g9-u7-u8/lesson-specs.json').read_text())
def clip(poly,a,b,c):
 """Intersect a polygon with a*x+b*y+c >= 0."""
 out=[]
 for p,q in zip(poly,poly[1:]+poly[:1]):
  fp=a*p[0]+b*p[1]+c;fq=a*q[0]+b*q[1]+c
  if fp>=0:out.append(p)
  if (fp>=0)!=(fq>=0):
   t=fp/(fp-fq);out.append((p[0]+t*(q[0]-p[0]),p[1]+t*(q[1]-p[1])))
 return out

def graph(s,d,scene,p):
 vid=s['video_id'];eligible=vid in ['inequality-plane-boundary-shading','inequality-system-intersection','inequality-test-origin','inequality-nonnegative-region','function-local-absolute-extrema']
 if not eligible or scene in [0,4]:return draw_card(s,d,scene,p)
 d.rounded_rectangle((145,350,1775,850),radius=35,fill='white')
 if vid=='function-local-absolute-extrema':
  pt=lambda x,y:(300+x*54,790-y*38)
  for x in range(0,9,2):d.line([pt(x,0),pt(x,10)],fill='#e2e8e5',width=1);text(d,(pt(x,0)[0],809),str(x),23,MUTED,anchor='mt')
  for y in range(0,11,2):d.line([pt(0,y),pt(8,y)],fill='#e2e8e5',width=1);text(d,(275,pt(0,y)[1]),str(y),23,MUTED,anchor='rm')
  d.line([pt(0,0),pt(8,0)],fill=INK,width=3);d.line([pt(0,0),pt(0,10)],fill=INK,width=3)
  points=[(0,1),(2,6),(4,2),(6,9),(8,3)];d.line([pt(*z) for z in points],fill=TEAL,width=6)
  for z in points:
   xx,yy=pt(*z);d.ellipse((xx-6,yy-6,xx+6,yy+6),fill=TEAL)
  chosen=points[{1:1,2:2,3:3}[scene]];xx,yy=pt(*chosen);d.ellipse((xx-10,yy-10,xx+10,yy+10),fill='#bd5736');text(d,(xx+15,yy-25),str(chosen),28,INK)
  text(d,(pt(8,0)[0]+18,pt(8,0)[1]),'x',26,INK);text(d,(pt(0,10)[0],pt(0,10)[1]-25),'y',26,INK)
 else:
  pt=lambda x,y:(540+x*39,605-y*39);box=[(-5,-5),(-5,5),(5,5),(5,-5)];lines=[];poly=box;dot=None
  if vid=='inequality-plane-boundary-shading':
   if scene==1:poly=[];lines=[(1,-1,False,TEAL),(-1,2,True,'#b76d36')]
   elif scene==2:poly=clip(poly,-1,1,1);lines=[(1,-1,False,TEAL)]
   else:poly=clip(poly,-1,-1,2);lines=[(-1,2,True,TEAL)]
  elif vid=='inequality-system-intersection':
   poly=clip(poly,-1,1,1);lines=[(1,-1,False,TEAL)]
   if scene>=2:poly=clip(poly,-1,-1,5);lines.append((-1,5,True,'#b76d36'))
   if scene==3:dot=(-1,4)
  elif vid=='inequality-test-origin':poly=clip(poly,-2,-1,4) if scene==3 else [];lines=[(-2,4,True,TEAL)];dot=(0,0)
  elif vid=='inequality-nonnegative-region':
   poly=clip(poly,1,0,0)
   if scene==2:poly=clip(box,0,1,0)
   if scene==3:poly=clip(poly,0,1,0)
  if poly:d.polygon([pt(*z) for z in poly],fill='#d7eee7')
  for k in range(-5,6):d.line([pt(k,-5),pt(k,5)],fill='#e1e7e4',width=1);d.line([pt(-5,k),pt(5,k)],fill='#e1e7e4',width=1)
  d.line([pt(-5,0),pt(5,0)],fill=INK,width=3);d.line([pt(0,-5),pt(0,5)],fill=INK,width=3)
  for k in [-4,-2,0,2,4]:text(d,(pt(k,0)[0],pt(k,0)[1]+9),str(k),21,MUTED,anchor='mt')
  for k in [-4,-2,2,4]:text(d,(pt(0,k)[0]-9,pt(0,k)[1]),str(k),21,MUTED,anchor='rm')
  for m,b,dash,color in lines:
   ps=[(xx,m*xx+b) for xx in [-5,5] if -5<=m*xx+b<=5]
   if m:ps += [((yy-b)/m,yy) for yy in [-5,5] if -5<=(yy-b)/m<=5]
   ps=sorted(set(ps));a,z=pt(*ps[0]),pt(*ps[-1])
   if dash:
    length=math.dist(a,z);n=max(1,int(length/14))
    for j in range(0,n,2):
     t0=j/n;t1=min((j+1)/n,1);d.line([(a[0]+(z[0]-a[0])*t0,a[1]+(z[1]-a[1])*t0),(a[0]+(z[0]-a[0])*t1,a[1]+(z[1]-a[1])*t1)],fill=color,width=5)
   else:d.line([a,z],fill=color,width=5)
  if dot:
   a,b=pt(*dot);d.ellipse((a-7,b-7,a+7,b+7),fill='#bd5736');text(d,(a+12,b-28),str(dot),26,INK)
  text(d,(760,605),'x',27,INK);text(d,(548,380),'y',27,INK)
 for j,line in enumerate(s['displays'][scene].split('\n')):
  size=40
  while d.textlength(line,font=font(size))>850:size-=1
  text(d,(870,510+j*85),line,size,TEAL)

def lessons(doc):
 out=make_lessons(SPECS,doc)
 for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:graph(s,d,scene,p)
 return out
