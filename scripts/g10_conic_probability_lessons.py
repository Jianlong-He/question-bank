import json,math
from pathlib import Path
from card_lessons import make_lessons,draw_card
import generate_sample_videos as v
from generate_sample_videos import text,TEAL,INK,font
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g10-u12-u13/lesson-specs.json').read_text())
BROWN='#b76d36';GRAY='#aab5b7'
def draw(s,d,scene,p):
 vid=s['video_id'];custom={'conics-nondegenerate-sections','geometry-circle-build-equation','conics-parabola-focus-directrix-locus','conics-parabola-signed-focus-form','probability-venn-disjoint-regions','probability-disjoint-positive-dependent'}
 if scene in [0,4] or vid not in custom:return draw_card(s,d,scene,p)
 d.rounded_rectangle((145,350,1775,850),radius=35,fill='white')
 def ln(pts,col=TEAL,w=4):d.line(pts,fill=col,width=w)
 def lab(x,y,t,size=27,col=INK):text(d,(x,y),t,size,col)
 def dot(P,t,dx=10,dy=-27):d.ellipse((P[0]-5,P[1]-5,P[0]+5,P[1]+5),fill=INK);lab(P[0]+dx,P[1]+dy,t)
 if vid=='conics-nondegenerate-sections':
  if scene==1:
   d.ellipse((245,480,455,690),outline=TEAL,width=4);d.ellipse((510,530,790,670),outline=BROWN,width=4);lab(300,725,'Circle');lab(590,725,'Ellipse');lab(250,430,'r = 3');lab(520,470,'Semiaxes 4 and 2')
  elif scene==2:
   xy=lambda x,y:(500+x*50,770-y*50);ln([xy(-5,0),xy(5,0)],GRAY,2);ln([xy(0,-.4),xy(0,6.5)],GRAY,2);ln([xy(-4.8+j*9.6/200,(-4.8+j*9.6/200)**2/4) for j in range(201)]);lab(560,720,'y = x²/4');lab(350,810,'Parabola: one open branch')
  else:
   xy=lambda x,y:(500+x*40,610-y*40);ln([xy(-7,0),xy(7,0)],GRAY,2);ln([xy(0,-4.5),xy(0,4.5)],GRAY,2)
   for sign in [-1,1]:ln([xy(sign*3*math.cosh(-1.3+j*2.6/200),2*math.sinh(-1.3+j*2.6/200)) for j in range(201)])
   lab(305,810,'Hyperbola: two branches');lab(320,425,'x²/9 − y²/4 = 1')
 elif vid=='geometry-circle-build-equation':
  C=(500,600);R=150;d.ellipse((350,450,650,750),outline=TEAL,width=4);ln([C,(650,600)],BROWN,3);dot(C,'(−5, 2)',-60,20);dot((650,600),'(1, 2)',10,-30);lab(552,560,'6');lab(325,810,'All boundary points are 6 units from center.',23)
 elif vid=='conics-parabola-focus-directrix-locus':
  xy=lambda x,y:(500+x*25,630-y*25)
  ln([xy(-10,-4),xy(10,-4)],BROWN,3);ln([xy(0,-5),xy(0,7)],GRAY,2)
  ln([xy(-9+j*18/200,(-9+j*18/200)**2/16) for j in range(201)])
  F=xy(0,4);V=xy(0,0);P=xy(8,4);Q=xy(8,-4)
  ln([F,P,Q],GRAY,3);dot(F,'F(0, 4)',-115,-35);dot(V,'V(0, 0)',-130,10);dot(P,'P(8, 4)',10,-30);lab(585,490,'8');lab(713,620,'8');lab(270,750,'Directrix y = −4');ln([xy(7.6,-4),xy(7.6,-3.6),xy(8,-3.6)],GRAY,2)
 elif vid=='conics-parabola-signed-focus-form':
  xy=lambda x,y:(500+(x-2)*25,480-y*25)
  ln([xy(-8,1),xy(12,1)],BROWN,3);ln([xy(2,-10),xy(2,3)],GRAY,2)
  ln([xy(-7+j*18/200,-3-((-7+j*18/200)-2)**2/16) for j in range(201)])
  dot(xy(2,-3),'V(2, −3)',15,-30);dot(xy(2,-7),'F(2, −7)',15,15);lab(265,407,'Directrix y = 1');ln([xy(2,1),xy(2,-7)],GRAY,3);lab(470,492,'4');lab(470,590,'4');lab(325,810,'p = −4; opens toward the focus')
 elif vid=='probability-venn-disjoint-regions':
  d.rectangle((220,420,815,825),outline=GRAY,width=3)
  d.ellipse((265,470,545,750),fill='#edf6f4',outline=TEAL,width=3);d.ellipse((475,470,755,750),outline=BROWN,width=3)
  lab(350,430,'A');lab(660,430,'B');lab(345,600,'7',36);lab(495,600,'9',36);lab(655,600,'14',36);lab(710,765,'20',32);lab(240,777,'Total = 50',25)
  lab(315,365,'Disjoint region counts',29)
 elif vid=='probability-disjoint-positive-dependent':
  d.ellipse((225,485,475,735),outline=TEAL,width=4);d.ellipse((545,485,795,735),outline=BROWN,width=4);lab(315,435,'A');lab(640,435,'B');lab(265,600,'1, 2, 3, 4',30);lab(600,600,'5, 6, 7',30);lab(350,795,'Outside: 8, 9, 10',27)
 for j,t in enumerate(s['displays'][scene].split('\n')):
  size=38
  while d.textlength(t,font=font(size))>850:size-=1
  text(d,(865,465+j*80),t,size,TEAL)
def lessons(doc):
 out=make_lessons(SPECS,doc)
 for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:draw(s,d,scene,p)
 return out
