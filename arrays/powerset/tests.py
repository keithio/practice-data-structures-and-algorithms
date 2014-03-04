#!/usr/bin/env python
import unittest
from powerset import get_powerset


class PowersetTest(unittest.TestCase):

    def test1(self):
        stimulus = [1, 2, 3]
        response = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
        self.assertEqual(response, get_powerset(stimulus))


if __name__ == '__main__':
    unittest.main()