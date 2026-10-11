"""Generate enrichment samples. Use --speech first (runs Kokoro offline),
then run without flags to render from cached narration with Pillow and FFmpeg.
"""
import argparse
import asyncio
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import tempfile

from PIL import Image, ImageDraw
import generate_sample_videos as video
from generate_sample_videos import text, centered, arrow, TEAL, BLUE, GOLD, INK, MUTED, LIGHT


LESSONS = [
    dict(badge='ENRICHMENT', track='Number theory 1', topic='Modular arithmetic',
         output_dir='enrichment/number-theory 1/U1modular-arithmetic', draw_key='enrichment-mod',
         slug='negative-remainders', title='Make a negative remainder positive',
         source='worksheets/enrichment/number-theory 1/U1modular-arithmetic/E-NT1U1W1.csv', ids=['2'],
         question='Find (5 − 9) mod 7.', answer='3', scenes=[
             ('THE QUESTION', 'Find (5 − 9) mod 7', "What happens when subtraction gives us a negative number in modular arithmetic? Let's try five minus nine, modulo seven."),
             ('SUBTRACT FIRST', '5 − 9 = −4', "First, subtract. Five minus nine is negative four. But our standard remainder must be between zero and six."),
             ('ADD THE MODULUS', '−4 + 7 = 3', "Add seven to move into that range. On the number line, we jump from negative four to three."),
             ('SOLVE', '(5 − 9) mod 7 = 3', "Three is in the right range. Adding seven keeps the same remainder modulo seven, so our answer is three."),
             ('CHECK', '−4 = 7 × (−1) + 3', "Here's the check: negative four equals seven times negative one, plus three. The remainder is three."),
         ]),
    dict(badge='ENRICHMENT', track='Number theory 1', topic='Prime factorization',
         output_dir='enrichment/number-theory 1/U2prime-factorization', draw_key='enrichment-primes',
         slug='prime-factor-tree', title='Build a prime factor tree',
         source='worksheets/enrichment/number-theory 1/U2prime-factorization/E-NT1U2W1.csv', ids=['1'],
         question='Find the prime factorization of 72.', answer='2³ × 3²', animation_seconds=[2,2,9,2,2], scenes=[
             ('THE QUESTION', 'Write 72 as a product of primes', "Let's break seventy-two into prime factors. A factor tree helps us keep track."),
             ('SPLIT THE NUMBER', '72 = 8 × 9', "Start with eight times nine. Neither number is prime, so both branches need to split again."),
             ('KEEP FACTORING', 'Stop only when every leaf is prime', "Eight splits into two and four. Four splits into two and two. Nine splits into three and three. Now every leaf is prime."),
             ('COLLECT THE PRIMES', '72 = 2³ × 3²', "We have three twos and two threes. Using exponents, that's two cubed times three squared."),
             ('CHECK', '2³ × 3² = 8 × 9 = 72', "Check the product. Two cubed is eight, and three squared is nine. Eight times nine gives us seventy-two."),
         ]),
    dict(badge='ENRICHMENT', track='Counting and probability 1', topic='Permutations and combinations',
         output_dir='enrichment/counting-and-probability 1/U3PeCo', draw_key='enrichment-combinations',
         slug='choosing-a-pair', title='Choose a pair without double counting',
         source='worksheets/enrichment/counting-and-probability 1/U3PeCo/E-CP1U3W1.csv', ids=['5'],
         question='How many teams of 2 can you choose from 4 students?', answer='6', scenes=[
             ('THE QUESTION', 'Choose 2 students from 4. How many teams?', "Four students want to form a team of two. There are no special roles. How many different teams can we make?"),
             ('COUNT ORDERED CHOICES', '4 × 3 = 12 ordered choices', "There are four choices for the first student, then three for the second. That gives twelve ordered choices."),
             ('SPOT THE REPEATS', 'A then B and B then A are the same team', "But choosing A then B gives the same team as choosing B then A. We've counted every team twice."),
             ('DIVIDE OUT THE REPEATS', 'C(4, 2) = 12 ÷ 2 = 6', "Divide twelve by two. That leaves six different teams. This is a combination, because order doesn't matter."),
             ('CHECK', 'List each pair once: 6 teams', "List the pairs to check: A B, A C, A D, B C, B D, and C D. Three plus two plus one gives six teams."),
         ]),
    dict(badge='ENRICHMENT', track='Counting and probability 1', topic='Probability mass functions',
         output_dir='enrichment/counting-and-probability 1/U5PMF', draw_key='enrichment-probability',
         slug='first-red-on-second-draw', title='First red on the second draw',
         source='worksheets/enrichment/counting-and-probability 1/U5PMF/E-CP1U5W1.csv', ids=['2'],
         question='Draw randomly without replacement from 3 red and 2 blue balls. What is the probability the first red is on draw 2?', answer='3/10', scenes=[
             ('THE QUESTION', 'First red on draw 2. What is the probability?', "A bag has three red balls and two blue balls. We draw randomly, without replacement. What's the chance our first red comes second?"),
             ('IDENTIFY THE PATH', 'We need BLUE first, then RED', "For the first red to come second, we need blue first, then red. Blue first has probability two fifths."),
             ('UPDATE THE BAG', 'After a blue: 3 red out of 4 balls remain', "Keep that blue ball out. Four balls remain, and three are red. So the next draw is red with probability three quarters."),
             ('MULTIPLY ALONG THE PATH', 'P(X = 2) = (2/5) × (3/4) = 3/10', "Multiply along this path: two fifths times three quarters. That's six twentieths, which simplifies to three tenths."),
             ('CHECK', '2 × 3 favourable ordered draws out of 5 × 4', "To check, count individual balls: two blue choices, then three red choices. Six favourable ordered draws out of twenty gives three tenths."),
         ]),
]


