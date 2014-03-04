#!/usr/bin/env python
import unittest
from find_max_circular import find_max_circular


class FindMaxCircularTest(unittest.TestCase):

    def test1(self):
        stimulus = [0, 1, 2, 3, 4, 5]
        response = 5
        self.assertEqual(response, find_max_circular(stimulus))

    def test2(self):
        stimulus = [2, 3, 4, 5, 0, 1]
        response = 5
        self.assertEqual(response, find_max_circular(stimulus))

    def test3(self):
        stimulus = [4, 5, 0, 1, 2, 3]
        response = 5
        self.assertEqual(response, find_max_circular(stimulus))


if __name__ == '__main__':
    unittest.main()