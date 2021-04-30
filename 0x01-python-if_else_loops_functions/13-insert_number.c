#include "lists.h"

/**
 *insert_node - adds a new node at the linked list
 *@head: pointer to a pointer to the head of a list
 *@number: integer to be added to the listint_t list
 *Return: the address of the new element
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_n, *ptr_temp = *head;

	new_n = malloc(sizeof(listint_t));
	if (new_n == NULL)
		return (NULL);
	new_n->n = number;
	if (*head == NULL)
	{
		*head = new_n;
		new_n->next = NULL;
		return (new_n);
	}
	if (new_n->n < 0)
	{
		new_n->next = *head;
		*head = new_n;
		return (new_n);
	}
	while (ptr_temp->next != NULL)
	{
		if (number >= ptr_temp->n && number < ptr_temp->next->n)
		{
			new_n->next = ptr_temp->next;
			ptr_temp->next = new_n;
			return (new_n);
		}
		ptr_temp = ptr_temp->next;
	}
	if (ptr_temp->next == NULL)
	{
		new_n->next = NULL;
		ptr_temp->next = new_n;
		return (new_n);
	}
	return (NULL);
}
