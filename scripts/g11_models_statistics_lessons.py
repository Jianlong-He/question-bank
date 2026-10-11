import json,math
from pathlib import Path
from card_lessons import make_lessons,draw_card
import generate_sample_videos as v
from generate_sample_videos import text,TEAL,INK
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g11-u9-u12/lesson-specs.json').read_text())
BROWN='#b76d36';GRAY='#aab5b7'
def draw(s,d,scene,p):
 vid=s['video_id'];custom={'statistics-population-random-sampling','statistics-randomized-controlled-study','probability-binomial-distribution-bars','function-periodic-model-test','model-average-cost-limit','model-linear-axis-scale','model-parallel-resistance'}
 if scene in [0,4] or vid not in custom:return draw_card(s,d,scene,p)
 d.rounded_rectangle((145,350,1775,850),radius=35,fill='white')
 def lab(X,Y,t,size=26,col=INK):text(d,(X,Y),t,size,col)
 def ln(points,col=TEAL,width=4):d.line(points,fill=col,width=width)
 if vid=='statistics-population-random-sampling':
  d.rounded_rectangle((235,450,800,760),radius=20,outline=TEAL,width=4);lab(265,473,'Population: 2400 cardholders',27)
  d.rounded_rectangle((320,555,710,695),radius=18,fill='#e0f0eb');lab(365,575,'Random sample: 120',25);lab(430,630,'5% of 2400',25)
  lab(250,790,'Subset drawn from the full list',25)
 elif vid=='statistics-randomized-controlled-study':
  lab(345,420,'40 seedlings',30);ln([(500,470),(500,530)]);ln([(310,530),(700,530)]);ln([(310,530),(310,600)]);ln([(700,530),(700,600)])
  for X,title in [(220,'20 treated'),(595,'20 controls')]:d.rounded_rectangle((X,605,X+235,690),radius=15,outline=TEAL,width=3);lab(X+18,630,title,27)
  lab(340,540,'Random assignment',22);lab(295,735,'Similar water and light',27)
 elif vid=='probability-binomial-distribution-bars':
  xy=lambda k,y:(300+k*130,775-y*650);ln([(240,450),(240,775),(800,775)],GRAY,3)
  for k,a in enumerate([.064,.288,.432,.216]):
   X,Y=xy(k,a);d.rectangle((X-35,Y,X+35,775),fill=TEAL);lab(X-30,Y-38,f'{a:.3f}',24);lab(X-8,790,str(k),25)
  for a in [.1,.2,.3,.4]:lab(175,765-a*650,f'{a:.1f}',22)
  lab(235,408,'Probability',27);lab(360,824,'Success count k',22)
 elif vid=='function-periodic-model-test':
  if scene<3:
   xy=lambda t,y:(240+t/28*550,610-y*125)
   ln([xy(0,0),xy(28,0)],GRAY,2)
   ln([xy(j/20,math.cos(math.pi*(j/20)/7)) for j in range(561)])
   for t in [0,7,14,21,28]:X,Y=xy(t,0);ln([(X,602),(X,618)],GRAY,2);lab(X-12,765,str(t),23)
   lab(245,412,'A(t)=cos(πt/7)',28);lab(320,808,'t in input units; period 14',24)
  else:
   xy=lambda t,y:(240+t/2*500,780-y/20*300);ln([xy(0,20),xy(0,0),xy(2.1,0)],GRAY,2);ln([xy(j/100,(j/100)**4+2) for j in range(201)])
   lab(250,430,'B(t)=t⁴+2',28);lab(270,730,'B(0)=2',25);lab(585,473,'B(2)=18',25);lab(280,808,'No positive shift repeats B(0)',24)
 elif vid=='model-average-cost-limit':
  xy=lambda n,a:(245+n/210*550,780-(a-5)/21*310)
  ln([xy(0,26),xy(0,5),xy(210,5)],GRAY,2);ln([xy(0,6),xy(210,6)],BROWN,3);ln([xy(n,6+210/n) for n in range(11,211)])
  for n in [35,70,140]:
   a=6+210/n;X,Y=xy(n,a);d.ellipse((X-5,Y-5,X+5,Y+5),fill=INK);lab(X+8,Y-20,f'({n},{a:g})',23)
  lab(250,408,'A(n)=6+210/n',28);lab(540,782,'Limit: $6/item',23,BROWN);lab(245,820,'n: items; A: dollars per item',24)
 elif vid=='model-linear-axis-scale':
  ln([(235,630),(835,630)],GRAY,3)
  for j in range(7):
   X=245+j*95;ln([(X,615),(X,645)],TEAL,4)
   if scene>=2:lab(X-10,665,str(3*j),28)
  lab(330,465,'6 equal spaces',32);lab(315,740,'Time (minutes)',29)
 elif vid=='model-parallel-resistance':
  # Parallel paths share both connection nodes.
  ln([(260,610),(350,610),(350,500),(440,500)]);ln([(350,610),(350,720),(440,720)])
  ln([(630,500),(725,500),(725,610),(815,610)]);ln([(630,720),(725,720),(725,610)])
  for Y,label in [(500,'9 Ω'),(720,'18 Ω')]:d.rectangle((440,Y-25,630,Y+25),outline=TEAL,width=4);lab(500,Y-58,label,29)
  for X in [350,725]:d.ellipse((X-7,603,X+7,617),fill=INK)
  lab(275,408,'Two branches in parallel',28)
 for j,line in enumerate(s['displays'][scene].split('\n')):lab(920,505+j*78,line,29 if len(line)<50 else 26,TEAL if j==0 else INK)
def lessons(doc):
 out=make_lessons(SPECS,doc)
 for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:draw(s,d,scene,p)
 return out
