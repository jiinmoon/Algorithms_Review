/*
 * =====================================================================================
 *
 *       Filename:  main.cpp
 *
 *    Description:  Array ADT in C style.
 *
 *        Version:  1.0
 *        Created:  08/19/2020 02:59:31 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Ji-In Moon (jmoon), jmoon@jiinmoon.com
 *        Company:  
 *
 * =====================================================================================
 */

#include <stdio.h>
#include <stdlib.h>

struct Array
{
    int A[10];
    int size;
    int length;
};

bool Append(struct Array *arr, int val)
{
    if (arr->length < arr->size) {
        arr->A[arr->length++] = val;
        return true;
    }
    return false;
}

bool Insert(struct Array *arr, int index, int val)
{
    if (0 <= index && index < arr->length)
    {
        for (int i = arr->length; i > index; --i)
            arr->A[i] = arr->A[i-1];
        arr->A[index] = val;
        arr->length++;
        return true;
    }
    return false;
}

int Delete(struct Array *arr, int index)
{
    if (0 <= index && index < arr->length)
    {
        int tmp = arr->A[index];
        for (int i = index; i < arr->length-1; ++i)
            arr->A[i] = arr->A[i+1];
        arr->length--;
        return tmp;
    }
    return -1;
}

void DisplayArray(struct Array arr)
{
    for (int i = 0; i < arr.length; ++i)
        printf("%d ", arr.A[i]);
    printf("\n");
}

int main()
{
    struct Array arr = { {1,2,3,4,5}, 10, 5 };
    DisplayArray(arr);
    Append(&arr, 50);
    Insert(&arr, -2, 99);
    DisplayArray(arr);
    Delete(&arr, 2);
    DisplayArray(arr);
    return 0;
}
