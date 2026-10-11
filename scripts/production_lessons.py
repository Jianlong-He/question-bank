"""Authored production lessons: stable IDs, analogous examples and explicit visuals."""
import copy
import math
from fractions import Fraction
from itertools import permutations

import generate_sample_videos as video
import generate_enrichment_videos as enrichment
from generate_sample_videos import text, centered, arrow, TEAL, BLUE, INK, MUTED, LIGHT


NEW_LESSONS=[
    dict(video_id='g1-u1-counting-backward',grade=1,unit=1,
         slug='counting-backward',title='Count backward on a number line',topic='Counting backward',
         source='worksheets/Grade 1/G1Unit 1/G1U1W1.csv',ids=['4','5'],draw_key='backward',
         question='Count backward from 18 to 14.',answer='18, 17, 16, 15, 14',
         animation_seconds=[2,2,2,4,2],scenes=[
             ('THE QUESTION','Count backward from 18 to 14',"Let's count backward from eighteen to fourteen. Each number will be one less."),
             ('FIND THE START','Start at 18',"Find eighteen on the number line. We begin here and move to the left."),
             ('TAKE ONE STEP','18 − 1 = 17',"One step left takes us from eighteen to seventeen. That's one less."),
             ('KEEP GOING','18, 17, 16, 15, 14',"Keep moving left, one step at a time. Eighteen, seventeen, sixteen, fifteen, fourteen. Stop at fourteen."),
             ('CHECK','Every step subtracts 1',"Check that each number is one smaller than the last. We started at eighteen and stopped at fourteen."),
         ]),
    dict(video_id='enrichment-number-theory-1-modular-addition',badge='ENRICHMENT',
         track='Number theory 1',topic='Modular arithmetic',
         output_dir='enrichment/number-theory 1/U1modular-arithmetic',draw_key='modular-addition',
         slug='modular-addition',title='Add, then find the remainder',
         source='worksheets/enrichment/number-theory 1/U1modular-arithmetic/E-NT1U1W1.csv',ids=['1','3','4','5'],
         question='Find (8 + 9) mod 6.',answer='5',scenes=[
             ('THE QUESTION','Find (8 + 9) mod 6',"Let's find eight plus nine, modulo six. We want the remainder after dividing the sum by six."),
             ('ADD FIRST','8 + 9 = 17',"First add the numbers. Eight plus nine is seventeen."),
             ('MAKE GROUPS OF SIX','17 = 6 + 6 + 5',"Seventeen contains two complete groups of six. That uses twelve, leaving five."),
             ('KEEP THE REMAINDER','(8 + 9) mod 6 = 5',"The remainder is five. It's between zero and five, so it's a valid standard remainder modulo six."),
             ('CHECK','17 = 6 × 2 + 5',"Check with division: six times two, plus five, equals seventeen. Our answer is five."),
         ]),
    dict(video_id='enrichment-counting-and-probability-1-choose-three',badge='ENRICHMENT',
         track='Counting and probability 1',topic='Permutations and combinations',
         output_dir='enrichment/counting-and-probability 1/U3PeCo',draw_key='choose-three',
         slug='choose-three',title='Choose three without counting order',
         source='worksheets/enrichment/counting-and-probability 1/U3PeCo/E-CP1U3W1.csv',ids=['5'],
         question='How many teams of 3 can you choose from 12 students?',answer='220',scenes=[
             ('THE QUESTION','Choose 3 students from 12. How many teams?',"Twelve students are available. How many teams of three can we choose, when order doesn't matter?"),
             ('COUNT ORDERED CHOICES','12 × 11 × 10 = 1320',"Count ordered choices first: twelve choices, then eleven, then ten. That's one thousand three hundred twenty."),
             ('COUNT THE REPEATS','Each team appears 3 × 2 × 1 = 6 times',"Each team of three appears in six different orders. These six arrangements all give the same team."),
             ('REMOVE THE REPEATS','C(12, 3) = 1320 ÷ 6 = 220',"Divide by six to remove those repeats. We get two hundred twenty different teams."),
             ('CHECK','220 teams × 6 orders = 1320',"Check: two hundred twenty teams, each in six orders, gives one thousand three hundred twenty. Our count is consistent."),
         ]),
]


