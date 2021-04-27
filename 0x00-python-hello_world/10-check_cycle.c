#include "lists.h"

/**
 *check_cycle - Function checks if a singly linked list has a cycle in it
 *@list: head of the linked list
 *Return: 0, if there is no cycle and 1, if there is a cycle
 *
 * Description: Use of Floyd's algorithm
 */
int check_cycle(listint_t *list)
{
    /* Declare two pointers and initialize them at the beginning of the list */
    listint_t *ptr_one = NULL, *ptr_two = NULL;

    ptr_one = list;
    ptr_two = list;

    while(ptr_one && ptr_two && ptr_two->next)
    {
        /* ptr_one advances one node at the time */
        ptr_one = ptr_one->next;
        /* ptr_two advances two nodes at the time */
        ptr_two = ptr_two->next->next;
        /* if both pointers point to the same node, it is because there is a cycle */
        if (ptr_one == ptr_two)
            return (1);
    }
    return (0);