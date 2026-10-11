"""Shared precise drawing primitives for unit-test illustrations."""
import math
import numpy as np
from PIL import Image, ImageDraw
from generate_question_graphs import Plot, font, BLUE, INK, ORANGE
GRAY = '#71808d'
PALE = '#e4eef7'


def canvas(title, note='', size=(1280,980)):
    im=Image.new('RGB',size,'white');d=ImageDraw.Draw(im)
    label(d,(size[0]/2,60),title,size=34)
    label(d,(size[0]/2,size[1]-48),note,size=23)
    return im,d


def label(d,p,text,color=INK,size=29):
    d.text(tuple(p),str(text),font=font(size),fill=color,anchor='mm')


def line(d,pts,color=BLUE,width=4,dashed=False):
    pts=[tuple(p) for p in pts]
    if not dashed:
        d.line(pts,fill=color,width=width,joint='curve');return
    for a,b in zip(pts,pts[1:]):
        a=np.array(a);v=np.array(b)-a;n=np.linalg.norm(v)
        if not n:continue
        for t in np.arange(0,n,24):d.line([tuple(a+v*t/n),tuple(a+v*min(n,t+12)/n)],fill=color,width=width)


def polygon(d,pts,fill=PALE,color=BLUE):
    d.polygon([tuple(p) for p in pts],fill=fill)
    line(d,list(pts)+[pts[0]],color)


def dot(d,p,color=BLUE,closed=True,r=8):
    x,y=p;d.ellipse((x-r,y-r,x+r,y+r),fill=color if closed else 'white',outline=color,width=3)


def arrow(d,a,b,color=BLUE,width=5):
    a=np.array(a);b=np.array(b);u=(b-a)/np.linalg.norm(b-a);v=np.array([-u[1],u[0]])
    line(d,[a,b],color,width);d.polygon([tuple(b),tuple(b-19*u+8*v),tuple(b-19*u-8*v)],fill=color)


def arc(d,c,r,a,b,color=ORANGE,width=3,head=False):
    pts=[(c[0]+r*math.cos(t),c[1]-r*math.sin(t)) for t in np.linspace(math.radians(a),math.radians(b),100)]
    line(d,pts,color,width)
    if head:arrow(d,pts[-6],pts[-1],color,width)


def angle(d,a,v,b,text='',r=52,offset=95):
    t1=math.degrees(math.atan2(v[1]-a[1],a[0]-v[0]));t2=math.degrees(math.atan2(v[1]-b[1],b[0]-v[0]))
    delta=(t2-t1+180)%360-180
    arc(d,v,r,t1,t1+delta)
    theta=math.radians(t1+delta/2)
    if text:label(d,(v[0]+offset*math.cos(theta),v[1]-offset*math.sin(theta)),text,ORANGE,27)


def right(d,a,v,b,size=22):
    a=np.array(a);v=np.array(v);b=np.array(b)
    u=(a-v)/np.linalg.norm(a-v)*size;w=(b-v)/np.linalg.norm(b-v)*size
    line(d,[v+u,v+u+w,v+w],GRAY,3)


def midlabel(d,a,b,text,off=(0,35),color=INK,size=28):
    label(d,(np.array(a)+b)/2+off,text,color,size)


def dimension(d,a,b,text,off=(0,34)):
    a=np.array(a);b=np.array(b);u=(b-a)/np.linalg.norm(b-a);v=np.array([-u[1],u[0]])
    line(d,[a,b],GRAY,2)
    for p in [a,b]:line(d,[p-8*v,p+8*v],GRAY,2)
    midlabel(d,a,b,text,off,size=26)


def fit(points,box=(220,230,1060,760)):
    pts=np.array(points,dtype=float);lo=pts.min(axis=0);hi=pts.max(axis=0)
    scale=min((box[2]-box[0])/max(.01,hi[0]-lo[0]),(box[3]-box[1])/max(.01,hi[1]-lo[1]))
    center=np.array([(box[0]+box[2])/2,(box[1]+box[3])/2])
    return [tuple((p-(lo+hi)/2)*[scale,-scale]+center) for p in pts]


def prism(d,box=(350,330,800,700),depth=(140,-110),dimensions=None):
    l,t,r,b=box;v=np.array(depth)
    front=np.array([(l,b),(r,b),(r,t),(l,t)]);back=front+v
    polygon(d,[front[3],front[2],back[2],back[3]],'#f0f5fa')
    polygon(d,[front[1],back[1],back[2],front[2]],'#d3e3f0')
    polygon(d,front)
    for a,bp in [(back[0],back[1]),(back[0],back[3]),(back[0],front[0])]:line(d,[a,bp],GRAY,3,True)
    if dimensions:
        x,y,z=dimensions
        midlabel(d,front[0],front[1],x,(0,42),size=25)
        midlabel(d,front[1],back[1],y,(45,25),size=25)
        midlabel(d,front[0],front[3],z,(-65,0),size=25)
    return front,back


def number_axis(d,lo,hi,y=620,left=130,right=1150,step=1,fmt=None):
    x=lambda n:left+(n-lo)/(hi-lo)*(right-left)
    arrow(d,(left-25,y),(right+25,y),INK,3)
    for n in np.arange(lo,hi+step*.01,step):
        line(d,[(x(n),y-10),(x(n),y+10)],INK,2)
        label(d,(x(n),y+42),fmt(n) if fmt else f'{n:g}',size=24)
    return x


def bar_chart(title,labels,values,ylabel='Count',hist=False):
    im,d=canvas(title);left,right,top,bottom=170,1150,200,780
    ymax=max(values)+1;step=1 if ymax<12 else 2;ymax=math.ceil(ymax/step)*step
    yy=lambda v:bottom-v/ymax*(bottom-top)
    for v in range(0,ymax+1,step):
        line(d,[(left,yy(v)),(right,yy(v))],'#dce3e9',2)
        label(d,(left-35,yy(v)),v,size=23)
    width=(right-left)/len(values)
    for i,(name,value) in enumerate(zip(labels,values)):
        x=left+i*width;pad=0 if hist else width*.19
        d.rectangle((x+pad,yy(value),x+width-pad,bottom),fill=PALE,outline=BLUE,width=3)
        label(d,(x+width/2,bottom+48),name,size=23)
    line(d,[(left,top),(left,bottom),(right,bottom)],INK,3)
    label(d,(left+15,top-40),ylabel,size=24)
    return im
