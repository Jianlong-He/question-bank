"""Grade 1 diagrams, data, clocks, calendars, and equal parts."""
import math,calendar
from algebra_lessons import authored
from card_lessons import make_lessons,draw_card
from number_sense_lessons import source
import generate_sample_videos as video

def g(w,q):return source(1,3,w,q)
SPECS=[]
def add(vid,title,question,answer,opening,steps,ref,expression,value):
 SPECS.append(authored(vid,title,question,answer,opening,steps,ref,expression=expression,value=value))

add('measure-touching-unit-blocks','Measure length with equal touching blocks',
 'How long is the ribbon in equal blocks?','9 blocks',
 'How long is this ribbon? We will measure it with equal blocks.',[
 ('LINE UP THE START','Start the first block at the end of the ribbon','Start at the same place.',
 'Line up the first block with the start of the ribbon.'),
 ('LEAVE NO GAPS','Equal blocks touch without overlapping','All blocks are the same size.',
 'Use blocks of the same size. Let them touch without gaps or overlaps.'),
 ('COUNT ALL THE BLOCKS','Count each unit exactly once','1, 2, 3, 4, 5, 6, 7, 8, 9',
 'Count each block once. There are nine equal blocks from one end of the ribbon to the other.'),
 ('INCLUDE THE UNIT','A measurement says how many and what unit','The ribbon is 9 blocks long.',
 'The ribbon is nine blocks long. Include the word blocks so the measurement has a unit.')],g(1,1),'5+4','9')
add('measure-compare-unit-heights','Compare and order heights measured in equal units',
 'Towers P, Q, R are 4, 9, and 7 blocks tall.\nOrder them from shortest to tallest.\nHow much taller is Q than R?','P,R,Q;2 blocks',
 'Three towers are four, nine, and seven equal blocks tall. Order them from shortest to tallest, then compare the tallest two.',[
 ('USE THE SAME UNIT','Every block has the same height','P: 4 blocks; Q: 9 blocks; R: 7 blocks',
 'The blocks all have the same height, so we can compare the counts.'),
 ('FIND SHORTEST AND TALLEST','A greater block count means a taller tower','4 < 7 < 9',
 'Four is smallest, then seven, then nine.'),
 ('NAME THE TOWERS IN ORDER','Match each count back to its label','Shortest to tallest: P, R, Q',
 'Match the numbers to the labels. The order is P, R, Q.'),
 ('FIND HOW MUCH TALLER','Subtract the two heights','9 − 7 = 2 blocks',
 'Q is nine blocks high and R is seven. Their difference is two blocks.')],g(1,3),'9-7','2')
add('data-read-small-bar-chart','Read values and compare bars on a small chart',
 'Read the favourite-fruit chart.\nHow many chose pears? Which fruit has the most votes?\nHow many fruits have more than 6 votes?','9;pears;1',
 'Read the favourite-fruit chart. How many chose pears, which fruit has the most votes, and how many fruits have more than six votes?',[
 ('READ THE SCALE','Numbered lines go up in twos','0, 2, 4, 6, 8, 10',
 'First read the scale. The numbered lines go up by two. Halfway between eight and ten is nine.'),
 ('FOLLOW THE PEAR BAR','Read the height at the top of the bar','Pears: 9 votes',
 'The pear bar ends halfway between eight and ten. Nine children chose pears.'),
 ('COMPARE BAR HEIGHTS','The tallest bar has the most votes','Pears have the most: 9 votes.',
 'Pears have the tallest bar, so pears have the most votes.'),
 ('COUNT BARS ABOVE THE LIMIT','More than six does not include six','Only pears have more than 6 votes: 1 fruit.',
 'Only the pear bar goes above six. A bar ending at six does not count as more than six. The answer is one fruit.')],g(2,1),'8+1','9')
