"""Analogous examples for corrected future-event and rigid-rotation questions."""
from algebra_lessons import authored
from card_lessons import make_lessons
from number_theory_lessons import source

SPECS=[
authored('crt-future-event-offsets','Find when periodic events with different starts coincide',
 'Three bells ring every 4, 5, and 7 minutes.\nTheir next rings are in 2, 3, and 5 minutes.\nWhen will they first ring together?','138 minutes',
 'Three bells ring every four, five, and seven minutes. Their next rings are in two, three, and five minutes. When will they first ring together?',[
 ('TRANSLATE THE NEXT RING','Time until the next event gives its positive remainder','t ≡ 2 (mod 4); t ≡ 3 (mod 5)\nt ≡ 5 (mod 7)',
 'The next rings give positive remainders. Time t must leave two modulo four, three modulo five, and five modulo seven.'),
 ('SPOT THE COMMON OFFSET','Each remainder is two below its modulus','t + 2 is divisible by 4, 5, and 7.',
 'Each remainder is two below its modulus. Adding two makes the time divisible by all three periods.'),
 ('FIND THE FIRST POSITIVE TIME','Use the least common multiple','LCM(4,5,7) = 140\nt + 2 = 140k, so t = 140k − 2.',
 'The least common multiple is one hundred forty. All possible times are one hundred forty k minus two.'),
 ('CHOOSE AND CHECK','k = 0 is in the past; k = 1 is the first future time','t = 138 minutes\n138 mod 4 = 2; mod 5 = 3; mod 7 = 5',
 'Zero gives a past time. One gives one hundred thirty-eight minutes, the first future time. Check that it has all three required remainders.')],source('CRT',4,4),equalities=[('138%4','2'),('138%5','3'),('138%7','5'),('4*5*7','140')]),
authored('modular-rigid-square-rotation','Track a labelled square through clockwise quarter-turns',
 'A square has fixed labels: A top, B right,\nC bottom, D left. Rotate it clockwise\n13 quarter-turns. Which label is now at the top?','D',
 'A square has fixed labels: A at the top, B on the right, C at the bottom, and D on the left. Rotate the square clockwise thirteen quarter-turns. Which label reaches the top?',[
 ('FOLLOW THE PHYSICAL MOTION','One clockwise turn moves the left side to the top','Initial top: A\nAfter one clockwise quarter-turn: D',
 'Follow the square itself. In one clockwise quarter-turn, the left side moves to the top, so D reaches the top.'),
 ('BUILD THE TOP-LABEL CYCLE','The labels stay attached to their sides','Turns:  0    1    2    3    4\nTop:    A    D    C    B    A',
 'The top labels are A, D, C, B, then A again. Four quarter-turns restore the starting position.'),
 ('REMOVE COMPLETE REVOLUTIONS','Only the remaining quarter-turns matter','13 = 4 × 3 + 1\n13 mod 4 = 1',
 'Thirteen is three full revolutions plus one quarter-turn. Only that last quarter-turn changes the final orientation.'),
 ('READ THE FINAL TOP LABEL','Apply one clockwise turn to the initial position','One remaining turn: A → D\nThe label at the top is D.',
 'One clockwise turn from the original position brings D to the top. The answer is D.')],source('modular-arithmetic','4HWb',2),expression='13%4',value='1'),
]

def lessons(doc):
 assert [t for t in range(140) if t%4==2 and t%5==3 and t%7==5]==[138]
 labels=['A','B','C','D']
 assert labels[-(13%4)]=='D'
 return make_lessons(SPECS,doc)
