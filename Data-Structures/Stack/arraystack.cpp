/*
 * =====================================================================================
 *
 *       Filename:  arraystack.cpp
 *
 *    Description:  Implments Stack.h using array. 
 *
 *        Version:  1.0
 *        Created:  08/16/2020 09:45:15 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Ji-In Moon (jmoon), jmoon@jiinmoon.com
 *        Company:  
 *
 * =====================================================================================
 */

#ifndef STACK_H
#include "arraystack.h"
#endif

#include <stdexcept>

template <class T>
void stack<T>::push(T item)
{
    if (needToResize()) 
        resize();
    data[top] = item;
    top ++;
}

template <class T>
T stack<T>::peek()
{
    if (top <= 0)
        throw std::out_of_range("peek at empty stack");
    return data[top-1];
}

template <class T>
T stack<T>::pop()
{
    if (top <= 0)
        throw std::out_of_range("pop at empty stack");
    top --;
    return data[top];
}

template <class T>
void stack<T>::resize()
{
    T* newdata = new T[size*2];
    for (int i = 0; i < size; i++)
        newdata[i] = data[i];
    delete data;
    data = newdata;
    size *= 2;
}

template <class T>
bool stack<T>::isEmpty() { return top == 0;}

template <class T>
bool stack<T>::needToResize() { return top == size; }
