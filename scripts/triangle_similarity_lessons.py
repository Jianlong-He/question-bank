"""Similarity and bisector methods with geometrically valid original diagrams."""
from math import sin,cos,radians,sqrt,hypot,isclose
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons,draw_card,centered_math
import generate_sample_videos as v

SPECS=[
authored('geometry-triangle-sas-similarity','Identify SAS similarity from sides and an included angle',
 'One triangle has sides 4 cm and 7 cm enclosing 50°.\nAnother has sides 12 cm and 21 cm enclosing 50°.\nAre the triangles similar? Explain.',
 'Yes, by SAS similarity; the length scale factor is 3',
 'One triangle has sides four and seven centimetres enclosing fifty degrees. Another has sides twelve and twenty-one centimetres enclosing fifty degrees. Are they similar?',[
 ('COMPARE MATCHING SIDES','Use the same larger-to-smaller order','12/4 = 3; 21/7 = 3',
  'Both corresponding side pairs have ratio three. Use the same comparison order for both ratios.'),
 ('CHECK THE INCLUDED ANGLE','The angle must be between the two compared sides','50° = 50°',
  'The included angle is the angle between those sides. Both included angles measure fifty degrees.'),
 ('NAME THE CRITERION','Two proportional side pairs and an equal included angle','SAS similarity',
  'Two proportional side pairs and their equal included angle establish side-angle-side similarity.'),
 ('INTERPRET SIMILARITY','Corresponding angles match; corresponding lengths scale','Length scale factor = 3',
  'The triangles have the same shape. Corresponding angles are equal, and every corresponding length is multiplied by three.')],
 g(10,8,1,6),expression='12/4',value='3',equalities=[('21/7','3')]),

authored('geometry-right-triangle-similarity-ratios','Explain equal trigonometric ratios using similarity',
 'Two right triangles share acute angle θ.\nTheir sides are 8, 15, 17 and 24, 45, 51.\nCompare opposite ÷ hypotenuse for angle θ.',
 '8/17 = 24/51; similarity preserves the ratio',
 'Two right triangles share acute angle theta. Their sides are eight, fifteen, seventeen, and twenty-four, forty-five, fifty-one. Compare opposite side divided by hypotenuse for theta.',[
 ('MATCH TWO ANGLES','Each triangle has a right angle and the same acute angle','90° matches 90°; θ matches θ → AA',
  'Both right angles match, and the acute angles theta match. The triangles are similar by angle-angle.'),
 ('COMPARE CORRESPONDING SIDES','The larger triangle has every side three times as long','24/8 = 45/15 = 51/17 = 3',
  'Every side of the larger triangle is three times its corresponding side in the smaller triangle.'),
 ('FORM THE RATIOS','Use sides in the same positions relative to theta','Small: 8/17\nLarge: 24/51 = (3 × 8)/(3 × 17) = 8/17',
  'The small ratio is eight seventeenths. In the large ratio, the common factor three cancels, giving the same value.'),
 ('WHY TRIG RATIOS MATCH','A common length multiplier cancels from a side ratio','sin θ = opposite/hypotenuse = 8/17',
  'This ratio is sine theta. Similarity makes it independent of triangle size. The same cancellation explains equal cosine and tangent ratios.')],
 g(10,9,3,10),expression='24/51',value='8/17',equalities=[('8**2+15**2','17**2'),('24**2+45**2','51**2'),('24/8','3'),('45/15','3'),('51/17','3')]),

authored('geometry-triangle-angle-bisector-length','Use the triangle angle-bisector theorem',
 'In triangle ABC, AD bisects angle A and D lies on BC.\nAB = 12 cm, AC = 20 cm and DC = 15 cm.\nFind BD.',
 '9 centimetres',
 'In triangle A B C, A D bisects angle A and meets B C at D. A B is twelve centimetres, A C is twenty, and D C is fifteen. Find B D.',[
 ('MATCH THE SEGMENTS','The bisector divides the opposite side proportionally','BD/DC = AB/AC',
  'The angle-bisector theorem compares the two base segments with their adjacent triangle sides. B D over D C equals A B over A C.'),
 ('SUBSTITUTE','Keep the side pairs in matching order','BD/15 = 12/20 = 3/5',
  'Substitute the known lengths. The side ratio twelve to twenty simplifies to three to five.'),
 ('SOLVE FOR THE SEGMENT','Multiply both sides by fifteen','BD = 15 × (3/5) = 9 cm',
  'Multiply both sides by fifteen. B D is nine centimetres.'),
 ('CHECK','The two ratios must match','9/15 = 12/20 = 3/5\nBC = 9 + 15 = 24 cm',
  'Nine over fifteen matches twelve over twenty. The whole base is twenty-four centimetres, which also fits a triangle with sides twelve and twenty.')],
 g(10,8,'2HW',1),expression='15*12/20',value='9',equalities=[('9/15','12/20')]),
]

