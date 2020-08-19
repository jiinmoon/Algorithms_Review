/*
 * =====================================================================================
 *
 *       Filename:  arrays.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  08/19/2020 10:27:32 AM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Ji-In Moon (jmoon), jmoon@jiinmoon.com
 *        Company:  
 *
 * =====================================================================================
 */

#include <iostream>
// malloc
#include <stdlib.h>

// different ways to initialize an array
void array_initialization()
{
    // array is an contiguous memory segment
    // if int array size 5 is made, suppose first memory address starts at 100;
    // then, next element will be accessed at 104, 108, 112, 116
    // 4 bytes or 32 bits refer to the individual sizeof(int)

    // uninitialized - garbage
    int A[5];
    // initialized to [1,2,3,4,5]
    int B[5] = {1,2,3,4,5};
    // initialized to [1,2,0,0,0]
    int C[5] = {1,2};
    // initialized to [0,0,0,0,0]
    int D[5] = {0};
    // initialized to [1,2,3,4,5]
    int E[] = {1,2,3,4,5};
    
    // array elements are accessed through subscript(index)
    A[0] = 10;      // changes first element in A from 1 to 10
    // or accessed through pointer
    *(A+2) = 100;   // changes third element in A from 3 to 100;
}

void array_in_heap()
{
    int *p, *q;
    // c style
    const size_t arr_size (4);
    p = (int *) malloc(arr_size * sizeof(int));
    for (size_t i = 0; i < arr_size; ++i)
    {
        int j;
        std::cin >> j;
        p[i] = j;
    }
    for (size_t i = 0; i < arr_size; ++i)
        std::cout << *(p+i) << " ";
    std::cout << std::endl;
    free(p);
    // C++
    q = new int[arr_size * 2];
    for (size_t i = 0; i < arr_size; ++ i)
        q[i] = p[i];
    p = q;
    q = 0; // same as NULL, or nullptr.
    for (size_t i = 0; i < arr_size * 2; ++i)
        std::cout << *(p+i) << " "; 
    std::cout << std::endl;
    delete(p);
}

int main()
{
    array_in_heap();
    return 0;
}
