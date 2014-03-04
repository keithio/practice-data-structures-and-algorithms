#!/usr/bin/env python
import unittest
from two_to_the import two_to_the


class TwoToTheTest(unittest.TestCase):

    def test0(self):
        self.assertEqual(1, two_to_the(0))

    def test1(self):
        self.assertEqual(2, two_to_the(1))

    def test2(self):
        self.assertEqual(4, two_to_the(2))

    def test3(self):
        self.assertEqual(8, two_to_the(3))


if __name__ == '__main__':
    unittest.main()