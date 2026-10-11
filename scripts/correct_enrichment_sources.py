"""Apply the eleven user-authorized enrichment corrections and sync the T7 index.

Run with --output pointing at the canonical videos folder. --check changes no files.
A before/after journal preserves every original changed row and problem mapping.
"""
import argparse,copy,csv,fcntl,hashlib,io,json
from pathlib import Path
from build_video_correspondence import ROOT,read_inventory,validate,digest
from generate_video_batch import save_json,update_overview
from review_enrichment_source_corrections_mappings import apply_review
from enrichment_source_corrections_lessons import SPECS,lessons
from video_example_checks import require_analogous_examples
from video_reuse import append_upload_row,update_reuse_checklist
from number_theory_lessons import source

BASE='worksheets/enrichment/number-theory 1/'
CORRECTIONS={}
def correction(topic,worksheet,qid,video,question,answer,hint,solution):
    CORRECTIONS[source(topic,worksheet,qid)]={
      'video_id':video,'fields':{'Question Choices':question,'Question Answers':answer,'Hints':hint,'Solution':solution}}

correction('CRT',4,2,'modular-common-remainder-bound',
 'A marching band forms rows of 5 with 3 people left over or rows of 7 with 3 people left over. There is at least one complete row in each arrangement. What is the smallest number of people?',
 '38','Subtract the common remainder, then use lcm(5,7). The complete-row condition excludes a band of only 3 people.',
 'Since x − 3 is divisible by both 5 and 7, x = 35k + 3 for an integer k. A band of 3 people cannot form a complete row, so the smallest allowed k is 1. Thus x = 38 (7 rows of 5 or 5 rows of 7, with 3 left over).')
correction('CRT',4,3,'modular-common-remainder-bound',
 "A baker has more than 5 cookies. Grouping them by 3, 4, or 5 always leaves 2 cookies remaining. What is the smallest possible number of cookies?",
 '62','Subtract 2, then use lcm(3,4,5). The total must be more than 5.',
 'Since x − 2 is divisible by 3, 4, and 5, x = 60k + 2 for an integer k. The condition x > 5 excludes k = 0 and all negative k. The smallest allowed k is 1, giving 62 cookies.')
correction('CRT',4,4,'crt-future-event-offsets',
 'Three bells toll every 3, 4, and 5 minutes, respectively. Their next tolls are in 1, 2, and 3 minutes, respectively. How many minutes from now will they first all toll at once?',
 '58','',
 'The time t satisfies t ≡ 1 (mod 3), t ≡ 2 (mod 4), and t ≡ 3 (mod 5). Each remainder is 2 less than its modulus, so t + 2 is divisible by 3, 4, and 5. Thus t = 60k − 2. The smallest positive time is 58 minutes (k = 1); later simultaneous tolls occur every 60 minutes.')
correction('Euclidean-division',3,1,'gcf-impossible-integer-target',
 'Select. Do integers x and y exist such that 12x + 18y = 1? ~~Yes | No~~',
 'No','gcd(12,18) = 6. Every integer combination of 12 and 18 is divisible by 6.',
 'No. For integer x and y, 12x + 18y = 6(2x + 3y) is divisible by 6, whereas 1 is not.')
correction('Euclidean-division',4,4,'number-theory-modular-inverse',
 'Select all that are true. Noting that 3*3 + 4*(-2) = 1, which statements are true? A) 3 is an inverse of 3 (mod 4), B) 2 is an inverse of 4 (mod 3), C) 3 is an inverse of 3 (mod 2): ~~A | B | C~~',
 'A, C','For each statement, multiply the two numbers and check whether the remainder is 1 in the stated modulus.',
 'A and C are true. A: 3*3 = 9 ≡ 1 (mod 4). B is false because 4*2 = 8 ≡ 2 (mod 3). C: 3*3 = 9 ≡ 1 (mod 2). An inverse may be represented by any integer in its congruence class.')
