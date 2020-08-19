/*
 * =====================================================================================
 *
 *       Filename:  calmain.cpp
 *
 *    Description:  main tester for calculator. 
 *
 *        Version:  1.0
 *        Created:  08/16/2020 10:52:44 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Ji-In Moon (jmoon), jmoon@jiinmoon.com
 *        Company:  
 *
 * =====================================================================================
 */

#include <iostream>
#include "calculator.cpp"

using namespace std;

int main()
{
    cout << evaluate("3+5-2") << endl;
    cout << evaluate("3+5*2") << endl;
    cout << evaluate("3*5-2") << endl;
    cout << evaluate("3*(5-2)") << endl;
    return 0;
}
