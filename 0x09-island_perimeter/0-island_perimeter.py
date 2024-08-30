#!/usr/bin/python3
"""ISLAND PERIMETER ALGORITHM"""


def island_perimeter(grid):
    """Function to calculate the perimeter of an island"""
    perimeter: int = 0
    for index, value in enumerate(grid):
        for index2, value2 in enumerate(value):
            if value2 == 1:
                if index == 0:
                    perimeter += 1
                else:
                    if grid[index - 1][index2] == 0:
                        perimeter += 1
                if index == len(grid) - 1:
                    perimeter += 1
                else:
                    if grid[index + 1][index2] == 0:
                        perimeter += 1
                if index2 == 0:
                    perimeter += 1
                else:
                    if grid[index][index2 - 1] == 0:
                        perimeter += 1
                if index2 == len(value) - 1:
                    perimeter += 1
                else:
                    if grid[index][index2 + 1] == 0:
                        perimeter += 1
    return perimeter
