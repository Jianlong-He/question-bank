"""Prime decomposition, synchronized events, and constructed Bezout identities."""
from algebra_lessons import authored
from number_theory_lessons import source
from card_lessons import make_lessons

def p(w,q):return source('prime-factorization',w,q)
def r(w,q):return source('number-theory1_review',w,q)
SPECS=[
authored('number-theory-prime-decomposition','Build a prime factorization and collect repeated factors',
 'Find the prime factorization of 264.\nWrite repeated primes using exponents.','2³ × 3 × 11',
 'Find the prime factorization of two hundred sixty-four. Write repeated primes using exponents.',[
 ('DIVIDE BY THE SMALLEST PRIME','Keep dividing by two while the result is even','264 = 2 × 132\n132 = 2 × 66; 66 = 2 × 33',
 'Start with two. Two hundred sixty-four divides to one hundred thirty-two, then sixty-six, then thirty-three. We have three factors of two.'),
 ('FACTOR THE ODD PART','Try the next small prime','33 = 3 × 11\nBoth 3 and 11 are prime.',
 'The remaining odd number is thirty-three. It factors as three times eleven, and both factors are prime.'),
 ('COLLECT EQUAL FACTORS','An exponent counts how often a prime occurs','264 = 2 × 2 × 2 × 3 × 11\n= 2³ × 3 × 11',
 'Combine the three twos into two cubed. The prime factorization is two cubed times three times eleven.'),
 ('MULTIPLY BACK TO CHECK','The factors must all be prime and recover the original','2³ × 3 × 11 = 8 × 33 = 264',
 'Check by multiplying back. Eight times thirty-three is two hundred sixty-four. Every factor is prime, so the factorization is complete.')],p(1,2),expression='2**3*3*11',value='264'),
authored('number-theory-synchronized-events','Use an LCM for the next simultaneous event',
 'Two runners take 24 and 36 minutes per lap.\nThey leave the starting line together at 8:25 AM.\nWhen are they next together at the starting line?','72 minutes later; 9:37 AM',
 'Two runners take twenty-four and thirty-six minutes per lap. They leave the starting line together at eight twenty-five A M. When are they next together at the starting line?',[
 ('MODEL BOTH RETURNS','The elapsed time must be a multiple of each lap time','Runner A: 24, 48, 72, … minutes\nRunner B: 36, 72, 108, … minutes',
 'Each runner returns at multiples of their own lap time. We need the first positive time appearing in both lists.'),
 ('FIND THE LEAST COMMON MULTIPLE','Use the largest prime powers in either number','24 = 2³ × 3; 36 = 2² × 3²\nLCM = 2³ × 3² = 72 minutes',
 'Factor the lap times. The least common multiple uses two cubed and three squared, giving seventy-two minutes.'),
 ('CHECK WHOLE NUMBERS OF LAPS','Both runners must finish a complete lap','72 ÷ 24 = 3 laps; 72 ÷ 36 = 2 laps',
 'In seventy-two minutes, the runners complete three and two laps. Both are at the starting line.'),
 ('ADD THE ELAPSED TIME','Convert minutes before reading the clock','72 minutes = 1 hour 12 minutes\n8:25 AM + 1:12 = 9:37 AM',
 'Seventy-two minutes is one hour twelve minutes. Add that to eight twenty-five A M to get nine thirty-seven A M.')],p(4,10),equalities=[('2**3*3**2','72'),('72/24','3'),('72/36','2'),('8*60+25+72','9*60+37')]),
authored('number-theory-build-bezout-signs','Find Bezout coefficients and adjust their signs',
 'Solve 7x + 11y = 1 with integers.\nGive a solution with y > 0 and one with x > 0,\nthen find the inverse of 7 modulo 11.','(-3,2); (8,-5); inverse 8',
 'Solve seven x plus eleven y equals one with integers. Give a solution with positive y, another with positive x, and the inverse of seven modulo eleven.',[
 ('RUN EUCLID','Divide until the remainder reaches one','11 = 7 + 4; 7 = 4 + 3; 4 = 3 + 1',
 'Euclidean division gives remainders four, three, and one. Now reverse those equations.'),
 ('SUBSTITUTE BACKWARD','Write one using the two original numbers','1 = 4 − 3 = 4 − (7 − 4)\n= 2(11 − 7) − 7 = 2 × 11 − 3 × 7',
 'One is four minus three. Replace three with seven minus four, then replace four with eleven minus seven. This gives twice eleven minus three times seven.'),
 ('ADJUST THE SIGNS','Adding eleven to x and subtracting seven from y preserves one','x=−3, y=2 gives y>0.\nx=−3+11=8, y=2−7=−5 gives x>0.',
 'Negative three and two give positive y. Add eleven to x and subtract seven from y to get eight and negative five, giving positive x.'),
 ('READ AND CHECK THE INVERSE','Modulo eleven, the multiple of eleven disappears','7 × 8 + 11(−5) = 56 − 55 = 1\n7 × 8 ≡ 1 (mod 11): inverse 8',
 'The new coefficients give fifty-six minus fifty-five equals one. Modulo eleven, seven times eight is one, so eight is the inverse.')],r(1,10),equalities=[('11*2-7*3','1'),('7*8+11*(-5)','1'),('7*8%11','1')]),
]
def lessons(doc):return make_lessons(SPECS,doc)