add('data-combine-compare-chart-values','Use chart values for totals and differences',
 'Use the fruit chart. Compare pears and plums,\nadd apples and plums, and find two equal counts.','5 more;10 total;apples and peaches equal',
 'Use the fruit chart to find a difference, a total, and two equal counts.',[
 ('READ THE COUNTS','Check the scale before calculating','Apples 6; pears 9; plums 4; peaches 6',
 'Read the bars: six for apples, nine for pears, four for plums, and six for peaches.'),
 ('FIND HOW MANY MORE','Subtract the smaller count from the larger','9 − 4 = 5 more pear votes',
 'For how many more pears than plums, subtract four from nine. There are five more pear votes.'),
 ('FIND THE COMBINED TOTAL','Together means add the two counts','6 + 4 = 10 apple-or-plum votes',
 'For apples and plums together, add six and four. The total is ten votes.'),
 ('LOOK FOR EQUAL HEIGHTS','Equal bars mean equal counts','Apples and peaches: 6 = 6',
 'Apples and peaches both have six votes. Their bars have the same height.')],g(2,5),'9-4','5')
add('time-read-analogue-early','Read the hour and minutes on an analogue clock',
 'What time does this clock show?','3:40',
 'What time does this clock show? Let us read the two hands.',[
 ('FIND THE SHORT HAND','The short hand tells the hour','It has passed 3 but has not reached 4.',
 'The short hand tells the hour. It has passed three but has not reached four, so the hour is three.'),
 ('FIND THE LONG HAND','The long hand tells the minutes','The long hand points to 8.',
 'The longer hand tells the minutes. It points to eight.'),
 ('COUNT MINUTES BY FIVES','Each numbered step is five minutes','5, 10, 15, 20, 25, 30, 35, 40',
 'Count around from twelve in fives. At eight, we reach forty minutes.'),
 ('PUT HOUR AND MINUTES TOGETHER','Write the hour first','3:40 — forty minutes past three',
 'Write the hour first, then the minutes. The time is three forty, or forty minutes past three.')],g(3,12),'8*5','40')
add('time-read-oclock-early','Read an exact hour and understand a full hour',
 'The short hand points to 9 and the long hand to 12.\nWhat time does the clock show?','9:00',
 'The short hand points to nine and the long hand to twelve. What time does the clock show?',[
 ('READ THE HOUR','The short hand points directly to nine','Hour: 9',
 'The short hand points to nine, so the hour is nine.'),
 ('READ ZERO MINUTES','At twelve, the minute count starts again','Minutes: 00',
 'The long hand at twelve means zero minutes past the hour.'),
 ('WRITE THE TIME','Use two zeros after the colon','9:00 — nine o’clock',
 'Write nine, then a colon and two zeros. We say nine o’clock.'),
 ('FOLLOW ONE FULL TURN','Sixty minutes make one hour','12 steps of 5 minutes = 60 minutes\n1 hour later: 10:00',
 'One full turn of the long hand takes sixty minutes, which is one hour. The next exact hour is ten o’clock.')],g(3,11),'12*5','60')
add('time-digital-minutes-past','Read minutes past the hour in a digital time',
 'At 8:17, how many minutes have passed since eight?','17 minutes',
 'At eight seventeen, how many minutes have passed since eight?',[
 ('FIND THE COLON','It separates the hour from the minutes','8 : 17',
 'The colon separates the two parts of the time.'),
 ('READ THE LEFT PART','The number before the colon is the hour','Hour: 8',
 'The number before the colon tells the hour. Here it is eight.'),
 ('READ THE RIGHT PART','The number after the colon counts minutes past','Minutes past: 17',
 'The number after the colon tells the minutes past that hour. Here it is seventeen.'),
 ('ANSWER IN MINUTES','Include the unit in your answer','17 minutes past eight',
 'Seventeen minutes have passed since eight. Say seventeen minutes, because the question asks for elapsed minutes.')],g(3,7),'8*60+17-8*60','17')
