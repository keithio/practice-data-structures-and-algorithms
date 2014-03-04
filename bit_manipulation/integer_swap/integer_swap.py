def integer_swap(a, b):
    """
    Swaps two integers without using temporary storage.
    """
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return (a, b)
