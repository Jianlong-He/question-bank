"""Failure, cancellation, overlap and resumability checks for production scheduling."""
import tempfile
import unittest
import json
from pathlib import Path
from threading import Event
from unittest.mock import patch
from video_pipeline import ready_lessons, pending_lessons
from prepare_video_review_batch import arithmetic_check
from lesson_catalogs import load_catalogs, load_catalog, CATALOGS


class PipelineTests(unittest.TestCase):
    def test_render_can_start_before_second_narration_finishes(self):
        rendering = Event()
        def prepare(items, publish, stop):
            publish(items[0])
            if not rendering.wait(2):raise RuntimeError('Renderer did not overlap preparation')
            publish(items[1])
        iterator = ready_lessons(['first', 'second'], prepare)
        self.assertEqual(next(iterator), 'first')
        rendering.set()
        self.assertEqual(list(iterator), ['second'])

    def test_speech_failure_is_propagated_after_ready_work(self):
        def prepare(items, publish, stop):
            publish('ready')
            raise RuntimeError('Voice failure')
        iterator = ready_lessons([], prepare)
        self.assertEqual(next(iterator), 'ready')
        with self.assertRaisesRegex(RuntimeError, 'Voice failure'):next(iterator)

    def test_cancel_unblocks_a_full_queue(self):
        stopped = Event()
        def prepare(items, publish, stop):
            for item in range(50):
                if stop.is_set():break
                publish(item)
            stopped.set()
        iterator = ready_lessons([], prepare)
        next(iterator)
        iterator.close()
        self.assertTrue(stopped.is_set())

    def test_serial_prepares_all_before_yielding(self):
        done = Event()
        def prepare(items, publish, stop):
            for item in items:publish(item)
            done.set()
        iterator = ready_lessons([1, 2], prepare, overlap=False)
        self.assertEqual(next(iterator), 1)
        self.assertTrue(done.is_set())
        self.assertEqual(list(iterator), [2])

    def test_resume_retries_missing_interrupted_and_revision_exports(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder);(root/'present.mp4').touch()
            cases = [('done', 'rendered', 'present.mp4'),
                     ('missing', 'rendered', 'gone.mp4'),
                     ('crashed', 'in_progress', None),
                     ('revision', 'needs_revision', 'present.mp4')]
            doc = {'videos': {vid: {'production_status': status, 'assets': {'mp4': path}}
                              for vid, status, path in cases}}
            lessons = [{'video_id': vid} for vid, _, _ in cases]
            self.assertEqual([l['video_id'] for l in pending_lessons(lessons, doc, root)],
                             ['missing', 'crashed', 'revision'])

    def test_arithmetic_check_finds_bad_key_without_approving_word_problems(self):
        row={'Question Choices':'What is 64 - 28?', 'Question Answers':'46'}
        result=arithmetic_check(row)
        self.assertEqual(result['status'],'numeric_key_mismatch')
        self.assertEqual(result['computed_answer'],'36')
        row['Question Answers']='36|36 puzzles'
        self.assertEqual(arithmetic_check(row)['status'],'numeric_key_matches')
        row['Question Choices']='Maria trades 20 rocks. How many are left?'
        self.assertEqual(arithmetic_check(row)['status'],'manual_review_required')

    def test_merged_catalogs_reject_conflicting_video_ids(self):
        with patch('lesson_catalogs.load_catalog',return_value=[{'video_id':'same'}]):
            with self.assertRaisesRegex(ValueError,'Duplicate video'):
                load_catalogs(['catalog-a','catalog-b'],{})
            self.assertEqual(load_catalogs(['catalog-a','catalog-a'],{}),[{'video_id':'same'}])

    def test_json_catalog_validates_math_before_returning_lessons(self):
        from algebra_lessons import authored
        vid='fixture-add';source='worksheets/fixture.csv'
        spec=authored(vid,'Add two numbers','What is 2 + 3?','5','Add two and three.',
            [('STEP','Add','2 + 3 = 5','Two plus three is five.')]*4,
            (source,'1'),expression='2+3',value='5')
        doc={'videos':{vid:{'title':'Add two numbers'}},'worksheets':{source:{
            'curriculum':{'kind':'grade','grade':2,'unit':1},
            'problems':{'1':{'video_links':[{'video_id':vid}]}}}}}
        with tempfile.TemporaryDirectory() as folder:
            path=Path(folder)/'catalog.json';path.write_text(json.dumps([spec]))
            with patch.dict(CATALOGS,{'fixture':str(path)}):
                self.assertEqual(load_catalog('fixture',doc)[0]['answer'],'5')
                spec['answer_value']='6';path.write_text(json.dumps([spec]))
                with self.assertRaises(AssertionError):load_catalog('fixture',doc)


if __name__ == '__main__':unittest.main()
