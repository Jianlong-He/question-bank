"""Build the full worksheet-to-video plan without generating or uploading videos.

Usage: python3 scripts/build_video_correspondence.py [--check] [--survey]
Existing checked mappings, video IDs, media assets, and YouTube fields survive.
Automatic method/template assignments remain needs_review until checked.
"""
from pathlib import Path
import argparse
import collections
import csv
import hashlib
import json
import re
import unicodedata
from video_reuse import validate_reuse
from video_mapping_rules import RULES

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'videos'
TARGET=OUT/'worksheet-video-correspondence.json'
RULE_VERSION='2026-10-08.1'
# Existing identifiers are stable, even if they contain the original grade.
LEGACY={
 'counting-next':'g1-u1-counting-forward',
 'counting-backward':'g1-u1-counting-backward',
 'multiplication-equal-groups':'g3-u1-equal-groups',
 'ratios-simplify':'g6-u1-simplifying-ratios',
 'number-theory-prime-factorization':'enrichment-number-theory-1-prime-factor-tree',
 'number-theory-modular-subtraction':'enrichment-number-theory-1-negative-remainders',
 'number-theory-modular-addition':'enrichment-number-theory-1-modular-addition',
 'counting-combinations-pairs':'enrichment-counting-and-probability-1-choosing-a-pair',
 'counting-combinations-three':'enrichment-counting-and-probability-1-choose-three',
 'probability-first-success-second':'enrichment-counting-and-probability-1-first-red-on-second-draw',
}

def digest(s):return hashlib.sha256(s.encode('utf-8')).hexdigest()
def slug(s):return re.sub('[^a-z0-9]+','-',s.lower()).strip('-')

def norm(text):
    superscripts=str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺','0123456789-+')
    text=re.sub(r'[⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺]+',lambda m:'^('+m[0].translate(superscripts)+')',text)
    text=unicodedata.normalize('NFKC',text).lower()
    for a,b in [('−','-'),('–','-'),('\\times','×'),('\\cdot','×'),('\\div','÷'),('\\sqrt','sqrt'),('\\left',''),('\\right','')]:text=text.replace(a,b)
    text=re.sub(r'\\(?:d?frac)\s*\{([^{}]+)\}\s*\{([^{}]+)\}',r'(\1/\2)',text)
    return re.sub(r'\s+',' ',text.replace('$','').replace('\\_','_')).strip()

def curriculum_titles():
    result={}
    def walk(items):
        for item in items:
            title=item.get('title','')
            m=re.fullmatch(r'(\d+)(?:st|nd|rd|th) grade math',title,re.I)
            if m:result[int(m[1])]=[n['title'] for n in item.get('submenu',[])]
            walk(item.get('submenu',[]))
    walk(json.loads((ROOT/'data/curriculum.json').read_text()))
    return result
TITLES=curriculum_titles()

def worksheet_meta(path):
    parts=path.parts
    if parts[1]=='enrichment':
        cur={'kind':'enrichment','track':parts[2],'topic':parts[3]}
        unit_topic=parts[3]
    else:
        grade=int(re.search(r'Grade (\d+)',parts[1]).group(1))
        match=re.search(r'(?:G\d+Unit|Unit)\s*(\d+)',str(path))
        unit=int(match.group(1)) if match else None
        assert unit is not None,path
        cur={'kind':'grade','grade':grade,'unit':unit}
        unit_topic=TITLES.get(grade,[])[unit-1]
    number=re.search(r'(?:W|worksheet)(\d+(?:-\d+)?)',path.stem,re.I)
    variant='homework' if re.search('HW',path.stem,re.I) else 'revision' if re.search('rev',path.stem,re.I) else 'practice'
    return {'curriculum':cur,'worksheet_number':number.group(1) if number else None,'worksheet_variant':variant,'unit_topic':unit_topic}

