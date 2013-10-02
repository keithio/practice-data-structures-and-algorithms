#!/usr/bin/env python
import unittest
from anagram import is_anagram


class IsAnagramTest(unittest.TestCase):

    def test_0(self):
        self.assertEqual(True, is_anagram('obo', 'boo'))

    def test_1(self):
        self.assertEqual(False, is_anagram('obo', 'bob'))

    def test_2(self):
        self.assertEqual(False, is_anagram('abc', 'xyz'))

    def test_3(self):
        self.assertEqual(True, is_anagram('mary', 'army'))


if __name__ == '__main__':
    unittest.main()