#!/usr/bin/python3
"""Defines a function to check if an object is an instance of or inherited."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of, or inherited from, a specified class.

    Args:
        obj (object): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if the object is an instance of or inherited ;
            otherwise False.
    """
    return isinstance(obj, a_class)