def raw_prompt(q):
    # Keep all options for identity/fallback; semantic rules inspect the stem.
    return re.split(r'~~|\bChoices:',q,maxsplit=1)[0].strip()

def numeric_method(question,unit_topic):
    q=norm(question)
    q=q.replace('*','×')
    q=re.sub(r'(?<=\d)\s*x\s*(?=[\d(])','×',q)
    q=q.replace('multiplied by','×').replace('divided by','÷').replace('plus','+').replace('minus','-')
    q=re.sub(r'^(?:(?:fill|compute|calculate|find|evaluate|simplify|what is|multiply|divide|add|subtract)\s*[:.]?\s*)+','',q)
    q=re.split(r'[?.]|write (?:your|the) (?:answer|result)',q)[0] if not re.search(r'\d\.\d',q) else re.split(r'\?|write (?:your|the) (?:answer|result)',q)[0]
    q=re.split(r'\b(?:using|give|express|leave|in simplest)\b',q)[0]
    q=re.sub(r'\s*=\s*_+\s*$','',q).strip(' .?')
    if not re.fullmatch(r'[\d\s.+×÷/()^_=-]+',q) or not re.search(r'\d',q):return None
    if '=' in q and re.search(r'_',q):return ('arithmetic-missing-number','Find missing numbers using inverse operations')
    if '^' in q:
        if re.search(r'\^\(?-',q):return ('arithmetic-negative-exponents','Evaluate negative exponents')
        if re.search(r'\^\(?\d+/',q):return ('rational-exponents','Convert and evaluate rational exponents')
        without_powers=re.sub(r'\^\(?\d+\)?','',q)
        if re.search(r'[+×÷/]|\d\s*-\s*\d',without_powers):return ('arithmetic-order-operations-with-powers','Use order of operations including powers')
        if re.search(r'\d\.\d',q):return ('arithmetic-powers-decimals','Evaluate powers of decimals')
        if re.search(r'-\d',q):return ('arithmetic-powers-signed-numbers','Evaluate powers of signed numbers')
        return ('arithmetic-evaluate-powers','Evaluate powers of whole numbers')
    ops=set(re.findall(r'[+×÷]',q))
    if re.search(r'\d\s*[-]\s*\d',q):ops.add('-')
    fractions=re.findall(r'(\d+)\s*/\s*(\d+)',q)
    if '/' in q and not fractions:ops.add('÷')
    if not ops and fractions and len(fractions)==1:
        if not re.search(r'fraction|denominator|numerator|simplify|reduce',question,re.I):
            return ('arithmetic-divide-whole-numbers','Divide whole numbers')
        return None
    if not ops:return None
    kind='fractions' if fractions else 'decimals' if re.search(r'\d\.\d',q) else 'integers' if re.search(r'(?:^|[ (×÷+])-\d',q) else 'whole-numbers'
    if kind=='fractions' and re.search(r'\d\s+\d\s*/',q):kind='mixed-numbers'
    if len(ops)>1 and not ops<= {'+','-'}:return ('arithmetic-order-operations-'+kind,'Use the order of operations with '+kind.replace('-',' '))
    op='add-subtract' if ops=={'+','-'} else {'+':'add','-':'subtract','×':'multiply','÷':'divide'}[next(iter(ops))]
    suffix=''
    if kind=='fractions' and op in ['add','subtract','add-subtract'] and len(fractions)>1:
        suffix='-like-denominators' if len(set(b for a,b in fractions))==1 else '-unlike-denominators'
    if kind=='whole-numbers' and op in ['add','subtract','add-subtract']:
        nums=[int(n) for n in re.findall(r'\d+',q)]
        suffix='-within-20' if max(nums)<=20 else '-column-method'
    return (f'arithmetic-{op}-{kind}{suffix}',f'{op.replace("-"," and ").capitalize()} {kind.replace("-"," ")}{suffix.replace("-"," ")}')

