/*
 * =====================================================================================
 *
 *       Filename:  main.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  08/21/2020 01:22:40 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Ji-In Moon (jmoon), jmoon@jiinmoon.com
 *        Company:  
 *
 * =====================================================================================
 */

#include <iostream>

struct ListNode
{
    int val;
    struct ListNode *next;
} *first = NULL;

void createLinkedList(const int a[], const int size)
{
    int i;
    struct ListNode *t, *last;
    first = (struct ListNode*) malloc(sizeof(struct ListNode));
    first->val = a[0];
    first->next = NULL;
    last = first;
    for (i = 1; i < size; i++)
    {
        t = (struct ListNode*) malloc(sizeof(struct ListNode));
        t->val = [A[i];
        t->next = NULL;
        last->next = t;
    }
}


int main()
{
    int a[] = {1,2,3,4,5};

    return 0;
}
