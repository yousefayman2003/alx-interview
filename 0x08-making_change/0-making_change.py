#!/usr/bin/python3
"""Module that implements makeChange function"""


def makeChange(coins, total):
    """
        Returns: fewest number of coins needed to meet total
                    If total is 0 or less, return 0
                    If total cannot be met by any number of coins you have,
                    return -1
    """
    if not coins or coins is None:
        return -1

    if total <= 0:
        return 0

    change = 0
    coins = sorted(coins, reverse=True)
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change

    return -1
