def selectionsort(values):
    """
    Performs a selection sort on a list of values.

    Time Complexity: O(n^2)
    """
    min_idx = None

    for i in range(len(values)):
        min_idx = i
        for j in range(i + 1, len(values)):
            # If j is less than the current min, update the index that has
            # the minimum
            if values[j] < values[min_idx]:
                min_idx = j

        # Swap values so the new minimum replaces the current iterated value
        temp = values[min_idx]
        values[min_idx] = values[i]
        values[i] = temp

    return values


print selectionsort([4, 1, 3, 2])