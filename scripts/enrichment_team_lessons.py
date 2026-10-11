"""Labelled team assignments and shared-team probabilities."""
from fractions import Fraction as F
from math import comb
from algebra_lessons import authored
from probability_lessons import enrichment
from card_lessons import make_lessons

def e(w,q):return enrichment('conditional-probability',w,q)
SPECS=[
authored('counting-labelled-teams','Divide people into labelled teams',
 'Divide 9 students into labelled teams A, B, C\nof sizes 2, 3, 4. How many divisions are possible?','1260',
 'Divide nine students into labelled teams A, B, and C of sizes two, three, and four. How many divisions are possible?',[
 ('CHOOSE TEAM A','Order within a team does not matter','C(9,2) = 36',
 'Choose two of nine students for team A. There are thirty-six choices.'),
 ('CHOOSE TEAM B','Use only the students who remain','C(7,3) = 35',
 'Seven students remain. Choose three of them for team B in thirty-five ways.'),
 ('THE LAST TEAM IS FORCED','All four remaining students form team C','36 × 35 × 1 = 1,260',
 'The remaining four form team C. Multiply thirty-six by thirty-five to get one thousand two hundred sixty.'),
 ('RESPECT LABELS','Do not divide by the number of team orders','For two labelled teams, choose the first;\nthe second is already determined.',
 'Team labels matter, even when some sizes are equal. For two labelled teams, choosing the first already determines the second.')],e(6,1),expression='36*35',value='1260'),
authored('counting-team-fixed-pair','Team divisions with two required members',
 'Divide 10 students into labelled teams A, B, C\nof sizes 4, 2, 4. Ira and Bo must be on A.\nHow many divisions are possible?','420',
 'Divide ten students into labelled teams A, B, and C of sizes four, two, and four. Ira and Bo must be on A. How many divisions are possible?',[
 ('FIX REQUIRED MEMBERS','Ira and Bo occupy two places on A','Team A needs 2 more; 8 students are available.',
 'Put Ira and Bo on A first. Two places remain on A, and eight students are available.'),
 ('COMPLETE TEAM A','Choose its other two members','C(8,2) = 28',
 'Choose the other two A members from eight students, giving twenty-eight choices.'),
 ('CHOOSE TEAM B','The final team is determined','C(6,2) = 15 choices for B\nThe remaining 4 form C.',
 'Choose two of the remaining six for B in fifteen ways. The remaining four form C.'),
 ('MULTIPLY','Each sequence creates exactly one labelled division','28 × 15 = 420',
 'Multiply to get four hundred twenty divisions. Fixed people use team places, but are not chosen again.')],e(6,8),expression='28*15',value='420'),
authored('counting-teams-multiple-reservations','Reserve required members on different teams',
 'Divide 11 students into labelled teams A, B, C\nof sizes 4, 3, 4. Jo and Lee must be on A;\nPaz must be on B. How many divisions are possible?','420',
 'Divide eleven students into labelled teams A, B, and C of sizes four, three, and four. Jo and Lee must be on A, and Paz on B. Count the divisions.',[
 ('RESERVE EVERY FIXED PERSON','Paz must be kept out of the pool for A','3 people fixed; 8 unassigned students\nA needs 2, B needs 2, C needs 4.',
 'Reserve all three people before choosing anyone else. Eight are unassigned, with two open places on A and two on B.'),
 ('FILL THE OPEN A PLACES','Choose from the eight unassigned students','C(8,2) = 28',
 'Choose two of the eight unassigned students to finish A. There are twenty-eight choices.'),
 ('FILL THE OPEN B PLACES','Paz is already on B','C(6,2) = 15\nThe remaining four form C.',
 'Paz already occupies one B place. Choose two of the six remaining students for its other places. The last four form C.'),
 ('MULTIPLY','Do not allow a reserved person onto another team','28 × 15 = 420',
 'Multiply twenty-eight by fifteen to get four hundred twenty. Reserving everyone first prevents assigning a required member to the wrong team.')],e(6,7),expression='28*15',value='420'),
authored('probability-same-different-teams','Two people on the same or different teams',
 'Assign 11 students uniformly to labelled teams\nof sizes 2, 3, 6. Find the probability that two named\nstudents are on the same team, and on different teams.','19/55 same; 36/55 different',
 'Assign eleven students uniformly to labelled teams of sizes two, three, and six. Find the probability two named students are on the same team, and on different teams.',[
 ('COUNT POSITION PAIRS','The two students occupy an equally likely pair of positions','All position pairs: C(11,2) = 55',
 'Think of fixed team positions. The two named students occupy any pair of eleven positions with equal probability. There are fifty-five pairs.'),
 ('COUNT SAME-TEAM PAIRS','A pair must be entirely inside one team','C(2,2) + C(3,2) + C(6,2)\n= 1 + 3 + 15 = 19',
 'Count pairs within each team and add. The counts one, three, and fifteen give nineteen favourable pairs.'),
 ('SAME OR DIFFERENT','Different teams is the complement','P(same) = 19/55\nP(different) = 1 − 19/55 = 36/55',
 'The same-team probability is nineteen fifty-fifths. Subtract from one for different teams: thirty-six fifty-fifths.'),
 ('EQUAL TEAM SHORTCUT','After placing one person, count matching open positions','If every team has size s among n people:\nP(same) = (s−1)/(n−1)',
 'When all team sizes are equal, place one person first. Then s minus one of the n minus one open positions are on that same team.')],e(6,3),expression='(1+3+15)/55',value='19/55'),
authored('probability-group-all-same-team','Several named people all on one team',
 'Assign 15 students uniformly to three labelled teams\nof size 5. Find the probability that three named\nstudents are all on the same team.','6/91',
 'Assign fifteen students uniformly to three labelled teams of size five. Find the probability that three named students are all on the same team.',[
 ('COUNT ALL POSITION SETS','Choose positions for the three named students','C(15,3) = 455',
 'The three named students occupy an equally likely set of three positions. There are four hundred fifty-five such sets.'),
 ('COUNT SETS WITHIN A TEAM','Any of the three teams can contain all three','3 × C(5,3) = 3 × 10 = 30',
 'Each team contains ten sets of three positions. Any of the three teams works, giving thirty favourable sets.'),
 ('DIVIDE','Use favourable sets over all sets','30/455 = 6/91',
 'Divide thirty by four hundred fifty-five. The probability simplifies to six ninety-firsts.'),
 ('EXTEND TO k NAMED PEOPLE','Add the within-team counts and divide by all position sets','P(all together)\n= [C(s1,k) + C(s2,k) + …] / C(n,k)',
 'For k named people, count k positions inside each team, add those counts, and divide by n choose k. A team smaller than k contributes zero.')],e('6HW',4),expression='30/455',value='6/91'),
]

def lessons(doc):
 assert comb(9,2)*comb(7,3)==1260
 assert comb(8,2)*comb(6,2)==420
 assert F(sum(comb(s,2) for s in [2,3,6]),comb(11,2))==F(19,55)
 assert F(3*comb(5,3),comb(15,3))==F(6,91)
 return make_lessons(SPECS,doc)
