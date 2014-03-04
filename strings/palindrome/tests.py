#!/usr/bin/env python
import unittest
from palindrome import is_palindrome


class IsPalindromeTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(True, is_palindrome('Able was I ere I saw Elba'))

    def test2(self):
        self.assertEqual(True, is_palindrome('A man, a plan, a canal - Panama!'))

    def test3(self):
        self.assertEqual(True, is_palindrome('Madam, I\'m Adam'))

    def test4(self):
        self.assertEqual(False, is_palindrome('My name is Keith.'))


if __name__ == '__main__':
    unittest.main()