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

void doubleNum(int &num)
{
    num *= 2;
}

int main()
{
    int x = 100;
    std::cout << x << std::endl;
    doubleNum(x);
    std::cout << x << std::endl;
    int *p = &x;
    doubleNum(*p);
    std::cout << x << std::endl;
    doubleNum(x);
    std::cout << x << std::endl;

    return 0;
}
