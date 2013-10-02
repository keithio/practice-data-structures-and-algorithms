"""
Given two strings, return the longest substring that they have in common.
"""


def longest_common_substring(s1, s2):
    """
    Return the longest common substring of two strings.
    """

    # Make sure each string has characters
    if not len(s1) or not len(s2):
        return ''

    # Store possible substrings
    record = [[0] * (len(s2) + 1) for i in xrange(len(s1) + 1)]

    longest = 0
    x_longest = 0

    for x in xrange(1, len(s1) + 1):
        for y in xrange(1, len(s2) + 1):
            if s1[x - 1] == s2[y - 1]:
                record[x][y] = record[x - 1][y - 1] + 1
                if record[x][y] > longest:
                    longest = record[x][y]
                    x_longest = x

    return s1[x_longest - longest: x_longest]
