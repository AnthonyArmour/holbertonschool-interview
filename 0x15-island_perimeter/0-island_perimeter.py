#!/usr/bin/python3
"""
Module contains function for solving the
island perimeter challenge.
"""


def island_perimeter(grid):
    """
        Returns the perimeter of the island described in grid

        Args:
            grid:list of list of integers:
                0 represents water
                1 represents land
                Each cell is square, with a side length of 1
                Cells are connected horizontally/vertically (not diagonally).
                grid is rectangular, with its width and height not
                exceeding 100.
    """

    m, n = len(grid), len(grid[0])
    land, neighbor = 0, 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                land += 1
                if i < m - 1 and grid[i+1][j] == 1:
                    neighbor += 1
                if j < n - 1 and grid[i][j+1] == 1:
                    neighbor += 1
    return land * 4 - 2 * neighbor


if __name__ == "__main__":
    # Answer -> 12

    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
