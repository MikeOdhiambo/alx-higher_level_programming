#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number in a linked list
 *
 * @head: Pointer to head node
 * @number: Number to be inserted
 * Return: Pointer to new node (Success), NULL (Failure)
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *num;
	listint_t *curr_node = *head;

	num = malloc(sizeof(listint_t));
	if (!num)
	{
		return (NULL);
	}
	num->n = number;
	num->next = NULL;

	if (curr_node == NULL)
	{
		curr_node = num;
		return (num);
	}
	while (curr_node->next)
	{
		if (curr_node->next == NULL)
		{
			curr_node->next = num;
			return (num);
		}
		if (curr_node->next->n > number)
		{
			num->next = curr_node->next;
			curr_node->next = num;
			return (num);
		}
		curr_node = curr_node->next;
	}
	free(num);
	return (NULL);
}
