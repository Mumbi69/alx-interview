#!/usr/bin/python3
"""Making Change"""


def makeChange(coins, total):
    """
    initializes an array dp to store the fewest number of coins
    needed to make each total from 0 to the given total.
    """
    if total == 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for i in coins:
        for coin in range(i, total + 1):
            dp[coin] = min(dp[coin], dp[coin - i] + 1)
    if dp[total] != float("inf"):
        return dp[total]
    else:
        return -1
