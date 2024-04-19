#!/usr/bin/python3
"""
This module contains a function that prints text with indentation.
"""


def text_indentation(text):
    """
    Prints text with indentation.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    Examples:
        >>> text_indentation("Hello. How are you?")
        Hello$
        $
        How are you?$
        $
        >>> text_indentation("This is a test: one, two, three.")
        This is a test:$
        $
        one, two, three.$
        $
        >>> text_indentation("What's up?")
        What's up?$
        $
        >>> text_indentation(123)
        Traceback (most recent call last):
        TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_marks = (".", "?", ":")
    for char in text:
        print(char, end="")
        if char in punctuation_marks:
            print("\n")
