import unittest
from fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):

    def setUp(self):
        self.numbers = range(1, 16)

    def test_output(self):
        """
        Make sure the correct output is generated.
        """
        correct = [1,
                   2,
                   'Fizz',
                   4,
                   'Buzz',
                   'Fizz',
                   7,
                   8,
                   'Fizz',
                   'Buzz',
                   11,
                   'Fizz',
                   13,
                   14,
                   'FizzBuzz'
                  ]
        self.assertEqual(correct, fizzbuzz(self.numbers))


if __name__ == '__main__':
    unittest.main()