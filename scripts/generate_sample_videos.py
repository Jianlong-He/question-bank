"""Render four narrated worksheet examples with Pillow, neural speech and FFmpeg.

Run with the bundled Python (Pillow required). Default outputs stay in videos/;
Run synthesize_video_narration.py first to populate the reusable speech cache.
Temporary rendering files are removed automatically. No worksheet is changed.
"""
from pathlib import Path
import csv
import html
import hashlib
import json
import math
import os
import subprocess as sp
import tempfile

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'videos'
W, H, FPS = 1920, 1080, 30
BG, INK, MUTED = '#f6f5f0', '#172c3a', '#5c6b73'
TEAL, BLUE, GOLD, LIGHT = '#087f78', '#4265bd', '#e7a33c', '#dde9e5'
FONT = Path('/System/Library/Fonts/Supplemental')
FONTS = {}
VOICE = 'Kokoro-82M v1.0 / af_heart'
VOICE_RATE = 0.95


def narration_path(lesson, index):
    speech = lesson['scenes'][index][2]
    digest = hashlib.sha256(f'{VOICE}|{VOICE_RATE}|{speech}'.encode()).hexdigest()[:16]
    return OUT / '.narration' / lesson['slug'] / f'{index+1}-{digest}.wav'


def font(size, bold=False):
    key = size, bold
    if key not in FONTS:
        FONTS[key] = ImageFont.truetype(str(FONT / ('Arial Bold.ttf' if bold else 'Arial.ttf')), size)
    return FONTS[key]


LESSONS = [
    dict(grade=1, unit=1, slug='counting-forward', title='One step forward',
         topic='Counting forward', source='worksheets/Grade 1/G1Unit 1/G1U1W1.csv', ids=['6'],
         question='What number comes after 27?', answer='28',
         scenes=[
             ('THE QUESTION', 'What number comes after 27?', "What comes after twenty-seven? Let's find out together."),
             ('FIND YOUR START', 'Start at 27', "Here's twenty-seven on our number line. We'll start right here."),
             ('TAKE ONE STEP', 'Move 1 step to the right', "Now, take one step to the right. That gives us one more."),
             ('SOLVE', '27 + 1 = 28', "We land on twenty-eight! So, twenty-seven plus one is twenty-eight."),
             ('CHECK', '26, 27, 28, 29', "Let's check: twenty-six, twenty-seven, twenty-eight, twenty-nine. Yes, twenty-eight comes next."),
         ]),
    dict(grade=3, unit=1, slug='equal-groups', title='Count equal groups',
         topic='Multiplication', source='worksheets/Grade 3/G3Unit 1/G3U1W1.csv', ids=['1'],
         question='4 groups of 2 dots. How many dots?', answer='8',
         scenes=[
             ('THE QUESTION', '4 groups of 2. How many dots?', "We've got four groups of dots. How many dots are there altogether?"),
             ('SEE THE GROUPS', '4 groups × 2 dots in each', "Look inside one group: one, two. Every group has two dots."),
             ('ADD THE GROUPS', '2 + 2 + 2 + 2 = 8', "Count two at a time. Two, four, six, eight. That's eight dots altogether."),
             ('WRITE THE MULTIPLICATION', '4 × 2 = 8', "Here's a shorter way to write it: four times two equals eight."),
             ('CHECK', '4 groups. 2 in each. 8 altogether.', "Four groups, two in each, eight altogether. That's what multiplication helps us count."),
         ]),
    dict(grade=6, unit=1, slug='simplifying-ratios', title='Simplify a ratio',
         topic='Ratios', source='worksheets/Grade 6/G6Unit 1/G6U1W1.csv', ids=['2'],
         question='Simplify the ratio 4 : 10.', answer='2 : 5',
         scenes=[
             ('THE QUESTION', 'Simplify 4 : 10', "Let's simplify four to ten. We need smaller whole numbers that keep the same relationship."),
             ('FIND A COMMON FACTOR', 'Both numbers divide by 2', "Both numbers divide by two. Two is their greatest common factor."),
             ('DIVIDE BOTH PARTS', '4 ÷ 2 = 2     and     10 ÷ 2 = 5', "Divide each part by two. Four becomes two, and ten becomes five."),
             ('SOLVE', '4 : 10 = 2 : 5', "Our answer is two to five. These numbers share no common factor greater than one, so we're done."),
             ('CHECK', '2 × 2 = 4     and     5 × 2 = 10', "Check by multiplying both parts by two. We get four and ten again, so the ratios match."),
         ]),
    dict(grade=10, unit=1, slug='absolute-value-vertex', title='Move the vertex',
         topic='Absolute-value functions', source='worksheets/Grade 10/G10Unit 1/G10U1W1.csv', ids=['1', '2'],
         question='Find the vertex of y = |x − 3| + 2.', answer='(3, 2)',
         scenes=[
             ('THE QUESTION', 'Find the vertex of y = |x − 3| + 2', "Where's the vertex of this graph? We can find it with two simple shifts."),
             ('START WITH THE PARENT GRAPH', 'y = |x| has vertex (0, 0)', "Start with y equals the absolute value of x. The bottom of the V sits at the origin: zero, zero."),
             ('SHIFT RIGHT', 'x − 3 moves the graph 3 units right', "See the minus three inside the bars? That moves the whole graph three units to the right."),
             ('SHIFT UP', '+ 2 moves the graph 2 units up', "Then the plus two outside moves it up two units. Our vertex is now three, two."),
             ('CHECK', 'x = 3:  y = |3 − 3| + 2 = 2', "Let's check. Put three in for x. Inside the bars, we get zero, leaving y equal to two. So the vertex is three, two."),
         ]),
]


