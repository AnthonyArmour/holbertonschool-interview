#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * reverse - reverses an array in place 
 * 
 * @arr: int array
 * @size: int size of array
 * 
 * Return: void
 */
void reverse(int *arr, int size)
{
    int i;

    for (i = 0; i < size/2; i++)
    {
        int temp = arr[i];
        arr[i] = arr[size - 1 - i];
        arr[size - 1 - i] = temp;
    }
}

/**
 * slide_line - 2048 game on a single dimension
 * 
 * @line: array representing board
 * @size: size_t size of line
 * @direction: int representing direction to slide
 * 
 * Return: 1 on success, else 0
 */
int slide_line(int *line, size_t size, int direction)
{
    int tmp[(int)size];
    int i, tmp_idx = 0, num1 = 0;

    if (direction == 44)
        reverse(line, (int)size);
    else if (direction != 33)
        return (0);

    for (i = 0; i < (int)size; i++)
        tmp[i] = 0;

    for (i = 0; i < (int)size; i++)
    {
        if (line[i] == 0)
            continue;

        if (num1 == 0)
            num1 = line[i];
        else if (num1 == line[i])
        {
            tmp[tmp_idx] = num1 + line[i];
            tmp_idx++;
            num1 = 0;

        }
        else
        {
            tmp[tmp_idx] = num1;
            tmp_idx++;
            num1 = line[i];
        }
        if (i == (int)size - 1)
            tmp[tmp_idx] = num1;
    }

    if (direction == 44)
        reverse(tmp, (int)size);

    memcpy(line, tmp, (int)size*sizeof(int));

    return (1);
}