correction('modular-arithmetic',4,1,'modular-numbered-clock-events',
 'The Space Mission: A satellite passes over your house every 8 hours. Count its pass at 2:00 as the first pass. What time on a 12-hour clock will its fifth pass be?',
 '10:00','The first pass is already at 2:00, so the fifth pass is 4 intervals later.',
 'There are 5 − 1 = 4 intervals before the fifth pass. The elapsed time is 4 × 8 = 32 hours. On a 12-hour clock, 2 + 32 = 34 ≡ 10 (mod 12), so the fifth pass is at 10:00.')
correction('modular-arithmetic',4,6,'modular-weekday-offset',
 'Weekday Shifts: In this simplified calendar example, ignore leap days and assume every birthday-to-birthday interval is exactly 365 days. Your birthday is on Tuesday now. What weekday will it be after one such interval? What weekday will it be after ten such intervals?',
 'Wednesday,Friday|wednesday,friday','An interval of exactly 365 days shifts the weekday by 365 mod 7 = 1. Reduce the total shift modulo 7.',
 'Since 365 mod 7 = 1, one interval shifts Tuesday to Wednesday. Ten intervals shift the weekday by 10 mod 7 = 3 days, from Tuesday to Friday. Answers: Wednesday, Friday. This example assumes no leap days.')
correction('modular-arithmetic',4,7,'modular-circular-movement',
 'The Color Sequence: A computer chip advances one position every millisecond through 8 colors at positions 0 to 7, wrapping from position 7 back to 0. It starts on Red at position 0. What position is it in after 1,003 single-position advances?',
 '3|position 3|Position 3','A full cycle contains 8 single-position advances. Divide 1003 by 8 and use the remainder.',
 '1,003 = 8 × 125 + 3. After 125 full cycles the chip is back at position 0; 3 more advances take it to position 3.')
correction('modular-arithmetic','4HWb',2,'modular-rigid-square-rotation',
 'A rigid square has fixed side labels: 1 at the top, 2 on the right, 3 at the bottom, and 4 on the left. Rotate the whole square clockwise through 15 quarter-turns. Which label is now at the top?',
 '2','One clockwise quarter-turn brings the left side to the top. Track the top label, then use 15 mod 4.',
 'The top-label sequence after successive clockwise quarter-turns is 1 → 4 → 3 → 2 → 1. Since 15 = 4 × 3 + 3, remove three full revolutions and make three more quarter-turns. The top label is 2.')
correction('number-theory1_review',1,2,'modular-unknown-modulus',
 r'Find the smallest positive integer $n$ such that $4\times 9\equiv 3\pmod n$, where $3\in\{0,...,n-1\}$.',
 '11|mod 11',r'Compute 4 times 9 and subtract 3;The modulus must divide 33;The stated remainder range requires n > 3',
 r'Since $4\times 9=36$, the congruence requires $n$ to divide $36-3=33$. The positive divisors are 1, 3, 11, and 33. The condition $3\in\{0,...,n-1\}$ requires $n>3$. The smallest allowed divisor is 11.')
correction('number-theory1_review',1,3,'modular-unknown-modulus',
 'Find the two smallest distinct integers n and m, both greater than 8, such that 8 is its own multiplicative inverse modulo each of n and m.',
 '9, 21|21, 9',r'For 8 to be its own inverse, $8\times 8\equiv 1\pmod k$;Thus k divides 63;Find the two smallest divisors of 63 greater than 8',
 r'The condition $8\times 8\equiv 1\pmod k$ means $k$ divides $64-1=63$. The positive divisors of 63 are 1, 3, 7, 9, 21, and 63. Those greater than 8 are 9, 21, and 63, so the two smallest distinct choices are 9 and 21.')


