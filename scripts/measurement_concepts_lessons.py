"""Capacity, units, decomposition and solid-volume methods."""
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons,draw_card,centered_math
import generate_sample_videos as v

SPECS=[
authored('measurement-capacity-metric-estimates','Choose reasonable metric capacities',
 'Choose the sensible capacity in each pair:\nMedicine dose: 10 mL or 10 L?\nBucket: 9 mL or 9 L?\nSports bottle: 750 mL or 750 L?',
 '10 mL; 9 L; 750 mL',
 'Choose sensible capacities for a medicine dose, a bucket, and a sports bottle. Think about the size of each container.',[
 ('COMPARE THE UNITS','One litre contains a thousand millilitres','1 L = 1000 mL',
  'One litre contains a thousand millilitres. The same number of litres is a thousand times as much liquid.'),
 ('A SMALL DOSE','A few millilitres suit a small amount','Medicine dose: 10 mL',
  'A small medicine dose could be ten millilitres. Ten litres would fill several large containers.'),
 ('A LARGE CONTAINER','A bucket can hold several litres','Bucket: 9 L',
  'A bucket can hold several litres, so nine litres makes sense. Nine millilitres would barely wet the bottom.'),
 ('CHECK NUMBER AND UNIT','Hundreds of millilitres can fit in a bottle','Sports bottle: 750 mL = 0.75 L',
  'For the sports bottle, choose seven hundred fifty millilitres, or three quarters of a litre. Compare both the number and the unit with the container.')],
 g(4,14,2,1),expression='750/1000',value='0.75'),

authored('measurement-capacity-customary-estimates','Choose reasonable customary capacity units',
 'Choose the better unit for each typical amount:\nSmall cream carton: 4 fluid ounces or 4 pints?\nFamily lemonade jug: 2 quarts or 2 gallons?\nOutdoor rain barrel: 50 cups or 50 gallons?',
 '4 fluid ounces; 2 quarts; 50 gallons',
 'Choose sensible units for a small cream carton, a family lemonade jug, and an outdoor rain barrel.',[
 ('SMALL AMOUNTS','Use fluid ounces for a small drink-size container','Small cream carton → 4 fluid ounces',
  'Four fluid ounces suit a small cream carton. Four pints would be much too large for this small container.'),
 ('MEDIUM CONTAINERS','Quarts suit a typical family serving jug','Family lemonade jug → 2 quarts',
  'Two quarts suit a typical family lemonade jug. Two gallons would require a much larger container.'),
 ('LARGE CONTAINERS','A rain barrel holds many gallons','Outdoor rain barrel → 50 gallons',
  'An outdoor rain barrel could hold fifty gallons. Fifty cups would be far too little for a large barrel.'),
 ('USE FAMILIAR SIZES','Match the unit to the amount being measured','Small spoonful → tablespoons\nServing bowl → cups\nU.S. units: 1 cup = 16 tablespoons',
  'Use tablespoons for a small spoonful and cups for a serving bowl. In U.S. customary units, one cup contains sixteen tablespoons. Match units to familiar amounts.')],
 g(4,14,2,7),expression='16/16',value='1'),

authored('measurement-volume-cubic-units','Choose cubic units for volume',
 'A storage box is 8 cm long, 4 cm wide and 3 cm high.\nFind its volume. Should its unit be cm² or cm³?',
 '96 cubic centimetres; cm³',
 'A storage box is eight centimetres long, four centimetres wide, and three centimetres high. Find its volume and choose square or cubic centimetres.',[
 ('THREE DIMENSIONS','Volume measures space inside a solid','V = 8 × 4 × 3',
  'Volume measures three-dimensional space. Multiply the length, width, and height.'),
 ('MULTIPLY THE LENGTHS','Eight times four times three is ninety-six','V = 96',
  'Eight times four is thirty-two. Multiply by three to get ninety-six.'),
 ('MULTIPLY THE UNITS','Three length units give a cubic unit','cm × cm × cm = cm³\nV = 96 cm³',
  'Centimetres times centimetres times centimetres gives cubic centimetres. The volume is ninety-six cubic centimetres.'),
 ('MATCH THE SCALE','Use larger cubes for larger spaces','Small objects → cm³\nLarge spaces → m³\nArea uses square units; volume uses cubic units.',
  'Small objects often use cubic centimetres. Large spaces use cubic metres. Square units measure area, while cubic units measure volume.')],
 g(5,11,1,8),expression='8*4*3',value='96'),

authored('geometry-volume-factor-order','Reordering factors preserves volume',
 'A box measures 9 cm by 3 cm by 2 cm.\nDoes 9 × 3 × 2 give a different volume from 2 × 9 × 3?',
 'No; both give 54 cubic centimetres',
 'A box measures nine centimetres by three centimetres by two centimetres. Does changing the order of these three factors change its volume?',[
 ('FIRST ORDER','Multiply nine, then three, then two','9 × 3 × 2 = 27 × 2 = 54',
  'In the first order, nine times three is twenty-seven. Multiply by two to get fifty-four.'),
 ('SECOND ORDER','Multiply two, then nine, then three','2 × 9 × 3 = 18 × 3 = 54',
  'In the other order, two times nine is eighteen. Multiply by three and you still get fifty-four.'),
 ('COMPARE','Both calculations use the same three factors','9 × 3 × 2 = 2 × 9 × 3',
  'Both products use exactly the same three dimensions. Multiplication gives the same result when the factors change order.'),
 ('KEEP EVERY FACTOR','Reordering preserves the product','Volume = 54 cm³ in either order',
  'Keep every factor exactly once. You can reorder them for an easier calculation without changing the volume.')],
 g(5,11,2,7),expression='9*3*2',value='54',equalities=[('9*3*2','2*9*3')]),

authored('geometry-volume-split-conservation','Splitting a solid preserves its total volume',
 'An 8 cm by 3 cm by 2 cm block is cut into\na 5 cm-long part and a 3 cm-long part.\nDoes the total volume change?',
 'No; 30 + 18 = 48 cubic centimetres',
 'An eight by three by two centimetre block is cut into a five centimetre-long part and a three centimetre-long part. Does the total volume change?',[
 ('BEFORE THE CUT','Find the original block’s volume','8 × 3 × 2 = 48 cm³',
  'Before the cut, multiply eight, three, and two. The original volume is forty-eight cubic centimetres.'),
 ('THE TWO PARTS','Only the length has been divided','Part A: 5 × 3 × 2 = 30 cm³\nPart B: 3 × 3 × 2 = 18 cm³',
  'The first part has volume thirty, and the second has volume eighteen. Both keep the original width and height.'),
 ('ADD THE PARTS','Count both pieces once','30 + 18 = 48 cm³',
  'Adding thirty and eighteen gives forty-eight, exactly the original volume.'),
 ('SAME MATERIAL','No piece is lost and no volume is counted twice','Whole volume = sum of the parts',
  'Splitting a solid preserves its total volume when no material is lost. Add all the non-overlapping parts to recover the whole.')],
 g(5,11,3,1),expression='8*3*2',value='48',equalities=[('5*3*2+3*3*2','48')]),

authored('geometry-volume-composite-convert-cubic-units','Add prism volumes and convert cubic units',
 'Two non-overlapping prisms form one solid:\n5 m × 4 m × 3 m and 2 m × 3 m × 4 m.\nFind the total volume in cm³.',
 '84,000,000 cubic centimetres',
 'Two non-overlapping prisms form one solid. They measure five by four by three metres, and two by three by four metres. Find the total volume in cubic centimetres.',[
 ('EACH PRISM','Multiply three dimensions for each part','5 × 4 × 3 = 60 m³\n2 × 3 × 4 = 24 m³',
  'The first prism has volume sixty cubic metres. The second has volume twenty-four cubic metres.'),
 ('ADD IN THE SAME UNIT','The sum is still in cubic metres','60 + 24 = 84 m³',
  'Add the two volumes to get eighty-four cubic metres. We still need to change the unit.'),
 ('CUBE THE CONVERSION','A metre is one hundred centimetres','1 m³ = 100 × 100 × 100 cm³\n1 m³ = 1,000,000 cm³',
  'A metre is one hundred centimetres. For cubic metres, multiply that conversion three times, giving one million cubic centimetres.'),
 ('CONVERT THE TOTAL','Multiply eighty-four by one million','84 m³ = 84,000,000 cm³',
  'Multiply eighty-four by one million. The answer is eighty-four million cubic centimetres. Always check the requested unit after adding volumes.')],
 g(5,11,3,8),expression='(5*4*3+2*3*4)*100**3',value='84000000'),

authored('measurement-choose-area-perimeter-volume','Choose area, perimeter or volume',
 'You need carpet to cover a 7 m by 4 m floor.\nShould you measure its area, perimeter or volume?',
 'Area; 28 square metres',
 'You need carpet to cover a seven metre by four metre floor. Should you measure its area, perimeter, or volume?',[
 ('WHAT ARE YOU MEASURING?','Carpet covers a flat surface','Covering a surface → area',
  'Carpet covers the floor’s flat surface, so the useful measurement is area.'),
 ('CALCULATE THE COVERAGE','Multiply length by width','7 × 4 = 28 m²',
  'Multiply seven by four. The floor has area twenty-eight square metres.'),
 ('COMPARE THE OTHER MEASUREMENTS','Each measurement answers a different question','Border around the floor → perimeter\nSpace inside a container → volume',
  'Perimeter measures the border around the floor. Volume measures the space inside a three-dimensional container.'),
 ('MATCH THE JOB','Choose the quantity before choosing a formula','Surface: square units\nBorder: length units\nSpace inside: cubic units',
  'Choose the quantity to match the job: square units for a surface, length units for a border, and cubic units for space inside.')],
 g(9,3,1,8),expression='7*4',value='28'),

authored('geometry-volume-rectangle','Prism volume with a decimal dimension',
 'A rectangular tank measures 8 m by 3 m by 1.2 m.\nFind its volume.','28.8 cubic metres',
 'A rectangular tank measures eight metres by three metres by one point two metres. Find its volume.',[
 ('CHOOSE THE FORMULA','Multiply length, width and height','V = 8 × 3 × 1.2',
  'Use the rectangular prism formula: length times width times height.'),
 ('FIND THE BASE AREA','Eight times three is twenty-four','Base area = 8 × 3 = 24 m²',
  'First multiply eight by three to find the base area, twenty-four square metres.'),
 ('MULTIPLY BY THE HEIGHT','Twenty-four times one point two','24 × 1.2 = 24 × 12 ÷ 10 = 28.8',
  'Multiply twenty-four by one point two. Twenty-four times twelve is two hundred eighty-eight; divide by ten to get twenty-eight point eight.'),
 ('USE CUBIC UNITS','Area times height gives volume','V = 28.8 m³',
  'The volume is twenty-eight point eight cubic metres. A decimal side length uses the same volume formula.')],
 g(9,3,2,1),expression='8*3*1.2',value='28.8'),

authored('geometry-volume-cavalieri','Compare volumes using matching cross-sections',
 'A straight prism has height 6 cm and base area 27 cm².\nA slanted solid has the same height, and every\nhorizontal cross-section also has area 27 cm².\nFind and compare their volumes.',
 'Both volumes are 162 cubic centimetres',
 'A straight prism is six centimetres high with base area twenty-seven square centimetres. A slanted solid has the same height and matching horizontal cross-sectional areas. Compare their volumes.',[
 ('FIND THE PRISM’S VOLUME','Base area times perpendicular height','V = 27 × 6 = 162 cm³',
  'The straight prism has volume twenty-seven times six, or one hundred sixty-two cubic centimetres.'),
 ('COMPARE AT EACH HEIGHT','Imagine slicing both solids horizontally','Every matching slice has equal area.',
  'Imagine thin horizontal slices through both solids. At every matching height, their cross-sectional areas are equal.'),
 ('MATCH THE HEIGHTS','The slices extend through the same total height','Equal heights + matching cross-sectional areas',
  'Their heights are also equal, so matching slices extend through the same total height.'),
 ('CONCLUDE EQUAL VOLUMES','This is Cavalieri’s principle','Straight prism: 162 cm³\nSlanted solid: 162 cm³',
  'Cavalieri’s principle says these conditions give equal volumes. The slanted solid also has volume one hundred sixty-two cubic centimetres.')],
 g(10,10,1,10),expression='27*6',value='162'),

authored('geometry-area-equivalent-decompositions','Find equivalent ways to calculate rectangle area',
 'A rectangle measures 39 cm by 7 cm.\nShow how splitting or extending its length\ncan help calculate the same area.',
 '273 square centimetres',
 'A rectangle measures thirty-nine centimetres by seven centimetres. Show how splitting or extending its length can help calculate the same area.',[
 ('SPLIT THE LENGTH','Thirty-nine is thirty plus nine','39 × 7 = (30 × 7) + (9 × 7)',
  'Split thirty-nine into thirty plus nine. Multiply each part by seven, then add the areas.'),
 ('ADD THE PARTS','Two smaller areas make the whole','210 + 63 = 273 cm²',
  'Thirty times seven is two hundred ten. Nine times seven is sixty-three. Their sum is two hundred seventy-three.'),
 ('EXTEND AND SUBTRACT','Thirty-nine is forty minus one','39 × 7 = (40 × 7) − (1 × 7)\n280 − 7 = 273 cm²',
  'Or extend the length to forty, then remove the extra strip. Forty times seven minus one times seven also gives two hundred seventy-three.'),
 ('SAME TOTAL AREA','Both methods preserve the original rectangle','Split and add, or extend and subtract.',
  'Both methods keep the same total area. To check another expression, make sure its added and subtracted lengths still give thirty-nine.')],
 g(4,3,'3Rev',5),expression='39*7',value='273',equalities=[('30*7+9*7','273'),('40*7-1*7','273')]),

authored('geometry-volume-cone','Find cone volume using a matching cylinder',
 'A cone has radius 5 cm and perpendicular height 9 cm.\nFind its exact volume in terms of pi.',
 '75π cubic centimetres',
 'A cone has radius five centimetres and perpendicular height nine centimetres. Find its exact volume in terms of pi.',[
 ('CIRCULAR BASE','The base area is pi times radius squared','B = πr² = π × 5² = 25π cm²',
  'The circular base has area pi times the radius squared. Five squared is twenty-five, giving twenty-five pi.'),
 ('MATCHING CYLINDER','Use the same radius and perpendicular height','Cylinder volume = 25π × 9 = 225π cm³',
  'A cylinder with the same radius and height has volume base area times height, or two hundred twenty-five pi.'),
 ('TAKE ONE THIRD','A cone has one third of that cylinder’s volume','Cone volume = 225π ÷ 3 = 75π cm³',
  'A cone has one third of the matching cylinder’s volume. Divide by three to get seventy-five pi cubic centimetres.'),
 ('REMEMBER THE FORMULA','The factor one third distinguishes the cone','V = (1/3)πr²h\nUse perpendicular height, not slant height.',
  'The cone formula is one third pi r squared h. Use the perpendicular height, and remember the factor of one third.')],
 g(10,10,2,4),expression='5**2*9/3',value='75'),
]


def diagram(spec,d,scene,p):
    if spec['video_id']=='geometry-volume-cavalieri' and scene in (2,3):
        for x,slant in [(530,0),(1120,15)]:
            for i in range(7):
                left,y=x+i*slant,700-i*42
                d.polygon([(left,y),(left+180,y),(left+235,y-35),(left+55,y-35)],fill='#D0E8E2',outline=v.TEAL,width=3)
        v.text(d,(640,365),'Straight prism',36,v.INK,True,anchor='mm')
        v.text(d,(1320,365),'Slanted solid',36,v.INK,True,anchor='mm')
        centered_math(d,750,'Both heights: 6 cm; each horizontal section: 27 cm²',38,v.INK)
        centered_math(d,835,spec['displays'][scene],42,v.TEAL)
        return
    draw_card(spec,d,scene,p)


def lessons(doc):
    batch=make_lessons(SPECS,doc)
    for spec in SPECS:v.DRAW[spec['video_id']]=lambda d,scene,p,s=spec:diagram(s,d,scene,p)
    return batch
