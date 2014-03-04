#!/usr/bin/env python
import unittest
from integer_swap import integer_swap


class IntegerSwapTest(unittest.TestCase):

    def test_1_2(self):
        self.assertEqual((2, 1), integer_swap(1, 2))

    def test_3_0(self):
        self.assertEqual((0, 3), integer_swap(3, 0))



if __name__ == '__main__':
    unittest.main()