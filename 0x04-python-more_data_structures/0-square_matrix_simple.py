#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix.

    Args:
        matrix: A 2D array of integers.

    Returns:
        A new 2D array with each value squared.
    """
    return [list(map(lambda x: x * x, row)) for row in matrix]
