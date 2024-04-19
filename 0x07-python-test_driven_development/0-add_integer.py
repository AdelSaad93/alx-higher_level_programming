#!/usr/bin/python3
"""
This module contains a function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number. Defaults to 98.

    Returns:
        int: The addition of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
        OverflowError: If either a or b is infinity.
        ValueError: If either a or b is NaN.

    Examples:
        >>> add_integer(2, 3)
        5
        >>> add_integer(2, -3)
        -1
        >>> add_integer(2.0, 3.0)
        5
        >>> add_integer(2.9, 0.2)
        2
        >>> add_integer(-2.9, -0.2)
        -2
        >>> add_integer(2.3, -3)
        -1
        >>> add_integer(2)
        100
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    if isinstance(a, float) and a in (float('inf'), float('-inf')):
        raise OverflowError("cannot convert float infinity to integer")
    if isinstance(b, float) and b in (float('inf'), float('-inf')):
        raise OverflowError("cannot convert float infinity to integer")
    if isinstance(a, float) and str(a) == 'nan':
        raise ValueError("cannot convert float NaN to integer")
    if isinstance(b, float) and str(b) == 'nan':
        raise ValueError("cannot convert float NaN to integer")
    return int(a) + int(b)
