"""All 24 questions in the agreed follow-up list, with mathematical renderers."""
import math
import numpy as np
from PIL import Image, ImageDraw

BLUE='#245a91'
ORANGE='#ad5626'
INK='#243342'
GRAY='#748494'


def add_listed_specs(add):
    def a(sheet,qid,kind,title,expected,**kw):
        add(sheet,qid,'listed_'+kind,title,expected,batch='listed-questions',**kw)
    a('G7U9W5',4,'isosceles-angles','Isosceles triangle','equal sides is 40°',apex_angle=40)
    a('G7U9W5',5,'triangle-angles','Triangle angles','(2x)°, (3x)°, and 40°',angles=[56,84,40],angle_labels=['(2x)°','(3x)°','40°'])
    a('G8U5W1',7,'exterior','Triangle and exterior angle','exterior angle of a triangle is $120',interior=50,exterior=120)
    a('G8U5W2',1,'transversal','Parallel lines and a transversal','exterior angle measures $68',angle=68,mode='corresponding')
    a('G8U5W2',2,'transversal','Parallel lines and a transversal','interior angle is $110',angle=110,mode='alternate')
    a('G8U5W5',5,'isosceles-area','Isosceles triangle and altitude','equal sides of 13 and a base of 10',side=13,base=10)
    a('G8U5W5',10,'garfield',"Garfield’s trapezoid construction",'a = 9$ and $b = 40',a=9,b=40)
    a('G9U7W2',1,'inequalities','Two inequalities','y >= x and y <= -x + 5',lines=[[1,0,'above'],[-1,5,'below']],point=[2,3],note='Blue: y ≥ x. Orange: y ≤ −x + 5. Both boundary lines are included.')
    a('G9U7W2',5,'inequalities','Two inequalities','y >= x + 1 and y <= x - 2',lines=[[1,1,'above'],[1,-2,'below']],note='Blue: y ≥ x + 1. Orange: y ≤ x − 2. Both boundary lines are included.')
    a('G10U8W2',2,'bisector','Internal angle bisector','AB=6, AC=9 and DC=6',AB=6,AC=9,DC=6)
    a('G10U8W2',10,'altitude','Altitude to the hypotenuse','altitude from the right-angle vertex')
    a('G10U8W3',1,'midsegment','Triangle with two marked midpoints','joins the midpoints of two sides')
    a('G10U10W1',8,'revolution','One full turn around a leg','Rotating a filled right triangle')
    a('G10U11W3',5,'tangents','Two tangents from P','lengths 3x-1 and 2x+4',labels=['3x − 1','2x + 4'])
    a('G10U11W4',4,'hexagon','Regular hexagon inscribed in a circle','regular hexagon inscribed')
    a('G10U11W4',5,'construction','Three noncollinear points','through three noncollinear points')
    a('G10U13W4',9,'venn','Sample space and two events','12 in A only 8 in B only 5 in both and 25 outside',counts=[12,5,8,25])
    a('G11U7W4',3,'intersections','Two function graphs','intersect at three points',mode='three',note='Illustrative functions matching the stated intersection pattern.')
    a('G11U7W4',10,'intersections','y = x² and y = 9','Solve x^2=9 by graphing',mode='quadratic',note='Blue: y = x². Orange: y = 9. Read the intersection x-values.')
    for qid,mode,expected in [(6,'zero','angle 0?'),(7,'quarter','pi/2?'),(8,'x','x-coordinate'),(9,'y','y-coordinate')]:
        a('G11U8W2',qid,'unit-circle','Unit circle',expected,mode=mode)
    a('G12U2W5',6,'cosine-law','Triangle ABC','a=5 b=7 and C=60',a=5,b=7,C=60)


