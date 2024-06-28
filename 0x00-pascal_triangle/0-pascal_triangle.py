#!/usr/bin/python3
"""Pascal's Triangle"""

def pascal_triangle(n): #Time complexity: O(n ^ 2) | Space complexity: O(n ^ 2)
  """Creates a Pascal's Triangle of height n"""
  if n <= 0:
    return [] #1
  elif n == 1:
    return [[1]] #1
  else:
    result = [[1]] #1
    for i in range(n - 1): #(O(n * n))
      row = create_rows(result[i]) #n
      result.append(row) #1
  return result


def create_rows(array): #Time complexity: O(n) | Space complexity: O(n)
  """Creates new rows of Pascal's Triangle"""
  result = []
  for i in range(len(array)): #n
    if i == 0:
      result.append(array[i])
    else:
      result.append(array[i] + array[i - 1])
  result.append(array[i])

  return result
