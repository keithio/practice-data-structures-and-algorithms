"""
Task: Find the missing term in an Arithmetic Progression.

An Arithmetic Progression is defined as one in which there is a constant
difference between the consecutive terms of a given series of numbers. You are
provided with consecutive elements of an Arithmetic Progression. There is
however one hitch: Exactly one term from the original series is missing from
the set of numbers which have been given to you. The rest of the given series
is the same as the original AP. Find the missing term.
"""


import sys


def find_missing_int(n, seq, round=1):
    """
    Returns the missing integer from a consequtive sequence of integers.
    """
    # Creates a list of integers from the sequence provided
    seq = map(int, seq.split())

    # Define an initial step size
    step = seq[round] - seq[round - 1]

    # Create a sequence using the step size between the first and second integers
    gen_seq = xrange(min(seq), max(seq) + 1, step)

    # Find the difference between the sequences
    diff = list(set(gen_seq) - set(seq))

    if len(diff) > 1:
        # Step size is incorrect
        find_missing_int(n, seq, 2)
    else:
        # Otherwise, return the missing integer
        return diff[0]


if __name__ == '__main__':
    n, seq = sys.stdin.readlines()
    print find_missing_int(n, seq)