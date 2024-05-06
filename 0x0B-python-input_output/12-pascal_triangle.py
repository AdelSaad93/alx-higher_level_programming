#!/usr/bin/python3


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]  # first element of each row is always 1
        prev_row = triangle[i - 1]

        for j in range(1, i):
            # Each element (except the first and last) is the sum of the
            # corresponding elements of the previous row
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)  # last element of each row is always 1
        triangle.append(row)

    return triangle

# Test the function
if __name__ == "__main__":
    def print_triangle(triangle):
        """
        Print the triangle
        """
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    print_triangle(pascal_triangle(5))