def refine(key,title,q,unit_topic):
    # Different formulas/representations are separate teaching videos.
    if key in ['geometry-area','geometry-volume','geometry-surface-area','geometry-perimeter']:
        shapes=[('composite',r'composite|combined|compound|l.shaped'),('sphere',r'sphere|hemisphere'),('cone',r'cone'),('cylinder',r'cylinder'),('pyramid',r'pyramid'),('cube',r'cube|cubic block'),('rectangular-prism',r'rectangular (prism|box)|cuboid'),('circle',r'circle|circular'),('trapezoid',r'trapezoid|trapezium'),('parallelogram',r'parallelogram'),('triangle',r'triangle|triangular'),('rectangle',r'rectangle|rectangular'),('square',r'\bsquare\b')]
        shape=next((name for name,pat in shapes if re.search(pat,q)), 'general')
        subtype=''
        if re.search(r'vertices.*\(|\(.*\).*\(.*\)',q):subtype='-coordinates'
        elif re.search(r'(?:find|what is|how (?:long|wide|tall)).*(?:width|height|length|base|radius|side)|what is the other side',q):subtype='-missing-dimension'
        if key=='geometry-area' and re.search(r'(?:find|what is|calculate).*perimeter',q):key='geometry-perimeter-from-area'
        return key+'-'+shape+subtype,title+' — '+shape.replace('-',' ')+subtype.replace('-',' ')
    if key=='geometry-angle-measure':
        methods=[('triangle-sum',r'triangle.*angles?|angles?.*triangle'),('parallelogram',r'parallelogram'),('inscribed',r'inscribed|semicircle|central angle|circle'),('bisector',r'bisect'),('intersecting-lines',r'intersect|adjacent|vertical angle'),('classification',r'acute|obtuse|right angle|straight angle|type of angle')]
        for method,pat in methods:
            if re.search(pat,q):return key+'-'+method,'Work with angles: '+method.replace('-',' ')
    if key=='complex-arithmetic':
        methods=[('root-count',r'how many|counting multiplicity'),('conjugate-roots',r'real.coefficient|real coefficients'),('locus',r'lie on|shape'),('rotation',r'rotat'),('plot',r'plot|real part|imaginary part|coordinate'),('negative-square-root',r'solve|sqrt|√'),('subtract',r'subtract'),('divide',r'divide|quotient|/'),('multiply',r'multiply|product|\^|\)\s*\('),('add',r'add|sum|\)\s*\+\s*\(')]
        for method,pat in methods:
            if re.search(pat,q):return key+'-'+method,'Complex numbers: '+method.replace('-',' ')
    if key=='linear-slope':
        method='from-points' if re.search(r'\([^)]*,[^)]*\).*\([^)]*,',q) else 'from-equation' if '=' in q else 'from-graph' if re.search(r'graph|rise|run',q) else 'interpretation'
        return key+'-'+method,'Find or interpret slope '+method.replace('-',' ')
    if key=='number-place-value':
        method='decimals' if re.search(r'\d\.\d|hundredths|tenths|thousandths',q) else 'expanded-form' if 'expanded' in q else 'whole-numbers'
        return key+'-'+method,'Place value: '+method.replace('-',' ')
    if key=='decimal-fraction-conversion':
        method='to-decimal' if re.search(r'as a decimal|decimal form|fraction.*decimal|decimal.*\d+/\d+',q) else 'to-fraction'
        return key+'-'+method,'Convert '+method.replace('-',' ')
    if key=='systems-solve':
        method='nonlinear' if re.search(r'\^|quadratic|circle|parabola',q) else 'model' if re.search(r'matches|scenario|represent|write',q) else 'solution-count' if re.search(r'infinite|no solution|one solution|how many solutions',q) else 'elimination' if 'elimination' in q else 'substitution'
        return key+'-'+method,'Solve or model systems: '+method.replace('-',' ')
    if key=='counting-combinations':
        if re.search(r'(teams?|groups?|choose|select|set|committee).*\b(?:2|two|pair)\b|\d+c2\b|c\(\d+[,; ]+2\)',q):return 'counting-combinations-pairs','Choose unordered pairs'
        if re.search(r'(teams?|groups?|choose|select|set|committee).*\b(?:3|three)\b|\d+c3\b|c\(\d+[,; ]+3\)',q):return 'counting-combinations-three','Choose unordered groups of three'
    if key=='probability-first-success':
        if re.search(r'largest|maximum|at most|support',q):return key+'-support','Find the support of a first-success distribution'
        if re.search(r'compute the sum|sum p\(|sum.*probabilit',q):return key+'-total','Check that a first-success distribution sums to one'
        if re.search(r'p\(2\)|x\s*=\s*2|comes? second|second draw|draw 2',q):return key+'-second','First success on draw two without replacement'
        if re.search(r'p\(1\)|x\s*=\s*1|first draw',q):return key+'-first','First success on the first draw'
    if key=='ratios-simplify' and ('fraction' in q):return key+'-fraction','Write ratios as simplified fractions'
    if key=='measurement-unit-conversion':
        unit='time' if re.search(r'minute|hour|second',q) else 'mass' if re.search(r'gram|pound|ounce|tonne',q) else 'capacity' if re.search(r'lit[er]|gallon|pint|quart|ml\b',q) else 'length'
        return key+'-'+unit,'Convert '+unit+' units'
    if key=='linear-equations-solve':
        if re.search(r'\^\(?2|[a-z]\s*\([^)]*[a-z]',q):return 'quadratics-equations','Solve quadratic equations'
        if re.search(r'\d+\s*\(',q):return key+'-parentheses','Solve linear equations with parentheses'
        if re.search(r'\b[a-z]\b[^a-z=]*=[^a-z=]*[a-z]\b|\d[a-z][^a-z=]*=[^a-z=]*[a-z]\b',q):return key+'-both-sides','Solve linear equations with variables on both sides'
        return key+'-one-side','Solve linear equations with variables on one side'
    if key=='number-rounding':
        return key+('-decimals' if re.search(r'\d\.\d|tenth|hundredth|thousandth',q) else '-whole'),'Round decimals' if re.search(r'\d\.\d|tenth|hundredth|thousandth',q) else 'Round whole numbers'
    return key,title

