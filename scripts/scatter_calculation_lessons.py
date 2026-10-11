"""Slope, linear prediction, coefficient interpretation and conditional rates."""
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons
SPECS=[
authored('scatter-slope-from-points','Find slope from paired observations or changes',
 'A straight pattern passes through (1, 4), (5, 14) and (9, 24).\nFind its slope.', '2.5',
 'A straight pattern passes through one, four; five, fourteen; and nine, twenty-four. Find its slope.',[
 ('CHANGES','Choose two points and subtract in matching order','Change in y = 14 − 4 = 10\nChange in x = 5 − 1 = 4',
 'Choose the first two points. Subtract their y coordinates to get ten, and their x coordinates in the same order to get four.'),
 ('SLOPE','Divide the vertical change by the horizontal change','Slope = change in y / change in x\n= 10/4 = 2.5',
 'Slope is vertical change divided by horizontal change. Ten divided by four is two point five.'),
 ('CHECK ANOTHER PAIR','The second interval must give the same slope','(24 − 14)/(9 − 5) = 10/4 = 2.5',
 'The second and third points also rise ten when x increases by four, so they give the same slope.'),
 ('INTERPRET','A rise of ten for a run of four means 2.5 per one','For each +1 in x, y increases by 2.5',
 'For each increase of one in x, y increases by two point five. If a question gives the changes directly, divide them in exactly the same way.')],
 g(8,7,6,8),equalities=[('(14-4)/(5-1)','2.5'),('(24-14)/(9-5)','2.5')]),
authored('scatter-predict-linear-pattern','Extend a linear pattern from three observations',
 'Points are (1, 6), (3, 14) and (5, 22).\nIf the same linear pattern continues, predict y at x = 8.', '34',
 'The points are one, six; three, fourteen; and five, twenty-two. If the same linear pattern continues, predict y at x equals eight.',[
 ('FIND THE RATE','Check that consecutive intervals have equal slopes','(14 − 6)/(3 − 1) = 4\n(22 − 14)/(5 − 3) = 4',
 'Both intervals have slope four. Each unit increase in x adds four to y.'),
 ('FIND THE INTERCEPT','Use y equals four x plus b and a known point','6 = 4(1) + b\nb = 2; y = 4x + 2',
 'Use the point one, six in y equals four x plus b. Six equals four plus b, so b is two. The rule is y equals four x plus two.'),
 ('PREDICT','Substitute eight into the rule','y = 4(8) + 2 = 34',
 'At x equals eight, the rule gives thirty-four.'),
 ('STATE THE ASSUMPTION','This extends beyond the observed x values','Prediction: 34, if the pattern continues',
 'Eight is beyond the observed x values. This is an extrapolation, so thirty-four is a prediction under the stated assumption that the same linear pattern continues.')],
 g(8,7,8,5),equalities=[('(14-6)/(3-1)','4'),('(22-14)/(5-3)','4'),('6-4*1','2'),('4*8+2','34')]),
authored('scatter-correlation-coefficient','Use the sign and magnitude of a correlation coefficient',
 'Compare r = 0.74 and r = −0.93.\nState each direction and identify the stronger linear association.', 'Positive; negative; r = −0.93 is stronger',
 'Compare correlation coefficients zero point seven four and negative zero point nine three. State each direction and identify the stronger linear association.',[
 ('DIRECTION','The sign tells whether the linear trend rises or falls','r = 0.74: positive\nr = −0.93: negative',
 'A positive coefficient indicates an upward linear trend. A negative coefficient indicates a downward linear trend.'),
 ('STRENGTH','Use distance from zero, ignoring the sign','|0.74| = 0.74\n|−0.93| = 0.93',
 'For linear strength, compare absolute values. They are zero point seven four and zero point nine three.'),
 ('COMPARE','The larger absolute value indicates the stronger linear association','0.93 > 0.74\nr = −0.93 is stronger',
 'Zero point nine three is larger, so negative zero point nine three represents the stronger linear association. Negative does not mean weak.'),
 ('REFERENCE POINTS','Values near either end of the range indicate strong linear association','r near +1: strong positive\nr near −1: strong negative',
 'A coefficient near positive one means a strong positive linear association. Near negative one means a strong negative linear association. Values near zero indicate little linear association; a curve may still be present.')],
 g(9,9,1,7),equalities=[('93/100-74/100','19/100')]),
authored('statistics-association-conditional-rates','Compare conditional percentages to assess association',
 'In a sample, 72% of library-club members volunteer.\nAmong nonmembers, 28% volunteer.\nDo these rates suggest an association?', 'Yes; the conditional rates differ by 44 percentage points',
 'In a sample, seventy-two percent of library-club members volunteer, compared with twenty-eight percent of nonmembers. Do these rates suggest an association?',[
 ('COMPARE THE SAME OUTCOME','Both rates measure volunteering within a group','Members: 72% volunteer\nNonmembers: 28% volunteer',
 'Both percentages describe the same outcome, volunteering, within different groups. These are conditional rates.'),
 ('FIND THE GAP','Subtract the percentages','72% − 28% = 44 percentage points',
 'The rates differ by forty-four percentage points. Say percentage points because we subtracted two percentages.'),
 ('INTERPRET','The volunteering rate differs by membership group','Different conditional rates suggest association',
 'The large difference suggests an association between club membership and volunteering in this sample.'),
 ('LIMIT THE CONCLUSION','An association alone does not establish a cause','Association does not prove causation',
 'This comparison does not prove that joining the club causes volunteering. Other differences between the groups could explain the association. Population conclusions would also depend on how the sample was collected.')],
 g(9,11,1,8),equalities=[('72-28','44')]),
]
def lessons(doc):return make_lessons(SPECS,doc)
