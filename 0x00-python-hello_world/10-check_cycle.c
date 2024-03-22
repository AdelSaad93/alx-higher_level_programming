#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the list
 *
 * Return: 1 if there is a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
    listint_t *tortoise, *hare;

    if (list == NULL)
        return (0);

    tortoise = list;
    hare = list->next;

    while (tortoise != NULL && hare != NULL && hare->next != NULL)
    {
        if (tortoise == hare)
            return (1);
        tortoise = tortoise->next;
        hare = hare->next->next;
    }

    return (0);
}

