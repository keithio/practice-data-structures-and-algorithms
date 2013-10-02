"""
Given two integers, write a function to swap them without using any temporary storage.
"""


def int_swap(a, b):
    """
    Swaps two integers without using temporary storage.
    """
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return (a, b)