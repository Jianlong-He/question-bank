"""Synthesize speech OFFLINE with Kokoro. Run with --all for all eight samples.

Local dependencies: .video-tools/python (kokoro-onnx, soundfile).
Model assets: .video-tools/models/kokoro-v1.0.onnx and voices-v1.0.bin.
Downloads are a separate setup step; this script blocks network connections.
"""
import argparse
import asyncio
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '.video-tools/python'))


def reject_network(event, args):
    if event in {'socket.connect', 'socket.getaddrinfo'}:
        raise RuntimeError('Narration is offline: network access is disabled.')


sys.addaudithook(reject_network)

import numpy as np
import onnxruntime as ort
ort.disable_telemetry_events()
import soundfile as sf
from kokoro_onnx import Kokoro
from generate_sample_videos import LESSONS, VOICE_RATE, narration_path, probe


def make_engine():
    model_dir=ROOT/'.video-tools/models'
    options=ort.SessionOptions()
    options.intra_op_num_threads=4
    options.inter_op_num_threads=1
    options.enable_mem_pattern=False
    session=ort.InferenceSession(str(model_dir/'kokoro-v1.0.onnx'),sess_options=options,providers=['CPUExecutionProvider'])
    engine=Kokoro.from_session(session,str(model_dir/'voices-v1.0.bin'))
    return engine


def synthesize(lessons, on_ready=None, stop_event=None, metrics=None):
    import time
    engine=None
    for lesson in lessons:
        if stop_event and stop_event.is_set():return
        started=time.perf_counter();generated=0
        for index, (_, _, speech) in enumerate(lesson['scenes']):
            if stop_event and stop_event.is_set():return
            target = narration_path(lesson, index)
            if target.exists():
                assert float(probe(target)['format']['duration']) > .5
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            temporary = target.with_suffix('.pending.wav')
            if engine is None:engine=make_engine()
            samples,rate=engine.create(speech,voice='af_heart',speed=VOICE_RATE,lang='en-us')
            assert rate==24000 and np.isfinite(samples).all()
            assert len(samples)>rate*.5 and np.max(np.abs(samples))>.01
            # Keep headroom while making the voice level consistent across scenes.
            peak=float(np.max(np.abs(samples)))
            samples=samples*(0.82/peak)
            sf.write(str(temporary),samples,rate,subtype='PCM_16')
            temporary.replace(target)
            generated+=1
            print(f"Ready locally: {lesson['slug']}, step {index+1} ({len(samples)/rate:.1f}s)",flush=True)

        if metrics is not None:metrics.append({'video_id':lesson['video_id'],'speech_seconds':round(time.perf_counter()-started,3),'scenes_generated':generated})
        if on_ready:on_ready(lesson)


async def main(lessons=LESSONS):
    synthesize(lessons)


if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--all',action='store_true')
    args=parser.parse_args()
    lessons=list(LESSONS)
    if args.all:
        from generate_enrichment_videos import LESSONS as enrichment
        lessons+=enrichment
    asyncio.run(main(lessons))
