"""Concrete Grade 1 arithmetic and place-value methods with fresh examples."""
from algebra_lessons import authored
from card_lessons import make_lessons,draw_card
from number_sense_lessons import source
import generate_sample_videos as video

def g(w,q):return source(1,2,w,q)
SPECS=[]
def add(vid,title,question,answer,opening,steps,ref,expression,value):
 SPECS.append(authored(vid,title,question,answer,opening,steps,ref,expression=expression,value=value))

add('add-count-on-small','Add by counting on from the first group',
 'There are 6 counters. Add 2 more.\nHow many counters are there now?','8',
 'There are six counters. Add two more. How many are there now?',[
 ('START WITH THE FIRST GROUP','Keep the six you already have','Start with 6.',
 'We already have six. We can start counting from six.'),
 ('ADD THE FIRST NEW COUNTER','One more makes seven','6 + 1 = 7',
 'Add one new counter. The total becomes seven.'),
 ('ADD THE SECOND NEW COUNTER','One more makes eight','7 + 1 = 8',
 'Add the second new counter. Now there are eight.'),
 ('WRITE THE ADDITION','Addition joins the groups','6 + 2 = 8',
 'Six and two more make eight. Addition joins the two groups into one total.')],g(1,1),'6+2','8')
add('subtract-take-away-small','Subtract by taking objects away',
 'There are 9 counters. Take away 4.\nHow many remain?','5',
 'Nine counters are on the table. Take away four. How many remain?',[
 ('START WITH THE WHOLE','There are nine before anything is removed','Start with 9 counters.',
 'Nine is the starting amount.'),
 ('REMOVE FOUR','Count only the counters being taken away','Take away 4 counters.',
 'Cross out four counters. Those are the ones being taken away.'),
 ('COUNT WHAT REMAINS','Do not count the crossed-out counters','5 counters remain.',
 'Count the counters that are left. There are five.'),
 ('WRITE THE SUBTRACTION','Taking away makes this group smaller','9 − 4 = 5',
 'Nine minus four is five. Taking objects away is subtraction.')],g(1,2),'9-4','5')
add('add-subtract-fact-family','Use the same two parts and whole in four facts',
 'The parts are 3 and 8; the whole is 11.\nWrite two additions and two subtractions.','3+8=11;8+3=11;11-3=8;11-8=3',
 'The parts are three and eight, and the whole is eleven. Let us write two additions and two subtractions.',[
 ('JOIN THE PARTS','Both parts together make the whole','3 + 8 = 11',
 'Joining three and eight makes eleven.'),
 ('SWAP THE PARTS','The whole stays the same','8 + 3 = 11',
 'Swap the parts. Eight plus three still makes eleven.'),
 ('REMOVE THE FIRST PART','Start from the whole','11 − 3 = 8',
 'Start with eleven and remove three. The other part, eight, remains.'),
 ('REMOVE THE OTHER PART','Each subtraction starts from the whole','11 − 8 = 3',
 'Start with eleven and remove eight. Three remains. These four facts use the same two parts and whole.')],g(2,1),'3+8','11')
add('add-swap-parts','Swap the order of two addends',
 'You know 6 + 9 = 15.\nWhat is 9 + 6?','15',
 'You know six plus nine is fifteen. What is nine plus six?',[
 ('NOTICE THE SAME PARTS','Both additions use six and nine','6 + 9 and 9 + 6',
 'Both additions use exactly the same two parts: six and nine.'),
 ('SWAP THE GROUPS','Moving a group does not add or remove objects','6 + 9 = 9 + 6',
 'Switching the groups does not add or remove any objects.'),
 ('KEEP THE TOTAL','The total is still fifteen','9 + 6 = 15',
 'The total stays fifteen, so nine plus six is fifteen.'),
 ('USE THE KNOWN FACT','For addition, either order gives the same total','6 + 9 = 15\n9 + 6 = 15',
 'Knowing one addition helps you know the other. Swapping the two addends keeps the total the same.')],g(2,3),'9+6','15')
add('add-balance-equation','Find a missing addend on the other side of equals',
 'Fill the gap: 4 + 8 = 7 + __.','5',
 'Fill the gap: four plus eight equals seven plus what?',[
 ('FIND THE KNOWN TOTAL','Both sides must have the same value','4 + 8 = 12',
 'First work out the side with no missing number. Four plus eight is twelve.'),
 ('READ THE NEW QUESTION','Seven and how many more make twelve?','7 + __ = 12',
 'The other side must also make twelve. It already has seven.'),
 ('FIND THE MISSING PART','Count up from seven to twelve','8, 9, 10, 11, 12: five more\n12 − 7 = 5',
 'Count up from seven to twelve. That takes five more, so the missing number is five.'),
 ('CHECK BOTH SIDES','Both totals are twelve','4 + 8 = 7 + 5\n12 = 12',
 'Put five back into the equation. Both sides equal twelve, so the equation balances.')],g(2,4),'4+8-7','5')
