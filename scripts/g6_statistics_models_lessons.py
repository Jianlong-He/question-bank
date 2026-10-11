import json
from pathlib import Path
from collections import Counter
from card_lessons import make_lessons
import generate_sample_videos as v
from generate_sample_videos import text,TEAL,INK,MUTED
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g6-u11/lesson-specs.json').read_text())
ORANGE='#C58634'
def bg(d):d.rounded_rectangle((145,340,1775,915),radius=32,fill='white')
def line(d,y,t,size=38,color=TEAL):text(d,(960,y),t,size,color,True,anchor='mm')
def dots(d,values,low,high,y=680,x0=380,x1=1520):
 c=Counter(values);scale=(x1-x0)/(high-low)
 d.line((x0,y,x1,y),fill=INK,width=3)
 for a in range(low,high+1):
  x=x0+(a-low)*scale;text(d,(x,y+24),str(a),30,INK,anchor='mt');d.line((x,y,x,y+8),fill=INK,width=2)
  for j in range(c[a]):d.ellipse((x-12,y-38-j*45-12,x+12,y-38-j*45+12),fill=TEAL)
def bars(d,values,labels,x0=420,y=755,w=240,scale=37):
 d.line((x0,y,x0+len(values)*w,y),fill=INK,width=3)
 d.line((x0,y,x0,y-max(values)*scale-45),fill=INK,width=3)
 for i,(value,label) in enumerate(zip(values,labels)):
  x=x0+i*w;d.rectangle((x,y-value*scale,x+w,y),fill='#D6EEEB',outline=TEAL,width=3);text(d,(x+w/2,y-value*scale-15),str(value),36,INK,True,anchor='mb');text(d,(x+w/2,y+25),label,32,INK,anchor='mt')
 text(d,(x0-55,y-max(values)*scale/2),'Count',28,MUTED,anchor='mm')
def draw_freq(vid,d,s):
 bg(d)
 if vid=='statistics-frequency-dot-plots':
  line(d,405,'Value: 2 → 1     3 → 2     4 → 3     6 → 1',38,INK);dots(d,[2,3,3,4,4,4,6],1,7);line(d,850,['','Frequencies count observations','One dot per observation','Mode 4; frequency 3'][s])
 else:
  dots(d,[1,3,3,5,6,6,8],0,9);x=380+5/9*1140;d.line((x,415,x,720),fill=ORANGE,width=4);line(d,405,'Strictly greater than 5: exclude 5',40,INK);line(d,850,'Count 6, 6, 8 → 3 observations')
def draw_hist(vid,d,s):
 bg(d)
 if vid=='statistics-read-histogram':
  line(d,395,'Books read by 15 students',42,INK);bars(d,[3,6,4,2],['0–9','10–19','20–29','30–39']);line(d,866,['','Bar heights count students','Total: 3 + 6 + 4 + 2 = 15','At least 20 books: 4 + 2 = 6'][s])
 else:
  line(d,425,'Total: 28 observations',48,INK)
  for i,label in enumerate(['7','?' if s==1 else '11','6','4']):
   x=400+i*290;d.rounded_rectangle((x-95,510,x+95,675),radius=20,fill='#D6EEEB');text(d,(x,590),label,72,TEAL,True,anchor='mm');text(d,(x,715),f'Bin {i+1}',33,INK,anchor='mm')
  line(d,845,['','Known counts: 7 + 6 + 4 = 17','Missing: 28 − 17 = 11','Check: 7 + 11 + 6 + 4 = 28'][s])
def draw_boxes(d,s):
 bg(d);x=lambda a:350+(a-10)*44
 for name,vals,y in [('A',(16,20,24,28,32),480),('B',(16,21,23,25,30),675)]:
  lo,q1,m,q3,hi=vals;text(d,(270,y),name,45,INK,True,anchor='mm');d.line((x(lo),y,x(hi),y),fill=INK,width=4)
  for n in [lo,hi]:d.line((x(n),y-28,x(n),y+28),fill=INK,width=4)
  d.rectangle((x(q1),y-45,x(q3),y+45),fill='#D6EEEB',outline=TEAL,width=4);d.line((x(m),y-45,x(m),y+45),fill=TEAL,width=6)
  for n in vals:text(d,(x(n),y+60),str(n),29,INK,anchor='mt')
  if name=='B':d.ellipse((x(38)-8,y-8,x(38)+8,y+8),fill=ORANGE);text(d,(x(38),y+60),'38',29,INK,anchor='mt');text(d,(x(38),y-45),'outlier',29,ORANGE,anchor='mm')
 line(d,855,['','Medians: A 24 > B 23','Ranges: A 16; B 22 (include the outlier)','IQR: A 8; B 4'][s],39)
