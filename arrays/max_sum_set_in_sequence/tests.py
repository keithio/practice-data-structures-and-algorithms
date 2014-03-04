#!/usr/bin/env python
import unittest
from max_sum_set_in_sequence import max_sum_set_in_sequence as mssis


class ShuffleTest(unittest.TestCase):

    def test1(self):
        stimulus = (1, -3, 5, 2, 9, -8, -6, 4)
        response = (16, (5, 2, 9))
        self.assertEqual(response, mssis(stimulus))

    def test2(self):
        stimulus = (-9, -11, -10, -3, -4, -13)
        response = (-3, (-3,))
        self.assertEqual(response, mssis(stimulus))

    def test3(self):
        stimulus = (9, -11, 10, -3, 4, 8)
        response = (19, (10, -3, 4, 8))
        self.assertEqual(response, mssis(stimulus))

    def test4(self):
        stimulus = (12, -10, 11, -5, 4, -2)
        response = (13, (12, -10, 11))
        self.assertEqual(response, mssis(stimulus))

    def test5(self):
        stimulus = (12, -10, 11, -5, 4, 2)
        response = (14, (12, -10, 11, -5, 4, 2))
        self.assertEqual(response, mssis(stimulus))


if __name__ == '__main__':
    unittest.main()