add('add-parts-to-target','Find all two-part ways to make a small total',
 'Use two whole-number parts, allowing zero, to make 7.\nList the pairs, counting reversed orders separately.','0+7,1+6,2+5,3+4,4+3,5+2,6+1,7+0',
 'Make seven using two whole-number parts. Zero is allowed, and we will list reversed orders separately.',[
 ('START WITH ZERO','Zero and seven make seven','0 + 7 = 7',
 'Start with zero in the first part. The second part must be seven.'),
 ('MOVE ONE BETWEEN THE PARTS','The total stays seven','1 + 6; 2 + 5; 3 + 4',
 'Add one to the first part and take one from the second. We get one and six, two and five, three and four.'),
 ('KEEP GOING TO ZERO','Stop when the second part reaches zero','4 + 3; 5 + 2; 6 + 1; 7 + 0',
 'Continue with four and three, five and two, six and one, seven and zero.'),
 ('CHECK EVERY PAIR','Every pair adds to the target','8 ordered pairs; each total is 7.',
 'There are eight ordered pairs. Every pair totals seven. A missing part is whatever brings the known part up to seven.')],g(3,1),'7+1','8')
add('add-bridge-ten-early','Make ten when adding two small numbers',
 'Use a ten to work out 7 + 5.','12',
 'Let us use a ten to work out seven plus five.',[
 ('FILL THE TEN','Seven needs three more to reach ten','7 + 3 = 10',
 'Seven needs three more to make ten.'),
 ('SPLIT THE FIVE','Use three now and keep two for later','5 = 3 + 2',
 'Split the five into three and two. Use the three to fill the ten.'),
 ('ADD THE LEFTOVER ONES','The two extra ones still count','7 + 5 = 10 + 2',
 'We now have a full ten and two extra ones.'),
 ('SAY THE TOTAL','One ten and two ones make twelve','10 + 2 = 12',
 'Ten plus two is twelve, so seven plus five is twelve.')],g(4,2),'7+5','12')
add('add-three-using-ten','Add three small numbers by making a ten',
 'Find 6 + 8 + 5.','19',
 'Find six plus eight plus five. We can make a ten first.',[
 ('MAKE A TEN','Six needs four from the eight','8 = 4 + 4\n6 + 4 = 10',
 'Six needs four to make ten. Split eight into four and four.'),
 ('KEEP THE LEFTOVERS','Four from the eight is still unused','6 + 8 + 5 = 10 + 4 + 5',
 'After making ten, we still have four and five to add.'),
 ('ADD THE OTHER PARTS','Four and five make nine','4 + 5 = 9',
 'Four plus five is nine.'),
 ('COMBINE WITH THE TEN','Every original part has been counted','10 + 9 = 19',
 'Ten and nine make nineteen. We used all six, all eight, and all five.')],g(4,6),'6+8+5','19')
add('add-make-next-ten','Add by reaching the next ten first',
 'Use the next ten to find 56 + 7.','63',
 'Use the next ten to find fifty-six plus seven.',[
 ('FIND THE NEXT TEN','The next full ten after fifty-six is sixty','56 + 4 = 60',
 'The next full ten is sixty. Fifty-six needs four to get there.'),
 ('SPLIT THE SEVEN','Keep track of what remains after using four','7 = 4 + 3',
 'Split seven into four and three.'),
 ('REACH THE TEN','Add the first part','56 + 7 = 56 + 4 + 3\n= 60 + 3',
 'Add four to reach sixty. Then the remaining three still need to be added.'),
 ('ADD THE REST','Sixty and three make sixty-three','60 + 3 = 63',
 'Sixty plus three is sixty-three. The answer is sixty-three.')],g(14,1),'56+7','63')
add('place-compare-digit-counts','Compare the numbers of tens and ones',
 'Compare 72 and 27.\nWhich has more tens? Which has more ones?','72 has more tens;27 has more ones',
 'Compare seventy-two and twenty-seven. Which has more tens, and which has more ones?',[
 ('READ THE FIRST NUMBER','The left digit counts tens; the right counts ones','72 = 7 tens + 2 ones',
 'Seventy-two has seven tens and two ones.'),
 ('READ THE SECOND NUMBER','Keep the place names attached to the digits','27 = 2 tens + 7 ones',
 'Twenty-seven has two tens and seven ones.'),
 ('COMPARE THE TENS','Seven tens is more than two tens','72 has more tens.',
 'Seven tens is more than two tens, so seventy-two has more tens.'),
 ('COMPARE THE ONES','Seven ones is more than two ones','27 has more ones.',
 'Twenty-seven has more ones: seven ones compared with two. Compare the place the question asks about.')],g(7,5),'7-2','5')
