"""Grade 7–12 unit-test visual recipes."""
from unit_test_visuals_common import *
from generate_question_graphs import render as existing_render
from question_graph_listed import render_listed


def render_upper(s):
    k=s['kind'];q=s['qid'];title=s['title']
    im,d=canvas(title,s.get('note',''))
    if k=='complementary':
        O=np.array([360,745]);A=O+[610,0];B=O+[0,-560];C=O+[500*math.cos(math.radians(48)),-500*math.sin(math.radians(48))]
        line(d,[A,O,B]);line(d,[O,C]);right(d,A,O,B,size=35)
        angle(d,A,O,C,'3x°',r=170,offset=235);angle(d,C,O,B,'(2x + 10)°',r=320,offset=390)
    elif k=='prism-slice':
        front,back=prism(d,(300,350,825,780),(150,-140))
        a=front[0]+[0,-230];b=front[1]+[0,-230];v=np.array([150,-140])
        polygon(d,[a,b,b+v,a+v],'#f5dec9',ORANGE)
        for idx in [0,1,2,3]:line(d,[front[idx],back[idx]],BLUE,3,dashed=idx==0)
        label(d,(640,860),'The orange slice is parallel to the base.',size=27)
    elif k=='transversal':
        t=math.radians(65);upper=np.array([700,335]);lower=upper+[-305/math.tan(t),305];v=np.array([math.cos(t),-math.sin(t)])
        for y in [335,640]:
            line(d,[(170,y),(1110,y)]);line(d,[(985,y-12),(1000,y),(985,y+12)])
        line(d,[lower-200*v,upper+200*v],GRAY,5)
        if s['mode']=='corresponding':
            for p,txt in [(upper,'65°'),(lower,'?')]:
                arc(d,p,65,0,65);label(d,p+[125*math.cos(t/2),-125*math.sin(t/2)],txt,ORANGE)
        else:
            arc(d,upper,65,180,245);label(d,upper+[-120,75],'65°',ORANGE)
            arc(d,lower,65,65,180);label(d,lower+[-70,-120],'?',ORANGE)
        label(d,(640,850),'The two blue lines are parallel.',size=26)
    elif k=='exterior':
        a=math.radians(45);b=math.radians(60);x=math.tan(b)/(math.tan(a)+math.tan(b));y=x*math.tan(a)
        A,B,C=fit([(0,0),(1,0),(x,y)],box=(180,240,960,770));D=np.array(B)+[220,0]
        line(d,[A,B,C,A]);line(d,[B,D],GRAY)
        angle(d,B,A,C,'45°',offset=115);angle(d,A,C,B,'?',offset=100);angle(d,C,B,D,'120°',offset=125,r=70)
    elif k=='right-triangle':
        mode=s['mode'];base,h=(6,8) if mode=='ladder-8' else (6,6*math.sqrt(3)) if mode=='ladder-10' else (12,3)
        A,B,C=fit([(0,0),(base,0),(base,h)],box=(250,220,1010,760))
        line(d,[A,B,C,A]);right(d,A,B,C)
        if mode=='ladder-8':
            midlabel(d,A,B,'6 ft',(0,50));midlabel(d,A,C,'10 ft',(-65,-20));midlabel(d,B,C,'h = ?',(75,0))
        elif mode=='ladder-10':
            midlabel(d,A,C,'12 ft',(-70,-20));midlabel(d,B,C,'h = ?',(75,0));angle(d,B,A,C,'60°',r=65,offset=115)
        else:
            midlabel(d,A,B,'12 ft',(0,60));midlabel(d,B,C,'3 ft',(70,0));angle(d,B,A,C,'θ',r=220,offset=285)
    elif k=='rotation':
        p=Plot(title,[-5,5,-5,5],equal_aspect=True,note=f'Rotate 90° {s["direction"]} about the origin. Only the original point is shown.')
        x,y=s['point'];p.point(x,y,label=f'P({x}, {y})')
        O=p.xy(0,0);arc(p.pen,O,62,135,45 if s['direction']=='clockwise' else 225,head=True)
        return p.finish()
    elif k=='curved-scatter':
        p=Plot(title,[0,10,0,12],ticks=[1,2],note='Illustrative points matching the rise-then-fall pattern described.')
        for x,y in [(1,2),(2,5),(3,7.5),(4,9),(5,10),(6,9.2),(7,7.6),(8,5.1),(9,2.2)]:p.point(x,y)
        return p.finish()
    elif k=='inequality':
        return existing_render(dict(kind='inequality',title=title,bounds=[-4,5,-6,8],ticks=[1,1],m=-2,c=3,side='below',closed=True))
    elif k=='four-functions':
        im=Image.new('RGB',(1600,1560),'white')
        for i,name in enumerate(['A','B','C','D']):
            p=Plot(name,[-4,4,-4,4],ticks=[2,2],size=(800,780),equal_aspect=True)
            if i==0:p.curve(lambda x:2*x)
            elif i==1:p.curve(lambda x:x*x)
            elif i==2:p.line([(2*math.cos(t),2*math.sin(t)) for t in np.linspace(0,2*math.pi,800)])
            else:p.curve(lambda x:1)
            im.paste(p.finish(),((i%2)*800,(i//2)*780))
        return im
    elif k=='partition':
        A=np.array([200,650]);B=np.array([1080,300]);P=A+.4*(B-A)
        line(d,[A,B])
        for pt,name in [(A,'A(0, 0)'),(B,'B(10, 5)'),(P,'P')]:dot(d,pt);label(d,pt+[0,60],name,size=30)
        midlabel(d,A,P,'2 parts',(-20,-45),ORANGE);midlabel(d,P,B,'3 parts',(-10,-50),ORANGE)
        label(d,(640,810),'AP : PB = 2 : 3',size=31)
    elif k=='triangle-coordinate':
        pts=s['points'];p=Plot(title,[-2,8,-2,11] if s.get('medians') else [-2,8,-2,6],equal_aspect=True)
        p.line(pts+[pts[0]])
        if s.get('medians'):
            for i in range(3):p.line([pts[i],((np.array(pts[(i+1)%3])+pts[(i+2)%3])/2)],ORANGE,3,True)
        for x,y in pts:
            p.point(x,y);label(p.pen,np.array(p.xy(x,y))+[40,-30],f'({x}, {y})',size=24)
        return p.finish()
    elif k=='table':
        xs=[170,620,865,1110];ys=[270,390,540,690]
        for x in xs:line(d,[(x,270),(x,690)],GRAY,3)
        for y in ys:line(d,[(170,y),(1110,y)],GRAY,3)
        for i,row in enumerate([['','In band','Not in band'],['Plays a sport','25','35'],['Does not play a sport','15','25']]):
            for j,v in enumerate(row):label(d,((xs[j]+xs[j+1])/2,(ys[i]+ys[i+1])/2),v,size=26)
        label(d,(640,790),'Given survey: 100 students',size=29)
    elif k=='hexagon':
        O=np.array([640,495]);r=310
        pts=[O+[r*math.cos(math.radians(t)),-r*math.sin(math.radians(t))] for t in range(0,360,60)]
        polygon(d,pts);dot(d,O);M=(pts[4]+pts[5])/2
        line(d,[O,M],ORANGE,4,True);right(d,O,M,pts[5]);midlabel(d,O,M,'a = ?',(-60,0),ORANGE)
        midlabel(d,pts[4],pts[5],'8',(0,45));label(d,O+[-25,-35],'O')
    elif k=='inscribed-angle':
        O=np.array([640,480]);r=300;point=lambda t:O+[r*math.cos(math.radians(t)),-r*math.sin(math.radians(t))]
        A=point(180);B=point(50);C=point(-50)
        d.ellipse((340,180,940,780),outline=BLUE,width=4);line(d,[B,A,C]);arc(d,O,r,-50,50,ORANGE,7)
        angle(d,B,A,C,'?',r=85,offset=140);label(d,(1040,480),'100°',ORANGE,31)
    elif k=='cyclic':
        O=np.array([640,475]);r=310;point=lambda t:O+[r*math.cos(math.radians(t)),-r*math.sin(math.radians(t))]
        A,B,C,D=[point(t) for t in [180,70,0,-70]]
        d.ellipse((330,165,950,785),outline=GRAY,width=3);line(d,[A,B,C,D,A])
        angle(d,B,A,D,'70°',r=80,offset=145);angle(d,D,C,B,'?',r=70,offset=120)
    elif k=='chord':
        O=np.array([640,440]);scale=65;r=5*scale
        A=O+[-4*scale,3*scale];B=O+[4*scale,3*scale];M=O+[0,3*scale]
        d.ellipse((O[0]-r,O[1]-r,O[0]+r,O[1]+r),outline=BLUE,width=4)
        line(d,[A,B]);line(d,[O,M],ORANGE,4,True);line(d,[O,B],GRAY,3);dot(d,O);label(d,O+[-25,-35],'O')
        right(d,O,M,B);midlabel(d,O,M,'3 cm',(-60,0),ORANGE);midlabel(d,O,B,'r = ?',(35,-32))
        dimension(d,A+[0,75],B+[0,75],'8 cm',(0,35))
    elif k=='focus':
        p=Plot(title,[-4,7,-4,7],equal_aspect=True,note='Only the given focus and directrix are shown.')
        y=s['directrix'];p.line([(-4,y),(7,y)],ORANGE,4,True);label(p.pen,p.xy(4.6,y-.5),f'y = {y}',ORANGE,25)
        x,y=s['focus'];p.point(x,y);label(p.pen,np.array(p.xy(x,y))+[85,-30],f'F({x}, {y})',size=25)
        return p.finish()
    elif k=='sine-triangle':
        a,b=math.radians(30),math.radians(45);x=math.tan(b)/(math.tan(a)+math.tan(b));y=x*math.tan(a)
        A,B,C=fit([(0,0),(1,0),(x,y)],box=(180,260,1100,745));line(d,[A,B,C,A])
        angle(d,B,A,C,'30°',r=125,offset=190);angle(d,A,B,C,'45°',r=95,offset=145)
        midlabel(d,B,C,'a = 10',(75,-10));midlabel(d,A,C,'b = ?',(-40,-45))
        for p,t,off in [(A,'A',(-35,35)),(B,'B',(35,35)),(C,'C',(0,-40))]:label(d,np.array(p)+off,t,size=32)
    elif k=='cosine-triangle':
        return render_listed(dict(kind='listed_cosine-law',title=title,a=5,b=7,C=60),Plot,font)
    elif k=='normal':
        mode=s['mode'];l,r,b,t=160,1140,745,220
        x=lambda v:l+(v-50)/40*(r-l);y=lambda v:b-v*6100
        line(d,[(l,b),(r,b)],INK,3)
        if mode!='compare':
            sd=5;fn=lambda v:math.exp(-.5*((v-70)/sd)**2)/(sd*math.sqrt(2*math.pi))
            low,high=(65,75) if mode=='middle' else (80,90)
            pts=[(x(v),y(fn(v))) for v in np.linspace(low,high,300)]
            d.polygon([(x(low),b)]+pts+[(x(high),b)],fill='#d7e6f2')
            line(d,[(x(v),y(fn(v))) for v in np.linspace(50,90,600)],BLUE,5)
            for v in [55,60,65,70,75,80,85]:
                line(d,[(x(v),b-8),(x(v),b+8)],INK,2);label(d,(x(v),b+38),v,size=25)
            label(d,(640,845),'Mean = 70; standard deviation = 5',size=28)
            label(d,(640,180),'Shaded region: '+('65 to 75' if mode=='middle' else 'above 80'),size=29)
        else:
            for sd,color in [(4,BLUE),(8,ORANGE)]:
                fn=lambda v:math.exp(-.5*((v-70)/sd)**2)/(sd*math.sqrt(2*math.pi))
                line(d,[(x(v),y(fn(v))) for v in np.linspace(50,90,600)],color,5)
            line(d,[(x(70),b),(x(70),t)],GRAY,2,True);label(d,(640,805),'Same mean',size=28)
            label(d,(380,870),'Curve A',BLUE,28);label(d,(900,870),'Curve B',ORANGE,28)
    elif k=='vector':
        O=np.array([700,750]) if s['mode']=='components' else np.array([340,750]);scale=230 if s['mode']=='components' else 60
        V=np.array([-1,math.sqrt(3)]) if s['mode']=='components' else np.array([5,5*math.sqrt(3)])
        arrow(d,[max(100,O[0]-420),O[1]],O+[440,0],GRAY,3);arrow(d,O+[0,100],O+[0,-580],GRAY,3)
        label(d,O+[450,35],'x');label(d,O+[-35,-585],'y');E=O+V*[scale,-scale];arrow(d,O,E,BLUE,6)
        if s['mode']=='polar':
            angle(d,O+[100,0],O,E,'60°',r=100,offset=155);midlabel(d,O,E,'Magnitude = 10',(-130,-5),size=27)
        else:
            angle(d,O+[100,0],O,E,'θ',r=100,offset=150);label(d,E+[-40,-50],'<−1, √3>',size=32)
    elif k=='boat':
        O=np.array([340,720]);arrow(d,O,O+[650,0],BLUE,7);arrow(d,O,O+[0,-380],ORANGE,7)
        label(d,(650,795),'Boat: 12 mph east',BLUE,31);label(d,(570,330),'Current: 5 mph north',ORANGE,29)
        right(d,O+[100,0],O,O+[0,-100]);label(d,(640,190),'Given velocity vectors',size=30)
    elif k=='piecewise':
        p=Plot(title,[-3,5,-3,5],equal_aspect=True,note='f(x) = x + 1 for x < 1; f(x) = 3 − x for x ≥ 1.')
        p.curve(lambda x:x+1,hi=1);p.curve(lambda x:3-x,lo=1,color=ORANGE);p.point(1,2,color=ORANGE)
        return p.finish()
    elif k=='reciprocal-limit':
        p=Plot(title,[0,6,-8,8],ticks=[1,2],note='Examine the branch to the right of x = 3.')
        p.curve(lambda x:1/(x-3),hi=2.98);p.curve(lambda x:1/(x-3),lo=3.02);p.line([(3,-8),(3,8)],GRAY,2,True)
        return p.finish()
    elif k=='hole':
        p=Plot(title,[-1,7,0,11],equal_aspect=True)
        p.curve(lambda x:x+3,hi=3);p.curve(lambda x:x+3,lo=3);p.point(3,6,closed=False)
        return p.finish()
    else:raise ValueError(k)
    return im
