def powerset(seq):
    """
    Returns the subsets of a given sequence.
    """
    if len(seq) < 2:
        # At last element of the set, return it and the empty set
        yield []
        yield seq
        return

    for s in powerset(seq[1:]):
        # Find the powerset using the remaining elements in the set
        yield [seq[0]] + s
        yield s


def get_powerset(st):
    """
    Returns the sorted powerset for a given set.
    """
    return sorted([item for item in powerset(st)])
