"""Solids of revolution, with explicit axis and new profile dimensions."""
from math import pi,sin,cos
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons,centered_math
import generate_sample_videos as v

SPECS=[
authored('geometry-revolution-rectangle','Rotate a rectangle to create a cylinder',
 'Rotate a filled 3 cm by 7 cm rectangle one full turn\nabout a 7 cm side. Name the solid and its dimensions.',
 'Cylinder: radius 3 cm, height 7 cm',
 'Rotate a filled three by seven centimetre rectangle one full turn about a seven centimetre side. Name the solid and its dimensions.',[
 ('AXIS','The seven-centimetre side stays fixed','Axis length = 7 cm',
  'The seven-centimetre side is the axis of rotation. It stays fixed and becomes the height of the solid.'),
 ('RADIUS','Distance from the axis becomes a circular radius','Radius = 3 cm',
  'The opposite side is three centimetres from the axis. As it turns, that distance becomes the circular radius.'),
 ('SOLID','Every height has the same circular cross-section','Cylinder: radius 3 cm; height 7 cm',
  'Every horizontal slice sweeps out a disk of the same radius. Stacking those disks creates a cylinder.'),
 ('CHECK','The diameter is twice the radius','Diameter = 6 cm; height = 7 cm',
  'The diameter is six centimetres, while the height stays seven. The perpendicular distance from the axis gives the radius, not the diameter.')],
 g(10,10,1,7),expression='2*3',value='6'),

authored('geometry-revolution-right-triangle','Rotate a right triangle to create a cone',
 'A filled right triangle has legs 4 cm and 9 cm.\nRotate it one full turn about the 9 cm leg.\nName the solid, its radius, and its height.',
 'Cone: radius 4 cm, height 9 cm',
 'A filled right triangle has legs four and nine centimetres. Rotate it one full turn about the nine centimetre leg. Name the solid, its radius, and its height.',[
 ('AXIS','The nine-centimetre leg becomes the height','Height = 9 cm',
  'The nine-centimetre leg stays fixed as the rotation axis, so the solid has height nine centimetres.'),
 ('BASE','The perpendicular leg sweeps out a disk','Base radius = 4 cm',
  'The four-centimetre leg sweeps out the circular base. Its length is the radius.'),
 ('TAPER','The hypotenuse sweeps out the sloping surface','The solid is a cone.',
  'The hypotenuse sweeps out a surface that narrows to the top point. The resulting solid is a cone.'),
 ('CHECK','Distinguish the base diameter from its radius','Radius = 4 cm; diameter = 8 cm; height = 9 cm',
  'The radius is four, the diameter is eight, and the height is nine centimetres. Rotating about the other leg would interchange the radius and height.')],
 g(10,10,1,8),expression='2*4',value='8'),

authored('geometry-revolution-semicircle','Rotate a semicircle to create a sphere',
 'A filled semicircle has radius 6 cm. Rotate it\none full turn about its diameter. Name the solid\nand give its radius and diameter.',
 'Sphere: radius 6 cm, diameter 12 cm',
 'A filled semicircle has radius six centimetres. Rotate it one full turn about its diameter. Name the solid and give its radius and diameter.',[
 ('AXIS','The straight diameter is the rotation axis','Axis through the center; length 12 cm',
  'The straight diameter stays fixed. It passes through the center and has length twelve centimetres.'),
 ('SURFACE','The curved edge stays six centimetres from the center','Every surface point has radius 6 cm.',
  'As the curved edge turns, it sweeps all directions around the axis while staying six centimetres from the center.'),
 ('SOLID','The filled region sweeps out the interior too','The solid is a sphere of radius 6 cm.',
  'The curved edge makes a spherical surface, and the filled region sweeps out its interior. The resulting solid is a sphere of radius six centimetres.'),
 ('CHECK','A full turn uses the entire diameter as its axis','Diameter = 2 × 6 = 12 cm',
  'The sphere has diameter twelve centimetres. Rotating a semicircle about its diameter makes a full sphere, not half of one.')],
 g(10,10,'1HW',4),expression='2*6',value='12'),
]


def diagram(spec,d,scene,p):
    vid=spec['video_id'];orange='#B66F4E';fill='#D4E8E1'
    v.text(d,(480,330),'REGION AND AXIS',28,v.MUTED,True)
    v.text(d,(1120,330),'AFTER ONE FULL TURN',28,v.MUTED,True)
    if vid.endswith('rectangle'):
        d.rectangle((550,420,670,700),fill=fill,outline=v.TEAL,width=4)
        d.line((550,390,550,735),fill=orange,width=5)
        v.text(d,(435,550),'7 cm',32,v.INK,True);v.text(d,(568,710),'3 cm',30,v.INK,True)
        d.rectangle((1160,420,1400,700),fill=fill)
        d.ellipse((1160,670,1400,730),fill=fill,outline=v.TEAL,width=4)
        d.line((1160,420,1160,700),fill=v.TEAL,width=4);d.line((1400,420,1400,700),fill=v.TEAL,width=4)
        d.ellipse((1160,390,1400,450),fill=fill,outline=v.TEAL,width=4)
        d.line((1280,420,1400,420),fill=orange,width=3)
        v.text(d,(1300,455),'r = 3 cm',30,v.INK,True);v.text(d,(1430,550),'h = 7 cm',30,v.INK,True)
    elif vid.endswith('right-triangle'):
        d.polygon([(550,390),(550,750),(710,750)],fill=fill,outline=v.TEAL,width=4)
        d.line((550,365,550,780),fill=orange,width=5)
        v.text(d,(435,560),'9 cm',32,v.INK,True);v.text(d,(595,765),'4 cm',30,v.INK,True)
        d.polygon([(1280,390),(1120,750),(1440,750)],fill=fill)
        d.ellipse((1120,710,1440,790),fill=fill,outline=v.TEAL,width=4)
        d.line((1120,750,1280,390,1440,750),fill=v.TEAL,width=4)
        d.line((1280,390,1280,750),fill=orange,width=3)
        d.line((1280,750,1440,750),fill=orange,width=3)
        v.text(d,(1310,540),'h = 9 cm',30,v.INK,True);v.text(d,(1315,795),'r = 4 cm',30,v.INK,True)
    else:
        cx,cy,r=570,565,180
        pts=[(cx,cy-r)]+[(cx+r*cos(-pi/2+i*pi/90),cy+r*sin(-pi/2+i*pi/90)) for i in range(91)]
        d.polygon(pts,fill=fill,outline=v.TEAL,width=4)
        d.line((cx,cy-r-25,cx,cy+r+25),fill=orange,width=5)
        d.line((cx,cy,cx+r,cy),fill=orange,width=3)
        v.text(d,(cx+35,cy+22),'6 cm',32,v.INK,True)
        cx=1280
        d.ellipse((cx-r,cy-r,cx+r,cy+r),fill=fill,outline=v.TEAL,width=4)
        d.ellipse((cx-r,cy-50,cx+r,cy+50),outline='#91B6A8',width=3)
        d.ellipse((cx-60,cy-r,cx+60,cy+r),outline='#91B6A8',width=3)
        d.line((cx,cy,cx+r,cy),fill=orange,width=3)
        v.text(d,(cx+28,cy+55),'r = 6 cm',30,v.INK,True)
    v.text(d,(815,540),'full turn →',30,v.MUTED,True)
    label='Rotate the filled region about the orange axis.' if scene==0 else spec['displays'][scene]
    centered_math(d,890,label,40,v.TEAL)


def lessons(doc):
    batch=make_lessons(SPECS,doc)
    for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:diagram(s,d,scene,p)
    return batch
