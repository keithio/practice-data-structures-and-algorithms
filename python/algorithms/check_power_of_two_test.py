#!/usr/bin/env python
import unittest
from check_power_of_two import check_power_of_two


class CheckPowerOfTwoTest(unittest.TestCase):

    def test_0(self):
        self.assertEqual(True, check_power_of_two(0))

    def test_1(self):
        self.assertEqual(True, check_power_of_two(1))

    def test_2(self):
        self.assertEqual(True, check_power_of_two(2))

    def test_3(self):
        self.assertEqual(False, check_power_of_two(3))

    def test_4(self):
        self.assertEqual(True, check_power_of_two(4))

    def test_5(self):
        self.assertEqual(False, check_power_of_two(5))

    def test_63(self):
        self.assertEqual(False, check_power_of_two(63))

    def test_64(self):
        self.assertEqual(True, check_power_of_two(64))



if __name__ == '__main__':
    unittest.main()