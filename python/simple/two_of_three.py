"""
Write a function that takes three booleans and returns true if at least two
are true.
"""

def two_of_three(a, b, c):
    return b or c if a else b and c
