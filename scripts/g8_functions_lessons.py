import json
from pathlib import Path
from card_lessons import make_lessons,draw_card
import generate_sample_videos as video
from generate_sample_videos import text,TEAL,INK,MUTED
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g8-u3/lesson-specs.json').read_text())
def graph_test(s,d,scene,p):
 if scene in [0,4]:return draw_card(s,d,scene,p)
 d.rounded_rectangle((145,360,1775,840),radius=35,fill='white')
 cx,cy,scale=560,595,43
 def pt(x,y):return (cx+x*scale,cy-y*scale)
 for k in range(-5,6):
  d.line([pt(k,-5),pt(k,5)],fill='#e5e9ed',width=2);d.line([pt(-5,k),pt(5,k)],fill='#e5e9ed',width=2)
 d.line([pt(-5,0),pt(5,0)],fill=INK,width=3);d.line([pt(0,-5),pt(0,5)],fill=INK,width=3)
 text(d,(cx+220,cy+4),'x',26,INK);text(d,(cx+6,cy-229),'y',26,INK)
 if scene==1:
  d.line([pt(-5,-2),pt(5,-2)],fill=TEAL,width=6);d.line([pt(2,-5),pt(2,5)],fill='#d06a23',width=4);dots=[pt(2,-2)]
 elif scene==2:
  d.line([pt(-2,-5),pt(-2,5)],fill=TEAL,width=8);dots=[pt(-2,1),pt(-2,3)]
 else:
  d.ellipse((cx-4*scale,cy-4*scale,cx+4*scale,cy+4*scale),outline=TEAL,width=6);d.line([pt(0,-5),pt(0,5)],fill='#d06a23',width=4);dots=[pt(0,4),pt(0,-4)]
 for x,y in dots:d.ellipse((x-9,y-9,x+9,y+9),fill='#c03b39')
 lines=s['displays'][scene].split('\n')
 for j,line in enumerate(lines):text(d,(870,490+j*78),line,40,INK)
 captions={1:'One intersection: passes',2:'Many outputs at x = −2: fails',3:'Two outputs at x = 0: fails'}
 text(d,(870,690),captions[scene],35,TEAL)
def lessons(doc):
 result=make_lessons(SPECS,doc)
 s=next(s for s in SPECS if s['video_id']=='function-vertical-line-test')
 video.DRAW[s['video_id']]=lambda d,scene,p:graph_test(s,d,scene,p)
 return result