def classify(question,meta):
    stem=raw_prompt(question)
    q=norm(stem)
    context=meta['unit_topic']
    # Explicit requested methods outrank incidental mention of a supporting method.
    for key,title,pattern in RULES:
        if key in {'number-theory-gcf','number-theory-lcm','probability-expected-value'} and pattern.search(q):return key,title,'rule'
    priorities=[
        ('fractions-common-denominator','Find a common denominator',r'least common denominator|lowest common denominator|\blcd\b'),
        ('counting-digit-constraints','Count numbers satisfying digit constraints',r'how many.*digit numbers|how many.*numbers.*digits'),
        ('algebra-rearrange-formula','Rearrange formulas to isolate a variable',r'(?:rearrange|solve for [a-z]).*=|=.*solve for [a-z]'),
        ('algebra-evaluate','Evaluate expressions by substitution',r'=.*when\s+[a-z]\s*='),
        ('complex-modulus','Find the modulus of a complex number',r'modulus.*i\b|modul[ui].*product'),
        ('complex-midpoint','Find the midpoint of complex numbers',r'midpoint.*(?:complex|\di\b)'),
        ('complex-distance','Find distance between complex numbers',r'distance.*(?:complex|\di\b)'),
        ('trigonometry-law-of-cosines','Solve triangles with the law of cosines',r'two sides.*included angle'),
        ('fractions-equivalent','Find equivalent fractions and missing numerators',r'(?:convert|write).*\d+/\d+.*(?:halves|thirds|fourths|fifths|sixths|eighths|ninths|tenths|twelfths)'),
    ]
    if re.search(r'^(?:fill\s*:\s*)?solve\b',q) and re.search(r'(?:x[^=]*y|y[^=]*x)\s*=|\by\s*=.*\bx',q) and q.count('=')>=2:
        key,title=refine('systems-solve','Solve simultaneous equations',q,context)
        return key,title,'rule'
    if re.search(r'complex (?:shape|figure)|rectangle.*triangle|triangle.*rectangle',q) and 'area' in q:
        return 'geometry-area-composite','Calculate area of composite figures','rule'
    if re.search(r'quadrilateral.*right angles|four right angles',q):return 'geometry-quadrilaterals','Classify quadrilaterals by their properties','rule'
    if re.search(r'two angles.*included side',q):return 'geometry-congruence','Use congruence and rigid transformations','rule'
    if re.search(r'(?:sides|a=).*included angle',q):return 'trigonometry-law-of-cosines','Solve triangles with the law of cosines','rule'
    if 'number line' in q and re.search(r'fraction|\d/\d',q):return 'fractions-number-line','Locate fractions on number lines','rule'
    for key,title,pattern in priorities:
        if re.search(pattern,q):return key,title,'rule'
    if re.search(r'(estimate|round)',q):
        if re.search(r'(estimate|≈).*(\+|-|×|÷|\\times|\bx\b)|estimate.*(sum|difference|product|quotient)',q):return 'arithmetic-estimation','Estimate arithmetic by rounding','rule'
    arithmetic=numeric_method(stem,context)
    if arithmetic:return *arithmetic,'rule'
    for key,title,pattern in RULES:
        if pattern.search(q):
            if key=='complex-arithmetic' and re.search(r'complex (shape|figure)',q):continue
            if key=='fractions-parts' and re.search(r'divid|multiply|multiplying|both|rational|[a-z]\s*[+]\s*\d|common denominator',q):continue
            key,title=refine(key,title,q,context)
            return key,title,'rule'
    # A normalized expression template is a conservative fallback, never a reviewed match.
    # Keep exponents, signs, fraction structure, options and variable names intact.
    template=norm(question)
    powers=[]
    template=re.sub(r'\^(?:\([^)]*\)|[+-]?\d+(?:/\d+)?)',lambda m: powers.append(m[0]) or f'EXPONENTTOKEN{chr(65+len(powers))}',template)
    template=re.sub(r'(?<![\w^])\d+(?:\.\d+)?', '#', template)
    for index,power in enumerate(powers,1):template=template.replace(f'EXPONENTTOKEN{chr(65+index)}',power)
    template=re.sub(r'\b(?:fill|select|compute|calculate|find|evaluate)\s*[:.]?\s*','',template)
    template=re.sub(r'\s+',' ',template).strip()
    domain=slug(context)
    key='pattern-'+domain+'-'+digest(template)[:12]
    title='Worked method: '+re.sub(r'\s+',' ',stem).strip()[:115]
    return key,title,'template'

