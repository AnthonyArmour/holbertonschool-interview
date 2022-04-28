#!/usr/bin/python3
"""
Module contains function for, given a list of
coins and a total ammount, finding the least amount of
coins to make the total ammount.
"""


def recurse(coins, total):
    """
    Recursive search for change.
    """

    if len(coins) == 0:
        return -1

    ctotal, cnt = total, 0

    for coin in coins:
        if coin <= ctotal:
            amt = int(ctotal / coin)
            ctotal -= coin * amt
            cnt += amt

        if ctotal == 0:
            return cnt

    coins.pop(0)
    return recurse(coins, total)


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the
    fewest number of coins needed to meet a given amount total.

    Args:
        coins: list of coins.
        total: value to meet.

    Return: Smallest possible number of coins, else -1
    """

    if total <= 0:
        return 0

    coins = sorted(coins, reverse=True)

    return recurse(coins, total)


if __name__ == "__main__":

    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))
    print(makeChange([1, 2, 10], 11))
    print(makeChange([1, 4, 5, 10], 1278652))