def bisector_points():
    return (20/3,sqrt(12**2-(20/3)**2)),(0,0),(24,0),(9,0)

def diagram(spec,d,scene,p):
    vid=spec['video_id']
    if scene not in (1,2,3):draw_card(spec,d,scene,p);return
    if vid=='geometry-triangle-sas-similarity':
        # Both triangles are to the same physical scale; the second is three times larger.
        for x,y,m,label in [(480,750,1,'small'),(850,750,3,'large')]:
            u=27*m;pts=[(x,y),(x+7*u,y),(x+4*u*cos(radians(50)),y-4*u*sin(radians(50)))]
            d.polygon(pts,fill='#D0E8E2',outline=v.TEAL,width=4)
            v.text(d,(x+3.5*u,y+25),f'{7*m} cm',29,v.INK,True,anchor='mm')
            v.text(d,(x+2*u*cos(radians(50))-35,y-2*u*sin(radians(50))-15),f'{4*m} cm',29,v.INK,True,anchor='mm')
            v.text(d,(x+65,y-26),'50°',26,v.INK,True,anchor='mm')
    elif vid=='geometry-right-triangle-similarity-ratios':
        for x,y,s,labels in [(550,700,15,('8','15','17')),(1000,700,23,('24','45','51'))]:
            pts=[(x,y),(x+15*s,y),(x,y-8*s)]
            d.polygon(pts,fill='#D0E8E2',outline=v.TEAL,width=4)
            d.line((x+15,y,x+15,y-15,x,y-15),fill=v.INK,width=3)
            v.text(d,(x-30,y-4*s),labels[0],30,v.INK,True,anchor='mm')
            v.text(d,(x+7.5*s,y+30),labels[1],30,v.INK,True,anchor='mm')
            v.text(d,(x+7.5*s+20,y-4*s-25),labels[2],30,v.INK,True,anchor='mm')
            v.text(d,(x+15*s+25,y-5),'θ',26,v.INK,True,anchor='mm')
        v.text(d,(960,380),'Diagrams shown at different display scales',27,v.MUTED,False,anchor='mm')
    else:
        A,B,C,D=bisector_points();coords=[(690+x*22,740-y*22) for x,y in [A,B,C,D]];aa,bb,cc,dd=coords
        d.polygon([aa,bb,cc],fill='#D0E8E2',outline=v.TEAL,width=4);d.line((*aa,*dd),fill='#B66F4E',width=4)
        for label,(x,y),(dx,dy) in zip('ABCD',coords,[(0,-28),(-23,20),(23,20),(0,28)]):v.text(d,(x+dx,y+dy),label,31,v.INK,True,anchor='mm')
        for a,b,label,dx,dy in [(aa,bb,'12 cm',-48,0),(aa,cc,'20 cm',35,-22),(dd,cc,'15 cm',0,42),(bb,dd,'?',0,42)]:
            v.text(d,((a[0]+b[0])/2+dx,(a[1]+b[1])/2+dy),label,30,v.INK,True,anchor='mm')
        v.text(d,(960,395),'AD divides angle A into two equal angles.',30,v.INK,True,anchor='mm')
    for i,line in enumerate(spec['displays'][scene].split('\n')):centered_math(d,845+i*58,line,40,v.TEAL)

def lessons(doc):
    A,B,C,D=bisector_points()
    assert isclose(hypot(A[0]-B[0],A[1]-B[1]),12)
    assert isclose(hypot(A[0]-C[0],A[1]-C[1]),20)
    assert 12+20>24 and 12+24>20 and 20+24>12
    # The bisector direction equals the sum of unit side vectors.
    u=((B[0]-A[0])/12+(C[0]-A[0])/20,(B[1]-A[1])/12+(C[1]-A[1])/20)
    w=(D[0]-A[0],D[1]-A[1]);assert isclose(u[0]*w[1]-u[1]*w[0],0,abs_tol=1e-9)
    batch=make_lessons(SPECS,doc)
    for spec in SPECS:v.DRAW[spec['video_id']]=lambda d,scene,p,s=spec:diagram(s,d,scene,p)
    return batch
