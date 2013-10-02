import unittest
from reverse_string import reverse_string


class TestReverseString(unittest.TestCase):

    def test_output(self):
        """
        Make sure the correct output is generated.
        """
        self.assertEqual('cba', reverse_string('abc'))


if __name__ == '__main__':
    unittest.main()