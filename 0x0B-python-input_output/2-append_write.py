#!/usr/bin/python3
"""Defines a function to append a string to the end of a text file."""


def append_write(filename="", text=""):
    """Append a string to the end of a text file and.

    Args:
        filename (str): The name of the text file.
        text (str): The string to append.

    Returns:
        int: The number of characters added.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
