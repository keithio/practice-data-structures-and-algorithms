def is_anagram(s1, s2):
    """
    Checks if two strings are anagrams.

    Time Complexity: O(n)
    """

    return sorted(s1) == sorted(s2)
