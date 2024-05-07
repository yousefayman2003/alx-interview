#!/usr/bin/python3
"""Module containing the Minimum Operations problem solution"""


def minOperations(n: int) -> int:
    """
        calculates the fewest number of operations needed
        to result in exactly n H characters

        Args:
            n (int): length of h characters needed

        Returns:
            int: min number of operations to get n chars, or 0 if impossible
    """
    if n < 2:
        return 0

    ops = 0
    min_ops = 2
    while n > 1:
        while n % min_ops == 0:
            ops += min_ops
            n /= min_ops
        min_ops += 1

    return ops
