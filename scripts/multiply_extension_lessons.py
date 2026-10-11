"""Larger products, standard columns, and a nine-cell partial-product model."""
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons,draw_card
import generate_sample_videos as video
SPECS=[
authored('multiply-three-digit-single','Multiply a three-digit number by a single digit',
 'Find 326 × 4.', '1304',
 'Find three hundred twenty-six times four. Split the three-digit number by place value.',[
 ('SPLIT BY PLACE','Separate hundreds, tens and ones','326 × 4 = (300 + 20 + 6) × 4',
 'Three hundred twenty-six is three hundred plus twenty plus six. Multiply every part by four.'),
 ('HUNDREDS AND TENS','Keep the value of each place','300 × 4 = 1200\n20 × 4 = 80',
 'Three hundred times four is twelve hundred. Twenty times four is eighty.'),
 ('ONES','Multiply the final part','6 × 4 = 24',
 'Six times four is twenty-four. We now have all three partial products.'),
 ('ADD AND CHECK','Include all three parts','1200 + 80 + 24 = 1304\n1304 ÷ 4 = 326',
 'Add twelve hundred, eighty, and twenty-four to get one thousand three hundred four. Divide by four to check that the original number returns.')],
 g(4,3,3,8),equalities=[('326*4','1304'),('300*4','1200'),('20*4','80'),('6*4','24'),('1200+80+24','1304')]),
authored('multiply-four-digit-single','Multiply a four-digit number using place-value parts',
 'Find 2318 × 6.', '13908',
 'Find two thousand three hundred eighteen times six. Use one partial product for each place.',[
 ('SPLIT BY PLACE','Separate thousands, hundreds, tens and ones','2318 = 2000 + 300 + 10 + 8',
 'Split the number into two thousand, three hundred, ten, and eight.'),
 ('LARGER PLACES','Multiply the thousands and hundreds by six','2000 × 6 = 12000\n300 × 6 = 1800',
 'Two thousand times six is twelve thousand. Three hundred times six is eighteen hundred.'),
 ('SMALLER PLACES','Multiply the tens and ones by six','10 × 6 = 60\n8 × 6 = 48',
 'Ten times six is sixty. Eight times six is forty-eight.'),
 ('ADD ALL PARTS','Keep the place values aligned when adding','12000 + 1800 + 60 + 48 = 13908\n2318 × 6 = 13908',
 'Add all four products. Twelve thousand plus eighteen hundred is thirteen thousand eight hundred. Adding sixty and forty-eight gives thirteen thousand nine hundred eight.')],
 g(4,3,5,9),equalities=[('2318*6','13908'),('2000*6','12000'),('300*6','1800'),('10*6','60'),('8*6','48'),('12000+1800+60+48','13908')]),
authored('multiply-standard-two-digit','Use the standard algorithm for two-digit multiplication',
 'Find 76 × 48 using the standard algorithm.', '3648',
 'Find seventy-six times forty-eight using the standard multiplication algorithm.',[
 ('MULTIPLY BY EIGHT','Start with the ones digit of forty-eight','8 × 6 = 48: write 8, carry 4\n8 × 7 + 4 = 60\n76 × 8 = 608',
 'Start with eight. Eight times six is forty-eight: write eight, carry four. Eight times seven plus four is sixty. The first row is six hundred eight.'),
 ('MULTIPLY BY FORTY','The four is in the tens place','4 × 6 = 24: write 4, carry 2\n4 × 7 + 2 = 30\n76 × 40 = 3040',
 'Next use the four tens. Four times six is twenty-four: write four, carry two. Four times seven plus two is thirty. Shift this row one place left: three thousand forty.'),
 ('ADD THE ROWS','Line up ones, tens, hundreds and thousands','608 + 3040 = 3648',
 'Add the aligned rows. Six hundred eight plus three thousand forty gives three thousand six hundred forty-eight.'),
 ('CHECK THE METHOD','The two rows match the split into forty and eight','76 × (40 + 8)\n= 3040 + 608 = 3648',
 'The rows represent multiplying by forty and by eight. Including both gives three thousand six hundred forty-eight.')],
 g(5,5,2,9),equalities=[('76*48','3648'),('76*8','608'),('76*40','3040'),('608+3040','3648'),('8*7+4','60'),('4*7+2','30')]),
authored('multiply-nine-part-grid','Multiply two three-digit numbers with nine partial products',
 'Find 324 × 213 using partial products.', '69012',
 'Find three hundred twenty-four times two hundred thirteen using partial products.',[
 ('SPLIT BOTH NUMBERS','Use hundreds, tens and ones for each factor','324 = 300 + 20 + 4\n213 = 200 + 10 + 3',
 'Split each number into hundreds, tens, and ones. Three parts times three parts will give nine partial products.'),
 ('PAIR EVERY PART','Each row value multiplies each column value','300×200 = 60000; 300×10 = 3000; 300×3 = 900\n20×200 = 4000; 20×10 = 200; 20×3 = 60\n4×200 = 800; 4×10 = 40; 4×3 = 12',
 'Fill every cell by multiplying its row value and column value. For example, three hundred times ten is three thousand. Include all nine cells.'),
 ('ADD EACH ROW','Keep every partial product exactly once','60000 + 3000 + 900 = 63900\n4000 + 200 + 60 = 4260\n800 + 40 + 12 = 852',
 'Add across the rows. Their totals are sixty-three thousand nine hundred, four thousand two hundred sixty, and eight hundred fifty-two.'),
 ('TOTAL','Add the three row totals','63900 + 4260 + 852 = 69012\n324 × 213 = 69012',
 'Adding the three row totals gives sixty-nine thousand twelve. A missing table entry can be found from its row and column factors.')],
 g(5,5,2,3),equalities=[('324*213','69012'),('60000+3000+900','63900'),('4000+200+60','4260'),('800+40+12','852'),('63900+4260+852','69012')]),
]
assert sum(a*b for a in [300,20,4] for b in [200,10,3])==69012

