import unittest
from reverse_string import reverse_string


class TestReverseString(unittest.TestCase):

    def test1(self):
        self.assertEqual('cba', reverse_string('abc'))

    def test2(self):
        self.assertEqual('zyx', reverse_string('xyz'))

    def test3(self):
        self.assertEqual('htieK', reverse_string('Keith'))


if __name__ == '__main__':
    unittest.main()