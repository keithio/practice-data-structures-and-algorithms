from random import random


def shuffle(values):
    """
    Returns the values in a different order.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    num_values = len(values)
    for v in range(num_values):
        # Get a random, different index
        s = v + int(random() * (num_values - v))
        # Swap values
        values[s], values[v] = values[v], values[s]
    return values