def read_inventory():
    result={}
    for p in sorted((ROOT/'worksheets').rglob('*.csv')):
        if p.name.startswith('._'):
            continue  # macOS resource-fork sidecars on portable drives are not CSV data.
        relative=p.relative_to(ROOT)
        meta=worksheet_meta(relative)
        with p.open(encoding='utf-8-sig',newline='') as f:rows=list(csv.DictReader(f))
        ids=[r.get('Question ID') for r in rows]
        if any(not re.fullmatch(r'\d+',i or '') for i in ids) or len(set(ids))!=len(ids):raise ValueError(f'Invalid/duplicate IDs in {p}')
        result[str(relative)]=(meta,rows)
    return result

def validate(doc,inventory,asset_root=ROOT):
    assert set(doc['worksheets'])==set(inventory),'Missing or extra worksheets'
    for file,(meta,rows) in inventory.items():
        assert all(doc['worksheets'][file][k]==v for k,v in meta.items()),file
        assert meta['worksheet_number'] is not None,file
        mapped=doc['worksheets'][file]['problems']
        assert set(mapped)=={r['Question ID'] for r in rows},file
        for row in rows:
            p=mapped[row['Question ID']]
            assert p['question_text']==row['Question Choices'] and p['question_sha256']==digest(row['Question Choices'])
            assert p['video_links'] or p['mapping_status']=='not_needed',(file,row['Question ID'])
            variants=row['Question Choices'].split('||')
            for link in p['video_links']:
                assert link['video_id'] in doc['videos']
                index=link['variant_index']
                assert index is None or 0<=index<len(variants)
                assert link['end_seconds'] is None or link['end_seconds']>link['start_seconds']
            if not any(l['variant_index'] is None for l in p['video_links']) and p['mapping_status']!='not_needed':
                assert set(l['variant_index'] for l in p['video_links'])==set(range(len(variants)))
    for vid,v in doc['videos'].items():
        assert v['production_status'] in ['planned','in_progress','rendered','needs_revision','retired']
        if v['production_status']=='rendered':assert v['assets']['mp4'] and (asset_root/v['assets']['mp4']).is_file(),vid
        for path in v['assets'].values():
            if path is not None:assert (asset_root/path).is_file(),path
        youtube=v['youtube']['video_id']
        assert youtube is None or re.fullmatch('[a-zA-Z0-9_-]{11}',youtube),vid
    validate_reuse(doc)

