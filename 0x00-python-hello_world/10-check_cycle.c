#include "lists.h"
/**
 * check_cycle - checks for cycles in a listint_t list
 * @list: pointer to list to be checked
 * Return: 1 (Cycles present) , 0 (No cycles)
 */
int check_cycle(listint_t *list)
{
	listint_t *curr = list;
	listint_t *temp;

	if (!list)
	{
		return (0);
	}
	while (curr)
	{
		temp = curr->next;
		while (temp)
		{
			if (temp->next == curr)
			{
				return (1);
			}
			temp = temp->next;
		}
		curr = curr->next;
	}
	return (0);
}
