"""Original Grade 2 grouping and multi-step arithmetic examples."""
from algebra_lessons import authored
from card_lessons import make_lessons,draw_card
from number_sense_lessons import source
import generate_sample_videos as video

def g(w,q):return source(2,1,w,q)
SPECS=[]
def add(vid,title,question,answer,opening,steps,ref,expression,value,equalities=()):
 SPECS.append(authored(vid,title,question,answer,opening,steps,ref,expression=expression,value=value,equalities=equalities))

add('count-array-rows-columns','Count an array by rows or columns',
 'Count the dots in two ways:\n4 rows with 6 dots in each row.','24 dots',
 'These dots are in four rows, with six in each row. Let us count them in two ways.',[
 ('COUNT ROWS','Each row goes across','4 rows; 6 dots in each row',
 'A row goes across. There are four rows, each with six dots.'),
 ('ADD THE ROWS','Use one addend for each row','6 + 6 + 6 + 6 = 24',
 'Write six once for each row. Six plus six plus six plus six is twenty-four.'),
 ('COUNT COLUMNS','Each column goes down','6 columns; 4 dots in each column',
 'A column goes down. There are six columns, each with four dots.'),
 ('ADD THE COLUMNS','The same dots give the same total','4 + 4 + 4 + 4 + 4 + 4 = 24',
 'Adding six fours also gives twenty-four. Both ways count every dot exactly once.')],g(2,1),'4*6','24')
add('count-daily-groups-week','Count equal daily amounts for one week',
 'Mina reads 4 pages each day for one week.\nHow many pages does she read?','28 pages',
 'Mina reads four pages each day for one week. How many pages does she read?',[
 ('COUNT THE DAYS','One week has seven days','7 days',
 'One week has seven days. That means seven equal groups.'),
 ('WRITE EACH DAILY AMOUNT','Use four pages for every day','4 + 4 + 4 + 4 + 4 + 4 + 4',
 'Write four once for each of the seven days.'),
 ('ADD IN FOURS','Keep track of all seven groups','4, 8, 12, 16, 20, 24, 28',
 'Count in fours: four, eight, twelve, sixteen, twenty, twenty-four, twenty-eight.'),
 ('ANSWER WITH THE UNIT','Seven groups of four','7 × 4 = 28 pages',
 'Mina reads twenty-eight pages. Multiplication is a shorter way to write the same repeated addition.')],g(2,10),'7*4','28')
add('divide-share-small-total','Share a small total into equal groups',
 'Share 18 buttons equally among 3 trays.\nHow many buttons go on each tray?','6 buttons',
 'Share eighteen buttons equally among three trays. How many buttons go on each tray?',[
 ('MAKE THE GROUPS','Every tray must receive the same number','18 buttons; 3 trays',
 'Start with three trays. Each tray must receive the same number of buttons.'),
 ('DEAL ONE TO EACH','One round uses three buttons','After 1 round: 1 button per tray',
 'Give one button to each tray. Each round uses three buttons.'),
 ('COUNT COMPLETE ROUNDS','Six rounds use all eighteen buttons','3 + 3 + 3 + 3 + 3 + 3 = 18',
 'Six rounds use all eighteen buttons. Every tray now has six.'),
 ('CHECK THE SHARES','Add the three equal shares','6 + 6 + 6 = 18\n18 ÷ 3 = 6 buttons per tray',
 'Check: six plus six plus six equals eighteen. Each tray receives six buttons.')],g('2Rev',3),'18/3','6')
