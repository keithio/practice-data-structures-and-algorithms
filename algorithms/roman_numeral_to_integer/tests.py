
#!/usr/bin/env python
import unittest
from roman_numeral_to_integer import roman_numeral_to_integer


class RomanNumeralToIntegerTest(unittest.TestCase):

    def testVI(self):
        self.assertEqual(6, roman_numeral_to_integer('VI'))

    def testIX(self):
        self.assertEqual(9, roman_numeral_to_integer('IX'))

    def testXI(self):
        self.assertEqual(11, roman_numeral_to_integer('XI'))

    def testLIX(self):
        self.assertEqual(59, roman_numeral_to_integer('LIX'))

    def testLCXI(self):
        self.assertEqual(61, roman_numeral_to_integer('LCXI'))

    def testLDXI(self):
        self.assertEqual(461, roman_numeral_to_integer('LDXI'))

    def testMCMLIV(self):
        self.assertEqual(1954, roman_numeral_to_integer('MCMLIV'))

    def testMCMXC(self):
        self.assertEqual(1990, roman_numeral_to_integer('MCMXC'))

    def testMMVIII(self):
        self.assertEqual(2008, roman_numeral_to_integer('MMVIII'))

    def testCMIV(self):
        self.assertEqual(904, roman_numeral_to_integer('CMIV'))

    def testMCMIV(self):
        self.assertEqual(1904, roman_numeral_to_integer('MCMIV'))

    def testMMMDCLXIV(self):
        self.assertEqual(3664, roman_numeral_to_integer('MMMDCLXIV'))


if __name__ == '__main__':
    unittest.main()