#include "menger.h"

/**
 * menger - 2D menger sponge
 * @level: int, level of the menger sponge
 */

void menger(int level)
{
	int size, row, col;
	char pound;

	size = pow(3, level);

	for (row = 0; row < size; row++)
	{
		for (col = 0; col < size; col++)
		{
			pound = get(row, col);
			printf("%c", pound);
		}
		printf("\n");
	}
}

/**
 * get - get pound or empty char
 * @row: row of the sponge
 * @col: column of the sponge
 * Return: # or empty char
 */

char get(int row, int col)
{
	while (row || col)
	{
		if (row % 3 == 1 && col % 3 == 1)
			return (' ');
		row /= 3;
		col /= 3;
	}
	return ('#');
}