add('calendar-neighbouring-weekdays','Find yesterday and tomorrow in weekday order',
 'Today is Wednesday.\nWhat day was yesterday? What day is tomorrow?','Tuesday;Thursday',
 'Today is Wednesday. What day was yesterday, and what day is tomorrow?',[
 ('READ THE DAYS IN ORDER','The week repeats after Sunday','Monday, Tuesday, Wednesday, Thursday\nFriday, Saturday, Sunday',
 'The days follow the same order each week: Monday through Sunday, then Monday again.'),
 ('GO BACK ONE DAY','Yesterday is immediately before today','Tuesday → Wednesday',
 'The day just before Wednesday is Tuesday. Yesterday was Tuesday.'),
 ('GO FORWARD ONE DAY','Tomorrow is immediately after today','Wednesday → Thursday',
 'The day just after Wednesday is Thursday. Tomorrow is Thursday.'),
 ('USE THE SAME ORDER ON A CALENDAR','Each following date moves forward one weekday','Tuesday, Wednesday, Thursday',
 'Neighbouring calendar dates move along this same order. Before means back one day, and after means forward one day.')],g(4,1),'2-1','1')
add('calendar-season-cycle','Follow the repeating order of four seasons',
 'What season comes after winter?\nWhat season comes before fall?','Spring;summer',
 'What season comes after winter? And what season comes before fall?',[
 ('NAME THE ORDER','The four seasons form a repeating cycle','Spring → Summer → Fall → Winter',
 'The order is spring, summer, fall, winter. Fall is also called autumn.'),
 ('CONTINUE AFTER WINTER','The cycle returns to the beginning','Winter → Spring',
 'After winter, the cycle returns to spring.'),
 ('LOOK BEFORE FALL','Find the previous season in the cycle','Summer → Fall',
 'The season just before fall is summer.'),
 ('CHECK BOTH ANSWERS','Before and after point in different directions','After winter: spring\nBefore fall: summer',
 'Check the direction asked for. After winter is spring; before fall is summer.')],g(4,4),'4-1','3')
add('calendar-neighbouring-months','Find the month immediately before or after another',
 'Which months come immediately before and after June?','May;July',
 'Which months come immediately before and after June?',[
 ('READ THE MONTH ORDER','Use the calendar sequence','April → May → June → July → August',
 'Read this part of the year: April, May, June, July, August.'),
 ('LOOK BEFORE JUNE','Move back one place','May comes before June.',
 'Move back one place from June. The previous month is May.'),
 ('LOOK AFTER JUNE','Move forward one place','July comes after June.',
 'Move forward one place from June. The next month is July.'),
 ('KEEP THE FULL YEAR IN MIND','The year repeats after December','12 months: January through December\nAfter December comes January.',
 'There are twelve months in order, January through December. After December, a new year starts with January.')],g(4,6),'6-1','5')
add('calendar-weeks-plus-days','Convert weeks and extra days into days',
 'A trip lasts 3 weeks and 2 days.\nHow many days is that?','23 days',
 'A trip lasts three weeks and two days. How many days is that altogether?',[
 ('USE SEVEN DAYS PER WEEK','Each full week has the same length','1 week = 7 days',
 'One week has seven days.'),
 ('COUNT THREE WEEKS','Add seven for every week','7 + 7 + 7 = 21 days',
 'Three weeks give seven plus seven plus seven, which is twenty-one days.'),
 ('ADD THE EXTRA DAYS','The two days are in addition to the full weeks','21 + 2 = 23',
 'Add the two extra days to twenty-one. We get twenty-three.'),
 ('INCLUDE THE UNIT','Everything is now measured in days','3 weeks and 2 days = 23 days',
 'The trip lasts twenty-three days. Convert the full weeks first, then add the extra days.')],g(4,10),'3*7+2','23')
