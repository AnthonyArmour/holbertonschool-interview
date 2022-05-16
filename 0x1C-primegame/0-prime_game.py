#!/usr/bin/python3
"""
Module contains prime game implementation.

Maria and Ben are playing a game. Given a set of consecutive integers
starting from 1 up to and including n, they take turns choosing a prime
number from the set and removing that number and its multiples from the set.
The player that cannot make a move loses the game.

They play x rounds of the game, where n may be different for each round.
Assuming Maria always goes first and both players play optimally, determine
who the winner of each game is.
"""


class PrimeGame():

    def __init__(self, n):
        self.list = list(range(1, n+1))

    def isPrime(self, x):
        """Returns True if prime number, else False"""
        if x > 1:
            for i in range(2, int(x/2)+1):
                if x % i == 0:
                    return False
            return True
        else:
            return False

    def removeMultiples(self, x):
        """Removes multiples of x from num list"""
        self.list.pop(self.list.index(x))
        for val in range(x+x, max(self.list), x):
            self.list.pop(self.list.index(val))

    def makeMove(self):
        """
        Makes optimal move for player
        if game is over returns True, else False
        """
        if len(self.list) == 0:
            return True
        for num in self.list:
            if self.isPrime(num):
                self.removeMultiples(num)
                return False
        return True

    def containsPrime(self):
        """
        checks for prime in list
        """
        if len(self.list) == 0:
            return False
        for num in self.list:
            if self.isPrime(num):
                return True
        return False

    def playGame(self):
        """Play single prime game and returns winner"""

        players = {1: "Maria", -1: "Ben"}
        turn = 1

        if self.containsPrime():
            done = False
        else:
            return "Ben"

        while not done:
            done = self.makeMove()
            turn *= -1

        return players[-1*turn]


def isWinner(x, nums):
    """
    where x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    You cannot import any packages in this task

    """

    players = {"Maria": 0, "Ben": 0}

    for i in range(x):
        game = PrimeGame(nums[i])
        players[game.playGame()] += 1

    if players["Maria"] > players["Ben"]:
        return "Maria"
    elif players["Maria"] < players["Ben"]:
        return "Ben"
    else:
        return None


if __name__ == "__main__":
    print("Winner: {}".format(isWinner(3, [4, 5, 1])))
