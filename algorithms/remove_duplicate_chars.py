def remove_duplicate_chars(string):
    """
    Return a string that has the duplicate characters removed. Assumes ASCII,
    and is case-sensitive.

    Should run in O(n^2)
    """
    if not string or len(string) < 2:
        return string
    return ''.join(set(string))


if __name__ == '__main__':
    print remove_duplicate_chars('abcd')
    print remove_duplicate_chars('aaaa')
    print remove_duplicate_chars('')
    print remove_duplicate_chars('aabbb')
