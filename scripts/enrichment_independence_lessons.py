"""Independence, complements, and conditional systems with fresh inputs."""
from fractions import Fraction as F
from itertools import product
from algebra_lessons import authored
from probability_lessons import enrichment
from card_lessons import make_lessons

def e(w,q):return enrichment('conditional-probability',w,q)
SPECS=[
authored('probability-independent-union-neither','Independent events: either and neither',
 'Independent events have P(A) = 0.35 and P(B) = 0.60.\nFind P(A or B) and P(neither).','0.74 either; 0.26 neither',
 'Independent events A and B have probabilities zero point three five and zero point six. Find the probability of either event and of neither.',[
 ('FIND THE OVERLAP','Independence lets us multiply','P(both) = 0.35 × 0.60 = 0.21',
 'Independence lets us multiply the probabilities. The overlap is zero point two one.'),
 ('COUNT EITHER EVENT','Or includes the overlap once','P(A or B) = 0.35 + 0.60 − 0.21 = 0.74',
 'Add the event probabilities and subtract the overlap. Either event occurs with probability zero point seven four.'),
 ('COUNT NEITHER','Neither is the complement of the union','P(neither) = 1 − 0.74 = 0.26',
 'Neither is the complement, so subtract from one. The result is zero point two six.'),
 ('CHECK WITH COMPLEMENTS','Complements of independent events are independent','P(neither) = (1 − 0.35)(1 − 0.60)\n= 0.65 × 0.40 = 0.26',
 'As a check, multiply the two complement probabilities. Zero point six five times zero point four also gives zero point two six.')],e(5,3),expression='.35+.60-.35*.60',value='.74',equalities=[('.65*.4','.26')]),
authored('probability-exactly-one-independent','Exactly one of two independent events',
 'Two independent sensors fail with probabilities\n0.12 and 0.18. Find P(exactly one fails).','0.2568',
 'Two independent sensors fail with probabilities zero point one two and zero point one eight. Find the probability that exactly one fails.',[
 ('FIRST FAILS, SECOND WORKS','Use the complement for the working sensor','0.12 × (1 − 0.18) = 0.0984',
 'If the first fails and the second works, multiply zero point one two by zero point eight two.'),
 ('FIRST WORKS, SECOND FAILS','Include the other possible order','(1 − 0.12) × 0.18 = 0.1584',
 'For the other order, multiply zero point eight eight by zero point one eight.'),
 ('ADD DISJOINT CASES','The two orders cannot happen together','0.0984 + 0.1584 = 0.2568',
 'These cases are disjoint. Add their probabilities to get zero point two five six eight.'),
 ('GENERAL RULE','Allow different probabilities for the two events','p(1 − q) + (1 − p)q\nIf p = q, this becomes 2p(1 − p).',
 'The general formula is p times one minus q, plus one minus p times q. For equal probabilities, it simplifies to twice p times one minus p.')],e('5HW',5),expression='.12*.82+.88*.18',value='.2568'),
authored('probability-test-independence','Check independence using the intersection',
 'Choose an integer uniformly from 1 through 16.\nA: the number is even. B: it is divisible by 4.\nAre A and B independent?','No',
 'Choose an integer uniformly from one through sixteen. A means even, and B means divisible by four. Are the events independent?',[
 ('COUNT EACH EVENT','Use the same sample space for all probabilities','P(A) = 8/16 = 1/2\nP(B) = 4/16 = 1/4',
 'Eight numbers are even, and four are divisible by four. Their probabilities are one half and one quarter.'),
 ('COUNT THE INTERSECTION','Find outcomes satisfying both conditions','Both: {4,8,12,16}\nP(A and B) = 4/16 = 1/4',
 'Every multiple of four is even. The intersection contains four numbers, so its probability is one quarter.'),
 ('COMPARE WITH THE PRODUCT','Independence requires equality','P(A)P(B) = (1/2)(1/4) = 1/8\n1/4 ≠ 1/8 → not independent',
 'The product is one eighth, which differs from one quarter. The events are not independent.'),
 ('GENERAL TEST','Count the intersection instead of assuming independence','Independent exactly when P(A and B) = P(A)P(B)',
 'In general, count the intersection from the actual outcomes. Equality with the product means independence; inequality means dependence.')],e(5,7),expression='(1/2)*(1/4)',value='1/8'),
authored('probability-pairwise-not-mutual','Pairwise independence does not imply mutual independence',
 'Roll two independent fair six-sided dice.\nA: first is odd. B: second is even. C: sum is odd.\nFind P(A and B and C).','1/4',
 'Roll two independent fair six-sided dice. A means the first is odd, B means the second is even, and C means the sum is odd. Find the probability of all three.',[
 ('USE PARITY CASES','Four parity pairs are equally likely','odd–odd, odd–even, even–odd, even–even\nEach has probability 1/4.',
 'The four parity pairs are equally likely. Each has probability one quarter.'),
 ('FIND THE COMMON OUTCOME','Odd plus even is already odd','A and B force odd–even.\nC then holds automatically.\nP(A and B and C) = 1/4',
 'A and B force odd then even. Their sum is already odd, so C adds no new restriction. The answer is one quarter.'),
 ('CHECK PAIRS','Each pair has intersection probability one quarter','P(A) = P(B) = P(C) = 1/2\nEvery pair: P(intersection) = 1/4',
 'Each event has probability one half, and each pair has intersection probability one quarter. The events are pairwise independent.'),
 ('CHECK ALL THREE','Mutual independence also requires the triple condition','P(A)P(B)P(C) = 1/8\nActual triple probability: 1/4',
 'Multiplying all three gives one eighth, not one quarter. Pairwise independence alone does not justify multiplying three probabilities.')],e(5,6),expression='9/36',value='1/4'),
authored('probability-working-system-condition','A working component given that the system works',
 'Four independent units each work with probability 0.60.\nThe system works if at least one works. Given that\nthe system works, find P(the first unit works).','125/203',
 'Four independent units each work with probability zero point six. The system works if at least one works. Given that the system works, find the chance the first unit works.',[
 ('SYSTEM FAILURE','Every unit must fail','P(all fail) = 0.40⁴ = 0.0256',
 'The system fails only when all four units fail. Multiply four failure probabilities to get zero point zero two five six.'),
 ('SYSTEM SUCCESS','Take the complement','P(system works) = 1 − 0.0256 = 0.9744',
 'Subtract from one. The system works with probability zero point nine seven four four.'),
 ('FIND THE INTERSECTION','First unit working guarantees system success','P(first works and system works) = 0.60',
 'If the first unit works, the system must work. So their intersection has probability zero point six.'),
 ('CONDITION','Divide by the probability of the given event','P(first works | system works)\n= 0.60/0.9744 = 125/203',
 'Divide by the probability that the system works. The conditional answer is one hundred twenty-five over two hundred three.')],e(5,8),expression='.60/(1-.40**4)',value='125/203'),
authored('probability-independent-missing-chance','Recover a missing probability from an independent union',
 'A and B are independent.\nP(A or B) = 0.82 and P(not A) = 0.40.\nFind P(B).','0.55',
 'A and B are independent. Their union has probability zero point eight two, and not A has probability zero point four. Find the probability of B.',[
 ('FIND NEITHER','The complement of A or B is neither','P(neither) = 1 − 0.82 = 0.18',
 'First find the probability of neither event. It is one minus zero point eight two, or zero point one eight.'),
 ('USE INDEPENDENCE','Complement probabilities multiply','0.18 = P(not A)P(not B)\n0.18 = 0.40 × P(not B)',
 'Because the events are independent, their complements are independent too. Multiply not A by not B to get neither.'),
 ('DIVIDE','Recover the complement of the unknown probability','P(not B) = 0.18/0.40 = 0.45',
 'Divide zero point one eight by zero point four. Not B has probability zero point four five.'),
 ('COMPLEMENT AGAIN','The question asks for B','P(B) = 1 − 0.45 = 0.55',
 'Finally subtract from one. B has probability zero point five five.')],e(5,9),expression='1-(1-.82)/.4',value='.55'),
authored('probability-at-least-one-working','At least one works with unequal failure probabilities',
 'Two independent alarms fail with probabilities\n0.10 and 0.15. Find P(at least one works).','0.985',
 'Two independent alarms fail with probabilities zero point one and zero point one five. Find the probability that at least one works.',[
 ('CHOOSE THE COMPLEMENT','Neither works means both fail','At least one works ↔ not both fail',
 'The opposite of at least one working is both failing.'),
 ('MULTIPLY FAILURE PROBABILITIES','Independence applies to the two failures','P(both fail) = 0.10 × 0.15 = 0.015',
 'The failures are independent, so multiply their probabilities. Both fail with probability zero point zero one five.'),
 ('SUBTRACT FROM ONE','Include one working or both working','P(at least one works) = 1 − 0.015 = 0.985',
 'Subtract from one. The probability of at least one working is zero point nine eight five.'),
 ('GENERAL RULE','For independent units, multiply all failure probabilities','P(at least one works) = 1 − P(all fail)',
 'This method includes the case where both work. With more independent units, multiply every failure probability before subtracting from one.')],e(5,10),expression='1-.10*.15',value='.985'),
]

def lessons(doc):
 pairs=list(product(range(1,7),repeat=2))
 A={x for x in pairs if x[0]%2==1};B={x for x in pairs if x[1]%2==0};C={x for x in pairs if sum(x)%2==1}
 assert [len(A&B),len(A&C),len(B&C),len(A&B&C)]==[9]*4
 assert F(3,5)/(1-F(2,5)**4)==F(125,203)
 return make_lessons(SPECS,doc)
