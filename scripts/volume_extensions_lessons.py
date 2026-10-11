"""Checked analogous examples for block counts, fractional dimensions and scaling."""
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons, draw_card
import generate_sample_videos as v

SPECS=[
authored('geometry-volume-count-blocks','Volume from the number of equal blocks',
 'A solid is packed with 18 identical blocks, without gaps.\nEach block has volume 4 cm³. Find the solid volume.','72 cubic centimetres',
 'A solid is packed with eighteen identical blocks, without gaps. Each block has volume four cubic centimetres. Find the solid volume.',[
 ('ONE BLOCK','Use the volume already given','Each block: 4 cm³',
  'We already know each block has volume four cubic centimetres. This is a volume, not a side length.'),
 ('COUNT ALL BLOCKS','Multiply count by volume per block','Total volume = 18 × 4',
  'Multiply the eighteen blocks by four cubic centimetres per block.'),
 ('CALCULATE','No gaps or overlaps are included','18 × 4 = 72 cm³',
  'Eighteen times four is seventy-two cubic centimetres.'),
 ('GENERAL RULE','Count times volume of one block','Total volume = number of blocks × one block volume',
  'Multiply the number of equal blocks by the volume of one block. For unit cubes, each cube contributes one cubic unit.')],
 g(5,11,1,7),expression='18*4',value='72'),

authored('geometry-volume-layers-of-blocks','Volume from layers of equal blocks',
 'A solid has 5 layers with 6 blocks in each layer.\nEach block has volume 2 cm³. Find the total volume.','60 cubic centimetres',
 'A solid has five layers with six blocks in each layer. Each block has volume two cubic centimetres. Find the total volume.',[
 ('COUNT THE BLOCKS','Layers times blocks per layer','5 × 6 = 30 blocks',
  'First count the blocks. Five layers of six blocks contain thirty blocks.'),
 ('USE BLOCK VOLUME','Each block occupies two cubic centimetres','30 × 2',
  'Each block has volume two cubic centimetres. Multiply the block count by two.'),
 ('CALCULATE','A block count and a volume are different quantities','30 × 2 = 60 cm³',
  'The total volume is sixty cubic centimetres. Thirty is the number of blocks, not the final volume.'),
 ('GENERAL RULE','Include all three factors','Volume = layers × blocks per layer × block volume',
  'Multiply layers, blocks per layer, and the volume of one block. When each block is a unit cube, its volume factor is one.')],
 g(5,11,1,10),expression='5*6*2',value='60'),

authored('geometry-volume-compare-block-counts','Compare volumes using equal-size blocks',
 'Box A holds 9 blocks; Box B holds 13 blocks.\nAll blocks have volume 2 cm³, with no gaps.\nWhich box has the larger volume?','Box B: 26 cubic centimetres',
 'Box A holds nine blocks, and Box B holds thirteen blocks. All blocks have volume two cubic centimetres, with no gaps. Which box has the larger volume?',[
 ('COMPARE THE UNITS','The blocks must be the same size','One block in either box: 2 cm³',
  'Both boxes use the same size blocks, so each counted block represents the same amount of space.'),
 ('FIND BOTH VOLUMES','Multiply each count by two','A: 9 × 2 = 18 cm³\nB: 13 × 2 = 26 cm³',
  'Box A has volume eighteen cubic centimetres. Box B has volume twenty-six cubic centimetres.'),
 ('COMPARE','Twenty-six is greater than eighteen','26 > 18, so Box B has the larger volume.',
  'Twenty-six is greater than eighteen, so Box B has the larger volume.'),
 ('GENERAL RULE','More equal-size blocks means more volume','Same block size → compare block counts',
  'With equal-size blocks, more blocks means more volume. If block sizes differ, calculate both volumes before comparing.')],
 g(5,11,1,4),expression='13*2',value='26',equalities=[('9*2','18')]),

authored('geometry-volume-compare-block-sizes','Compare volumes when block sizes differ',
 'Two solids each contain 11 blocks, without gaps.\nA uses 3 cm³ blocks; B uses 5 cm³ blocks.\nWhich solid has the larger volume?','Solid B: 55 cubic centimetres',
 'Two solids each contain eleven blocks, without gaps. A uses three-cubic-centimetre blocks. B uses five-cubic-centimetre blocks. Which solid has the larger volume?',[
 ('SAME COUNT','Each solid has eleven blocks','A: 11 blocks     B: 11 blocks',
  'The block counts are equal, but the blocks do not have the same volume.'),
 ('CALCULATE','Multiply each count by its block volume','A: 11 × 3 = 33 cm³\nB: 11 × 5 = 55 cm³',
  'Solid A has volume thirty-three cubic centimetres. Solid B has volume fifty-five cubic centimetres.'),
 ('COMPARE','B uses larger blocks','55 > 33, so Solid B has the larger volume.',
  'Fifty-five is greater than thirty-three. Solid B has the larger volume.'),
 ('GENERAL RULE','Equal counts need not mean equal volumes','Same block count → larger blocks give larger volume',
  'When block counts match, larger blocks give greater total volume. Always check the size of the counting unit.')],
 g(6,10,2,5),expression='11*5',value='55',equalities=[('11*3','33')]),

authored('geometry-volume-cube-fractional-side','Cube volume with a fractional side',
 'A cube has side length 2/5 ft. Find its volume.','8/125 cubic feet',
 'A cube has side length two fifths of a foot. Find its volume.',[
 ('THREE EQUAL DIMENSIONS','Multiply the side length three times','V = (2/5) × (2/5) × (2/5)',
  'A cube has three equal dimensions. Multiply two fifths by itself three times.'),
 ('MULTIPLY NUMERATORS','Multiply the top numbers and the bottom numbers','V = (2 × 2 × 2)/(5 × 5 × 5)',
  'Multiply the three numerators together and the three denominators together.'),
 ('SIMPLIFY','Eight and one hundred twenty-five share no common factor','V = 8/125 ft³',
  'The result is eight over one hundred twenty-five cubic feet. The fraction is already simplified.'),
 ('CHECK THE SCALE','A side under one foot gives volume under one cubic foot','0 < 8/125 < 1',
  'Each side is less than one foot, so the volume is less than one cubic foot. Remember to cube the denominator as well as the numerator.')],
 g(6,10,2,2),expression='(2/5)**3',value='8/125'),

authored('geometry-volume-prism-fractional-dimensions','Prism volume with fractional dimensions',
 'A prism measures 2 2/3 m by 3/7 m by 1 3/4 m.\nFind its volume.','2 cubic metres',
 'A rectangular prism measures two and two thirds metres, by three sevenths of a metre, by one and three quarters metres. Find its volume.',[
 ('CONVERT MIXED NUMBERS','Write every dimension as one fraction','2 2/3 = 8/3     1 3/4 = 7/4',
  'Convert mixed numbers to improper fractions. Two and two thirds is eight thirds. One and three quarters is seven quarters.'),
 ('MULTIPLY','Volume is length times width times height','V = (8/3) × (3/7) × (7/4)',
  'Multiply all three dimensions.'),
 ('CANCEL COMMON FACTORS','Cancel across the complete product','V = (8 × 3 × 7)/(3 × 7 × 4)\nV = 8/4 = 2',
  'Cancel matching factors of three and seven. Eight divided by four is two.'),
 ('STATE THE VOLUME','Three metre measurements give cubic metres','V = 2 m³',
  'The volume is two cubic metres. If the simplified answer is an improper fraction, convert it to a mixed number when requested.')],
 g(6,10,2,10),expression='(8/3)*(3/7)*(7/4)',value='2'),

authored('geometry-volume-dimension-scale-factors','How dimension changes affect volume',
 'A prism has volume 18 cm³. Its length doubles,\nits width triples, and its height stays the same.\nFind the new volume.','108 cubic centimetres',
 'A prism has volume eighteen cubic centimetres. Its length doubles, its width triples, and its height stays the same. Find the new volume.',[
 ('TRACK EACH DIMENSION','Record one scale factor for each length','Length: ×2     Width: ×3     Height: ×1',
  'The three dimension scale factors are two, three, and one.'),
 ('MULTIPLY SCALE FACTORS','Volume multiplies all three dimensions','Volume factor = 2 × 3 × 1 = 6',
  'Volume is a product of three dimensions, so multiply their scale factors. The volume factor is six.'),
 ('SCALE THE ORIGINAL','Multiply the original volume by six','New volume = 18 × 6 = 108 cm³',
  'Multiply eighteen by six. The new volume is one hundred eight cubic centimetres.'),
 ('GENERAL RULE','Unchanged dimensions contribute a factor of one','Volume factor = a × b × c\nAll dimensions scaled by k → volume scaled by k³',
  'Multiply all dimension factors, using one for unchanged dimensions. If every dimension scales by the same factor k, volume scales by k cubed.')],
 g(6,10,3,9),expression='18*2*3*1',value='108',identities=[('(a*x)*(b*y)*(c*z)','a*b*c*x*y*z')]),

authored('geometry-volume-water-level-change','Find volume from a change in water level',
 'A rectangular tank has a 9 cm by 7 cm base.\nFully submerged blocks raise the water from 4 cm to 8 cm.\nNo water spills. Find the blocks’ total volume.','252 cubic centimetres',
 'A rectangular tank has a nine by seven centimetre base. Fully submerged blocks raise the water from four to eight centimetres. No water spills. Find the blocks\' total volume.',[
 ('CHANGE IN HEIGHT','Use the rise, not the final water height','8 − 4 = 4 cm',
  'The water rises by eight minus four, or four centimetres.'),
 ('BASE AREA','Multiply the two base dimensions','9 × 7 = 63 cm²',
  'The tank base area is nine times seven, or sixty-three square centimetres.'),
 ('DISPLACED VOLUME','Base area times rise gives added occupied volume','63 × 4 = 252 cm³',
  'Multiply the base area by the rise. The displaced volume is two hundred fifty-two cubic centimetres.'),
 ('INTERPRET','Fully submerged blocks displace their own volume','Blocks’ volume = 252 cm³',
  'Because the blocks are fully submerged and no water spills, this is their total volume. For a water-level drop, base area times the drop gives the volume lost.')],
 g(6,10,3,10),expression='9*7*(8-4)',value='252'),

authored('geometry-volume-container-minus-block','Subtract an occupied volume',
 'A 10 cm by 8 cm by 6 cm tank contains a solid block\nmeasuring 4 cm by 3 cm by 5 cm. Water fills all remaining\nspace to the rim. Find the water volume.','420 cubic centimetres',
 'A ten by eight by six centimetre tank contains a solid block measuring four by three by five centimetres. Water fills all remaining space to the rim. Find the water volume.',[
 ('WHOLE CONTAINER','Use the tank’s inside dimensions','Tank volume = 10 × 8 × 6 = 480 cm³',
  'Multiply the tank\'s inside dimensions. Its total capacity is four hundred eighty cubic centimetres.'),
 ('OCCUPIED SPACE','The solid block takes up part of the tank','Block volume = 4 × 3 × 5 = 60 cm³',
  'The solid block occupies four times three times five, or sixty cubic centimetres.'),
 ('SUBTRACT','Water cannot occupy the solid block','Water volume = 480 − 60 = 420 cm³',
  'Subtract the block volume from the tank capacity. The water occupies four hundred twenty cubic centimetres.'),
 ('CHECK','Water and solid together fill the container','420 + 60 = 480 cm³',
  'The water and block volumes add to the whole tank volume. Use the same length units for every dimension.')],
 g(5,11,3,9),expression='10*8*6-4*3*5',value='420'),
]


def diagram(spec,d,scene,p):
    if spec['video_id']=='geometry-volume-water-level-change' and scene==1:
        x,y,w,h=590,390,670,385
        d.rectangle((x,y,x+w,y+h),fill='white',outline=v.INK,width=4)
        top=y+h-8*38;old=y+h-4*38
        d.rectangle((x+4,top,x+w-4,y+h-4),fill='#D0E8E2')
        d.line((x,top,x+w,top),fill=v.TEAL,width=5)
        for k in range(x,x+w,24):d.line((k,old,min(k+12,x+w),old),fill=v.INK,width=3)
        v.text(d,(x+w+30,top-20),'8 cm',38,v.INK,True)
        v.text(d,(x+w+30,old-20),'4 cm',38,v.INK,True)
        v.text(d,(x+110,y+h+20),'Tank cross-section; base: 9 cm × 7 cm',30,v.INK)
        v.centered(d,870,'Rise = 8 − 4 = 4 cm',48,v.TEAL,True);return
    draw_card(spec,d,scene,p)


def lessons(doc):
    result=make_lessons(SPECS,doc)
    for spec in SPECS:v.DRAW[spec['video_id']]=lambda d,scene,p,s=spec:diagram(s,d,scene,p)
    return result
