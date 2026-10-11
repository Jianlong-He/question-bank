"""Distinct area reasoning and density examples, checked before local rendering."""
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons, draw_card
import generate_sample_videos as v

SPECS=[
authored('geometry-area-rectangle-missing-dimension','Find a rectangle side from its area',
 'A rectangle has area 63 cm² and length 9 cm.\nFind its width.','7 centimetres',
 'A rectangle has area sixty-three square centimetres and length nine centimetres. Find its width.',[
 ('USE THE AREA','Length times width gives area','9 × width = 63',
  'The area is length times width. Nine multiplied by the unknown width equals sixty-three.'),
 ('UNDO MULTIPLICATION','Divide by the known side','width = 63 ÷ 9 = 7',
  'Divide the area by the known length. Sixty-three divided by nine is seven.'),
 ('LENGTH UNITS','The answer is a length','Width = 7 cm',
  'The width is seven centimetres. A side uses length units, even though the given area uses square units.'),
 ('CHECK','Multiply the two side lengths','9 × 7 = 63 cm²',
  'Nine times seven gives the original area of sixty-three square centimetres, so the width checks.')],
 g(3,10,2,9),expression='63/9',value='7'),

authored('geometry-area-add-known-parts','Add the areas of separate pieces',
 'A shape is made of two pieces with no overlap.\nTheir areas are 38 cm² and 47 cm². Find the total area.','85 square centimetres',
 'A shape is made of two pieces with no overlap. Their areas are thirty-eight and forty-seven square centimetres. Find the total area.',[
 ('IDENTIFY THE PARTS','Both areas are already known','Piece A: 38 cm²     Piece B: 47 cm²',
  'We know the area of each piece. We do not need their side lengths.'),
 ('ADD','Count each piece once','Total area = 38 + 47',
  'The pieces do not overlap, so add their areas. Count each piece exactly once.'),
 ('CALCULATE','Combine the two areas','38 + 47 = 85 cm²',
  'Thirty-eight plus forty-seven is eighty-five square centimetres.'),
 ('GENERAL RULE','Use matching area units','Total area = sum of the non-overlapping parts',
  'This works for rectangles, triangles, or other pieces when their areas are known. Use matching area units before adding.')],
 g(3,10,4,7),expression='38+47',value='85'),

authored('geometry-area-two-rectangles','Find area by splitting into two rectangles',
 'An L-shape has two non-overlapping rectangles:\n7 m by 4 m, and 3 m by 6 m. Find its area.','46 square metres',
 'An L-shape has two non-overlapping rectangles, seven metres by four metres, and three metres by six metres. Find its area.',[
 ('FIRST RECTANGLE','Multiply its length and width','7 × 4 = 28 m²',
  'For the first rectangle, multiply seven by four. Its area is twenty-eight square metres.'),
 ('SECOND RECTANGLE','Find the other area separately','3 × 6 = 18 m²',
  'For the second rectangle, multiply three by six. Its area is eighteen square metres.'),
 ('ADD THE AREAS','The pieces cover the shape without overlap','28 + 18 = 46 m²',
  'Add twenty-eight and eighteen. The total area is forty-six square metres.'),
 ('CHECK THE PARTITION','Include every part exactly once','Find each rectangle area, then add.',
  'Check that your rectangles cover the whole shape without overlapping. Find each area, then add the results.')],
 g(3,10,5,6),expression='7*4+3*6',value='46'),

authored('geometry-area-subtract-known-cutout','Subtract a cut-out from an area',
 'A sheet has area 96 cm². A 27 cm² piece is removed.\nWhat area remains?','69 square centimetres',
 'A sheet has area ninety-six square centimetres. A piece with area twenty-seven square centimetres is removed. What area remains?',[
 ('START WITH THE WHOLE','The whole includes the piece being removed','Whole: 96 cm²     Removed: 27 cm²',
  'Start with the area of the whole sheet, which includes the piece we are removing.'),
 ('SUBTRACT','Remove the cut-out area once','Remaining area = 96 − 27',
  'Subtract the cut-out area from the whole area.'),
 ('CALCULATE','The remaining surface is smaller','96 − 27 = 69 cm²',
  'Ninety-six minus twenty-seven is sixty-nine square centimetres.'),
 ('CHECK','Add the removed piece back','69 + 27 = 96 cm²',
  'Check by adding the removed area back. Sixty-nine plus twenty-seven recovers the whole area of ninety-six.')],
 g(3,10,'5HW',3),expression='96-27',value='69',equalities=[('69+27','96')]),

authored('geometry-equal-area-different-sides','Equal area can have different side lengths',
 'Rectangle A is 2 by 12 units. Rectangle B is 4 by 6 units.\nDo equal areas force equal side lengths?','No; both areas are 24 square units',
 'Rectangle A is two by twelve units. Rectangle B is four by six units. Do equal areas force equal side lengths?',[
 ('FIRST AREA','Multiply the sides of A','2 × 12 = 24 square units',
  'Rectangle A has area two times twelve, or twenty-four square units.'),
 ('SECOND AREA','Multiply the sides of B','4 × 6 = 24 square units',
  'Rectangle B also has area twenty-four square units.'),
 ('COMPARE','The products match, but the factors differ','Same area: 24\nDifferent sides: 2 and 12; 4 and 6',
  'The areas match, but the side lengths are different. Two and twelve are not the same pair as four and six.'),
 ('CONCLUDE','One counterexample is enough','Equal area does not force equal side lengths.',
  'So equal areas do not force equal side lengths. Different factor pairs can give the same product.')],
 g(3,10,2,8),expression='2*12',value='24',equalities=[('2*12','4*6')]),

authored('geometry-equal-perimeter-different-area','Equal perimeter can have different areas',
 'Rectangle A is 4 m by 8 m. Rectangle B is 5 m by 7 m.\nBoth use 24 m of fencing. Must their areas match?','No; the areas are 32 and 35 square metres',
 'Rectangle A is four metres by eight metres. Rectangle B is five metres by seven metres. Both use twenty-four metres of fencing. Must their areas match?',[
 ('COMPARE PERIMETERS','Perimeter measures the boundary','A: 2 × (4 + 8) = 24 m\nB: 2 × (5 + 7) = 24 m',
  'Twice length plus width gives twenty-four metres for each boundary.'),
 ('COMPARE AREAS','Area measures the surface inside','A: 4 × 8 = 32 m²\nB: 5 × 7 = 35 m²',
  'Now multiply the sides. The areas are thirty-two and thirty-five square metres.'),
 ('COMPARE RESULTS','The boundaries match; the surfaces do not','32 m² ≠ 35 m²',
  'The areas are different, even though the perimeters are equal.'),
 ('CONCLUDE','Check area separately from perimeter','Equal perimeter does not force equal area.',
  'Equal perimeter does not force equal area. Use addition for the boundary and multiplication for the rectangular surface.')],
 g(4,13,1,10),expression='4*8',value='32',equalities=[('2*(4+8)','2*(5+7)'),('5*7','35')]),

authored('geometry-area-from-perimeter-and-side','Find area from perimeter and one side',
 'A rectangle has perimeter 38 m and width 7 m.\nFind its area.','84 square metres',
 'A rectangle has perimeter thirty-eight metres and width seven metres. Find its area.',[
 ('HALVE THE PERIMETER','One length plus one width is half the boundary','length + width = 38 ÷ 2 = 19 m',
  'The perimeter counts two lengths and two widths. Divide by two to get one length plus one width: nineteen metres.'),
 ('FIND THE LENGTH','Subtract the known width','length = 19 − 7 = 12 m',
  'Subtract the seven-metre width. The length is twelve metres.'),
 ('FIND THE AREA','Multiply the two side lengths','Area = 12 × 7 = 84 m²',
  'Multiply twelve by seven. The area is eighty-four square metres.'),
 ('CHECK','The side lengths must recover the perimeter','2 × (12 + 7) = 38 m',
  'Check the boundary: twice twelve plus seven is thirty-eight metres, matching the given perimeter.')],
 g(3,11,3,9),expression='(38/2-7)*7',value='84',equalities=[('2*(12+7)','38')]),

authored('geometry-rectangle-from-area-and-perimeter','Find rectangle sides from area and perimeter',
 'A rectangle has area 30 cm² and perimeter 26 cm.\nIts length is greater than its width. Find both sides.','Length 10 cm; width 3 cm',
 'A rectangle has area thirty square centimetres and perimeter twenty-six centimetres. Its length is greater than its width. Find both sides.',[
 ('PRODUCT AND SUM','Area gives a product; half-perimeter gives a sum','length × width = 30\nlength + width = 26 ÷ 2 = 13',
  'The side lengths multiply to thirty. They must also add to thirteen, half the perimeter.'),
 ('TRY FACTOR PAIRS','List positive whole-number factors of thirty','1 and 30: sum 31\n2 and 15: sum 17\n3 and 10: sum 13\n5 and 6: sum 11',
  'Try factor pairs of thirty. Only three and ten add to thirteen.'),
 ('LABEL THE SIDES','The longer side is the length','Length = 10 cm\nWidth = 3 cm',
  'The length is ten centimetres, and the width is three centimetres.'),
 ('CHECK BOTH CONDITIONS','Verify both the product and the boundary','10 × 3 = 30 cm²\n2 × (10 + 3) = 26 cm',
  'Ten times three gives thirty square centimetres, and twice their sum gives twenty-six centimetres. Both conditions hold.')],
 g(4,13,1,7),expression='10*3',value='30',equalities=[('2*(10+3)','26')]),

authored('measurement-density-from-mass-volume','Find density from mass and volume',
 'An object has mass 216 g and volume 48 cm³.\nFind its density.','4.5 grams per cubic centimetre',
 'An object has mass two hundred sixteen grams and volume forty-eight cubic centimetres. Find its density.',[
 ('MEANING','Density is mass per unit of volume','Density = mass ÷ volume',
  'Density tells us the mass for each unit of volume. Divide mass by volume.'),
 ('SUBSTITUTE','Keep the quantities in the correct order','Density = 216 ÷ 48',
  'Put two hundred sixteen grams over forty-eight cubic centimetres.'),
 ('DIVIDE','State mass per cubic centimetre','216 ÷ 48 = 4.5 g/cm³',
  'The density is four point five grams per cubic centimetre.'),
 ('CHECK','Density times volume recovers mass','4.5 × 48 = 216 g',
  'Multiply the density by the volume. Four point five times forty-eight gives the original mass of two hundred sixteen grams.')],
 g(10,10,3,2),expression='216/48',value='4.5',equalities=[('4.5*48','216')]),

authored('measurement-mass-from-density-volume','Find mass from density and volume',
 'A material has density 3.5 g/cm³ and volume 18 cm³.\nFind its mass.','63 grams',
 'A material has density three point five grams per cubic centimetre and volume eighteen cubic centimetres. Find its mass.',[
 ('MEANING','Each cubic centimetre has mass 3.5 grams','Mass = density × volume',
  'Density gives mass per cubic centimetre. Multiply it by the number of cubic centimetres.'),
 ('SUBSTITUTE','Use compatible units','Mass = 3.5 × 18',
  'The volume is already in cubic centimetres, so multiply three point five by eighteen.'),
 ('CALCULATE','The result is a mass','3.5 × 18 = 63 g',
  'Three point five times eighteen is sixty-three grams.'),
 ('CHECK','Mass divided by volume gives density','63 ÷ 18 = 3.5 g/cm³',
  'Divide sixty-three grams by eighteen cubic centimetres. We recover the given density of three point five grams per cubic centimetre.')],
 g(10,10,3,3),expression='3.5*18',value='63'),

authored('measurement-volume-from-mass-density','Find volume from mass and density',
 'An object has mass 126 g and density 4.5 g/cm³.\nFind its volume.','28 cubic centimetres',
 'An object has mass one hundred twenty-six grams and density four point five grams per cubic centimetre. Find its volume.',[
 ('REARRANGE','Mass equals density times volume','Volume = mass ÷ density',
  'Mass equals density times volume. Divide mass by density to find the volume.'),
 ('SUBSTITUTE','Use grams in both quantities','Volume = 126 ÷ 4.5',
  'The mass and density both use grams. Divide one hundred twenty-six by four point five.'),
 ('DIVIDE','The result is a volume','126 ÷ 4.5 = 28 cm³',
  'The volume is twenty-eight cubic centimetres.'),
 ('CHECK','Density times volume gives mass','4.5 × 28 = 126 g',
  'Check by multiplying the density by the volume. Four point five times twenty-eight gives the original mass.')],
 g(10,10,3,4),expression='126/4.5',value='28'),

authored('geometry-area-rectangle-plus-triangle','Add a rectangle and triangle area',
 'A shape joins a 7 cm by 5 cm rectangle to a triangle\nwith base 7 cm and perpendicular height 4 cm.\nThe pieces do not overlap. Find the total area.','49 square centimetres',
 'A shape joins a seven by five centimetre rectangle to a triangle with base seven and perpendicular height four centimetres. The pieces do not overlap. Find the total area.',[
 ('RECTANGLE','Multiply length and width','7 × 5 = 35 cm²',
  'The rectangle area is seven times five, or thirty-five square centimetres.'),
 ('TRIANGLE','Use half of base times perpendicular height','½ × 7 × 4 = 14 cm²',
  'The triangle area is one half times seven times four, or fourteen square centimetres.'),
 ('ADD','Combine the non-overlapping parts','35 + 14 = 49 cm²',
  'Add the two areas. Thirty-five plus fourteen gives forty-nine square centimetres.'),
 ('CHECK THE FORMULAS','Each piece needs its own area rule','Rectangle: length × width\nTriangle: ½ × base × perpendicular height',
  'Use the correct rule for each piece. In particular, remember the one-half factor for the triangle.')],
 g(6,8,3,7),expression='7*5+7*4/2',value='49'),
]


