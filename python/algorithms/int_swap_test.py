#!/usr/bin/env python
import unittest
from int_swap import int_swap


class IntSwapTest(unittest.TestCase):

    def test_1_2(self):
        self.assertEqual((2, 1), int_swap(1, 2))

    def test_3_0(self):
        self.assertEqual((0, 3), int_swap(3, 0))



if __name__ == '__main__':
    unittest.main()