def draw_shapes(d,s):
 bg(d)
 for j,(vals,label) in enumerate([([1,2,3,5,8,12,6],'Left-skewed'),([1,3,6,10,6,3,1],'Symmetric'),([6,12,8,5,3,2,1],'Right-skewed')]):
  x0=280+j*510;y=735;w=48
  for i,h in enumerate(vals):d.rectangle((x0+i*w,y-h*23,x0+(i+1)*w,y),fill='#D6EEEB' if s!=j+1 else '#FFE5BA',outline=TEAL,width=2)
  d.line((x0,y,x0+7*w,y),fill=INK,width=3);text(d,(x0+168,780),label,33,INK,True,anchor='mm');text(d,(x0+168,832),'Travel time →',29,MUTED,anchor='mm')
 line(d,393,'Follow the long tail, not the tallest bar',43)
def draw_features(d,s):
 bg(d);dots(d,[2,3,3,3,4,4,5,14],1,15,x0=300,x1=1600)
 line(d,405,['','Cluster: seven values from 2 to 5','Gap: no values strictly between 5 and 14','Peak: three dots at 3'][s],40,INK)
 if s==1:d.rounded_rectangle((350,470,690,725),radius=20,outline=ORANGE,width=4)
 if s==2:d.line((750,530,1480,530),fill=ORANGE,width=4)
 line(d,850,'The isolated value 14 is far from the cluster',37)
def draw_info(d,s):
 bg(d)
 if s==1:dots(d,[2,4,4,7,9],0,10);line(d,405,'Exact values: 2, 4, 4, 7, 9',42,INK);line(d,850,'Third observation → median 4')
 elif s==2:bars(d,[3,2],['0–4','5–9'],x0=570,w=380,scale=75);line(d,405,'Counts alone do not reveal the exact median',40,INK)
 else:
  x=lambda n:360+n*120;y=570;d.line((x(2),y,x(9),y),fill=INK,width=4)
  for n in [2,9]:d.line((x(n),y-35,x(n),y+35),fill=INK,width=4)
  d.rectangle((x(3),y-70,x(8),y+70),fill='#D6EEEB',outline=TEAL,width=4);d.line((x(4),y-70,x(4),y+70),fill=TEAL,width=6)
  for n,label in [(2,'min 2'),(3,'Q1 3'),(4,'median 4'),(8,'Q3 8'),(9,'max 9')]:text(d,(x(n),730 if n%2 else 690),label,29,INK,anchor='mt')
  line(d,405,'Median is marked by the line inside the box',40,INK);line(d,850,'A summary, not the complete list of observations',37)
def lessons(doc):
 ls=make_lessons(SPECS,doc)
 for l in ls:
  vid=l['video_id'];old=v.DRAW[vid];fn=None
  if vid in ['statistics-frequency-dot-plots','statistics-dot-plot-threshold']:fn=lambda d,s,vid=vid:draw_freq(vid,d,s)
  elif vid in ['statistics-read-histogram','statistics-histogram-missing-count']:fn=lambda d,s,vid=vid:draw_hist(vid,d,s)
  elif vid=='statistics-compare-box-plots':fn=draw_boxes
  elif vid=='statistics-distribution-shapes':fn=draw_shapes
  elif vid=='statistics-clusters-gaps-outliers':fn=draw_features
  elif vid=='statistics-display-information':fn=draw_info
  if fn:v.DRAW[vid]=lambda d,s,p,fn=fn,old=old:fn(d,s) if s in [1,2,3] else old(d,s,p)
 return ls
