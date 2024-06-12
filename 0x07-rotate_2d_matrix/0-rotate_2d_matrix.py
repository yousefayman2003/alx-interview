#!/usr/bin/python3
"""Module containing Rotate 2D Matrix Solution."""


def rotate_2d_matrix(matrix):
    """
        Rotates a two dimension matrix 90 degrees clockwise.

        Args:
            matrix (list[[list]]): A 2D matrix
    """
    n = len(matrix)
    for i in range(n // 2):
        y = (n - i - 1)
        for j in range(i, y):
            x = (n - 1 - j)
            curr = matrix[i][j]
            matrix[i][j] = matrix[x][i]
            matrix[x][i] = matrix[y][x]
            matrix[y][x] = matrix[j][y]
            matrix[j][y] = curr
