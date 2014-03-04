#!/usr/bin/env python
import unittest
from find_missing_int import find_missing_int


class FindMissingIntTest(unittest.TestCase):

    def test1(self):
        stimulus = ('5', '1 3 5 9 11')
        response = 7
        self.assertEqual(response, find_missing_int(*stimulus))

    def test2(self):
        stimulus = ('5', '1 11 31 41 51')
        response = 21
        self.assertEqual(response, find_missing_int(*stimulus))

    def test3(self):
        stimulus = ('5', '-20 -10 10 20 30')
        response = 0
        self.assertEqual(response, find_missing_int(*stimulus))

    def test4(self):
        stimulus = ('5', '-50 -40 -30 -10 0')
        response = -20
        self.assertEqual(response, find_missing_int(*stimulus))


if __name__ == '__main__':
    unittest.main()