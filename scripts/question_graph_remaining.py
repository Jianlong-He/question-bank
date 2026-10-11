"""Visuals for the 21 agreed remaining Grade 7–12 questions."""
import math
from collections import Counter
import numpy as np
from PIL import Image, ImageDraw

BLUE='#245a91'
ORANGE='#ad5626'
INK='#243342'
GRAY='#748494'
GREEN='#3f785b'


def add_remaining_specs(add):
    def a(sheet,qid,kind,title,expected,**kw):
        add(sheet,qid,'remaining_'+kind,title,expected,batch='remaining-visuals',**kw)
    a('G8U5W8',2,'volume-comparison','Cylinder and cone','same radius and height',volume=300)
    a('G8U5W9',6,'cylinder-net','Closed cylinder and its net','radius 4 cm and height 6 cm',radius=4,height=6)
    a('G8U7W9',10,'negative-scatter','Scatter plot','very close to a steep downward line',
      points=[[1,20],[2,18.2],[3,15.8],[4,14.2],[5,11.8],[6,10.1],[7,7.9],[8,6.2],[9,4.1]])
    a('G9U10W3',5,'boxplots','Compare the box plots','median 12 and box plot B has median 15',
      rows=[[6,9,12,16,20],[8,11,15,19,23]],labels=['A','B'],mode='median',
      note='Illustrative box plots with the stated medians; other positions are example values.')
    a('G9U10W3',6,'boxplots','Compare the box plots','IQR 4 and box plot B has IQR 9',
      rows=[[3,8,10,12,17],[1,5,9,14,21]],labels=['A','B'],mode='iqr',
      note='Illustrative box plots with the stated IQRs; other positions are example values.')
    a('G9U10W3',9,'boxplots','Box plot','much longer right whisker',
      rows=[[2,4,7,10,24]],labels=[''],mode='shape',
      note='Illustrative box plot matching the stated whisker lengths.')
    a('G9U10W3',10,'dotplots','Two dot plots','plot A has range 6 and plot B has range 14',
      rows=[[7,8,9,10,10,10,11,12,13],[3,5,8,9,10,11,12,15,17]])
    a('G9U8W3',5,'endpoint-domain','Graph with included endpoints','x = -5 to x = 7',lo=-5,hi=7)
    a('G9U8W3',6,'endpoint-range','Graph with an excluded upper endpoint','outputs from -2 up to 9',lo=-2,hi=9)
    a('G9U16W2',6,'reflections','Two successive reflections','distinct parallel lines',mode='parallel')
    a('G9U16W3',6,'reflections','Two successive reflections','perpendicular intersecting line',mode='perpendicular')
    a('G10U10W1',10,'slices','Solids with matching cross-sections','equal cross-sectional areas at every height')
    a('G10U11W3',1,'chord','Radius perpendicular to a chord','radius meets a chord at a right angle',length=None)
    a('G10U11W3',10,'chord','Radius perpendicular to a chord','chord is 16 units long',length=16)
    a('G11U13W3',8,'asymptote-crossing','A rational function and its asymptote','cross a horizontal asymptote')
    a('G12U6W2',4,'vectors','Add the two given vectors','(3 1) and (-2 5)',mode='addition',u=[3,1],v=[-2,5])
    a('G12U6W2',7,'vectors','Parallelogram rule','which diagonal represents u+v',mode='parallelogram',u=[4,0],v=[1,3])
    a('G12U10W6',4,'hole','Graph with a missing point','missing point with a finite two-sided limit',mode='example')
    a('G12U10W6',9,'hole','f(x) = (x² − 4)/(x − 2), x ≠ 2','f(x)=(x^2-4)/(x-2)',mode='specified')
    add('G7U9W4',9,'gap_pyramid','A slice parallel to the base','one-third the height',
        batch='remaining-visuals',square=False,halfway=False,cut_fraction=1/3)
    a('G7U9W5',9,'triangular-prism','Triangular prism','triangular base area of 18',area=18,height=7)