add('calendar-month-lengths','Compare month lengths in a common year',
 'In a common year, how many more days\ndoes January have than February?','3 days',
 'In a common year, how many more days does January have than February?',[
 ('READ JANUARY','January has thirty-one days','January: 31 days',
 'January has thirty-one days.'),
 ('READ FEBRUARY','A common year is not a leap year','February: 28 days',
 'February has twenty-eight days in a common year. In a leap year it has twenty-nine.'),
 ('COMPARE THE COUNTS','How many more means find the difference','31 − 28 = 3 days',
 'Subtract twenty-eight from thirty-one. January has three more days.'),
 ('REMEMBER MONTHS VARY','Other months have thirty or thirty-one days','February is the shortest month.\nA month is not always four weeks.',
 'The other months have thirty or thirty-one days, so February is shortest. A month is not always four weeks.')],g(4,11),'31-28','3')
add('shape-round-and-straight','Recognize curved shapes and straight-sided shapes',
 'Which drawing has straight sides and corners:\nthe oval or the pentagon?','Pentagon',
 'Which drawing has straight sides and corners, the oval or the pentagon?',[
 ('TRACE THE OVAL','A smooth curved outline has no corners','Oval: curved outline; no straight sides',
 'The oval has one smooth curved outline, with no straight sides or corners.'),
 ('TRACE THE PENTAGON','Its outline turns at five corners','Pentagon: 5 straight sides and 5 corners',
 'The pentagon has five straight sides meeting at five corners.'),
 ('COMPARE ROUND SHAPES','A circle is equally wide in every direction','Circle: round\nThis oval: longer in one direction',
 'A circle is equally wide in every direction. This oval is longer in one direction.'),
 ('ANSWER USING THE FEATURES','Look at the outline, not the colour','The pentagon has straight sides and corners.',
 'The pentagon is the drawing with straight sides and corners. Use the outline to recognize the shape.')],g(6,3),'1+1+1+1+1','5')
add('shape-square-properties-early','Recognize a square even when it is turned',
 'One drawing has four equal sides and four square corners.\nAnother has two long sides and two short sides.\nWhich drawing is a square?','The first drawing',
 'One drawing has four equal sides and four square corners. Another has two long and two short sides. Which is a square?',[
 ('CHECK THE SIDES','All four sides of a square are equal','First drawing: 6, 6, 6, 6 units',
 'The first drawing has four sides of six units each. All four sides are equal.'),
 ('CHECK THE CORNERS','A square has four square corners','4 square corners',
 'Its four corners are square corners, like the corner of a sheet of paper.'),
 ('COMPARE THE RECTANGLE','This rectangle has unequal neighbouring sides','Second drawing: 6, 9, 6, 9 units',
 'The second drawing has long and short sides. It is a rectangle, but it is not a square.'),
 ('TURNING DOES NOT CHANGE A SHAPE','A square stays a square when turned','A square is also a rectangle and a rhombus.',
 'Turning the first drawing does not change its sides or corners. It stays a square. A square is also a rectangle and a rhombus.')],g(5,2),'6+6+6+6','24')
add('shape-rhombus-trapezoid-early','Tell a rhombus and a trapezoid apart',
 'Drawing P has four equal sides.\nDrawing Q has just one pair of parallel sides.\nName each drawing.','P rhombus;Q trapezoid',
 'Drawing P has four equal sides. Drawing Q has just one pair of parallel sides. What are their names?',[
 ('COUNT THE SIDES','Both drawings have four straight sides','P and Q are quadrilaterals.',
 'Both drawings have four straight sides. They are quadrilaterals.'),
 ('CHECK THE EQUAL SIDES','A rhombus has four equal sides','P is a rhombus.',
 'All four sides of P are equal, so P is a rhombus.'),
 ('LOOK FOR PARALLEL SIDES','Parallel sides stay the same distance apart','Q is a trapezoid.',
 'Q has just one pair of parallel sides. It is a trapezoid.'),
 ('USE THE PROPERTIES','Turning a drawing does not change its name','P: 4 equal sides\nQ: exactly 1 pair of parallel sides',
 'Look at the side properties, not which way the drawing points. Turning either shape does not change its name.')],g(6,6),'2+2','4')
