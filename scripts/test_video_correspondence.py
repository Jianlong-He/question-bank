"""Regression checks for teaching-method boundaries and rebuilding saved work."""
import copy
import unittest
from build_video_correspondence import build, classify, digest, norm
from video_example_checks import example_collisions, signature


def method(question, topic='Arithmetic', grade=3):
    return classify(question, {'unit_topic':topic,'curriculum':{'kind':'grade','grade':grade,'unit':1}})[0]


class MethodTests(unittest.TestCase):
    def test_same_method_across_grades(self):
        self.assertEqual(method('Compute 25 + 37',grade=2),method('Compute 46 + 28',grade=5))

    def test_different_operations(self):
        self.assertNotEqual(method('Compute 25 + 37'),method('Compute 37 - 25'))

    def test_fraction_denominators(self):
        self.assertNotEqual(method('Compute 1/4 + 2/4'),method('Compute 1/4 + 2/5'))

    def test_shapes_and_inverse_questions(self):
        rectangle=method('A rectangle is 6 meters long and 3 meters wide. What is its area?')
        circle=method('Find the area of a circle of radius 5.')
        missing=method('A rectangle has area 30 square units. One side is 5 units long. What is the other side?')
        self.assertEqual(rectangle,'geometry-area-rectangle')
        self.assertNotEqual(rectangle,circle)
        self.assertNotEqual(rectangle,missing)

    def test_superscripts_keep_meaning(self):
        self.assertEqual(norm('3⁻²'),'3^(-2)')
        self.assertEqual(method('Compute 3⁻²'),'arithmetic-negative-exponents')
        self.assertNotEqual(method('Compute 4²'),method('Compute 4² + 3'))

    def test_systems_do_not_capture_given_constants(self):
        self.assertTrue(method('Solve y = 2x and x + y = 12').startswith('systems-solve'))
        self.assertFalse(method('Find the sum of the first 3 terms of a geometric sequence with a = 6 and r = 4.').startswith('systems'))

    def test_complex_shapes_are_geometry(self):
        self.assertEqual(method('A complex shape is split into a rectangle and a triangle. Find total area.'),'geometry-area-composite')

    def test_counting_group_sizes(self):
        self.assertNotEqual(method('Choose a committee of 2 from 8 students.'),method('Choose a committee of 3 from 8 students.'))

    def test_template_preserves_exponents(self):
        self.assertEqual(method('Mystery task 25 to x^2 now'),method('Mystery task 30 to x^2 now'))
        self.assertNotEqual(method('Mystery task 25 to x^2 now'),method('Mystery task 25 to x^3 now'))


class RebuildTests(unittest.TestCase):
    def setUp(self):
        self.path='worksheets/Grade 3/G3Unit 1/G3U1W1.csv'
        self.meta={'curriculum':{'kind':'grade','grade':3,'unit':1},'worksheet_number':'1','worksheet_variant':'practice','unit_topic':'Arithmetic'}
        self.inventory={self.path:(self.meta,[{'Question ID':'7','Question Choices':'Compute 25 + 37'}])}

    def test_preserves_checked_links_and_youtube(self):
        original,_,_=build({'videos':{}},self.inventory)
        p=original['worksheets'][self.path]['problems']['7']
        p['mapping_status']='reviewed'
        vid=p['video_links'][0]['video_id']
        original['videos'][vid]['youtube']={'video_id':'AbCdEfGhI12','visibility':'unlisted'}
        result,_,_=build(original,self.inventory)
        self.assertEqual(result['worksheets'][self.path]['problems']['7'],p)
        self.assertEqual(result['videos'][vid],original['videos'][vid])

    def test_changed_question_requires_review(self):
        original,_,_=build({'videos':{}},self.inventory)
        original['worksheets'][self.path]['problems']['7']['mapping_status']='reviewed'
        changed=copy.deepcopy(self.inventory)
        changed[self.path][1][0]['Question Choices']='Compute 47 - 26'
        result,_,_=build(original,changed)
        p=result['worksheets'][self.path]['problems']['7']
        self.assertEqual(p['mapping_status'],'needs_review')
        self.assertEqual(p['question_sha256'],digest('Compute 47 - 26'))
        self.assertIn('Question changed',p['notes'])

    def test_preserves_manual_correction_awaiting_example_review(self):
        original,_,_=build({'videos':{}},self.inventory)
        p=original['worksheets'][self.path]['problems']['7']
        p['mapping_method']='manual'
        p['notes']='Content reviewed; destination example still needs checking.'
        p['mapping_rule']='content-review'
        result,_,_=build(original,self.inventory)
        self.assertEqual(result['worksheets'][self.path]['problems']['7'],p)

    def test_variants_have_separate_links_when_methods_differ(self):
        self.inventory[self.path][1][0]['Question Choices']='Compute 25 + 37||Compute 47 - 26'
        result,_,_=build({'videos':{}},self.inventory)
        links=result['worksheets'][self.path]['problems']['7']['video_links']
        self.assertEqual([l['variant_index'] for l in links],[0,1])
        self.assertNotEqual(links[0]['video_id'],links[1]['video_id'])

    def test_rebuild_is_idempotent(self):
        original,_,_=build({'videos':{}},self.inventory)
        result,_,_=build(original,self.inventory)
        self.assertEqual(original,result)


