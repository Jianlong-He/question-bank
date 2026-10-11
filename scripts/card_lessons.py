"""Equation-card renderer for authored, checked worked examples."""
import ast
import copy
from fractions import Fraction
import operator
import re
from functools import lru_cache
from symbolic_checks import polynomial, solve_linear

import generate_sample_videos as video
from generate_sample_videos import text, centered, wrap, TEAL, INK, MUTED, LIGHT


SUPERSCRIPT_CHARS='⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺ᵃᵇᵉᵏᵗ'
SUPERSCRIPT_MAP=str.maketrans(SUPERSCRIPT_CHARS,'0123456789-+abekt')


def math_runs(value,size):
    """Render superscripts using ordinary glyphs; Arial lacks some Unicode powers."""
    return [(part.translate(SUPERSCRIPT_MAP) if raised else part,
             video.font(round(size*.62) if raised else size,True),raised)
            for part in re.findall(f'[{SUPERSCRIPT_CHARS}]+|[^{SUPERSCRIPT_CHARS}]+',value)
            for raised in [part[0] in SUPERSCRIPT_CHARS]]


def math_width(d,value,size):
    return sum(d.textlength(part,font=font) for part,font,raised in math_runs(value,size))


def centered_math(d,y,value,size,color):
    if not any(c in SUPERSCRIPT_CHARS for c in value):
        centered(d,y,value,size,color,True)
        return
    runs=math_runs(value,size)
    x=(video.W-math_width(d,value,size))/2
    for part,font,raised in runs:
        d.text((x,y+size*(.42 if raised else .9)),part,font=font,fill=color,anchor='ls')
        x+=d.textlength(part,font=font)


@lru_cache(maxsize=None)
def has_card_glyph(char):
    font=video.font(60,True)
    mask,missing=font.getmask(char),font.getmask('\uffff')
    return not (mask.size==missing.size and bytes(mask)==bytes(missing))


def exact(expression):
    """Evaluate only authored numeric arithmetic; decimal literals stay exact."""
    tree=ast.parse(expression,mode='eval')
    def walk(node):
        if isinstance(node,ast.Expression):return walk(node.body)
        if isinstance(node,ast.Constant) and type(node.value) in (int,float):
            return Fraction(ast.get_source_segment(expression,node))
        if isinstance(node,ast.UnaryOp) and isinstance(node.op,(ast.USub,ast.UAdd)):
            return -walk(node.operand) if isinstance(node.op,ast.USub) else walk(node.operand)
        if isinstance(node,ast.BinOp):
            operations={ast.Add:operator.add,ast.Sub:operator.sub,ast.Mult:operator.mul,ast.Div:operator.truediv,ast.Pow:operator.pow,ast.Mod:operator.mod}
            if type(node.op) in operations:return operations[type(node.op)](walk(node.left),walk(node.right))
        raise ValueError(f'Unsupported arithmetic: {expression}')
    return walk(tree)


def draw_card(spec,d,scene,p):
    lines=spec['displays'][scene].split('\n')
    d.rounded_rectangle((145,360,1775,840),radius=35,fill='white')
    size=76 if len(lines)<3 else 59
    while max(math_width(d,s,size) for s in lines)>1490 and size>30:size-=2
    gap=size+38
    start=600-(len(lines)*gap)/2
    for i,line in enumerate(lines):
        centered_math(d,start+i*gap,line,size,TEAL if i==len(lines)-1 else INK)
    if scene==4:centered(d,915,'Check the method, then try your worksheet.',32,MUTED)


def make_lessons(specs,doc):
    result=[]
    references={}
    for file,w in doc['worksheets'].items():
        for qid,p in w['problems'].items():
            for link in p['video_links']:
                references.setdefault(link['video_id'],[]).append((file,qid,w))
    for spec in specs:
        vid=spec['video_id']
        for char in set(''.join(spec['displays'])):
            assert char.isspace() or char in SUPERSCRIPT_CHARS or has_card_glyph(char),(vid,'Missing display glyph',char)
        assert vid in doc['videos'],vid
        assert spec.get('expression') or spec.get('equalities') or spec.get('identities') or spec.get('linear_equation'),f'No math verification for {vid}'
        if spec.get('expression'):assert exact(spec['expression'])==Fraction(spec['answer_value']),vid
        for left,right in spec.get('equalities',[]):assert exact(left)==exact(right),(vid,left,right)
        for left,right in spec.get('identities',[]):assert polynomial(left)==polynomial(right),(vid,left,right)
        if spec.get('linear_equation'):
            left,right,variable,answer=spec['linear_equation']
            assert solve_linear(left,right,variable)==Fraction(answer),vid
        refs=references.get(vid,[])
        if not refs:
            # Removing an unsuitable last mapping must not remove completed media.
            # Keep the rendered record/asset in the library; it has no active
            # worksheet lesson to generate until a suitable reference is reviewed.
            record=doc['videos'][vid]
            assert record['production_status']=='rendered' and record['assets'].get('mp4'),f'Unlinked unrendered lesson: {vid}'
            continue
        refs.sort(key=lambda r:(r[2]['curriculum']['kind']!='grade',r[2]['curriculum'].get('grade',99),r[0],int(r[1])))
        if spec.get('source_ref'):
            refs=[r for r in refs if (r[0],r[1])==tuple(spec['source_ref'])]
            assert refs,f'Source reference is not linked: {vid}'
        file,qid,w=refs[0];cur=w['curriculum']
        folder=f'Grade {cur["grade"]}/Unit {cur["unit"]}' if cur['kind']=='grade' else f'enrichment/{cur["track"]}/{cur["topic"]}'
        lesson={
            'video_id':vid,'slug':vid,'title':doc['videos'][vid]['title'],
            'badge':'WORKED METHOD','topic':spec['topic'],'output_dir':folder,
            'source':file,'ids':[qid],'draw_key':vid,
            'question':spec['question'],'answer':spec['answer'],
            'scenes':spec['scenes'],'static_scenes':True,
        }
        video.DRAW[vid]=lambda d,scene,p,spec=spec:draw_card(spec,d,scene,p)
        result.append(lesson)
    return result


def spec(video_id,topic,question,answer,expression,answer_value,opening,steps,equalities=()):
    assert len(steps)==4,video_id
    return {'video_id':video_id,'topic':topic,'question':question,'answer':answer,
            'expression':expression,'answer_value':answer_value,
            'scenes':[('THE QUESTION','Try a similar example',opening)]+[(label,heading,speech) for label,heading,display,speech in steps],
            'displays':[question]+[display for label,heading,display,speech in steps],
            'equalities':list(equalities)}
