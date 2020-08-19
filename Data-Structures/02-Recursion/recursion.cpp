/*
 * =====================================================================================
 *
 *       Filename:  recursion.cpp
 *
 *    Description:   
 *
 *        Version:  1.0
 *        Created:  08/19/2020 08:09:49 AM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Ji-In Moon (jmoon), jmoon@jiinmoon.com
 *        Company:  
 *
 * =====================================================================================
 */

#include <iostream>

void printNum1(int n)
{
    if (n < 0) return;
    std::cout << n << std::endl;
    printNum1(n-1);
}

void printNum2(int n)
{
    if (n < 0) return;
    printNum2(n-1);
    std::cout << n << std::endl;
}

// equivalent to (n*(n+1)) * 0.5
int sumNaturalNums(int n)
{
    if (n == 0)
        return 0;
    return sumNaturalNums(n-1) + n;
}

int factorialOf(int n)
{
    if (n == 0)
        return 1;
    return factorialOf(n-1) * n;
}

int powOf(int base, int n)
{
    if (n == 0) return base;
    return powOf(base, n-1) * base;
}

// requires less multiplication ops
// if even we can reduce it
// if odd, take one base out
int powOfImp(int base, int n)
{
    if (n == 0) return 1;
    if (n%2 == 0)
        return powOfImp(base * base, n * 0.5);
    return base * powOfImp(base * base, (n-1) * 0.5);
}

int main()
{
    int n (10);
    int base (5);
    printNum1(n);
    printNum2(n);
    std::cout << "Sum 1..10 : " << sumNaturalNums(n) << std::endl;
    std::cout << "10! : " << factorialOf(n) << std::endl;
    std::cout << "5^10 : " << powOf(base, n) << std::endl;
    std::cout << "5^10 : " << powOfImp(base, n) << std::endl;
}
