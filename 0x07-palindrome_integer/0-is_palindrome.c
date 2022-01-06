#include <stdio.h>

/**
 * is_palindrome - Checks if integer is palindrome
 * @n: unsigned long int to check
 * Return: 1 if palindrome, else 0
 */
int is_palindrome(unsigned long n)
{
    int reversed = 0, remainder, original;

    original = n;

    /* reversed integer is stored in reversed variable */
    while (n != 0) {
        remainder = n % 10;
        reversed = reversed * 10 + remainder;
        n /= 10;
    }

    /* palindrome if orignal and reversed are equal */
    if (original == reversed)
        return(1);
    else
        return(0);

}
