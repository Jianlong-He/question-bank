#!/usr/bin/env python3
"""Render selected Grade 7–12 question visuals from explicit mathematical data.

Run with the bundled Python runtime (Pillow and NumPy). Source CSVs are read-only.
Images contain given information or clearly identified illustrative examples,
not worked solutions. The JSON manifest records each question and graph recipe.
"""
from pathlib import Path
import csv
import hashlib
import json
import math
import re

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'images/worksheet-images'
REPORT = ROOT / 'images/generated-question-graphs.json'
BLUE = '#245a91'
INK = '#243342'
GRID = '#dce3e9'
ORANGE = '#ad5626'
FONT = '/System/Library/Fonts/Supplemental/Arial.ttf'


def font(size):
    return ImageFont.truetype(FONT, size)


class Plot:
    """A fixed-scale, clipped Cartesian plot; all data use mathematical units."""
    def __init__(self, title, bounds, ticks=(1, 1), labels=('x', 'y'), note='', size=(1280, 980), equal_aspect=False, xtick_format=None):
        self.image = Image.new('RGB', size, 'white')
        self.draw = ImageDraw.Draw(self.image)
        self.bounds = bounds
        self.xtick_format = xtick_format
        w, h = size
        self.rect = (120, 135, w - 65, h - 145)
        if equal_aspect:
            l,t,r,b=self.rect
            xmin,xmax,ymin,ymax=bounds
            scale=min((r-l)/(xmax-xmin),(b-t)/(ymax-ymin))
            cx,cy=(l+r)/2,(t+b)/2
            halfw,halfh=scale*(xmax-xmin)/2,scale*(ymax-ymin)/2
            self.rect=tuple(round(v) for v in (cx-halfw,cy-halfh,cx+halfw,cy+halfh))
        self.draw.text((w / 2, 40), title, font=font(34), fill=INK, anchor='mt')
        self.draw.text((w / 2, h - 35), note, font=font(23), fill=INK, anchor='mm')
        self.layer = Image.new('RGBA', size, (0, 0, 0, 0))
        self.pen = ImageDraw.Draw(self.layer)
        self.axes(ticks, labels)

    def xy(self, x, y):
        xmin, xmax, ymin, ymax = self.bounds
        l, t, r, b = self.rect
        return (l + (x - xmin) / (xmax - xmin) * (r - l),
                b - (y - ymin) / (ymax - ymin) * (b - t))

    def axes(self, ticks, labels):
        xmin, xmax, ymin, ymax = self.bounds
        l, t, r, b = self.rect
        for x in np.arange(math.ceil(xmin / ticks[0]) * ticks[0], xmax + 1e-8, ticks[0]):
            px, _ = self.xy(x, ymin)
            self.draw.line((px, t, px, b), fill=GRID, width=2)
            self.draw.text((px, b + 18), self.xtick_format(x) if self.xtick_format else f'{x:g}', font=font(24), fill=INK, anchor='mt')
        for y in np.arange(math.ceil(ymin / ticks[1]) * ticks[1], ymax + 1e-8, ticks[1]):
            _, py = self.xy(xmin, y)
            self.draw.line((l, py, r, py), fill=GRID, width=2)
            self.draw.text((l - 18, py), f'{y:g}', font=font(24), fill=INK, anchor='rm')
        self.draw.rectangle(self.rect, outline='#b3bdc7', width=2)
        if ymin <= 0 <= ymax:
            self.draw.line((*self.xy(xmin, 0), *self.xy(xmax, 0)), fill=INK, width=3)
        if xmin <= 0 <= xmax:
            self.draw.line((*self.xy(0, ymin), *self.xy(0, ymax)), fill=INK, width=3)
        self.draw.text(((l+r)/2, b+65), labels[0], font=font(28), fill=INK, anchor='mt')
        self.draw.text((l, t-30), labels[1], font=font(27), fill=INK, anchor='lb')

    def line(self, points, color=BLUE, width=5, dashed=False):
        pixels = [self.xy(float(x), float(y)) for x, y in points]
        if dashed:
            # Dash by pixel distance, independent of curve sampling density.
            offset = 0.0
            for (x1,y1),(x2,y2) in zip(pixels,pixels[1:]):
                length = math.hypot(x2-x1,y2-y1)
                if not length:
                    continue
                used = 0.0
                while used < length:
                    span = min(14 - offset % 14, length-used)
                    if int(offset // 14) % 2 == 0:
                        self.pen.line((x1+(x2-x1)*used/length,y1+(y2-y1)*used/length,
                                       x1+(x2-x1)*(used+span)/length,y1+(y2-y1)*(used+span)/length),fill=color,width=width)
                    used += span
                    offset += span
        elif len(pixels)>1:
            self.pen.line(pixels, fill=color, width=width, joint='curve')

    def curve(self, fn, lo=None, hi=None, **kwargs):
        xmin,xmax,_,_=self.bounds
        x = np.linspace(xmin if lo is None else lo, xmax if hi is None else hi, 1600)
        self.line([(a,fn(a)) for a in x], **kwargs)

    def point(self, x, y, closed=True, label=None, color=BLUE):
        px,py=self.xy(x,y)
        self.pen.ellipse((px-9,py-9,px+9,py+9),fill=color if closed else 'white',outline=color,width=4)
        if label:
            self.pen.text((px+16,py-16),label,font=font(25),fill=INK,anchor='lb')

    def finish(self):
        self.image.paste(self.layer.crop(self.rect), self.rect[:2], self.layer.crop(self.rect))
        return self.image


SPECS=[]
def add(sheet,qid,kind,title,expected,**data):
    grade=re.match(r'G(\d+)',sheet)[1]
    unit=re.match(r'G\d+U(\d+)',sheet)[1]
    source=f'worksheets/Grade {grade}/G{grade}Unit {unit}/{sheet}.csv'
    SPECS.append(dict(source_csv=source,question_id=str(qid),kind=kind,title=title,
                      expected=expected,**data))


# Grade 7: a graph of the given proportional relationship, or an unsolved number line.
add('G7U1W2',10,'line','Toy car: distance and time','y = 6x',bounds=[0,5,0,30],ticks=[1,5],
    m=6,c=0,labels=['Time (seconds)','Distance (meters)'])
add('G7U1W4',8,'line','Pay and hours worked','$68 for 4 hours',bounds=[0,10,0,170],ticks=[2,34],
    m=17,c=0,labels=['Hours worked','Pay ($)'],points=[[4,68],[8,136]])
add('G7U3W1',3,'numberline','Number line','start at -3',start=-3,bounds=[-12,4],
    note='Start at the marked point. Make the move described in the question.')
add('G7U3W1HW',3,'numberline','Number line','start at -4',start=-4,bounds=[-12,4],
    note='Start at the marked point. Make the move described in the question.')

# Grade 8: function tests and data patterns; invented scatter data are labeled illustrative.
add('G8U3W6',3,'circle','Circle','graph of a circle',bounds=[-4,4,-3,3],ticks=[1,1],radius=2,
    note='Illustrative circle; each grid step is 1 unit.')
add('G8U3W11',1,'line','Horizontal line','horizontal line',bounds=[-4,4,-3,3],ticks=[1,1],m=0,c=1,
    note='Illustrative horizontal line.')
add('G8U3W12',4,'function_choices','Three graphs','Vertical Line Test')
add('G8U3W12HW',4,'function_choices','Three graphs','Select the graph that passes the Vertical Line Test',
    batch='necessary-visual-audit',reason='Supply the actual three graph choices requested by the question.')
add('G8U7W1',3,'scatter','Scatter plot','straight upward line',bounds=[0,10,0,12],ticks=[1,2],
    points=[[1,2],[2,2.8],[3,4.3],[4,5],[5,6.2],[6,6.7],[7,8.3],[8,8.9],[9,10.2]],
    note='Illustrative data matching the pattern described in the question.')
cloud=[[1,5],[2,8],[3,2],[4,7],[5,4],[6,1],[7,9],[8,3],[9,6],[10,5],
       [1.5,2],[2.5,6],[3.5,9],[4.5,1],[5.5,7],[6.5,4],[7.5,6],[8.5,8],[9.5,2]]
add('G8U7W3',3,'scatter','Scatter plot','scattered randomly',bounds=[0,11,0,10],ticks=[1,1],points=cloud,
    note='Illustrative data matching the pattern described in the question.')
add('G8U7W3',6,'scatter','Scatter plot','curved pattern',bounds=[0,10,0,22],ticks=[1,2],
    points=[[1,1.2],[2,1.6],[3,2.7],[4,4.1],[5,6],[6,8.1],[7,11.3],[8,14.6],[9,18.1]],
    note='Illustrative data matching the pattern described in the question.')
add('G8U7W6',8,'scatter','Given data points','(2, 6)',bounds=[0,8,0,18],ticks=[1,2],
    points=[[2,6],[4,10],[6,14]],point_labels=True)
add('G8U7W6Rev',3,'scatter','Given data points','(2, 5)',bounds=[0,8,0,20],ticks=[1,2],
    points=[[2,5],[4,11],[6,17]],point_labels=True)

# Grade 9: preserve the specified solid/dashed boundary and shading direction.
add('G9U7W1',7,'inequality','Shaded coordinate plane','solid boundary y = 2x + 1',
    bounds=[-4,4,-6,6],ticks=[1,1],m=2,c=1,side='above',closed=True)
add('G9U7W1',8,'inequality','Shaded coordinate plane','dashed horizontal boundary y = -3',
    bounds=[-4,4,-6,6],ticks=[1,1],m=0,c=-3,side='below',closed=False)
add('G9U7W1Rev',2,'inequality','Shaded coordinate plane','solid boundary y = 3x + 2',
    bounds=[-4,4,-6,6],ticks=[1,1],m=3,c=2,side='above',closed=True)
add('G9U7W1Rev',3,'inequality','Shaded coordinate plane','dashed horizontal boundary y = -2',
    bounds=[-4,4,-6,6],ticks=[1,1],m=0,c=-2,side='below',closed=False)
add('G9U9W1',10,'scatter','Scatter plot','far from the main pattern',bounds=[0,10,0,22],ticks=[1,2],
    points=[[1,3],[2,4.7],[3,7.2],[4,9],[5,10.8],[6,13.1],[7,15],[8,16.8],[9,19],[3,19]],
    note='Illustrative data. No points have been classified or removed.')

# Grade 10: precise branch domains, endpoint inclusion, and quadratic intercepts.
add('G10U1W2',3,'piecewise','Piecewise function','y=-x for x<0 and y=x^2 for x>=0',
    bounds=[-5,4,-1,10],ticks=[1,1],note='y = -x for x < 0; y = x² for x ≥ 0.')
add('G10U1W2',8,'endpoints','Given endpoint markers','open circle at (2, 4)',
    bounds=[0,4,-3,6],ticks=[1,1],open_point=[2,4],closed_point=[2,-1],
    note='Only the endpoint information given in the question is shown.')
add('G10U1W2Rev',3,'endpoints','Given endpoint markers','open circle at (3, 1)',
    bounds=[0,6,-1,7],ticks=[1,1],open_point=[3,1],closed_point=[3,5],
    note='Only the endpoint information given in the question is shown.')
add('G10U3W1',10,'quadratic','Quadratic graph','crosses the x-axis at -4 and 6',
    bounds=[-6,8,-30,30],ticks=[1,5],roots=[-4,6],
    note='Illustrative quadratic with the stated x-intercepts; no symmetry line is added.')

# Grade 11: exact functions, with local views that retain the polynomial's true scale.
add('G11U13W3Rev',4,'reciprocal','y = 1/x','y = 1/x',bounds=[-6,6,-6,6],ticks=[1,1])
add('G11U4W3Rev',2,'polynomial','f(x) = (x + 1)²(x - 6)³','at x = 6',
    bounds=[5,7,-60,70],ticks=[0.25,10],note='Local view near x = 6.')
add('G11U4W3Rev',3,'polynomial','f(x) = (x + 1)²(x - 6)³','at x = -1',
    bounds=[-2,0,-550,50],ticks=[0.25,100],note='Local view near x = -1.')
add('G11U6W1HW',5,'shift','Two quadratic graphs','(x + 6)^2',
    bounds=[-10,4,-2,20],ticks=[1,2],
    note='Solid blue: y = x². Dashed orange: y = (x + 6)².')

# Grade 12: schematic functions satisfy the stated one-sided limits exactly.
add('G12U10W1',2,'limit','Graph near x = 2','y=4 from both sides',
    bounds=[-1,5,0,8],ticks=[1,1],at=2,left=4,right=4,
    note='Illustrative graph satisfying the stated approach from both sides.')
add('G12U10W1',3,'limit','Graph near x = 1','3 from the left and 5 from the right',
    bounds=[-2,4,0,8],ticks=[1,1],at=1,left=3,right=5,
    note='Illustrative graph satisfying the stated one-sided behavior.')
add('G12U10W1HW',2,'limit','Graph near x = 3','y = 7 from both sides',
    bounds=[0,6,3,11],ticks=[1,1],at=3,left=7,right=7,
    note='Illustrative graph satisfying the stated approach from both sides.')
add('G12U10W1HW',3,'limit','Graph near x = 4','2 from the left and 6 from the right',
    bounds=[1,7,-1,9],ticks=[1,1],at=4,left=2,right=6,
    note='Illustrative graph satisfying the stated one-sided behavior.')
add('G12U10W1Rev',1,'limit','Graph near x = 0','y = -2 from both sides',
    bounds=[-3,3,-6,2],ticks=[1,1],at=0,left=-2,right=-2,
    note='Illustrative graph satisfying the stated approach from both sides.')
add('G12U10W1Rev',2,'limit','Graph near x = 5','f(5) = 9',
    bounds=[2,8,-1,11],ticks=[1,1],at=5,left=1,right=1,value=9,
    note='Illustrative graph; the filled point records the stated function value.')


from question_graph_expansion import add_specs, render_extra
add_specs(add)
from question_graph_gaps import add_gap_specs, render_gap
add_gap_specs(add)
from question_graph_listed import add_listed_specs, render_listed
add_listed_specs(add)
from question_graph_remaining import add_remaining_specs, render_remaining
add_remaining_specs(add)


def render(spec):
    kind=spec['kind']
    if kind.startswith('remaining_'):
        return render_remaining(spec, Plot, font)
    if kind.startswith('listed_'):
        return render_listed(spec, Plot, font)
    if kind.startswith('gap_'):
        return render_gap(spec, Plot, font)
    if kind.startswith('extra_'):
        return render_extra(spec, Plot, font)
    if kind=='numberline':
        im=Image.new('RGB',(1280,520),'white');d=ImageDraw.Draw(im)
        d.text((640,40),spec['title'],font=font(34),fill=INK,anchor='mt')
        lo,hi=spec['bounds'];px=lambda x:100+(x-lo)/(hi-lo)*1080
        d.line((80,245,1200,245),fill=INK,width=4)
        d.polygon([(80,245),(95,237),(95,253)],fill=INK)
        d.polygon([(1200,245),(1185,237),(1185,253)],fill=INK)
        for x in range(lo,hi+1):
            d.line((px(x),232,px(x),258),fill=INK,width=3)
            d.text((px(x),280),str(x),font=font(26),fill=INK,anchor='mt')
        x=px(spec['start']);d.ellipse((x-10,235,x+10,255),fill=BLUE)
        d.text((x,195),'Start',font=font(28),fill=BLUE,anchor='mb')
        d.text((640,430),spec['note'],font=font(25),fill=INK,anchor='mm')
        return im
    if kind=='function_choices':
        im=Image.new('RGB',(1920,820),'white')
        for i,title in enumerate(['Circle','S-curve on its side','Straight line (diagonal)']):
            p=Plot(title,[-3,3,-3,3],size=(640,800),equal_aspect=True)
            # Square plotting region for equal x/y scale in each choice.
            if i==0:
                p.line([(2*math.cos(t),2*math.sin(t)) for t in np.linspace(0,2*math.pi,800)])
            elif i==1:
                p.line([(y**3-y,y) for y in np.linspace(-1.7,1.7,800)])
            else:p.curve(lambda x:x)
            im.paste(p.finish(),(640*i,0))
        return im
    p=Plot(spec['title'],spec['bounds'],spec.get('ticks',(1,1)),spec.get('labels',('x','y')),spec.get('note',''),equal_aspect=(kind=='circle'))
    xmin,xmax,ymin,ymax=spec['bounds']
    if kind=='inequality':
        # Clip a translucent half-plane to the plot while retaining grid visibility.
        l,t,r,b=p.rect
        for px in range(l,r+1):
            x=xmin+(px-l)/(r-l)*(xmax-xmin)
            y=spec['m']*x+spec['c'];py=p.xy(x,max(ymin,min(ymax,y)))[1]
            if spec['side']=='above' and y<ymax:
                p.pen.line((px,t,px,py),fill=(36,90,145,45))
            elif spec['side']=='below' and y>ymin:
                p.pen.line((px,py,px,b),fill=(36,90,145,45))
        p.curve(lambda x:spec['m']*x+spec['c'],dashed=not spec['closed'])
    elif kind=='line':p.curve(lambda x:spec['m']*x+spec['c'])
    elif kind=='circle':p.line([(spec['radius']*math.cos(t),spec['radius']*math.sin(t)) for t in np.linspace(0,2*math.pi,1000)])
    elif kind=='piecewise':
        p.curve(lambda x:-x,hi=0);p.curve(lambda x:x*x,lo=0);p.point(0,0)
    elif kind=='endpoints':
        p.point(*spec['open_point'],closed=False)
        p.point(*spec['closed_point'],closed=True)
    elif kind=='quadratic':
        a,b=spec['roots'];p.curve(lambda x:(x-a)*(x-b));p.point(a,0);p.point(b,0)
    elif kind=='reciprocal':
        p.curve(lambda x:1/x,hi=-0.04);p.curve(lambda x:1/x,lo=0.04)
    elif kind=='polynomial':p.curve(lambda x:(x+1)**2*(x-6)**3)
    elif kind=='shift':
        p.curve(lambda x:x*x);p.curve(lambda x:(x+6)**2,color=ORANGE,dashed=True)
    elif kind=='limit':
        a=spec['at'];left=spec['left'];right=spec['right']
        p.curve(lambda x:left+0.3*(x-a),hi=a)
        p.curve(lambda x:right+0.3*(x-a),lo=a)
        p.point(a,left,closed=False);p.point(a,right,closed=False)
        if 'value' in spec:p.point(a,spec['value'])
    elif kind!='scatter':raise ValueError(kind)
    for x,y in spec.get('points',[]):
        p.point(x,y,label=f'({x:g}, {y:g})' if spec.get('point_labels') else None)
    return p.finish()


def main():
    entries=[];source_hashes={}
    previous={e['output_file']:e['sha256'] for e in json.loads(REPORT.read_text())['images']} if REPORT.exists() else {}
    for spec in SPECS:
        source=ROOT/spec['source_csv'];source_hashes[source]=hashlib.sha256(source.read_bytes()).hexdigest()
        with source.open(encoding='utf-8-sig',newline='') as handle:
            rows=list(csv.DictReader(handle))
        row=next(r for r in rows if r['Question ID']==spec['question_id'])
        assert spec['expected'] in row['Question Choices'],(source,row['Question Choices'])
        assert not any(v.strip() for k,v in row.items() if k and 'image' in k.lower() and v),source
        folder=OUT/source.relative_to(ROOT/'worksheets').parent/source.stem
        target=folder/f'WS-{source.stem}Q{spec["question_id"]}I1.png'
        image=render(spec)
        if target.exists():
            with Image.open(target) as old:identical=old.size==image.size and old.convert('RGB').tobytes()==image.tobytes()
            if not identical:
                # Update only our own generated image, provided nobody has edited it.
                assert previous.get(str(target.relative_to(ROOT)))==hashlib.sha256(target.read_bytes()).hexdigest(),target
                image.save(target)
        else:
            folder.mkdir(parents=True,exist_ok=True);image.save(target)
        with Image.open(target) as check:check.verify()
        entries.append({**spec,'question':row['Question Choices'],
                        'output_file':str(target.relative_to(ROOT)),
                        'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
                        'dimensions':list(image.size),'method':'deterministic mathematical rendering with Pillow/NumPy'})
    for path,digest in source_hashes.items():assert hashlib.sha256(path.read_bytes()).hexdigest()==digest,path
    REPORT.write_text(json.dumps({'summary':{'images_created':len(entries),'worksheets':len(source_hashes),
                       'grades':[7,8,9,10,11,12],'csv_contents_changed':False},'images':entries},indent=2)+'\n')
    # Small previews are for visual inspection, not question assets.
    contact=Image.new('RGB',(1600,math.ceil(len(entries)/4)*290),'#e8edf1')
    d=ImageDraw.Draw(contact)
    for i,e in enumerate(entries):
        with Image.open(ROOT/e['output_file']) as im:
            im.thumbnail((390,245));x=(i%4)*400+(400-im.width)//2;y=(i//4)*290
            contact.paste(im,(x,y))
        d.text(((i%4)*400+10,(i//4)*290+250),Path(e['output_file']).stem,font=font(18),fill=INK)
    contact.save(ROOT/'images/generated-question-graphs-preview.jpg',quality=92)
    preview_dir=ROOT/'images/graph-previews'
    preview_dir.mkdir(exist_ok=True)
    for grade in range(7,13):
        subset=[e for e in entries if f'/Grade {grade}/' in e['source_csv'] and e.get('batch')=='coverage-expansion']
        if not subset:
            continue
        sheet=Image.new('RGB',(1600,math.ceil(len(subset)/4)*330),'#e8edf1')
        sd=ImageDraw.Draw(sheet)
        for i,e in enumerate(subset):
            with Image.open(ROOT/e['output_file']) as im:
                im.thumbnail((390,290));x=(i%4)*400+(400-im.width)//2;y=(i//4)*330
                sheet.paste(im,(x,y))
            sd.text(((i%4)*400+8,(i//4)*330+295),Path(e['output_file']).stem,font=font(18),fill=INK)
        sheet.save(preview_dir/f'grade-{grade}-additional.jpg',quality=95)
    # Separate contact sheets keep the priority-gap batch easy to review.
    for batch in ['priority-gaps','listed-questions','remaining-visuals']:
        gaps=[e for e in entries if e.get('batch')==batch]
        page_size=10 if batch=='priority-gaps' else 8
        for page,start in enumerate(range(0,len(gaps),page_size),1):
            subset=gaps[start:start+page_size]
            sheet=Image.new('RGB',(1280,math.ceil(len(subset)/2)*530),'#e8edf1')
            sd=ImageDraw.Draw(sheet)
            for i,e in enumerate(subset):
                with Image.open(ROOT/e['output_file']) as im:
                    im.thumbnail((630,480));x=(i%2)*640+(640-im.width)//2;y=(i//2)*530
                    sheet.paste(im,(x,y))
                sd.text(((i%2)*640+12,(i//2)*530+490),Path(e['output_file']).stem,font=font(21),fill=INK)
            sheet.save(preview_dir/f'{batch}-{page}.jpg',quality=95)
    print(json.dumps(json.loads(REPORT.read_text())['summary'],indent=2))


if __name__=='__main__':
    main()
