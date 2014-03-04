from __future__ import division


def fibonacci(n):
    """
    Returns the nth Fibonacci numbers.
    """
    if n < 1:
        raise ValueError('Please specify the number of Fibonacci numbers to '
                         'generate.')
    return _fibonacci(n)[0]


def _fibonacci(n):
    """
    Computes the nth number in the Fibonacci sequence.
    """
    if not n:
        return 0, 1

    a, b = _fibonacci(n // 2)

    c = a * ((2 * b) - a)
    d = (b * b) + (a * a)

    if n % 2:
        return d, (c + d)
    else:
        return c, d


print fibonacci(5)