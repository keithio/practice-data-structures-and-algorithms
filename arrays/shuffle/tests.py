#!/usr/bin/env python
import unittest
from shuffle import shuffle


class ShuffleTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(sum(range(5)), sum(shuffle(range(5))))


if __name__ == '__main__':
    unittest.main()