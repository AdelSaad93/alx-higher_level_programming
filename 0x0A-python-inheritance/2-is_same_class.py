#!/usr/bin/python3
"""Defines a function to check if an object is an instance."""


def is_same_class(obj, a_class):
    """Check if an object is an instance of a specified class.

    Args:
        obj (object): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if the object is an instance of the specified class;
            otherwise False.
    """
    return type(obj) is a_class
