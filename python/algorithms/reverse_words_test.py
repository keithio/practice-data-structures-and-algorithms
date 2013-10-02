from __future__ import unicode_literals
import unittest
from reverse_words import reverse_words


class TestReverseString(unittest.TestCase):

    def test_alnum(self):
        self.assertEqual('words some testing', reverse_words('testing some '
                                                             'words'))

    def test_not_alnum(self):
        self.assertEqual('words some testing', reverse_words('testing some '
                                                             'words.'))


if __name__ == '__main__':
    unittest.main()