add('place-change-three-digit-units','Add or subtract ones, tens, and hundreds',
 'Start with 426. Find 1 more, 10 more,\n100 more, and 10 less.','427;436;526;416',
 'Start with four hundred twenty-six. Find one more, ten more, one hundred more, and ten less.',[
 ('CHANGE THE ONES','Add one to the six ones','426 + 1 = 427',
 'One more changes the six ones to seven ones. The result is four hundred twenty-seven.'),
 ('CHANGE THE TENS','Add one ten to the two tens','426 + 10 = 436',
 'Ten more changes the two tens to three tens, giving four hundred thirty-six.'),
 ('CHANGE THE HUNDREDS','Add one hundred to the four hundreds','426 + 100 = 526',
 'One hundred more changes four hundreds to five hundreds. The answer is five hundred twenty-six.'),
 ('TAKE AWAY A TEN','Remove one ten from the original number','426 − 10 = 416',
 'Ten less removes one ten from the original number. Four hundred twenty-six becomes four hundred sixteen.')],g(10,4),'426-10','416')
add('count-hundreds-pattern','Fill a counting pattern with steps of one hundred',
 'Fill the gap: 140, 240, __, 440, 540.','340',
 'Fill the missing number: one hundred forty, two hundred forty, a gap, four hundred forty, five hundred forty.',[
 ('COMPARE NEIGHBOURS','The step is one hundred','240 − 140 = 100',
 'The first step adds one hundred.'),
 ('KEEP THE SAME STEP','Add one hundred to the number before the gap','240 + 100 = 340',
 'Add one hundred to two hundred forty. We get three hundred forty.'),
 ('CHECK THE NEXT NUMBER','Another hundred reaches four hundred forty','340 + 100 = 440',
 'Three hundred forty plus one hundred is four hundred forty, matching the next number.'),
 ('READ THE PATTERN','The tens and ones stay the same','140, 240, 340, 440, 540',
 'The missing number is three hundred forty. In this pattern, the hundreds increase and the last two digits stay the same.')],g(10,6),'240+100','340')
add('arithmetic-follow-changes','Follow several additions and subtractions in order',
 'Start at 352. Add 4, subtract 10,\nthen add 100. Where do you finish?','446',
 'Start at three hundred fifty-two. Add four, subtract ten, then add one hundred. Where do you finish?',[
 ('DO THE FIRST CHANGE','Carry the new total into the next step','352 + 4 = 356',
 'First add four. Three hundred fifty-two becomes three hundred fifty-six.'),
 ('DO THE SECOND CHANGE','Subtract from the new total','356 − 10 = 346',
 'Now subtract ten from that new total. We have three hundred forty-six.'),
 ('DO THE THIRD CHANGE','Add one hundred to the current total','346 + 100 = 446',
 'Add one hundred. The final total is four hundred forty-six.'),
 ('CHECK THE ORDER','Each operation uses the previous result','352 → 356 → 346 → 446',
 'Check the path in order. Each change starts where the previous one ended.')],g(10,10),'352+4-10+100','446')
add('subtract-missing-part-whole','Find a missing removed amount or starting amount',
 'Fill the gaps: 75 − __ = 42\nand __ − 18 = 36.','33;54',
 'Fill two gaps: seventy-five minus what equals forty-two? And what minus eighteen equals thirty-six?',[
 ('FIND THE REMOVED PART','Subtract what remains from the starting whole','75 − 42 = 33',
 'In the first question, seventy-five is the whole and forty-two remains. Their difference is the removed amount, thirty-three.'),
 ('CHECK THE FIRST GAP','Put the removed amount back into the question','75 − 33 = 42',
 'Seventy-five minus thirty-three is forty-two, so the first gap is correct.'),
 ('FIND THE STARTING WHOLE','Add the removed part and the remaining part','18 + 36 = 54',
 'In the second question, we need the starting whole. Add the eighteen removed and the thirty-six remaining to get fifty-four.'),
 ('CHECK THE SECOND GAP','The whole must be large enough for both parts','54 − 18 = 36',
 'Fifty-four minus eighteen is thirty-six. The missing starting amount is fifty-four.')],g(13,4),'75-42','33')
