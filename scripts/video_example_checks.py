"""Block detectable copies of linked worksheet tasks before rendering.

Literal checks cover every example. Numeric task checks cover ratios, equal groups,
and simple combinations. This is a guardrail, not a substitute for reviewing other methods,
paraphrases, figures, or the pedagogical suitability of an automatic mapping.
"""
import re
import ast
from fractions import Fraction
from build_video_correspondence import norm, raw_prompt


def numeric_signature(question):
    q=norm(raw_prompt(question)).replace('×','*').replace('÷','/').replace('^','**').replace('⁄','/')
    q=re.sub(r'(\d+)\s+(\d+)\s*/\s*(\d+)',r'(\1+\2/\3)',q)
    q=re.sub(r'(?<=\d)\s*x\s*(?=\d)','*',q)
    q=re.sub(r'^(?:(?:fill|find|compute|calculate|evaluate|simplify|what is)\s*[:.]?\s*)+','',q)
    m=re.match(r'[\d.\s()+*/-]+',q)
    if not m:return None
    expression=m[0].strip().rstrip('.')
    try:tree=ast.parse(expression,mode='eval')
    except SyntaxError:return None
    def walk(node):
        if isinstance(node,ast.Expression):return walk(node.body)
        if isinstance(node,ast.Constant) and type(node.value) in (float,int):return ('n',str(Fraction(ast.get_source_segment(expression,node))))
        if isinstance(node,ast.UnaryOp) and isinstance(node.op,(ast.USub,ast.UAdd)):
            operand=walk(node.operand)
            if operand[0]=='n':return ('n',str(-Fraction(operand[1]) if isinstance(node.op,ast.USub) else Fraction(operand[1])))
            return ('negative' if isinstance(node.op,ast.USub) else 'positive',operand)
        if isinstance(node,ast.BinOp) and isinstance(node.op,(ast.Add,ast.Sub,ast.Mult,ast.Div,ast.Pow)):
            children=[walk(node.left),walk(node.right)]
            if isinstance(node.op,(ast.Add,ast.Mult)):children.sort(key=repr)
            return (type(node.op).__name__,*children)
        raise ValueError('Non-numeric expression')
    try:return walk(tree)
    except (ValueError,ZeroDivisionError):return None


