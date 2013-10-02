#!/usr/bin/env python
import unittest
from longest_common_substring import longest_common_substring


class LongestCommonSubstringTest(unittest.TestCase):

    def test_string1_empty(self):
        self.assertEqual('', longest_common_substring('string1', ''))

    def test_empty_string2(self):
        self.assertEqual('', longest_common_substring('', 'string2'))

    def test_string1_string2(self):
        self.assertEqual('string', longest_common_substring('string1',
                                                            'string2'))

    def test_animal_mallard(self):
        self.assertEqual('mal', longest_common_substring('animal', 'mallard'))


if __name__ == '__main__':
    unittest.main()