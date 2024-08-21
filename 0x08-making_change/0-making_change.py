#!/usr/bin/python3

from typing import List


def bottom_up_solution(coins: List[int], amount: int) -> int:
    dp_array = [amount + 2] * (amount + 1)
    dp_array[0] = 0
    for coin in coins:
        for index in range(len(dp_array)):
            value = dp_array[index]
            if index >= coin:
                dp_array[index] = min(value, dp_array[index - coin] + 1)
    if dp_array[amount] == amount + 2:
        return -1
    return dp_array[amount]
