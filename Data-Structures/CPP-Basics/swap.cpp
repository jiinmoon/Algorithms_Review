/*
 * =====================================================================================
 *
 *       Filename:  swap.cpp
 *
 *    Description:  ll.
 *
 *        Version:  1.0
 *        Created:  08/18/2020 04:22:15 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *        Company:  
 *
 * =====================================================================================
 */

#include <iostream>

// bad usage of std
using namespace std;

void swap(int a, int b);

int main()
{
    int x = 0, y = 10;
    cout << "x : " << x << " y : " << y << endl;
    std::swap(x, y);
    cout << "x : " << x << " y : " << y << endl;

    return 0;
}

void swap(int a, int b)
{
    int t = a;
    b = a;
    a = t;
}
