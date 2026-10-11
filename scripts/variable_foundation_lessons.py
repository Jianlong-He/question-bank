"""Identify variables, polynomial parts, and model input/output roles."""
from algebra_lessons import authored
from number_sense_lessons import source as g
from card_lessons import make_lessons
SPECS=[
authored('variable-coefficient-constant','Identify a variable, coefficient and constant',
 'In −6m + 13, identify the variable,\nits coefficient and the constant term.', 'Variable m; coefficient −6; constant 13',
 'In negative six m plus thirteen, identify the variable, its coefficient, and the constant term.',[
 ('VARIABLE','A letter can represent different or unknown values','Variable: m',
 'The variable is m. It represents a value that may vary or be unknown.'),
 ('COEFFICIENT','The coefficient multiplies the variable','−6m = (−6) × m\nCoefficient: −6',
 'Negative six multiplies m, so negative six is the coefficient. Keep the sign attached to the number.'),
 ('CONSTANT TERM','A constant term has no variable factor','Constant term: 13',
 'Thirteen is the constant term. It does not change when m changes.'),
 ('CHECK THE ROLES','Try two values of the variable','m = 1 → −6m + 13 = 7\nm = 2 → −6m + 13 = 1',
 'Changing m changes the expression value. The coefficient stays negative six and the constant stays thirteen. A number-only calculation contains no variable.')],
 g(6,6,1,1),equalities=[('-6*1+13','7'),('-6*2+13','1')]),
authored('variable-polynomial-coefficients','Read signed, missing and constant polynomial coefficients',
 'For 5z⁴ − z² + 8z − 14, find the constant term\nand the coefficients of z² and z³.', 'Constant −14; z² coefficient −1; z³ coefficient 0',
 'For five z to the fourth minus z squared plus eight z minus fourteen, find the constant term and the coefficients of z squared and z cubed.',[
 ('CONSTANT TERM','The constant has no variable factor','Constant term: −14',
 'The term without z is negative fourteen. Include its negative sign.'),
 ('IMPLICIT COEFFICIENT','A minus sign alone means multiplication by negative one','−z² = (−1)z²\nCoefficient of z²: −1',
 'Negative z squared means negative one times z squared. Its coefficient is negative one, not zero.'),
 ('MISSING POWER','A missing term has coefficient zero','No z³ term → 0z³\nCoefficient of z³: 0',
 'There is no z cubed term, so its coefficient is zero. Insert that zero when aligning polynomial division or listing coefficients.'),
 ('LIST IN DESCENDING POWERS','Do not skip a power in a coefficient list','5z⁴ + 0z³ − z² + 8z − 14\nCoefficients: 5, 0, −1, 8, −14',
 'Read coefficients from the fourth power down to the constant. The list is five, zero, negative one, eight, negative fourteen.')],
 g(11,1,1,10),identities=[('5*z**4-z*z+8*z-14','5*z**4+0*z**3-z*z+8*z-14'),('-z*z','(-1)*z*z')]),
authored('variable-model-input-output','Identify independent inputs and dependent outputs',
 'A rental cost is C = 3t + b. Time t varies and fee b is fixed.\nIdentify the independent variable, dependent variable and parameter.', 'Independent t; dependent C; fixed parameter b',
 'A rental cost C is three t plus b. Time t varies and fee b is fixed. Identify the independent variable, dependent variable, and fixed parameter.',[
 ('IDENTIFY WHAT VARIES','Time is the input chosen for this model','Independent variable: t',
 'Time is the varying input. We choose a time and use the formula to calculate the cost. Time t is independent in this model.'),
 ('IDENTIFY WHAT IS CALCULATED','Cost changes in response to the input','Dependent variable: C',
 'The cost is calculated from the input, so C is the dependent variable.'),
 ('KEEP THE PARAMETER FIXED','A symbol can represent a fixed setting','Fixed parameter: b\nIf b = 4: t = 2 gives C = 10.',
 'The fee b is fixed for this rental, so it is a parameter. With fee four and time two, the cost is ten.'),
 ('USE THE STATED MODEL','An output may depend on more than one input','If A = L × W is computed from L and W:\ninputs L, W; dependent output A.',
 'An output can depend on several inputs, as area depends on chosen length and width. Identify what is given and what is computed; the letter name alone does not decide the role.')],
 g(6,7,7,4),equalities=[('3*2+4','10')]),
]
def lessons(doc):return make_lessons(SPECS,doc)
