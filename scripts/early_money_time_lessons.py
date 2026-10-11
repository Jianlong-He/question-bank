"""Original Grade 2 money and elapsed-minute examples."""
from algebra_lessons import authored
from card_lessons import make_lessons,draw_card
from number_sense_lessons import source
import generate_sample_videos as video
from early_measurement_lessons import clock,card

def g(w,q):return source(2,5,w,q)
SPECS=[
authored('money-total-mixed-coins','Find the total value of a group of coins',
 'Find the value in cents:\n3 quarters, 2 dimes, 4 nickels, and 3 pennies.','118 cents',
 'Find the total value of three quarters, two dimes, four nickels, and three pennies.',[
 ('COUNT THE QUARTERS','Each quarter is worth 25 cents','25 + 25 + 25 = 75 cents',
 'Each quarter is twenty-five cents. Count twenty-five, fifty, seventy-five.'),
 ('COUNT DIMES AND NICKELS','A dime is 10 cents; a nickel is 5 cents','Dimes: 10 + 10 = 20\nNickels: 5 + 5 + 5 + 5 = 20',
 'Two dimes make twenty cents. Four nickels also make twenty cents.'),
 ('COUNT THE PENNIES','Each penny is worth 1 cent','1 + 1 + 1 = 3 cents',
 'Each penny is one cent, so three pennies make three cents.'),
 ('ADD THE VALUES','Use cents for every group','75 + 20 + 20 + 3 = 118 cents',
 'Add the group values: seventy-five plus twenty plus twenty plus three. The total is one hundred eighteen cents.')],g('1',6),expression='3*25+2*10+4*5+3',value='118'),
authored('money-total-bills','Add the values of different bills',
 'You have 3 one-dollar bills, 2 five-dollar bills,\nand 2 ten-dollar bills. How much money is that?','$33',
 'You have three one-dollar bills, two five-dollar bills, and two ten-dollar bills. Find the total value.',[
 ('COUNT ONE-DOLLAR BILLS','Add the value of each bill','$1 + $1 + $1 = $3',
 'Three one-dollar bills are worth three dollars.'),
 ('COUNT FIVE-DOLLAR BILLS','Two bills, each worth five dollars','$5 + $5 = $10',
 'Two five-dollar bills are worth ten dollars.'),
 ('COUNT TEN-DOLLAR BILLS','Two bills, each worth ten dollars','$10 + $10 = $20',
 'Two ten-dollar bills are worth twenty dollars.'),
 ('ADD ALL THREE GROUPS','Count dollars, not the number of bills','$3 + $10 + $20 = $33',
 'Add three, ten, and twenty dollars. The total is thirty-three dollars. The number of bills alone does not tell their value.')],g('1',8),expression='3+2*5+2*10',value='33'),
authored('money-compare-coin-groups','Compare groups of coins using cents',
 'Which group is worth the most?\n3 quarters; 8 dimes; 14 nickels; 65 pennies.','8 dimes',
 'Which is worth the most: three quarters, eight dimes, fourteen nickels, or sixty-five pennies?',[
 ('CHANGE EVERY GROUP TO CENTS','Compare values in the same unit','Quarter: 25¢   Dime: 10¢\nNickel: 5¢   Penny: 1¢',
 'Use cents for every group. A quarter is twenty-five, a dime ten, a nickel five, and a penny one cent.'),
 ('COUNT QUARTERS AND DIMES','Count by each coin’s value','3 quarters = 75¢\n8 dimes = 80¢',
 'Three quarters are seventy-five cents. Eight dimes are eighty cents.'),
 ('COUNT NICKELS AND PENNIES','More coins can still mean less money','14 nickels = 70¢\n65 pennies = 65¢',
 'Fourteen nickels are seventy cents. Sixty-five pennies are sixty-five cents.'),
 ('CHOOSE THE GREATEST VALUE','Match the largest value to its group','80 > 75 > 70 > 65\n8 dimes are worth the most.',
 'Eighty cents is the greatest value, so eight dimes are worth the most.')],g('1',9),expression='8*10',value='80',equalities=[('3*25','75'),('14*5','70')]),
authored('money-check-exact-payment','Check whether bills and coins cover a price',
 'A puzzle costs $15.40. You have 3 five-dollar bills,\n1 quarter, 1 dime, and 1 nickel. Is that enough?','Yes, exactly $15.40',
 'A puzzle costs fifteen dollars and forty cents. You have three five-dollar bills, a quarter, a dime, and a nickel. Is that enough?',[
 ('TOTAL THE BILLS','Keep dollars and cents labelled','$5 + $5 + $5 = $15',
 'The three five-dollar bills make fifteen dollars.'),
 ('TOTAL THE COINS','Use each coin’s value','25¢ + 10¢ + 5¢ = 40¢',
 'The quarter, dime, and nickel make twenty-five plus ten plus five, or forty cents.'),
 ('COMBINE DOLLARS AND CENTS','One dollar contains 100 cents','$15 and 40¢ = $15.40',
 'Together, the bills and coins make fifteen dollars and forty cents.'),
 ('COMPARE WITH THE PRICE','Equal to the price is enough','$15.40 = $15.40\nYes — exactly enough.',
 'The payment equals the price. Yes, it is exactly enough to buy the puzzle.')],g('1',10),expression='3*500+25+10+5',value='1540'),
authored('time-move-minutes-within-hour','Find a time a few minutes earlier or later',
 'This clock shows 6:15.\nWhat time is 10 minutes later?\nWhat time is 10 minutes earlier?','6:25 later;6:05 earlier',
 'This clock shows six fifteen. Find the time ten minutes later and ten minutes earlier.',[
 ('READ THE STARTING TIME','The long hand counts minutes','6:15',
 'The short hand has passed six. The long hand points to three, meaning fifteen minutes.'),
 ('MOVE FORWARD TEN MINUTES','Later means add minutes','15 + 10 = 25\nTen minutes later: 6:25',
 'For ten minutes later, add ten to fifteen. That is twenty-five, so the time is six twenty-five.'),
 ('RETURN TO THE ORIGINAL TIME','Earlier is measured from 6:15','15 − 10 = 5\nTen minutes earlier: 6:05',
 'Return to the original six fifteen. For ten minutes earlier, subtract ten. The time is six oh five.'),
 ('CHECK THE ORDER','Both changes stay within this hour','6:05 → 6:15 → 6:25\nEach gap is 10 minutes.',
 'Six oh five comes before six fifteen, and six twenty-five comes after. Each gap is ten minutes.')],g('2',9),expression='15+10',value='25',equalities=[('15-10','5')])
]
def lessons(doc):
 result=make_lessons(SPECS,doc)
 spec=SPECS[-1]
 def draw(d,i,p):
  if i<2:
   card(d);clock(d,6,15)
   video.text(d,(960,510),'6:15 — six fifteen',45,video.TEAL,True)
   if i==0:
    video.text(d,(960,590),'10 minutes later?',37,video.INK,True)
    video.text(d,(960,650),'10 minutes earlier?',37,video.INK,True)
   else:video.text(d,(960,600),'Long hand: 3 means 15 minutes',33,video.INK,True)
  else:draw_card(spec,d,i,p)
 video.DRAW[spec['video_id']]=draw
 return result