def build(old,inventory):
    videos=dict(old['videos'])
    worksheets={}
    rule_counts=collections.Counter()
    fallback=[]
    for file,(meta,rows) in inventory.items():
        problems={}
        for row in rows:
            q=row['Question Choices'];qid=row['Question ID'];h=digest(q)
            previous=old.get('worksheets',{}).get(file,{}).get('problems',{}).get(qid)
            keep=bool(previous and previous['question_sha256']==h and
                      (previous['mapping_status'] in ['reviewed','not_needed'] or previous.get('mapping_method')=='manual'))
            if keep:
                problem=dict(previous)
                problem.setdefault('mapping_method','manual')
                problem.setdefault('mapping_rule',None)
            else:
                classifications=[classify(v,meta) for v in q.split('||')]
                same=len(set(k for k,t,m in classifications))==1
                links=[]
                for index,(key,title,method) in enumerate(classifications):
                    vid=LEGACY.get(key,key)
                    if vid not in videos:
                        videos[vid]={
                            'title':title,'curriculum':{'kind':'shared','topic':key.split('-')[0]},
                            'question_type':title,'production_status':'planned','target_duration_seconds':60,
                            'duration_seconds':None,'example':None,'assets':{'mp4':None,'captions':None},
                            'youtube':{'video_id':None,'visibility':None},
                            'notes':'Draft '+('teaching-method group' if method=='rule' else 'question-template group')+'. Review linked questions, choose a new analogous worked example, and confirm difficulty before rendering.',
                            'planning':{'basis':method,'rule':key,'review_status':'needs_review'}
                        }
                    link={'video_id':vid,'coverage':'full','example_mode':'similar_question','variant_index':None if same else index,'start_seconds':0,'end_seconds':None}
                    if link not in links:links.append(link)
                    rule_counts[method]+=1
                    if method=='template':fallback.append((file,qid,key,q))
                notes='Automatically proposed grouping; review the method, difficulty and any linked rendered example before using with students.'
                if previous and previous['question_sha256']!=h:notes='Question changed since the previous mapping. '+notes
                problem={'question_text':q,'question_sha256':h,'mapping_status':'needs_review','video_links':links,'notes':notes,
                         'mapping_method':'rule' if all(m=='rule' for k,t,m in classifications) else 'template',
                         'mapping_rule':';'.join(dict.fromkeys(k for k,t,m in classifications))}
            problem['requires_source_visual']=bool(re.search(r'(shown above|picture|diagram|figure|graph above|plot above|number line.*shown|building above|dragon above|dargon above)',q,re.I))
            problems[qid]=problem
        worksheets[file]={**meta,'problems':problems}
    # Preserve unused existing records (including YouTube uploads) instead of deleting them.
    doc={'$schema':'./worksheet-video-correspondence.schema.json','schema_version':old.get('schema_version','1.1.0'),'path_base':'repository_root',
         'scope':{'mode':'all_worksheets','description':'Complete Grade 1–12 and enrichment CSV inventory. Newly generated links are draft method/template assignments marked needs_review; coverage describes intended teaching coverage, not verified suitability. Existing reviewed mappings and media/YouTube records are preserved.'},
         'mapping_rule_version':RULE_VERSION,'videos':dict(sorted(videos.items())),'worksheets':worksheets}
    return doc,rule_counts,fallback

