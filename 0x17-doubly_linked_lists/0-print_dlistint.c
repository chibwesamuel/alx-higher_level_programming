#include "lists.h"

/**
 * print_dlistint - function that prints all the elements of a dlistint_t list
 * @h: node pointer
 *
 * Return: 0 on success
 */

size_t print_dlistint(const dlistint_t *h)
{
	sixe_t node = 0;

	while (h)
	{
		node++;
		printf("%d\n", h->n);
		h = h->next;
	}
	return (node);
}