def signature(question,video_id):
    q=norm(raw_prompt(question))
    numbers=re.findall(r'\d+',q)
    if video_id.startswith('arithmetic-'):return numeric_signature(question)
    if video_id in {'geometry-area-rectangle','geometry-volume-rectangular-prism','geometry-volume-cube'}:
        # Compare concrete dimensions even when their order or units are renamed.
        # Ignore unit powers; inverse, algebraic and composite tasks need manual review.
        cleaned=re.sub(r'\b(cm|mm|km|m|ft|in)\s*\^\(?[23]\)?',r'\1',q)
        values=re.findall(r'\d+(?:\.\d+)?(?:/\d+)?',cleaned)
        if not re.search(r'perimeter|cut.out|shaded|remaining|larger|smaller|\bx\b',cleaned):
            expected=2 if video_id=='geometry-area-rectangle' else 3
            if len(values)==expected:
                return (video_id,*sorted((str(Fraction(x)) for x in values),key=Fraction))
            if video_id=='geometry-volume-cube' and 'side' in cleaned and len(values)==1:
                return (video_id,*(str(Fraction(values[0])),)*3)
    if video_id=='counting-factorials':
        factorial=re.search(r'\b(\d+)\s*!',q)
        if factorial and len(numbers)==1:return ('factorial',int(factorial[1]))
    if video_id=='pattern-pmf-bfe65fc756d0':
        red=[int(n) for n in re.findall(r'\b(\d+)\s+(?:different\s+)?red\b',q)]
        blue=[int(n) for n in re.findall(r'\b(\d+)\s+(?:different\s+)?blue\b',q)]
        draw=re.search(r'\b(?:choose|draw)\s+(\d+)',q)
        if len(red)>=2 and blue:
            n=int(draw[1]) if draw else (red[-1]+blue[-1] if len(blue)>=2 else None)
            if n is not None:return ('hypergeometric-counts',red[0],blue[0],n,red[-1])
    if video_id.startswith('probability-first-success'):
        # Recognize the two concrete object vocabularies used in this family.
        # A change of objects or their order does not create new numeric inputs.
        counts={name:int(n) for n,name in re.findall(r'\b(\d+)\s+(red|blue|candies|candy|cockroaches)\b',q)}
        pair=None
        if 'red' in counts and 'blue' in counts and 'first red' in q:
            pair=(counts['red'],counts['blue'])
        elif ('candies' in counts or 'candy' in counts) and 'cockroaches' in counts and ('first candy' in q or 'candy is picked' in q):
            pair=(counts.get('candies',counts.get('candy')),counts['cockroaches'])
        if pair:
            if video_id=='probability-first-success-first':return ('first-draw',*pair)
            if re.search(r'no replacement|without replacement|not replaced',q):
                if video_id.endswith('-support'):return ('latest-finite-success',*pair)
                if video_id.endswith('-total'):return ('finite-distribution-total',*pair)
                target=re.search(r'(?:draw\s+|p\s*\(\s*|x\s*=\s*)(\d+)',q)
                if target:return ('finite-first-success',*pair,int(target[1]))
    if video_id in {'statistics-mean','statistics-median','statistics-mode','statistics-mean-absolute-deviation'}:
        lists=re.findall(r'\d+(?:\.\d+)?(?:\s*,\s*\d+(?:\.\d+)?){2,}',q.replace(' and ', ', '))
        if len(lists)==1:
            data=[str(Fraction(n)) for n in re.findall(r'\d+(?:\.\d+)?',lists[0])]
            return (video_id,*sorted(data,key=Fraction))
    if video_id in {'number-theory-gcf','number-theory-lcm'}:
        if len(numbers)==2:return (video_id,*sorted(map(int,numbers)))
    if video_id in {'number-place-value-whole-numbers','number-place-value-expanded-form'}:
        # Conservative for single-number prompts, including a differently worded task.
        if len(numbers)==1:return (video_id,int(numbers[0]))
    if video_id.startswith('number-rounding-'):
        rounded=re.search(r'round\s+([0-9]+(?:\.[0-9]+)?)\s+to the nearest\s+(\w+)',q)
        if rounded:
            place={'ten':'10','tens':'10','hundred':'100','hundreds':'100','thousand':'1000','thousands':'1000',
                   'tenth':'0.1','tenths':'0.1','hundredth':'0.01','hundredths':'0.01','thousandth':'0.001','thousandths':'0.001'}.get(rounded[2],rounded[2])
            return ('round',str(Fraction(rounded[1])),place)
    if video_id in {'fractions-compare','fractions-common-denominator'}:
        fractions=re.findall(r'\b(\d+)\s*/\s*(\d+)\b',q)
        if len(fractions)==2 and len(numbers)==4:
            return (video_id,*sorted((int(a),int(b)) for a,b in fractions))
    if video_id=='fractions-mixed-improper':
        mixed=re.search(r'\b(\d+)\s+(\d+)\s*/\s*(\d+)\b',q)
        if mixed and len(numbers)==3:return ('fraction-conversion',str(Fraction(mixed[1])+Fraction(int(mixed[2]),int(mixed[3]))))
        improper=re.search(r'\b(\d+)\s*/\s*(\d+)\b',q)
        if improper and len(numbers)==2:return ('fraction-conversion',str(Fraction(int(improper[1]),int(improper[2]))))
    if video_id=='decimal-fraction-conversion-to-decimal':
        fraction=re.search(r'\b(\d+)\s*/\s*(\d+)\b',q)
        if fraction and len(numbers)==2:return ('fraction-to-decimal',str(Fraction(int(fraction[1]),int(fraction[2]))))
    if video_id=='decimal-fraction-conversion-to-fraction':
        decimal=re.search(r'\b\d+\.\d+\b',q)
        if decimal and len(numbers)==2:return ('decimal-to-fraction',str(Fraction(decimal[0])))
    if video_id=='number-theory-modular-multiplication':
        factors=re.search(r'(\d+)\s*[×*]\s*(\d+)',q)
        modulus=re.search(r'\bmod(?:ulo)?\s*(\d+)',q)
        if factors and modulus and len(numbers)==3:
            return ('mod-multiply',*sorted(map(int,factors.groups())),int(modulus[1]))
    if video_id=='number-theory-modular-inverse':
        inverse=re.search(r'inverse of\s+(\d+)\s*\(?\s*mod(?:ulo)?\s*(\d+)',q)
        if inverse:return ('inverse',*map(int,inverse.groups()))
    if video_id=='number-theory-euler-totient':
        totient=re.search(r'[ϕφ]\s*\(\s*(\d+)\s*\)',q)
        if totient and len(numbers)==1 and '!' not in q:return ('totient',int(totient[1]))
    if video_id=='number-theory-euclidean-algorithm':
        fraction=re.search(r'(\d+)\s*/\s*(\d+)',q)
        if fraction:return ('reduce-fraction',*map(int,fraction.groups()))
    if video_id=='g1-u1-counting-backward':
        m=re.search(r'backward(?:s)? from (\d+) to (\d+)',q)
        if m:return ('count-backward',*m.groups(),'10' if 'by tens' in q else '1')
    if video_id=='enrichment-number-theory-1-modular-addition':
        addition=re.search(r'(\d+)\s*\+\s*(\d+)',q)
        modulus=re.search(r'\bmod(?:ulo)?\s*(\d+)',q)
        if addition and modulus:return ('mod-add',*sorted(map(int,addition.groups())),int(modulus[1]))
    if video_id=='g3-u1-equal-groups':
        m=re.search(r'(\d+)\s+groups? of\s+(\d+)',q)
        if m:return ('equal-groups',*sorted(map(int,m.groups())))
    if video_id=='g6-u1-simplifying-ratios' and 'ratio' in q:
        m=re.search(r'(\d+)\s*:\s*(\d+)',q)
        if m:return ('ratio',*m.groups())
        if len(numbers)==2:return ('ratio',*numbers)
    if video_id in {'enrichment-counting-and-probability-1-choosing-a-pair','enrichment-counting-and-probability-1-choose-three','counting-combinations'}:
        if len(numbers)==2:
            m=re.search(r'(\d+)\s*c\s*(\d+)|c\(\s*(\d+)\s*,\s*(\d+)\s*\)',q)
            if m:return ('combination',*(m.groups()[:2] if m.group(1) else m.groups()[2:]))
            n=re.search(r'from\s+(\d+)',q)
            k=re.search(r'(?:teams? of|committee of|committee|choose|chooses|select)\s+(\d+)',q)
            if n and k:return ('combination',n[1],k[1])
    return None


def plain(question):
    return re.sub(r'[^\w]+','',norm(raw_prompt(question)))


def example_collisions(doc,video_id,question):
    expected=signature(question,video_id)
    collisions=[]
    for file,w in doc['worksheets'].items():
        for qid,p in w['problems'].items():
            links=[link for link in p['video_links'] if link['video_id']==video_id]
            for index,variant in enumerate(p['question_text'].split('||')):
                if not any(l['variant_index'] in (None,index) for l in links):continue
                if plain(question)==plain(variant) or (expected is not None and signature(variant,video_id)==expected):
                    collisions.append({'worksheet':file,'question_id':qid,'variant_index':index,'question':variant})
    return collisions


def require_analogous_examples(doc,lessons):
    for lesson in lessons:
        hits=example_collisions(doc,lesson['video_id'],lesson['question'])
        if hits:raise ValueError(f'Example answers a linked worksheet question: {lesson["video_id"]}: {hits}')
