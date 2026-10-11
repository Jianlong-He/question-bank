"""Original arithmetic-property and measurement lessons with mathematical diagrams."""
from itertools import permutations
from algebra_lessons import authored
from probability_lessons import enrichment as e
from number_sense_lessons import source as g
from card_lessons import make_lessons,draw_card
import generate_sample_videos as v

SPECS=[
authored('arithmetic-commutative-property','Changing the order of multiplication',
 'Compare 2 × 7 and 7 × 2.\nDoes changing the factor order change the product?','No; both are 14',
 'Compare two times seven and seven times two. Does changing the factor order change the product?',[
 ('FIRST ARRAY','Two rows, seven in each row','2 × 7 = 14',
  'Two rows with seven dots in each row contain fourteen dots.'),
 ('TURN THE ARRAY','Seven rows, two in each row','7 × 2 = 14',
  'Turn the array. Now there are seven rows with two dots each. No dots were added or removed.'),
 ('COMPARE','The same objects give the same total','2 × 7 = 7 × 2 = 14',
  'Both arrangements contain fourteen dots. The products are equal.'),
 ('THE PROPERTY','Factor order does not change a product','a × b = b × a',
  'This is the commutative property of multiplication. Changing factor order leaves the product unchanged.')],
 g(3,2,3,5),expression='2*7',value='14',identities=[('a*b','b*a')]),

authored('arithmetic-regroup-products','Choosing a convenient multiplication order',
 'Calculate 25 × 13 × 8 using a convenient order.','2600',
 'Calculate twenty-five times thirteen times eight using a convenient order.',[
 ('REORDER','Bring useful factors together','25 × 13 × 8 = 25 × 8 × 13',
  'Use the commutative property to bring twenty-five and eight together.'),
 ('REGROUP','Choose which multiplication to do first','(25 × 8) × 13',
  'The associative property lets us group twenty-five times eight first.'),
 ('EASY PRODUCT','Twenty-five times eight makes two hundred','200 × 13 = 2,600',
  'Twenty-five times eight is two hundred. Two hundred times thirteen is two thousand six hundred.'),
 ('WHY IT WORKS','Order and grouping preserve the product','Reorder: a × b = b × a\nRegroup: (a × b) × c = a × (b × c)',
  'Reordering factors and changing their grouping preserve the product. Look for a pair that makes ten, one hundred, or another easy number.')],
 e('PCF',2,1),expression='25*13*8',value='2600',identities=[('(a*b)*c','a*(b*c)')]),

authored('pattern-pcf-370425ce3b84','Multiplication by splitting one factor',
 'Use distribution to calculate 43 × 16.','688',
 'Use the distributive property to calculate forty-three times sixteen.',[
 ('SPLIT','Break sixteen into tens and ones','43 × 16 = 43 × (10 + 6)',
  'Split sixteen into ten plus six.'),
 ('DISTRIBUTE','Multiply forty-three by both parts','43 × 10 + 43 × 6',
  'Multiply forty-three by ten and by six. Both parts must be included.'),
 ('PARTIAL PRODUCTS','Calculate each multiplication','430 + 258',
  'The partial products are four hundred thirty and two hundred fifty-eight.'),
 ('ADD','Combine the partial products','430 + 258 = 688\na(b + c) = ab + ac',
  'Add them to get six hundred eighty-eight. The same rule works with larger numbers: split a factor, multiply each part, then add.')],
 e('PCF',2,5),expression='43*16',value='688',equalities=[('43*6','258'),('430+258','688')]),

authored('arithmetic-distribute-two-sums','Multiplying two expanded numbers',
 'Expand and calculate (400 + 20 + 7)(30 + 2).','13664',
 'Expand and calculate four hundred plus twenty plus seven, times thirty plus two.',[
 ('PAIR EVERY TERM','Each first-factor part multiplies each second-factor part','400×30 + 400×2\n+ 20×30 + 20×2\n+ 7×30 + 7×2',
  'Multiply each of the three parts in the first factor by both parts in the second. That gives six products.'),
 ('CALCULATE','Keep the place values','12,000 + 800\n+ 600 + 40\n+ 210 + 14',
  'The products are twelve thousand, eight hundred, six hundred, forty, two hundred ten, and fourteen.'),
 ('ADD','Include all six products','12,000 + 800 + 600 + 40 + 210 + 14 = 13,664',
  'Adding all six products gives thirteen thousand six hundred sixty-four.'),
 ('CHECK THE STRUCTURE','Three parts times two parts gives six products','(400 + 20 + 7)(30 + 2) = 427 × 32\nEvery part is multiplied exactly once by each other part.',
  'This is four hundred twenty-seven times thirty-two. With two parts in each factor, there would be four products instead of six.')],
 e('PCF',2,10),expression='427*32',value='13664',equalities=[('12000+800+600+40+210+14','13664')]),

authored('pattern-pcf-276f557682ac','Finding a missing multiplication factor',
 'Find the missing factor: 6 × ? × 7 = 210.','5',
 'Find the missing factor in six times a missing number times seven equals two hundred ten.',[
 ('KNOWN FACTORS','Multiply the known numbers first','6 × 7 = 42',
  'Multiply the known factors, six and seven, to get forty-two.'),
 ('SIMPLIFY THE QUESTION','What times forty-two makes two hundred ten?','42 × ? = 210',
  'Now the missing factor multiplied by forty-two must equal two hundred ten.'),
 ('DIVIDE','Undo multiplication by forty-two','? = 210 ÷ 42 = 5',
  'Divide two hundred ten by forty-two. The missing factor is five.'),
 ('CHECK','Put the answer into the original product','6 × 5 × 7 = 210',
  'Check in the original expression. Six times five times seven equals two hundred ten.')],
 e('PCF',1,8),expression='210/(6*7)',value='5',equalities=[('6*5*7','210')]),

authored('geometry-area-rectangle','Rectangle area from rows of squares',
 'A rectangle is 8 cm long and 7 cm wide.\nFind its area.','56 square centimetres',
 'A rectangle is eight centimetres long and seven centimetres wide. Find its area.',[
 ('UNIT SQUARES','Each small square is one square centimetre','8 squares in each row; 7 rows',
  'Imagine covering the rectangle with one-centimetre squares. There are eight squares in each row and seven rows.'),
 ('MULTIPLY','Count all the squares','8 × 7 = 56',
  'Multiply eight by seven to count all fifty-six squares.'),
 ('AREA UNITS','Area measures a surface','Area = 56 cm²',
  'The area is fifty-six square centimetres. The square unit describes a surface, not just a length.'),
 ('GENERAL RULE','Use matching length units','Area of a rectangle = length × width',
  'For a rectangle, multiply length by width. First express both lengths in the same unit, then write the result in square units.')],
 g(3,10,3,1),expression='8*7',value='56'),

authored('geometry-volume-rectangular-prism','Rectangular prism volume in layers',
 'A rectangular box is 7 cm long, 5 cm wide, and 4 cm high.\nFind its volume.','140 cubic centimetres',
 'A rectangular box is seven centimetres long, five centimetres wide, and four centimetres high. Find its volume.',[
 ('ONE LAYER','Cover the base with one-centimetre cubes','7 × 5 = 35 cubes in one layer',
  'The base holds seven times five unit cubes, or thirty-five cubes in one layer.'),
 ('STACK THE LAYERS','The height gives four layers','35 × 4 = 140 cubes',
  'The height gives four layers. Multiply thirty-five by four to get one hundred forty cubes.'),
 ('VOLUME UNITS','A unit cube occupies one cubic centimetre','Volume = 140 cm³',
  'Each unit cube occupies one cubic centimetre, so the volume is one hundred forty cubic centimetres.'),
 ('GENERAL RULE','Three dimensions describe a rectangular box','V = length × width × height\nEquivalently: V = base area × height',
  'Multiply length, width, and height, using matching length units. Equivalently, multiply the base area by the perpendicular height.')],
 g(5,11,2,4),expression='7*5*4',value='140'),

authored('geometry-volume-cube','The volume of a cube',
 'A cube has side length 3 cm. Find its volume.','27 cubic centimetres',
 'A cube has side length three centimetres. Find its volume.',[
 ('EQUAL DIMENSIONS','Length, width and height are all three centimetres','3 cm × 3 cm × 3 cm',
  'All three dimensions of a cube are equal, so each dimension is three centimetres.'),
 ('ONE LAYER','Three rows of three unit cubes','3 × 3 = 9 cubes',
  'One layer contains three rows of three unit cubes, giving nine cubes.'),
 ('THREE LAYERS','Multiply by the height','9 × 3 = 27 cm³',
  'There are three layers. Nine times three gives twenty-seven cubic centimetres.'),
 ('GENERAL RULE','Multiply the side length three times','V = s × s × s = s³',
  'For a cube, multiply the side length by itself three times. We write this as s cubed.')],
 g(5,11,2,2),expression='3**3',value='27'),

authored('geometry-volume-rectangular-prism-missing-dimension','Finding a prism height from volume',
 'A rectangular prism has volume 330 cm³.\nIts base is 11 cm by 5 cm. Find its height.','6 centimetres',
 'A rectangular prism has volume three hundred thirty cubic centimetres. Its base is eleven by five centimetres. Find its height.',[
 ('BASE AREA','Multiply the two known lengths','11 × 5 = 55 cm²',
  'Multiply eleven by five. The base area is fifty-five square centimetres.'),
 ('VOLUME EQUATION','Base area times height gives volume','55 × h = 330',
  'The volume is base area times height, so fifty-five times h equals three hundred thirty.'),
 ('DIVIDE','Undo multiplication by the base area','h = 330 ÷ 55 = 6 cm',
  'Divide three hundred thirty by fifty-five to get a height of six centimetres.'),
 ('CHECK','Multiply all three dimensions','11 × 5 × 6 = 330 cm³',
  'Check by multiplying eleven, five, and six. The result matches the given volume.')],
 g(5,11,3,7),expression='330/(11*5)',value='6'),

authored('geometry-area-conservation','Area stays the same when pieces move',
 'An L-shape is cut and rearranged into a 9 by 5 rectangle.\nNo pieces are lost or overlap. Find the original area.','45 square units',
 'An L-shape is cut and rearranged into a nine by five rectangle. No pieces are lost or overlap. Find the original area.',[
 ('KEEP EVERY PIECE','Cutting and moving does not add or remove material','The same two pieces are used.',
  'Cut the shape into two rectangles. Moving a piece does not change how much surface it covers.'),
 ('REARRANGE','Join the pieces without gaps or overlaps','Rectangle: 9 units by 5 units',
  'Join the two pieces into a rectangle nine units by five units, without gaps or overlaps.'),
 ('CALCULATE','Use the rectangle area formula','9 × 5 = 45 square units',
  'The rectangle has area nine times five, or forty-five square units.'),
 ('TRANSFER THE AREA','The original shape has the same area','Original area = rearranged area = 45 square units',
  'The original shape has the same forty-five square units of area. Rearranging all the pieces preserves area when nothing is lost or overlapped.')],
 g(6,8,3,5),expression='9*5',value='45'),

authored('number-place-value-maximize-difference','Arrange digits to make the greatest difference',
 'Use digits 1, 4, 6, 8 once in EACH four-digit number.\nMake one number minus the other as large as possible.','7173',
 'Use the digits one, four, six, and eight once in each of two four-digit numbers. Make the first number minus the second as large as possible.',[
 ('MAXIMIZE THE FIRST NUMBER','Put larger digits in larger place values','Largest: 8,641',
  'Make the first number as large as possible. Put the digits in descending order to get eight thousand six hundred forty-one.'),
 ('MINIMIZE THE SECOND NUMBER','Put smaller digits in larger place values','Smallest: 1,468',
  'Make the number being subtracted as small as possible. Ascending order gives one thousand four hundred sixty-eight.'),
 ('SUBTRACT','Largest minus smallest','8,641 − 1,468 = 7,173',
  'Subtract one thousand four hundred sixty-eight from eight thousand six hundred forty-one. The difference is seven thousand one hundred seventy-three.'),
 ('WHY THIS IS MAXIMUM','Each number uses its own copy of every digit','Increase the first number; decrease the second.\nIf zero is available, a multi-digit number cannot start with zero.',
  'Increasing the first number or decreasing the second increases their difference. If zero is available, the smaller number must still start with a nonzero digit.')],
 g(4,2,3,10),expression='8641-1468',value='7173'),
]


