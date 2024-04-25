#!/usr/bin/python3
"""Module containing Pascal's Triangle function"""


def pascal_triangle(n):
    """
        returns a list of lists of integers representing
        the Pascal’s triangle of n

        Args:
            n (int): number of rows

        Returns:
            an empty list if n <= 0, else 2D list representing pascal triangle
    """
    if n <= 0:
        return []

    if n == 1:
        return [[1]]

    prev_rows = pascal_triangle(n - 1)
    new_row = [1] * n

    for i in range(1, n - 1):
        new_row[i] = prev_rows[-1][i-1] + prev_rows[-1][i]

    prev_rows.append(new_row)

    return prev_rows
