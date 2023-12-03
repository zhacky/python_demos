from unittest import TestCase

from codewars import pell_numbers


class Test(TestCase):

    def test_pell_1(self):
        # given
        n = 1
        expected = 1
        # when
        result = pell_numbers.pell(n)
        # then
        self.assertEqual(result, expected, "given 1 must result 1")

    def test_pell_2(self):
        # given
        n = 2
        expected = 2
        # when
        result = pell_numbers.pell(n)
        # then
        self.assertEqual(result, expected, "given 2 must result 2")

    def test_pell_3(self):
        # given
        n = 3
        expected = 5
        # when
        result = pell_numbers.pell(n)
        # then
        self.assertEqual(result, expected, "given 3 must result 5")

    def test_pell_4(self):
        # given
        n = 4
        expected = 12
        # when
        result = pell_numbers.pell(n)
        # then
        self.assertEqual(result, expected, "given 4 must result 12")


