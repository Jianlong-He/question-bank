"""Short, concrete counting and place-value examples for the earliest worksheets."""
from algebra_lessons import authored
from card_lessons import make_lessons,draw_card
from number_sense_lessons import source
import generate_sample_videos as video

def g(w,q):return source(1,1,w,q)
SPECS=[]
def add(vid,title,question,answer,opening,steps,ref,expression,value):
 SPECS.append(authored(vid,title,question,answer,opening,steps,ref,expression=expression,value=value))

add('count-objects-one-to-one','Count each object exactly once',
 'How many counters are shown?','9',
 'How many counters are here? Let us count them carefully.',[
 ('START AT ONE','Touch one counter for each number','One counter gets one counting number.',
 'Start on the left. Point to the first counter and say one.'),
 ('COUNT IN ORDER','Keep moving along the row','1, 2, 3, 4, 5',
 'Count across the first row. One, two, three, four, five.'),
 ('COUNT THE REST','Keep the count going on the next row','6, 7, 8, 9',
 'Continue on the next row. Six, seven, eight, nine. Count each counter once.'),
 ('SAY THE TOTAL','The last counting number tells how many','There are 9 counters.',
 'The last number we said was nine. There are nine counters altogether.')],g(1,1),'5+4','9')
add('count-fill-ones','Fill a missing number when counting by ones',
 'Fill the gap: 84, 85, __, 87, 88.','86',
 'There is a missing number: eighty-four, eighty-five, a gap, eighty-seven, eighty-eight.',[
 ('FIND THE STEP','Each number is one more','84 → 85 is a step of 1.',
 'Look at the numbers we know. Eighty-five is one more than eighty-four.'),
 ('FILL THE GAP','Count one more than the number before it','85 + 1 = 86',
 'One more than eighty-five is eighty-six. Put eighty-six in the gap.'),
 ('CHECK THE NEXT NUMBER','One more should reach the next number','86 + 1 = 87',
 'One more than eighty-six is eighty-seven. That matches the next number.'),
 ('READ THE WHOLE LIST','Do not skip or repeat a number','84, 85, 86, 87, 88',
 'Read the list: eighty-four, eighty-five, eighty-six, eighty-seven, eighty-eight. Each step adds one.')],g(1,2),'85+1','86')
add('count-previous-one','Find the number immediately before another',
 'What number comes immediately before 80?','79',
 'What number comes immediately before eighty?',[
 ('GO BACK ONE','Before means one smaller when counting by ones','78, 79, 80, 81',
 'When we count by ones, the number before is one smaller.'),
 ('LOOK AT THE NEIGHBOURS','Seventy-nine leads into eighty','78 → 79 → 80',
 'Count seventy-eight, seventy-nine, eighty. The number just before eighty is seventy-nine.'),
 ('WRITE THE ANSWER','Subtract one from the starting number','80 − 1 = 79',
 'Eighty minus one is seventy-nine. Crossing a ten does not change the size of the step.'),
 ('CHECK FORWARD','Adding one should get back to the start','79 + 1 = 80',
 'Check by counting forward once. Seventy-nine, eighty. The answer is seventy-nine.')],g(2,2),'80-1','79')
add('place-teen-ten-frame','Build a teen number from one ten and extra ones',
 'One ten frame is full. A second has 8 dots.\nHow many dots are there altogether?','18',
 'One ten frame is full. Another has eight dots. How many dots are there altogether?',[
 ('USE THE FULL FRAME','A full ten frame holds ten dots','1 full frame = 10 dots',
 'A ten frame has two rows of five. A full frame holds ten dots.'),
 ('COUNT THE EXTRA ONES','The second frame holds eight more','10 and 8 more',
 'Keep the ten together. The other frame has eight extra dots.'),
 ('PUT THE PARTS TOGETHER','One ten and eight ones make eighteen','10 + 8 = 18',
 'Ten and eight more make eighteen. Eighteen has one ten and eight ones.'),
 ('TAKE THE NUMBER APART','The ten and ones are the same two parts','18 = 10 + 8\n18 − 8 = 10; 18 − 10 = 8',
 'We can take eighteen apart again. Remove eight and ten remains. Remove ten and eight remains.')],g(3,6),'10+8','18')
