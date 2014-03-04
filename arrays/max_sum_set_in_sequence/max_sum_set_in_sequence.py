def max_sum_set_in_sequence(values):
    """
    Returns the set in the sequence that returns the maximum sum.

    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    max_from = [None for v in values]
    max_end_from = [v + 1 for v in range(len(values))]

    for i in range(len(values) - 1):
        max_from[i] = values[i]

        # Determine if any increase occurs from the right
        j = len(values)
        while i < j:
            sum_ij = sum(values[i:j])
            # If there is an increase, update values
            if sum_ij > max_from[i]:
                max_from[i] = sum_ij
                max_end_from[i] = j
            j -= 1

    # Get the maximum sum
    seq_sum = max(max_from)

    # Get the range for the maximum sum from the sequence
    seq_start = max_from.index(seq_sum)
    seq_end = max_end_from[seq_start]

    # Return the maximum sum and its generating sequence
    return seq_sum, values[seq_start:seq_end]