def box(d, bounds, fill='white', outline=None):
    d.rounded_rectangle(bounds, radius=26, fill=fill, outline=outline, width=4)


def draw_mod(d, scene, p):
    if scene == 0:
        box(d, (420, 380, 1500, 690))
        centered(d, 440, '(5 − 9) mod 7', 85, TEAL, True)
        centered(d, 585, 'Standard remainders: 0, 1, 2, 3, 4, 5, 6', 38)
        return
    y=635
    def x(n): return 300+(n+5)*130
    arrow(d, (230,y), (1700,y), MUTED, 5)
    for n in range(-5,6):
        d.line((x(n),y-13,x(n),y+13), fill=INK, width=4)
        text(d,(x(n),y+33),str(n).replace('-','−'),34,INK,False,'mt')
    d.ellipse((x(-4)-15,y-15,x(-4)+15,y+15),fill=BLUE)
    if scene >= 2:
        progress=p if scene==2 else 1
        end=x(-4)+(x(3)-x(-4))*progress
        arrow(d,(x(-4),y-120),(max(x(-4)+25,end),y-120),TEAL,7)
        d.ellipse((end-18,y-18,end+18,y+18),fill=TEAL)
        centered(d,395,'+ 7',72,TEAL,True)
        text(d,(x(3),y+90),'remainder 3',32,TEAL,True,'mt')
    else:
        centered(d,435,'Negative four is outside the range 0 to 6.',42,MUTED)
    centered(d,790,'A jump of 7 preserves the remainder modulo 7.',36,MUTED)


def draw_primes(d, scene, p):
    nodes={'72':(960,360),'8':(650,475),'9':(1280,475),'a':(460,600),'4':(800,600),'b':(1175,600),'c':(1400,600),'d':(710,730),'e':(915,730)}
    values={'a':'2','b':'3','c':'3','d':'2','e':'2'}
    edges=[('72','8'),('72','9'),('8','a'),('8','4'),('4','d'),('4','e'),('9','b'),('9','c')]
    show=0 if scene==0 else 2 if scene==1 else 2+int(6*p) if scene==2 else 8
    visible={'72'}
    for a,b in edges[:show]:
        d.line([nodes[a],nodes[b]],fill='#b6c8c0',width=5)
        visible.add(b)
    for key in visible:
        x,y=nodes[key]
        prime=key in values
        d.ellipse((x-43,y-43,x+43,y+43),fill=TEAL if prime else 'white',outline=TEAL if prime else '#b6c8c0',width=3)
        text(d,(x,y-24),values.get(key,key),45,'white' if prime else INK,True,'mt')
    if scene>=3: centered(d,810,'2 × 2 × 2 × 3 × 3 = 2³ × 3²',42,TEAL,True)
    elif scene<2: centered(d,800,'Composite numbers split. Prime numbers stop.',37,MUTED)


