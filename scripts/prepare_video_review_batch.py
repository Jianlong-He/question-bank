"""Read-only review packets: source rows, shared references and reuse candidates.

Arithmetic results and text-similarity candidates are aids, never approvals.
"""
import argparse
from collections import Counter, defaultdict
import csv
import hashlib
import json
from pathlib import Path
import re
from fractions import Fraction
from build_video_correspondence import ROOT
from card_lessons import exact


def arithmetic_check(row):
    prompt=row['Question Choices'].strip().replace('−','-').replace('×','*').replace('÷','/')
    match=re.fullmatch(r'(?:What is|Calculate|Compute|Evaluate|Find)\s+([\d\s.+*/()\-]+)\s*\?',prompt,re.I)
    if not match:return {'status':'manual_review_required'}
    try:
        answer=exact(match[1])
        keys=[]
        for part in row['Question Answers'].split('|'):
            if re.fullmatch(r'\s*-?\d+(?:\.\d+)?(?:/\d+)?\s*',part):keys.append(Fraction(part.strip()))
        return {'status':('numeric_key_matches' if answer in keys else 'numeric_key_mismatch') if keys else 'manual_review_required',
                'computed_answer':str(answer),'scope':'Numeric answer only; review wording, choices, hints and every solution step separately.'}
    except (ValueError,SyntaxError,ZeroDivisionError):return {'status':'manual_review_required'}


def tokens(text):
    stop={'the','and','what','how','many','find','with','from','that','this','which','are','for','has','have','does','then','than','more','less','select','fill','each'}
    return {s for s in re.findall(r'[a-z]{3,}',text.lower()) if s not in stop}


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True,help='Canonical videos directory (read only).')
    p.add_argument('--grade',type=int,required=True);p.add_argument('--unit',type=int,action='append')
    p.add_argument('--packet',type=Path,required=True);p.add_argument('--limit',type=int,default=200)
    a=p.parse_args();assert a.limit>0
    d=json.loads((a.output/'worksheet-video-correspondence.json').read_text())
    refs=defaultdict(list)
    for f,w in d['worksheets'].items():
        for q,problem in w['problems'].items():
            for link in problem['video_links']:refs[link['video_id']].append([f,q])
    available=[]
    for vid,v in d['videos'].items():
        if v['production_status']=='rendered':
            question=(v.get('example') or {}).get('question','')
            available.append((vid,tokens(v['title']+' '+question),v))
    selected=[];total=0
    worksheets=sorted(d['worksheets'].items(),key=lambda x:(x[1]['curriculum'].get('unit',999),x[0]))
    for f,w in worksheets:
        c=w['curriculum']
        if c.get('grade')!=a.grade or (a.unit and c.get('unit') not in a.unit):continue
        with (ROOT/f).open(encoding='utf-8-sig',newline='') as stream:rows={r['Question ID']:r for r in csv.DictReader(stream)}
        for q,problem in sorted(w['problems'].items(),key=lambda item:int(item[0])):
            if problem['mapping_status']!='needs_review':continue
            total+=1
            if len(selected)>=a.limit:continue
            row=rows[q];terms=tokens(row['Question Choices'])
            ranked=sorted(((len(terms&t)/max(1,len(terms|t)),vid,v) for vid,t,v in available),key=lambda x:(-x[0],x[1]))
            candidates=[{'video_id':vid,'title':v['title'],'example':v.get('example'),'text_overlap_score':round(score,3)} for score,vid,v in ranked[:3] if score>0]
            selected.append({'worksheet':f,'worksheet_number':w['worksheet_number'],'question_id':q,
                'source_row_sha256':hashlib.sha256(json.dumps(row,sort_keys=True,ensure_ascii=False).encode()).hexdigest(),
                'source_row':row,'mapping':problem,'arithmetic_check':arithmetic_check(row),
                'reuse_candidates_unreviewed':candidates})
    families={vid:refs[vid] for item in selected for vid in [l['video_id'] for l in item['mapping']['video_links']]}
    report={'grade':a.grade,'units':a.unit,'total_pending_in_scope':total,'questions_in_packet':len(selected),
        'instructions':'Review every source answer, hint, solution, choice and required figure. Candidates are text matches only; do not auto-approve or merge. Reuse a video only if its method fits and its example differs. Preserve all original references before any consolidation.',
        'arithmetic_summary':dict(Counter(r['arithmetic_check']['status'] for r in selected)),
        'questions':selected,'original_family_references_all_grades':families}
    a.packet.parent.mkdir(parents=True,exist_ok=True);a.packet.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({'packet':str(a.packet),'questions':len(selected),'total_pending':total,'original_families':len(families),'arithmetic':report['arithmetic_summary']},indent=2))


if __name__=='__main__':main()
