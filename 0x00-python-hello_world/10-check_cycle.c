#include "lists.h"

/**
 *check_cycle - 
 *@list: 
 *Return: 
 */
int check_cycle(listint_t *list)
{
    /* Declaro dos punteros y los inicializo al inicio de la lista */
    listint_t *ptr_slow = NULL, *ptr_fast = NULL;

    ptr_slow = list;
    ptr_fast = list;

    while(ptr_slow && ptr_fast && ptr_fast->next)
    {
        /* ptr_slow avanza un nodo a la vez */
        ptr_slow = ptr_slow->next;
        /* ptr_fast avanza dos nodos a la vez */
        ptr_fast = ptr_fast->next->next;
        if (ptr_slow == ptr_fast)
            return (1);
    }
    return (0);
}