"""Bounded producer/consumer scheduling; only the caller writes the manifest."""
from concurrent.futures import ThreadPoolExecutor
from queue import Queue, Empty, Full
from threading import Event


def ready_lessons(lessons, prepare, overlap=True):
    """Yield each lesson after preparation. Propagate failures and cancel on close.

    prepare receives (lessons, on_ready, stop_event). One producer owns the voice
    model. The caller owns rendering and every manifest/checklist update.
    """
    stop = Event()
    if not overlap:
        ready = []
        prepare(lessons, ready.append, stop)
        yield from ready
        return
    queue = Queue(maxsize=2)

    def publish(lesson):
        while not stop.is_set():
            try:
                queue.put(lesson, timeout=.1)
                return
            except Full:
                pass

    with ThreadPoolExecutor(max_workers=1, thread_name_prefix='local-narration') as pool:
        future = pool.submit(prepare, lessons, publish, stop)
        try:
            while True:
                try:
                    yield queue.get(timeout=.1)
                except Empty:
                    if future.done():
                        future.result()
                        return
        finally:
            stop.set()


def pending_lessons(batch, doc, asset_root):
    """Skip only completed exports that still exist; interrupted work is retryable."""
    return [lesson for lesson in batch
            if not (doc['videos'][lesson['video_id']]['production_status'] == 'rendered'
                    and doc['videos'][lesson['video_id']]['assets']['mp4']
                    and (asset_root / doc['videos'][lesson['video_id']]['assets']['mp4']).is_file())]
