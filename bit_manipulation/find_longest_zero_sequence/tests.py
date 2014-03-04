#!/usr/bin/env python
import unittest
from find_longest_zero_sequence import find_longest_zero_sequence


class IsAnagramTest(unittest.TestCase):

    def test15(self):
        self.assertEqual(0, find_longest_zero_sequence(15))

    def test133(self):
        self.assertEqual(4, find_longest_zero_sequence(133))


if __name__ == '__main__':
    unittest.main()