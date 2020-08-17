/*
 * =====================================================================================
 *
 *       Filename:  arraystacktester.cpp
 *
 *    Description:  tests arraystack.h 
 *
 *        Version:  1.0
 *        Created:  08/16/2020 09:58:06 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Ji-In Moon (jmoon), jmoon@jiinmoon.com
 *        Company:  
 *
 * =====================================================================================
 */

#include <iostream>
#include "arraystack.h"

using namespace std;

int main()
{
    stack<int> stk; 
    cout << stk.isEmpty() << endl; 
    for (int i = 0; i < 5; i++)
        stk.push(i);
    cout << stk.peek() << endl; // 4
    while (!stk.isEmpty())
        cout << stk.pop() << " ";
    cout << endl;

    return 0;
}