def draw_standard(d,scene,p):
 if scene!=3:return draw_card(SPECS[2],d,scene,p)
 d.rounded_rectangle((145,360,1775,840),radius=35,fill='white')
 xs=[690,870,1050,1230]
 for j,label in enumerate(['1000s','100s','10s','1s']):d.text((xs[j],410),label,font=video.font(30,True),fill=video.MUTED,anchor='mm')
 for y,note,number in [(490,'76 × 8',608),(594,'76 × 40',3040),(756,'Total',3648)]:
  d.text((295,y),note,font=video.font(36,True),fill=video.MUTED,anchor='lm')
  for x,c in zip(xs,str(number).rjust(4)):
   if c!=' ':d.text((x,y),c,font=video.font(72,True),fill=video.TEAL if y==756 else video.INK,anchor='mm')
 d.text((555,594),'+',font=video.font(55,True),fill=video.INK,anchor='mm')
 d.line((625,661,1300,661),fill=video.MUTED,width=3)

def draw_grid(d,scene,p):
 if scene!=2:return draw_card(SPECS[3],d,scene,p)
 x0,y0=355,375;cw,ch=300,105
 rows=[300,20,4];cols=[200,10,3]
 for r in range(4):
  for c in range(4):
   x=x0+c*cw;y=y0+r*ch
   d.rectangle((x,y,x+cw,y+ch),fill='#e5f1ed' if r==0 or c==0 else 'white',outline='#b4beba',width=2)
   value='×' if r==c==0 else str(cols[c-1]) if r==0 else str(rows[r-1]) if c==0 else str(rows[r-1]*cols[c-1])
   d.text((x+cw/2,y+ch/2),value,font=video.font(44,True),fill=video.TEAL if r*c else video.INK,anchor='mm')

def lessons(doc):
 result=make_lessons(SPECS,doc)
 video.DRAW['multiply-standard-two-digit']=draw_standard
 video.DRAW['multiply-nine-part-grid']=draw_grid
 return result