def draw_backward(d,scene,p):
    y=610
    def x(n):return 360+(n-14)*300
    d.line((260,y,1660,y),fill='#b4beba',width=7)
    for n in range(14,19):
        d.line((x(n),y-18,x(n),y+18),fill=INK,width=5)
        text(d,(x(n),y+45),str(n),53,INK,True,'mt')
    location=18 if scene<2 else 18-p if scene==2 else 17-3*p if scene==3 else 14
    d.ellipse((x(location)-22,y-22,x(location)+22,y+22),fill=TEAL)
    if scene>=2:
        start=18 if scene==2 else 17 if scene==3 else 18
        end=location if scene<4 else 14
        arrow(d,(x(start),y-110),(min(x(start)-20,x(end)),y-110),TEAL,8)
        centered(d,410,'Move left: one less each time',44,TEAL,True)
    if scene>=3:centered(d,795,'18  →  17  →  16  →  15  →  14',49,TEAL,True)


def draw_modular_addition(d,scene,p):
    if scene<2:
        centered(d,450,'8 + 9' if scene==0 else '8 + 9 = 17',105,TEAL,True)
        centered(d,670,'Modulo 6: keep the remainder',45,MUTED)
        return
    for i in range(17):
        group,within=(0,i) if i<6 else (1,i-6) if i<12 else (2,i-12)
        x=280+group*540+(within%3)*100
        y=455+(within//3)*115
        color=TEAL if group<2 else BLUE
        d.ellipse((x-28,y-28,x+28,y+28),fill=color)
    for group in range(2):
        x=210+group*540
        d.rounded_rectangle((x,380,x+340,650),radius=26,outline=TEAL,width=5)
        text(d,(x+170,685),'6',56,TEAL,True,'mt')
    text(d,(1460,685),'5 left',56,BLUE,True,'mt')
    centered(d,810,'17 − 12 = 5' if scene==2 else 'Remainder: 5',52,TEAL,True)


def draw_choose_three(d,scene,p):
    if scene==0:
        for i,label in enumerate('ABCDEFGHIJKL'):
            x=350+(i%6)*240;y=420+(i//6)*200
            d.ellipse((x-55,y-55,x+55,y+55),fill=TEAL)
            text(d,(x,y-32),label,55,'white',True,'mt')
        centered(d,800,'Choose 3. No roles. Order does not matter.',40,INK,True)
    elif scene==1:
        for i,value in enumerate(['12','11','10']):
            x=260+i*550
            d.rounded_rectangle((x,400,x+310,650),radius=30,fill='white')
            text(d,(x+155,445),value,100,TEAL,True,'mt')
            if i<2:text(d,(x+420,470),'×',75,TEAL,True,'mt')
        centered(d,785,'1320 ordered choices',56,TEAL,True)
    elif scene==2:
        for i,group in enumerate(permutations('ABC')):
            x=430+(i%3)*400;y=385+(i//3)*195
            d.rounded_rectangle((x,y,x+290,y+125),radius=22,fill=LIGHT)
            text(d,(x+145,y+33),' '.join(group),48,TEAL,True,'mt')
        centered(d,820,'Same 3 students. Same team. 6 orders.',41,INK,True)
    else:
        centered(d,440,'1320 ÷ 6 = 220',90,TEAL,True)
        centered(d,635,'220 different teams',56,INK,True)
        if scene==4:centered(d,790,'220 × 6 = 1320 ordered choices',42,MUTED)


video.DRAW.update({'backward':draw_backward,'modular-addition':draw_modular_addition,'choose-three':draw_choose_three})


def lessons():
    result=[]
    for source in [*video.LESSONS,*enrichment.LESSONS]:
        lesson=copy.deepcopy(source)
        if 'grade' in lesson:lesson['video_id']=f'g{lesson["grade"]}-u{lesson["unit"]}-{lesson["slug"]}'
        else:
            prefix='number-theory-1' if lesson['track']=='Number theory 1' else 'counting-and-probability-1'
            lesson['video_id']=f'enrichment-{prefix}-{lesson["slug"]}'
        result.append(lesson)
    result+=copy.deepcopy(NEW_LESSONS)
    return result


def check_answers():
    assert 27+1==28 and 4*2==8
    assert math.gcd(4,10)==2 and (4//2,10//2)==(2,5)
    assert abs(3-3)+2==2
    enrichment.check_answers()
    assert list(range(18,13,-1))==[18,17,16,15,14]
    assert (8+9)%6==5
    assert math.comb(12,3)==12*11*10//math.factorial(3)==220
