"""Grade 1–6 unit-test visual recipes; display givens without worked answers."""
from collections import Counter
from unit_test_visuals_common import *


def render_lower(s):
    k=s['kind'];g=s['grade'];q=s['qid'];title=s['title']
    if k=='bars':return bar_chart(title,s['labels'],s['values'],s.get('ylabel','Count'),s.get('hist',False))
    im,d=canvas(title,s.get('note',''))
    if k=='circle-array':
        for j in range(3):
            for i in range(7):
                x=235+i*135;y=310+j*170
                d.ellipse((x-45,y-45,x+45,y+45),fill=PALE,outline=BLUE,width=3)
    elif k=='blocks':
        tens,ones=s['tens'],s['ones']
        label(d,(440,225),'Tens',size=32);label(d,(950,225),'Ones',size=32)
        for i in range(tens):
            for j in range(10):
                x=240+i*88;y=300+j*42
                d.rectangle((x,y,x+42,y+42),fill=PALE,outline=BLUE,width=2)
        for i in range(ones):
            x=850+(i%3)*80;y=380+(i//3)*100
            d.rectangle((x,y,x+42,y+42),fill=PALE,outline=BLUE,width=2)
    elif k=='tally':
        rows=s['rows']
        for j,(name,n) in enumerate(rows):
            y=300+j*180;label(d,(270,y),name,size=32)
            for group in range((n+4)//5):
                count=min(5,n-group*5);x=480+group*170
                for z in range(min(4,count)):line(d,[(x+z*27,y-40),(x+z*27,y+40)],BLUE,5)
                if count==5:line(d,[(x-12,y+30),(x+94,y-30)],ORANGE,5)
    elif k=='suns':
        for j,(name,n) in enumerate(zip(['Monday','Tuesday','Wednesday'],[3,5,2])):
            y=285+j*200;label(d,(215,y),name,size=29)
            for i in range(n):
                x=445+i*125;d.ellipse((x-26,y-26,x+26,y+26),fill='#f9d571',outline=ORANGE,width=2)
                for a in range(0,360,45):
                    t=math.radians(a);line(d,[(x+34*math.cos(t),y+34*math.sin(t)),(x+46*math.cos(t),y+46*math.sin(t))],ORANGE,3)
        label(d,(640,865),'Key: one sun represents one sun symbol in the question.',size=23)
    elif k=='solid':
        if q in [3,11]:
            prism(d,box=(360,300,790 if q==11 else 740,710 if q==11 else 680),depth=(170,-105))
            label(d,(640,845),'Dashed lines show hidden edges.',size=24)
        else:
            # Four visual choices in the same order as the source.
            for i,name in enumerate(['A','B','C','D']):label(d,(170+310*i,240),name,size=32)
            d.ellipse((75,650,265,710),fill=PALE,outline=BLUE,width=4)
            line(d,[(75,680),(170,330),(265,680)])
            d.ellipse((385,650,575,710),fill=PALE,outline=BLUE,width=4)
            d.rectangle((385,400,575,680),fill=PALE)
            line(d,[(385,400),(385,680)]);line(d,[(575,400),(575,680)])
            d.arc((385,650,575,710),0,180,fill=BLUE,width=4)
            d.ellipse((385,370,575,430),fill='#f0f5fa',outline=BLUE,width=4)
            d.rectangle((710,415,890,660),fill=PALE,outline=BLUE,width=4)
            prism(d,(1010,455,1160,605),(65,-70))
            label(d,(640,820),'Choose the shape that resembles a soup can.',size=27)
    elif k=='jumps':
        den,n=s['den'],s['n'];hi=3 if den==4 else 1.2
        def fmt(v):
            num=round(v*den)
            return '0' if num==0 else f'{num}/{den}'
        x=number_axis(d,0,hi,y=620,step=1/den,fmt=fmt)
        for i in range(n):
            a=x(i/den);b=x((i+1)/den);cx=(a+b)/2;r=(b-a)/2
            pts=[(cx+r*math.cos(t),620-100*math.sin(t)) for t in np.linspace(math.pi,0,70)]
            line(d,pts);arrow(d,pts[-7],pts[-1]);label(d,(cx,460),f'+1/{den}' if den==5 else '+3/4',size=25)
        # The frog jumps are 3/4, rather than one tick; rebuild that case below.
        if den==4:
            im,d=canvas(title);x=number_axis(d,0,3,620,step=.25,fmt=fmt)
            for i in range(3):
                a=x(i*.75);b=x((i+1)*.75);cx=(a+b)/2;r=(b-a)/2
                pts=[(cx+r*math.cos(t),620-160*math.sin(t)) for t in np.linspace(math.pi,0,70)]
                line(d,pts);arrow(d,pts[-7],pts[-1]);label(d,(cx,400),'+3/4',size=27)
        dot(d,(x(0),620));label(d,(x(0),715),'Start',size=25)
    elif k=='strips':
        for j in range(5):
            y=230+j*115
            for i in range(6):d.rectangle((320+i*105,y,425+i*105,y+65),fill=PALE if i==0 else 'white',outline=BLUE,width=3)
            label(d,(235,y+32),'1/6',size=27)
    elif k=='angle-choice':
        for i,a in enumerate([45,90,30,120]):
            v=np.array([280+(i%2)*640,400+(i//2)*390]);r=200
            A=v+[r,0];B=v+[r*math.cos(math.radians(a)),-r*math.sin(math.radians(a))]
            line(d,[A,v,B]);angle(d,A,v,B,f'{a}°',offset=100)
            label(d,v+[0,65],chr(65+i),size=32)
    elif k=='angle-name':
        O=(440,710);P=(1040,710);Q=(760,255)
        line(d,[P,O,Q])
        for pt,name,off in [(P,'P',(25,30)),(O,'O',(-30,35)),(Q,'Q',(20,-35))]:dot(d,pt);label(d,np.array(pt)+off,name,size=34)
        angle(d,P,O,Q,r=90)
    elif k=='vertical':
        a=s['angle'];v=np.array([640,490]);r=370;t=math.radians(a)
        A=v+[r,0];B=v+[r*math.cos(t),-r*math.sin(t)];C=2*v-A;D=2*v-B
        line(d,[A,C]);line(d,[B,D]);angle(d,A,v,B,f'{a}°',r=80,offset=145)
        if g==7:angle(d,C,v,D,'?',r=80,offset=145)
    elif k=='ramp-angle':
        O=np.array([210,775]);r=780
        for a,color in [(0,GRAY),(18,BLUE),(42,ORANGE)]:
            line(d,[O,O+[r*math.cos(math.radians(a)),-r*math.sin(math.radians(a))]],color)
        arc(d,O,210,0,18,BLUE);label(d,O+[265,-40],'18°',BLUE)
        arc(d,O,500,0,42,GRAY);label(d,O+[510,-215],'42°',GRAY)
        arc(d,O,350,18,42);label(d,O+[330,-200],'?',ORANGE,size=34)
    elif k=='straight-parts':
        O=np.array([640,730]);r=490
        angles=[0,25,85,180]
        for a in angles:line(d,[O,O+[r*math.cos(math.radians(a)),-r*math.sin(math.radians(a))]])
        for a,b,txt,rad in [(0,25,'25°',210),(25,85,'x°',145),(85,180,'95°',170)]:
            arc(d,O,rad,a,b);t=math.radians((a+b)/2);label(d,O+[(rad+65)*math.cos(t),-(rad+65)*math.sin(t)],txt,ORANGE)
    elif k=='protractor':
        O=np.array([640,755]);r=500
        arc(d,O,r,0,180,GRAY);arc(d,O,r-75,0,180,GRAY)
        line(d,[O+[-r,0],O+[r,0]],GRAY,3)
        for a in range(0,181):
            t=math.radians(a);dr=27 if a%10==0 else 18 if a%5==0 else 8
            line(d,[O+[(r-dr)*math.cos(t),-(r-dr)*math.sin(t)],O+[r*math.cos(t),-r*math.sin(t)]],GRAY,2)
            if a%10==0:label(d,O+[(r-52)*math.cos(t),-(r-52)*math.sin(t)],str(a),size=20)
        for a in [35,80]:
            t=math.radians(a);line(d,[O,O+[r*math.cos(t),-r*math.sin(t)]],BLUE,5)
            label(d,O+[(r+50)*math.cos(t),-(r+50)*math.sin(t)],f'{a}°',BLUE,26)
        arc(d,O,180,35,80);label(d,(780,510),'?',ORANGE,34)
    elif k=='decimal-area':
        # Schematic partitions keep the narrow column legible; all lengths are labeled.
        xs=[260,825,1030];ys=[235,650,770]
        for i in range(2):
            for j in range(2):d.rectangle((xs[i],ys[j],xs[i+1],ys[j+1]),fill=PALE,outline=BLUE,width=4)
        for a,b,v in zip(xs,xs[1:],['1.5','0.4']):label(d,((a+b)/2,185),v)
        for a,b,v in zip(ys,ys[1:],['30','6']):label(d,(200,(a+b)/2),v)
        label(d,(640,850),'Schematic area model; use the labeled side lengths.',size=24)
    elif k=='hundreds':
        for idx in range(5):
            x=180+(idx%3)*340;y=220+(idx//3)*340
            for j in range(10):
                for i in range(10):d.rectangle((x+i*25,y+j*25,x+(i+1)*25,y+(j+1)*25),fill=PALE if j*10+i<36 else 'white',outline=BLUE,width=1)
        label(d,(1015,685),'Each grid = 1 whole',size=23)
    elif k=='two-prisms':
        for idx,dim in enumerate(s['dims']):
            x=220+idx*620
            prism(d,(x,330,x+265,650),(95,-100),[f'{v} {s["measure_unit"]}' for v in dim])
            label(d,(x+160,800),'First part' if idx==0 else 'Second part',size=28)
        label(d,(640,180),'Schematic: the two non-overlapping parts are shown separately.',size=26)
    elif k=='coordinate':
        bounds=s['bounds'];p=Plot(title,bounds,ticks=s.get('ticks',[1,1]),equal_aspect=True,note=s.get('note',''))
        pts=s['points']
        if s.get('connect'):p.line(pts+([pts[0]] if s.get('close') else []))
        for i,(x,y) in enumerate(pts):
            p.point(x,y)
            name=s.get('names',['']*len(pts))[i]
            pos=np.array(p.xy(x,y))+np.array(s.get('offsets',[[15,-30]]*len(pts))[i])
            label(p.pen,pos,f'{name}({x:g}, {y:g})',size=24)
        return p.finish()
    elif k=='lineplot':
        values=[2.25,2.5,2.5,2.75,2.5,3,2.5,2.25,2.5]
        x=number_axis(d,2,3.25,720,step=.25,fmt=lambda v:{2:'2',2.25:'2 1/4',2.5:'2 1/2',2.75:'2 3/4',3:'3',3.25:'3 1/4'}[v])
        for v,count in Counter(values).items():
            for j in range(count):
                px=x(v);py=670-j*85;line(d,[(px-16,py-16),(px+16,py+16)]);line(d,[(px-16,py+16),(px+16,py-16)])
        label(d,(640,850),'Volume (teaspoons)    •    Each × represents one measurement.',size=25)
    elif k=='inequality-number':
        x=number_axis(d,-4,4,540);arrow(d,(x(1),540),(110,540),BLUE,8);dot(d,(x(1),540),closed=False,r=13)
    elif k=='hanger':
        line(d,[(640,210),(640,330)],GRAY,5);line(d,[(310,330),(970,330)],INK,6)
        for x in [310,970]:
            line(d,[(x,330),(x-145,570),(x+145,570),(x,330)],GRAY,3)
            line(d,[(x-150,580),(x+150,580)],INK,5)
        d.rectangle((205,455,315,565),fill=PALE,outline=BLUE,width=3);label(d,(260,510),'h',size=36)
        d.ellipse((340,465,435,560),fill='#f5e4d7',outline=ORANGE,width=3);label(d,(387,512),'9',size=34)
        d.rectangle((895,455,1045,565),fill=PALE,outline=BLUE,width=3);label(d,(970,510),'26',size=36)
        label(d,(640,745),'The hanger is balanced.',size=30)
    elif k in ['composite-area','trapezoid']:
        if k=='composite-area':
            A,B,C,D,E=fit([(0,0),(10,0),(16,0),(10,4),(0,4)])
            polygon(d,[A,C,D,E]);line(d,[B,D],ORANGE,3,True);right(d,D,B,C)
            midlabel(d,A,B,'10',(0,45));midlabel(d,B,C,'6',(0,45));midlabel(d,E,A,'4',(-45,0));midlabel(d,B,D,'4',(-30,0))
        else:
            low,high,h=s['bases'][0],s['bases'][1],s['height']
            a=(low-high)/2
            A,B,C,D,H=fit([(0,0),(low,0),(a+high,h),(a,h),(a,0)])
            polygon(d,[A,B,C,D]);line(d,[D,H],GRAY,3,True);right(d,D,H,B)
            midlabel(d,A,B,f'{low}'+s.get('measure_unit',''),(0,50));midlabel(d,D,C,f'{high}'+s.get('measure_unit',''),(0,-45))
            midlabel(d,D,H,f'{h}'+s.get('measure_unit',''),(45,0))
            if s.get('split'):line(d,[D,B],ORANGE,4)
    elif k=='rectangle-given':
        # A schematic avoids locating the unknown lower side on a numbered axis.
        A=(300,300);B=(1010,300);C=(1010,730);D=(300,730)
        line(d,[A,B,C,D,A]);label(d,(300,235),s['left']);label(d,(1010,235),s['right'])
        label(d,(655,500),s['given'],size=32);midlabel(d,D,C,'Bottom side: y = ?',(0,55))
        label(d,(640,840),'Schematic; the lower side has not been located on a coordinate grid.',size=24)
    elif k in ['pyramid-net','triangular-net']:
        if k=='pyramid-net':
            l,r,t,b=550,730,430,610
            square=[(l,t),(r,t),(r,b),(l,b)];polygon(d,square)
            for tri in [[(l,t),(r,t),(640,t-220)],[(r,t),(r,b),(r+220,520)],[(r,b),(l,b),(640,b+220)],[(l,b),(l,t),(l-220,520)]]:polygon(d,tri,'#f4f7fa')
            line(d,[(640,t),(640,t-220)],ORANGE,3,True);right(d,(r,t),(640,t),(640,t-220),15)
            label(d,(700,310),'22 cm',ORANGE,25);label(d,(640,560),'18 cm',size=25)
            label(d,(640,500),'Square base',size=22)
        else:
            # Valid 3-4-5 triangular-prism net: rectangles of widths 3,4,5 and length 6.
            xs=[280,460,700,1000];t,b=370,730
            for i in range(3):d.rectangle((xs[i],t,xs[i+1],b),fill=PALE,outline=BLUE,width=4)
            polygon(d,[(280,t),(460,t),(280,t-240)],'#f4f7fa')
            # Triangle with hypotenuse 5 along lower edge of last rectangle; altitude 12/5.
            polygon(d,[(700,b),(1000,b),(808,b+144)],'#f4f7fa')
            if q==2:
                for i,v in enumerate([3,4,5]):label(d,((xs[i]+xs[i+1])/2,550),str(v),size=30)
                label(d,(1070,550),'6',size=30);label(d,(220,250),'4',size=28)
                label(d,(420,200),'5',size=28);right(d,(280,t-240),(280,t),(460,t))
            else:
                label(d,(640,185),'Fold along the shared edges.',size=28)
    elif k=='boxplot':
        vals=s['values'];partial=len(vals)==3
        lo,hi=(60,115) if partial else (10,38)
        x=number_axis(d,lo,hi,720,step=5 if partial else 2)
        if partial:q1,med,q3=vals
        else:
            low,q1,med,q3,high=vals;line(d,[(x(low),450),(x(high),450)],GRAY,3)
            for v in [low,high]:line(d,[(x(v),420),(x(v),480)])
        d.rectangle((x(q1),380,x(q3),520),fill=PALE,outline=BLUE,width=4);line(d,[(x(med),380),(x(med),520)],ORANGE,5)
        if partial:label(d,(640,820),'Only the supplied quartiles are shown; whisker endpoints were not given.',size=23)
        for v in vals:label(d,(x(v),320),str(v),size=27)
    else:raise ValueError(k)
    return im
