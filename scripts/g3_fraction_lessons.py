"""Verified introductory fraction models, comparisons and number lines."""
import json
from pathlib import Path
from card_lessons import make_lessons,draw_card
import generate_sample_videos as video
from early_measurement_lessons import card
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g3-u5-u6/lesson-specs.json').read_text())
def label(d,x,y,s,size=36):d.text((x,y),s,font=video.font(size,True),fill=video.INK,anchor='mm')
def bar(d,y,n,k,text,x=420,width=1160,height=70):
 label(d,300,y+height/2,text,36)
 for a in range(n):
  l=x+a*width/n;r=x+(a+1)*width/n
  d.rectangle((l,y,r,y+height),fill=video.TEAL if a<k else video.LIGHT,outline='white',width=3)
 d.rectangle((x,y,x+width,y+height),outline=video.INK,width=2)
def line(d,n,wholes,point,mid=False):
 x=330;y=610;width=1260
 d.line((x,y,x+width,y),fill=video.INK,width=4)
 for j in range(n*wholes+1):
  pos=x+width*j/(n*wholes);d.line((pos,y-16,pos,y+16),fill=video.INK,width=3)
  if j%n==0:label(d,pos,y+58,str(j//n),38)
 if point is not None:
  pos=x+width*point/(n*wholes);d.ellipse((pos-12,y-12,pos+12,y+12),fill=video.TEAL);label(d,pos,y-70,f'{point}/{n}',40)
 if mid:
  pos=x+width/2;d.ellipse((pos-10,y-10,pos+10,y+10),fill='#E9AA32');label(d,pos,y+108,'6/12 = 1/2',32)
def draw(s,d,i,p):
 draw_card(s,d,i,p);vid=s['video_id']
 if i==0:return
 if vid=='fraction-read-parts-early':
  card(d);bar(d,555,11,6,'6/11');label(d,960,460,'One whole strip: 11 equal parts',40)
  label(d,960,730,['','Count equal parts of one whole.','Numerator 6: shaded parts','Denominator 11: all equal parts','6 shaded + 5 unshaded = 11'][i],40)
 elif vid=='fraction-remaining-parts-early' and i in [2,3]:
  card(d)
  for j in range(20):
   x=360+j*60;d.rectangle((x,530,x+60,620),fill='#CB684F' if j<9 else video.TEAL,outline='white',width=3)
  label(d,960,450,'One whole cake: 20 equal pieces',40)
  label(d,960,715,'Eaten: 5 + 4 = 9 pieces = 9/20',40)
  label(d,960,780,'Remaining: 20 − 9 = 11 pieces = 11/20',40)
 elif vid=='fraction-half-benchmark-early' and i in [1,2,3]:
  card(d);bar(d,475,14,5,'5/14');bar(d,650,13,8,'8/13')
  x=1000
  for y in range(425,755,20):d.line((x,y,x,y+12),fill='#C16D35',width=4)
  label(d,x,795,'1/2 of each equal-sized whole',32)
 elif vid=='fraction-same-denominator-early':
  card(d)
  for y,k in zip([435,565,695],[2,7,9]):bar(d,y,13,k,f'{k}/13')
 elif vid=='fraction-same-numerator-early':
  card(d)
  for y,n in zip([435,565,695],[13,10,6]):bar(d,y,n,4,f'4/{n}')
 elif vid=='fraction-equivalent-bars-early':
  card(d)
  for j,(n,k) in enumerate([(5,2),(15,6),(20,8)][:min(i,3)]):bar(d,435+130*j,n,k,f'{k}/{n}')
  if i==1:label(d,960,675,'Two fifths of one whole bar',42)
 elif vid=='fraction-line-to-one-early':
  card(d);line(d,12,1,5 if i>1 else None,i==3)
  label(d,960,440,'12 equal spaces from 0 to 1',40)
  label(d,960,795,{1:'Each space is 1/12',2:'Five jumps from 0 reach 5/12',3:'Half of twelve spaces is six',4:'12 − 5 = 7 more jumps to 1'}[i],38)
 elif vid=='fraction-line-beyond-one-early':
  card(d);line(d,5,3,13 if i>1 else None)
  label(d,960,440,'1 = 5/5; 2 = 10/5; 3 = 15/5',40)
  label(d,960,785,{1:'Each space is 1/5',2:'2 < 13/5 < 3',3:'Gap to 2: 3/5; gap to 3: 2/5',4:'13/5 + 2/5 = 15/5 = 3'}[i],40)
 elif vid=='fraction-same-part-different-wholes':
  card(d);bar(d,465,3,2,'A: 9 cm',width=696);bar(d,635,3,2,'B: 15 cm',width=1160)
  label(d,960,790,'Shaded lengths: 6 cm and 10 cm',40)
 elif vid=='fraction-count-parts-several-wholes':
  card(d)
  for j in range(3):
   x=300+j*470
   for k in range(5):d.rectangle((x+k*80,500,x+(k+1)*80,650),fill=video.TEAL,outline='white',width=3)
   label(d,x+200,705,'1 card = 5 fifths',31)
  label(d,960,785,'3 cards × 5 fifths per card = 15 fifths',38)
 elif vid=='fraction-compare-one-early' and i in [1,2,3]:
  card(d);k={1:10,2:8,3:13}[i]
  for j in range(15):
   x=330+j*84;d.rectangle((x,530,x+84,620),fill=video.TEAL if j<k else video.LIGHT,outline='white',width=3)
  d.rectangle((330,530,1170,620),outline=video.INK,width=5)
  label(d,750,710,'One whole: 10 tenths',36)
  label(d,960,440,{1:'10/10 = 1',2:'8/10 < 1',3:'13/10 > 1'}[i],48)
def lessons(doc):
 result=make_lessons(SPECS,doc)
 for s in SPECS:video.DRAW[s['video_id']]=lambda d,i,p,s=s:draw(s,d,i,p)
 return result