def render_listed(s,Plot,font):
    kind=s['kind'].removeprefix('listed_')
    def canvas(note=''):
        im=Image.new('RGB',(1280,980),'white');d=ImageDraw.Draw(im)
        d.text((640,40),s['title'],font=font(34),fill=INK,anchor='mt')
        d.text((640,930),note,font=font(23),fill=INK,anchor='mm')
        return im,d
    def label(d,p,text,color=INK,size=29):d.text(tuple(p),str(text),font=font(size),fill=color,anchor='mm')
    def line(d,pts,color=BLUE,width=5,dashed=False):
        pts=[tuple(p) for p in pts]
        if not dashed:d.line(pts,fill=color,width=width,joint='curve');return
        for a,b in zip(pts,pts[1:]):
            a=np.array(a);v=np.array(b)-a;length=np.linalg.norm(v)
            for t in np.arange(0,length,24):
                d.line([tuple(a+v*t/length),tuple(a+v*min(t+12,length)/length)],fill=color,width=width)
    def dot(d,p,color=BLUE):
        x,y=p;d.ellipse((x-7,y-7,x+7,y+7),fill=color)
    def arc(d,c,r,t1,t2,color=ORANGE,width=3):
        pts=[(c[0]+r*math.cos(t),c[1]-r*math.sin(t)) for t in np.linspace(t1,t2,100)]
        line(d,pts,color,width)
    def angle(d,a,v,b,text=None,r=50,offset=90,double=False):
        t1=math.atan2(v[1]-a[1],a[0]-v[0]);t2=math.atan2(v[1]-b[1],b[0]-v[0])
        delta=(t2-t1+math.pi)%(2*math.pi)-math.pi
        arc(d,v,r,t1,t1+delta)
        if double:arc(d,v,r+9,t1,t1+delta)
        if text:label(d,(v[0]+offset*math.cos(t1+delta/2),v[1]-offset*math.sin(t1+delta/2)),text,ORANGE,27)
    def right(d,a,v,b,size=24):
        a=np.array(a);v=np.array(v);b=np.array(b)
        u=(a-v)/np.linalg.norm(a-v)*size;w=(b-v)/np.linalg.norm(b-v)*size
        line(d,[v+u,v+u+w,v+w],INK,3)
    def tick(d,a,b,n=1,color=ORANGE):
        a=np.array(a);b=np.array(b);u=(b-a)/np.linalg.norm(b-a);w=np.array([-u[1],u[0]])
        for off in np.linspace(-7*(n-1),7*(n-1),n):
            mid=(a+b)/2+u*off;line(d,[mid-12*w,mid+12*w],color,3)
    def arrow(d,a,b,color=ORANGE):
        a=np.array(a);b=np.array(b);v=(b-a)/np.linalg.norm(b-a);n=np.array([-v[1],v[0]])
        line(d,[a,b],color,4);d.polygon([tuple(b),tuple(b-18*v+8*n),tuple(b-18*v-8*n)],fill=color)
    def fit(points,box=(210,210,1070,780)):
        pts=np.array(points,dtype=float);lo=pts.min(axis=0);hi=pts.max(axis=0)
        scale=min((box[2]-box[0])/(hi[0]-lo[0]),(box[3]-box[1])/(hi[1]-lo[1]))
        center=np.array([(box[0]+box[2])/2,(box[1]+box[3])/2])
        return [tuple((p-(lo+hi)/2)*[scale,-scale]+center) for p in pts]

    if kind in ['isosceles-angles','triangle-angles','exterior']:
        im,d=canvas('Use the given angle labels; no unknown angle is evaluated.')
        if kind=='isosceles-angles':
            half=math.radians(s['apex_angle']/2);height=550;base=2*height*math.tan(half)
            A=(640-base/2,780);B=(640+base/2,780);C=(640,230)
            line(d,[A,B,C,A]);tick(d,A,C);tick(d,B,C)
            angle(d,A,C,B,'40°',r=90,offset=145)
            angle(d,B,A,C,'?',r=48,offset=83);angle(d,C,B,A,'?',r=48,offset=83)
        else:
            alpha,beta=(s['angles'][:2] if kind=='triangle-angles' else [50,60])
            a,b=math.radians(alpha),math.radians(beta)
            cx=math.tan(b)/(math.tan(a)+math.tan(b));cy=cx*math.tan(a)
            A,B,C=fit([(0,0),(1,0),(cx,cy)],box=(190,240,960,780))
            line(d,[A,B,C,A])
            if kind=='triangle-angles':
                for u,v,w,txt in [(B,A,C,s['angle_labels'][0]),(C,B,A,s['angle_labels'][1]),(A,C,B,s['angle_labels'][2])]:angle(d,u,v,w,txt,r=55,offset=115)
            else:
                D=(B[0]+210,B[1]);line(d,[B,D],GRAY,4)
                angle(d,B,A,C,'50°',r=50,offset=105);angle(d,A,C,B,'?',r=50,offset=95)
                angle(d,C,B,D,'120°',r=60,offset=115)
        return im

    if kind=='transversal':
        im,d=canvas('The two blue lines are parallel. Find the angle marked ?.')
        theta=math.radians(68 if s['mode']=='corresponding' else 70)
        upper=(560,340);lower=(560-300/math.tan(theta),640)
        for y in [340,640]:
            line(d,[(170,y),(1110,y)])
            line(d,[(930,y-12),(948,y),(930,y+12)],BLUE,3)
        v=np.array([math.cos(theta),-math.sin(theta)])
        line(d,[np.array(lower)-160*v,np.array(upper)+190*v],GRAY,5)
        if s['mode']=='corresponding':
            arc(d,upper,65,0,theta);arc(d,lower,65,0,theta)
            for p,txt in [(upper,'68°'),(lower,'?')]:label(d,(p[0]+112*math.cos(theta/2),p[1]-112*math.sin(theta/2)),txt,ORANGE)
        else:
            arc(d,upper,65,theta+math.pi,2*math.pi)
            arc(d,lower,65,theta,math.pi)
            label(d,(upper[0]+70,upper[1]+94),'110°',ORANGE)
            label(d,(lower[0]-65,lower[1]-95),'?',ORANGE)
        return im

    if kind=='isosceles-area':
        im,d=canvas('The dashed segment is perpendicular to the base; equal marks show the base is bisected.')
        h=math.sqrt(s['side']**2-(s['base']/2)**2)
        A,B,C=fit([(-s['base']/2,0),(s['base']/2,0),(0,h)])
        D=((A[0]+B[0])/2,A[1]);line(d,[A,B,C,A]);line(d,[C,D],ORANGE,4,True)
        right(d,C,D,B);tick(d,A,D);tick(d,D,B)
        label(d,(640,835),'Base = 10');label(d,(695,490),'h = ?',ORANGE)
        for pt,offset in [((np.array(A)+C)/2,[-50,0]),((np.array(B)+C)/2,[50,0])]:label(d,pt+offset,'13')
        return im

    if kind=='garfield':
        im,d=canvas('Two congruent right triangles form the outer parts of the trapezoid; c is unknown.')
        a,b=s['a'],s['b']
        O,Q,S,R,P=fit([(0,0),(b,0),(a+b,0),(a+b,b),(0,a)],box=(190,210,1090,800))
        d.polygon([O,Q,P],fill='#e1ecf6');d.polygon([Q,S,R],fill='#e1ecf6')
        line(d,[O,S,R,P,O]);line(d,[P,Q,R],ORANGE)
        right(d,P,O,Q);right(d,Q,S,R);right(d,P,Q,R)
        for u,v,txt,offset in [(O,P,'a = 9',[-65,0]),(O,Q,'b = 40',[0,43]),(Q,S,'a = 9',[0,43]),(S,R,'b = 40',[65,0]),(P,Q,'c',[-5,-30]),(Q,R,'c',[-35,0])]:
            label(d,(np.array(u)+v)/2+offset,txt,size=27)
        return im

    if kind=='inequalities':
        p=Plot(s['title'],[-4,7,-5,8],ticks=[1,1],note=s['note'])
        l,t,r,b=p.rect;xx=np.linspace(-4,7,r-l);yy=np.linspace(8,-5,b-t)
        X,Y=np.meshgrid(xx,yy)
        for (m,c,side),color,rgb in zip(s['lines'],[BLUE,ORANGE],[(36,90,145),(173,86,38)]):
            mask=Y>=m*X+c if side=='above' else Y<=m*X+c
            arr=np.zeros((b-t,r-l,4),dtype=np.uint8);arr[:,:,:3]=rgb;arr[:,:,3]=mask.astype(np.uint8)*42
            shade=Image.new('RGBA',p.image.size);shade.paste(Image.fromarray(arr),(l,t))
            p.image=Image.alpha_composite(p.image.convert('RGBA'),shade).convert('RGB')
            p.line([(-4,m*(-4)+c),(7,m*7+c)],color=color)
        if 'point' in s:p.point(*s['point'],label='(2, 3)',color=INK)
        return p.finish()

    if kind=='bisector':
        im,d=canvas('Matching arcs show that AD bisects angle A. Only the given lengths are labeled.')
        AB,AC,DC=s['AB'],s['AC'],s['DC'];BD=DC*AB/AC;BC=BD+DC
        x=(AB**2-AC**2+BC**2)/(2*BC);y=math.sqrt(AB**2-x*x)
        B,C,A,D=fit([(0,0),(BC,0),(x,y),(BD,0)],box=(210,240,1070,760))
        line(d,[A,B,C,A]);line(d,[A,D],ORANGE,4)
        angle(d,B,A,D,r=60);angle(d,D,A,C,r=60)
        for p,name,off in [(A,'A',[0,-40]),(B,'B',[-25,30]),(C,'C',[25,30]),(D,'D',[0,35])]:label(d,np.array(p)+off,name)
        label(d,(np.array(A)+B)/2+[-50,0],'6');label(d,(np.array(A)+C)/2+[45,-25],'9')
        label(d,(np.array(B)+D)/2+[0,85],'BD = ?');label(d,(np.array(D)+C)/2+[0,85],'DC = 6')
        return im

    if kind=='altitude':
        im,d=canvas('CD is perpendicular to AB. Compare the angles in the three triangles.')
        A,B,C=fit([(0,0),(10,0),(3.6,4.8)],box=(210,240,1070,780))
        D=(C[0],A[1]);line(d,[A,B,C,A]);line(d,[C,D],ORANGE,4)
        right(d,A,C,B);right(d,C,D,B)
        for p,name,off in [(A,'A',[-30,30]),(B,'B',[30,30]),(C,'C',[0,-40]),(D,'D',[0,40])]:label(d,np.array(p)+off,name)
        return im

    if kind=='midsegment':
        im,d=canvas('Matching tick marks show that M and N are midpoints. Compare MN with BC.')
        A=np.array([500,220]);B=np.array([210,780]);C=np.array([1070,780]);M=(A+B)/2;N=(A+C)/2
        line(d,[A,B,C,A]);line(d,[M,N],ORANGE,5)
        tick(d,A,M);tick(d,M,B);tick(d,A,N,2);tick(d,N,C,2)
        for p,txt,off in [(A,'A',[0,-40]),(B,'B',[-30,30]),(C,'C',[30,30]),(M,'M',[-40,0]),(N,'N',[40,0])]:label(d,p+off,txt)
        return im

    if kind=='revolution':
        im,d=canvas('The filled triangle turns 360° about the vertical leg; the faint outline shows the sweep.')
        T=(640,230);O=(640,780);R=(900,780)
        d.polygon([T,(380,780),R],fill='#f3f6f9')
        d.ellipse((380,710,900,850),fill='#f3f6f9',outline=GRAY,width=3)
        line(d,[(380,780),T,R],GRAY,3)
        d.polygon([T,O,R],fill='#dce8f2');line(d,[T,O,R,T],BLUE,5);right(d,T,O,R)
        line(d,[(640,160),(640,880)],ORANGE,3,True)
        label(d,(770,160),'Axis of rotation',ORANGE,size=27)
        # Rotation arrow wraps around the axis in a horizontal plane.
        ts=np.linspace(math.radians(25),math.radians(325),180)
        pts=[(640+125*math.cos(t),450+34*math.sin(t)) for t in ts]
        line(d,pts,ORANGE,4);arrow(d,pts[-3],pts[-1]);label(d,(455,385),'360°',ORANGE)
        return im

    if kind=='tangents':
        im,d=canvas('PA and PB are tangent to the circle at A and B.')
        O=np.array([470,490]);radius=235;dist=590;P=O+[dist,0]
        tx=radius*radius/dist;ty=radius*math.sqrt(dist*dist-radius*radius)/dist
        A=O+[tx,-ty];B=O+[tx,ty]
        d.ellipse((235,255,705,725),outline=BLUE,width=5)
        line(d,[A,P,B]);line(d,[A,O,B],GRAY,3,True)
        right(d,O,A,P);right(d,O,B,P)
        for pt,name,off in [(O,'O',[-25,20]),(A,'A',[-12,-36]),(B,'B',[-12,36]),(P,'P',[35,0])]:label(d,pt+off,name)
        label(d,(A+P)/2+[15,-45],s['labels'][0]);label(d,(B+P)/2+[15,45],s['labels'][1])
        return im

    if kind=='hexagon':
        im,d=canvas('O is the center. Compare the highlighted side AB with radius OA.')
        O=np.array([640,500]);r=290
        pts=[O+np.array([r*math.cos(t),-r*math.sin(t)]) for t in np.linspace(0,2*math.pi,7)[:-1]]
        d.ellipse((350,210,930,790),outline=GRAY,width=3);line(d,pts+[pts[0]])
        for p in pts:line(d,[O,p],GRAY,2)
        line(d,[pts[0],pts[1]],ORANGE,7);line(d,[O,pts[0]],BLUE,6)
        label(d,O+[-25,30],'O');label(d,pts[0]+[30,10],'A');label(d,pts[1]+[20,-30],'B')
        label(d,(O+pts[0])/2+[0,35],'Radius');label(d,(pts[0]+pts[1])/2+[100,-10],'Side',ORANGE)
        return im

    if kind=='construction':
        im,d=canvas('Find a construction for the center of a circle through A, B, and C.')
        pts=[(270,680),(610,240),(1010,640)]
        line(d,pts,GRAY,3)
        for p,txt,off in zip(pts,['A','B','C'],[(-30,30),(0,-40),(30,30)]):dot(d,p);label(d,np.array(p)+off,txt)
        return im

    if kind=='venn':
        im,d=canvas('Each number counts outcomes in one disjoint region of the sample space.')
        d.rectangle((140,190,1140,820),outline=INK,width=3)
        # Transparent fills show both events while leaving the intersection readable.
        for bbox,color in [((270,300,750,750),(36,90,145,35)),((530,300,1010,750),(173,86,38,35))]:
            overlay=Image.new('RGBA',im.size);od=ImageDraw.Draw(overlay);od.ellipse(bbox,fill=color)
            im=Image.alpha_composite(im.convert('RGBA'),overlay).convert('RGB')
        d=ImageDraw.Draw(im);d.ellipse((270,300,750,750),outline=BLUE,width=4);d.ellipse((530,300,1010,750),outline=ORANGE,width=4)
        label(d,(420,260),'A',BLUE);label(d,(860,260),'B',ORANGE)
        for p,n in zip([(425,520),(640,520),(855,520),(1030,760)],s['counts']):label(d,p,n,size=38)
        label(d,(280,230),'Sample space',size=25)
        return im

    if kind=='intersections':
        bounds=[-4,4,-6,6] if s['mode']=='three' else [-5,5,-1,16]
        p=Plot(s['title'],bounds,ticks=[1,1] if s['mode']=='three' else [1,2],note=s['note'])
        if s['mode']=='three':
            p.curve(lambda x:0.45*(x+2)*x*(x-2)+1)
            p.curve(lambda x:1,color=ORANGE)
            p.pen.text(p.xy(-3.5,4.8),'y = f(x)',font=font(25),fill=BLUE)
            p.pen.text(p.xy(2.4,1.6),'y = g(x)',font=font(25),fill=ORANGE)
        else:
            p.curve(lambda x:x*x);p.curve(lambda x:9,color=ORANGE)
        return p.finish()

    if kind=='unit-circle':
        p=Plot(s['title'],[-1.5,1.5,-1.5,1.5],ticks=[0.5,0.5],equal_aspect=True,
               note='Radius = 1. Angles are measured counterclockwise from the positive x-axis.')
        p.line([(math.cos(t),math.sin(t)) for t in np.linspace(0,2*math.pi,500)])
        theta=0 if s['mode']=='zero' else math.pi/2 if s['mode']=='quarter' else math.radians(40)
        P=[math.cos(theta),math.sin(theta)];p.line([(0,0),P],ORANGE,4)
        p.point(*P,color=ORANGE)
        if s['mode'] in ['zero','quarter']:
            if theta:arc(p.pen,p.xy(0,0),60,0,theta)
            label(p.pen,np.array(p.xy(*P))+[45,-40],'P',ORANGE)
            pos=p.xy(0.5,0.18) if theta==0 else p.xy(0.3,0.38)
            label(p.pen,pos,'0 radians' if theta==0 else 'π/2',ORANGE,25)
        else:
            p.line([(P[0],0),P,(0,P[1])],color=GRAY,width=3,dashed=True)
            p.pen.text(tuple(np.array(p.xy(*P))+[16,-18]),'P(x, y)',font=font(26),fill=INK,anchor='lb')
            arc(p.pen,p.xy(0,0),55,0,theta)
            label(p.pen,np.array(p.xy(0,0))+[90,-30],'θ',ORANGE)
            label(p.pen,p.xy(P[0]/2,-0.16),'x',BLUE)
            label(p.pen,p.xy(-0.15,P[1]/2),'y',BLUE)
            label(p.pen,p.xy(-0.7,1.25),'Identify the '+s['mode']+'-coordinate',size=24)
        return p.finish()

    if kind=='cosine-law':
        im,d=canvas('Sides a, b, and c are opposite angles A, B, and C, respectively.')
        theta=math.radians(s['C']);C,A,B=fit([(0,0),(s['b'],0),(s['a']*math.cos(theta),s['a']*math.sin(theta))],box=(240,230,1040,770))
        line(d,[C,A,B,C]);angle(d,A,C,B,'60°',r=55,offset=100)
        for pt,name,off in [(A,'A',[25,30]),(B,'B',[0,-40]),(C,'C',[-30,30])]:label(d,np.array(pt)+off,name)
        label(d,(np.array(C)+A)/2+[0,65],'b = 7');label(d,(np.array(C)+B)/2+[-65,-10],'a = 5')
        label(d,(np.array(A)+B)/2+[45,-35],'c')
        return im
    raise ValueError(kind)