def render_remaining(s,Plot,font):
    kind=s['kind'].removeprefix('remaining_')
    def canvas(note=''):
        im=Image.new('RGB',(1280,980),'white');d=ImageDraw.Draw(im)
        d.text((640,40),s['title'],font=font(34),fill=INK,anchor='mt')
        d.text((640,930),note,font=font(23),fill=INK,anchor='mm')
        return im,d
    def label(d,p,text,color=INK,size=28):d.text(tuple(p),str(text),font=font(size),fill=color,anchor='mm')
    def line(d,pts,color=BLUE,width=4,dashed=False):
        pts=[tuple(p) for p in pts]
        if not dashed:d.line(pts,fill=color,width=width,joint='curve');return
        for a,b in zip(pts,pts[1:]):
            a=np.array(a);v=np.array(b)-a;n=np.linalg.norm(v)
            for t in np.arange(0,n,24):d.line([tuple(a+v*t/n),tuple(a+v*min(n,t+12)/n)],fill=color,width=width)
    def arrow(d,a,b,color=BLUE):
        a=np.array(a);b=np.array(b);u=(b-a)/np.linalg.norm(b-a);v=np.array([-u[1],u[0]])
        line(d,[a,b],color,5);d.polygon([tuple(b),tuple(b-20*u+9*v),tuple(b-20*u-9*v)],fill=color)
    def dot(d,p,color=BLUE):
        x,y=p;d.ellipse((x-7,y-7,x+7,y+7),fill=color)
    def dim(d,a,b,text,offset=(0,30),color=INK):
        a=np.array(a);b=np.array(b);u=(b-a)/np.linalg.norm(b-a);v=np.array([-u[1],u[0]])
        line(d,[a,b],color,2)
        for p in [a,b]:line(d,[p-9*v,p+9*v],color,2)
        label(d,(a+b)/2+offset,text,color,25)
    def cylinder(d,cx,top,bottom,rx,ry=38):
        d.rectangle((cx-rx,top,cx+rx,bottom),fill='#e8f0f7')
        d.ellipse((cx-rx,bottom-ry,cx+rx,bottom+ry),fill='#e8f0f7',outline=BLUE,width=3)
        line(d,[(cx-rx,top),(cx-rx,bottom)]);line(d,[(cx+rx,top),(cx+rx,bottom)])
        d.ellipse((cx-rx,top-ry,cx+rx,top+ry),fill='#f4f8fb',outline=BLUE,width=3)
    if kind=='volume-comparison':
        im,d=canvas('The two solids have the same radius r and perpendicular height h. Schematic view.')
        top,bottom,rx=300,700,155
        cylinder(d,350,top,bottom,rx)
        T=(925,top);O=(925,bottom)
        d.polygon([T,(925-rx,bottom),(925+rx,bottom)],fill='#e8f0f7')
        d.ellipse((925-rx,bottom-38,925+rx,bottom+38),fill='#e8f0f7',outline=BLUE,width=3)
        line(d,[(925-rx,bottom),T,(925+rx,bottom)])
        for cx in [350,925]:
            line(d,[(cx,bottom),(cx+rx,bottom)],ORANGE,4);label(d,(cx+rx/2,bottom+65),'r',ORANGE)
        dim(d,(565,top),(565,bottom),'h',offset=(30,0))
        line(d,[T,O],GRAY,3,True);label(d,(890,505),'h',GRAY)
        label(d,(350,205),'Cylinder');label(d,(925,205),'Cone')
        label(d,(350,820),'Volume = 300');label(d,(925,820),'Volume = ?')
        return im
    if kind=='cylinder-net':
        im,d=canvas('The net contains two circular ends and one rectangle. Diagram is schematic.')
        cylinder(d,265,410,650,110,32)
        line(d,[(265,410),(375,410)],ORANGE,3);label(d,(320,370),'r = 4 cm',ORANGE,24)
        dim(d,(420,410),(420,650),'6 cm',offset=(44,0))
        label(d,(265,760),'Closed cylinder')
        # The net itself is drawn to scale: width 2πr, height 6, circle radius 4.
        scale=19;r=4*scale;left=645;right=left+8*math.pi*scale;top=460;bottom=top+6*scale;cx=(left+right)/2
        d.rectangle((left,top,right,bottom),fill='#e8f0f7',outline=BLUE,width=4)
        for cy in [top-r,bottom+r]:
            d.ellipse((cx-r,cy-r,cx+r,cy+r),fill='#f4f8fb',outline=BLUE,width=4)
            line(d,[(cx,cy),(cx+r,cy)],ORANGE,3)
            label(d,(cx,cy-26),'4 cm',ORANGE,23)
        dim(d,(right+25,top),(right+25,bottom),'6 cm',offset=(42,0))
        label(d,(cx,top+48),'Width = circumference of an end',size=23)
        label(d,(cx,820),'Net of the closed cylinder')
        return im
    if kind=='negative-scatter':
        p=Plot(s['title'],[0,10,0,22],ticks=[1,2],note='Illustrative data matching the pattern described in the question.')
        for pt in s['points']:p.point(*pt)
        return p.finish()
    if kind=='boxplots':
        im,d=canvas(s['note']);x=lambda v:155+v/26*990
        ys=[490] if len(s['rows'])==1 else [360,650]
        for values,name,y in zip(s['rows'],s['labels'],ys):
            low,q1,med,q3,high=values
            line(d,[(x(low),y),(x(high),y)],GRAY,3)
            for val in [low,high]:line(d,[(x(val),y-25),(x(val),y+25)],BLUE,3)
            d.rectangle((x(q1),y-55,x(q3),y+55),fill='#e8f0f7',outline=BLUE,width=4)
            line(d,[(x(med),y-55),(x(med),y+55)],ORANGE,5)
            label(d,(95,y),name,size=32)
            if s['mode']=='median':label(d,(x(med),y-98),f'Median = {med}',ORANGE,25)
            if s['mode']=='iqr':dim(d,(x(q1),y+85),(x(q3),y+85),f'IQR = {q3-q1}',offset=(0,35),color=ORANGE)
        line(d,[(x(0),825),(x(26),825)],INK,3)
        for n in range(0,27,2):line(d,[(x(n),816),(x(n),834)],INK,2);label(d,(x(n),861),n,size=24)
        label(d,(650,170),'Both plots use the same number scale.' if len(ys)==2 else 'Read the relative lengths of the two whiskers.',size=25)
        return im
    if kind=='dotplots':
        im,d=canvas('Illustrative data: both medians are 10; the ranges match those stated in the question.')
        x=lambda v:180+(v-2)/16*960
        for name,values,y in zip(['A','B'],s['rows'],[390,730]):
            label(d,(100,y-65),name,size=32);line(d,[(x(2),y),(x(18),y)],INK,3)
            for n in range(2,19,2):line(d,[(x(n),y-8),(x(n),y+8)],INK,2);label(d,(x(n),y+35),n,size=23)
            for val,count in Counter(values).items():
                for i in range(count):dot(d,(x(val),y-30-27*i))
            label(d,(660,y+95),f'Given range: {max(values)-min(values)}',size=26)
        return im
    if kind=='endpoint-domain':
        p=Plot(s['title'],[-7,9,-3,5],ticks=[1,1],note='Illustrative curve defined only for −5 ≤ x ≤ 7; both endpoints are filled.')
        fn=lambda x:1+1.5*math.sin((x+5)*math.pi/12)
        p.curve(fn,lo=-5,hi=7);p.point(-5,fn(-5));p.point(7,fn(7));return p.finish()
    if kind=='endpoint-range':
        p=Plot(s['title'],[-1,5,-4,11],ticks=[1,1],note='Illustrative graph with outputs −2 ≤ y < 9. The upper endpoint is open.')
        p.line([(0,-2),(4,9)]);p.point(0,-2);p.point(4,9,closed=False);return p.finish()
    if kind=='reflections':
        parallel=s['mode']=='parallel'
        p=Plot(s['title'],[-6,7,-1,5] if parallel else [-4,4,-4,4],ticks=[1,1],equal_aspect=True,
          note='Illustrative example. Blue: original. Orange: after first reflection. Green: after second.')
        if parallel:
            original=[(-4,1),(-3,1),(-4,3)]
            first=[(-2-x,y) for x,y in original];second=[(6-x,y) for x,y in first]
            for x,txt in [(-1,'First: x = −1'),(3,'Second: x = 3')]:
                p.line([(x,-1),(x,5)],GRAY,3,True);label(p.pen,p.xy(x,4.4),txt,GRAY,23)
        else:
            original=[(1,1),(3,1),(1,3)];first=[(x,-y) for x,y in original];second=[(-x,y) for x,y in first]
            label(p.pen,p.xy(2.3,0.35),'First: x-axis',GRAY,23)
            label(p.pen,p.xy(-1.5,3.6),'Second: y-axis',GRAY,23)
        for pts,col in zip([original,first,second],[BLUE,ORANGE,GREEN]):p.line(pts+[pts[0]],col,5)
        return p.finish()
    if kind=='slices':
        im,d=canvas('At every corresponding height, the two cross-sectional areas are equal.')
        # Two prisms share congruent horizontal bases and height; one is sheared.
        for origin,shift,name in [(np.array([200,775]),0,'Solid A'),(np.array([730,775]),105,'Solid B')]:
            base=np.array([[0,0],[210,0],[290,-65],[80,-65]])+origin
            def section(t):return base+np.array([shift*t,-470*t])
            top=section(1)
            for i in range(4):line(d,[base[i],top[i]],GRAY,3,dashed=i==3)
            line(d,list(base)+[base[0]],BLUE,3);line(d,list(top)+[top[0]],BLUE,3)
            for t in [0.25,0.5,0.75]:
                pts=section(t);d.polygon([tuple(p) for p in pts],fill='#f4e4d7');line(d,list(pts)+[pts[0]],ORANGE,3)
            label(d,(origin[0]+145,180),name)
        dim(d,(145,305),(145,775),'h',offset=(-30,0));dim(d,(1165,305),(1165,775),'h',offset=(30,0))
        label(d,(640,855),'Same perpendicular height h',size=26)
        return im
    if kind=='chord':
        im,d=canvas('OT is a radius and OT is perpendicular to chord AB at M.')
        O=np.array([640,450]);r=290;offset=140;half=math.sqrt(r*r-offset*offset)
        A=O+[-half,offset];B=O+[half,offset];M=O+[0,offset];T=O+[0,r]
        d.ellipse((350,160,930,740),outline=BLUE,width=4)
        line(d,[A,B],BLUE,5);line(d,[O,T],ORANGE,4)
        line(d,[M+[0,-23],M+[23,-23],M+[23,0]],INK,3)
        for pt,txt,off in [(O,'O',[-25,-25]),(A,'A',[-32,0]),(B,'B',[32,0]),(M,'M',[-25,30]),(T,'T',[0,35])]:label(d,pt+off,txt)
        dot(d,O)
        if s['length']:
            dim(d,(A[0],815),(B[0],815),'AB = 16',offset=(0,32))
            label(d,(O[0]-half/2,M[1]-35),'?',ORANGE);label(d,(O[0]+half/2,M[1]-35),'?',ORANGE)
        return im
    if kind=='asymptote-crossing':
        p=Plot(s['title'],[-8,8,-0.75,0.75],ticks=[2,0.25],note='Example: f(x) = x/(x² + 1). Dashed orange: horizontal asymptote y = 0.')
        p.line([(-8,0),(8,0)],ORANGE,4,True);p.curve(lambda x:x/(x*x+1));return p.finish()
    if kind=='vectors':
        if s['mode']=='addition':
            p=Plot(s['title'],[-3,5,-1,8],ticks=[1,1],equal_aspect=True,note='The vectors are shown head-to-tail. Find the combined displacement.')
            u=np.array(s['u']);v=np.array(s['v']);end=u+v
            arrow(p.pen,p.xy(0,0),p.xy(*u),BLUE);arrow(p.pen,p.xy(*u),p.xy(*end),ORANGE)
            label(p.pen,p.xy(1.5,-0.45),'(3, 1)',BLUE,25);label(p.pen,p.xy(3.1,4),'(−2, 5)',ORANGE,25)
        else:
            im,d=canvas('The vectors share the tail O. Decide which diagonal represents u + v.')
            O=np.array([280,750]);U=np.array([840,750]);V=np.array([420,330]);W=U+V-O
            arrow(d,O,U,BLUE);arrow(d,O,V,ORANGE)
            line(d,[U,W,V],GRAY,3,True);line(d,[O,W],GREEN,3);line(d,[U,V],GRAY,3)
            for p,txt,off in [(O,'O',[-30,30]),(U,'A',[25,30]),(V,'B',[-25,-30]),(W,'C',[25,-30])]:label(d,p+off,txt)
            label(d,(O+U)/2+[0,40],'u',BLUE);label(d,(O+V)/2+[-40,0],'v',ORANGE)
            return im
        return p.finish()
    if kind=='hole':
        p=Plot(s['title'],[-3,6,-2,9],ticks=[1,1],note='The open circle marks an excluded point.' if s['mode']=='specified' else 'Illustrative example: both sides approach the same finite height at the missing point.')
        p.curve(lambda x:x+2);p.point(2,4,closed=False);return p.finish()
    if kind=='triangular-prism':
        im,d=canvas('Schematic prism. The distance between the triangular bases is perpendicular to both bases.')
        # A right triangular prism, projected with the prism axis oblique on the page.
        front=np.array([[260,690],[650,690],[440,315]]);shift=np.array([340,-140]);back=front+shift
        line(d,[back[0],back[1]],GRAY,3,dashed=True)
        line(d,[back[2],back[0]],GRAY,3,dashed=True)
        line(d,[back[1],back[2]],BLUE,4)
        for a,b in zip(front,back):line(d,[a,b],BLUE,4,dashed=tuple(a)==tuple(front[0]))
        d.polygon([tuple(p) for p in front],fill='#e1ecf6');line(d,list(front)+[front[0]],BLUE,5)
        label(d,(450,580),'Base area',size=28);label(d,(450,620),'18',size=34)
        dim(d,front[1]+[40,55],back[1]+[40,55],'7',offset=(20,35))
        return im
    raise ValueError(kind)