add('count-ten-frames','Count full ten frames and groups of ten',
 'There are 4 full ten frames.\nHow many dots do they hold?','40',
 'Four ten frames are full. How many dots do they hold altogether?',[
 ('COUNT THE FRAMES','Each full frame is one group of ten','4 full frames; 10 dots in each',
 'There are four frames. Every full frame has ten dots.'),
 ('COUNT BY TENS','Say one total for each frame','10, 20, 30, 40',
 'Count the groups: ten, twenty, thirty, forty.'),
 ('NAME THE TOTAL','Four tens make forty','10 + 10 + 10 + 10 = 40',
 'Four tens make forty. The four full frames hold forty dots.'),
 ('WORK BACKWARD','Forty dots fill four ten frames','40 dots = 4 full ten frames',
 'You can also work backward. To show forty dots in full ten frames, you need four frames.')],g(2,7),'10+10+10+10','40')
add('count-tens-both-directions','Count forward and backward in steps of ten',
 'Count by tens from 60 to 90.\nThen count back to 60.','60,70,80,90;90,80,70,60',
 'Count by tens from sixty to ninety, then count back to sixty.',[
 ('START WITH THE GIVEN NUMBER','Forward steps add ten','60 → 70',
 'Start by saying sixty. Add ten to get seventy.'),
 ('KEEP THE SAME STEP','Add ten until you reach ninety','60, 70, 80, 90',
 'Add ten again for eighty, and again for ninety. Include the starting number.'),
 ('REVERSE THE DIRECTION','Backward steps take away ten','90, 80, 70, 60',
 'Now take away ten each time. Ninety, eighty, seventy, sixty.'),
 ('CHECK EVERY GAP','The ones digit stays the same','70 − 60 = 10\n90 − 80 = 10',
 'Every gap is ten. In these numbers, the tens change while the ones stay zero.')],g(2,4),'90-60','30')
add('count-fives-both-directions','Count forward and backward in steps of five',
 'Count by fives from 55 to 75.\nWhat comes just before 55 in this pattern?','55,60,65,70,75;50',
 'Count by fives from fifty-five to seventy-five. Then find the number just before fifty-five in that pattern.',[
 ('ADD FIVE EACH TIME','The step is five, even across a ten','55 + 5 = 60; 60 + 5 = 65',
 'Add five each time. Fifty-five becomes sixty, then sixty-five.'),
 ('FINISH THE LIST','Include the starting and stopping numbers','55, 60, 65, 70, 75',
 'Continue: seventy, seventy-five. That gives the full list.'),
 ('GO BACK FIVE','Before in this pattern means five less','55 − 5 = 50',
 'The number before fifty-five in this pattern is five less. That is fifty.'),
 ('CHECK THE PATTERN','Each neighbouring pair is five apart','50, 55, 60, 65, 70, 75',
 'Read the longer list. Every neighbouring pair is five apart. Use that same gap to check a missing number.')],g(6,1),'55-5','50')
add('count-twos-both-directions','Count forward and backward in steps of two',
 'Count by twos from 23 to 31.\nWhat comes just before 23 in this pattern?','23,25,27,29,31;21',
 'Count by twos from twenty-three to thirty-one. What comes just before twenty-three in this pattern?',[
 ('ADD TWO','Jump over one counting number','23 + 2 = 25',
 'Add two to twenty-three. We reach twenty-five, jumping over twenty-four.'),
 ('KEEP GOING','Use the same jump until the stopping number','23, 25, 27, 29, 31',
 'Keep adding two. Twenty-seven, twenty-nine, thirty-one. We have reached the stopping number.'),
 ('GO BACK TWO','Before in this pattern means two less','23 − 2 = 21',
 'Go back two to find the number before twenty-three in this pattern. It is twenty-one.'),
 ('CHECK THE GAPS','Counting by twos can start on an odd number','21, 23, 25, 27, 29, 31',
 'The gaps are all two. Counting by twos can start on an odd number as well as an even number.')],g(7,1),'23+2*4','31')