def grid(d,x,y,cols,rows,size=40,color=None):
    for row in range(rows):
        for col in range(cols):
            d.rectangle((x+col*size,y+row*size,x+(col+1)*size,y+(row+1)*size),fill=color or '#D9EEEA',outline=v.TEAL,width=2)


def diagram(spec,d,scene,p):
    vid=spec['video_id']
    if vid=='arithmetic-commutative-property' and scene in [1,2]:
        rows,cols=(2,7) if scene==1 else (7,2)
        step=45;x=(v.W-cols*step)/2;y=410
        for r in range(rows):
            for c in range(cols):d.ellipse((x+c*step,y+r*step,x+c*step+26,y+r*step+26),fill=v.TEAL)
        v.centered(d,800,spec['displays'][scene],70,v.INK,True);return
    if vid=='geometry-area-rectangle' and scene in [1,2]:
        grid(d,680,390,8,7,55)
        v.centered(d,795,spec['displays'][scene],60,v.TEAL,True);return
    if vid in {'geometry-volume-rectangular-prism','geometry-volume-cube'} and scene in [1,2,3]:
        cube=vid=='geometry-volume-cube';a,b,h=(3,3,3) if cube else (7,5,4)
        x,y=620,720;w=a*70;ht=h*65;dx=b*26;dy=-b*17
        d.polygon([(x,y-ht),(x+dx,y-ht+dy),(x+w+dx,y-ht+dy),(x+w,y-ht)],fill='#E0EFE9',outline=v.TEAL,width=4)
        d.polygon([(x+w,y-ht),(x+w+dx,y-ht+dy),(x+w+dx,y+dy),(x+w,y)],fill='#B2D9D2',outline=v.TEAL,width=4)
        d.rectangle((x,y-ht,x+w,y),fill='#D0E8E2',outline=v.TEAL,width=4)
        for i in range(1,h):
            d.line((x,y-i*65,x+w,y-i*65),fill=v.TEAL,width=2)
            d.line((x+w,y-i*65,x+w+dx,y-i*65+dy),fill=v.TEAL,width=2)
        for i in range(1,a):
            d.line((x+i*70,y-ht,x+i*70,y),fill=v.TEAL,width=2)
            d.line((x+i*70,y-ht,x+i*70+dx,y-ht+dy),fill=v.TEAL,width=2)
        for i in range(1,b):
            d.line((x+i*26,y-ht-i*17,x+w+i*26,y-ht-i*17),fill=v.TEAL,width=2)
            d.line((x+w+i*26,y-ht-i*17,x+w+i*26,y-i*17),fill=v.TEAL,width=2)
        v.text(d,(x+w/2-40,y+20),f'{a} cm',34,v.INK)
        v.text(d,(x+w+dx+20,y-ht/2),f'{h} cm',34,v.INK)
        v.text(d,(x+w+dx/2+25,y+dy/2+25),f'{b} cm',34,v.INK)
        v.centered(d,805,spec['displays'][scene],52,v.TEAL,True);return
    if vid=='geometry-area-conservation' and scene in [1,2]:
        scale=36
        if scene==1:
            grid(d,780,580,6,5,scale);grid(d,780,400,3,5,scale,'#F1DBB9')
        else:
            grid(d,650,500,6,5,scale);grid(d,866,500,3,5,scale,'#F1DBB9')
            v.centered(d,710,'9 units across; 5 units high',40,v.INK,True)
        v.centered(d,820,spec['displays'][scene],45,v.TEAL,True);return
    draw_card(spec,d,scene,p)


def lessons(doc):
    nums=[int(''.join(p)) for p in permutations('1468')]
    assert max(nums)-min(nums)==7173
    result=make_lessons(SPECS,doc)
    for spec in SPECS:v.DRAW[spec['video_id']]=lambda d,scene,p,s=spec:diagram(s,d,scene,p)
    return result
