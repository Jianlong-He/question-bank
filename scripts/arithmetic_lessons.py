"""Authored arithmetic examples. Fractions verify the calculations exactly."""
from card_lessons import spec, make_lessons
from fractions import Fraction
from math import lcm


def fraction_text(value,mixed=False):
    f=Fraction(value)
    if mixed and f>1 and f.denominator!=1:
        return f'{f.numerator//f.denominator} {f.numerator%f.denominator}/{f.denominator}'
    return str(f)


def fraction_speech(value,mixed=False):
    f=Fraction(value)
    if f.denominator==1:return str(f.numerator)
    if mixed and f>1:
        return f'{f.numerator//f.denominator} and {fraction_speech(Fraction(f.numerator%f.denominator,f.denominator))}'
    return f'{f.numerator} over {f.denominator}'


def fraction_spec(vid,values,operation,mixed=False):
    values=[Fraction(v) for v in values]
    symbols={'add':'+','subtract':'−','multiply':'×','divide':'÷','add-subtract':'+'}
    def join(items,ascii=False):
        if operation=='add-subtract':return f'{items[0]} + {items[1]} - {items[2]}' if ascii else f'{items[0]} + {items[1]} − {items[2]}'
        symbol= {'add':'+','subtract':'-','multiply':'*','divide':'/'}[operation] if ascii else symbols[operation]
        return f' {symbol} '.join(items)
    expression=join([f'({v.numerator}/{v.denominator})' for v in values],True)
    from card_lessons import exact
    result=exact(expression)
    answer=fraction_text(result,mixed)
    question='Find '+join([fraction_text(v,mixed) for v in values])+'.'
    display_improper=join([str(v) for v in values])
    start=f"Let's {operation.replace('-',' and ')} these {'mixed numbers' if mixed else 'fractions'}."
    if mixed:
        method=('CONVERT','Change mixed numbers to improper fractions', '\n'.join(f'{fraction_text(v,True)} = {v}' for v in values),
                'First convert each mixed number to an improper fraction. Multiply the whole number by its denominator, then add the numerator.')
    else:
        method=('CHOOSE THE METHOD','Work with numerators and denominators',display_improper,
                'Keep track of the numerator and denominator of each fraction.')
    if operation in ('add','subtract','add-subtract'):
        denominator=lcm(*(v.denominator for v in values))
        numerators=[v.numerator*(denominator//v.denominator) for v in values]
        converted=join([f'{n}/{denominator}' for n in numerators])
        second=('MATCH DENOMINATORS','Use a common denominator',converted,
                f'Use {denominator} as the common denominator. Rewrite each fraction without changing its value.')
        third=('COMBINE','Combine the numerators',f'({join([str(n) for n in numerators])}) / {denominator}\n= {answer}',
               f"Now {operation.replace('-',' and ')} the numerators and keep the denominator. Simplify the result to {fraction_speech(result,mixed)}.")
        if operation=='add':check=f'{result} − {values[1]} = {values[0]}';spoken='Subtract the second fraction from the sum. You should recover the first fraction.'
        elif operation=='subtract':check=f'{result} + {values[1]} = {values[0]}';spoken='Add the subtracted fraction back to the answer. You recover the first fraction.'
        else:check=f'{result} + {values[2]} − {values[1]} = {values[0]}';spoken='Undo the last subtraction with addition, then undo the first addition with subtraction. You recover the starting fraction.'
    elif operation=='multiply':
        numerator=values[0].numerator*values[1].numerator;denominator=values[0].denominator*values[1].denominator
        second=('MULTIPLY','Multiply across',f'({values[0].numerator} × {values[1].numerator}) / ({values[0].denominator} × {values[1].denominator})',
                'Multiply the numerators together. Then multiply the denominators together.')
        third=('SIMPLIFY','Reduce the product',f'{numerator}/{denominator} = {answer}',
               f'Simplify the fraction. The product is {fraction_speech(result,mixed)}.')
        check=f'({result}) ÷ ({values[1]}) = {values[0]}';spoken='Divide the product by the second factor to recover the first factor.'
    else:
        reciprocal=1/values[1]
        second=('RECIPROCAL','Multiply by the reciprocal',f'({values[0]}) × ({reciprocal})',
                f'Keep the first fraction and multiply by the reciprocal of the second. The reciprocal is {fraction_speech(reciprocal)}.')
        third=('MULTIPLY','Multiply and simplify',f'({values[0]}) × ({reciprocal}) = {answer}',
               f'Multiply across and simplify. The quotient is {fraction_speech(result,mixed)}.')
        check=f'({result}) × ({values[1]}) = {values[0]}';spoken='Multiply the quotient by the original divisor. You should get the dividend back.'
    fourth=('CHECK','Undo the calculation',check,spoken)
    return spec(vid,operation.replace('-',' and ').capitalize()+' fractions',question,answer,expression,str(result),start,[method,second,third,fourth])


SPECS=[
spec('arithmetic-add-whole-numbers-within-20','Addition within 20','Find 8 + 6.','14','8+6','14',
     "Let's add eight and six. Making ten gives us a useful shortcut.",[
 ('MAKE TEN','Take 2 from the 6','6 = 2 + 4',"Split six into two and four. The two will help eight reach ten."),
 ('ADD THE FIRST PART','8 plus 2 makes 10','8 + 2 = 10',"Eight plus two is ten. We still have four left to add."),
 ('ADD WHAT REMAINS','10 plus 4 makes 14','10 + 4 = 14',"Ten plus four is fourteen. So eight plus six is fourteen."),
 ('CHECK','Subtract to check','14 − 6 = 8',"Check by subtracting six from fourteen. We get eight, our starting number.")], [('8+6','14'),('14-6','8')]),
spec('arithmetic-subtract-whole-numbers-within-20','Subtraction within 20','Find 16 − 9.','7','16-9','7',
     "Let's find sixteen minus nine. We'll subtract in two easy steps.",[
 ('BREAK UP NINE','Subtract 6, then 3','9 = 6 + 3',"Break nine into six and three. Taking away six gets us to ten."),
 ('REACH TEN','16 minus 6 is 10','16 − 6 = 10',"Sixteen minus six is ten."),
 ('FINISH','Subtract the remaining 3','10 − 3 = 7',"Now subtract the remaining three. Ten minus three is seven."),
 ('CHECK','Add back the amount removed','7 + 9 = 16',"Seven plus nine is sixteen. That confirms our answer is seven.")]),
spec('arithmetic-add-whole-numbers-column-method','Column addition','Find 468 + 257.','725','468+257','725',
     "Let's add four hundred sixty-eight and two hundred fifty-seven. Line up matching place values.",[
 ('ONES','Add the ones and regroup','8 + 7 = 15\nWrite 5 ones; carry 1 ten.',"Eight ones plus seven ones makes fifteen. Write five ones and carry one ten."),
 ('TENS','Include the carried ten','6 + 5 + 1 = 12\nWrite 2 tens; carry 1 hundred.',"Six tens plus five tens plus one carried ten makes twelve tens. Write two tens and carry one hundred."),
 ('HUNDREDS','Add the hundreds','4 + 2 + 1 = 7\n468 + 257 = 725',"Four hundreds plus two hundreds plus the carried hundred makes seven hundreds. The sum is seven hundred twenty-five."),
 ('CHECK','Subtract one addend','725 − 257 = 468',"Subtract two hundred fifty-seven from the sum. We get four hundred sixty-eight, so the addition checks.")]),
spec('arithmetic-subtract-whole-numbers-column-method','Column subtraction','Find 752 − 386.','366','752-386','366',
     "Let's subtract three hundred eighty-six from seven hundred fifty-two. We will regroup by place value.",[
 ('ONES','Regroup one ten','12 − 6 = 6\n5 tens becomes 4 tens.',"We cannot take six ones from two ones, so regroup one ten. Twelve minus six is six."),
 ('TENS','Regroup one hundred','14 − 8 = 6\n7 hundreds becomes 6 hundreds.',"Four tens is not enough to subtract eight tens. Regroup one hundred, then fourteen tens minus eight tens is six tens."),
 ('HUNDREDS','Finish the subtraction','6 − 3 = 3\n752 − 386 = 366',"Six hundreds minus three hundreds is three hundreds. Our answer is three hundred sixty-six."),
 ('CHECK','Add to check','366 + 386 = 752',"Add the difference to the number we subtracted. Three hundred sixty-six plus three hundred eighty-six is seven hundred fifty-two.")]),
spec('arithmetic-multiply-whole-numbers','Multiplication','Find 23 × 14.','322','23*14','322',
     "Let's multiply twenty-three by fourteen. Split fourteen into ten and four.",[
 ('SPLIT A FACTOR','Use the distributive property','23 × 14 = 23 × (10 + 4)',"Multiplying by fourteen is the same as multiplying by ten and by four, then adding."),
 ('PARTIAL PRODUCTS','Calculate both products','23 × 10 = 230\n23 × 4 = 92',"Twenty-three times ten is two hundred thirty. Twenty-three times four is ninety-two."),
 ('ADD','Combine the partial products','230 + 92 = 322',"Add the partial products. Two hundred thirty plus ninety-two is three hundred twenty-two."),
 ('CHECK','Divide by one factor','322 ÷ 14 = 23',"Dividing the product by fourteen gives twenty-three. The multiplication checks.")]),
spec('arithmetic-divide-whole-numbers','Division','Find 156 ÷ 12.','13','156/12','13',
     "Let's divide one hundred fifty-six by twelve using easy multiples.",[
 ('USE TEN GROUPS','Start with a known multiple','12 × 10 = 120',"Ten groups of twelve make one hundred twenty."),
 ('FIND WHAT REMAINS','Subtract the first 120','156 − 120 = 36\n12 × 3 = 36',"Subtract one hundred twenty. Thirty-six remains, which is three more groups of twelve."),
 ('COMBINE','Add the number of groups','10 + 3 = 13\n156 ÷ 12 = 13',"Ten groups plus three groups makes thirteen groups. The quotient is thirteen."),
 ('CHECK','Multiply to check','13 × 12 = 156',"Thirteen times twelve is one hundred fifty-six, with no remainder.")]),
spec('arithmetic-add-decimals','Adding decimals','Find 8.67 + 5.85.','14.52','8.67+5.85','14.52',
 "Find eight point six seven plus five point eight five. Align the decimal points and add by place.",[
 ('MATCH PLACES','Align ones, tenths and hundredths','8.67 + 5.85',
  "Line up the decimal points. Match each place with the same place below it. Add trailing zeros if a number has fewer decimal places."),
 ('HUNDREDTHS','Ten hundredths regroup as one tenth','7 + 5 = 12 hundredths\nWrite 2 hundredths; carry 1 tenth.',
  "Seven plus five is twelve hundredths. Write two in the hundredths place and carry one to the tenths."),
 ('TENTHS','Include the carried tenth','6 + 8 + 1 = 15 tenths\nWrite 5 tenths; carry 1 one.',
  "Add six tenths, eight tenths, and the carried tenth. Fifteen tenths gives five tenths, with one whole carried to the ones."),
 ('ONES AND CHECK','Include the carried one and keep the decimal aligned','8 + 5 + 1 = 14\n8.67 + 5.85 = 14.52\n14.52 − 5.85 = 8.67',
  "Eight plus five plus the carried one is fourteen. The sum is fourteen point five two. Subtract five point eight five to recover the first number and check.")],equalities=[('7+5','12'),('6+8+1','15'),('8+5+1','14'),('14.52-5.85','8.67')]),
spec('arithmetic-subtract-decimals','Subtracting decimals','Find 20 − 8.46.','11.54','20-8.46','11.54',
     "Find twenty minus eight point four six. Line up the decimal points before subtracting.",[
 ('MATCH PLACES','Add trailing zeros to show hundredths','20 = 20.00\n20.00 − 8.46',
  "Write twenty as twenty point zero zero. Trailing zeros do not change its value. Align tens, ones, tenths, and hundredths."),
 ('REGROUP THROUGH ZEROS','Exchange from the next place to the left','20 = 10 + 9 + 0.9 + 0.10',
  "The zero hundredths cannot supply six. Exchange a ten for ten ones, one of those ones for ten tenths, and a tenth for ten hundredths. This leaves one ten, nine ones, nine tenths, and ten hundredths."),
 ('SUBTRACT BY PLACE','Work from right to left','20.00 − 8.46 = 11.54',
  "Ten minus six gives four hundredths. Nine minus four gives five tenths. Nine minus eight leaves one one, and one ten remains. The answer is eleven point five four."),
 ('CHECK','Add the amount removed back to the answer','11.54 + 8.46 = 20.00',
  "Add eight point four six back to eleven point five four. Getting twenty confirms the subtraction.")],equalities=[('10+9+0.9+0.10','20'),('11.54+8.46','20')]),
spec('arithmetic-multiply-decimals','Multiplying decimals','Find 2.4 × 1.7.','4.08','2.4*1.7','4.08',
     "Let's multiply two point four by one point seven. First multiply without the decimal points.",[
 ('MULTIPLY WHOLE NUMBERS','Ignore decimal points briefly','24 × 17 = 408',"Twenty-four times seventeen is four hundred eight."),
 ('COUNT PLACES','One decimal place in each factor','1 + 1 = 2 decimal places',"Each original factor has one decimal place. Together, the product needs two decimal places."),
 ('PLACE THE DECIMAL','Move two places from the right','408 → 4.08',"Place the decimal point two digits from the right. The product is four point zero eight."),
 ('CHECK','Estimate the size','2.4 × 1.7 is between 2.4 and 4.8',"One point seven is between one and two, so the product must be between two point four and four point eight. Four point zero eight fits.")]),
spec('arithmetic-divide-decimals','Dividing decimals','Find 6.72 ÷ 0.8.','8.4','6.72/0.8','8.4',
     "Let's divide six point seven two by zero point eight. Make the divisor a whole number first.",[
 ('SCALE BOTH','Multiply both numbers by 10','6.72 ÷ 0.8 = 67.2 ÷ 8',"Multiply both numbers by ten. This keeps the quotient unchanged and gives sixty-seven point two divided by eight."),
 ('DIVIDE','Break the dividend into useful parts','64 ÷ 8 = 8\n3.2 ÷ 8 = 0.4',"Sixty-four divided by eight is eight. The remaining three point two divided by eight is zero point four."),
 ('COMBINE','Add the two parts','8 + 0.4 = 8.4',"Add eight and zero point four. The quotient is eight point four."),
 ('CHECK','Multiply by the original divisor','8.4 × 0.8 = 6.72',"Multiply eight point four by zero point eight. We get six point seven two, the original dividend.")]),
spec('arithmetic-multiply-integers','Multiplying signed integers','Find (−7) × 9.','−63','-7*9','-63',
     "Let's multiply negative seven by nine. Work out the size and the sign separately.",[
 ('MAGNITUDE','Multiply the positive sizes','7 × 9 = 63',"Seven times nine is sixty-three. That's the magnitude of our answer."),
 ('SIGN','Different signs give a negative','negative × positive = negative',"One factor is negative and one is positive. Different signs make a negative product."),
 ('COMBINE','Attach the negative sign','(−7) × 9 = −63',"Put the sign and magnitude together. Negative seven times nine is negative sixty-three."),
 ('CHECK','Use the inverse operation','−63 ÷ 9 = −7',"Divide negative sixty-three by nine. We recover negative seven.")]),
spec('arithmetic-divide-integers','Dividing signed integers','Find (−96) ÷ (−8).','12','(-96)/(-8)','12',
     "Let's divide negative ninety-six by negative eight. First ignore the signs.",[
 ('MAGNITUDE','Divide the positive sizes','96 ÷ 8 = 12',"Ninety-six divided by eight is twelve."),
 ('SIGN','Matching signs give a positive','negative ÷ negative = positive',"Both numbers are negative. Matching signs give a positive quotient."),
 ('COMBINE','Use the positive quotient','(−96) ÷ (−8) = 12',"The quotient is positive twelve."),
 ('CHECK','Multiply by the divisor','12 × (−8) = −96',"Twelve times negative eight is negative ninety-six. That matches the dividend.")]),
spec('arithmetic-evaluate-powers','Evaluating powers','Find 6³.','216','6**3','216',
     "Let's evaluate six cubed. The exponent tells us how many copies of the base to multiply.",[
 ('EXPAND','Use three factors of 6','6³ = 6 × 6 × 6',"Six cubed means six times six times six. It does not mean six times three."),
 ('MULTIPLY','Multiply the first two factors','6 × 6 = 36',"Six times six is thirty-six."),
 ('FINISH','Multiply by the last factor','36 × 6 = 216',"Thirty-six times six is two hundred sixteen. That's six cubed."),
 ('CHECK','Divide off one factor','216 ÷ 6 = 36 = 6²',"Divide by one factor of six. We get thirty-six, which is six squared.")]),
spec('arithmetic-negative-exponents','Negative exponents','Find 5⁻³.','1/125','5**(-3)','1/125',
     "Let's evaluate five to the power negative three. A negative exponent means take a reciprocal.",[
 ('RECIPROCAL','Move the power to the denominator','5⁻³ = 1 / 5³',"Five to the negative third power is one divided by five cubed. The answer is not a negative number."),
 ('EVALUATE THE POWER','Multiply three copies of 5','5³ = 5 × 5 × 5 = 125',"Five cubed is five times five times five, which is one hundred twenty-five."),
 ('WRITE THE RESULT','Keep the reciprocal','5⁻³ = 1/125',"So five to the negative third power equals one over one hundred twenty-five."),
 ('CHECK','Multiply by the positive power','(1/125) × 125 = 1',"A number times its reciprocal is one. Our answer times one hundred twenty-five gives one.")]),
spec('arithmetic-powers-decimals','Powers of decimals','Find 0.7³.','0.343','0.7**3','0.343',
     "Let's find zero point seven cubed. Multiply three copies of zero point seven.",[
 ('EXPAND','Write the repeated multiplication','0.7³ = 0.7 × 0.7 × 0.7',"The exponent three means there are three factors."),
 ('MULTIPLY DIGITS','Multiply 7 by 7 by 7','7 × 7 × 7 = 343',"Seven times seven times seven is three hundred forty-three."),
 ('PLACE THE DECIMAL','Count three decimal places','343 thousandths = 0.343',"Each factor has one decimal place, so the product has three. The answer is zero point three four three."),
 ('CHECK','Check the size','0 < 0.343 < 0.7 < 1',"Multiplying positive numbers smaller than one makes the result smaller. Zero point three four three has the right size.")]),
spec('arithmetic-powers-signed-numbers','Powers of signed numbers','Find (−4)³.','−64','(-4)**3','-64',
     "Let's evaluate negative four cubed. The parentheses show that the negative sign belongs to the base.",[
 ('EXPAND','Repeat the entire negative base','(−4)³ = (−4) × (−4) × (−4)',"Multiply three copies of negative four."),
 ('MULTIPLY TWO','Two negatives give a positive','(−4) × (−4) = 16',"The first two negative factors multiply to positive sixteen."),
 ('MULTIPLY THE LAST','A positive times a negative is negative','16 × (−4) = −64',"Sixteen times negative four is negative sixty-four."),
 ('CHECK','Check parity and magnitude','Odd power → negative\n4³ = 64',"An odd power of a negative number is negative. The magnitude is four cubed, or sixty-four.")]),
]

SPECS += [
    fraction_spec('arithmetic-add-fractions-like-denominators',['3/13','5/13'],'add'),
    fraction_spec('arithmetic-add-fractions-unlike-denominators',['3/7','2/5'],'add'),
    fraction_spec('arithmetic-subtract-fractions-unlike-denominators',['5/7','2/9'],'subtract'),
    fraction_spec('arithmetic-multiply-fractions',['3/7','5/8'],'multiply'),
    fraction_spec('arithmetic-divide-fractions',['5/9','7/12'],'divide'),
    fraction_spec('arithmetic-add-mixed-numbers',['19/6','17/8'],'add',True),
    fraction_spec('arithmetic-subtract-mixed-numbers',['29/6','13/8'],'subtract',True),
    fraction_spec('arithmetic-multiply-mixed-numbers',['11/4','7/3'],'multiply',True),
    fraction_spec('arithmetic-divide-mixed-numbers',['23/5','13/7'],'divide',True),
    fraction_spec('arithmetic-add-subtract-fractions',['2/5','3/5','1/5'],'add-subtract'),
    fraction_spec('arithmetic-add-subtract-fractions-unlike-denominators',['5/6','3/8','1/4'],'add-subtract'),
    fraction_spec('arithmetic-add-subtract-mixed-numbers',['13/4','7/3','7/5'],'add-subtract',True),
]

SPECS += [
spec('arithmetic-add-subtract-whole-numbers-within-20','Add and subtract','Find 8 + 7 − 6.','9','8+7-6','9',
     "Let's calculate eight plus seven minus six. Addition and subtraction have equal priority.",[
 ('ORDER','Work from left to right','8 + 7 − 6',"With only addition and subtraction, work from left to right."),
 ('ADD','Do the first operation','8 + 7 = 15',"First add eight and seven. That makes fifteen."),
 ('SUBTRACT','Do the next operation','15 − 6 = 9',"Now subtract six from fifteen. The answer is nine."),
 ('CHECK','Reverse the two operations','9 + 6 − 7 = 8',"Undo the subtraction by adding six, then undo the addition by subtracting seven. We return to eight.")]),
spec('arithmetic-add-subtract-whole-numbers-column-method','Add and subtract','Find 384 + 257 − 169.','472','384+257-169','472',
     "Let's add three hundred eighty-four and two hundred fifty-seven, then subtract one hundred sixty-nine.",[
 ('ORDER','Follow the operations from left to right','384 + 257 − 169',"Addition and subtraction have equal priority, so work from left to right."),
 ('ADD','Line up place values','384 + 257 = 641',"Add the first two numbers, regrouping where needed. Their sum is six hundred forty-one."),
 ('SUBTRACT','Regroup and subtract','641 − 169 = 472',"Subtract one hundred sixty-nine from six hundred forty-one. The result is four hundred seventy-two."),
 ('CHECK','Undo both steps','472 + 169 − 257 = 384',"Add back one hundred sixty-nine, then subtract two hundred fifty-seven. You recover the starting number.")]),
spec('arithmetic-missing-number','Missing numbers','Find the missing number: □ + 47 = 93.','46','93-47','46',
     "What number plus forty-seven equals ninety-three? Use the inverse operation to find out.",[
 ('INVERSE','Undo addition with subtraction','□ = 93 − 47',"The unknown has forty-seven added to it. Undo that by subtracting forty-seven from ninety-three."),
 ('SUBTRACT','Regroup the ones','13 − 7 = 6\n8 − 4 = 4',"Regroup ninety-three as eight tens and thirteen ones. Subtract the ones and then the tens."),
 ('SOLVE','Fill the missing value','□ = 46',"The missing number is forty-six."),
 ('CHECK','Put it in the original equation','46 + 47 = 93',"Forty-six plus forty-seven equals ninety-three, so the value fits.")]),
spec('arithmetic-estimation','Estimate a sum','Estimate 396 + 582 to the nearest hundred.','About 1,000','400+600','1000',
     "Let's estimate three hundred ninety-six plus five hundred eighty-two by rounding to the nearest hundred.",[
 ('ROUND FIRST','Round 396 to a hundred','396 ≈ 400',"Three hundred ninety-six is closer to four hundred than to three hundred."),
 ('ROUND SECOND','Round 582 to a hundred','582 ≈ 600',"Five hundred eighty-two rounds to six hundred."),
 ('ADD','Add the rounded numbers','400 + 600 = 1000',"Add four hundred and six hundred. The estimated sum is one thousand."),
 ('CHECK','Compare with the exact sum','396 + 582 = 978\n978 is close to 1000.',"The exact sum is nine hundred seventy-eight, which is close to our estimate. An estimate need not equal the exact answer.")]),
spec('arithmetic-order-operations-whole-numbers','Order of operations','Find 8 + 6 × 7 − 12.','38','8+6*7-12','38',
     "Let's evaluate eight plus six times seven minus twelve. Multiplication comes before addition and subtraction.",[
 ('MULTIPLY','Do multiplication first','6 × 7 = 42',"Multiply six by seven to get forty-two."),
 ('REWRITE','Keep the other operations','8 + 42 − 12',"Replace only the multiplication with forty-two. Keep the addition and subtraction."),
 ('LEFT TO RIGHT','Add, then subtract','8 + 42 = 50\n50 − 12 = 38',"Now work left to right. Eight plus forty-two is fifty; fifty minus twelve is thirty-eight."),
 ('CHECK','Check using an equivalent grouping','42 + (8 − 12) = 42 − 4 = 38',"As a check, eight minus twelve is negative four. Forty-two minus four is still thirty-eight.")]),
spec('arithmetic-order-operations-decimals','Order with decimals','Find 1.8 + 0.6 × 2.5.','3.3','1.8+0.6*2.5','3.3',
     "Let's calculate one point eight plus zero point six times two point five. The usual order of operations still applies.",[
 ('MULTIPLY','Multiply before adding','0.6 × 2.5',"Do the multiplication before the addition."),
 ('DECIMAL PLACES','Calculate the product','6 × 25 = 150\n0.6 × 2.5 = 1.50',"Six times twenty-five is one hundred fifty. With two decimal places, the product is one point five zero."),
 ('ADD','Add the remaining term','1.8 + 1.5 = 3.3',"Add one point eight and one point five. The answer is three point three."),
 ('CHECK','Undo the final addition','3.3 − 1.8 = 1.5',"Subtract one point eight from the answer. We recover the multiplication result, one point five.")]),
spec('arithmetic-order-operations-fractions','Order with fractions','Find 2/3 + (3/4 × 2/5).','29/30','2/3+(3/4*2/5)','29/30',
     "Let's add two thirds to three quarters times two fifths. Start with the multiplication.",[
 ('MULTIPLY','Multiply the two fractions','3/4 × 2/5 = 6/20 = 3/10',"Multiply across. Six twentieths simplifies to three tenths."),
 ('COMMON DENOMINATOR','Use thirtieths for the addition','2/3 = 20/30\n3/10 = 9/30',"Rewrite two thirds as twenty thirtieths and three tenths as nine thirtieths."),
 ('ADD','Add the numerators','20/30 + 9/30 = 29/30',"Twenty plus nine is twenty-nine, so the result is twenty-nine thirtieths."),
 ('CHECK','Subtract to recover the first term','29/30 − 9/30 = 20/30 = 2/3',"Subtract the multiplication result. We get two thirds again.")]),
spec('arithmetic-order-operations-integers','Order with signed integers','Find −5 + 3 × (−4) − (−8).','−9','-5+3*(-4)-(-8)','-9',
     "Let's calculate with negative numbers. First do the multiplication, then handle the remaining signs.",[
 ('MULTIPLY','Multiply before adding or subtracting','3 × (−4) = −12',"Three times negative four is negative twelve."),
 ('REWRITE','Subtracting a negative means adding','−5 − 12 + 8',"Subtracting negative eight is the same as adding positive eight."),
 ('COMBINE','Work from left to right','−5 − 12 = −17\n−17 + 8 = −9',"Negative five minus twelve is negative seventeen. Adding eight gives negative nine."),
 ('CHECK','Group positives and negatives','8 − (5 + 12) = 8 − 17 = −9',"The positives total eight and the negative magnitudes total seventeen. Eight minus seventeen confirms negative nine.")]),
spec('arithmetic-order-operations-with-powers','Order with powers','Find 3² + 4 × (7 − 2).','29','3**2+4*(7-2)','29',
     "Let's evaluate three squared plus four times the quantity seven minus two. Follow the order of operations.",[
 ('GROUPING','Work inside parentheses','7 − 2 = 5\n3² + 4 × 5',"First subtract inside the parentheses. Seven minus two is five."),
 ('POWER','Evaluate the exponent','3² = 9\n9 + 4 × 5',"Three squared is nine. Replace the power with nine."),
 ('MULTIPLY THEN ADD','Finish in the correct order','4 × 5 = 20\n9 + 20 = 29',"Four times five is twenty. Add nine to get twenty-nine."),
 ('CHECK','Use distribution to check','9 + 28 − 8 = 29',"Distribute four across the original parentheses: four times seven minus four times two. Nine plus twenty-eight minus eight is twenty-nine.")]),
]


def draw_decimal_subtraction(d,scene,p):
    from card_lessons import draw_card
    import generate_sample_videos as video
    item=next(s for s in SPECS if s['video_id']=='arithmetic-subtract-decimals')
    if scene not in (2,3):return draw_card(item,d,scene,p)
    d.rounded_rectangle((145,360,1775,840),radius=35,fill='white')
    video.centered(d,386,'Regrouped 20.00: the value stays the same',32,video.MUTED)
    for i,(label,top,bottom,answer) in enumerate(zip(['Tens','Ones','Tenths','Hundredths'],[1,9,9,10],[0,8,4,6],[1,1,5,4])):
        x=600+260*i
        d.text((x,462),label,font=video.font(32,True),fill=video.MUTED,anchor='mm')
        d.text((x,540),str(top),font=video.font(68,True),fill=video.INK,anchor='mm')
        if scene==3:
            d.text((x,634),str(bottom),font=video.font(68,True),fill=video.INK,anchor='mm')
            d.text((x,760),str(answer),font=video.font(68,True),fill=video.TEAL,anchor='mm')
    if scene==2:video.centered(d,705,'10 + 9 + 0.9 + 0.10 = 20.00',52,video.TEAL,True)
    else:
        d.text((360,634),'−',font=video.font(68,True),fill=video.INK,anchor='mm')
        d.line((465,686,1530,686),fill=video.MUTED,width=3)
        for y in [540,634,760]:d.text((990,y),'.',font=video.font(68,True),fill=video.TEAL if y==760 else video.INK,anchor='mm')

def draw_decimal_addition(d,scene,p):
    from card_lessons import draw_card
    import generate_sample_videos as video
    item=next(s for s in SPECS if s['video_id']=='arithmetic-add-decimals')
    if scene!=1:return draw_card(item,d,scene,p)
    d.rounded_rectangle((145,360,1775,840),radius=35,fill='white')
    for x,label in [(650,'Ones'),(1030,'Tenths'),(1360,'Hundredths')]:
        d.text((x,452),label,font=video.font(38,True),fill=video.MUTED,anchor='mm')
    for y,values in [(550,['8','.','6','7']),(690,['5','.','8','5'])]:
        for x,c in zip([650,840,1030,1360],values):
            d.text((x,y),c,font=video.font(82,True),fill=video.INK,anchor='mm')
    d.text((390,690),'+',font=video.font(65,True),fill=video.INK,anchor='mm')
    d.line((535,760,1460,760),fill=video.MUTED,width=3)

def lessons(doc):
    import generate_sample_videos as video
    result=make_lessons(SPECS,doc)
    video.DRAW['arithmetic-subtract-decimals']=draw_decimal_subtraction
    video.DRAW['arithmetic-add-decimals']=draw_decimal_addition
    return result
