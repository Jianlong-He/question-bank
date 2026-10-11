"""Explicit Grade 7–12 diagram recipes; no question or answer cells are changed."""
import math
from fractions import Fraction
import numpy as np
from PIL import Image, ImageDraw

BLUE='#245a91'
ORANGE='#ad5626'
INK='#243342'
GRAY='#6a7580'


def add_specs(add):
    def a(sheet,qid,kind,title,expected,**kw):
        add(sheet,qid,'extra_'+kind,title,expected,batch='coverage-expansion',**kw)

    for sheet,qid,pos,neg,pairs,expected in [
        ('G7U3W1',6,4,9,0,'4 positive tiles and 9 negative'),
        ('G7U3W1Rev',1,5,11,0,'5 positive tiles and 11 negative'),
        ('G7U3W2',6,4,7,2,'7 negative tiles, 4 positive tiles, and 2 zero pairs'),
        ('G7U3W2Rev',2,3,8,2,'8 negative tiles, 3 positive tiles, and 2 zero pairs'),
        ('G7U3W3',6,10,3,4,'10 positive tiles, 3 negative tiles, and 4 zero pairs'),
        ('G7U3W3Rev',2,12,4,3,'12 positive tiles, 4 negative tiles, and 3 zero pairs')]:
        a(sheet,qid,'tiles','Integer tiles',expected,positive=pos,negative=neg,pairs=pairs)
    for sheet,qid,key,label,unknown,expected in [
        ('G7U8W5',1,'0.5 cm on the drawing represents 7 m in real life.','Hallway on drawing: 2.8 cm','Real hallway length: ?','2.8 cm'),
        ('G7U8W5HW',1,'0.5 cm on the drawing represents 6 m in real life.','Hallway on drawing: 3.5 cm','Real hallway length: ?','3.5 cm'),
        ('G7U8W5Rev',1,'2 cm on the drawing represents 25 m in real life.','Real road length: 125 m','Length on drawing: ?','125 m')]:
        a(sheet,qid,'scale','Scale drawing',expected,key=key,label=label,unknown=unknown)
    a('G7U9W1',7,'angles','Two supplementary angles','(3x + 10)',angle=115,mode='supplementary',labels=['(3x + 10)°','(2x - 5)°'])
    a('G7U9W1HW',4,'angles','Two supplementary angles','(2x + 20)',angle=90,mode='supplementary',labels=['(2x + 20)°','(3x - 15)°'])
    a('G7U9W1Rev',4,'angles','Two intersecting lines','(5x - 20)',angle=105,mode='vertical',labels=['(5x - 20)°','105°'])
    a('G7U9W3',10,'ring','Circular washer','outer radius of 6 and an inner radius of 4',outer=6,inner=4)
    a('G7U9W3Rev',5,'ring','Circular washer','outer radius of 7 and an inner radius of 3',outer=7,inner=3)

    for sheet,c1,c2 in [('G8U4W2',2,8),('G8U4W2HW',3,9)]:
        a(sheet,2,'system','Two linear equations',f'y = x + {c1}',bounds=[-2,6,-3,13],ticks=[1,2],
          lines=[[1,c1],[-2,c2]],note=f'Blue: y = x + {c1}. Orange: y = -2x + {c2}.')
    for sheet,qid in [('G8U4W5',9),('G8U4W5Rev',4)]:
        a(sheet,qid,'system_choices','Three systems','Lines crossing at 90 degrees')
    for sheet,qid,point,operation,expected in [
        ('G8U6W1',2,[3,5],'Translate 2 units left and 4 units up.','P(3,5)'),
        ('G8U6W1',5,[4,-2],'Reflect across the x-axis.','A(4, -2)'),
        ('G8U6W1',9,[2,3],'Rotate 180° about the origin.','B(2,3)'),
        ('G8U6W1HW',2,[2,6],'Translate 3 units left and 2 units up.','P(2,6)'),
        ('G8U6W1HW',4,[5,-3],'Reflect across the x-axis.','A(5, -3)'),
        ('G8U6W1HW',5,[3,4],'Rotate 180° about the origin.','B(3,4)'),
        ('G8U6W1Rev',5,[-3,6],'Translate 4 units right and 2 units down.','P(-3, 6)')]:
        a(sheet,qid,'scaffold','Given point',expected,point=point,operation=operation,bounds=[-10,10,-10,10],ticks=[2,2])

    for sheet,qid in [('G9U8W7',6),('G9U8W7HW',5)]:
        a(sheet,qid,'inverse','A function and its inverse','reflections across which line',bounds=[-5,5,-5,5],ticks=[1,1])
    a('G9U8W7Rev',5,'power','f(x) = x²','x^2 on all real numbers',power=2,bounds=[-4,4,-1,10],ticks=[1,1])
    a('G9U14W2',9,'exponential','Exponential graph','(0, 6) and (1, 18)',base=3,coefficient=6,bounds=[-2,2,-2,60],ticks=[0.5,10],points=[[0,6],[1,18]])
    a('G9U14W3Rev',2,'exponential','y = (1/3)^x','(1/3)^x',base=1/3,coefficient=1,bounds=[-2,3,-1,10],ticks=[1,1])
    a('G9U14W3Rev',3,'exponential','y = 6^x','6^x',base=6,coefficient=1,bounds=[-2,2,-2,40],ticks=[0.5,5])
    for qid,mode,expected in [(1,'translation','5 units right'),(2,'rotation','90 degrees'),(3,'reflection','across the y-axis'),(4,'dilation','twice its original distance')]:
        a('G9U15W1Rev',qid,'transform','Figure A and figure B',expected,mode=mode,bounds=[-5,10,-5,8],ticks=[1,1])
    a('G9U17W2',5,'congruence','Two triangles: given markings','AB = DE, BC = EF, and angle B = angle E',criterion='SAS')
    a('G9U17W2',6,'congruence','Two triangles: given markings','angle A = angle D, angle B = angle E, and AB = DE',criterion='ASA')

    for sheet,qid,adj,opp,hyp,expected in [
        ('G10U9W1',2,6,8,'?','legs 6 and 8'),('G10U9W1HW',1,9,12,'?','legs 9 and 12'),
        ('G10U9W1Rev',1,7,24,'?','legs 7 and 24'),
        ('G10U9W3',4,4,3,5,'opposite side 3 adjacent side 4 and hypotenuse 5'),
        ('G10U9W3HW',1,12,5,13,'opposite side 5 adjacent side 12 and hypotenuse 13'),
        ('G10U9W3Rev',2,15,8,17,'opposite side 8 adjacent side 15 and hypotenuse 17')]:
        a(sheet,qid,'triangle','Right triangle',expected,adjacent=adj,opposite=opp,hypotenuse=hyp,theta=('W3' in sheet))
    for sheet,qid,r,theta,label,expected in [
        ('G10U11W1',4,4,math.pi/2,'π/2','r=4 and theta=pi/2'),
        ('G10U11W1HW',2,6,math.pi/3,'π/3','r=6 and theta=pi/3'),
        ('G10U11W1Rev',5,8,math.pi/4,'45°','45-degree sector')]:
        a(sheet,qid,'sector','Circular sector',expected,radius=r,theta=theta,angle_label=label)
    for sheet,qid,arc in [('G10U11W2',2,100),('G10U11W2HW',1,80),('G10U11W2Rev',2,150)]:
        a(sheet,qid,'inscribed','Inscribed angle',f'{arc}-degree arc',arc=arc)
    a('G10U11W3',6,'tangent','Radius and tangent segment','length 12 and the radius to its endpoint is 5',radius=5,tangent=12)
    a('G10U11W3HW',3,'tangent','Radius and tangent segment','length 24 and the radius to its endpoint is 7',radius=7,tangent=24)
    a('G10U12W2',3,'parabola_focus','Focus and directrix','focus (0, 2)',p=2,bounds=[-8,8,-4,10],ticks=[2,2],directrix=True)
    a('G10U12W2HW',1,'parabola_focus','Focus and directrix','focus (0, 3)',p=3,bounds=[-10,10,-5,12],ticks=[2,2],directrix=True)
    a('G10U12W2Rev',5,'parabola_focus','Given vertex and focus','focus (0, 5)',p=5,bounds=[-8,8,-2,10],ticks=[2,2],directrix=False)

    for sheet,qid,fn,A,B,D,expected in [
        ('G11U8W4',2,'sin',1,1,0,'period of y=sin(x)'),
        ('G11U8W4HW',2,'cos',1,1,0,'period of y = cos(x)'),
        ('G11U8W4Rev',2,'cos',1,1,0,'amplitude of y = cos(x)'),
        ('G11U8W4',4,'tan',1,1,0,'period of y=tan(x)'),
        ('G11U8W4HW',3,'tan',1,1,0,'period of y = tan(x)'),
        ('G11U8W5',10,'sin',3,0.5,-2,'3sin(0.5x)-2'),
        ('G11U8W5HW',1,'sin',5,1,-3,'5sin(x) - 3'),
        ('G11U8W5Rev',1,'cos',-2,1,6,'-2cos(x) + 6')]:
        a(sheet,qid,'trig','Trigonometric graph',expected,function=fn,A=A,B=B,D=D,
          note='Angles on the horizontal axis are measured in radians.')
    a('G11U6W1',9,'function_transform','Two quadratic graphs','y=-(x+2)^2+1',function='quadratic',h=-2,k=1,factor=-1,bounds=[-7,5,-15,15],ticks=[1,3],note='Blue: y = x². Orange: y = -(x + 2)² + 1.')
    a('G11U6W1Rev',4,'function_transform','Two absolute-value graphs','|x - 4| + 2',function='absolute',h=4,k=2,factor=1,bounds=[-4,10,-1,10],ticks=[1,1],note='Blue: y = |x|. Orange: y = |x - 4| + 2.')
    a('G11U6W1Rev',5,'function_transform','Two quadratic graphs','x^2 - 9',function='quadratic',h=0,k=-9,factor=1,bounds=[-5,5,-11,16],ticks=[1,3],note='Blue: y = x². Orange: y = x² - 9.')

    for sheet,qid,power,expected in [('G12U1W3',3,2,'f(x)=x^2'),('G12U1W3HW',3,3,'f(x) = x^3'),('G12U1W3HW',5,2,'right branch of the parabola')]:
        a(sheet,qid,'power',f'f(x) = x{chr(178) if power==2 else chr(179)}',expected,power=power,bounds=[-4,4,-10,10] if power==3 else [-4,4,-1,10],ticks=[1,2])
    for sheet,qid,h,k,rx,ry,expected in [
        ('G12U5W1',3,2,-1,5,3,'(x-2)^2/25+(y+1)^2/9'),
        ('G12U5W1',4,0,0,5,3,'x^2/25+y^2/9'),
        ('G12U5W1HW',3,0,0,6,4,'x^2/36 + y^2/16'),
        ('G12U5W1Rev',2,0,0,3,5,'x^2/9 + y^2/25')]:
        a(sheet,qid,'ellipse','Ellipse',expected,h=h,k=k,rx=rx,ry=ry,bounds=[h-rx-2,h+rx+2,k-ry-2,k+ry+2],ticks=[1,1])
    for sheet,qid,a0,b0,vertical,asymptotes,expected in [
        ('G12U5W2',4,3,4,False,False,'x^2/9-y^2/16'),
        ('G12U5W2',5,3,4,False,True,'x^2/9-y^2/16'),
        ('G12U5W2HW',4,4,3,False,False,'x^2/16 - y^2/9'),
        ('G12U5W2Rev',2,3,2,True,False,'y^2/9 - x^2/4')]:
        a(sheet,qid,'hyperbola','Hyperbola',expected,a=a0,b=b0,vertical=vertical,asymptotes=asymptotes,bounds=[-10,10,-10,10],ticks=[2,2])


