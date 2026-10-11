"""New, exactly checked enrichment examples; never worksheet answer recordings."""
from math import gcd
from algebra_lessons import authored
from card_lessons import make_lessons


def source(topic, worksheet, qid):
    unit = {'modular-arithmetic': 1, 'prime-factorization': 2,
            'Euclidean-division': 3, 'number-theory1_review': 4, 'CRT': 5, 'RSA': 6}[topic]
    return (f'worksheets/enrichment/number-theory 1/U{unit}{topic}/E-NT1U{unit}W{worksheet}.csv',str(qid))


SPECS = [
authored('number-theory-euclidean-algorithm', 'Euclid and fraction simplification',
 'Simplify 414/690\nusing the Euclidean algorithm.', '3/5',
 "Let's simplify four hundred fourteen over six hundred ninety using the Euclidean algorithm to find the greatest common divisor.", [
 ('DIVIDE', 'Divide the larger number by the smaller', '690 = 1 × 414 + 276',
  'Six hundred ninety is one times four hundred fourteen, plus a remainder of two hundred seventy-six.'),
 ('REPEAT', 'Use the previous divisor and remainder', '414 = 1 × 276 + 138\n276 = 2 × 138 + 0',
  'Repeat. Four hundred fourteen leaves remainder one hundred thirty-eight. The next division has remainder zero.'),
 ('GREATEST COMMON DIVISOR', 'Take the last nonzero remainder', 'gcd(414, 690) = 138',
  'The last nonzero remainder is one hundred thirty-eight. That is the greatest common divisor.'),
 ('SIMPLIFY', 'Divide numerator and denominator by 138', '(414 ÷ 138)/(690 ÷ 138) = 3/5',
  'Divide the numerator and denominator by one hundred thirty-eight. The simplified fraction is three fifths.')],
 source('Euclidean-division',2,6),expression='414/690',value='3/5',
 equalities=[('690','414+276'),('414','276+138'),('276','2*138'),('414/138','3'),('690/138','5')]),

authored('number-theory-euler-totient', 'Euler’s totient function',
 'Find ϕ(45).', '24',
 "Let's find phi of forty-five. It counts the positive integers less than forty-five that are coprime to forty-five.", [
 ('FACTOR', 'Find the distinct prime factors', '45 = 3² × 5\nDistinct primes: 3 and 5',
  'Forty-five factors as three squared times five. Its distinct prime factors are three and five.'),
 ('FORMULA', 'Use each distinct prime once', 'ϕ(45) = 45(1 − 1/3)(1 − 1/5)',
  'Multiply forty-five by one minus one third, then by one minus one fifth. Use each distinct prime only once.'),
 ('CALCULATE', 'Simplify the factors', '45 × (2/3) × (4/5)\n= 30 × (4/5) = 24',
  'Forty-five times two thirds is thirty. Thirty times four fifths is twenty-four.'),
 ('ANSWER', 'Interpret the count', 'ϕ(45) = 24',
  'There are twenty-four positive integers below forty-five with no common factor with forty-five other than one.')],
 source('RSA',2,6),expression='45*(1-1/3)*(1-1/5)',value='24'),

authored('number-theory-modular-inverse', 'Finding a modular inverse',
 'Find the inverse of 11 (mod 26).', '19 modulo 26',
 "Let's find the inverse of eleven modulo twenty-six. We need a multiplier that gives remainder one.", [
 ('EUCLIDEAN ALGORITHM', 'Find a greatest common divisor of 1', '26 = 2 × 11 + 4\n11 = 2 × 4 + 3\n4 = 1 × 3 + 1',
  'Use the Euclidean algorithm. The remainders are four, three, and one, so an inverse exists.'),
 ('BACK SUBSTITUTE', 'Write 1 using 26 and 11', '1 = 4 − 3 = 3 × 4 − 11\n= 3 × 26 − 7 × 11',
  'Substitute backwards. One equals three times twenty-six minus seven times eleven. So negative seven is an inverse.'),
 ('POSITIVE REPRESENTATIVE', 'Add the modulus to −7', '−7 + 26 = 19',
  'Add twenty-six to negative seven to get the positive representative, nineteen.'),
 ('CHECK', 'The product leaves remainder 1', '11 × 19 = 209 = 8 × 26 + 1\n11 × 19 ≡ 1 (mod 26)',
  'Eleven times nineteen is two hundred nine, which leaves remainder one when divided by twenty-six.')],
 source('modular-arithmetic',3,8),expression='(-7)%26',value='19',
 equalities=[('26','2*11+4'),('11','2*4+3'),('4','3+1'),('3*26-7*11','1'),('(11*19)%26','1')]),

authored('number-theory-modular-multiplication', 'Multiplying modulo a number',
 'Find 17 × 14 (mod 9).', '4',
 "Let's find seventeen times fourteen modulo nine. Reduce the factors first to keep the arithmetic small.", [
 ('REDUCE THE FACTORS', 'Replace each factor by its remainder', '17 ≡ 8 (mod 9)\n14 ≡ 5 (mod 9)',
  'Seventeen leaves remainder eight when divided by nine. Fourteen leaves remainder five.'),
 ('MULTIPLY', 'Multiply the reduced factors', '8 × 5 = 40',
  'Multiply the remainders. Eight times five is forty.'),
 ('REDUCE AGAIN', 'Keep the final remainder', '40 = 4 × 9 + 4\n17 × 14 ≡ 4 (mod 9)',
  'Forty is four times nine plus four, so the result is four modulo nine.'),
 ('CHECK', 'Check the original product', '17 × 14 = 238 = 26 × 9 + 4',
  'The original product is two hundred thirty-eight. Dividing by nine also leaves remainder four.')],
 source('modular-arithmetic',2,1),expression='(17*14)%9',value='4',
 equalities=[('17%9','8'),('14%9','5'),('40%9','4'),('17*14','26*9+4')]),

authored('number-theory-rsa-encryption', 'A small RSA encryption example',
 'Encrypt M = 7\nwith public key n = 55, e = 3.', 'C = 13',
 "Let's encrypt the message seven in a small RSA example. The public modulus is fifty-five and the public exponent is three.", [
 ('MESSAGE RANGE', 'The message must be below the modulus', '0 ≤ 7 < 55',
  'Seven is between zero and fifty-four, so it is in the allowed message range.'),
 ('ENCRYPTION RULE', 'Raise the message to the public exponent', 'C = Mᵉ mod n\nC = 7³ mod 55',
  'The ciphertext is the message raised to the public exponent, reduced modulo the modulus.'),
 ('COMPUTE', 'Evaluate the power and divide', '7³ = 343\n343 = 6 × 55 + 13',
  'Seven cubed is three hundred forty-three. Six copies of fifty-five leave a remainder of thirteen.'),
 ('CIPHERTEXT', 'Keep the remainder', 'C = 13\n0 ≤ 13 < 55',
  'The ciphertext is thirteen. It is also within the required range, from zero up to fifty-four.')],
 source('RSA',6,2),expression='7**3%55',value='13',
 equalities=[('7**3','343'),('343','6*55+13')]),
]


def lessons(doc):
    assert gcd(414,690)==138
    assert sum(gcd(i,45)==1 for i in range(1,45))==24
    assert pow(11,-1,26)==19
    assert gcd(3,(5-1)*(11-1))==1
    assert pow(pow(7,3,55),pow(3,-1,40),55)==7
    return make_lessons(SPECS,doc)
