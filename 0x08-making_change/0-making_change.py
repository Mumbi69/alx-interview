#!/usr/bin/python3
"""Making Change"""


def makeChange(coins, total):
    """
    initializes an array dp to store the fewest number of coins
    needed to make each total from 0 to the given total.
    """
    if total <= 0:
        return 0

    coins = sorted(coins)[::-1]
    dp = 0
    for coin in coins:
        if total <= 0:
            break
        while total >= coin:
            total -= coin
            dp += 1
    if total:
        return -1
    return dp