add('add-regroup-ones-early','Exchange ten ones for a ten when adding',
 'Add 16 + 7. Show the regrouping.','23',
 'Add sixteen and seven. Let us show how regrouping works.',[
 ('SPLIT THE FIRST NUMBER','Sixteen is one ten and six ones','16 = 1 ten + 6 ones',
 'Sixteen has one ten and six ones.'),
 ('ADD THE ONES','The original ten is still there','6 ones + 7 ones = 13 ones\n1 ten + 13 ones',
 'Six ones plus seven ones make thirteen ones. Keep the original ten too.'),
 ('EXCHANGE TEN ONES','Ten of the thirteen ones become another ten','13 ones = 1 ten + 3 ones\n1 ten + 1 ten + 3 ones',
 'Exchange ten of the thirteen ones for another ten. Three ones remain.'),
 ('READ THE TOTAL','Two tens and three ones make twenty-three','16 + 7 = 23',
 'Now we have two tens and three ones, which make twenty-three.')],g(15,6),'16+7','23')
add('add-missing-part-many','Find one missing part when several known parts are given',
 'Fill the gap: 20 + __ + 4 + 2 = 66.','40',
 'Find the missing part: twenty plus a gap plus four plus two equals sixty-six.',[
 ('COMBINE THE KNOWN PARTS','Find how much is already included','20 + 4 + 2 = 26',
 'Add the known parts first. Twenty, four, and two make twenty-six.'),
 ('KEEP THE SAME TOTAL','The missing part must complete sixty-six','26 + __ = 66',
 'We already have twenty-six. The missing part must bring that up to sixty-six.'),
 ('FIND THE DIFFERENCE','Subtract the known amount from the total','66 − 26 = 40',
 'Sixty-six minus twenty-six is forty, so forty is missing.'),
 ('CHECK IN THE ORIGINAL','Use all the parts, including the missing one','20 + 40 + 4 + 2 = 66',
 'Put forty in the original gap. Twenty plus forty plus four plus two is sixty-six. It checks.')],g(12,9),'66-20-4-2','40')

add('place-cross-hundred-ten','Add or subtract a ten across one hundred',
 'Find 94 + 10. Then take 10 away again.','104;94',
 'Find ninety-four plus ten. Then take ten away again.',[
 ('LOOK AT THE TENS','Ninety-four has nine tens and four ones','94 = 9 tens + 4 ones',
 'Ninety-four has nine tens and four ones.'),
 ('ADD ONE TEN','Ten tens make one hundred','9 tens + 1 ten = 10 tens = 100',
 'Add one ten. We now have ten tens, which make one hundred.'),
 ('KEEP THE FOUR ONES','Use zero to show there are no extra tens','100 + 4 = 104',
 'Keep the four ones. The total is one hundred four. Its tens digit is zero.'),
 ('UNDO THE ADDITION','Taking away a ten brings the original amount back','104 − 10 = 94',
 'Take away a ten again. One hundred becomes nine tens, and the four ones stay. We return to ninety-four.')],g(9,7),'94+10','104')

def draw_visual(s,d,scene,p):
 draw_card(s,d,scene,p)
 vid=s['video_id']
 if vid in ('add-count-on-small','subtract-take-away-small') and scene<4:
  d.rounded_rectangle((145,360,1775,840),radius=35,fill='white')
  if vid=='add-count-on-small':
   count=6 if scene==1 else 7 if scene==2 else 8
   for i in range(count):
    x=560+i*115;d.ellipse((x-35,525,x+35,595),fill=video.TEAL if i<6 else '#DC8B34')
   video.centered(d,715,['6 counters and 2 more','Start with 6.','One more: 7','Two more: 8'][scene],48,video.TEAL)
  else:
   for i in range(9):
    x=500+i*115;d.ellipse((x-33,525,x+33,591),fill=video.TEAL)
    if scene>=2 and i>=5:
     d.line((x-42,515,x+42,601),fill='#BD453C',width=8);d.line((x+42,515,x-42,601),fill='#BD453C',width=8)
   video.centered(d,715,['Take 4 away from 9.','Start with 9.','Cross out 4.','5 counters remain.'][scene],48,video.TEAL)

def lessons(doc):
 assert [(a,7-a) for a in range(8)]==[(0,7),(1,6),(2,5),(3,4),(4,3),(5,2),(6,1),(7,0)]
 assert 54-18==36 and 75-33==42 and 16+7==23
 result=make_lessons(SPECS,doc)
 for s in SPECS:video.DRAW[s['video_id']]=lambda d,i,p,s=s:draw_visual(s,d,i,p)
 return result