add('count-two-stage-steps','Follow a counting pattern when the step changes',
 'Start at 0. Take 3 jumps of ten,\nthen 3 jumps of five. Where do you finish?','45',
 'Start at zero. Take three jumps of ten, then three jumps of five. Where do you finish?',[
 ('FIRST KIND OF JUMP','Take exactly three jumps of ten','0 → 10 → 20 → 30',
 'The first three jumps go to ten, twenty, and thirty.'),
 ('CHANGE THE STEP','Start the new jumps where the old ones finished','30 → 35 → 40 → 45',
 'Stay at thirty and change to jumps of five. Go to thirty-five, forty, and forty-five.'),
 ('READ THE FINISH','Do not restart at zero when the step changes','Finish: 45',
 'The final number is forty-five. We continued from thirty when the step changed.'),
 ('CHECK BOTH PARTS','Check the number and size of each jump','10 + 10 + 10 = 30\n5 + 5 + 5 = 15; 30 + 15 = 45',
 'Three tens give thirty. Three fives add fifteen more. Together they make forty-five.')],g(7,7),'3*10+3*5','45')
add('count-number-of-jumps','Count jumps separately from the starting number',
 'Start at 0 and jump by twos to 12.\nHow many jumps do you make?','6',
 'Start at zero and jump by twos to twelve. How many jumps do you make?',[
 ('START BEFORE THE FIRST JUMP','Saying zero does not use a jump','Start: 0. Jumps so far: 0.',
 'Zero is the starting place. We have not made a jump yet.'),
 ('COUNT THREE JUMPS','Count one jump for each move','0 → 2 → 4 → 6\n3 jumps',
 'One jump reaches two. Two jumps reach four. Three jumps reach six.'),
 ('CONTINUE TO TWELVE','Keep counting the moves','6 → 8 → 10 → 12\n3 more jumps',
 'Three more jumps reach eight, ten, then twelve.'),
 ('ADD THE JUMPS','Count moves, not all the numbers spoken','3 + 3 = 6 jumps',
 'Three jumps and three more make six jumps. The starting zero was not a jump.')],g(7,6),'12/2','6')
add('count-equal-groups-fives','Count objects in equal groups of five',
 'Four bags each hold 5 beads.\nHow many beads are there altogether?','20',
 'Four bags each hold five beads. How many beads are there altogether?',[
 ('LOOK AT ONE GROUP','Each bag has the same number','5 beads in each bag',
 'Each bag holds five beads. The groups are equal.'),
 ('COUNT THE FIRST TWO GROUPS','Add five for each bag','5, 10',
 'The first bag gives five beads. The second brings the total to ten.'),
 ('COUNT ALL FOUR GROUPS','Say one total for each group','5, 10, 15, 20',
 'The third brings us to fifteen. The fourth brings us to twenty.'),
 ('WRITE THE TOTAL','Four groups of five make twenty','5 + 5 + 5 + 5 = 20 beads',
 'Four groups of five make twenty beads. Counting by fives keeps track of the equal groups.')],g(7,9),'5+5+5+5','20')
add('count-pairs-groups','Count how many pairs can be made',
 'Put 14 children into pairs.\nHow many pairs can you make?','7',
 'Fourteen children line up in pairs. How many pairs can you make?',[
 ('MAKE A PAIR','A pair has two children','1 pair = 2 children',
 'A pair is a group of two children.'),
 ('COUNT CHILDREN BY TWOS','Each count makes one more pair','2, 4, 6, 8',
 'One pair uses two children. Two pairs use four. Three pairs use six. Four pairs use eight.'),
 ('KEEP MAKING PAIRS','Stop when every child has a partner','10, 12, 14\n5, 6, 7 pairs',
 'Five pairs use ten children, six pairs use twelve, and seven pairs use fourteen.'),
 ('SAY HOW MANY GROUPS','The question asks for pairs, not children','14 children make 7 pairs.',
 'All fourteen children have partners. There are seven pairs.')],g(7,10),'14/2','7')
