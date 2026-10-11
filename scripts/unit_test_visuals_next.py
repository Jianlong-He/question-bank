"""The 68 additional unit-test illustrations approved in the next-image list."""
import json
import re
from pathlib import Path
from unit_test_visuals_common import *

ROOT=Path(__file__).resolve().parents[1]
CANDIDATES=ROOT/'images/unit-test-next-image-candidates.json'

def next_specs():
    out=[]
    for e in json.loads(CANDIDATES.read_text())['recommendations']:
        g,u=map(int,re.search(r'G(\d+)Unit(\d+)\.csv',e['source_csv']).groups())
        out.append(dict(grade=g,unit=u,qid=int(e['question_id']),kind='next',title=e['recommended_visual'],
                        expected_question=e['question'],batch='additional-68'))
    return out


def tick(d,a,b,n=1):
    a=np.array(a);b=np.array(b);v=(b-a)/np.linalg.norm(b-a);w=np.array([-v[1],v[0]])
    for offset in np.linspace(-7*(n-1),7*(n-1),n):
        p=(a+b)/2+offset*v;line(d,[p-12*w,p+12*w],ORANGE,3)


def regular(cx,cy,r,n):
    return [(cx+r*math.cos(2*math.pi*i/n-math.pi/2),cy+r*math.sin(2*math.pi*i/n-math.pi/2)) for i in range(n)]


def rect(d,box,top='',side='',inside=''):
    l,t,r,b=box;d.rectangle(box,fill=PALE,outline=BLUE,width=4)
    if top:label(d,((l+r)/2,t-38),top)
    if side:label(d,(l-55,(t+b)/2),side)
    if inside:label(d,((l+r)/2,(t+b)/2),inside)


def tri_angles(d,angles,box,labels=None,r=38,offset=75,base_labels_below=False):
    a,b=map(math.radians,angles[:2]);x=math.tan(b)/(math.tan(a)+math.tan(b));y=x*math.tan(a)
    A,B,C=fit([(0,0),(1,0),(x,y)],box=box);line(d,[A,B,C,A])
    if labels:
        for i,(p,v,w,t) in enumerate([(B,A,C,labels[0]),(A,B,C,labels[1]),(A,C,B,labels[2])]):
            if t:
                angle(d,p,v,w,'' if base_labels_below and i<2 else t,r=r,offset=offset)
                if base_labels_below and i<2:label(d,np.array(v)+[38 if i==0 else -38,35],t,ORANGE,27)
    return np.array([A,B,C])


def triangle_labels(d,pts,names='ABC'):
    for pt,n,off in zip(pts,names,[(-25,35),(25,35),(0,-35)]):label(d,np.array(pt)+off,n)


def grid(d,x,y,nx,ny,shaded,size=32,columns=False):
    for j in range(ny):
        for i in range(nx):
            index=i*ny+j if columns else j*nx+i
            d.rectangle((x+i*size,y+j*size,x+(i+1)*size,y+(j+1)*size),fill=PALE if index<shaded else 'white',outline=BLUE,width=2)


def cube_layer(d,origin,cells,scale=40):
    # Orthographic isometric projection; cubes in the nearer rows are drawn last.
    origin=np.array(origin);vx=np.array([scale,scale*.45]);vy=np.array([-scale,scale*.45]);vz=np.array([0,-scale*.8])
    for i,j in sorted(cells,key=lambda z:sum(z)):
        a=origin+i*vx+j*vy;b=a+vx;c=a+vx+vy;e=a+vy
        polygon(d,[a,b,c,e],'#f1f6fa')
        polygon(d,[e,c,c-vz,e-vz],'#dce9f3')
        polygon(d,[b,c,c-vz,b-vz],'#c8ddeb')


def render_next(s):
    g,u,q=s['grade'],s['unit'],s['qid']
    if g<=6:return render_foundation(g,u,q)
    return render_secondary(g,u,q)


