/*
 * =====================================================================================
 *
 *       Filename:  arraystack.h
 *
 *    Description:  Defines stack interface that uses array underneath. 
 *
 *        Version:  1.0
 *        Created:  08/16/2020 09:40:42 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Ji-In Moon (jmoon), jmoon@jiinmoon.com
 *        Company:  
 *
 * =====================================================================================
 */

#define STACK_H

template <class T>
class stack
{
    private:
        T* data;
        int top;
        int size;
        void resize();
        bool needToResize();

    public:
        stack()
        {
            size = 5;
            data = new T[size];
            top = 0;
        }
        void push(T item);
        T peek();
        T pop();
        bool isEmpty();
};

#include "arraystack.cpp"
