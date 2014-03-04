from random import randint


def toss_coin():
    """
    Randomly returns either a zero or a one.
    """
    return randint(0, 1)


def roll_die():
    """
    Return a random value between 1 and 6 inclusive. Use three coin flips, 0
    or 1, to twiddle bits to get values between 0 and 7 inclusive (2^3).
    Repeat until a value between 1 and 6 is found.
    """
    result = 0
    # Flip until we get a roll in the right range
    while result < 1 or result > 6:
        result = 0
        tosses = [toss_coin() for x in range(3)]
        for t, toss in enumerate(tosses):
            if toss:
                result |= 2 ** t
    return result