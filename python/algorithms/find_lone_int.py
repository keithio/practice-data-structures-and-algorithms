"""
Given an array of integers where each number appears exactly twice, except for
one integer that appears exactly once, find the lone integer.
"""

def find_lone_int(ints):
    """
    Returns the integer that appears exactly once in the list.
    """
    loner = 0
    for i in ints:
        loner = loner ^ i  # cancel out pairs
    return loner