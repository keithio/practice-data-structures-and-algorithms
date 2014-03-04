def add(a, b):
    """
    Implements add without using the `+` operator.
    """
    return a - ~b - 1


def sub(a, b):
    """
    Implements subtract without using the `-`operator.
    """
    return a + ~b + 1