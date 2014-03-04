
#!/usr/bin/env python
import unittest
from find_lone_integer import find_lone_integer


class FindLoneIntegerTest(unittest.TestCase):

    def test_ordered(self):
        self.assertEqual(3, find_lone_integer([1, 1, 2, 2, 3, 5, 5]))

    def test_unordered(self):
        self.assertEqual(3, find_lone_integer([1, 5, 2, 5, 2, 1, 3]))


if __name__ == '__main__':
    unittest.main()