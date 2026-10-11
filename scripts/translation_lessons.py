"""Translations, inverse/composite vectors, and rigid-motion properties."""
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons,draw_card,centered_math
from reflection_lessons import axes,point
import generate_sample_videos as v

SPECS=[
authored('geometry-translation','Translate a point using a vector',
 'Translate P(−6, −2) by vector <8, −5>.\nFind the image coordinates.', '(2, −7)',
 'Translate negative six, negative two by the vector eight, negative five. Find the image coordinates.',[
 ('READ THE VECTOR','Horizontal change first; vertical change second','<8, −5>: 8 right, 5 down',
  'The first component changes x, and the second changes y. Here we move eight units right and five down. A zero component means no movement in that direction.'),
 ('ADD TO X','Apply the horizontal change','x′ = −6 + 8 = 2',
  'Add eight to negative six. The new x-coordinate is two.'),
 ('ADD TO Y','Apply the vertical change','y′ = −2 + (−5) = −7',
  'Add negative five to negative two. The new y-coordinate is negative seven.'),
 ('WRITE THE IMAGE','Every point receives the same slide','P′ = (2, −7)\n(x, y) → (x + 8, y − 5)',
  'The image is two, negative seven. This same vector slides every point the same distance in the same direction. That transformation is a translation.')],
 g(8,6,1,2),expression='-6+8',value='2',equalities=[('-2-5','-7')]),

authored('geometry-translation-find-vector','Find a translation vector from two positions',
 'A translation sends P(−7, 6) to P′(2, −4).\nFind its horizontal and vertical changes.', '<9, −10>',
 'A translation sends negative seven, six to two, negative four. Find the horizontal and vertical changes.',[
 ('DIFFERENCE RULE','Subtract original from image in each coordinate','Change = image coordinate − original coordinate',
  'For each coordinate, subtract the original value from the image value. Keep that order.'),
 ('HORIZONTAL','Image x minus original x','Δx = 2 − (−7) = 9',
  'Two minus negative seven equals nine. The point moves nine units right.'),
 ('VERTICAL','Image y minus original y','Δy = −4 − 6 = −10',
  'Negative four minus six equals negative ten. The point moves ten units down.'),
 ('CHECK','Add the changes to the original point','Vector <9, −10>\n(−7 + 9, 6 − 10) = (2, −4)',
  'The translation vector is nine, negative ten. Adding it to the original point gives the stated image. These are signed coordinate changes, not a single total distance.')],
 g(8,6,4,1),expression='2-(-7)',value='9',equalities=[('-4-6','-10')]),

authored('geometry-translation-inverse','Reverse a translation by negating its vector',
 'What translation reverses the rule\n(x, y) → (x − 4, y + 7)?', '(x, y) → (x + 4, y − 7)',
 'What translation reverses the rule x minus four, y plus seven?',[
 ('ORIGINAL MOVE','Read the changes separately','Original vector = <−4, 7>',
  'The original move takes every point four units left and seven up.'),
 ('REVERSE BOTH','Undo each change with its opposite','Inverse vector = <4, −7>',
  'To undo the move, go four right and seven down. Negate both vector components.'),
 ('WRITE THE RULE','The two translations must add to zero','(x, y) → (x + 4, y − 7)',
  'The inverse rule adds four to x and subtracts seven from y.'),
 ('CHECK','Try an original point and return it to its start','(3, −2) → (−1, 5) → (3, −2)',
  'Three, negative two first becomes negative one, five. The inverse returns it to three, negative two. Each forward change is exactly canceled.')],
 g(9,15,2,6),identities=[('(x-4)+4','x'),('(y+7)-7','y')],equalities=[('3-4','-1'),('-2+7','5')]),

authored('geometry-translation-compose','Combine two translation vectors',
 'Apply translation <−6, 8>, then <9, −5>.\nFind one vector with the same overall effect.', '<3, 3>',
 'Apply the translation negative six, eight, followed by nine, negative five. Find one vector with the same overall effect.',[
 ('COMBINE LIKE COMPONENTS','Add horizontal to horizontal and vertical to vertical','<−6 + 9, 8 + (−5)>',
  'Add the horizontal changes together and the vertical changes together. Do not mix the two coordinates.'),
 ('HORIZONTAL','Six left followed by nine right','−6 + 9 = 3',
  'Six left followed by nine right gives three units right overall.'),
 ('VERTICAL','Eight up followed by five down','8 − 5 = 3',
  'Eight up followed by five down gives three units up overall.'),
 ('RESULT','One translation produces the same final position','Combined vector = <3, 3>\n(x, y) → (x + 3, y + 3)',
  'The combined vector is three, three. Every point finishes three units right and three up from where it started.')],
 g(9,15,2,9),expression='-6+9',value='3',equalities=[('8-5','3')]),

authored('geometry-translation-rigid-properties','Use the measurements preserved by translations',
 'A triangle has sides 6, 8, and 10 cm and a right angle.\nTranslate it by <−7, 3>. Find its new perimeter\nand right-angle measure. Is the image congruent?',
 '24 cm; 90 degrees; yes',
 'A triangle has sides six, eight, and ten centimetres and a right angle. Translate it by negative seven, three. Find the new perimeter and right-angle measure, and decide whether it is congruent.',[
 ('SIDE LENGTHS','Sliding every point equally preserves distances','Image sides: 6, 8, 10 cm',
  'A translation slides every point by the same vector. Distances between points stay the same, so all side lengths are unchanged.'),
 ('PERIMETER','Add the unchanged side lengths','P′ = 6 + 8 + 10 = 24 cm',
  'The image perimeter is six plus eight plus ten, or twenty-four centimetres.'),
 ('ANGLES','A translation preserves the shape as well as its size','Right angle stays 90°',
  'Angle measures stay the same too, so the right angle remains ninety degrees.'),
 ('RIGID MOTIONS','Preserved lengths and angles give congruence','Translations, rotations, reflections: rigid motions',
  'The image is congruent. Translations, rotations, and reflections are rigid motions. Any sequence of these preserves lengths and angles, so its final image is also congruent.')],
 g(9,15,1,5),expression='6+8+10',value='24',equalities=[('6**2+8**2','10**2')]),

authored('geometry-translation-then-dilation','Decide whether a mixed transformation is rigid',
 'A segment is 8 cm long. Translate it, then dilate\nby scale factor 0.75. Find the final length.\nIs the combined transformation rigid?',
 '6 cm; not rigid',
 'A segment is eight centimetres long. Translate it, then dilate by scale factor zero point seven five. Find the final length and decide whether the combined transformation is rigid.',[
 ('TRANSLATION','The slide does not change the length','After translation: 8 cm',
  'Translation preserves distances. The segment is still eight centimetres long after the slide.'),
 ('DILATION','Apply the length scale factor','Final length = 8 × 0.75 = 6 cm',
  'The dilation multiplies length by zero point seven five, giving six centimetres.'),
 ('RIGIDITY','A rigid transformation must preserve every distance','6 ≠ 8, so the sequence is not rigid.',
  'The final length differs from the original. Therefore, this sequence is not rigid.'),
 ('CHECK THE FACTOR','Dilation does not always change lengths','|k| = 1: lengths preserved\n|k| ≠ 1: lengths change',
  'Check the factor rather than the name alone. Dilation scales lengths by the absolute value of k. At one or negative one, it preserves distances; other nonzero factors change them.')],
 g(9,16,2,5),expression='8*0.75',value='6'),
]


