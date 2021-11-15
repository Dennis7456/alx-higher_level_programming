#include "lists.h"

/**
 * check_cycle - function checks if a singly linked list has a cycle in it.
 * @list: pointer to the beginning of the node
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *temp, *check;

	if (list == NULL || list->next == NULL)
		return (0);
	temp = list;
	check = temp->next;

	while (temp != NULL && check->next != NULL
		&& check->next->next != NULL)
	{
		if (temp == check)
			return (1);
		temp = temp->next;
		check = check->next->next;
	}
	return (0);
}