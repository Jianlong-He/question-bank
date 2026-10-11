import json
from pathlib import Path
from card_lessons import make_lessons
def lessons(doc):
 specs=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g5-u10-u11/lesson-specs.json').read_text())
 return make_lessons(specs,doc)
