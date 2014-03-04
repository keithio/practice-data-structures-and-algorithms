def roman_numeral_to_integer(numerals):
    """
    Converts roman numeral to integer.

    Should run in O(n)
    """

    mapping = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    # Total value container
    total = 0

    # Current value container
    curr = 0

    # Previous value container
    prev = 0

    # Iterate over each letter in the roman numeral
    for numeral in list(numerals):
        curr = mapping[numeral]

        if curr <= prev:
            total += curr
        else:
            # If the current value is greater than the previous, e.g. IX,
            # subtract twice (to avoid double counting)
            total += curr - prev * 2
        prev = curr

    return total