def draw_combinations(d, scene, p):
    if scene==0:
        for i,c in enumerate('ABCD'):
            x=480+i*320
            d.ellipse((x-65,415,x+65,545),fill=TEAL)
            text(d,(x,440),c,62,'white',True,'mt')
        centered(d,660,'Choose 2. No roles. Order does not matter.',45,INK,True)
    elif scene==1:
        for i,(n,label) in enumerate([('4','choices for the first student'),('3','choices for the second student')]):
            x=270+i*810
            box(d,(x,385,x+570,730))
            text(d,(x+285,425),n,115,TEAL,True,'mt')
            text(d,(x+285,620),label,31,INK,False,'mt')
        centered(d,495,'×',85,TEAL,True)
        centered(d,785,'12 ordered choices',43,TEAL,True)
    elif scene==2:
        for x,label in [(260,'A → B'),(1120,'B → A')]:
            box(d,(x,400,x+540,645))
            text(d,(x+270,470),label,76,TEAL,True,'mt')
        centered(d,480,'=',82,MUTED,True)
        centered(d,725,'Same two students. Same team.',46,INK,True)
        centered(d,800,'Each team was counted 2 times.',36,MUTED)
    else:
        pairs=list(combinations('ABCD',2))
        for i,pair in enumerate(pairs):
            col,row=i%3,i//3
            x,y=490+col*350,405+row*185
            active=scene==4 or i<max(1,int(p*6))
            box(d,(x,y,x+240,y+128),LIGHT if active else 'white')
            text(d,(x+120,y+33),' + '.join(pair),45,TEAL if active else MUTED,True,'mt')
        centered(d,790,'3 + 2 + 1 = 6 teams',44,TEAL,True)


def draw_probability(d, scene, p):
    red='#b84249'
    def bag(x, remaining=False):
        box(d,(x,400,x+610,715),'white', '#ccd8d0')
        text(d,(x+305,425),'AFTER ONE BLUE' if remaining else 'START: 5 BALLS',29,MUTED,True,'mt')
        balls=[(110,535,red,'R'),(300,535,red,'R'),(490,535,red,'R'),(200,645,BLUE,'B')]
        if not remaining: balls.append((400,645,BLUE,'B'))
        for dx,y,color,label in balls:
            d.ellipse((x+dx-35,y-35,x+dx+35,y+35),fill=color)
            text(d,(x+dx,y-22),label,37,'white',True,'mt')
    bag(190)
    if scene>=2:
        arrow(d,(840,555),(1070,555),TEAL,7)
        bag(1120,True)
        text(d,(960,450),'remove 1 blue',30,MUTED,False,'mt')
        if scene>=3:
            text(d,(495,755),'P(blue first) = 2/5',39,BLUE,True,'mt')
            text(d,(1425,755),'P(red next | blue first) = 3/4',34,red,True,'mt')
        else:
            text(d,(1425,760),'3 red / 4 remaining = 3/4',39,red,True,'mt')
    else:
        box(d,(1060,415,1730,720))
        text(d,(1395,445),'X = draw of the first red',37,INK,True,'mt')
        text(d,(1395,535),'BLUE  →  RED' if scene==1 else 'Find P(X = 2)',49,TEAL,True,'mt')
        text(d,(1395,645),'2 blue out of 5 = 2/5' if scene==1 else 'Random draws · no replacement',30,MUTED,False,'mt')
    if scene==4: centered(d,822,'6/20 = 3/10 = 30%',35,TEAL,True)


video.DRAW.update({'enrichment-mod':draw_mod,'enrichment-primes':draw_primes,
                   'enrichment-combinations':draw_combinations,'enrichment-probability':draw_probability})


def check_answers():
    assert (5-9)%7==3 and -4==7*(-1)+3
    assert 2**3*3**2==72
    assert len(list(combinations('ABCD',2)))==6
    assert Fraction(2,5)*Fraction(3,4)==Fraction(3,10)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--speech',action='store_true')
    parser.add_argument('--preview',action='store_true')
    args=parser.parse_args()
    check_answers()
    if args.speech:
        from synthesize_video_narration import main as synthesize
        asyncio.run(synthesize(LESSONS))
        return
    destination=video.OUT/'enrichment'
    destination.mkdir(exist_ok=True)
    sheet=Image.new('RGB',(3200,1440),'white')
    if args.preview:
        for row,lesson in enumerate(LESSONS):
            for scene in range(5):
                im=video.base(lesson,scene)
                video.DRAW[lesson['draw_key']](ImageDraw.Draw(im),scene,1)
                sheet.paste(im.resize((640,360)),(scene*640,row*360))
        sheet.save('/tmp/enrichment-video-preview.jpg',quality=95)
        return
    with tempfile.TemporaryDirectory(prefix='enrichment-videos-') as directory:
        for row,lesson in enumerate(LESSONS):
            _,posters=video.render(lesson,Path(directory))
            for col,poster in enumerate(posters):
                sheet.paste(poster,(col*640,row*360))
    sheet.save(destination/'sample-contact-sheet.jpg',quality=93)
    video.write_gallery(destination)
    video.write_gallery()
    print('Enrichment videos and galleries are ready.',flush=True)


if __name__=='__main__':
    main()
