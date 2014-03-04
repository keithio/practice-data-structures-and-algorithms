#!/usr/bin/env python
import unittest
from find_anagrams import FindAnagrams


class FindAnagramsTest(unittest.TestCase):

    def test1(self):
        dictionary = ['adam', 'madam', 'mary', 'yarm']
        stimulus = 'army'
        response = ['mary', 'yarm']
        fa = FindAnagrams(dictionary, stimulus)
        self.assertEqual(response, fa())


if __name__ == '__main__':
    unittest.main()