class ExampleChecks(unittest.TestCase):
    def test_rectangular_measurement_copies_ignore_dimension_order(self):
        vid='geometry-area-rectangle'
        a='A rectangle is 8 cm long and 7 cm wide. Find its area.'
        b='A rectangular garden is 7 meters long and 8 meters wide. What is its area?'
        self.assertEqual(signature(a,vid),(vid,'7','8'))
        self.assertEqual(signature(a,vid),signature(b,vid))
        self.assertNotEqual(signature(a,vid),signature(b.replace('8 meters','9 meters'),vid))
        vid='geometry-volume-rectangular-prism'
        self.assertEqual(signature('Box: length 7 cm, width 5 cm, height 4 cm. Find volume.',vid),
                         signature('A rectangular tank is 4 m by 7 m by 5 m. Find volume in m³.',vid))

    def test_cube_side_and_three_equal_dimensions_match(self):
        vid='geometry-volume-cube'
        self.assertEqual(signature('A cube has side length 3 cm. Find its volume.',vid),(vid,'3','3','3'))
        self.assertEqual(signature('A cube has side length 3 cm. Find its volume.',vid),
                         signature('A cube measures 3 cm × 3 cm × 3 cm. Find its volume in cm³.',vid))

    def test_statistics_detects_reordered_dataset(self):
        vid='statistics-mean'
        self.assertEqual(signature('Find the mean of 6, 11, 8 and 15.',vid),signature('Data: 15, 8, 6, 11. Find the mean.',vid))
        self.assertNotEqual(signature('Find the mean of 6, 11, 8 and 15.',vid),signature('Data: 15, 8, 6, 6. Find the mean.',vid))

    def test_first_success_copy_cannot_just_rename_objects(self):
        vid='probability-first-success'
        a='5 red and 4 blue balls; no replacement. Find P(first red on draw 3).'
        b='A bowl contains 5 candies and 4 cockroaches. Cockroaches are not replaced. Find p(3), where X is the draw of the first candy.'
        self.assertEqual(signature(a,vid),('finite-first-success',5,4,3))
        self.assertEqual(signature(a,vid),signature(b,vid))
        self.assertNotEqual(signature(a,vid),signature(b.replace('p(3)','p(4)'),vid))
        self.assertIsNone(signature(b.replace('not replaced','replaced'),vid))

    def test_first_draw_collision_ignores_later_replacement(self):
        vid='probability-first-success-first'
        a='6 red and 5 blue balls. X is the draw of the first red. Find p(1).'
        b='6 candies and 5 cockroaches, with replacement. X is the draw of the first candy. Find p(1).'
        self.assertEqual(signature(a,vid),('first-draw',6,5))
        self.assertEqual(signature(a,vid),signature(b,vid))

    def test_hypergeometric_example_must_not_solve_the_favourable_count(self):
        vid='pattern-pmf-bfe65fc756d0'
        a='5 red and 6 blue balls; choose 4 uniformly. Find P(exactly 2 red), without replacement.'
        b='A bag contains 5 different red tokens and 6 different blue tokens. How many ways can 2 red and 2 blue tokens be selected?'
        self.assertEqual(signature(a,vid),('hypergeometric-counts',5,6,4,2))
        self.assertEqual(signature(a,vid),signature(b,vid))
        self.assertNotEqual(signature(a,vid),signature(a.replace('5 red and 6 blue','6 red and 7 blue'),vid))

    def test_general_combination_and_factorial_copies(self):
        self.assertEqual(signature('Choose a committee of 4 from 16 people.','counting-combinations'),signature('Evaluate C(16,4).','counting-combinations'))
        self.assertEqual(signature('Evaluate 8!.','counting-factorials'),('factorial',8))
        self.assertIsNone(signature('Evaluate 8!/(3!*5!).','counting-factorials'))
    def test_factor_pair_problem_ignores_operand_order(self):
        vid='number-theory-gcf'
        self.assertEqual(signature('Find the GCF of 42 and 70.',vid),signature('What is gcd(70,42)?',vid))

    def test_rounding_preserves_target_place(self):
        vid='number-rounding-whole'
        self.assertEqual(signature('Round 73 to the nearest ten.',vid),signature('Round 73 to the nearest 10.',vid))
        self.assertNotEqual(signature('Round 73 to the nearest ten.',vid),signature('Round 73 to the nearest hundred.',vid))

    def test_mixed_number_different_representation_still_overlaps(self):
        vid='fractions-mixed-improper'
        self.assertEqual(signature('Convert 4 3/7 to an improper fraction.',vid),signature('Convert 31/7 to a mixed number.',vid))
        self.assertNotEqual(signature('Convert 4 3/7 to an improper fraction.',vid),signature('Add 4 3/7 and 2 5/7.',vid))

    def test_fraction_comparison_ignores_list_order(self):
        vid='fractions-compare'
        self.assertEqual(signature('Which is larger: 7/12 or 5/8?',vid),signature('Compare 5/8 and 7/12.',vid))

    def test_modular_product_rejects_commuted_copy(self):
        vid='number-theory-modular-multiplication'
        self.assertEqual(signature('Find 17 × 14 (mod 9).',vid),signature('Find 14 * 17 modulo 9',vid))
        self.assertNotEqual(signature('Find 17 × 14 (mod 9).',vid),signature('Find 14 * 17 modulo 8',vid))

    def test_totient_does_not_confuse_factorial(self):
        vid='number-theory-euler-totient'
        self.assertEqual(signature('Find ϕ(45).',vid),signature('Calculate φ(45)',vid))
        self.assertNotEqual(signature('Find ϕ(45).',vid),signature('Calculate ϕ(45)!',vid))

    def test_inverse_and_fraction_notation(self):
        self.assertEqual(signature('Find inverse of 11 (mod26).','number-theory-modular-inverse'),('inverse',11,26))
        self.assertEqual(signature('Simplify 414/690 using Euclid.','number-theory-euclidean-algorithm'),('reduce-fraction',414,690))

    def test_choose_three_compares_worded_question_and_notation(self):
        vid='enrichment-counting-and-probability-1-choose-three'
        self.assertEqual(signature('How many teams of 3 can you choose from 6 students?',vid),signature('Evaluate 6C3.',vid))
        self.assertNotEqual(signature('How many teams of 3 can you choose from 12 students?',vid),signature('Evaluate 6C3.',vid))

    def test_modular_addition_preserves_modulus_and_ignores_operand_order(self):
        vid='enrichment-number-theory-1-modular-addition'
        self.assertEqual(signature('Find (8 + 9) mod 6.',vid),signature('Find 9 + 8 (mod 6)',vid))
        self.assertNotEqual(signature('Find (8 + 9) mod 6.',vid),signature('Find 9 + 8 (mod 7)',vid))

    def test_backward_counting_distinguishes_step_size(self):
        vid='g1-u1-counting-backward'
        self.assertNotEqual(signature('Count backward from 100 to 0',vid),signature('Count backward from 100 to 0 by tens',vid))

    def test_swapped_multiplication_factors_still_overlap(self):
        vid='g3-u1-equal-groups'
        self.assertEqual(signature('4 groups of 3 dots. How many dots?',vid),signature('How many in 3 groups of 4?',vid))
        self.assertNotEqual(signature('4 groups of 2 dots. How many dots?',vid),signature('How many in 3 groups of 4?',vid))

    def test_ratio_copy_despite_wording(self):
        vid='g6-u1-simplifying-ratios'
        self.assertEqual(signature('Simplify the ratio 8 : 12.',vid),signature('Simplify the ratio 8:12',vid))
        self.assertNotEqual(signature('Simplify the ratio 4:10',vid),signature('Simplify the ratio 8:12',vid))

    def test_combination_copy_despite_notation(self):
        vid='enrichment-counting-and-probability-1-choosing-a-pair'
        self.assertEqual(signature('How many teams of 2 can you choose from 5 students?',vid),signature('Evaluate 5C2.',vid))
        self.assertNotEqual(signature('How many teams of 2 can you choose from 4 students?',vid),signature('Evaluate 5C2.',vid))

    def test_only_linked_variants_are_checked(self):
        p={'question_text':'Compute 2 + 3||Compute 4 + 5','video_links':[{'video_id':'sample','variant_index':1}]}
        doc={'worksheets':{'worksheet.csv':{'problems':{'1':p}}}}
        self.assertFalse(example_collisions(doc,'sample','Compute 2 + 3'))
        self.assertTrue(example_collisions(doc,'sample','Compute 4 + 5'))


if __name__=='__main__':
    unittest.main()
