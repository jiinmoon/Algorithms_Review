/*
 * =====================================================================================
 *
 *       Filename:  main.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  08/18/2020 08:30:06 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Ji-In Moon (jmoon), jmoon@jiinmoon.com
 *        Company:  
 *
 * =====================================================================================
 */

#include <iostream>
#include "Arithmetic.h"

using std::cout;
using std::endl;

int main()
{
    Arithmetic<float> ari(0.14, 3.33);
    cout << ari.add() << endl;
    cout << ari.sub() << endl;

    Arithmetic<int> ari2(14, 33);
    cout << ari2.add() << endl;
    cout << ari2.sub() << endl;
}
