/*
 * =====================================================================================
 *
 *       Filename:  main3.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  08/18/2020 07:58:43 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Ji-In Moon (jmoon), jmoon@jiinmoon.com
 *        Company:  
 *
 * =====================================================================================
 */

#include <iostream>
#include "Rectangle.h"

using std::cout;
using std::endl;

int main()
{
    Rectangle r;
    cout << r.area() << endl;
    r.setLength(20);
    r.setWidth(30);
    cout << r.area() <<endl;
}
