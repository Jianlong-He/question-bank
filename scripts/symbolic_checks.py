"""Small exact polynomial checker for authored lesson identities and equations."""
import ast
from fractions import Fraction


def polynomial(expression):
    tree=ast.parse(expression,mode='eval')
    def clean(p):return {k:v for k,v in p.items() if v}
    def add(a,b,sign=1):
        result=dict(a)
        for k,v in b.items():result[k]=result.get(k,Fraction(0))+sign*v
        return clean(result)
    def multiply(a,b):
        result={}
        for ka,va in a.items():
            for kb,vb in b.items():
                key=tuple(sorted(ka+kb));result[key]=result.get(key,Fraction(0))+va*vb
        return clean(result)
    def walk(n):
        if isinstance(n,ast.Expression):return walk(n.body)
        if isinstance(n,ast.Constant) and type(n.value) in (int,float):return clean({():Fraction(ast.get_source_segment(expression,n))})
        if isinstance(n,ast.Name):return {(n.id,):Fraction(1)}
        if isinstance(n,ast.UnaryOp) and isinstance(n.op,(ast.UAdd,ast.USub)):
            return {k:v*(-1 if isinstance(n.op,ast.USub) else 1) for k,v in walk(n.operand).items()}
        if isinstance(n,ast.Call) and isinstance(n.func,ast.Name) and n.func.id=='abs' and len(n.args)==1:
            p=walk(n.args[0]);assert set(p)<= {()}
            return clean({():abs(p.get((),Fraction(0)))})
        if isinstance(n,ast.BinOp):
            left,right=walk(n.left),walk(n.right)
            if isinstance(n.op,ast.Add):return add(left,right)
            if isinstance(n.op,ast.Sub):return add(left,right,-1)
            if isinstance(n.op,ast.Mult):return multiply(left,right)
            if isinstance(n.op,ast.Div):
                assert set(right)<= {()} and right.get((),0)!=0
                return clean({k:v/right[()] for k,v in left.items()})
            if isinstance(n.op,ast.Pow):
                assert set(right)<= {()}
                exponent=right.get((),Fraction(0));assert exponent.denominator==1 and 0<=exponent<=10
                result={():Fraction(1)}
                for _ in range(int(exponent)):result=multiply(result,left)
                return result
        raise ValueError(f'Unsupported authored polynomial: {expression}')
    return walk(tree)


def solve_linear(left,right,variable):
    a=polynomial(f'({left})-({right})')
    assert set(a)<={(),(variable,)} and a.get((variable,),0)!=0
    return -a.get((),Fraction(0))/a[(variable,)]
