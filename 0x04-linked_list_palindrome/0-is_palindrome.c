#include "lists.h"

/**
 * helper - checks if a linked list is a palindrome
 * @left: Starts at head and ends at the middle
 * @right: Starts at 2nd node in list and ends at last node
 * Return: 1 if palindrome, 0 if not
 */
int helper(listint_t **left, listint_t *right)
{
	/* Empty list is a palindrome */
	if (!right)
		return (1);

	/* Recursion */
	if (!is_palindrome_helper(left, right->next))
		return (0);

	/* Check if left and right nodes are equal */
	if ((*left)->n != right->n)
		return (0);

	/* Move left to next node */
	*left = (*left)->next;
	return (1);
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	if (!head || !*head)
		return (1);

	return (helper(head, *head));
}