add('place-add-one-ten','Add one ten to a two-digit number',
 'Add 1 ten to 43. What number do you get?','53',
 'Add one ten to forty-three. What number do you get?',[
 ('LOOK AT THE PARTS','Forty-three has four tens and three ones','43 = 4 tens + 3 ones',
 'Forty-three has four tens and three ones.'),
 ('ADD A TEN','Only the number of tens changes','4 tens + 1 ten = 5 tens',
 'Add one more ten. Four tens become five tens.'),
 ('KEEP THE ONES','No extra ones were added','5 tens + 3 ones = 53',
 'The three ones stay the same. Five tens and three ones make fifty-three.'),
 ('CHECK THE CHANGE','One ten is ten ones','43 + 10 = 53',
 'Check that the total increased by ten. Forty-three plus ten is fifty-three.')],g(4,9),'43+10','53')
add('place-remove-extra-ones','Take away the extra ones to leave full tens',
 'There are 73 counters. Take away 3.\nHow many counters remain?','70',
 'There are seventy-three counters. Take away three. How many remain?',[
 ('SPLIT TENS AND ONES','Keep the seven full tens together','73 = 70 + 3',
 'Seventy-three is seven full tens and three extra ones.'),
 ('TAKE AWAY THE ONES','Remove the three extra counters','3 − 3 = 0 ones',
 'Take away the three extra counters. No extra ones are left.'),
 ('KEEP THE FULL TENS','No full ten was removed','7 tens = 70',
 'All seven full tens remain. Seven tens make seventy.'),
 ('WRITE AND CHECK','Adding the removed ones brings the total back','73 − 3 = 70\n70 + 3 = 73',
 'Seventy-three minus three is seventy. Add the three back to check.')],g(4,8),'73-3','70')
add('order-number-line-direction','Use a number line to compare whole numbers',
 'On a number line, which is greater: 6 or 9?','9',
 'On a number line, which number is greater, six or nine?',[
 ('LOOK AT THE LINE','The numbers get bigger to the right','5, 6, 7, 8, 9, 10',
 'On this number line, the numbers get bigger as you move to the right.'),
 ('FIND BOTH NUMBERS','Nine is to the right of six','6 < 9',
 'Nine is to the right of six, so nine is greater than six.'),
 ('READ THE SIGN','The open side faces the greater number','6 < 9 means six is less than nine.',
 'The open side of the comparison sign faces the greater number. Six is less than nine.'),
 ('REVERSE THE ORDER','The greater number stays the same','9 > 6',
 'If we write nine first, turn the sign around. Nine is greater than six.')],g(5,4),'9-6','3')
add('order-count-object-groups','Count groups before comparing their sizes',
 'Compare the circles, squares, and triangles.\nWhich group has the most? Which has the fewest?','Circles most; squares fewest',
 'Compare the circles, squares, and triangles. Which group has the most, and which has the fewest?',[
 ('COUNT EACH GROUP','Count each object once','Circles: 6; squares: 3; triangles: 5',
 'Count each group carefully. There are six circles, three squares, and five triangles.'),
 ('FIND THE MOST','Choose the largest count','6 is greater than 5 and 3.\nCircles have the most.',
 'Six is the largest count, so the circles have the most.'),
 ('FIND THE FEWEST','Choose the smallest count','3 is less than 5 and 6.\nSquares have the fewest.',
 'Three is the smallest count, so the squares have the fewest.'),
 ('ADD ONE TO EVERY GROUP','Equal increases keep the order the same','New counts: 7 circles, 4 squares, 6 triangles',
 'If every group gets one more object, the counts become seven, four, and six. Circles still have the most and squares the fewest.')],g(5,6),'6+1','7')