add('fractions-name-equal-parts','Name halves, thirds, and fourths',
 'Three rectangular cards are divided into equal parts.\nWhich card shows thirds?','Card Q',
 'Three rectangular cards are divided into equal parts. Which card shows thirds?',[
 ('CHECK EQUAL SIZE','Each part of a card must cover the same area','Equal parts share one whole fairly.',
 'Before naming the parts, check that each part of a card has the same area.'),
 ('COUNT TWO PARTS','Two equal parts are halves','P: 2 halves make one whole.',
 'Card P has two equal parts. Each part is a half. Two halves make the whole card.'),
 ('COUNT THREE PARTS','Three equal parts are thirds','Q: 3 thirds make one whole.',
 'Card Q has three equal parts. These are thirds, so Q answers our question.'),
 ('COUNT FOUR PARTS','Four equal parts are fourths, or quarters','R: 4 fourths make one whole.',
 'Card R has four equal parts. These are fourths, also called quarters. Four fourths make the whole card.')],g(7,4),'1+1+1','3')
add('fractions-equal-size-check','Check equal areas before calling pieces quarters',
 'Both rectangles have four pieces.\nWhich one is divided into fourths: X or Y?','Y',
 'Both rectangles have four pieces. Which one is divided into fourths, X or Y?',[
 ('COUNT THE PIECES','Four pieces alone are not enough','X: 4 pieces; Y: 4 pieces',
 'Both rectangles have four pieces. But counting pieces is only the first check.'),
 ('COMPARE THEIR AREAS','The pieces in X are unequal','X has unequal pieces.',
 'In X, some pieces are larger than others. They are not fourths.'),
 ('CHECK THE OTHER RECTANGLE','The four pieces in Y have equal area','Y has 4 equal parts: fourths.',
 'In Y, all four pieces have equal area. Each is one fourth of the rectangle.'),
 ('USE BOTH CHECKS','The same equal-area rule applies to halves','Halves: 2 equal parts\nFourths: 4 equal parts',
 'The answer is Y. Halves also need equal areas: two unequal pieces are not halves.')],g(7,6),'4/4','1')

# Draw original diagrams; never copy the worksheet pictures into lessons.
def card(d):d.rounded_rectangle((145,360,1775,840),radius=35,fill='white')
def clock(d,h,m):
 cx,cy,r=650,590,190;d.ellipse((cx-r,cy-r,cx+r,cy+r),outline=video.INK,width=5)
 for n in range(1,13):
  a=n*math.pi/6;x=cx+math.sin(a)*(r-30);y=cy-math.cos(a)*(r-30)
  d.text((x,y),str(n),font=video.font(29,True),fill=video.INK,anchor='mm')
 for angle,length,color,width in [((h%12+m/60)*math.pi/6,105,video.INK,13),(m*math.pi/30,145,video.TEAL,8)]:
  d.line((cx,cy,cx+math.sin(angle)*length,cy-math.cos(angle)*length),fill=color,width=width)
 d.ellipse((cx-9,cy-9,cx+9,cy+9),fill=video.INK)
def bars(d):
 vals=[6,9,4,6];names=['Apples','Pears','Plums','Peaches'];left=420;bottom=750
 for v in range(0,11,2):
  y=bottom-v*30;d.line((left,y,1530,y),fill='#D8DDDB',width=2);d.text((left-35,y),str(v),font=video.font(25),fill=video.INK,anchor='mm')
 for i,(name,n) in enumerate(zip(names,vals)):
  x=500+i*260;d.rectangle((x,bottom-n*30,x+120,bottom),fill=video.TEAL if i!=1 else '#DC8B34');d.text((x+60,bottom+38),name,font=video.font(28,True),fill=video.INK,anchor='mm')
def partitions(d,counts,labels,equal=True):
 for row,n in enumerate(counts):
  x=480;y=395+row*130;w=900;h=92
  video.text(d,(330,y+20),labels[row],37,video.INK,True)
  d.rectangle((x,y,x+w,y+h),fill='#D6ECE7',outline=video.INK,width=3)
  boundaries=[i/n for i in range(1,n)] if equal or row==1 else [1/8,1/4,1/2]
  for part in boundaries:d.line((x+w*part,y,x+w*part,y+h),fill=video.INK,width=3)
