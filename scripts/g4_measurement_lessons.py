import json
from pathlib import Path
from card_lessons import make_lessons
def lessons(doc):
 return make_lessons(json.loads((Path(__file__).resolve().parents[1]/'videos/production-g4-u14/lesson-specs.json').read_text()),doc)
