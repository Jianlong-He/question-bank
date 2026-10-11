import sys,unittest
sys.path.insert(0,'/Users/hejianlong/Desktop/loot-sheet/scripts')
from card_lessons import make_lessons,spec
class CatalogReferenceTests(unittest.TestCase):
 def setUp(self):
  self.spec=spec('review-demo','Demo','1+2','3','1+2','3','Find the sum',[('STEP','Add','1+2=3','Add one and two.')]*4)
  self.doc={'videos':{'review-demo':{'title':'Demo','production_status':'rendered','assets':{'mp4':'videos/demo.mp4'}}},'worksheets':{}}
 def link(self):self.doc['worksheets']={'worksheet.csv':{'curriculum':{'kind':'grade','grade':3,'unit':8},'problems':{'1':{'video_links':[{'video_id':'review-demo'}]}}}}
 def test_unlinked_completed_asset_is_preserved_without_generated_lesson(self):
  self.assertEqual(make_lessons([self.spec],self.doc),[]);self.assertEqual(self.doc['videos']['review-demo']['assets']['mp4'],'videos/demo.mp4')
 def test_unlinked_planned_is_rejected(self):
  self.doc['videos']['review-demo']['production_status']='planned'
  with self.assertRaisesRegex(AssertionError,'Unlinked unrendered'):make_lessons([self.spec],self.doc)
 def test_unlinked_missing_asset_is_rejected(self):
  self.doc['videos']['review-demo']['assets']['mp4']=None
  with self.assertRaisesRegex(AssertionError,'Unlinked unrendered'):make_lessons([self.spec],self.doc)
 def test_linked_rendered_still_loads(self):
  self.link();self.assertEqual(make_lessons([self.spec],self.doc)[0]['video_id'],'review-demo')
 def test_stale_explicit_anchor_is_still_rejected(self):
  self.link();self.spec['source_ref']=('other.csv','1')
  with self.assertRaisesRegex(AssertionError,'Source reference is not linked'):make_lessons([self.spec],self.doc)
if __name__=='__main__':unittest.main()
