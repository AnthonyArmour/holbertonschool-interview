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

    def __init__(self, nums, x):
        self.list = list(range(1, max(nums)+1))
        self.nums = sorted(nums)
        self.x = x
        #         Maria  Ben
        self.games = {1: 0, -1: 0}

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
        for val in range(x+x, max(self.list)+1, x):
            if val in self.list:
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

    def checkGames(self, turn):
        """Checks if games have ended, tallies
        scores, and removes games"""
        for n in self.nums.copy():
            if not self.containsPrime(self.nextHighest(n)):
                self.games[turn] += self.nums.count(n)
                while n in self.nums:
                    self.nums.pop(self.nums.index(n))
            else:
                break

    def containsPrime(self, lst=None):
        """
        checks for prime in list
        """
        if not lst:
            lst = self.list

        if len(lst) == 0:
            return False
        for num in lst:
            if self.isPrime(num):
                return True
        return False

    def nextHighest(self, n):
        """returns list up to n or
        up to value less than and closest to n"""

        if n in self.list:
            return self.list[:self.list.index(n)+1]

        size = len(self.list)
        low, high = 0, n - 1 if size >= n else size - 1
        idx = False

        while low <= high:
            mid = (low + high) // 2

            val = self.list[mid]
            if val < n:
                idx = mid
                low = mid + 1
            else:
                high = mid - 1

        return self.list[:idx+1]

    def playGames(self):
        """Play single prime game and returns winner"""

        turn = 1

        if 1 in self.nums:
            self.games[-1] += self.nums.count(1)
            while 1 in self.nums:
                self.nums.pop(self.nums.index(1))

        if self.containsPrime():
            done = False
        else:
            self.games[-1] += len(self.nums)
            done = True

        while not done:
            done = self.makeMove()
            if not done:
                self.checkGames(turn)
            turn *= -1


def isWinner(x, nums):
    """
    where x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    You cannot import any packages in this task

    """

    if x <= 0:
        return None

    game = PrimeGame(nums, x)
    game.playGames()

    if game.games[1] > game.games[-1]:
        return "Maria"
    elif game.games[1] < game.games[-1]:
        return "Ben"
    else:
        return None


if __name__ == "__main__":
    # print("Winner: {}".format(isWinner(5, [3])))
    # print("Winner: {}".format(isWinner(3, [2, 5, 10])))
    # print("Winner: {}".format(isWinner(3, [4, 5, 1])))
    # print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
    # print("Winner: {}".format(isWinner(4, [11, 30, 1, 7])))
    # print("Winner: {}".format(isWinner(6, [1, 1, 0, 0, 1, 8])))
    # print("Winner: {}".format(isWinner(10, [5, 5, 5, 5, 5, 2, 2, 2, 2, 2])))

    nums = [0] * 100
    for i in range(100):
        nums[i] = i * i

    print("Winner: {}".format(isWinner(100, nums)))

    nums = [0] * 10000
    for i in range(10000):
        nums[i] = i

    print("Winner: {}".format(isWinner(10000, nums)))
