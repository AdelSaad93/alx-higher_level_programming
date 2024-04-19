#!/usr/bin/python3
"""
This module contains a function that prints a person's name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the person's name.

    Args:
        first_name (str): The first name.
        last_name (str): The last name. Defaults to an empty string.

    Raises:
        TypeError: If first_name or last_name is not a string.

    Examples:
        >>> say_my_name("John", "Smith")
        My name is John Smith
        >>> say_my_name("Walter", "White")
        My name is Walter White
        >>> say_my_name("Bob")
        My name is Bob
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
