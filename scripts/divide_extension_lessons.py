"""Long division diagrams, remainders, decimal quotients and zero rules."""
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons,draw_card
import generate_sample_videos as video
SPECS=[
authored('divide-two-digit-long','Use long division with a two-digit divisor',
 'Find 5184 ÷ 24 using long division.', '216',
 'Find five thousand one hundred eighty-four divided by twenty-four using long division.',[
 ('FIRST QUOTIENT DIGIT','Twenty-four goes into fifty-one twice','51 ÷ 24 = 2 remainder 3\n51 − 48 = 3',
 'Twenty-four does not fit into five, so start with fifty-one. It fits twice. Write two above the second digit, subtract forty-eight, and keep the remainder three.'),
 ('BRING DOWN EIGHT','Repeat divide, multiply and subtract','38 ÷ 24 = 1 remainder 14\n38 − 24 = 14',
 'Bring down eight to make thirty-eight. Twenty-four fits once. Write one in the next quotient place and subtract twenty-four, leaving fourteen.'),
 ('BRING DOWN FOUR','Finish the last quotient digit','144 ÷ 24 = 6\n144 − 144 = 0',
 'Bring down four to make one hundred forty-four. Twenty-four fits six times, with no remainder.'),
 ('READ AND CHECK','The quotient digits are two, one and six','5184 ÷ 24 = 216\n216 × 24 = 5184',
 'Read the quotient: two hundred sixteen. Multiply it by twenty-four to check that it gives the original dividend.')],
 g(5,5,'5HW',3),equalities=[('5184/24','216'),('51-24*2','3'),('38-24','14'),('144-24*6','0'),('216*24','5184')]),
authored('divide-two-digit-remainder','Find and check a whole-number quotient and remainder',
 'Find the quotient and remainder of 7265 ÷ 34.', '213 remainder 23',
 'Divide seven thousand two hundred sixty-five by thirty-four. Give a whole-number quotient and remainder.',[
 ('FIRST DIGIT','Thirty-four fits twice into seventy-two','72 − 2 × 34 = 4',
 'Start with seventy-two. Thirty-four fits twice. Subtract sixty-eight, leaving four.'),
 ('BRING DOWN SIX','The next partial dividend is forty-six','46 − 1 × 34 = 12',
 'Bring down six to make forty-six. Thirty-four fits once. Subtract thirty-four, leaving twelve.'),
 ('BRING DOWN FIVE','The final partial dividend is one hundred twenty-five','125 − 3 × 34 = 23',
 'Bring down five to make one hundred twenty-five. Thirty-four fits three times. Subtract one hundred two, leaving twenty-three.'),
 ('CHECK BOTH PARTS','The remainder must be smaller than the divisor','Quotient 213, remainder 23\n34 × 213 + 23 = 7265; 0 ≤ 23 < 34',
 'The quotient is two hundred thirteen, with remainder twenty-three. Check divisor times quotient plus remainder. It gives the dividend, and the remainder is smaller than thirty-four.')],
 g(5,5,'5HW',4),equalities=[('34*213+23','7265'),('72-2*34','4'),('46-34','12'),('125-3*34','23')]),
authored('divide-whole-to-decimal','Write a non-whole quotient as a decimal',
 'Find 90 ÷ 40. Give the answer as a decimal.', '2.25',
 'Find ninety divided by forty. Give the answer as a decimal.',[
 ('WHOLE PART','Two groups of forty use eighty','90 = 2 × 40 + 10',
 'Forty fits twice into ninety, using eighty and leaving ten.'),
 ('FRACTIONAL PART','The remainder is still divided by forty','90/40 = 2 + 10/40 = 2 + 1/4',
 'The leftover ten is ten fortieths of another group. Simplify ten fortieths to one fourth.'),
 ('CONVERT TO DECIMAL','One fourth is twenty-five hundredths','1/4 = 25/100 = 0.25\n2 + 0.25 = 2.25',
 'One fourth is twenty-five hundredths, or zero point two five. Add the two whole groups to get two point two five.'),
 ('CHECK','Multiply the decimal quotient by the divisor','2.25 × 40 = 90',
 'Two point two five times forty is ninety. The remainder became a fractional part of the quotient, rather than an extra whole-number digit.')],
 g(5,9,1,7),equalities=[('90/40','2.25'),('2*40+10','90'),('10/40','1/4'),('1/4','0.25'),('2.25*40','90')]),
authored('divide-zero-numerator-denominator','Distinguish zero divided by a number from division by zero',
 'Evaluate 0 ÷ 28 and 28 ÷ 0.', '0; undefined',
 'Evaluate zero divided by twenty-eight and twenty-eight divided by zero. The position of zero matters.',[
 ('ZERO NUMERATOR','Ask what number times twenty-eight gives zero','28 × 0 = 0\n0 ÷ 28 = 0',
 'Division reverses multiplication. Zero times twenty-eight is zero, so zero divided by twenty-eight equals zero.'),
 ('ZERO DENOMINATOR','Ask what number times zero could give twenty-eight','0 × any number = 0',
 'For twenty-eight divided by zero, we would need a number that gives twenty-eight when multiplied by zero. Every number times zero gives zero.'),
 ('NO POSSIBLE QUOTIENT','No number satisfies the required multiplication','28 ÷ 0 is undefined',
 'There is no possible quotient. Twenty-eight divided by zero is undefined, not zero.'),
 ('GENERAL RULE','The divisor must be nonzero','For a ≠ 0: 0/a = 0\nDivision by zero is undefined.',
 'Zero divided by a nonzero number is zero. Division by zero is undefined. Always check which number is the divisor.')],
 g(9,1,3,1),equalities=[('0/28','0'),('28*0','0')]),
]
LONG={
 'divide-two-digit-long':dict(dividend='5184',divisor='24',quotient='216',rows=['48','38','24','144','144','0']),
 'divide-two-digit-remainder':dict(dividend='7265',divisor='34',quotient='213',rows=['68','46','34','125','102','23'])}