def render_foundation(g,u,q):
    im,d=canvas('Given diagram')
    if (g,u)==(2,8):
        if q==1:rect(d,(300,290,980,730))
        elif q==2:polygon(d,[(310,735),(970,735),(610,240)])
        elif q==5:rect(d,(400,280,880,760),top='5 cm');label(d,(640,845),'All four sides are equal.',size=28)
        elif q==6:
            im,d=canvas('Shape choices')
            for i in range(4):
                cx=190+i*300;label(d,(cx,250),chr(65+i),size=34)
                if i==0:d.ellipse((cx-110,410,cx+110,630),fill=PALE,outline=BLUE,width=4)
                elif i==1:polygon(d,regular(cx,530,130,3))
                elif i==2:rect(d,(cx-105,425,cx+105,635))
                else:polygon(d,regular(cx,530,130,5))
        else:
            im,d=canvas('Solid choices')
            for cx,txt in [(240,'A'),(640,'B'),(1050,'C')]:label(d,(cx,240),txt,size=34)
            d.ellipse((110,650,370,730),fill=PALE,outline=BLUE,width=4)
            line(d,[(110,690),(240,330),(370,690)])
            prism(d,(535,440,710,615),(85,-90))
            d.ellipse((910,400,1190,680),fill=PALE,outline=BLUE,width=4)
            d.arc((910,485,1190,595),0,180,fill=GRAY,width=2)
    elif (g,u)==(3,5):
        im,d=canvas('Six equal pieces','Orange pieces represent the two pieces eaten.')
        O=(640,490);r=300
        for i in range(6):d.pieslice((340,190,940,790),i*60-90,(i+1)*60-90,fill='#f0d3bb' if i<2 else PALE,outline=BLUE,width=4)
    elif (g,u)==(3,10):
        if q==1:rect(d,(410,220,870,772),top='5 cm',side='6 cm')
        elif q==2:
            rect(d,(300,330,980,700),top='Length = ?',side='7 cm',inside='Area = 28 cm²')
            label(d,(640,820),'Schematic; use the given measurements.',size=25)
        else:
            im,d=canvas('Square made of unit squares','Each small square has area 1 square unit.')
            grid(d,370,230,3,3,9,size=180)
    elif (g,u)==(4,4):
        im,d=canvas('Multiplication area model','Schematic partitions; use the labeled lengths.')
        xs=[260,860,1040];ys=[240,680,810]
        cols,rows=([30,2],[20,4]) if q==6 else ([60,2],[50,3])
        for i in range(2):
            for j in range(2):rect(d,(xs[i],ys[j],xs[i+1],ys[j+1]))
        for i,v in enumerate(cols):label(d,((xs[i]+xs[i+1])/2,190),str(v))
        for j,v in enumerate(rows):label(d,(205,(ys[j]+ys[j+1])/2),str(v))
    elif (g,u)==(4,6):
        im,d=canvas('Tables joined along a side','One place is available along each exposed side of a table.')
        for count,cx,y in [(1,350,310),(2,920,310)]:
            left=cx-count*105/2
            for i in range(count):
                rect(d,(left+i*105,y,left+(i+1)*105,y+105))
                for yy in [y-35,y+140]:dot(d,(left+(i+.5)*105,yy),ORANGE,r=10)
            for xx in [left-35,left+count*105+35]:dot(d,(xx,y+52),ORANGE,r=10)
            label(d,(cx,y+205),f'{count} table'+('s' if count>1 else ''),size=27)
        for i in range(4):rect(d,(360+i*140,650,500+i*140,790))
        label(d,(640,850),'4 tables: count the seating places.',size=27)
    elif (g,u)==(4,11):
        if q==4:
            A,B,C=fit([(0,0),(8,0),(0,6)]);line(d,[A,B,C,A]);right(d,B,A,C)
            midlabel(d,A,B,'8 cm');midlabel(d,A,C,'6 cm',(-60,0));midlabel(d,B,C,'10 cm',(65,-30))
        else:
            im,d=canvas('Which shape has a line of symmetry?')
            shapes=[[(0,0),(4,0),(1,3)],[(0,0),(3,0),(4.5,2),(2,4),(-1,2)],[(0,0),(5,0),(3.5,2.5),(1,2.5)],[(0,0),(4,0),(2,2*math.sqrt(3))]]
            # Perturb the pentagon so it has no reflection symmetry.
            shapes[1][3]=(2.5,4)
            for i,pts in enumerate(shapes):
                cx=340+(i%2)*610;cy=330+(i//2)*390
                polygon(d,fit(pts,box=(cx-190,cy-140,cx+190,cy+140)))
                label(d,(cx,cy+185),chr(65+i),size=32)
    elif (g,u)==(5,11):
        layers,count=(2,16) if q==2 else (3,9) if q==5 else (2,11)
        im,d=canvas('Unit-cube layers','Layers are separated to show their cubes. Illustrative arrangement.')
        cells=[(i,j) for j in range(4 if count!=9 else 3) for i in range(4 if count!=9 else 3)][:count]
        for z in range(layers):
            y=(230+z*290) if layers==2 else (180+z*220)
            cube_layer(d,(730,y),cells,scale=43 if layers==2 else 39)
            label(d,(270,y+90),f'Layer {z+1}: {count} cubes',size=28)
    elif (g,u)==(5,16):
        if q==1:
            # Base 12, left side 7, right side 9.
            x=(7**2+12**2-9**2)/24;y=math.sqrt(7**2-x*x)
            A,B,C=fit([(0,0),(12,0),(x,y)]);line(d,[A,B,C,A])
            midlabel(d,A,B,'12 cm');midlabel(d,A,C,'7 cm',(-65,-15));midlabel(d,B,C,'9 cm',(60,-25))
        elif q==2:
            A,B,C=fit([(0,0),(8,0),(0,5)]);line(d,[A,B,C,A]);right(d,B,A,C);label(d,np.array(A)+[80,-75],'90°',ORANGE)
        elif q==6:
            pts=fit([(0,0),(8,0),(6,4),(1,4)]);polygon(d,pts)
            for a,b in [(pts[0],pts[1]),(pts[3],pts[2])]:
                p=(np.array(a)+b)/2;line(d,[p+[-14,-12],p,p+[-14,12]],ORANGE,3)
            label(d,(640,850),'Matching arrow marks indicate parallel sides.',size=25)
        else:
            im,d=canvas('Triangle choices')
            for i,ang in enumerate([[30,60,90],[100,40,40],[50,50,80]]):
                # Place the obtuse angle at the top to keep all diagrams well spaced.
                order=[ang[1],ang[2],ang[0]] if i==1 else ang
                tri_angles(d,order,(75+i*410,340,390+i*410,665),[f'{v}°' for v in order],r=27,offset=45,base_labels_below=True)
                label(d,(235+i*410,790),chr(65+i),size=33)
    elif (g,u)==(6,3):
        im,d=canvas('Shaded parts of a whole','Each outlined grid represents 1 whole.')
        if q==1:grid(d,440,240,10,10,86,size=40)
        elif q==8:
            grid(d,180,300,10,10,100,size=38);grid(d,730,300,10,10,45,size=38,columns=True)
        elif q==2:grid(d,240,300,5,4,7,size=140)
        else:
            # Twenty equal rectangular parts inside a square.
            for j in range(4):
                for i in range(5):d.rectangle((390+i*100,240+j*125,490+i*100,365+j*125),fill=PALE if j*5+i<9 else 'white',outline=BLUE,width=3)
    elif (g,u)==(6,5):
        im,d=canvas('Number line')
        if q==3:
            yy=lambda n:770-(n+9.6)/.7*560
            arrow(d,(640,830),(640,160),INK,3)
            for k in range(8):
                v=-9.6+k*.1;line(d,[(625,yy(v)),(655,yy(v))],INK,3)
            label(d,(550,yy(-9.4)),'−9.4');dot(d,(640,yy(-9.1)));label(d,(710,yy(-9.1)),'P')
            label(d,(920,470),'Each tick = 0.1',size=27)
        elif q==4:
            arrow(d,(150,530),(1150,530),INK,3)
            for x,name in [(360,'0'),(650,'a'),(920,'b')]:dot(d,(x,530));label(d,(x,585),name,size=32)
        elif q==5:
            yy=lambda n:790-(n+4)/6*560
            arrow(d,(640,850),(640,150),INK,3)
            for n in range(-4,3):line(d,[(627,yy(n)),(653,yy(n))],INK,3);label(d,(585,yy(n)),n,size=25)
            for v,txt in [(-3.6,'−3.6'),(1.4,'1.4')]:dot(d,(640,yy(v)));label(d,(730,yy(v)),txt)
        else:
            x=lambda n:180+n*115
            arrow(d,(130,540),(1170,540),INK,3)
            for n in range(9):line(d,[(x(n),528),(x(n),552)],INK,3)
            label(d,(x(4),590),'0');dot(d,(x(3),540));label(d,(x(3),475),'P')
            label(d,(640,735),'Each interval is 1/8.',size=29)
    elif (g,u)==(6,7):
        im,d=canvas('Tape diagram','Schematic; segment lengths are not a measuring scale.')
        l,m,r=250,735,1050;y=410
        rect(d,(l,y,m,y+150),inside='18' if q==2 else 'w')
        rect(d,(m,y,r,y+150),inside='x' if q==2 else '2.4')
        dimension(d,(l,y-80),(r,y-80),'31' if q==2 else '5.9',(0,-35))
    elif (g,u)==(6,10):
        im,d=canvas('Given solid','Dashed lines show hidden edges.')
        A=np.array([310,715]);B=np.array([735,715]);C=np.array([450,270]);v=np.array([240,-100])
        polygon(d,[B,B+v,C+v,C],'#d5e5f1');polygon(d,[A,B,C])
        line(d,[A,A+v,B+v],GRAY,3,True);line(d,[A+v,C+v],GRAY,3,True);line(d,[C,C+v,B+v,B])
    else:raise ValueError((g,u,q))
    return im


def render_secondary(g,u,q):
    im,d=canvas('Given diagram')
    if (g,u)==(7,8):
        if q==1:
            im,d=canvas('Original rectangle and scale copy')
            rect(d,(175,415,415,575),top='6 cm',side='4 cm')
            rect(d,(650,330,1130,650),top='12 cm',side='?')
            label(d,(295,755),'Original');label(d,(890,755),'Scale copy')
        elif q==4:
            im,d=canvas('Choose a scale copy','Compare side ratios. The panels use different drawing scales.')
            rect(d,(515,165,765,315),top='5',side='3');label(d,(970,225),'Original')
            for i,(h,w) in enumerate([(6,8),(9,15),(5,7),(4,6)]):
                cx=340+(i%2)*600;cy=490+(i//2)*300;ww=280;hh=ww*h/w
                rect(d,(cx-ww/2,cy-hh/2,cx+ww/2,cy+hh/2),top=str(w),side=str(h))
                label(d,(cx+200,cy),chr(65+i),size=32)
        else:
            im,d=canvas('Corresponding sides in scaled triangles')
            for idx,(a,b,hyp) in enumerate([(6,8,'10'),(9,12,'?')]):
                O=np.array([160+idx*540,730]);A=O;B=O+[b*35,0];C=O+[0,-a*35]
                line(d,[A,B,C,A]);midlabel(d,A,B,str(b));midlabel(d,A,C,str(a),(-40,0));midlabel(d,B,C,hyp,(40,-30))
                label(d,(O[0]+b*17.5,830),'Original' if idx==0 else 'Scale copy')
    elif (g,u)==(7,9):
        im,d=canvas('Cube and its net','Each edge of the cube is 3 inches.')
        prism(d,(190,380,390,580),(90,-85));label(d,(315,720),'Cube')
        for i,j in [(1,0),(0,1),(1,1),(2,1),(3,1),(1,2)]:rect(d,(630+i*120,300+j*120,750+i*120,420+j*120))
        dimension(d,(750,265),(870,265),'3 in',(0,-35));label(d,(870,770),'Net')
    elif (g,u)==(8,5):
        if q==8:
            p=Plot('Two given points',[-1,7,0,8],equal_aspect=True)
            for x,y in [(1,2),(4,6)]:p.point(x,y,label=f'({x}, {y})')
            p.line([(1,2),(4,6)]);return p.finish()
        a,b=(9,12) if q==5 else (5,12)
        A,B,C=fit([(0,0),(b,0),(0,a)]);line(d,[A,B,C,A]);right(d,B,A,C)
        midlabel(d,A,C,f'{a} '+('cm' if q==5 else 'in'),(-55,0))
        midlabel(d,A,B,'12 cm' if q==5 else '? in',(0,50));midlabel(d,B,C,'? cm' if q==5 else '13 in',(60,-30))
    elif (g,u)==(8,7):
        points={1:[(1,48),(2,55),(3,59),(4,66),(5,74),(6,77),(7,84),(8,89)],
                2:[(5,95),(8,89),(11,75),(14,72),(17,55),(20,47),(23,39),(26,23)],
                7:[(1,3),(2,5),(3,7),(4,9),(5,11),(6,13),(7,15),(8,17),(9,19),(3,16)],
                8:[(2,3),(2.3,3.5),(2.5,2.8),(2.8,3.3),(3,3.8),(7,7),(7.3,7.6),(7.5,6.8),(8,7.2)]}[q]
        bounds=[0,10,0,100] if q==1 else [0,30,0,110] if q==2 else [0,10,0,22] if q==7 else [0,10,0,10]
        labels=['Study hours','Test score'] if q==1 else ['Outdoor temperature (°C)','Hot chocolate sales'] if q==2 else ['x','y']
        ticks=[1,10] if q==1 else [5,10] if q==2 else [1,2] if q==7 else [1,1]
        p=Plot('Scatter plot',bounds,ticks=ticks,labels=labels,note='Illustrative data; no points or patterns have been labeled with an answer.')
        for pt in points:p.point(*pt)
        return p.finish()
    elif (g,u)==(9,15):
        p=Plot('Transformation setup',[-5,7,-6,7],equal_aspect=True,
               note='Only the original point and the transformation reference are shown.')
        if q==7:
            p.point(3,1,label='P(3, 1)');p.line([(-5,5),(6,-6)],ORANGE,4,True)
            label(p.pen,p.xy(-2,3.5),'y = −x',ORANGE,25)
        else:
            p.point(3,4,label='P(3, 4)');p.point(1,1,label='C(1, 1)',color=ORANGE)
            label(p.pen,p.xy(2.5,6),'Scale factor = 2',size=27)
        return p.finish()
    elif (g,u)==(9,17):
        if q in [2,9]:
            im,d=canvas('Marked triangles','Matching marks indicate equal given sides or angles.')
            sets=[]
            for i in range(2):
                pts=np.array(fit([(0,0),(6,0),(2,5)],box=(130+i*620,270,530+i*620,720)))
                A,B,C=pts;line(d,[A,B,C,A]);triangle_labels(d,pts,'ABC' if i==0 else 'DEF');sets.append(pts)
                tick(d,A,B,1)
                if q==2:
                    tick(d,A,C,2);angle(d,B,A,C,r=55)
                else:
                    angle(d,B,A,C,r=55);angle(d,A,B,C,r=55);angle(d,A,B,C,r=65)
        elif q==6:
            im,d=canvas('Rhombus and its diagonals')
            A,B,C,D=np.array([(640,200),(1050,490),(640,780),(230,490)])
            line(d,[A,B,C,D,A]);line(d,[A,C],ORANGE,4);line(d,[B,D],ORANGE,4)
            for a,b in [(A,B),(B,C),(C,D),(D,A)]:tick(d,a,b)
        else:
            im,d=canvas('Compass construction choices')
            for i in range(4):
                cx=340+(i%2)*610;cy=320+(i//2)*415;A=np.array([cx-125,cy]);B=np.array([cx+125,cy]);M=(A+B)/2
                line(d,[A,B]);dot(d,A);dot(d,B);label(d,A+[0,35],'A');label(d,B+[0,35],'B')
                if i==0:arc(d,M,155,25,155)
                elif i==1:
                    arc(d,A,195,-62,62);arc(d,B,195,118,242)
                elif i==2:d.ellipse((A[0]-135,cy-135,A[0]+135,cy+135),outline=ORANGE,width=3)
                else:
                    arc(d,A,185,-65,65);arc(d,B,115,105,255)
                label(d,(cx,cy+200),chr(65+i),size=32)
    elif (g,u)==(10,8):
        if q==3:
            im,d=canvas('Similar triangles ABC and DEF','The two drawings show the given corresponding sides.')
            for i,scale in enumerate([1,1.5]):
                pts=np.array([(0,0),(6,0),(4,math.sqrt(60))])*scale
                A,B,C=pts*[45,-45]+[170+i*580,770];line(d,[A,B,C,A]);triangle_labels(d,[A,B,C],'ABC' if i==0 else 'DEF')
                midlabel(d,A,B,'6' if i==0 else '9',(0,70));midlabel(d,B,C,'8' if i==0 else '?',(50,-10))
        elif q==5:
            im,d=canvas('Person and tree shadows','Schematic: sunlight has the same angle of elevation in both triangles.')
            for i,box in enumerate([(150,320,430,740),(640,230,1110,740)]):
                A,B,C=fit([(0,0),(4,0),(0,6)],box=box);line(d,[A,B,C,A]);right(d,B,A,C)
                midlabel(d,A,B,'4 ft' if i==0 else '30 ft',(0,50));midlabel(d,A,C,'6 ft' if i==0 else 'h = ?',(-65,0))
                label(d,(np.array(A)[0]+80,825),'Person' if i==0 else 'Tree')
                angle(d,A,B,C,r=35)
        elif q==6:
            im,d=canvas('Angle bisector in triangle ABC')
            B,C,A,D=map(np.array,fit([(0,0),(10,0),(1,math.sqrt(63)),(4,0)],box=(180,220,1070,745)))
            line(d,[A,B,C,A]);line(d,[A,D],ORANGE);angle(d,B,A,D,r=85);angle(d,D,A,C,r=85)
            for pt,name,off in [(A,'A',(0,-45)),(B,'B',(-30,30)),(C,'C',(30,30)),(D,'D',(0,40))]:label(d,pt+off,name)
            midlabel(d,A,B,'8',(-65,0));midlabel(d,A,C,'12',(55,-40));midlabel(d,B,D,'4',(0,78));midlabel(d,D,C,'?',(0,78))
        else:
            im,d=canvas('Triangle with an interior segment')
            A=np.array([475,210]);B=np.array([210,780]);C=np.array([1060,780]);f=.5 if q==8 else .38;M=A+f*(B-A);N=A+f*(C-A)
            line(d,[A,B,C,A]);line(d,[M,N],ORANGE)
            for pt,name,off in [(A,'A',(0,-38)),(B,'B',(-30,35)),(C,'C',(30,35)),(M,'M',(-35,0)),(N,'N',(35,0))]:label(d,pt+off,name)
            if q==8:
                tick(d,A,M);tick(d,M,B);tick(d,A,N,2);tick(d,N,C,2)
                label(d,(640,860),'Matching ticks mark the two midpoints.',size=25)
            else:
                for a,b in [(M,N),(B,C)]:
                    p=(a+b)/2;line(d,[p+[-14,-12],p,p+[-14,12]],ORANGE,3)
                label(d,(640,860),'MN is parallel to BC.',size=27)
    elif (g,u)==(10,10):
        if q==6:
            im,d=canvas('Rotate the filled right triangle','Turn the triangle through 360° about the marked leg.')
            T=(560,230);O=(560,770);R=(970,770);polygon(d,[T,O,R]);right(d,T,O,R)
            line(d,[(560,160),(560,850)],ORANGE,4,True);label(d,(420,170),'Rotation axis',ORANGE,27)
            pts=[(560+120*math.cos(t),430+42*math.sin(t)) for t in np.linspace(.2,5.8,160)]
            line(d,pts,ORANGE,4);arrow(d,pts[-6],pts[-1],ORANGE);label(d,(350,435),'360°',ORANGE)
        else:
            im,d=canvas('Cylinder and slice' if q==5 else 'Cylinder and cone',
                        'The highlighted slice is parallel to the base.' if q==5 else 'Both solids have the same radius r and height h.')
            def cylinder(cx,t,b,r):
                d.rectangle((cx-r,t,cx+r,b),fill=PALE)
                d.ellipse((cx-r,b-40,cx+r,b+40),fill=PALE,outline=BLUE,width=4)
                line(d,[(cx-r,t),(cx-r,b)]);line(d,[(cx+r,t),(cx+r,b)])
                d.ellipse((cx-r,t-40,cx+r,t+40),fill='#f5f8fa',outline=BLUE,width=4)
            if q==5:
                cylinder(640,245,760,230);d.ellipse((410,435,870,515),fill='#f2d6c0',outline=ORANGE,width=4)
            else:
                cylinder(350,290,720,145)
                T=np.array([960,290]);O=np.array([960,720]);L=O+[-145,0];R=O+[145,0]
                polygon(d,[L,T,R]);d.ellipse((815,680,1105,760),fill=PALE,outline=BLUE,width=4)
                for cx in [350,960]:line(d,[(cx,720),(cx+145,720)],ORANGE);label(d,(cx+70,780),'r',ORANGE)
                dimension(d,(565,290),(565,720),'h',(35,0));line(d,[T,O],GRAY,3,True);label(d,(915,500),'h')
                label(d,(350,840),'Volume = 90');label(d,(960,840),'Volume = ?')
    elif (g,u)==(10,11):
        if q in [1,2]:
            theta=60 if q==1 else 90;im,d=canvas('Given arc' if q==1 else 'Given sector')
            O=np.array([640,490]);r=295;t=math.radians(theta);A=O+[r,0];B=O+[r*math.cos(t),-r*math.sin(t)]
            if q==2:d.pieslice((345,195,935,785),-theta,0,fill='#f0d8c4')
            d.ellipse((345,195,935,785),outline=BLUE,width=4);line(d,[A,O,B]);arc(d,O,r,0,theta,ORANGE,7)
            angle(d,A,O,B,f'{theta}°',r=80,offset=125);midlabel(d,O,A,'r = 6' if q==1 else 'r = 10',(0,40));dot(d,O)
        elif q==6:
            im,d=canvas('Radius and tangent')
            O=np.array([500,490]);P=O+[290,0];d.ellipse((210,200,790,780),outline=BLUE,width=4)
            line(d,[O,P]);line(d,[(790,140),(790,850)],ORANGE);dot(d,O);dot(d,P);label(d,O+[-30,30],'O');label(d,P+[30,30],'P')
            angle(d,O,P,P+[0,-200],'?',r=55,offset=90);label(d,(930,210),'Tangent',ORANGE)
        else:
            im,d=canvas('Two tangents from one external point')
            O=np.array([430,490]);r=240;P=O+[640,0];x=r*r/640;y=r*math.sqrt(640**2-r**2)/640
            A=O+[x,-y];B=O+[x,y];d.ellipse((190,250,670,730),outline=BLUE,width=4);line(d,[A,P,B]);dot(d,P)
            for p,n,off in [(A,'A',(-20,-35)),(B,'B',(-20,35)),(P,'P',(35,0))]:label(d,p+off,n)
            midlabel(d,A,P,'9 cm',(0,-45));midlabel(d,B,P,'?',(0,45));label(d,(640,850),'PA and PB are tangent segments.',size=27)
    elif (g,u)==(11,4):
        if q==4:
            p=Plot('p(x) = (x − 2)²(x + 1)',[-2,4,-5,10],ticks=[1,1]);p.curve(lambda x:(x-2)**2*(x+1));return p.finish()
        p=Plot('Polynomial end behavior',[-4,4,-8,3],ticks=[1,1],note='Illustrative polynomial matching the stated end behavior; no equation is supplied.')
        fn=lambda x:1.5-.13*x**4;p.curve(fn)
        for x,dx in [(-2.8,-.12),(2.8,.12)]:arrow(p.pen,p.xy(x,fn(x)),p.xy(x+dx,fn(x+dx)))
        return p.finish()
    elif (g,u)==(12,2):
        im,d=canvas('Triangle ABC')
        if q==12:
            C,A,B=map(np.array,fit([(0,0),(6,0),(0,8)],box=(300,220,990,770)));line(d,[C,A,B,C]);right(d,A,C,B)
            for p,n,off in [(C,'C',(-30,35)),(A,'A',(30,35)),(B,'B',(0,-40))]:label(d,p+off,n)
            midlabel(d,C,A,'b = 6',(0,65));midlabel(d,C,B,'a = 8',(-80,0));midlabel(d,A,B,'c = ?',(70,-20))
        else:
            A,B,C=tri_angles(d,[40,60,80],(160,230,1080,750),['40°','60°',''])
            triangle_labels(d,[A,B,C]);midlabel(d,A,C,'b = ?',(-55,-40));midlabel(d,B,C,'a = 12',(65,-20))
    elif (g,u)==(12,3):
        if q==4:
            im,d=canvas('Complex number in polar form')
            O=np.array([360,740]);E=O+[520*.5,-520*math.sqrt(3)/2]
            arrow(d,(180,740),(1090,740),GRAY,3);arrow(d,(360,850),(360,150),GRAY,3)
            label(d,(1080,800),'Real');label(d,(255,170),'Imaginary',size=25);arrow(d,O,E)
            angle(d,O+[100,0],O,E,'π/3',r=90,offset=145);midlabel(d,O,E,'r = 2',(-70,-20))
        else:
            p=Plot('Complex plane',[-2,2,-1,3],ticks=[1,1],labels=['Real','Imaginary'],equal_aspect=True)
            x=1 if q==3 else -1;y=1;p.line([(0,0),(x,y)]);p.point(x,y,label='1 + i' if q==3 else '−1 + i')
            return p.finish()
    else:raise ValueError((g,u,q))
    return im
