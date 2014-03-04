def check_power_of_two(x):
    """
    Check if x is a power of two.
    """
    return (x & (x - 1)) == 0
