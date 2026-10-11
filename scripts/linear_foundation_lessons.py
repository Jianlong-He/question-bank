"""One-step equations, coefficients and price models with new checked inputs."""
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons

SPECS=[
authored('linear-one-step-add-subtract','Undo addition and subtraction in one-step equations',
 'Solve x + 27 = 68 and y − 19 = 35.', 'x = 41; y = 54',
 'Solve x plus twenty-seven equals sixty-eight, and y minus nineteen equals thirty-five.',[
 ('FIRST EQUATION','Undo addition with subtraction','x + 27 − 27 = 68 − 27',
  'Subtract twenty-seven from both sides of the first equation. Doing the same thing on both sides preserves equality.'),
 ('FIND X','Simplify and check the original equation','x = 41\n41 + 27 = 68',
  'Sixty-eight minus twenty-seven is forty-one. Substituting forty-one recovers sixty-eight.'),
 ('SECOND EQUATION','Undo subtraction with addition','y − 19 + 19 = 35 + 19\ny = 54',
  'For the second equation, add nineteen to both sides. The value of y is fifty-four.'),
 ('CHECK AND GENERALIZE','Use the opposite operation on both sides','54 − 19 = 35\nUndo +a with −a; undo −a with +a.',
  'Fifty-four minus nineteen is thirty-five. To isolate a variable, undo its addition or subtraction on both sides, then check the original equation.')],
 g(6,7,1,8),equation=('x+27','68','x','41'),equalities=[('54-19','35')]),

authored('linear-unknown-subtrahend','Solve when the unknown is the amount subtracted',
 'Solve 93 − x = 58.', 'x = 35',
 'Solve ninety-three minus x equals fifty-eight.',[
 ('READ THE ORDER','x is being subtracted from ninety-three','93 − x = 58',
  'The unknown is the amount being taken away. Keep the subtraction order straight.'),
 ('ADD X','Move the unknown by adding it to both sides','93 = 58 + x',
  'Add x to both sides. The equation becomes ninety-three equals fifty-eight plus x.'),
 ('SUBTRACT','Remove fifty-eight from both sides','x = 93 − 58 = 35',
  'Subtract fifty-eight from both sides. The missing amount is thirty-five.'),
 ('CHECK','Substitute into the original subtraction','93 − 35 = 58',
  'Ninety-three minus thirty-five equals fifty-eight. When a minus x equals b, the missing subtracted amount is a minus b.')],
 g(6,7,2,10),equation=('93-x','58','x','35'),equalities=[('93-35','58')]),

authored('linear-one-step-multiply-divide','Undo multiplication and division in equations',
 'Solve 9x = 117 and y/13 = 6.', 'x = 13; y = 78',
 'Solve nine x equals one hundred seventeen, and y divided by thirteen equals six.',[
 ('UNDO MULTIPLICATION','Divide both sides by the nonzero coefficient','9x/9 = 117/9 → x = 13',
  'Nine x means nine times x. Divide both sides by nine to get x equals thirteen.'),
 ('CHECK X','Multiply the solution by the original coefficient','9 × 13 = 117',
  'Nine times thirteen is one hundred seventeen, so the first solution checks.'),
 ('UNDO DIVISION','Multiply both sides by the denominator','(y/13) × 13 = 6 × 13 → y = 78',
  'To undo division by thirteen, multiply both sides by thirteen. The value of y is seventy-eight.'),
 ('CHECK Y','Test the second solution in the original equation','78/13 = 6',
  'Seventy-eight divided by thirteen is six. Undo multiplication by dividing, and undo division by multiplying. Apply the same operation to both sides.')],
 g(6,7,2,3),equation=('9*x','117','x','13'),equalities=[('78/13','6')]),

authored('linear-decimal-additive-equation','Solve a one-step equation with decimal addition or subtraction',
 'Solve x − 7.4 = 12.8.', 'x = 20.2',
 'Solve x minus seven point four equals twelve point eight.',[
 ('INVERSE OPERATION','Undo subtraction by adding the same number','x − 7.4 + 7.4 = 12.8 + 7.4',
  'Add seven point four to both sides. The subtraction and addition on the left cancel.'),
 ('ALIGN PLACE VALUES','Add tenths to tenths and whole parts to whole parts','12.8 + 7.4 = 20.2',
  'Eight tenths plus four tenths is one whole and two tenths. Twelve plus seven plus that whole gives twenty point two.'),
 ('STATE THE SOLUTION','The variable is now alone','x = 20.2',
  'The solution is x equals twenty point two.'),
 ('CHECK','Substitute into the original equation','20.2 − 7.4 = 12.8',
  'Subtract seven point four from twenty point two to recover twelve point eight. Decimals follow the same equation rules as whole numbers.')],
 g(6,7,3,4),equation=('x-7.4','12.8','x','20.2'),equalities=[('20.2-7.4','12.8')]),

authored('linear-decimal-multiplier-equation','Solve an equation with a decimal coefficient',
 'Solve 1.6x = 12.8.', 'x = 8',
 'Solve one point six x equals twelve point eight.',[
 ('COEFFICIENT','One point six is multiplying the variable','1.6 × x = 12.8',
  'The coefficient one point six multiplies x. We need to undo that multiplication.'),
 ('DIVIDE BOTH SIDES','Divide by the same nonzero coefficient','x = 12.8 ÷ 1.6',
  'Divide both sides by one point six. It cancels from the left.'),
 ('CALCULATE','Scale both dividend and divisor by ten','12.8 ÷ 1.6 = 128 ÷ 16 = 8',
  'Multiply both numbers in the division by ten. One hundred twenty-eight divided by sixteen is eight.'),
 ('CHECK','Multiply the solution by the original coefficient','1.6 × 8 = 12.8',
  'One point six times eight is twelve point eight. The method is the same if the equation is written with the number on the left and the variable term on the right.')],
 g(6,7,4,7),equation=('1.6*x','12.8','x','8'),equalities=[('128/16','8')]),

authored('linear-fraction-additive-equations','Undo addition or subtraction of a fraction',
 'Solve x − 5/18 = 7/18 and y + 5/18 = 11/18.\nSimplify both answers.', 'x = 2/3; y = 1/3',
 'Solve x minus five eighteenths equals seven eighteenths, and y plus five eighteenths equals eleven eighteenths. Simplify both answers.',[
 ('FIND X','Add five eighteenths to both sides','x = 7/18 + 5/18 = 12/18',
  'Add five eighteenths to both sides of the first equation. Add the numerators and keep the common denominator.'),
 ('SIMPLIFY X','Divide numerator and denominator by six','x = 12/18 = 2/3',
  'Twelve eighteenths simplifies to two thirds.'),
 ('FIND Y','Subtract five eighteenths from both sides','y = 11/18 − 5/18 = 6/18 = 1/3',
  'In the second equation, subtract five eighteenths. Six eighteenths simplifies to one third.'),
 ('CHECK BOTH','Use eighteenths to check the original equations','12/18 − 5/18 = 7/18\n6/18 + 5/18 = 11/18',
  'Both answers check in the original equations. Undo addition or subtraction on both sides, then simplify the resulting fraction.')],
 g(6,7,3,5),equation=('x-5/18','7/18','x','2/3'),equalities=[('1/3+5/18','11/18')]),

authored('linear-fraction-coefficient-equation','Solve an equation with a fractional coefficient',
 'Solve (7/9)x = 14/15.\nWrite the answer as a simplified fraction and mixed number.', 'x = 6/5 = 1 1/5',
 'Solve seven ninths times x equals fourteen fifteenths. Write the answer as a simplified fraction and a mixed number.',[
 ('RECIPROCAL','The reciprocal of seven ninths is nine sevenths','(9/7) × (7/9) = 1',
  'Multiply by nine sevenths, the reciprocal of seven ninths. Their product is one.'),
 ('BOTH SIDES','Multiply the entire equation by the reciprocal','x = (14/15) × (9/7)',
  'Apply that multiplication to both sides, leaving x alone on the left.'),
 ('SIMPLIFY','Cancel common factors before multiplying','x = (2/5) × 3 = 6/5 = 1 1/5',
  'Cancel fourteen with seven, and nine with fifteen. The product is six fifths, or one and one fifth.'),
 ('CHECK','Substitute the simplified fraction','(7/9) × (6/5) = 42/45 = 14/15',
  'Seven ninths of six fifths is fourteen fifteenths, as required. Division by a nonzero fraction is multiplication by its reciprocal.')],
 g(6,7,5,2),equation=('7/9*x','14/15','x','6/5'),equalities=[('7/9*6/5','14/15')]),

authored('linear-combine-coefficients-equation','Combine like terms before solving an equation',
 'Solve 7x + 4x = 99.', 'x = 9',
 'Solve seven x plus four x equals ninety-nine.',[
 ('LIKE TERMS','Both terms have the same variable part','7x + 4x = (7 + 4)x',
  'Both terms are multiples of the same variable x, so combine their coefficients.'),
 ('COMBINE','Add the coefficients, keeping the variable','11x = 99',
  'Seven plus four is eleven. The equation becomes eleven x equals ninety-nine.'),
 ('DIVIDE','Undo multiplication by eleven','x = 99 ÷ 11 = 9',
  'Divide both sides by eleven. The solution is nine.'),
 ('CHECK','Use the original two terms','7(9) + 4(9) = 63 + 36 = 99',
  'Check the original equation, not just the combined one. Sixty-three plus thirty-six equals ninety-nine, so x equals nine works.')],
 g(6,7,4,3),equation=('7*x+4*x','99','x','9'),equalities=[('7*9+4*9','99')]),

authored('linear-mixed-coefficients-equation','Combine decimal and fractional coefficients',
 'Solve 2.4x + (3/5)x = 21.', 'x = 7',
 'Solve two point four x plus three fifths x equals twenty-one.',[
 ('SAME FORMAT','Convert the fraction coefficient to a decimal','3/5 = 0.6',
  'Three fifths equals zero point six. Write the coefficients in the same format before adding.'),
 ('COMBINE LIKE TERMS','Both terms contain the same variable','2.4x + 0.6x = 3x',
  'Two point four plus zero point six is three. The variable part stays x.'),
 ('SOLVE','Divide both sides by three','3x = 21 → x = 7',
  'Divide both sides by three to get x equals seven.'),
 ('CHECK','Evaluate both original terms','2.4(7) + (3/5)(7) = 16.8 + 4.2 = 21',
  'In the original equation, the terms are sixteen point eight and four point two. They add to twenty-one, confirming the solution.')],
 g(6,7,5,6),equation=('2.4*x+3/5*x','21','x','7'),equalities=[('3/5','0.6'),('2.4*7+3/5*7','21')]),

authored('linear-price-times-quantity-equation','Write and solve a price-times-quantity equation',
 'Tickets cost $8.25 each. A group pays $74.25.\nWrite an equation for the number t of tickets,\nthen solve it.', '8.25t = 74.25; t = 9 tickets',
 'Tickets cost eight dollars and twenty-five cents each. A group pays seventy-four dollars and twenty-five cents. Write an equation for the number t of tickets, then solve it.',[
 ('MODEL','Price per ticket times ticket count equals total cost','8.25 × t = 74.25',
  'Multiply the price per ticket by the unknown number of tickets to match the total cost.'),
 ('ISOLATE','Divide both sides by the price per ticket','t = 74.25 ÷ 8.25',
  'Divide both sides by eight point two five.'),
 ('CALCULATE','Scale both values equally to remove the decimals','7425 ÷ 825 = 9',
  'Multiply both numbers by one hundred. Seven thousand four hundred twenty-five divided by eight hundred twenty-five is nine.'),
 ('CHECK AND INTERPRET','The count must be a whole number of tickets','8.25 × 9 = 74.25\nThe group bought 9 tickets.',
  'Nine tickets cost seventy-four dollars and twenty-five cents. Report both the equation and the ticket count when the question requests them.')],
 g(6,7,5,9),equation=('8.25*t','74.25','t','9'),equalities=[('7425/825','9')]),
]

def lessons(doc):return make_lessons(SPECS,doc)
