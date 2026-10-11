import json
from pathlib import Path
import generate_sample_videos as v
from card_lessons import make_lessons,draw_card
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g12-u1-u2/lesson-specs.json').read_text())
def lessons(doc):
 out=make_lessons(SPECS,doc)
 for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:draw_card(s,d,scene,p)
 return out
