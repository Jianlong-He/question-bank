"""Original early arithmetic stories that need distinct interpretation steps."""
from algebra_lessons import authored
from card_lessons import make_lessons
from number_sense_lessons import source

def g(w,q):return source(2,4,w,q)
SPECS=[
authored('story-remaining-weekly-capacity','Find remaining capacity after linked daily amounts',
 'A club can pack 240 meals this week.\nMonday: 54 meals. Tuesday: 12 more than Monday.\nWednesday: 18 fewer than Tuesday.\nHow many more meals can it pack this week?','72 meals',
 'A club can pack two hundred forty meals this week. It packs fifty-four on Monday, twelve more on Tuesday, and eighteen fewer than Tuesday on Wednesday. Find the remaining capacity.',[
 ('FIND TUESDAY','More than Monday means add twelve','54 + 12 = 66 meals',
 'Tuesday is twelve more than Monday, so fifty-four plus twelve gives sixty-six meals.'),
 ('FIND WEDNESDAY','Compare Wednesday with Tuesday','66 − 18 = 48 meals',
 'Wednesday is eighteen fewer than Tuesday. Subtract eighteen from sixty-six to get forty-eight.'),
 ('TOTAL ALL THREE DAYS','Include every day once','54 + 66 + 48 = 168 meals',
 'Add all three days: fifty-four plus sixty-six is one hundred twenty. Add forty-eight to get one hundred sixty-eight.'),
 ('SUBTRACT FROM CAPACITY','The unused part is still available','240 − 168 = 72 meals',
 'Subtract one hundred sixty-eight from the capacity of two hundred forty. The club can pack seventy-two more meals.')],g('1Rev',5),expression='240-(54+(54+12)+(54+12-18))',value='72',equalities=[('54+12','66'),('66-18','48'),('54+66+48','168')]),
authored('story-change-two-groups','Track changes to two groups before finding the total',
 'A shelter has 32 cats and 28 dogs.\nFourteen cats leave and 9 dogs arrive.\nHow many animals are there now?','55 animals',
 'A shelter has thirty-two cats and twenty-eight dogs. Fourteen cats leave and nine dogs arrive. How many animals are there now?',[
 ('UPDATE THE CATS','Only the cats are affected by this change','32 − 14 = 18 cats',
 'First update the cats. Fourteen leave, so thirty-two minus fourteen is eighteen cats.'),
 ('UPDATE THE DOGS','Only the dogs are affected by this change','28 + 9 = 37 dogs',
 'Now update the dogs. Nine arrive, so twenty-eight plus nine is thirty-seven dogs.'),
 ('COMBINE THE NEW COUNTS','Add the groups after their changes','18 + 37 = 55 animals',
 'Add the new counts: eighteen cats plus thirty-seven dogs equals fifty-five animals.'),
 ('CHECK USING THE ORIGINAL TOTAL','Apply each change exactly once','32 + 28 = 60\n60 − 14 + 9 = 55',
 'Check from the original sixty animals. Fourteen leave and nine arrive, giving fifty-five again.')],g('1Rev',3),expression='32-14+28+9',value='55'),
authored('story-ignore-no-count-change','Decide which events change the number of objects',
 'A library has 48 books. It receives 16 more.\nA helper cleans 12 books and returns them to the shelf.\nHow many books does the library have?','64 books',
 'A library has forty-eight books and receives sixteen more. A helper cleans twelve books and returns them to the shelf. How many books does the library have?',[
 ('IDENTIFY THE NEW BOOKS','Receiving books increases the count','48 + 16',
 'The sixteen new books increase the number in the library, so add them.'),
 ('CHECK WHAT CLEANING DOES','The cleaned books stay in the library','Cleaning changes condition, not quantity.',
 'Cleaning a book does not remove it from the library. The same twelve books are returned to the shelf.'),
 ('CALCULATE THE ACTUAL CHANGE','Only the delivery changes the count','48 + 16 = 64',
 'Only the delivery changes the count. Forty-eight plus sixteen equals sixty-four.'),
 ('EXPLAIN THE UNUSED NUMBER','Do not subtract objects that remain','64 books in the library',
 'There are sixty-four books. The number twelve tells us how many were cleaned, not how many left.')],g('2HW',2),expression='48+16',value='64')
]
def lessons(doc):return make_lessons(SPECS,doc)
