from __future__ import division


def find_duplicate(values):
    """
    Returns any duplicate items from a list.
    """
    seen = set()
    seen_again = set(v for v in values if v in seen or seen.add(v))
    return list(seen_again)