add('order-compute-both-sides','Work out both sides before choosing a comparison sign',
 'Choose <, >, or = :\n9 − 2  __  3 + 5','<',
 'Compare nine minus two with three plus five. Which sign belongs in the gap?',[
 ('WORK OUT THE LEFT SIDE','Find its total first','9 − 2 = 7',
 'Work out the left side first. Nine minus two is seven.'),
 ('WORK OUT THE RIGHT SIDE','Find this total too','3 + 5 = 8',
 'Now work out the right side. Three plus five is eight.'),
 ('COMPARE THE TOTALS','Seven is smaller than eight','7 < 8',
 'Seven is smaller than eight. Use the less-than sign.'),
 ('PUT THE SIGN IN THE ORIGINAL','The open side faces the greater total','9 − 2 < 3 + 5\nEqual totals would use =.',
 'Put that sign back in the original question. Nine minus two is less than three plus five. If both totals were equal, we would use equals.')],g(8,5),'(3+5)-(9-2)','1')

# Concrete illustrations supplement the same checked five-scene lesson structure.
def counters(d,counts,labels=None,shapes=None,y=550):
 for row,n in enumerate(counts):
  yy=y+row*110;x=780 if labels else (video.W-n*78)/2
  if labels:video.text(d,(300,yy-20),labels[row],38,video.INK,True)
  for i in range(n):
   xx=x+i*78;box=(xx-22,yy-22,xx+22,yy+22);shape=(shapes or ['circle']*len(counts))[row]
   if shape=='square':d.rectangle(box,fill=video.TEAL)
   elif shape=='triangle':d.polygon([(xx,yy-25),(xx-25,yy+22),(xx+25,yy+22)],fill=video.TEAL)
   else:d.ellipse(box,fill=video.TEAL)

def frame(d,x,y,n):
 for i in range(10):
  xx=x+(i%5)*90;yy=y+(i//5)*90
  d.rectangle((xx,yy,xx+90,yy+90),outline=video.INK,width=3)
  if i<n:d.ellipse((xx+19,yy+19,xx+71,yy+71),fill=video.TEAL)

def draw_visual(s,d,scene,p):
 vid=s['video_id'];draw_card(s,d,scene,p)
 if vid=='count-objects-one-to-one' and scene<4:
  d.rounded_rectangle((145,360,1775,840),radius=35,fill='white')
  counters(d,[5,4],y=520)
  video.centered(d,740,['Count the counters.','Start on the first counter.','First row: 1, 2, 3, 4, 5','Next row: 6, 7, 8, 9'][scene],42,video.TEAL)
 if vid=='place-teen-ten-frame' and scene<3:
  d.rounded_rectangle((145,360,1775,840),radius=35,fill='white');frame(d,390,490,10);frame(d,1050,490,8)
  video.centered(d,740,['How many dots altogether?','A full frame holds 10 dots.','10 dots and 8 more'][scene],44,video.TEAL)
 if vid=='count-ten-frames' and scene<3:
  d.rounded_rectangle((145,360,1775,840),radius=35,fill='white')
  for i in range(4):frame(d,430+(i%2)*650,395+(i//2)*210,10)
  if scene==2:video.centered(d,800,'10, 20, 30, 40',33,video.TEAL)
 if vid=='order-count-object-groups' and scene==0:
  d.rounded_rectangle((145,360,1775,840),radius=35,fill='white');counters(d,[6,3,5],['Circles','Squares','Triangles'],['circle','square','triangle'],y=465)
  video.centered(d,800,'Which group has the most? The fewest?',34,video.TEAL)
 if vid=='order-number-line-direction' and scene<3:
  d.rounded_rectangle((145,360,1775,840),radius=35,fill='white')
  y=570;d.line((340,y,1570,y),fill=video.INK,width=5);d.polygon([(1570,y),(1545,y-15),(1545,y+15)],fill=video.INK)
  for i,n in enumerate(range(5,11)):
   x=400+i*220;d.line((x,y-17,x,y+17),fill=video.INK,width=4);video.text(d,(x-22,y+40),str(n),44,video.TEAL if n in (6,9) else video.INK,True)
  video.centered(d,730,'Numbers get bigger to the right →',43,video.TEAL)

def lessons(doc):
 result=make_lessons(SPECS,doc)
 for s in SPECS:video.DRAW[s['video_id']]=lambda d,i,p,s=s:draw_visual(s,d,i,p)
 return result
