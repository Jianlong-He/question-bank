"""Cylinder, sphere, pyramid and prism volume/surface-area lessons."""
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons,draw_card,centered_math
import generate_sample_videos as v

SPECS=[
authored('geometry-volume-cylinder','Find the volume of a cylinder',
 'A cylinder has radius 4 cm and height 6 cm.\nFind its exact volume in terms of pi.','96π cubic centimetres',
 'A cylinder has radius four centimetres and height six centimetres. Find its exact volume in terms of pi.',[
 ('START WITH THE BASE','The base is a circle','B = πr² = π × 4²',
  'Start with the circular base. Its area is pi times the radius squared.'),
 ('SQUARE THE RADIUS','Four squared is sixteen','B = 16π cm²',
  'Four squared is sixteen, so the base area is sixteen pi square centimetres.'),
 ('MULTIPLY BY HEIGHT','Volume is base area times height','V = 16π × 6 = 96π cm³',
  'Multiply the base area by the height, six. Sixteen pi times six is ninety-six pi cubic centimetres.'),
 ('KEEP THE FORMULA','Use radius squared, then multiply by height','V = πr²h\nExact volume = 96π cm³',
  'The cylinder formula is pi r squared h. Leave pi in the answer when an exact volume is requested.')],
 g(10,10,2,3),expression='4**2*6',value='96'),

authored('geometry-volume-compare-cylinders','Compare cylinder volumes',
 'Cylinder A: radius 2 cm, height 9 cm.\nCylinder B: radius 3 cm, height 5 cm.\nWhich has the larger volume?','Cylinder B; 45π cm³ is greater than 36π cm³',
 'Cylinder A has radius two centimetres and height nine. Cylinder B has radius three centimetres and height five. Which has the larger volume?',[
 ('SAME FORMULA','Use pi times radius squared times height','V = πr²h',
  'Both cylinders use the same formula: pi times radius squared times height.'),
 ('CYLINDER A','Square two and multiply by nine','A: π × 2² × 9 = 36π cm³',
  'For A, two squared is four, and four times nine is thirty-six. Its volume is thirty-six pi.'),
 ('CYLINDER B','Square three and multiply by five','B: π × 3² × 5 = 45π cm³',
  'For B, three squared is nine, and nine times five is forty-five. Its volume is forty-five pi.'),
 ('COMPARE','Pi is the same positive factor in both answers','45π > 36π\nCylinder B has the larger volume.',
  'Since pi is positive, compare forty-five with thirty-six. Cylinder B is larger, even though it is shorter. Radius is squared in the formula.')],
 g(8,5,8,10),expression='3**2*5-2**2*9',value='9',equalities=[('2**2*9','36'),('3**2*5','45')]),

authored('geometry-volume-sphere','Find the volume of a sphere',
 'A sphere has radius 4 cm.\nFind its exact volume in terms of pi.','256π/3 cubic centimetres',
 'A sphere has radius four centimetres. Find its exact volume in terms of pi.',[
 ('CHOOSE THE FORMULA','Sphere volume uses the radius cubed','V = (4/3)πr³',
  'Use four thirds times pi times the radius cubed.'),
 ('CUBE THE RADIUS','Multiply four by itself three times','r³ = 4³ = 4 × 4 × 4 = 64',
  'The radius is four, so cube four. Four times four times four equals sixty-four.'),
 ('MULTIPLY THE COEFFICIENT','Multiply sixty-four by four thirds','V = (4/3) × 64 × π = 256π/3',
  'Multiply sixty-four by four thirds. The exact volume is two hundred fifty-six pi over three.'),
 ('CHECK WHAT WAS GIVEN','The formula needs radius, not diameter','V = 256π/3 cm³\nIf given diameter, divide it by 2 first.',
  'Use cubic centimetres for volume. Make sure the formula receives the radius. If the question gives a diameter, halve it first.')],
 g(8,5,8,7),expression='(4/3)*4**3',value='256/3'),

authored('geometry-volume-pyramid','Find the volume of a pyramid',
 'A square pyramid has base side 7 cm\nand perpendicular height 6 cm. Find its volume.','98 cubic centimetres',
 'A square pyramid has base side seven centimetres and perpendicular height six centimetres. Find its volume.',[
 ('FIND THE BASE AREA','The base is a seven-by-seven square','B = 7 × 7 = 49 cm²',
  'Find the square base area first. Seven times seven is forty-nine square centimetres.'),
 ('USE THE PYRAMID FORMULA','Take one third of base area times height','V = Bh/3 = 49 × 6 ÷ 3',
  'A pyramid has one third of the volume of a prism with the same base area and perpendicular height.'),
 ('CALCULATE','Multiply, then divide by three','49 × 6 = 294\n294 ÷ 3 = 98 cm³',
  'Forty-nine times six is two hundred ninety-four. Divide by three to get ninety-eight cubic centimetres.'),
 ('CHECK THE HEIGHT','Use the height perpendicular to the base','V = 98 cm³\nIf B is already given, start with V = Bh/3.',
  'Use the perpendicular height, not a sloping edge. If the base area is already given, substitute it directly into base area times height divided by three.')],
 g(10,10,2,2),expression='7*7*6/3',value='98'),

authored('geometry-volume-triangle','Find the volume of a triangular prism',
 'A prism has a triangular end with base 9 cm\nand perpendicular triangle height 4 cm.\nThe prism is 5 cm long. Find its volume.','90 cubic centimetres',
 'A prism has a triangular end with base nine centimetres and perpendicular triangle height four centimetres. The prism is five centimetres long. Find its volume.',[
 ('AREA OF THE TRIANGLE','Use half of base times triangle height','B = (1/2) × 9 × 4 = 18 cm²',
  'First find the triangular end area. Half of nine times four is eighteen square centimetres.'),
 ('LENGTH OF THE PRISM','Use the distance between its triangular ends','Prism length = 5 cm',
  'The prism extends five centimetres between its triangular ends. This is different from the triangle’s own height.'),
 ('MULTIPLY AREA BY LENGTH','Volume is base area times prism length','V = 18 × 5 = 90 cm³',
  'Multiply the triangular area, eighteen, by the prism length, five. The volume is ninety cubic centimetres.'),
 ('TWO STEPS','Find the end area, then extend it through the prism','V = B × prism length\nIf B is given, no triangle calculation is needed.',
  'Find the end area first, then multiply by the prism’s length. When the triangle’s area is already given, use it directly.')],
 g(6,10,3,6),expression='(1/2)*9*4*5',value='90'),

authored('geometry-surface-area-cube','Find a cube’s surface area',
 'A cube has side length 6 cm.\nFind its total surface area.','216 square centimetres',
 'A cube has side length six centimetres. Find its total surface area.',[
 ('ONE FACE','Every face is a square','One face = 6 × 6 = 36 cm²',
  'Each face is a square with sides six centimetres. Its area is thirty-six square centimetres.'),
 ('COUNT THE FACES','A cube has six equal square faces','6 equal faces',
  'A cube has six faces. Remember the back and bottom faces, even when you cannot see them.'),
 ('ADD ALL SIX','Multiply one face’s area by six','Surface area = 6 × 36 = 216 cm²',
  'Multiply the area of one face by six. Six times thirty-six equals two hundred sixteen.'),
 ('KEEP SQUARE UNITS','Surface area covers the outside faces','Surface area = 6s²\nAnswer: 216 cm²',
  'Surface area uses square units because it measures the faces. The general formula is six times the side length squared.')],
 g(6,10,4,8),expression='6*6**2',value='216'),

authored('geometry-surface-area-rectangular-prism','Find a rectangular prism’s surface area',
 'A rectangular prism is 7 cm long, 4 cm wide\nand 2 cm high. Find its total surface area.','100 square centimetres',
 'A rectangular prism is seven centimetres long, four centimetres wide, and two centimetres high. Find its total surface area.',[
 ('TOP AND BOTTOM','These two faces are seven by four','2 × (7 × 4) = 56 cm²',
  'The top and bottom are each seven by four. Together their area is fifty-six square centimetres.'),
 ('FRONT AND BACK','These two faces are seven by two','2 × (7 × 2) = 28 cm²',
  'The front and back are each seven by two. Their combined area is twenty-eight square centimetres.'),
 ('BOTH ENDS','These two faces are four by two','2 × (4 × 2) = 16 cm²',
  'Each end is four by two. Both ends together cover sixteen square centimetres.'),
 ('ADD THE THREE PAIRS','Count all six faces exactly once','56 + 28 + 16 = 100 cm²\nSurface area = 2(lw + lh + wh)',
  'Add the three pairs to get one hundred square centimetres. The formula is twice the sum of length times width, length times height, and width times height.')],
 g(6,10,5,4),expression='2*(7*4+7*2+4*2)',value='100'),

authored('geometry-surface-area-pyramid','Find a square pyramid’s surface area',
 'A square pyramid has base side 10 cm.\nEach triangular face has base 10 cm\nand perpendicular face height 12 cm.\nFind the total surface area.','340 square centimetres',
 'A square pyramid has base side ten centimetres. Each triangular face has base ten and perpendicular face height twelve. Find the total surface area.',[
 ('SQUARE BASE','Multiply the base side by itself','Base area = 10 × 10 = 100 cm²',
  'The square base has area ten times ten, or one hundred square centimetres.'),
 ('ONE TRIANGULAR FACE','Use the height measured within the face','Triangle area = (1/2) × 10 × 12 = 60 cm²',
  'For one triangular face, multiply half of ten by twelve. Its area is sixty square centimetres.'),
 ('FOUR TRIANGLES','All four triangular faces have the same area','4 × 60 = 240 cm²',
  'There are four equal triangular faces. Their combined area is four times sixty, or two hundred forty.'),
 ('BASE PLUS ALL FACES','Include the square and all four triangles','100 + 240 = 340 cm²',
  'Add the square base to the four triangles. The surface area is three hundred forty square centimetres. Use the triangle’s face height for this calculation.')],
 g(6,10,5,7),expression='10**2+4*(1/2)*10*12',value='340'),

authored('geometry-surface-area-scale-factor','Scale surface area when dimensions change',
 'A box has surface area 240 cm².\nEvery length is multiplied by 3.\nWhat is the new surface area?','2160 square centimetres',
 'A box has surface area two hundred forty square centimetres. Every length is multiplied by three. What is the new surface area?',[
 ('LOOK AT ONE FACE','Both side lengths grow by three','New face area = (3l)(3w)',
  'Look at one rectangular face. Both its length and width are multiplied by three.'),
 ('MULTIPLY THE SCALE FACTORS','Three times three gives an area factor of nine','(3l)(3w) = 9lw',
  'The new area is three times three times the original area. Each face becomes nine times as large.'),
 ('SCALE THE WHOLE SURFACE','Every face has the same area multiplier','240 × 9 = 2160 cm²',
  'Every face has that same factor, so multiply the total surface area by nine. The result is two thousand one hundred sixty.'),
 ('GENERAL RULE','Square the length scale factor','Lengths × k → surface area × k²',
  'When all lengths are multiplied by k, surface area is multiplied by k squared. Apply that factor to the original total area.')],
 g(6,10,5,9),expression='240*3**2',value='2160',identities=[('(3*l)*(3*w)','9*l*w')]),
]


