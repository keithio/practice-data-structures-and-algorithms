#!/usr/bin/env python
import unittest
from binary_search import binary_search


class BinarySearchTest(unittest.TestCase):

    def test_good(self):
        self.assertEqual(1, binary_search(range(1, 5), 2))

    def test_bad(self):
        self.assertEqual(-1, binary_search(range(1, 5), 9))


if __name__ == '__main__':
    unittest.main()