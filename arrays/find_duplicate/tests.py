#!/usr/bin/env python
import unittest
from find_duplicate import find_duplicate


class FindDuplicateTest(unittest.TestCase):

    def test1(self):
        stimulus = [3, 2, 1]
        self.assertEqual([], find_duplicate(stimulus))

    def test2(self):
        stimulus = [2, 1, 3, 1]
        self.assertEqual([1], find_duplicate(stimulus))


if __name__ == '__main__':
    unittest.main()