"""Checked Grade 2 Units 6-8 diagrams and analogous examples."""
import json,math
from pathlib import Path
from card_lessons import make_lessons,draw_card
import generate_sample_videos as video
from early_measurement_lessons import card,clock
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g2-u6-u8/lesson-specs.json').read_text())
def label(d,x,y,s,size=34,color=None):
 d.text((x,y),s,font=video.font(size,True),fill=color or video.INK,anchor='mm')
def strip(d,x,y,w,color):d.rounded_rectangle((x,y,x+w,y+55),radius=8,fill=color)
def picture(d,names,counts,key,unit):
 card(d);label(d,960,395,f'Key: 1 square = {key} {unit}',32)
 for j,(name,n) in enumerate(zip(names,counts)):
  y=475+j*120;label(d,400,y+24,name)
  for i in range(n):d.rectangle((630+i*115,y,680+i*115,y+50),fill=video.TEAL,outline=video.INK,width=2)
 label(d,960,810,'Count the data symbols; exclude the key.',27)
def plot(d,selected=()):
 card(d);label(d,960,390,'Badges owned by students — each dot is 1 student',30)
 d.line((430,745,1490,745),fill=video.INK,width=4)
 for i,n in enumerate([1,3,5,4,2]):
  x=510+220*i;d.line((x,730,x,760),fill=video.INK,width=4);label(d,x,790,str(i+1))
  for j in range(n):
   y=695-j*52;d.ellipse((x-17,y-17,x+17,y+17),fill='#DC8B34' if i+1 in selected else video.TEAL)
 label(d,960,835,'Number of badges',27)
def grid(d,x,y,rows,cols,size=62,unequal=False):
 widths=[.6,1.4,.8,1.2] if unequal else [1]*cols
 bounds=[x]
 for width in widths:bounds.append(bounds[-1]+size*width)
 for r in range(rows):
  for c in range(cols):d.rectangle((bounds[c],y+r*size,bounds[c+1],y+(r+1)*size),fill='#D6ECE7',outline=video.INK,width=3)
def draw(s,d,i,p):
 draw_card(s,d,i,p);vid=s['video_id']
 if vid=='measure-read-zero-ruler' and i<4:
  card(d);x=430;step=125;strip(d,x,475,6*step,video.TEAL)
  d.rectangle((x-20,570,x+8*step+25,710),fill='#F5DE9F',outline=video.INK,width=3)
  for k in range(9):
   xx=x+k*step;d.line((xx,570,xx,630),fill=video.INK,width=4);label(d,xx,670,str(k),31)
  label(d,960,765,['Read the strip length in centimeters.','Start at 0 cm.','The far end is at 6 cm.','Count 6 equal intervals.'][i],36)
 if vid=='measure-unit-size-count' and i<4:
  card(d)
  for row,(n,color) in enumerate([(6,'#4279BD'),(3,'#DC8B34')]):
   for k in range(n):d.rectangle((510+k*150*(6/n),465+row*155,510+(k+1)*150*(6/n),550+row*155),fill=color,outline='white',width=5)
   label(d,345,505+row*155,'Blue' if row==0 else 'Orange',32)
  label(d,960,790,'The same ribbon length: 6 blue blocks = 3 orange blocks',32)
 if vid=='measure-double-half-third' and i==0:
  card(d);strip(d,510,475,900,video.TEAL);label(d,960,580,'Original strip: 18 cm',43);label(d,960,710,'Double? Half? One third?',40)
 if vid=='measure-estimate-nearby-length' and i<2:
  card(d);strip(d,430,470,720,'#4279BD');strip(d,430,625,840,'#DC8B34');label(d,1320,500,'12 cm');label(d,1470,655,'? cm');label(d,960,790,'Choose: 8 cm, 14 cm, or 25 cm',37)
 if vid=='measure-longer-then-total' and i<2:
  card(d);strip(d,560,465,480,video.TEAL);strip(d,560,620,480,video.TEAL);strip(d,1040,620,340,'#DC8B34');label(d,385,492,'First');label(d,385,647,'Second');label(d,800,570,'24 cm');label(d,1210,725,'17 cm extra');label(d,960,810,'Find the second length before adding both.',30)
 if vid=='time-cross-hour-minutes' and i==0:
  card(d);clock(d,8,55);video.text(d,(970,510),'8:55',52,video.TEAL,True);video.text(d,(970,610),'20 minutes later?',38,video.INK,True)
 if vid=='data-picture-count-one' and i<4:picture(d,['Trains','Boats','Kites'],[3,7,4],1,'toy')
 if vid=='data-picture-total-difference' and i<2:picture(d,['Comics','Poems','Myths'],[7,2,5],1,'book')
 if vid=='data-picture-scaled-key' and i<2:picture(d,['Ari','Bo','Cy'],[2,5,3],3,'shells')
 if vid.startswith('data-lineplot-') and i<2:
  plot(d,[4] if vid=='data-lineplot-count-mode' and i==1 else [1,2,3] if vid=='data-lineplot-threshold' and i==1 else [])
 if vid=='shape-count-seven-sides-corners' and i<4:
  card(d);cx=760;cy=600;r=185;points=[(cx+r*math.sin(j*2*math.pi/7),cy-r*math.cos(j*2*math.pi/7)) for j in range(7)]
  d.polygon(points,fill='#D6ECE7',outline=video.INK,width=5)
  for j,(x,y) in enumerate(points):
   if i in (1,2,3):
    if i==3:label(d,cx+(x-cx)*1.18,cy+(y-cy)*1.18,str(j+1),26)
    else:
     nx,ny=points[(j+1)%7];label(d,cx+((x+nx)/2-cx)*1.14,cy+((y+ny)/2-cy)*1.14,str(j+1),26)
   if j==0:d.ellipse((x-8,y-8,x+8,y+8),fill='#DC8B34')
  label(d,1320,545,['Count sides and corners.','Count each straight side.','Count each corner.','7 sides; 7 corners.'][i],31)
  label(d,1320,640,'Orange dot: start here',27)
 if vid=='shape-check-equal-square-grid' and i<4:
  card(d);grid(d,405,470,2,4,88);grid(d,1140,470,2,4,88,True);label(d,580,725,'P');label(d,1315,725,'Q');label(d,960,810,'Check the rows, columns, and the shape of every cell.',30)
 if vid=='count-compare-two-arrays' and i<3:
  card(d);grid(d,360,465,2,7,65);grid(d,1120,465,3,6,65);label(d,585,750,'P: 2 rows of 7',33);label(d,1315,750,'Q: 3 rows of 6',33)
def lessons(doc):
 assert sum([1,3,5,4,2])==15 and sum([1,3,5])==9 and sum([4,2])==6
 assert sum([2,5,3])*3==30 and (5-2)*3==9
 result=make_lessons(SPECS,doc)
 for s in SPECS:video.DRAW[s['video_id']]=lambda d,i,p,s=s:draw(s,d,i,p)
 return result