def pi_label(x):
    value=Fraction(float(x/math.pi)).limit_denominator(12)
    if value==0:return '0'
    sign='−' if value<0 else '';value=abs(value)
    return sign+('' if value.numerator==1 else str(value.numerator))+'π'+('' if value.denominator==1 else '/'+str(value.denominator))


def render_extra(s,Plot,font):
    kind=s['kind'].removeprefix('extra_')
    def canvas(note=''):
        im=Image.new('RGB',(1280,980),'white');d=ImageDraw.Draw(im)
        d.text((640,40),s['title'],font=font(35),fill=INK,anchor='mt')
        d.text((640,930),note,font=font(24),fill=INK,anchor='mm')
        return im,d
    def arc(d,c,r,start,end,color=BLUE,width=4):
        points=[(c[0]+r*math.cos(t),c[1]-r*math.sin(t)) for t in np.linspace(start,end,250)]
        d.line(points,fill=color,width=width)
    def label(d,xy,text,color=INK,size=30):d.text(xy,str(text),font=font(size),fill=color,anchor='mm')
    def circle_point(c,r,t):return (c[0]+r*math.cos(t),c[1]-r*math.sin(t))

    if kind=='tiles':
        im,d=canvas('Each blue + tile represents +1. Each orange − tile represents −1.')
        def tile(x,y,positive):
            color=BLUE if positive else ORANGE
            d.rounded_rectangle((x,y,x+64,y+64),radius=7,fill='#edf3f8' if positive else '#fcf0e8',outline=color,width=3)
            label(d,(x+32,y+32),'+' if positive else '−',color,36)
        for count,positive,y,title in [(s['positive'],True,200,'Positive tiles'),(s['negative'],False,410,'Negative tiles')]:
            d.text((100,y-60),title,font=font(30),fill=INK)
            for i in range(count):tile(100+i*85,y,positive)
        if s['pairs']:
            d.text((100,590),'Zero pairs',font=font(30),fill=INK)
            for i in range(s['pairs']):
                x=100+220*i;d.rounded_rectangle((x-10,650,x+150,734),radius=10,outline=GRAY,width=2)
                tile(x,660,True);tile(x+76,660,False)
        return im
    if kind=='scale':
        im,d=canvas('Schematic only; use the written scale, not the size of this image.')
        label(d,(640,160),s['key'],size=30)
        d.rectangle((250,350,1030,560),fill='#eef4fa',outline=BLUE,width=5)
        d.line((250,620,1030,620),fill=INK,width=3)
        for x in [250,1030]:d.line((x,600,x,640),fill=INK,width=3)
        label(d,(640,285),s['label']);label(d,(640,725),s['unknown'])
        return im
    if kind=='angles':
        im,d=canvas('Diagram is schematic; use the given angle labels.')
        c=(640,490);theta=math.radians(s['angle']);r=350
        ends=[0,math.pi,theta]+([theta+math.pi] if s['mode']=='vertical' else [])
        for t in ends:d.line((*c,*circle_point(c,r,t)),fill=BLUE,width=5)
        arc(d,c,95,0,theta)
        label(d,circle_point(c,205,theta/2),s['labels'][0])
        if s['mode']=='vertical':
            arc(d,c,95,math.pi,math.pi+theta);label(d,circle_point(c,205,math.pi+theta/2),s['labels'][1])
        else:
            arc(d,c,125,theta,math.pi,color=ORANGE);label(d,circle_point(c,245,(theta+math.pi)/2),s['labels'][1])
        return im
    if kind=='ring':
        im,d=canvas();c=(640,485);r=310;ri=r*s['inner']/s['outer']
        d.ellipse((c[0]-r,c[1]-r,c[0]+r,c[1]+r),fill='#dce8f2',outline=BLUE,width=5)
        d.ellipse((c[0]-ri,c[1]-ri,c[0]+ri,c[1]+ri),fill='white',outline=BLUE,width=4)
        d.line((*c,c[0]+r,c[1]),fill=ORANGE,width=4)
        d.line((*c,c[0],c[1]-ri),fill=BLUE,width=4)
        label(d,(c[0]+r/2,c[1]+40),f'Outer radius {s["outer"]}',size=26)
        label(d,(c[0]-120,c[1]-ri/2),f'Inner radius {s["inner"]}',size=26)
        return im
    if kind=='triangle':
        im,d=canvas('Only the given side lengths are labeled.')
        adj,opp=s['adjacent'],s['opposite'];scale=min(800/adj,570/opp)
        left=(640-adj*scale/2,780);right=(left[0]+adj*scale,780);top=(right[0],780-opp*scale)
        d.line([left,right,top,left],fill=BLUE,width=6)
        d.line([(right[0]-24,right[1]),(right[0]-24,right[1]-24),(right[0],right[1]-24)],fill=INK,width=3)
        label(d,((left[0]+right[0])/2,825),adj)
        label(d,(right[0]+65,(right[1]+top[1])/2),opp)
        mid=((left[0]+top[0])/2-45,(left[1]+top[1])/2-20);label(d,mid,s['hypotenuse'])
        if s['theta']:
            theta=math.atan2(opp,adj);arc(d,left,75,0,theta)
            label(d,circle_point(left,110,theta/2),'θ')
        return im
    if kind=='sector':
        im,d=canvas();c=(640,510);r=300;theta=s['theta']
        d.ellipse((340,210,940,810),outline='#bdc7d1',width=3)
        pts=[c]+[circle_point(c,r,t) for t in np.linspace(0,theta,200)]+[c]
        d.polygon(pts,fill='#e0ecf6');d.line(pts,fill=BLUE,width=5)
        arc(d,c,75,0,theta,color=ORANGE)
        label(d,circle_point(c,130,theta/2),s['angle_label'],size=29)
        label(d,(795,550),f'r = {s["radius"]}',size=29)
        return im
    if kind=='inscribed':
        im,d=canvas('The highlighted arc is intercepted by the angle at P.')
        c=(580,490);r=295;half=math.radians(s['arc']/2)
        d.ellipse((c[0]-r,c[1]-r,c[0]+r,c[1]+r),outline=BLUE,width=4)
        A=circle_point(c,r,half);B=circle_point(c,r,-half);P=circle_point(c,r,math.pi)
        d.line([A,P,B],fill=BLUE,width=5);arc(d,c,r,-half,half,color=ORANGE,width=8)
        for xy,name,offset in [(A,'A',(20,-20)),(B,'B',(20,20)),(P,'P',(-30,0))]:label(d,(xy[0]+offset[0],xy[1]+offset[1]),name)
        label(d,(P[0]+100,P[1]),'?');label(d,(985,490),f'{s["arc"]}°',ORANGE)
        return im
    if kind=='tangent':
        im,d=canvas('OT is a radius; PT is tangent at T. Find OP.')
        r=s['radius'];t=s['tangent'];dist=math.hypot(r,t)
        scale=min(620/(dist+r),260/r);origin=(370,560)
        xy=lambda x,y:(origin[0]+x*scale,origin[1]-y*scale)
        O=xy(0,0);P=xy(dist,0);T=xy(r*r/dist,r*t/dist)
        d.ellipse((O[0]-r*scale,O[1]-r*scale,O[0]+r*scale,O[1]+r*scale),outline=BLUE,width=4)
        d.line([O,T,P,O],fill=BLUE,width=4)
        # A right-angle mark uses normalized OT and PT directions.
        u=np.array(O)-np.array(T);u=u/np.linalg.norm(u)*22
        v=np.array(P)-np.array(T);v=v/np.linalg.norm(v)*22
        d.line([tuple(np.array(T)+u),tuple(np.array(T)+u+v),tuple(np.array(T)+v)],fill=INK,width=3)
        for pos,txt in [(O,'O'),(P,'P')]:label(d,(pos[0],pos[1]+35),txt)
        label(d,(T[0]-5,T[1]-35),'T')
        label(d,((O[0]+T[0])/2-40,(O[1]+T[1])/2),r)
        label(d,((T[0]+P[0])/2+15,(T[1]+P[1])/2-35),t)
        label(d,((O[0]+P[0])/2,O[1]+40),'?')
        return im
    if kind=='congruence':
        im,d=canvas('Matching marks indicate the equal sides and angles given in the question.')
        triangles=[[(170,680),(540,680),(440,310)],[(735,680),(1105,680),(1005,310)]]
        for pts,names in zip(triangles,['ABC','DEF']):
            A,B,C=pts;d.line(pts+[A],fill=BLUE,width=5)
            for pt,name in zip(pts,names):label(d,(pt[0],pt[1]+35 if pt!=C else pt[1]-35),name)
            def tick(a,b,n):
                u=(np.array(b)-a);u=u/np.linalg.norm(u);normal=np.array([-u[1],u[0]])
                for offset in np.linspace(-7*(n-1),7*(n-1),n):
                    mid=(np.array(a)+b)/2+u*offset
                    d.line([tuple(mid-normal*12),tuple(mid+normal*12)],fill=ORANGE,width=4)
            tick(A,B,1)
            angB=math.atan2(B[1]-C[1],C[0]-B[0])
            arc(d,B,52,angB,math.pi,color=ORANGE)
            if s['criterion']=='SAS':tick(B,C,2)
            else:
                theta=math.atan2(A[1]-C[1],C[0]-A[0]);arc(d,A,50,0,theta,color=ORANGE);arc(d,A,60,0,theta,color=ORANGE)
        return im
    if kind=='system_choices':
        im=Image.new('RGB',(1920,820),'white')
        for i,title in enumerate(['Lines crossing at 90°','Lines that never touch','One line on top of another']):
            p=Plot(title,[-3,3,-3,3],size=(640,800),equal_aspect=True)
            if i==0:p.curve(lambda x:x);p.curve(lambda x:-x,color=ORANGE)
            elif i==1:p.curve(lambda x:x+1);p.curve(lambda x:x-1,color=ORANGE)
            else:p.curve(lambda x:x,width=8);p.curve(lambda x:x,color=ORANGE,width=4,dashed=True)
            im.paste(p.finish(),(640*i,0))
        return im
    if kind=='trig':
        A,B,D=s['A'],s['B'],s['D'];fn=s['function']
        xmax=2*math.pi/B;dy=4 if fn=='tan' else abs(A)+1
        p=Plot(s['title'],[-xmax,xmax,D-dy,D+dy],ticks=[math.pi/(2*B),1 if dy<=6 else 2],note=s['note'],labels=('x (radians)','y'),xtick_format=pi_label)
        if fn=='tan':
            cuts=[-xmax]+[math.pi/2+k*math.pi for k in range(-3,3) if -xmax<math.pi/2+k*math.pi<xmax]+[xmax]
            for lo,hi in zip(cuts,cuts[1:]):p.curve(math.tan,lo=lo+0.02,hi=hi-0.02)
            for cut in cuts[1:-1]:p.line([(cut,-dy),(cut,dy)],color=GRAY,width=2,dashed=True)
        else:
            f=math.sin if fn=='sin' else math.cos;p.curve(lambda x:A*f(B*x)+D)
        return p.finish()

    p=Plot(s['title'],s['bounds'],s.get('ticks',(1,1)),labels=('','y') if kind=='scaffold' else ('x','y'),note=s.get('note',''),equal_aspect=kind in {'scaffold','inverse','transform','ellipse','hyperbola','parabola_focus'})
    if kind=='system':
        for (m,c),color in zip(s['lines'],[BLUE,ORANGE]):p.curve(lambda x:m*x+c,color=color)
    elif kind=='scaffold':
        x,y=s['point'];p.point(x,y,label=f'({x}, {y})')
        if s['operation'].startswith('Reflect'):p.line([(-10,0),(10,0)],color=ORANGE,width=4,dashed=True)
        p.draw.text((p.rect[2]+25,p.xy(0,0)[1]),'x',font=font(27),fill=INK,anchor='mm')
        p.draw.text((640,897),s['operation'],font=font(27),fill=INK,anchor='mm')
        p.draw.text((640,940),'Locate the image point yourself; only the original point is marked.',font=font(23),fill=INK,anchor='mm')
    elif kind=='inverse':
        p.curve(lambda x:2*x+1);p.curve(lambda x:(x-1)/2,color=ORANGE)
        p.curve(lambda x:x,color=GRAY,width=3,dashed=True)
        p.draw.text((640,940),'Illustrative pair: blue f; orange inverse. Dashed line is a reference line.',font=font(23),fill=INK,anchor='mm')
    elif kind=='power':p.curve(lambda x:x**s['power'])
    elif kind=='exponential':
        p.curve(lambda x:s['coefficient']*s['base']**x)
        for x,y in s.get('points',[]):p.point(x,y,label=f'({x}, {y})')
    elif kind=='transform':
        pts=np.array([[1.,1.],[3.,1.],[2.,3.]])
        if s['mode']=='dilation':pts=np.array([[2.,1.],[3.,1.],[2.,2.]])
        if s['mode']=='translation':dest=pts+[5,0]
        elif s['mode']=='rotation':dest=np.column_stack([-pts[:,1],pts[:,0]])
        elif s['mode']=='reflection':dest=pts*[-1,1];p.line([(0,-5),(0,8)],color=GRAY,dashed=True)
        else:dest=2*pts
        p.line(np.vstack([pts,pts[0]]));p.line(np.vstack([dest,dest[0]]),color=ORANGE,dashed=True)
        for points,color,suffix in [(pts,BLUE,''),(dest,ORANGE,'′')]:
            for xy,name,offset in zip(points,['P','Q','R'],[(-20,27),(24,27),(15,-25)]):
                p.point(*xy,color=color);px,py=p.xy(*xy)
                p.pen.text((px+offset[0],py+offset[1]),name+suffix,font=font(25),fill=INK,anchor='mm')
        p.draw.text((640,940),'Illustrative figures. Solid blue: A. Dashed orange: B.',font=font(23),fill=INK,anchor='mm')
    elif kind=='parabola_focus':
        param=s['p'];p.point(0,param,label=f'Focus (0, {param})')
        if s['directrix']:
            p.curve(lambda x:x*x/(4*param));p.line([(s['bounds'][0],-param),(s['bounds'][1],-param)],color=ORANGE,dashed=True)
            p.draw.text((640,940),f'Dashed line: y = -{param}. The vertex is not marked.',font=font(23),fill=INK,anchor='mm')
        else:
            p.point(0,0,label='Vertex (0, 0)')
            p.draw.text((640,940),'Only the given vertex and focus are shown.',font=font(23),fill=INK,anchor='mm')
    elif kind=='function_transform':
        f=abs if s['function']=='absolute' else lambda x:x*x
        p.curve(f);p.curve(lambda x:s['factor']*f(x-s['h'])+s['k'],color=ORANGE,dashed=True)
    elif kind=='ellipse':
        p.line([(s['h']+s['rx']*math.cos(t),s['k']+s['ry']*math.sin(t)) for t in np.linspace(0,2*math.pi,1400)])
    elif kind=='hyperbola':
        a,b=s['a'],s['b']
        for sign in [-1,1]:
            pts=[(sign*a*math.cosh(t),b*math.sinh(t)) for t in np.linspace(-2.5,2.5,1600)]
            if s['vertical']:pts=[(y,x) for x,y in pts]
            p.line(pts)
        if s['asymptotes']:
            p.curve(lambda x:b/a*x,color=GRAY,width=3,dashed=True);p.curve(lambda x:-b/a*x,color=GRAY,width=3,dashed=True)
    else:raise ValueError(kind)
    return p.finish()