def draw_visual(s,d,scene,p):
 draw_card(s,d,scene,p);vid=s['video_id']
 if vid=='measure-touching-unit-blocks' and scene<4:
  card(d);d.rectangle((400,460,1480,525),fill='#DC8B34')
  for i in range(9):d.rectangle((400+i*120,550,520+i*120,670),outline=video.INK,width=4,fill='#D6ECE7')
  video.centered(d,740,'Equal blocks touch from one end to the other.',38,video.TEAL)
 if vid=='measure-compare-unit-heights' and scene==0:
  card(d)
  for x,n,label in [(520,4,'P'),(940,9,'Q'),(1360,7,'R')]:
   for k in range(n):d.rectangle((x-23,760-(k+1)*39,x+23,760-k*39),outline=video.INK,width=2,fill='#D6ECE7')
   d.text((x,798),label+': '+str(n),font=video.font(28,True),fill=video.INK,anchor='mm')
 if vid in ('data-read-small-bar-chart','data-combine-compare-chart-values') and scene in (0,1):card(d);bars(d)
 if vid in ('time-read-analogue-early','time-read-oclock-early') and scene<4:
  card(d);clock(d,3,40) if vid=='time-read-analogue-early' else clock(d,9,0)
  texts=['Read the two hands.','Short hand: hour','Long hand: minutes','Count minutes by fives.'] if vid=='time-read-analogue-early' else ['What time is it?','Short hand: 9','Long hand: 00 minutes','9:00 — nine o’clock']
  video.text(d,(970,550),texts[scene],37,video.TEAL,True)
 if vid=='shape-round-and-straight' and scene<4:
  card(d);d.ellipse((320,460,700,680),outline=video.TEAL,width=6)
  pts=[(1120+145*math.sin(i*2*math.pi/5),580-145*math.cos(i*2*math.pi/5)) for i in range(5)]
  d.polygon(pts,outline=video.INK,width=6);video.text(d,(420,730),'Oval',38,video.TEAL,True);video.text(d,(1020,760),'Pentagon',38,video.INK,True)
  if scene==3:
   card(d);d.ellipse((380,450,660,730),outline=video.TEAL,width=6);d.ellipse((1000,480,1470,700),outline=video.INK,width=6)
   video.text(d,(450,770),'Circle',35,video.TEAL,True);video.text(d,(1180,770),'Oval',35,video.INK,True)
 if vid=='shape-square-properties-early' and scene<4:
  card(d);d.polygon([(590,410),(765,585),(590,760),(415,585)],outline=video.TEAL,width=5);d.rectangle((1020,470,1460,700),outline=video.INK,width=5)
  video.text(d,(445,785),'4 equal sides',30,video.TEAL,True);video.text(d,(1070,745),'Long and short sides',30,video.INK,True)
 if vid=='shape-rhombus-trapezoid-early' and scene<4:
  card(d);d.polygon([(570,410),(725,590),(570,770),(415,590)],outline=video.TEAL,width=5);d.polygon([(1090,450),(1290,450),(1430,730),(950,730)],outline=video.INK,width=5)
  video.text(d,(530,785),'P',30,video.TEAL,True);video.text(d,(1160,775),'Q',30,video.INK,True)
 if vid=='fractions-name-equal-parts' and scene<4:card(d);partitions(d,[2,3,4],['P','Q','R'])
 if vid=='fractions-equal-size-check' and scene<4:card(d);partitions(d,[4,4],['X','Y'],False)

def lessons(doc):
 assert calendar.monthrange(2025,1)[1]-calendar.monthrange(2025,2)[1]==3
 assert 3*7+2==23 and [6,9,4,6].count(6)==2
 assert sum(n>6 for n in [6,9,4,6])==1
 result=make_lessons(SPECS,doc)
 for s in SPECS:video.DRAW[s['video_id']]=lambda d,i,p,s=s:draw_visual(s,d,i,p)
 return result
