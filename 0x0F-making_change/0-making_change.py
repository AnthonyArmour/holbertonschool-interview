#!/usr/bin/python3
"""
Module contains function for, given a list of
coins and a total ammount, finding the least amount of
coins to make the total ammount.
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the
    fewest number of coins needed to meet a given amount total.

    Args:
        coins: list of coins.
        total: value to meet.

    Return: Smallest possible number of coins, else -1
    """

    cnt = 0

    for coin in sorted(coins, reverse=True):
        if total == 0:
            return cnt
        if coin <= total:
            amt = int(total / coin)
            total -= coin * amt
            cnt += amt

    return -1


if __name__ == "__main__":

    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))
