#include <unistd.h>

#include "lists.h"

/**
 * list_len - Finds the length of a linked list
 * @head: Pointer to head node
 * Return: Length of linked list
 */
int list_len(listint_t *head)
{
	int len;

	for (len = 0; head; len++)
		head = head->next;
	return (len);
}

/**
 * is_palindrome - checks if a linked list is palindromic
 * @head: Pointer to pointer of head node
 * Return: 1 (is palindromic), 0 (otherwise)
 */

int is_palindrome(listint_t **head)
{
	int *cpy, i, len, mid;
	listint_t *curr = *head;

	if (!head)
		return (1);

	len = list_len(curr);
	cpy = malloc(len * sizeof(int));
	if (!cpy)
		return (1);
	curr = *head;

	for (i = 0; curr; i++)
	{
		cpy[i] = curr->n;
		curr = curr->next;
	}
	mid = i / 2;
	for (i = 0; i <= mid; i++)
	{
		if (cpy[i] != cpy[len - (i + 1)])
			return (0);
		continue;
	}
	return (1);
}

