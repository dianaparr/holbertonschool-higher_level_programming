#include "lists.h"

/**
 *is_palindrome - checks if a list is a palindrome
 *@head: pointer to a pointer to the head of a list
 *Return: 0 if it's not a palindrome, 1 it's palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr_temp = *head;
	unsigned int counter = 0, a = 0, b = 0;
	int array_list[BUFSIZ];

	if (*head == NULL)
		return (1);
	while (ptr_temp != NULL)
	{
		/* fill array */
		array_list[counter] = ptr_temp->n;
		ptr_temp = ptr_temp->next;
		counter++;
	}
	b = (counter - 1);
	while (a < b)
	{
		if (array_list[a] != array_list[b])
		{
			return (0);
		}
		else
		{
			a++;
			b--;
			continue;
		}
	}
	return (1);
}
