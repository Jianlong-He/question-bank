"""Question-specific visual aids for the remaining six priority topic areas."""
import math
import numpy as np
from PIL import Image, ImageDraw

BLUE = '#245a91'
ORANGE = '#ad5626'
INK = '#243342'
GRAY = '#748494'


def add_gap_specs(add):
    def a(sheet, qid, kind, title, expected, **data):
        add(sheet, qid, 'gap_' + kind, title, expected,
            batch='priority-gaps', **data)

    for sheet, qid, square, expected in [
        ('G7U9W3', 9, False, 'halfway up the height'),
        ('G7U9W3Rev', 4, True, 'halfway up the height'),
        ('G10U10W1', 5, False, 'strictly between the base and apex')]:
        a(sheet, qid, 'pyramid', 'A slice parallel to the base', expected,
          square=square, halfway=sheet.startswith('G7'))
    a('G10U10W1', 6, 'cube', 'A plane through a cube', 'parallel to one face')
    for sheet, qid, sides, expected in [
        ('G10U9W1', 5, [1, 2, 2], 'side lengths 1 2 and 2'),
        ('G10U9W1Rev', 2, [2, 3, 6], 'side lengths 2 3 and 6')]:
        a(sheet, qid, 'box', 'Space diagonal of a rectangular box', expected, sides=sides)
    for sheet, qid, run, rise, expected in [
        ('G8U5W6', 4, 8, 15, 'base is 8 ft'),
        ('G8U5W6HW', 3, 5, 12, 'base is 5 ft')]:
        a(sheet, qid, 'ladder', 'Ladder against a wall', expected, run=run, rise=rise)
    a('G10U9W3', 8, 'ramp', 'Ramp above level ground', 'sloping length 10 m',
      angle=30, hypotenuse=10)
    a('G10U9W3', 9, 'ramp', 'Sight line above level ground', 'horizontal distance is 20 m',
      angle=45, run=20)
    a('G9U10W1', 4, 'histogram', 'Frequency histogram', 'frequency 3 for 0–5',
      bins=[0, 5, 10], frequencies=[3, 7])
    a('G11U12W1', 7, 'normal', 'Normal distribution', 'mean 50 and standard deviation 4',
      mode='standard-deviations', mean=50, sd=4)
    a('G11U12W1', 8, 'normal', 'Symmetric normal distribution', 'lies above its mean', mode='area')
    for sheet, qid, base, shift, expected in [
        ('G11U5W1', 8, 3, 0, 'log base 3 of x'),
        ('G11U6W4', 6, 2, 0, 'log base 2 of x'),
        ('G11U6W4', 7, 2, 4, 'log base 2 of (x-4)')]:
        argument='x' if not shift else f'(x − {shift})'
        a(sheet, qid, 'log', f'y = log base {base} of {argument}', expected,
          base=base, shift=shift)
    a('G11U5W1', 9, 'log-family', 'Examples of basic logarithmic graphs',
      'every basic real logarithmic graph', bases=[2, 3, 0.5],
      note='y = log base b of x. Blue: b = 2. Orange: b = 3. Gray: b = 1/2.')
    for sheet, qid, numerator, shift, expected in [
        ('G11U13W2', 1, 1, 4, '1/(x-4)'),
        ('G11U13W2', 2, 3, -2, '3/(x+2)'),
        ('G12U4W1', 4, 1, 2, '1/(x-2)'),
        ('G12U4W1HW', 4, 1, 7, '1/(x - 7)')]:
        argument=f'x − {shift}' if shift >= 0 else f'x + {-shift}'
        a(sheet, qid, 'rational', f'f(x) = {numerator}/({argument})', expected,
          numerator=numerator, shift=shift)
    a('G12U10W6', 6, 'rational', 'A graph near a vertical asymptote', 'at a vertical asymptote',
      numerator=1, shift=0, note='Illustrative example: y = 1/x.')
    a('G12U10W6Rev', 2, 'jump', 'Graph near x = 1', 'from y = 2 to y = 5 at x = 1',
      at=1, left=2, right=5)
    for qid, points, bounds, expected in [
        (1, [[1, 2], [4, 6]], [-1, 7, -1, 8], '(1, 2) and (4, 6)'),
        (2, [[-2, 3], [-2, -5]], [-6, 2, -7, 5], '(-2, 3) and (-2, -5)'),
        (3, [[2, -4], [8, 6]], [0, 11, -6, 9], '(2, -4) and (8, 6)')]:
        a('G9U18W1', qid, 'segment', 'Given endpoints', expected, points=points, bounds=bounds)
    a('G9U18W1', 4, 'midpoint', 'A segment and its midpoint', 'midpoint of A(1, 7)',
      labels=['A(1, 7)', 'M(5, 5)', 'B(x, 3)'])
    a('G12U6W1', 3, 'vector', 'Given displacement', '4 units right and 3 units up',
      points=[[0, 0], [4, 3]], bounds=[-1, 7, -1, 6], steps=True)
    a('G12U6W1', 4, 'vector', 'Vector from initial to terminal point', 'initial point (2 1)',
      points=[[2, 1], [7, 5]], bounds=[0, 10, -1, 8], steps=False)


