import json,math
from pathlib import Path
from card_lessons import make_lessons,draw_card
import generate_sample_videos as v
from generate_sample_videos import text,TEAL,INK,font
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g10-u7-u9/lesson-specs.json').read_text())
BROWN='#b76d36';GRAY='#aab5b7'
def draw(s,d,scene,p):
 vid=s['video_id']
 if scene in [0,4] or vid.startswith('exponential-') or vid=='scale-drawing-corresponding-units':return draw_card(s,d,scene,p)
 d.rounded_rectangle((145,350,1775,850),radius=35,fill='white')
 def line(pts,color=TEAL,width=4):d.line(pts,fill=color,width=width)
 def label(pt,val,dx=0,dy=0):text(d,(pt[0]+dx,pt[1]+dy),val,25,INK)
 def poly(pts,color=TEAL):line(pts+[pts[0]],color)
 def fit(points,box):
  xs=[p[0] for p in points];ys=[p[1] for p in points];sc=min((box[2]-box[0])/(max(xs)-min(xs)),(box[3]-box[1])/(max(ys)-min(ys)))
  return [(box[0]+(x-min(xs))*sc,box[3]-(y-min(ys))*sc) for x,y in points]
 def right(pt):line([(pt[0],pt[1]-15),(pt[0]-15,pt[1]-15),(pt[0]-15,pt[1])],GRAY,2)
 if vid in ['geometry-triangle-aa-similarity','geometry-triangle-sss-similarity','geometry-similar-corresponding-length']:
  if vid=='geometry-triangle-aa-similarity':
   cx=math.tan(math.radians(68))/(math.tan(math.radians(42))+math.tan(math.radians(68)));pts=[(0,0),(1,0),(cx,cx*math.tan(math.radians(42)))];labs1=['42°','68°','70°'];labs2=labs1
  elif vid=='geometry-triangle-sss-similarity':pts=[(0,0),(11,0),((7**2+11**2-8**2)/22,math.sqrt(7**2-((7**2+11**2-8**2)/22)**2))];labs1=['7','8','11'];labs2=['14','16','22']
  else:pts=[(0,0),(8,0),(1.25,math.sqrt(100-1.25**2))];labs1=['10','12','8'];labs2=['17.5','21','14']
  for j,box in enumerate([(230,460,455,745),(515,410,790,745)]):
   P=fit(pts,box);poly(P,TEAL if j==0 else BROWN)
   if vid=='geometry-triangle-aa-similarity':
    for z,lab,off in zip(P,labs1,[(-15,12),(-10,12),(-5,-35)]):label(z,lab,*off)
   else:
    for aa,bb,lab,off in [(P[0],P[2],(labs1 if j==0 else labs2)[0],(-40,0)),(P[1],P[2],(labs1 if j==0 else labs2)[1],(12,0)),(P[0],P[1],(labs1 if j==0 else labs2)[2],(-10,15))]:label(((aa[0]+bb[0])/2,(aa[1]+bb[1])/2),lab,*off)
  label((245,810),'Corresponding triangles; separate drawing scales')
 elif vid in ['geometry-triangle-midsegment','geometry-triangle-parallel-side-splitter']:
  mid=vid.endswith('midsegment');A=(6,16) if mid else (7.5,math.sqrt(225-7.5**2));B=(0,0);C=(26,0) if mid else (24,0);f=.5 if mid else 1/3
  D=tuple(A[i]+f*(B[i]-A[i]) for i in range(2));E=tuple(A[i]+f*(C[i]-A[i]) for i in range(2));P=fit([A,B,C,D,E],(270,450,745,750));A,B,C,D,E=P;poly([A,B,C]);line([D,E],BROWN)
  for pt,name,offset in [(A,'A',(-10,-35)),(B,'B',(-25,10)),(C,'C',(10,10)),(D,'D',(-30,-10)),(E,'E',(15,-10))]:label(pt,name,*offset)
  if mid:
   label(((D[0]+E[0])/2,D[1]),'13',-10,-35);label(((B[0]+C[0])/2,B[1]),'26',-10,15);label((300,810),'D and E are midpoints; DE parallel to BC')
  else:
   for X,Y,val,dx in [(A,D,'5',-35),(D,B,'10',-40),(A,E,'7',15),(E,C,'14',15)]:label(((X[0]+Y[0])/2,(X[1]+Y[1])/2),val,dx,0)
   label((350,810),'DE parallel to BC')
 elif vid=='geometry-regular-hexagon-six-triangles':
  cx,cy,r=510,615,180;P=[(cx+r*math.cos(j*math.pi/3),cy-r*math.sin(j*math.pi/3)) for j in range(6)];poly(P)
  for pt in P:line([(cx,cy),pt],GRAY,2)
  # Rightmost triangular sector uses vertices at angles -60 and 0.
  V=P[5];W=P[0];M=((V[0]+W[0])/2,(V[1]+W[1])/2);line([(cx,cy),M],BROWN,4)
  label((565,590),'6',0,-10);label((660,680),'6');label((415,555),'60°');label((350,825),'Six equilateral triangles; altitude = 3√3')
 elif vid in ['linear-slope-similar-triangles','linear-parallel-equal-slopes']:
  parallel='parallel' in vid
  def xy(x,y):return(285+x*25,720-y*25)
  line([xy(-1,0),xy(18,0)],GRAY,2);line([xy(0,-4.5),xy(0,11)],GRAY,2)
  if parallel:
   for b,col in [(2,TEAL),(-4,BROWN)]:line([xy(0,b),xy(15,9+b)],col);label(xy(0,b),str(b),-28,-10)
   label((435,435),'Both slopes = 3/5');label(xy(10,8),'y = (3/5)x + 2',-70,-38);label(xy(11,2.6),'y = (3/5)x − 4',-75,20)
  else:
   line([xy(0,0),xy(16,32/3)]);line([xy(0,0),xy(6,0),xy(6,4)],BROWN,3);line([xy(0,0),xy(15,0),xy(15,10)],GRAY,3)
   label(xy(3,0),'6',0,12);label(xy(6,2),'4',10,0);label(xy(15,5),'10',12,0);label(xy(7.5,-2),'Whole run = 15',-60,0);right(xy(6,0));right(xy(15,0))
 elif vid=='geometry-similar-shadow-height':
  for X,Y,run,rise,col in [(245,745,80,50,TEAL),(425,745,336,210,BROWN)]:
   poly([(X,Y),(X,Y-rise),(X+run,Y)],col);label((X+run/2,Y),'4 m' if run==80 else '28 m',-20,15);label((X,Y-rise/2),'2.5 m' if run==80 else '17.5 m',-65,-8)
  label((260,815),'Same sun angle; upright objects; level ground')
 elif vid=='trigonometry-rise-from-ramp-length':
  x,y=275,750;run=440;rise=run*math.tan(math.radians(25));poly([(x,y),(x+run,y),(x+run,y-rise)]);right((x+run,y));label((x+110,y-50),'25°');label((x+225,y-rise/2),'16 m',-15,-40);label((x+run,y-rise/2),'rise',20,0);label((360,810),'Horizontal run is not the ramp length')
 for j,t in enumerate(s['displays'][scene].split('\n')):
  size=38
  while d.textlength(t,font=font(size))>850:size-=1
  text(d,(865,475+j*80),t,size,TEAL)
def lessons(doc):
 out=make_lessons(SPECS,doc)
 for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:draw(s,d,scene,p)
 return out
