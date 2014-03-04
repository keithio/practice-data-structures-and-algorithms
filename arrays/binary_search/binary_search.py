from __future__ import division


def binary_search(array, value, low=0, high=None):
    """
    Returns the index of the search parameter in the list.

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    high = high if high is not None else len(array)

    while low < high:
        # Divide the search space into two halves
        mid = (low + high) // 2
        mid_value = array[mid]

        if mid_value < value:
            # Use last half for next search
            low = mid + 1
        elif mid_value > value:
            # Use first half for next search
            high = mid
        else:
            # Index found
            return mid

    # Index could not be found
    return -1