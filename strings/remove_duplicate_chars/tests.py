#!/usr/bin/env python
import unittest
from remove_duplicate_chars import remove_duplicate_chars


class RemoveDuplicateCharsTest(unittest.TestCase):

    def test_aaaa(self):
        """
        Make sure the correct output is generated.
        """
        self.assertEqual('a', remove_duplicate_chars('aaaa'))

    def test_aabbb(self):
        """
        Make sure the correct output is generated.
        """
        self.assertEqual('ab', remove_duplicate_chars('aabbb'))


if __name__ == '__main__':
    unittest.main()