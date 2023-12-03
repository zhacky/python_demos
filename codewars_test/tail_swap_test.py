from unittest import TestCase

from codewars.tail_swap import tail_swap


class Test(TestCase):

    def test_tail_swap(self):
        sample_test_cases = [
            #     strings                 expected
            (['abc:123', 'cde:456'], ['abc:456', 'cde:123']),
            (['a:12345', '777:xyz'], ['a:xyz', '777:12345']),
        ]
        for strings, expected in sample_test_cases:
            TestCase.assertEqual(self, expected, tail_swap(strings))
