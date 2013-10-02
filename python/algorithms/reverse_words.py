"""
Given a sentence, write a function that returns the reverses the order of the
words.
"""
import re


def reverse_words(str):
    """
    Returns the reverse word order of the provided string.
    """
    # If necessary, remove non-alphanumeric characters
    if not str.isalnum():
        str = re.sub(r'\W+', ' ', str)

    # Split the words into a list
    words = str.split()

    # Return the reversed sentence
    return ' '.join(words[::-1])