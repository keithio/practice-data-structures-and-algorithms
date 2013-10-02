import unittest
from two_of_three import two_of_three


class TestFizzBuzz(unittest.TestCase):

    def setUp(self):
        # Create all permutations of True and False
        self.ttt = (True, True, True)
        self.ttf = (True, True, False)
        self.tft = (True, False, True)
        self.tff = (True, False, False)
        self.ftt = (False, True, True)
        self.ftf = (False, True, False)
        self.fft = (False, False, True)
        self.fff = (False, False, False)

    def test_ttt(self):
        self.assertEqual(True, two_of_three(*self.ttt))

    def test_ttf(self):
        self.assertEqual(True, two_of_three(*self.ttf))

    def test_tft(self):
        self.assertEqual(True, two_of_three(*self.tft))

    def test_tff(self):
        self.assertEqual(False, two_of_three(*self.tff))

    def test_ftt(self):
        self.assertEqual(True, two_of_three(*self.ftt))

    def test_ftf(self):
        self.assertEqual(False, two_of_three(*self.ftf))

    def test_fft(self):
        self.assertEqual(False, two_of_three(*self.fft))

    def test_fff(self):
        self.assertEqual(False, two_of_three(*self.fff))


if __name__ == '__main__':
    unittest.main()