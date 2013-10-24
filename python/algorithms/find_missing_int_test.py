#!/usr/bin/env python
import unittest
from find_missing_int import find_missing_int


class FindMissingIntTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(7, find_missing_int(5, '1 3 5 9 11'))

    def test2(self):
        self.assertEqual(21, find_missing_int(5, '1 11 31 41 51'))


if __name__ == '__main__':
    unittest.main()