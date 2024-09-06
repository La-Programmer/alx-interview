#!/usr/bin/python3
"""PRIME GAME ALGORITHM
"""


def get_primes(n):
    """Gets the length of primes
    """
    marked_array = []
    primes = []
    for i in range(2, n + 1):
        for j in range(i * i, n + 1):
            if j in marked_array:
                continue
            elif j % i == 0:
                marked_array.append(j)
    for prime in range(2, n + 1):
        if prime not in marked_array:
            primes.append(prime)
    return len(primes)


def isWinner(x, nums):
    """Choose a winner between Maria and Ben
    """
    ben = 0
    maria = 0
    for i in nums:
        length_of_primes = get_primes(i)
        if length_of_primes % 2 == 0:
            ben += 1
        else:
            maria += 1
    if maria > ben:
        return "Maria"
    return "Ben"