def text(d, xy, s, size=40, color=INK, bold=False, anchor=None):
    d.text(xy, s, font=font(size, bold), fill=color, anchor=anchor)


def centered(d, y, s, size=40, color=INK, bold=False):
    text(d, (W // 2, y), s, size, color, bold, 'mt')


def wrap(d, s, size, width):
    lines, current = [], ''
    for word in s.split():
        trial = f'{current} {word}'.strip()
        if d.textlength(trial, font=font(size)) > width and current:
            lines.append(current)
            current = word
        else:
            current = trial
    return lines + [current]


def arrow(d, a, b, color=TEAL, width=8):
    d.line([a, b], fill=color, width=width)
    angle = math.atan2(b[1] - a[1], b[0] - a[0])
    points = [b] + [(b[0] - 23 * math.cos(angle + v), b[1] - 23 * math.sin(angle + v)) for v in [-.5, .5]]
    d.polygon(points, fill=color)


def base(lesson, scene):
    im = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((72, 52, 350, 110), radius=29, fill=TEAL)
    badge = lesson.get('badge') or f"GRADE {lesson['grade']} · UNIT {lesson['unit']}"
    text(d, (211, 64), badge, 27, 'white', True, 'mt')
    text(d, (385, 64), lesson['topic'], 30, MUTED)
    text(d, (1848, 65), 'WORKED EXAMPLE', 26, MUTED, False, 'rt')
    for j in range(5):
        x = 72 + j * 357
        d.rounded_rectangle((x, 142, x + 340, 149), radius=3, fill=TEAL if j <= scene else '#dce0db')
    label, heading, speech = lesson['scenes'][scene]
    text(d, (88, 183), f'0{scene + 1} / {label}', 27, TEAL, True)
    text(d, (88, 231), heading, 57 if len(heading) < 39 else 48, INK, True)
    # Narration is audio only; keep mathematical working in the scene drawings.
    text(d, (88, 1041), 'Similar practice question · explained step by step', 20, MUTED)
    text(d, (1830, 1041), 'AI narration · generated locally', 20, MUTED, False, 'rt')
    return im


def draw_count(d, scene, p):
    y, left, gap = 600, 360, 300
    d.line((260, y, 1660, y), fill='#b4beba', width=7)
    arrow(d, (1600, y), (1700, y), MUTED, 7)
    for i, n in enumerate(range(25, 30)):
        x = left + i * gap
        d.line((x, y - 18, x, y + 18), fill=INK, width=5)
        text(d, (x, y + 45), str(n), 53, INK, True, 'mt')
    start, end = left + 2 * gap, left + 3 * gap
    x = start if scene < 2 else start + (end - start) * (p if scene == 2 else 1)
    d.ellipse((x - 22, y - 22, x + 22, y + 22), fill=TEAL)
    if scene >= 2:
        arrow(d, (start, y - 125), (start + (end-start) * max(.08, p if scene == 2 else 1), y - 125))
        text(d, ((start + end)/2, y - 200), '+ 1', 54, TEAL, True, 'mt')
    if scene >= 3:
        d.rounded_rectangle((790, 748, 1130, 834), radius=25, fill=LIGHT)
        centered(d, 760, 'Answer: 28', 48, TEAL, True)
    else:
        centered(d, 750, 'Next number = one more', 37, MUTED)


def draw_groups(d, scene, p):
    for i in range(4):
        x, y = 200 + i * 395, 395
        active = scene != 2 or i <= min(3, int(p * 4))
        color = TEAL if active else '#bdcbc5'
        d.rounded_rectangle((x, y, x + 335, y + 265), radius=35, fill='white', outline=color, width=5)
        for dx, dy in [(96, 133), (238, 133)]:
            d.ellipse((x+dx-30, y+dy-30, x+dx+30, y+dy+30), fill=color)
        text(d, (x+168, y+290), f'Group {i+1}', 30, MUTED, False, 'mt')
        if scene == 2 and active:
            text(d, (x+168, y+350), str((i+1)*2), 48, TEAL, True, 'mt')
    if scene >= 3:
        centered(d, 760, '2 + 2 + 2 + 2 = 4 × 2 = 8', 47, TEAL, True)
    elif scene < 2:
        centered(d, 760, 'Each group has the same number of dots.', 37, MUTED)


def draw_ratio(d, scene, p):
    for row, (n, color) in enumerate([(4, TEAL), (10, BLUE)]):
        y = 417 + row * 190
        text(d, (280, y + 10), str(n), 65, color, True, 'mt')
        for i in range(n):
            x = 450 + i * 88
            d.ellipse((x, y+20, x+42, y+62), fill=color)
        if scene >= 1:
            for group in range(n//2):
                x = 433 + group * 176
                d.rounded_rectangle((x, y, x+149, y+85), radius=18, outline=color, width=4)
            text(d, (1590, y+8), f'{n//2} groups', 43, color, True)
    if scene == 0:
        centered(d, 787, 'Keep the same relationship.', 38, MUTED)
    elif scene < 3:
        centered(d, 787, 'Each outlined group contains 2 dots.', 38, MUTED)
    else:
        centered(d, 764, '4 : 10 = 2 : 5', 63, TEAL, True)


def draw_graph(d, scene, p):
    # Integer grid: x = -3..8, y = -1..8. Graph paths are clipped to this box.
    x0, y0, scale = 580, 790, 51
    def pt(x,y): return (x0+x*scale,y0-y*scale)
    for x in range(-3,9):
        d.line([pt(x,-1),pt(x,8)], fill='#e0e4de', width=2)
        if x: text(d, (pt(x,0)[0],y0+16),str(x),22,MUTED,False,'mt')
    for y in range(-1,9):
        d.line([pt(-3,y),pt(8,y)], fill='#e0e4de', width=2)
        if y>0: text(d,(x0-15,pt(0,y)[1]-12),str(y),22,MUTED,False,'rt')
    arrow(d,pt(-3,0),pt(8.4,0),INK,3)
    arrow(d,pt(0,-1),pt(0,8.4),INK,3)
    text(d,pt(8.6,.25),'x',26)
    text(d,pt(.25,8.6),'y',26)
    def graph(h,k,color,width):
        coords=[pt(-3,abs(-3-h)+k),pt(h,k),pt(8,abs(8-h)+k)]
        # Clamp endpoints at y=8 so lines do not overlap the title.
        coords=[pt(max(-3,h-(8-k)),8 if abs(-3-h)+k>8 else abs(-3-h)+k),pt(h,k),pt(min(8,h+(8-k)),8 if abs(8-h)+k>8 else abs(8-h)+k)]
        d.line(coords,fill=color,width=width,joint='curve')
    graph(0,0,'#b4c1bd',5)
    if scene == 0:
        h,k=3,2
    elif scene == 1:
        h,k=0,0
    elif scene == 2:
        h,k=3*p,0
    elif scene == 3:
        h,k=3,2*p
    else:
        h,k=3,2
    graph(h,k,TEAL,8)
    vx,vy=pt(h,k)
    d.ellipse((vx-11,vy-11,vx+11,vy+11),fill=GOLD)
    if scene > 0:
        label = '(0, 0)' if scene==1 else '(3, 0)' if scene==2 else '(3, 2)'
        if p >= .99 or scene in [1,4]: text(d,(vx+20,vy-45),label,32,TEAL,True)
    d.rounded_rectangle((1150,380,1810,820),radius=28,fill='white')
    lines = {
        0:['Vertex = turning point','Look for the bottom','of the V.'],
        1:['Parent function','y = |x|','Vertex: (0, 0)'],
        2:['Horizontal shift','3 units right','(0, 0) → (3, 0)'],
        3:['Vertical shift','2 units up','(3, 0) → (3, 2)'],
        4:['Vertex: (3, 2)','|3 − 3| + 2','0 + 2 = 2'],
    }[scene]
    for i,line in enumerate(lines):
        text(d,(1190,435+i*115),line,38 if len(line)>19 else 45,TEAL if i==0 else INK,i==0)


DRAW = {1: draw_count, 3: draw_groups, 6: draw_ratio, 10: draw_graph}


def probe(path):
    return json.loads(sp.check_output(['ffprobe','-v','error','-show_format','-show_streams','-of','json',str(path)]))


def stamp(s):
    ms=round(s*1000)
    return f'{ms//3600000:02d}:{ms//60000%60:02d}:{ms//1000%60:02d},{ms%1000:03d}'


def encode_static_scenes(sequence, elapsed, silent):
    # The output -r/CFR conversion can truncate a sparse image sequence's final
    # hold. Generate frames in the filter graph and explicitly count every frame.
    sp.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',str(sequence),
            '-vf',f'fps={FPS},tpad=stop_mode=clone:stop_duration=1',
            '-frames:v',str(round(elapsed*FPS)),'-an','-c:v','libx264',
            '-preset','fast','-crf','21','-pix_fmt','yuv420p',str(silent)],check=True)


def render(lesson, scratch, output_root=OUT, write_companions=True):
    directory = output_root / (lesson.get('output_dir') or f"Grade {lesson['grade']}/Unit {lesson['unit']}")
    directory.mkdir(parents=True, exist_ok=True)
    export_name = lesson.get('video_id', lesson['slug'])
    target = directory / f"{export_name}.mp4"
    rows = list(csv.DictReader((ROOT/lesson['source']).open(newline='',encoding='utf-8-sig')))
    sources=[r for r in rows if r['Question ID'] in lesson['ids']]
    assert len(sources)==len(lesson['ids'])
    durations, audiofiles = [], []
    for index, (_,_,speech) in enumerate(lesson['scenes']):
        audiofile = narration_path(lesson, index)
        if not audiofile.exists():
            raise FileNotFoundError(f'Run synthesize_video_narration.py first: {audiofile}')
        seconds = float(probe(audiofile)['format']['duration'])
        durations.append(math.ceil((seconds+1.1)*FPS)/FPS)
        audiofiles.append(audiofile)
    assert sum(durations)<60, (lesson['slug'],durations)
    print(f"Rendering {target} ({sum(durations):.1f}s)",flush=True)
    silent = scratch / f"{lesson['slug']}-silent.mp4"
    command=['ffmpeg','-v','error','-y','-f','rawvideo','-vcodec','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-an','-c:v','libx264','-preset','fast','-crf','21','-pix_fmt','yuv420p',str(silent)]
    if lesson.get('static_scenes'):
        posters=[]
        elapsed=sum(durations)
        playlist=[]
        for index,duration in enumerate(durations):
            im=base(lesson,index)
            DRAW[lesson['draw_key']](ImageDraw.Draw(im),index,1)
            frame=scratch/f'scene-{index}.png'
            im.save(frame)
            posters.append(im.resize((640,360)))
            if write_companions and index==3:
                im.save(directory/f'{export_name}-poster.jpg',quality=92)
            playlist += [f"file '{frame.name}'",f'duration {duration:.6f}']
        playlist.append(f"file 'scene-{len(durations)-1}.png'")
        sequence=scratch/'scenes.txt'
        sequence.write_text('\n'.join(playlist)+'\n')
        encode_static_scenes(sequence,elapsed,silent)
    else:
        encoder=sp.Popen(command,stdin=sp.PIPE)
        posters=[]
        elapsed=0
        for index,duration in enumerate(durations):
            back=base(lesson,index)
            static=None
            frames=round(duration*FPS)
            for frame in range(frames):
                # Reveal at the lesson's pace, then hold the complete step for reading.
                animation_seconds=lesson.get('animation_seconds', [2]*5)[index]
                progress=min(1,frame/(FPS*min(animation_seconds,duration-1)))
                eased=progress*progress*(3-2*progress)
                if static is None:
                    im=back.copy()
                    d=ImageDraw.Draw(im)
                    DRAW[lesson.get('draw_key', lesson.get('grade'))](d,index,eased)
                    if progress>=1:
                        static=im.tobytes()
                        if index==3 and write_companions:
                            im.save(directory / f"{export_name}-poster.jpg",quality=92)
                        posters.append(im.resize((640,360)))
                    encoder.stdin.write(im.tobytes() if static is None else static)
                else:
                    encoder.stdin.write(static)
            elapsed += duration
        encoder.stdin.close()
        assert encoder.wait()==0
    audioargs=[]
    filters=[]
    for i,(audiofile,duration) in enumerate(zip(audiofiles,durations)):
        audioargs += ['-i',str(audiofile)]
        filters.append(f'[{i+1}:a]aresample=48000,adelay=250,apad,atrim=duration={duration:.6f},asetpts=PTS-STARTPTS[a{i}]')
    filters.append(''.join(f'[a{i}]' for i in range(5))+'concat=n=5:v=0:a=1[a]')
    pending = scratch / f'{export_name}-complete.mp4'
    sp.run(['ffmpeg','-v','error','-y','-i',str(silent),*audioargs,'-filter_complex',';'.join(filters),'-map','0:v','-map','[a]','-c:v','copy','-c:a','aac','-b:a','160k','-movflags','+faststart',str(pending)],check=True)
    metadata={**lesson,'duration_seconds':round(elapsed,2),'voice':VOICE,'voice_rate':VOICE_RATE,'speech_engine':'Kokoro ONNX (local, CPU)','model_license':'Apache-2.0','video':str(target.relative_to(output_root)),'subtitles':False,'source_questions':sources}
    # Verify the deliverable itself, including a complete decode of video and audio.
    details=probe(pending)
    video=next(s for s in details['streams'] if s['codec_type']=='video')
    audio=next(s for s in details['streams'] if s['codec_type']=='audio')
    assert (video['width'],video['height'],video['codec_name'])==(W,H,'h264')
    assert audio['codec_name']=='aac'
    assert abs(float(video['duration'])-elapsed)<2/FPS,('Video ends before narration',video['duration'],elapsed)
    assert abs(float(audio['duration'])-elapsed)<2/FPS,('Audio timing mismatch',audio['duration'],elapsed)
    assert not any(s['codec_type']=='subtitle' for s in details['streams'])
    assert 1<float(details['format']['duration'])<60
    sp.run(['ffmpeg','-v','error','-i',str(pending),'-f','null','-'],check=True)
    # Scratch lives on the destination volume for an atomic final replacement.
    pending.replace(target)
    if write_companions:
        target.with_suffix('.json').write_text(json.dumps(metadata,indent=2,ensure_ascii=False)+'\n')
    print(f"Verified: {target.name}",flush=True)
    return metadata,posters


def main():
    OUT.mkdir(exist_ok=True)
    # Independent arithmetic checks of all four example answers.
    assert 27+1==28
    assert sum([2]*4)==4*2==8
    assert math.gcd(4,10)==2 and (4//2,10//2)==(2,5)
    assert abs(3-3)+2==2
    entries,rows=[],[]
    with tempfile.TemporaryDirectory(prefix='worksheet-videos-') as directory:
        for lesson in LESSONS:
            entry,posters=render(lesson,Path(directory))
            entries.append(entry)
            rows.append(posters)
    sheet=Image.new('RGB',(640*5,360*4),'white')
    for row,posters in enumerate(rows):
        for col,poster in enumerate(posters): sheet.paste(poster,(640*col,360*row))
    sheet.save(OUT/'sample-contact-sheet.jpg',quality=90)
    write_gallery()
    print('Grade videos are ready. Open videos/index.html to preview.',flush=True)


def write_gallery(destination=OUT):
    entries=[]
    for path in sorted(destination.rglob('*.json')):
        if path.name.startswith('._') or path.name == 'catalog.json' or '.narration' in path.parts:
            continue
        entry=json.loads(path.read_text())
        if 'video' in entry and 'source_questions' in entry:
            entries.append(entry)
    (destination/'catalog.json').write_text(json.dumps(entries,indent=2,ensure_ascii=False)+'\n')
    cards=[]
    for entry in entries:
        url=html.escape(os.path.relpath(OUT/entry['video'],destination),quote=True)
        poster=url.replace('.mp4','-poster.jpg')
        label=entry.get('track') or f"Grade {entry['grade']} / Unit {entry['unit']}"
        cards.append(f'''<article><p class="eyebrow">{html.escape(label.upper())} · {entry['duration_seconds']:.0f} SEC</p><h2>{html.escape(entry['title'])}</h2><p>{html.escape(entry['question'])}</p><video controls preload="metadata" poster="{poster}" src="{url}"></video><p><a href="{url}" download>Download MP4</a></p></article>''')
    (destination/'index.html').write_text('''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Worksheet video samples</title><style>body{margin:0;background:#f6f5f0;color:#172c3a;font:18px system-ui,sans-serif}main{max-width:1280px;margin:auto;padding:48px 32px}h1{font-size:44px;margin:0 0 12px}header{margin-bottom:36px}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(430px,1fr));gap:28px}article{background:white;padding:24px;border-radius:18px}h2{margin:6px 0;font-size:28px}.eyebrow{font-size:13px;letter-spacing:1px;color:#087f78;font-weight:700}video{width:100%;border-radius:10px}a{color:#087f78}p{line-height:1.5}@media(max-width:520px){.grid{grid-template-columns:1fr}main{padding:24px 16px}}</style><main><header><p class="eyebrow">WORKSHEET COMPANIONS</p><h1>A little help. One clear example.</h1><p>Short lessons with local narration and animated mathematical working, without subtitles.<br>Each example uses new numbers to teach a method from your worksheets.</p></header><section class="grid">'''+''.join(cards)+'</section></main></html>')


if __name__=='__main__':
    main()
