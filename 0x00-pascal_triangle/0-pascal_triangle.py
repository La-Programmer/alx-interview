#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """Creates a Pascal's Triangle of height n"""
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        result = [[1]]
        for i in range(n - 1):
            row = create_rows(result[i])
            result.append(row)
    return result


def create_rows(array):
    """Creates new rows of Pascal's Triangle"""
    result = []
    for i in range(len(array)):
        if i == 0:
            result.append(array[i])
        else:
            result.append(array[i] + array[i - 1])
    result.append(array[i])

    return result