def diagram(spec,d,scene,p):
    vid=spec['video_id']
    if vid in ('geometry-translation','geometry-translation-find-vector') and scene in (1,4):
        xy=axes(d)
        a,b=((-6,-2),(2,-7)) if vid=='geometry-translation' else ((-7,6),(2,-4))
        mid=(b[0],a[1])
        d.line([xy(*a),xy(*mid),xy(*b)],fill='#B66F4E',width=4)
        X,Y=xy(*b);direction=1 if b[1]<a[1] else -1
        d.polygon([(X,Y),(X-8,Y-15*direction),(X+8,Y-15*direction)],fill='#B66F4E')
        point(d,xy,*a,f'P{a}',(-190,-35));point(d,xy,*b,f'P′{b}',(12,8))
        v.text(d,xy((a[0]+b[0])/2,a[1]+1),'+8' if vid=='geometry-translation' else '+9',30,v.INK,True)
        v.text(d,xy(b[0]+.7,(a[1]+b[1])/2),'−5' if vid=='geometry-translation' else '−10',30,v.INK,True)
        centered_math(d,910,'Vector <8, −5>' if vid=='geometry-translation' else 'Vector <9, −10>',43,v.TEAL)
    else:draw_card(spec,d,scene,p)


def lessons(doc):
    batch=make_lessons(SPECS,doc)
    for s in SPECS:v.DRAW[s['video_id']]=lambda d,scene,p,s=s:diagram(s,d,scene,p)
    return batch