def render_gap(s, Plot, font):
    kind=s['kind'].removeprefix('gap_')
    def canvas(note=''):
        im=Image.new('RGB', (1280, 980), 'white'); d=ImageDraw.Draw(im)
        d.text((640, 40), s['title'], font=font(34), fill=INK, anchor='mt')
        d.text((640, 930), note, font=font(23), fill=INK, anchor='mm')
        return im,d
    def label(d, xy, text, color=INK, size=29):
        d.text(xy, str(text), font=font(size), fill=color, anchor='mm')
    def line(d, points, color=BLUE, width=5, dashed=False):
        if not dashed:
            d.line(points, fill=color, width=width, joint='curve'); return
        for a,b in zip(points,points[1:]):
            a=np.array(a); b=np.array(b); length=np.linalg.norm(b-a)
            for t in np.arange(0,length,24):
                d.line([tuple(a+(b-a)*t/length),tuple(a+(b-a)*min(t+12,length)/length)],fill=color,width=width)
    def arrow(d, start, end, color=BLUE, width=5):
        line(d,[start,end],color,width)
        v=np.array(end)-start; v=v/np.linalg.norm(v)
        n=np.array([-v[1],v[0]])
        d.polygon([end,tuple(np.array(end)-v*19+n*9),tuple(np.array(end)-v*19-n*9)],fill=color)
    def dot(d, pt, color=BLUE):
        x,y=pt;d.ellipse((x-7,y-7,x+7,y+7),fill=color)

    if kind=='pyramid':
        im,d=canvas('Schematic perspective view; the orange slice is parallel to the base.')
        # Affine projection of a right pyramid; halfway cuts use t = 1/2 exactly.
        width,depth=(4,4) if s['square'] else (6,3)
        project=lambda x,y,z:(640+76*x-45*y,740-25*x-34*y-110*z)
        base=[project(-width/2,-depth/2,0),project(width/2,-depth/2,0),
              project(width/2,depth/2,0),project(-width/2,depth/2,0)]
        apex=project(0,0,4.5); t=s.get('cut_fraction',0.5 if s['halfway'] else 0.55)
        cut=[tuple((1-t)*np.array(p)+t*np.array(apex)) for p in base]
        for i in range(4):
            line(d,[base[i],base[(i+1)%4]],dashed=i in [1,2])
            line(d,[base[i],apex],dashed=i==2)
        # A translucent-looking fill keeps the slice distinct without naming its shape.
        d.polygon(cut,fill='#f7e5d7')
        line(d,cut+[cut[0]],ORANGE,5)
        line(d,[apex,cut[0]]);line(d,[apex,cut[1]]);line(d,[apex,cut[3]])
        label(d,(1000,420),'Slice',ORANGE)
        line(d,[(935,445),cut[1]],ORANGE,2)
        label(d,(640,890),'Square base' if s['square'] else 'Rectangular base')
        if s['halfway']:
            label(d,(260,180),'Slice at half the height',size=27)
        elif 'cut_fraction' in s:
            label(d,(320,180),'Slice at one-third the height',size=27)
        return im

    if kind in ['cube','box']:
        im,d=canvas('Schematic perspective view; dashed edges are hidden.')
        lengths=[1,1,1] if kind=='cube' else s['sides']
        sx,sy,sz=lengths
        project=lambda x,y,z:np.array([x*130+y*72,-y*65-z*110])
        raw=[project(x*sx,y*sy,z*sz) for z in (0,1) for y in (0,1) for x in (0,1)]
        low=np.min(raw,axis=0); high=np.max(raw,axis=0)
        scale=min(750/(high[0]-low[0]),610/(high[1]-low[1]))
        convert=lambda p:tuple((p-(low+high)/2)*scale+np.array([640,490]))
        pts=[convert(p) for p in raw]
        edges=[(0,1),(0,2),(1,3),(2,3),(4,5),(4,6),(5,7),(6,7),(0,4),(1,5),(2,6),(3,7)]
        if kind=='cube':
            cut=[convert(project(x,y,0.5)) for x,y in [(0,0),(1,0),(1,1),(0,1)]]
            d.polygon(cut,fill='#f7e5d7');line(d,cut+[cut[0]],ORANGE,5)
        for a,b in edges:line(d,[pts[a],pts[b]],dashed=(a,b) in [(0,2),(2,3),(2,6)])
        if kind=='cube':
            label(d,(640,865),'Orange slice: parallel to the top and bottom faces',ORANGE,size=27)
        else:
            line(d,[pts[0],pts[7]],ORANGE,5,dashed=True)
            label(d,tuple((np.array(pts[0])+pts[7])/2+[-95,-35]),'d = ?',ORANGE)
            for a,b,text,offset in [(0,1,sx,[0,42]),(1,3,sy,[55,20]),(1,5,sz,[50,0])]:
                label(d,tuple((np.array(pts[a])+pts[b])/2+offset),text)
        return im

    if kind in ['ladder','ramp']:
        im,d=canvas('Only the given measurements are labeled.')
        if kind=='ladder':run,rise=s['run'],s['rise']
        elif 'hypotenuse' in s:
            run=s['hypotenuse']*math.cos(math.radians(s['angle']))
            rise=s['hypotenuse']*math.sin(math.radians(s['angle']))
        else:run=s['run'];rise=run*math.tan(math.radians(s['angle']))
        scale=min(720/run,520/rise)
        A=(640-run*scale/2,760);B=(640+run*scale/2,760);C=(B[0],760-rise*scale)
        line(d,[(A[0]-70,760),(B[0]+70,760)],GRAY,4)
        line(d,[B,C],GRAY,5);line(d,[A,C],BLUE,7)
        line(d,[(B[0]-25,760),(B[0]-25,735),(B[0],735)],INK,3)
        mid=tuple((np.array(A)+C)/2+[-40,-35])
        if kind=='ladder':
            label(d,tuple(np.array(mid)+[-55,0]),'Ladder: ?',BLUE)
            label(d,((A[0]+B[0])/2,810),f'{run} ft')
            label(d,(B[0]+70,(B[1]+C[1])/2),f'{rise} ft')
            label(d,(B[0]+65,C[1]-35),'Wall',GRAY,size=25)
        else:
            label(d,(B[0]+90,(B[1]+C[1])/2),'Rise: ?')
            if 'hypotenuse' in s:label(d,mid,f'{s["hypotenuse"]} m',BLUE)
            else:label(d,((A[0]+B[0])/2,810),f'{s["run"]} m')
            theta=math.radians(s['angle'])
            arc=[(A[0]+85*math.cos(t),A[1]-85*math.sin(t)) for t in np.linspace(0,theta,80)]
            line(d,arc,ORANGE,3)
            label(d,(A[0]+130*math.cos(theta/2),A[1]-130*math.sin(theta/2)),f'{s["angle"]}°',ORANGE)
        return im

    if kind=='normal':
        im,d=canvas('The shaded region is the area above the mean.' if s['mode']=='area' else 'Find the value at the marked position using the given mean and standard deviation.')
        baseline=760
        xy=lambda z:(640+130*z,baseline-480*math.exp(-z*z/2))
        points=[xy(z) for z in np.linspace(-3.6,3.6,500)]
        if s['mode']=='area':
            d.polygon([(640,baseline)]+[xy(z) for z in np.linspace(0,3.6,250)]+[(1108,baseline)],fill='#dce8f2')
        line(d,[(140,baseline),(1140,baseline)],INK,3)
        line(d,points,BLUE,5);line(d,[(640,baseline),xy(0)],GRAY,2,dashed=True)
        label(d,(640,810),'Mean' if s['mode']=='area' else 'Mean = 50')
        if s['mode']=='standard-deviations':
            line(d,[(900,baseline),xy(2)],ORANGE,4)
            label(d,(900,810),'?',ORANGE)
            label(d,(640,140),'Standard deviation = 4')
            for a,b in [(640,770),(770,900)]:
                arrow(d,(a,240),(b,240),ORANGE,3)
                label(d,((a+b)/2,200),'+1 SD',ORANGE,size=24)
            label(d,(920,865),'2 standard deviations above the mean',size=23)
        return im

    if kind=='midpoint':
        im,d=canvas('Schematic only; M is the midpoint and AM = MB. No coordinate scale is shown.')
        A=np.array([230,330]);B=np.array([1050,730]);M=(A+B)/2
        line(d,[tuple(A),tuple(B)])
        for pt,text in zip([A,M,B],s['labels']):
            dot(d,tuple(pt));label(d,tuple(pt+[0,-55]),text)
        v=B-A;v=v/np.linalg.norm(v);normal=np.array([-v[1],v[0]])
        for pt in [(A+M)/2,(M+B)/2]:line(d,[tuple(pt-18*normal),tuple(pt+18*normal)],ORANGE,4)
        return im

    if kind=='histogram':
        p=Plot(s['title'],[0,10,0,8],ticks=[5,1],labels=['Interval','Frequency'])
        for a,b,height in zip(s['bins'],s['bins'][1:],s['frequencies']):
            p.pen.rectangle((*p.xy(a,height),*p.xy(b,0)),fill='#dce8f2',outline=BLUE,width=4)
            p.pen.text(p.xy((a+b)/2,height+0.35),str(height),font=font(28),fill=INK,anchor='mm')
        return p.finish()
    if kind in ['log','log-family']:
        h=s.get('shift',0)
        p=Plot(s['title'],[h-2,h+8,-5,5],ticks=[1,1],note=s.get('note',''))
        bases=s.get('bases',[s.get('base')])
        for base,color in zip(bases,[BLUE,ORANGE,GRAY]):
            # Sample by y, preserving resolution arbitrarily close to the asymptote.
            p.line([(h+base**y,y) for y in np.linspace(-5,5,2400) if base**y<=8],color=color)
        return p.finish()
    if kind=='rational':
        h=s['shift'];n=s['numerator']
        p=Plot(s['title'],[h-6,h+6,-6,6],ticks=[1,1],note=s.get('note',''))
        for lo,hi in [(h-6,h-0.001),(h+0.001,h+6)]:
            p.curve(lambda x:n/(x-h),lo=lo,hi=hi)
        return p.finish()
    if kind=='jump':
        p=Plot(s['title'],[-2,4,0,7],ticks=[1,1],note='Illustrative graph matching the stated jump; the value at x = 1 is not specified.')
        a=s['at'];p.line([(-2,s['left']),(a,s['left'])]);p.line([(a,s['right']),(4,s['right'])])
        p.point(a,s['left'],closed=False);p.point(a,s['right'],closed=False)
        return p.finish()
    if kind in ['segment','vector']:
        p=Plot(s['title'],s['bounds'],ticks=[1,1],equal_aspect=True)
        A,B=s['points'];p.line([A,B])
        if kind=='vector':
            arrow(p.pen,p.xy(*A),p.xy(*B))
            if s['steps']:
                C=[B[0],A[1]]
                p.line([A,C,B],color=ORANGE,width=3,dashed=True)
                p.pen.text(p.xy(2,-0.45),'4 right',font=font(25),fill=ORANGE,anchor='mm')
                p.pen.text(p.xy(4.8,1.5),'3 up',font=font(25),fill=ORANGE,anchor='mm')
            else:
                for pt,name in [(A,'Initial'),(B,'Terminal')]:
                    p.point(*pt,label=f'{name} ({pt[0]}, {pt[1]})')
        else:
            for pt in [A,B]:p.point(*pt,label=f'({pt[0]}, {pt[1]})')
        return p.finish()
    raise ValueError(kind)