add('compare-equal-group-totals','Compare totals made from equal groups',
 'Ava has 3 packs of 7 stickers.\nNoah has 4 packs of 4 stickers. Who has more?','Ava;21 > 16',
 'Ava has three packs of seven stickers. Noah has four packs of four. Who has more stickers?',[
 ('COUNT AVA’S STICKERS','Find the first total','7 + 7 + 7 = 21',
 'Ava has seven plus seven plus seven, which is twenty-one stickers.'),
 ('COUNT NOAH’S STICKERS','Find the second total','4 + 4 + 4 + 4 = 16',
 'Noah has four plus four plus four plus four, which is sixteen stickers.'),
 ('COMPARE TOTALS','Compare stickers, not just packs','21 > 16',
 'Twenty-one is greater than sixteen, so Ava has more stickers.'),
 ('CHECK WHAT EACH PACK HOLDS','More packs need not mean more objects','Ava: fewer packs, but 5 more stickers',
 'Ava has fewer packs, but each pack holds more. Always find both totals before comparing.')],g('2Rev',4),'3*7-4*4','5', [('3*7','21'),('4*4','16')])
add('count-combine-equal-packs','Combine pack counts before counting the objects',
 'A shop sells 3 packs in the morning and 2 later.\nEach pack holds 4 erasers. How many erasers are sold?','20 erasers',
 'A shop sells three packs in the morning and two later. Each pack holds four erasers. How many erasers are sold?',[
 ('COUNT ALL THE PACKS','Combine morning and later sales','3 + 2 = 5 packs',
 'Add the pack counts first. Three plus two is five packs.'),
 ('USE THE AMOUNT PER PACK','Each of the five packs has four erasers','4 + 4 + 4 + 4 + 4',
 'Each of those five packs holds four erasers, so add five fours.'),
 ('FIND THE TOTAL','Count in fours five times','5 × 4 = 20 erasers',
 'Five groups of four is twenty. Twenty erasers were sold.'),
 ('CHECK ANOTHER WAY','Count each sale, then combine','3 × 4 = 12; 2 × 4 = 8\n12 + 8 = 20',
 'Check separately: twelve erasers in the morning and eight later. Together, they make twenty.')],g('2Rev',5),'(3+2)*4','20')
add('arithmetic-missing-small-part','Find a missing part using the whole',
 'Fill the gaps:\n13 + __ = 19\n17 − __ = 12','6;5',
 'Fill the gaps in thirteen plus something equals nineteen, and seventeen minus something equals twelve.',[
 ('NAME THE WHOLE','An addition joins two parts','Whole: 19; known part: 13',
 'In the addition, nineteen is the whole and thirteen is one known part.'),
 ('SUBTRACT THE KNOWN PART','The difference is the missing part','19 − 13 = 6\n13 + 6 = 19',
 'Subtract thirteen from nineteen to find six. Thirteen plus six checks the answer.'),
 ('COMPARE START AND FINISH','Find how much was removed','17 − 12 = 5',
 'In the subtraction, we start with seventeen and finish with twelve. The difference, five, was removed.'),
 ('CHECK THE ORIGINAL SENTENCE','Put the number back in the gap','17 − 5 = 12',
 'Put five into the gap. Seventeen minus five is twelve. Both missing parts now check.')],g(4,4),'19-13','6',[('17-12','5')])
add('add-find-third-part-two-stages','Find a missing third part after a clue',
 'Three numbers total 18. The first is 5.\nThe second is 1 more than 6. Find the third.','6',
 'Three numbers total eighteen. The first is five. The second is one more than six. Find the third number.',[
 ('SOLVE THE CLUE','Find the second number first','6 + 1 = 7',
 'One more than six is seven, so the second number is seven.'),
 ('ADD THE KNOWN PARTS','Combine the first two numbers','5 + 7 = 12',
 'The first two numbers total five plus seven, which is twelve.'),
 ('FIND WHAT IS LEFT','Subtract the known total from the whole','18 − 12 = 6',
 'Subtract twelve from eighteen. Six is left for the third number.'),
 ('CHECK ALL THREE','Their sum must match the given total','5 + 7 + 6 = 18',
 'Check all three: five plus seven plus six equals eighteen. The third number is six.')],g('1Rev',2),'18-(5+6+1)','6')
