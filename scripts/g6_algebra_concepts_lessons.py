import json
from pathlib import Path
from card_lessons import make_lessons
SPECS=json.loads((Path(__file__).resolve().parents[1]/'videos/production-g6-u6/lesson-specs.json').read_text())
def lessons(doc):return make_lessons(SPECS,doc)
