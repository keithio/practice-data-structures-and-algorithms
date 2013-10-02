def roman_numerals_to_int(numerals):
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

    total = 0
    curr = 0
    prev = 0
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


if __name__ == '__main__':
    print roman_numerals_to_int('VI') == 6
    print roman_numerals_to_int('IX') == 9
    print roman_numerals_to_int('XI') == 11
    print roman_numerals_to_int('LIX') == 59
    print roman_numerals_to_int('LCXI') == 61
    print roman_numerals_to_int('LDXI') == 461
    print roman_numerals_to_int('MCMLIV') == 1954
    print roman_numerals_to_int('MCMXC') == 1990
    print roman_numerals_to_int('MMVIII') == 2008
    print roman_numerals_to_int('CMIV') == 904
    print roman_numerals_to_int('MCMIV') == 1904
    print roman_numerals_to_int('MMMDCLXIV') == 3664
