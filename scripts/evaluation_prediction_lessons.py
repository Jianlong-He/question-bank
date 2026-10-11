"""Predicted values from fitted linear models, with fresh positive/negative slopes."""
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons
SPECS=[authored('evaluation-linear-prediction','Predict a value using a line of best fit',
 'Model A: y = 6x + 11. Predict y when x = 7.\nModel B: y = −4x + 38. Predict y when x = 5.', 'Model A: 53; Model B: 18',
 'Use two fitted models to predict y. Model A is six x plus eleven with x equal to seven. Model B is negative four x plus thirty-eight with x equal to five.',[
 ('FIRST MODEL','Replace x by seven','Predicted y = 6(7) + 11',
 'Substitute seven for x in the first model. Multiply before adding.'),
 ('CALCULATE','Six times seven is forty-two','Predicted y = 42 + 11 = 53',
 'Six times seven is forty-two. Add eleven to get the predicted value fifty-three.'),
 ('NEGATIVE SLOPE','Keep the negative sign on the coefficient','Predicted y = (−4)(5) + 38\n= −20 + 38 = 18',
 'For the second model, negative four times five is negative twenty. Add thirty-eight to get eighteen.'),
 ('INTERPRET','A fitted model gives a prediction','Model A predicts 53.\nModel B predicts 18.',
 'These are predictions from the fitted lines. Actual observations may differ. Substitute the given input, follow the operation order, and report the predicted response.')],
 g(8,7,10,1),equalities=[('6*7+11','53'),('-4*5+38','18')])]
def lessons(doc):return make_lessons(SPECS,doc)
