from unittest import TestCase

from codewars.camel_case import toCamelCase


class Test(TestCase):
    def test_to_camel_case(self):
        # given
        word = 'the_stealth_warrior'
        expected = 'theStealthWarrior'
        # when
        actual = toCamelCase(word=word)
        # then
        self.assertEqual(expected, actual, 'test if word is converted to camel case')

