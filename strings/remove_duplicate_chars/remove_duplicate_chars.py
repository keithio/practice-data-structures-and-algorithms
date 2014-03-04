def remove_duplicate_chars(string):
    """
    Return a string that has the duplicate characters removed. Assumes ASCII,
    and is case-sensitive.

    Time: O(n)
    Space: O(n)
    """
    if not string or len(string) < 2:
        return string
    return ''.join(set(string))
