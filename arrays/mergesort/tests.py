#!/usr/bin/env python
import unittest
from mergesort import mergesort


class MergeSortTest(unittest.TestCase):

    def test1(self):
        stimulus = [3, 2, 1]
        response = [1, 2, 3]
        self.assertEqual(response, mergesort(stimulus))

    def test2(self):
        stimulus = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3]
        response = [1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8, 9, 9, 9]
        self.assertEqual(response, mergesort(stimulus))


if __name__ == '__main__':
    unittest.main()