def rect(d,box,fill='#D0E8E2'):
    d.rectangle(box,fill=fill,outline=v.TEAL,width=4)


def diagram(spec,d,scene,p):
    vid=spec['video_id']
    if vid=='geometry-area-two-rectangles' and scene in (1,2):
        # Scale: 38 pixels per metre, both pieces share a three-metre edge.
        x,y,s=825,415,38
        rect(d,(x,y+6*s,x+7*s,y+10*s))
        rect(d,(x,y,x+3*s,y+6*s),'#F1DBB9')
        v.text(d,(x+130,y+2*s),'3 m × 6 m',37,v.INK,True)
        v.text(d,(x+30,y+7*s),'7 m × 4 m',37,v.INK,True)
        v.centered(d,850,spec['displays'][scene],48,v.TEAL,True);return
    if vid=='geometry-equal-area-different-sides' and scene in (1,2):
        rect(d,(410,525,410+12*38,525+2*38))
        rect(d,(1120,450,1120+6*38,450+4*38),'#F1DBB9')
        v.text(d,(430,650),'A: 2 × 12',45,v.INK,True)
        v.text(d,(1120,650),'B: 4 × 6',45,v.INK,True)
        v.centered(d,790,spec['displays'][scene],52,v.TEAL,True);return
    if vid=='geometry-equal-perimeter-different-area' and scene in (1,2):
        rect(d,(480,420,480+8*43,420+4*43))
        rect(d,(1110,420,1110+7*43,420+5*43),'#F1DBB9')
        v.text(d,(485,660),'A: 4 m × 8 m',42,v.INK,True)
        v.text(d,(1100,660),'B: 5 m × 7 m',42,v.INK,True)
        for i,line in enumerate(spec['displays'][scene].split('\n')):v.centered(d,755+i*65,line,44,v.TEAL,True)
        return
    if vid=='geometry-area-rectangle-plus-triangle' and scene in (1,2):
        x,y,s=750,550,44
        rect(d,(x,y,x+7*s,y+5*s))
        d.polygon([(x,y),(x+7*s,y),(x+3.5*s,y-4*s)],fill='#F1DBB9',outline=v.TEAL,width=4)
        d.line((x+3.5*s,y,x+3.5*s,y-4*s),fill=v.INK,width=3)
        d.line((x+3.5*s,y-17,x+3.5*s+17,y-17,x+3.5*s+17,y),fill=v.INK,width=3)
        v.text(d,(x+3.5*s+25,y-2.4*s),'4 cm',35,v.INK,True)
        v.text(d,(x+7*s+25,y+2*s),'5 cm',35,v.INK,True)
        v.text(d,(x+2.7*s,y+5*s+15),'7 cm',35,v.INK,True)
        v.centered(d,850,spec['displays'][scene],47,v.TEAL,True);return
    draw_card(spec,d,scene,p)


def lessons(doc):
    # Independently check all positive integer side pairs used by the search lesson.
    assert [(w,30//w) for w in range(1,6) if 30%w==0 and w+30//w==13]==[(3,10)]
    result=make_lessons(SPECS,doc)
    for spec in SPECS:v.DRAW[spec['video_id']]=lambda d,scene,p,s=spec:diagram(s,d,scene,p)
    return result