def summary(doc):
    links=collections.defaultdict(list)
    pergrade=collections.defaultdict(lambda:dict(worksheets=0,problems=0,needs_review=0))
    for file,w in doc['worksheets'].items():
        grade=file.split('/')[1];counts=pergrade[grade];counts['worksheets']+=1
        for qid,p in w['problems'].items():
            counts['problems']+=1;counts['needs_review']+=p['mapping_status']=='needs_review'
            for link in p['video_links']:links[link['video_id']].append((file,qid))
    reused={vid:refs for vid,refs in links.items() if len(refs)>1}
    cross={vid:refs for vid,refs in links.items() if len(set(f.split('/')[1] for f,q in refs))>1}
    return {'worksheet_count':len(doc['worksheets']),'problem_count':sum(v['problems'] for v in pergrade.values()),
            'video_count':len(doc['videos']),'required_video_count':sum(v['production_status']!='retired' for v in doc['videos'].values()),
            'production_status_counts':dict(collections.Counter(v['production_status'] for v in doc['videos'].values())),
            'referenced_video_count':len(links),'unreferenced_video_ids':sorted(set(doc['videos'])-set(links)),
            'problems_requiring_source_visual_review':sum(p['requires_source_visual'] for w in doc['worksheets'].values() for p in w['problems'].values()),
            'mapping_status_counts':dict(collections.Counter(p['mapping_status'] for w in doc['worksheets'].values() for p in w['problems'].values())),
            'mapping_method_counts':dict(collections.Counter(p['mapping_method'] for w in doc['worksheets'].values() for p in w['problems'].values())),
            'videos_reused_by_multiple_problems':len(reused),'videos_shared_across_grades_or_enrichment':len(cross),
            'per_curriculum':dict(pergrade),
            'most_reused_videos':[{'video_id':vid,'problem_links':len(refs),'curricula':sorted(set(f.split('/')[1] for f,q in refs))} for vid,refs in sorted(reused.items(),key=lambda item:-len(item[1]))[:20]]}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');parser.add_argument('--survey',action='store_true');args=parser.parse_args()
    old=json.loads(TARGET.read_text());inventory=read_inventory()
    if args.check:
        validate(old,inventory);print(json.dumps(summary(old),indent=2));return
    doc,counts,fallback=build(old,inventory)
    validate(doc,inventory)
    if args.survey:
        print(json.dumps(summary(doc),indent=2))
        Path('/tmp/worksheet-video-map').mkdir(parents=True,exist_ok=True)
        Path('/tmp/worksheet-video-map/fallback.json').write_text(json.dumps(fallback,ensure_ascii=False))
        Path('/tmp/worksheet-video-map/proposed.json').write_text(json.dumps(doc,ensure_ascii=False))
        return
    TARGET.write_text(json.dumps(doc,indent=2,ensure_ascii=False)+'\n')
    report=summary(doc)
    (OUT/'correspondence-summary.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()
