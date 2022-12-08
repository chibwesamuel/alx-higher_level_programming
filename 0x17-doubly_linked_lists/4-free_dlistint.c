#include "lists.h"

/**
 * free_dlistint - function that frees a dlistint_t list
 * @head: pointer to head of node
 *
 * Return: Always 0
 */

void free_dlistint(dlistint_t *head)
{
	dlistint_t *tmp;

	while (head)
	{
		tmp = head->next;
		free(head);
		head = tmp;
	}
}
