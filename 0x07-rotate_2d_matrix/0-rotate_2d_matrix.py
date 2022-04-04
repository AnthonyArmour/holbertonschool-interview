#!/usr/bin/python3
"""
Module contains function for transposing a 2d matrix.
"""


def rotate_2d_matrix(matrix):
    """transposes a 2d matrix"""
    s = -(len(matrix) - 1)
    mcopy = [row.copy() for row in matrix]
    for x, row in enumerate(mcopy, start=s):
        for i, element in enumerate(row):
            matrix[i][-x] = element


if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
