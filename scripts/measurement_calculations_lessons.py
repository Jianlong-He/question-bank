"""Reviewed fractional, decimal and algebraic measurement examples."""
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons,draw_card,centered_math
import generate_sample_videos as v

SPECS=[
authored('geometry-area-fractional-sides','Rectangle area with fractional sides',
 'A rectangle is 3/8 m long and 4/9 m wide.\nFind its area.','1/6 square metre',
 'A rectangle is three eighths of a metre long and four ninths of a metre wide. Find its area.',[
 ('CHOOSE THE FORMULA','Area is length times width','A = (3/8) × (4/9)',
  'Use length times width. Multiply three eighths by four ninths.'),
 ('MULTIPLY FRACTIONS','Multiply the numerators and denominators','A = (3 × 4)/(8 × 9) = 12/72',
  'Multiply the numerators to get twelve, and the denominators to get seventy-two.'),
 ('SIMPLIFY','Divide both parts by twelve','12/72 = 1/6',
  'Twelve and seventy-two are both divisible by twelve, giving one sixth.'),
 ('USE AREA UNITS','Metres times metres gives square metres','A = 1/6 m²',
  'The area is one sixth of a square metre. Multiplying two lengths gives square units.')],
 g(5,6,5,1),expression='(3/8)*(4/9)',value='1/6'),

authored('geometry-area-fraction-of-unit-square','Area of one part of a unit square',
 'A 1 m by 1 m square is split into 15 equal rectangles.\nWhat is the area of one small rectangle?','1/15 square metre',
 'A one metre by one metre square is split into fifteen equal rectangles. What is the area of one small rectangle?',[
 ('FIND THE WHOLE','Multiply the two side lengths','Whole area = 1 × 1 = 1 m²',
  'First find the whole area. One metre times one metre gives one square metre.'),
 ('EQUAL PARTS','Share the whole area equally','15 equal parts share 1 m²',
  'The fifteen rectangles have equal areas, so each gets the same share of that square metre.'),
 ('DIVIDE','Divide the whole area by the number of parts','One part = 1 ÷ 15 = 1/15 m²',
  'Divide one by fifteen. Each rectangle has area one fifteenth of a square metre.'),
 ('CHECK THE WHOLE','All the parts must add to the original area','15 × (1/15) = 1 m²',
  'Check by multiplying one fifteenth by fifteen. The pieces add back to one square metre.')],
 g(5,6,5,5),expression='1/15',value='1/15',equalities=[('15*(1/15)','1')]),

authored('geometry-area-equal-fractional-tiles','Whole and shaded areas from equal tiles',
 'A rectangle contains 15 equal tiles; 4 are shaded.\nEach tile is 2/3 m by 3/10 m.\nFind the whole area and the shaded area.','Whole: 3 m²; shaded: 4/5 m²',
 'A rectangle contains fifteen equal tiles, with four shaded. Each tile is two thirds of a metre by three tenths of a metre. Find the whole area and the shaded area.',[
 ('ONE TILE','Multiply its two side lengths','Tile area = (2/3) × (3/10) = 1/5 m²',
  'Start with one tile. Two thirds times three tenths simplifies to one fifth of a square metre.'),
 ('THE WHOLE','Use all fifteen tiles','Whole area = 15 × (1/5) = 3 m²',
  'For the whole rectangle, multiply one fifth by all fifteen tiles. The area is three square metres.'),
 ('THE SHADED PART','Use only the four shaded tiles','Shaded area = 4 × (1/5) = 4/5 m²',
  'For the shaded part, multiply one fifth by four. The shaded area is four fifths of a square metre.'),
 ('MATCH THE COUNT','Same tile area, different numbers of tiles','Area = tile count × area of one tile',
  'Use the same tile area both times. Change the count depending on whether you need the whole rectangle or just its shaded part.')],
 g(5,6,'5Rev',5),expression='15*(2/3)*(3/10)',value='3',equalities=[('4*(2/3)*(3/10)','4/5')]),

authored('geometry-area-shaded-fraction','Shaded area from a fraction of the whole',
 'A 1 m by 6 m rectangle has 15 equal parts.\nFive parts are shaded. Find the shaded area.','2 square metres',
 'A one metre by six metre rectangle has fifteen equal parts. Five parts are shaded. Find the shaded area.',[
 ('WHOLE AREA','Find the area of the entire rectangle','Whole area = 1 × 6 = 6 m²',
  'The whole rectangle has area one times six, or six square metres.'),
 ('SHADED FRACTION','Compare shaded parts with all equal parts','Shaded fraction = 5/15 = 1/3',
  'Five out of fifteen equal parts are shaded. That fraction simplifies to one third.'),
 ('TAKE THAT SHARE','Multiply the whole area by the shaded fraction','Shaded area = 6 × (1/3) = 2 m²',
  'Take one third of the whole area. Six times one third is two square metres.'),
 ('A SECOND WAY','Each part has area six fifteenths','5 × (6/15) = 2 m²',
  'You can also find the area of one part, then multiply by the five shaded parts. Both methods give two square metres.')],
 g(5,6,'5Rev',2),expression='6*(5/15)',value='2',equalities=[('5*(6/15)','2')]),

authored('geometry-area-decimal-sides','Rectangle area with decimal sides',
 'A rectangle is 4.6 m long and 0.3 m wide.\nFind its area.','1.38 square metres',
 'A rectangle is four point six metres long and zero point three metres wide. Find its area.',[
 ('USE LENGTH TIMES WIDTH','Substitute both side lengths','A = 4.6 × 0.3',
  'Area is length times width, so multiply four point six by zero point three.'),
 ('MULTIPLY WHOLE NUMBERS','Temporarily leave out the decimal points','46 × 3 = 138',
  'First multiply forty-six by three to get one hundred thirty-eight.'),
 ('PUT THE DECIMAL BACK','There are two decimal places in total','4.6 × 0.3 = 1.38',
  'Each factor has one decimal place. Put two decimal places in the product to get one point three eight.'),
 ('CHECK SIZE AND UNITS','Three tenths of 4.6 is less than 4.6','A = 1.38 m²',
  'The area is one point three eight square metres. That makes sense: three tenths of four point six is smaller than four point six.')],
 g(5,8,3,10),expression='4.6*0.3',value='1.38'),

authored('geometry-volume-fractional-block-count','Total volume of blocks with fractional volume',
 'There are 18 identical blocks.\nEach block has volume 1/48 m³.\nFind their total volume.','3/8 cubic metre',
 'There are eighteen identical blocks. Each has volume one forty-eighth of a cubic metre. Find their total volume.',[
 ('COUNT EQUAL VOLUMES','Multiply the count by one block’s volume','Total = 18 × (1/48)',
  'The volume of one block is already given. Multiply it by eighteen, the number of blocks.'),
 ('WRITE THE PRODUCT','Multiply the numerator by eighteen','18 × (1/48) = 18/48',
  'Eighteen times one forty-eighth is eighteen forty-eighths.'),
 ('SIMPLIFY','Eighteen and forty-eight share a factor of six','18/48 = 3/8',
  'Divide both numerator and denominator by six. The fraction becomes three eighths.'),
 ('KEEP CUBIC UNITS','Volume describes three-dimensional space','Total volume = 3/8 m³',
  'The total volume is three eighths of a cubic metre. When the volume per block is given, multiply by the number of blocks.')],
 g(6,10,2,3),expression='18*(1/48)',value='3/8'),

authored('geometry-area-composite','Surface area from the areas of all faces',
 'A triangular prism has two triangular faces of 30 cm²,\ntwo rectangular faces of 65 cm², and one of 50 cm².\nFind its total surface area.','240 square centimetres',
 'A triangular prism has two triangular faces of thirty square centimetres, two rectangular faces of sixty-five, and one of fifty. Find its total surface area.',[
 ('THE TRIANGLES','Count both triangular faces','2 × 30 = 60 cm²',
  'There are two triangular faces, each with area thirty. Together they cover sixty square centimetres.'),
 ('THE RECTANGLES','Include each of the three rectangles','2 × 65 + 50 = 180 cm²',
  'Two rectangles have area sixty-five each, and the third has area fifty. Their total is one hundred eighty.'),
 ('ALL FACES','Add the triangle and rectangle totals','60 + 180 = 240 cm²',
  'Add the two totals. Sixty plus one hundred eighty equals two hundred forty square centimetres.'),
 ('COUNT EACH FACE ONCE','Surface area is the area of the outside faces','Surface area = 240 cm²\n2 triangles + 3 rectangles = 5 faces',
  'Check that all five outside faces were counted once. Surface area is the sum of their areas, in square units.')],
 g(6,10,4,6),expression='2*30+2*65+50',value='240'),

authored('geometry-area-write-quadratic-equation','Write an equation from a rectangle’s area',
 'A rectangle has width x cm and length (x + 4) cm.\nIts area is 77 cm². Write an equation for x.','x(x + 4) = 77',
 'A rectangle has width x centimetres and length x plus four centimetres. Its area is seventy-seven square centimetres. Write an equation for x.',[
 ('NAME THE SIDES','Keep the full expression for each side','Width = x\nLength = x + 4',
  'The width is x. The entire expression x plus four represents the length.'),
 ('USE THE AREA FORMULA','Multiply length by width','A = x(x + 4)',
  'Area is length times width, so multiply x by the quantity x plus four.'),
 ('USE THE GIVEN AREA','Set the product equal to seventy-seven','x(x + 4) = 77',
  'The given area is seventy-seven. Set the product equal to seventy-seven to form the equation.'),
 ('AN EQUIVALENT FORM','Expand and move everything to one side','x² + 4x − 77 = 0\nFor a real rectangle, x > 0.',
  'You can also expand and subtract seventy-seven. This gives x squared plus four x minus seventy-seven equals zero. A rectangle needs a positive width.')],
 g(10,3,5,3),identities=[('x*(x+4)-77','x**2+4*x-77')]),

authored('geometry-area-polynomial-product','Write rectangle area as a polynomial',
 'A rectangle has sides (x + 3) cm and (x + 7) cm.\nWrite its area as a polynomial.','x² + 10x + 21 square centimetres',
 'A rectangle has sides x plus three centimetres and x plus seven centimetres. Write its area as a polynomial.',[
 ('LENGTH TIMES WIDTH','Multiply the two side expressions','A = (x + 3)(x + 7)',
  'Use length times width. Keep each side expression inside parentheses.'),
 ('DISTRIBUTE','Multiply each term by each term','A = x² + 7x + 3x + 21',
  'Multiply x by x and by seven, then three by x and by seven. This gives x squared, seven x, three x, and twenty-one.'),
 ('COMBINE LIKE TERMS','Seven x plus three x is ten x','A = x² + 10x + 21',
  'Combine the two x terms. Seven x plus three x equals ten x.'),
 ('CHECK WITH A VALUE','For x = 2, the sides are five and nine','5 × 9 = 45\n2² + 10(2) + 21 = 45',
  'Check with x equal to two. Both the side product and the polynomial give forty-five square centimetres.')],
 g(11,1,3,9),identities=[('(x+3)*(x+7)','x**2+10*x+21')],equalities=[('5*9','2**2+10*2+21')]),

authored('geometry-area-divide-polynomial-side','Find a side by dividing a polynomial area',
 'A rectangle has area (24x⁴ + 16x³) cm²\nand width 8x² cm, with x > 0. Find its length.','3x² + 2x centimetres',
 'A rectangle has area twenty-four x to the fourth plus sixteen x cubed, in square centimetres. Its width is eight x squared centimetres, with x positive. Find its length.',[
 ('DIVIDE BY THE KNOWN SIDE','Length equals area divided by width','Length = (24x⁴ + 16x³)/(8x²)',
  'Length equals area divided by width. Divide the whole area expression by eight x squared.'),
 ('DIVIDE EVERY TERM','Divide coefficients and subtract exponents','24x⁴/(8x²) = 3x²\n16x³/(8x²) = 2x',
  'Divide each term. Twenty-four divided by eight is three, and four minus two is two. The other term becomes two x.'),
 ('COMBINE THE RESULTS','Keep the addition between the terms','Length = 3x² + 2x cm',
  'Put the terms together. The length is three x squared plus two x centimetres.'),
 ('MULTIPLY TO CHECK','Width times length must recover the area','8x²(3x² + 2x) = 24x⁴ + 16x³',
  'Multiply your length by the width. You recover the original area, confirming that each term was divided correctly.')],
 g(11,3,1,7),identities=[('8*x**2*(3*x**2+2*x)','24*x**4+16*x**3')]),

authored('geometry-area-substitute-variable','Find area after substituting a value',
 'A rectangle has length (x + 4) cm and width 7 cm.\nFind its area when x = 9.','91 square centimetres',
 'A rectangle has length x plus four centimetres and width seven centimetres. Find its area when x equals nine.',[
 ('SUBSTITUTE','Replace x with its given value','Length = 9 + 4',
  'First replace x with nine in the expression for length.'),
 ('FIND THE LENGTH','Evaluate the expression before multiplying','Length = 13 cm',
  'Nine plus four is thirteen, so the rectangle is thirteen centimetres long.'),
 ('FIND THE AREA','Multiply length by width','A = 13 × 7 = 91 cm²',
  'Multiply thirteen by the width, seven. The area is ninety-one square centimetres.'),
 ('CHECK THE ORDER','Evaluate the side, then calculate area','A = (9 + 4) × 7 = 91 cm²',
  'Keep the parentheses around the length expression. Add to find the length first, then multiply by the width.')],
 g(9,1,1,8),expression='(9+4)*7',value='91'),

authored('geometry-perimeter-additive-side-equation','Find width when length is a fixed amount longer',
 'A rectangle has perimeter 44 cm.\nIts length is 8 cm more than its width.\nFind the width.','7 centimetres',
 'A rectangle has perimeter forty-four centimetres. Its length is eight centimetres more than its width. Find the width.',[
 ('WRITE BOTH SIDES','Let the width be w','Width = w\nLength = w + 8',
  'Let w be the width. Since the length is eight more, write it as w plus eight.'),
 ('USE ALL FOUR SIDES','Perimeter counts two lengths and two widths','2(w + 8) + 2w = 44',
  'Two lengths plus two widths make forty-four. Write two times w plus eight, plus two w, equals forty-four.'),
 ('SOLVE THE EQUATION','Expand, subtract sixteen, then divide by four','4w + 16 = 44\n4w = 28 → w = 7',
  'Expand and collect terms. Four w plus sixteen equals forty-four. Subtract sixteen and divide by four to get seven.'),
 ('CHECK BOTH SIDES','The length is fifteen centimetres','2(15) + 2(7) = 44 cm\nWidth = 7 cm',
  'The width is seven and the length is fifteen. Twice fifteen plus twice seven is forty-four, so the perimeter checks.')],
 g(9,6,5,7),equation=('2*(w+8)+2*w','44','w','7'),equalities=[('2*15+2*7','44')]),

authored('geometry-volume-linear-drain-model','Write a linear model for a draining tank',
 'A tank starts with 150 L and loses 6 L each minute.\nWrite its volume V after t minutes, until it is empty.','V = 150 − 6t; 0 ≤ t ≤ 25',
 'A tank starts with one hundred fifty litres and loses six litres each minute. Write its volume after t minutes, until it is empty.',[
 ('STARTING AMOUNT','This is the volume at time zero','Starting volume = 150 L',
  'The starting volume is one hundred fifty litres. This is the value when t is zero.'),
 ('TOTAL LOST','Multiply the rate by elapsed time','Volume lost = 6t L',
  'At six litres per minute, the tank loses six t litres after t minutes.'),
 ('SUBTRACT THE LOSS','Remaining volume is start minus loss','V = 150 − 6t',
  'Subtract that loss from the starting amount. The model is V equals one hundred fifty minus six t.'),
 ('CHECK THE TIME INTERVAL','Use this model only until the tank is empty','150 ÷ 6 = 25 minutes\n0 ≤ t ≤ 25',
  'The tank empties after twenty-five minutes. Use the formula from time zero through twenty-five minutes; it cannot describe negative water volume.')],
 g(9,5,1,5),identities=[('150-6*t','6*(25-t)')],equalities=[('150/6','25')]),
]


