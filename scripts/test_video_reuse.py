import copy
import unittest
from video_reuse import merge_reviewed_duplicate,update_reuse_checklist,validate_reuse

class ReuseTests(unittest.TestCase):
    def setUp(self):
        self.doc={'videos':{
          'old':{'production_status':'planned','youtube':{'video_id':None},'assets':{'mp4':None,'captions':None},'planning':{'review_status':'needs_review'}},
          'shared':{'production_status':'rendered','youtube':{'video_id':'Abc12345678'},'assets':{'mp4':'videos/shared.mp4'}}},
          'worksheets':{'file':{'problems':{'1':{'requires_source_visual':False,'video_links':[{'video_id':'old'}]}}}}}
    def merge(self):merge_reviewed_duplicate(self.doc,'old',{('file','1'):'shared'})
    def test_keeps_ids_and_uploaded_destination(self):
        shared=copy.deepcopy(self.doc['videos']['shared']);self.merge();validate_reuse(self.doc)
        self.assertEqual(self.doc['videos']['shared'],shared)
        self.assertEqual(set(self.doc['videos']),{'old','shared'})
        self.assertEqual(self.doc['videos']['old']['reuse_video_ids'],['shared'])
        self.assertEqual(self.doc['worksheets']['file']['problems']['1']['video_links'],[{'video_id':'shared'}])
    def test_protects_uploaded_or_rendered_draft(self):
        for field,value in [('youtube',{'video_id':'Abc12345678'}),('assets',{'mp4':'old.mp4'})]:
            with self.subTest(field=field):
                doc=copy.deepcopy(self.doc);doc['videos']['old'][field]=value;before=copy.deepcopy(doc)
                with self.assertRaises(AssertionError):merge_reviewed_duplicate(doc,'old',{('file','1'):'shared'})
                self.assertEqual(doc,before)
    def test_requires_all_references_and_completed_target(self):
        before=copy.deepcopy(self.doc)
        with self.assertRaises(AssertionError):merge_reviewed_duplicate(self.doc,'old',{})
        self.assertEqual(self.doc,before)
        self.doc['videos']['shared']['production_status']='planned';before=copy.deepcopy(self.doc)
        with self.assertRaises(AssertionError):self.merge()
        self.assertEqual(self.doc,before)
    def test_validator_rejects_retired_links_and_reuse_chains(self):
        self.merge();self.doc['worksheets']['file']['problems']['1']['video_links'][0]['video_id']='old'
        with self.assertRaises(AssertionError):validate_reuse(self.doc)
        self.doc['worksheets']['file']['problems']['1']['video_links'][0]['video_id']='shared'
        self.doc['videos']['shared']['reuse_video_ids']=['old']
        with self.assertRaises(AssertionError):validate_reuse(self.doc)
    def test_checklist_preserves_active_ids_and_is_idempotent(self):
        self.merge()
        s='All 2 videos in the current plan.\n| Old | old.mp4 |  |\n| Shared | shared.mp4 | Abc12345678 |\n'
        result=update_reuse_checklist(s,self.doc)
        self.assertIn('| Shared | shared.mp4 | Abc12345678 |',result)
        self.assertNotIn('| old.mp4 |',result)
        self.assertIn('`old` → `shared.mp4`',result)
        self.assertEqual(update_reuse_checklist(result,self.doc),result)
        with self.assertRaises(AssertionError):update_reuse_checklist(s.replace('| old.mp4 |  |','| old.mp4 | Xyz12345678 |'),self.doc)
    def test_new_upload_row_stays_above_reuse_footer(self):
        from video_reuse import append_upload_row
        self.merge();s=update_reuse_checklist('| Old | old.mp4 |  |\n| Shared | shared.mp4 |  |\n',self.doc)
        result=append_upload_row(s,'new','New')
        self.assertLess(result.index('| new.mp4 |'),result.index('## Shared video reuse'))

    def test_mixed_template_can_reuse_two_completed_methods(self):
        self.doc['videos']['second']=copy.deepcopy(self.doc['videos']['shared'])
        self.doc['worksheets']['file']['problems']['2']=copy.deepcopy(self.doc['worksheets']['file']['problems']['1'])
        merge_reviewed_duplicate(self.doc,'old',{('file','1'):'shared',('file','2'):'second'})
        validate_reuse(self.doc)
        self.assertEqual(self.doc['videos']['old']['reuse_video_ids'],['second','shared'])
        self.assertEqual(self.doc['worksheets']['file']['problems']['2']['video_links'][0]['video_id'],'second')

    def test_existing_reuse_survives_a_target_media_revision(self):
        self.merge();self.doc['videos']['shared']['production_status']='needs_revision'
        validate_reuse(self.doc)
        self.doc['videos']['shared']['assets']['mp4']=None
        with self.assertRaises(AssertionError):validate_reuse(self.doc)

if __name__=='__main__':unittest.main()