for data in LONG.values():
 current=int(data['dividend'][:2]);divisor=int(data['divisor'])
 for j,q in enumerate(data['quotient']):
  assert current//divisor==int(q)
  assert int(data['rows'][2*j])==divisor*int(q)
  remainder=current%divisor
  if j<2:
   current=remainder*10+int(data['dividend'][j+2])
   assert int(data['rows'][2*j+1])==current
  else:assert int(data['rows'][2*j+1])==remainder

def draw_long(spec,d,scene,p):
 if scene not in (1,2,3):return draw_card(spec,d,scene,p)
 data=LONG[spec['video_id']]
 d.rounded_rectangle((145,335,1775,880),radius=35,fill='white')
 xs=[460,540,620,700]
 def digits(value,y,last,color=video.INK):
  for x,c in zip(xs[last-len(value)+1:last+1],value):
   d.text((x,y),c,font=video.font(48,True),fill=color,anchor='mm')
 for j,char in enumerate(data['quotient'][:scene]):digits(char,371,j+1,video.TEAL)
 d.line((410,403,750,403),fill=video.INK,width=3);d.line((410,403,410,468),fill=video.INK,width=3)
 d.text((340,442),data['divisor'],font=video.font(48,True),fill=video.INK,anchor='mm')
 digits(data['dividend'],442,3)
 for j in range(scene):
  subtract_y=494+110*j;remain_y=subtract_y+57;last=j+1
  digits(data['rows'][2*j],subtract_y,last)
  d.text((410,subtract_y),'−',font=video.font(40,True),fill=video.INK,anchor='mm')
  d.line((435,subtract_y+27,xs[last]+35,subtract_y+27),fill=video.MUTED,width=2)
  remainder=data['rows'][2*j+1]
  if j<2 and j==scene-1:digits(remainder[:-1],remain_y,last,video.TEAL)
  else:digits(remainder,remain_y,min(last+1,3),video.TEAL)
 # Only previous steps include the digit brought down for the next step.
 for j,line in enumerate(spec['displays'][scene].split('\n')):
  d.text((875,500+90*j),line,font=video.font(38,True),fill=video.TEAL if j else video.INK,anchor='lm')
 d.text((875,725),'Divide → multiply → subtract',font=video.font(31,True),fill=video.MUTED,anchor='lm')
 d.text((875,779),'Bring down the next digit.',font=video.font(31,True),fill=video.MUTED,anchor='lm')

def lessons(doc):
 result=make_lessons(SPECS,doc)
 for s in SPECS[:2]:video.DRAW[s['video_id']]=lambda d,scene,p,s=s:draw_long(s,d,scene,p)
 return result
