def find_longest_zero_sequence(n):
    """
    Finds the longest sequence of zeros in the binary representatation of n.
    """
    max_zeros = 0
    zero_count = 0

    while n:
        # From each position, count how many zeros follow

        # Check if 2^0 is not set
        if n & 1 == 0:
            zero_count += 1
            if zero_count > max_zeros:
                max_zeros = zero_count
        else:
            zero_count = 0

        # Shift to the next bit
        # Essentially divides by 2
        n = n >> 1

    return max_zeros
