def quicksort(values):
    """
    Returns the sorted list of values.

    Time Complexity: O(n^2) to O(n log n)
    Space Complexity: O(1)
    """
    # Set the value for pivoting
    if not len(values):
        return values

    pivot = values[0]

    # Sort the lower range
    low_range = quicksort([value for value in values[1:] if value < pivot])
    # Sort the higher range
    high_range = quicksort([value for value in values[1:] if value >= pivot])

    # Return the combined, sorted list
    return low_range + [pivot] + high_range