def diagram(spec,d,scene,p):
    vid=spec['video_id']
    if vid in ('geometry-area-fraction-of-unit-square','geometry-area-equal-fractional-tiles','geometry-area-shaded-fraction') and scene in (1,2,3):
        shaded=4 if vid.endswith('fractional-tiles') else 5 if vid.endswith('shaded-fraction') else 1
        cw,ch=(72,120) if vid.endswith('unit-square') else (180,50) if vid.endswith('shaded-fraction') else (160,72)
        left,top=(1920-5*cw)/2,510-1.5*ch
        for r in range(3):
            for c in range(5):
                x,y=left+cw*c,top+ch*r
                d.rectangle((x,y,x+cw,y+ch),fill='#F1DBB9' if r*5+c<shaded else '#D0E8E2',outline=v.TEAL,width=3)
        v.centered(d,700,'15 equal parts',32,v.INK)
        for i,line in enumerate(spec['displays'][scene].split('\n')):centered_math(d,770+i*60,line,44,v.TEAL)
        return
    draw_card(spec,d,scene,p)


def lessons(doc):
    batch=make_lessons(SPECS,doc)
    for spec in SPECS:v.DRAW[spec['video_id']]=lambda d,scene,p,s=spec:diagram(s,d,scene,p)
    return batch
