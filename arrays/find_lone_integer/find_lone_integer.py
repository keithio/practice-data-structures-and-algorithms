def find_lone_integer(ints):
    """
    Returns the integer that appears exactly once in the list.
    """
    loner = 0
    for i in ints:
        loner = loner ^ i  # cancel out pairs
    return loner
