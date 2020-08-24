/*
 * =====================================================================================
 *
 *       Filename:  Stack.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  08/23/2020 09:59:04 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Ji-In Moon (jmoon), jmoon@jiinmoon.com
 *        Company:  
 *
 * =====================================================================================
 */

#include "Stack.h"

Stack::Stack(int initial_size)
{
    top = 0; 
    stack_size = initial_size;
    A = new int[stack_size];
}

Stack::~Stack() { delete []A; }


