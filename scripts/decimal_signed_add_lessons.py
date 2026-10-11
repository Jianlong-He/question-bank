"""Adding decimals of opposite signs with a checked fresh example."""
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons
SPECS=[
authored('add-decimals-opposite-signs','Add decimals with opposite signs',
 'Find −7.6 + 2.85.', '−4.75',
 'Find negative seven point six plus two point eight five. The numbers have opposite signs.',[
 ('COMPARE MAGNITUDES','Ignore the signs briefly and compare distances from zero','7.60 > 2.85',
 'Compare the magnitudes. Seven point six is greater than two point eight five. The greater magnitude belongs to the negative number.'),
 ('FIND THE DIFFERENCE','Subtract the smaller magnitude from the larger','7.60 − 2.85 = 4.75',
 'Subtract two point eight five from seven point six zero. Align decimal points and regroup as needed. The difference is four point seven five.'),
 ('USE THE SIGN','Keep the sign of the number with greater magnitude','−7.6 + 2.85 = −4.75',
 'Use the negative sign because the negative number had greater magnitude. The sum is negative four point seven five.'),
 ('CHECK BY REVERSING','Subtract the amount added to recover the starting value','−4.75 − 2.85 = −7.60',
 'Subtract two point eight five from the result to return to negative seven point six. Adding a positive amount moved the starting value toward zero.')],
 g(7,4,2,5),equalities=[('-7.6+2.85','-4.75'),('7.60-2.85','4.75'),('-4.75-2.85','-7.60')]),
]
def lessons(doc):return make_lessons(SPECS,doc)
