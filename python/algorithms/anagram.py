def is_anagram(s1, s2):
    """
    Checks if two strings are anagrams.

    Should run in O(n)
    """

    return sorted(s1) == sorted(s2)


if __name__ == '__main__':
    print is_anagram('obo', 'boo')
    print is_anagram('obo', 'bob')
    print is_anagram('abc', 'xyz')