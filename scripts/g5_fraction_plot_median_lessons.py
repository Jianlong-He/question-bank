import json
from pathlib import Path
from card_lessons import make_lessons
import generate_sample_videos as v
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g5-u15-u16/lesson-specs.json').read_text())
def draw(s,d,scene,p):
 d.rounded_rectangle((145,345,1775,930),radius=35,fill='white')
 left,y,w=230,780,600
 def x(n):return left+(n-.25)/1.5*w
 v.arrow(d,(left-20,y),(left+w+30,y),v.INK,4)
 for i,label in enumerate(['1/4','1/2','3/4','1','1 1/4','1 1/2','1 3/4'],1):
  px=x(i/4);d.line((px,y-10,px,y+10),fill=v.INK,width=3);v.text(d,(px,y+20),label,29,v.INK,False,'mt')
 v.text(d,(left+w/2,y+75),'Ribbon length (metres)',30,v.INK,True,'mt')
 counts=[(.5,2),(.75,2),(1,1),(1.25,3)]+([(1.5,1)] if scene==4 else [])
 idx=0
 for value,n in counts:
  for j in range(n):
   idx+=1;px=x(value);py=y-45-j*62
   selected=(scene==1 and idx==3) or (scene in [2,3] and idx in [4,5]) or (scene==4 and idx==5)
   color='#cb7816' if selected else v.TEAL
   d.ellipse((px-11,py-11,px+11,py+11),fill=color)
   if scene>0:v.text(d,(px+18,py),str(idx),24,color,True,'lm')
 v.text(d,(left,420),'Each dot = one ribbon',29,v.MUTED,True)
 lines=[]
 for part in s['displays'][scene].split('\n'):lines+=v.wrap(d,part,44,740)
 py=610-len(lines)*32
 for line in lines:v.text(d,(950,py),line,44,v.TEAL,True);py+=64
 if scene==4:v.centered(d,965,'Check the method, then try your worksheet.',30,v.MUTED)
def lessons(doc):
 ls=make_lessons(SPECS,doc)
 for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:draw(s,d,scene,p)
 return ls
