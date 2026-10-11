"""Checked regrouping and subtraction-chain lessons with explicit place columns."""
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons,draw_card
import generate_sample_videos as video
SPECS=[
authored('subtract-two-digit-regroup','Subtract two-digit numbers by regrouping a ten',
 'Find 64 − 28.', '36',
 'Find sixty-four minus twenty-eight. Start with the ones.',[
 ('REGROUP A TEN','Exchange one ten for ten ones','64 = 6 tens + 4 ones\n64 = 5 tens + 14 ones',
 'Four ones are not enough to take away eight. Exchange one ten for ten ones. Sixty-four becomes five tens and fourteen ones.'),
 ('SUBTRACT ONES','Now there are enough ones','14 − 8 = 6 ones',
 'Fourteen ones minus eight ones leaves six ones.'),
 ('SUBTRACT TENS','Use the five tens left after regrouping','5 − 2 = 3 tens\n30 + 6 = 36',
 'Use the five tens left after the exchange. Five tens minus two tens leaves three tens. Three tens and six ones make thirty-six.'),
 ('CHECK BY ADDING','The answer plus the amount removed returns the start','36 + 28 = 64',
 'Add twenty-eight back to thirty-six to get sixty-four. When subtracting a one-digit number, its tens digit is zero. Use the same regrouping method.')],
 g(1,2,5,9),equalities=[('64-28','36'),('5*10+14','64'),('14-8','6'),('5-2','3'),('36+28','64')]),
authored('subtract-two-digit-chain','Subtract several numbers from left to right',
 'Find 53 − 26 − 18.', '9',
 'Find fifty-three minus twenty-six minus eighteen. Work from left to right.',[
 ('FIRST SUBTRACTION','Regroup fifty-three as four tens and thirteen ones','53 − 26\n13 − 6 = 7 ones; 4 − 2 = 2 tens\n53 − 26 = 27',
 'First subtract twenty-six. Regroup fifty-three into four tens and thirteen ones. Subtract the ones and tens to get twenty-seven.'),
 ('USE THE NEW TOTAL','Subtract eighteen from twenty-seven','27 − 18\n17 − 8 = 9 ones; 1 − 1 = 0 tens\n27 − 18 = 9',
 'Now subtract eighteen from twenty-seven. Regroup again: one ten and seventeen ones. Seventeen minus eight is nine; one ten minus one ten is zero.'),
 ('CHECK WHAT WAS REMOVED','Add the two amounts taken away','26 + 18 = 44\n53 − 44 = 9',
 'Check by adding the two amounts removed. Twenty-six plus eighteen is forty-four. Fifty-three minus forty-four is nine.'),
 ('ANSWER','Each subtraction starts from the previous result','53 − 26 − 18 = 27 − 18 = 9',
 'The answer is nine. Keep the order: subtract the second number, then subtract the third from the result.')],
 g(2,1,'4HW',4),equalities=[('53-26','27'),('27-18','9'),('26+18','44'),('53-44','9'),('4*10+13','53'),('1*10+17','27')]),
authored('subtract-large-number-chain','Subtract large whole numbers in sequence',
 'Find 864,532 − 32,765 − 241,356.', '590,411',
 'Find eight hundred sixty-four thousand, five hundred thirty-two, minus thirty-two thousand, seven hundred sixty-five, minus two hundred forty-one thousand, three hundred fifty-six.',[
 ('FIRST SUBTRACTION','Align places; subtract 32,765 first','864,532 − 32,765 = 831,767',
 'Align place values, including the leading zero. Work right to left. Exchange from the next place whenever needed. The regrouped columns give eight hundred thirty-one thousand, seven hundred sixty-seven.'),
 ('SECOND SUBTRACTION','Use the previous result; subtract 241,356','831,767 − 241,356 = 590,411',
 'Now subtract from that result. Exchange one hundred thousand for ten ten-thousands. The remaining difference is five hundred ninety thousand, four hundred eleven.'),
 ('CHECK','Add back both amounts removed','32,765 + 241,356 = 274,121\n590,411 + 274,121 = 864,532',
 'Add both removed amounts, then add their total to the answer. This returns the starting number.'),
 ('ANSWER','Subtraction chains run from left to right','864,532 − 32,765 − 241,356\n= 831,767 − 241,356 = 590,411',
 'The answer is five hundred ninety thousand, four hundred eleven. Each subtraction uses the result of the previous one.')],
 g(4,2,'3HW',1),equalities=[('864532-32765','831767'),('831767-241356','590411'),('32765+241356','274121'),('590411+274121','864532')]),
]
# Every regrouped digit has its original place value; verify each column.
GRIDS={1:([8,6,3,14,12,12],[0,3,2,7,6,5],[8,3,1,7,6,7],864532),
       2:([7,13,1,7,6,7],[2,4,1,3,5,6],[5,9,0,4,1,1],831767)}
for top,bottom,result,original in GRIDS.values():
 assert sum(x*10**(5-i) for i,x in enumerate(top))==original
 assert [a-b for a,b in zip(top,bottom)]==result

def draw_columns(d,scene,p):
 if scene not in GRIDS:return draw_card(SPECS[2],d,scene,p)
 top,bottom,result,original=GRIDS[scene]
 d.rounded_rectangle((145,360,1775,840),radius=35,fill='white')
 video.centered(d,378,'Regrouped places (same value as '+f'{original:,}'+')',30,video.MUTED)
 labels=['100,000s','10,000s','1,000s','100s','10s','1s']
 for i,label in enumerate(labels):
  x=490+200*i
  d.text((x,446),label,font=video.font(26,True),fill=video.MUTED,anchor='mm')
  for y,row in [(517,top),(619,bottom),(758,result)]:
   d.text((x,y),str(row[i]),font=video.font(64,True),fill=video.TEAL if y==758 else video.INK,anchor='mm')
 d.text((296,619),'−',font=video.font(64,True),fill=video.INK,anchor='mm')
 d.line((365,679,1630,679),fill=video.MUTED,width=3)

def lessons(doc):
 result=make_lessons(SPECS,doc)
 video.DRAW['subtract-large-number-chain']=draw_columns
 return result