add('subtract-small-chain','Subtract several small amounts in order',
 'A jar has 27 beads. Remove 6, then 3, then 4.\nHow many beads remain?','14 beads',
 'A jar has twenty-seven beads. Remove six, then three, then four. How many beads remain?',[
 ('FIRST CHANGE','Start with twenty-seven','27 − 6 = 21',
 'Start with twenty-seven. Remove six to leave twenty-one.'),
 ('SECOND CHANGE','Use the new amount','21 − 3 = 18',
 'Now use twenty-one. Remove three more to leave eighteen.'),
 ('THIRD CHANGE','Keep following the story','18 − 4 = 14',
 'Remove the last four from eighteen. Fourteen beads remain.'),
 ('CHECK TOTAL REMOVED','Combine the removals for a check','6 + 3 + 4 = 13\n27 − 13 = 14',
 'In all, thirteen beads were removed. Twenty-seven minus thirteen is fourteen, which checks our answer.')],g(3,4),'27-6-3-4','14')
add('arithmetic-small-story-changes','Follow increases and decreases in a story',
 'A box has 19 pencils. Remove 5, add 8,\nthen remove 4. How many are in the box?','18 pencils',
 'A box has nineteen pencils. Remove five, add eight, then remove four. How many pencils are in the box?',[
 ('READ THE FIRST CHANGE','Removing means subtract','19 − 5 = 14',
 'Removing five means subtract five. Fourteen pencils remain.'),
 ('READ THE SECOND CHANGE','Adding more means add','14 + 8 = 22',
 'Eight more pencils go into the box. Fourteen plus eight is twenty-two.'),
 ('READ THE LAST CHANGE','Use the latest total','22 − 4 = 18',
 'Remove four from the latest total, twenty-two. That leaves eighteen.'),
 ('CHECK THE DIRECTION','One fewer pencil overall','9 removed; 8 added\n19 − 1 = 18 pencils',
 'Nine pencils were removed and eight added. That is one fewer overall, so eighteen is correct.')],g(4,10),'19-5+8-4','18')
add('arithmetic-work-backwards-small','Find a starting amount by working backwards',
 'Remove 5 counters, add 8, then remove 2.\nThe final count is 17. What was the starting count?','16 counters',
 'Remove five counters, add eight, then remove two. Seventeen remain. What was the starting count?',[
 ('UNDO THE LAST CHANGE','Work backwards from the final count','17 + 2 = 19',
 'Start at seventeen and undo the last change. Put back two to get nineteen.'),
 ('UNDO THE MIDDLE CHANGE','Reverse adding eight','19 − 8 = 11',
 'Before eight were added, there were nineteen minus eight, or eleven counters.'),
 ('UNDO THE FIRST CHANGE','Reverse removing five','11 + 5 = 16',
 'Put back the first five removed. The starting count was sixteen.'),
 ('CHECK FORWARDS','Follow the original story','16 − 5 + 8 − 2 = 17',
 'Check forwards: sixteen, then eleven, then nineteen, then seventeen. The starting count is sixteen.')],g('4Rev',5),'17+2-8+5','16')

def draw_array(s,d,scene,p):
 if scene==4:return draw_card(s,d,scene,p)
 d.rounded_rectangle((145,360,1775,850),radius=35,fill='white')
 for r in range(4):
  for c in range(6):
   x,y=645+c*125,435+r*94
   d.ellipse((x-22,y-22,x+22,y+22),fill=video.TEAL)
 if scene in (1,2):
  for r in range(4):d.rounded_rectangle((590,399+r*94,1325,471+r*94),radius=16,outline=video.INK,width=3)
 if scene==3:
  for c in range(6):d.rounded_rectangle((607+c*125,396,683+c*125,755),radius=16,outline=video.INK,width=3)
 labels=['4 rows with 6 dots each','4 rows; 6 dots in each','6 + 6 + 6 + 6 = 24','6 columns; 4 dots in each']
 video.centered(d,792,labels[scene],40,video.INK,True)

def lessons(doc):
 result=make_lessons(SPECS,doc)
 s=SPECS[0]
 video.DRAW[s['video_id']]=lambda d,scene,p:draw_array(s,d,scene,p)
 return result
