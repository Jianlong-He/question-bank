"""Cyclic-time and gear-alignment methods from enrichment questions."""
from math import lcm
from algebra_lessons import authored
from card_lessons import make_lessons


def e(w,q):return (f'worksheets/enrichment/number-theory 1/U1modular-arithmetic/E-NT1U1W{w}.csv',str(q))

SPECS=[
authored('enrichment-cycles-flash-timer','Count event intervals before reducing a timer reading',
 'A beacon flashes at time 0, then every 9 seconds.\nA timer cycles through 0 to 11 and repeats.\nWhat does it show at the sixth flash?', '9',
 'A beacon flashes at time zero, then every nine seconds. A timer cycles from zero through eleven. What does it show at the sixth flash?',[
 ('COUNT INTERVALS','The first flash already happens at time zero','Sixth flash → 6 − 1 = 5 intervals',
  'The first flash happens before any waiting. To reach the sixth flash, wait through five intervals, not six.'),
 ('ELAPSED TIME','Multiply the interval count by the spacing','5 × 9 = 45 seconds',
  'Five intervals of nine seconds give forty-five seconds elapsed.'),
 ('TIMER CYCLE','Zero through eleven makes a twelve-second cycle','45 = 3 × 12 + 9',
  'The timer repeats every twelve seconds. Forty-five is three full cycles plus nine seconds.'),
 ('READ THE REMAINDER','The remainder is the displayed timer value','45 mod 12 = 9',
  'The timer shows nine. When counting numbered events, account for the first event at time zero before taking the remainder.')],
 e(4,2),expression='((6-1)*9)%12',value='9',equalities=[('(6-1)*9','45'),('45','3*12+9')]),

authored('enrichment-cycles-elapsed-remainder','Find the position within a repeating time cycle',
 'A wheel completes one turn every 54 seconds.\nIt starts at the beginning of a turn at time 0.\nAfter 749 seconds, how far into a turn is it?', '47 seconds into the current turn',
 'A wheel completes one turn every fifty-four seconds, starting at the beginning at time zero. After seven hundred forty-nine seconds, how far into a turn is it?',[
 ('CYCLE LENGTH','Remove complete fifty-four-second turns','Current position = elapsed time mod 54',
  'Complete turns return to the starting position. Only the time remaining after complete turns determines the current position.'),
 ('FULL CYCLES','Find the greatest complete multiple below the elapsed time','13 × 54 = 702 seconds',
  'Thirteen full turns take seven hundred two seconds. Fourteen would exceed the elapsed time.'),
 ('REMAINDER','Subtract the time spent on full turns','749 − 702 = 47 seconds',
  'Subtract seven hundred two from seven hundred forty-nine. The remainder is forty-seven seconds.'),
 ('CHECK','The remainder must be smaller than one cycle','749 = 13 × 54 + 47; 0 ≤ 47 < 54',
  'Forty-seven is between zero and fifty-four, so it is a valid remainder. The wheel is forty-seven seconds into its next turn.')],
 e(4,5),expression='749%54',value='47',equalities=[('13*54+47','749')]),

authored('enrichment-cycles-gear-alignment','Use a common multiple to find gear realignment',
 'A gear with 18 teeth drives a gear with 42 teeth.\nHow many full turns of the smaller gear occur\nbefore both first return to their starting orientations?',
 '7 turns of the smaller gear',
 'A gear with eighteen teeth drives one with forty-two teeth. How many full turns of the smaller gear occur before both first return to their starting orientations?',[
 ('COMMON TOOTH COUNT','Both gears must complete whole numbers of turns','Use the least common multiple of 18 and 42.',
  'The same number of teeth passes the contact point on each gear. Both counts must be whole multiples of their tooth totals.'),
 ('FACTOR','Take the highest needed power of each prime','18 = 2 × 3²; 42 = 2 × 3 × 7\nLCM = 2 × 3² × 7 = 126',
  'Eighteen is two times three squared. Forty-two is two times three times seven. Their least common multiple is one hundred twenty-six.'),
 ('SMALLER GEAR','Divide common tooth count by its tooth total','126 ÷ 18 = 7 full turns',
  'Divide one hundred twenty-six by eighteen. The smaller gear completes seven full turns.'),
 ('CHECK THE OTHER GEAR','Both turn counts must be whole numbers','126 ÷ 42 = 3 full turns',
  'The larger gear completes three full turns, so both regain their original orientations. Using the least common multiple makes this the first return.')],
 e('4HWa',3),expression='126/18',value='7',equalities=[('126/42','3'),('2*3**2*7','126')]),
]


def lessons(doc):
    assert lcm(18,42)==126
    assert all((n*18)%42 for n in range(1,7))
    assert [9*i for i in range(6)]==[0,9,18,27,36,45]
    return make_lessons(SPECS,doc)
