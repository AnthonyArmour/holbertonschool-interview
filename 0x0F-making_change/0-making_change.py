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

    if total <= 0:
        return 0

    counts = []

    def recurse(coins, total, cnt):
        """Recursive search for change."""

        if len(coins) == 0:
            return

        big_coin = coins.pop(0)
        amt = int(total / big_coin)
        total -= big_coin * amt
        cnt += amt

        if total == 0:
            counts.append(cnt)
            return

        for i, coin in enumerate(coins):
            if coin <= total:
                recurse(coins[i:], total, cnt)

        return


    coins = sorted(coins, reverse=True)

    for i, coin in enumerate(coins):
        if coin <= total:
            recurse(coins[i:], total, 0)

    # print(counts)

    if len(counts) == 0:
        return -1
    else:
        return min(counts)


if __name__ == "__main__":

    # print(makeChange([1, 2, 25], 37))
    # print(makeChange([1256, 54, 48, 16, 102], 1453))
    # print(makeChange([1, 2, 10], 11))
    print(makeChange([200, 6, 5, 4, 3], 413))
    print(makeChange([500, 300, 200, 6, 5, 4, 3], 1413))
    print(makeChange([507, 500, 300, 200, 6, 5, 4, 3], 1413))
