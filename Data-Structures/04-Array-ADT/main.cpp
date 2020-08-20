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

int maxOf(int x, int y) { return (x >= y) ? x : y; }
int minOf(int x, int y) { return (x < y) ? x : y; }

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

int LinearSearch(struct Array *arr, int key)
{
    for (int i = 0; i < arr->length; ++i)
        if (arr->A[i] == key)
            return i;
    return -1;
}

// assumes sorted arr
int BinSearch(struct Array *arr, int key, int lo, int hi)
{
    while (lo <= hi)
    {
        int mid = lo + (hi - lo) * 0.5;
        if (arr->A[mid] == key) 
            return mid;
        (arr->A[mid] > key) ? 
            hi = mid - 1 : 
            lo = mid + 1;
    }
    return -1;
}

int Get(struct Array *arr, int index)
{
    if (0 <= index && index < arr->length)
        return arr->A[index];
    return -1;
}

bool Set(struct Array *arr, int index, int key)
{
    if (0 <= index && index < arr->length)
    {
        arr->A[index] = key;
        return true;
    }
    return false;
}

int Max(struct Array *arr)
{
    if (arr->length > 0)
    {
        int maxThusFar = arr->A[0];
        for (int i = 0; i < arr->length; ++i)
            maxThusFar = maxOf(maxThusFar, arr->A[i]);
        return maxThusFar;
    }
    return -1;
}

int Min(struct Array *arr)
{
    if (arr->length > 0)
    {
        int minThusFar = arr->A[0];
        for (int i = 0; i < arr->length; ++i)
            minThusFar = minOf(minThusFar, arr->A[i]);
        return minThusFar;
    }
    return -1;
}

int Sum(struct Array *arr)
{
    if (arr->length > 0)
    {
        int sum = 0;
        for (int i = 0; i < arr->length; ++i)
            sum += arr->A[i];
        return sum;
    }
    return -1;
}

int Avg(struct Array *arr)
{
    int sum = Sum(arr);
    return (sum > 0) ? sum / arr->length : sum;
}

bool Reverse(struct Array *arr)
{
    if (arr->length != 0)
    {
        for (int i = 0, j = arr->length-1; i < j; ++i, --j)
        {
            int t = arr->A[i];
            arr->A[i] = arr->A[j];
            arr->A[j] = t;
        }
        return true;
    }
    return false;
}

bool LShift(struct Array *arr)
{
    if (arr->length != 0)
    {
        int t = arr->A[0];
        for (int i = 0; i < arr->length-1; ++i)
            arr->A[i] = arr->A[i+1];
        arr->A[arr->length-1] = t;
        return true;
    }
    return false;
}


void DisplayArray(struct Array *arr)
{
    for (int i = 0; i < arr->length; ++i)
        printf("%d ", arr->A[i]);
    printf("\n");
}

int main()
{
    struct Array arr = { {1,2,3,4,5}, 10, 5 };
    DisplayArray(&arr);
    Append(&arr, 50);
    Insert(&arr, -2, 99);
    DisplayArray(&arr);
    Delete(&arr, 2);
    DisplayArray(&arr);
    printf("%d is at %d\n", 50, LinearSearch(&arr, 50));
    printf("%d is at %d\n", 1, BinSearch(&arr, 1, 0, arr.length));
    printf("Max is %d\n", Max(&arr));
    printf("Sum is %d\n", Sum(&arr));
    printf("Avg is %d\n", Avg(&arr));
    Reverse(&arr);
    DisplayArray(&arr);
    LShift(&arr);
    DisplayArray(&arr);
    
    return 0;
}