def diagram(spec,d,scene,p):
    vid=spec['video_id']
    if vid=='geometry-surface-area-cube' and scene in (1,2,3):
        for i,(c,r) in enumerate([(1,0),(0,1),(1,1),(2,1),(1,2),(1,3)]):
            x,y=825+c*90,370+r*90
            d.rectangle((x,y,x+90,y+90),fill='#F1DBB9' if i==2 else '#D0E8E2',outline=v.TEAL,width=3)
            v.text(d,(x+45,y+45),'36',28,v.INK,True,anchor='mm')
        v.centered(d,752,'Unfolded cube: each face covers 36 cm²',32,v.INK)
        centered_math(d,825,spec['displays'][scene],44,v.TEAL)
        return
    if vid=='geometry-surface-area-pyramid' and scene in (1,2,3):
        x,y,size,reach=905,475,110,132
        shapes=[[(x,y),(x+size,y),(x+size/2,y-reach)],
                [(x+size,y),(x+size,y+size),(x+size+reach,y+size/2)],
                [(x,y+size),(x+size,y+size),(x+size/2,y+size+reach)],
                [(x,y),(x,y+size),(x-reach,y+size/2)]]
        for points in shapes:d.polygon(points,fill='#D0E8E2',outline=v.TEAL,width=3)
        d.rectangle((x,y,x+size,y+size),fill='#F1DBB9',outline=v.TEAL,width=3)
        v.centered(d,752,'Unfolded pyramid: 1 square + 4 equal triangles',32,v.INK)
        centered_math(d,825,spec['displays'][scene],44,v.TEAL)
        return
    draw_card(spec,d,scene,p)


def lessons(doc):
    batch=make_lessons(SPECS,doc)
    for spec in SPECS:v.DRAW[spec['video_id']]=lambda d,scene,p,s=spec:diagram(s,d,scene,p)
    return batch
