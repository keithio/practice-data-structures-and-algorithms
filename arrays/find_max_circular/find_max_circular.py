from __future__ import division


def find_max_circular(values):
    """
    Returns the largest element in a list of values sorted circularly.
    """
    # Handle the singleton case
    if len(values) == 1:
        return values[0]

    # Set the search boundaries
    low = 0
    high = len(values) - 1

    # If the list of values it monotonically increasing, return the last value
    if values[low] < values[high]:
        return values[high]

    # Do a modified binary search to find the largest element
    while low < high:
        # Divide the search space into two halves
        mid = (low + high) // 2

        # Determine the half of the list in which the max must reside
        if values[mid] > values[high]:
            # If only one element remains on the right side, it is the max
            if high - mid == 1:
                return values[mid]

            # Otherwise, limit next search to the right side
            low = mid + 1

        else:
            #If only one element remains on the left side, it is the max
            if mid - low == 1:
                return values[low]

            # Otherwise, limit the next search to the left side
            high = mid

    # No max could be found
    return -1