def prepare_csv(path,changes):
    """Preserve every untouched CSV record byte-for-byte, including the BOM."""
    original=path.read_bytes();bom=b'\xef\xbb\xbf' if original.startswith(b'\xef\xbb\xbf') else b''
    text=original[len(bom):].decode('utf-8');lines=text.splitlines(keepends=True)
    reader=csv.reader(io.StringIO(text,newline=''));header=next(reader);end=reader.line_num
    pieces=[''.join(lines[:end])];records=[]
    for values in reader:
        start=end;end=reader.line_num;raw=''.join(lines[start:end]);row=dict(zip(header,values))
        qid=row['Question ID']
        if qid in changes:
            before=row.copy();row.update(changes[qid]['fields'])
            ending='\r\n' if raw.endswith('\r\n') else '\n' if raw.endswith('\n') else ''
            buffer=io.StringIO(newline='');csv.writer(buffer,lineterminator=ending or '\n').writerow([row[h] for h in header]);raw=buffer.getvalue()
            if not ending:raw=raw.rstrip('\n')
            records.append({'question_id':qid,'before':before,'after':row})
        pieces.append(raw)
    updated=bom+''.join(pieces).encode('utf-8')
    assert len(records)==len(changes)
    return original,updated,records


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True,type=Path);parser.add_argument('--check',action='store_true');args=parser.parse_args()
    with (ROOT/'videos/.production.lock').open('a+') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        path=args.output/'worksheet-video-correspondence.json';doc=json.loads(path.read_text());before=copy.deepcopy(doc)
        assert not any(v['production_status']=='in_progress' for v in doc['videos'].values())
        inventory=read_inventory();staged={};journal=[]
        for file in sorted({f for f,q in CORRECTIONS}):
            changes={q:c for (f,q),c in CORRECTIONS.items() if f==file}
            old,new,records=prepare_csv(ROOT/file,changes);staged[file]=(old,new)
            for rec in records:
                qid=rec['question_id'];rec.update(worksheet=file,video_id=CORRECTIONS[(file,qid)]['video_id'],before_mapping=copy.deepcopy(doc['worksheets'][file]['problems'][qid]));journal.append(rec)
            meta,rows=inventory[file]
            for row in rows:
                if row['Question ID'] in changes:row.update(changes[row['Question ID']]['fields'])
        apply_review(doc)
        for (file,qid),c in CORRECTIONS.items():
            p=doc['worksheets'][file]['problems'][qid];q=c['fields']['Question Choices']
            assert len(p['video_links'])==1
            p['video_links'][0]['video_id']=c['video_id']
            p.update(question_text=q,question_sha256=digest(q),mapping_status='reviewed',mapping_method='manual',mapping_rule='enrichment-source-corrections-20261008',requires_source_visual=False,
                     notes='Source wording, accepted answers, hints, and solution corrected with user authorization on 2026-10-08. Rechecked against the corresponding analogous teaching example.')
        validate(doc,inventory,asset_root=args.output.parent);require_analogous_examples(doc,lessons(doc))
        for vid in {c['video_id'] for c in CORRECTIONS.values()}:
            v=doc['videos'][vid]
            if v['production_status']=='rendered':require_analogous_examples(doc,[{'video_id':vid,'question':v['example']['question']}])
        assert all((v['youtube'],v['assets'])==(doc['videos'][vid]['youtube'],doc['videos'][vid]['assets']) for vid,v in before['videos'].items())
        content=(args.output/'youtube-upload-checklist.md').read_text()
        for vid in sorted(set(doc['videos'])-set(before['videos'])):content=append_upload_row(content,vid,doc['videos'][vid]['title'])
        if not args.check:
            journalpath=args.output/'enrichment-source-corrections-2026-10-08.json'
            if not journalpath.exists():save_json(journalpath,{'date':'2026-10-08','corrections':journal})
            for file,(old,new) in staged.items():
                assert (ROOT/file).read_bytes()==old
                if old!=new:(ROOT/file).write_bytes(new)
            save_json(path,doc);(args.output/'youtube-upload-checklist.md').write_text(update_reuse_checklist(content,doc));update_overview(args.output,doc,[s['video_id'] for s in SPECS])
        print(f'Validated 11 corrections across {len(staged)} CSVs; all corresponding question hashes and video links synchronized. Check only: {args.check}')

if __name__=='__main__':main()
