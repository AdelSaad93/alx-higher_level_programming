#!/usr/bin/python3
"""Defines a function that reads a text file and prints its contents."""


def read_file(filename=""):
    """Read a text file (UTF8) and print its contents to stdout.

    Args:
        filename (str): The name of the text file to read.
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")
