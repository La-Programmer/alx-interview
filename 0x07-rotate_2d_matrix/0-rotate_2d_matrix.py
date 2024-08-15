#!/usr/bin/python3
"""Module 2D in-place matrix rotation
"""


def transpose_matrix(matrix):
    """Transpose a matrix"""
    length = len(matrix)
    for i in range(0, length):
        for j in range(i, length):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp


def rotate_2d_matrix(matrix):
    """Rotate a matrix by 90 deg"""
    if matrix:
        transpose_matrix(matrix)
        for row in matrix:
            row.reverse()
