/*
 * =====================================================================================
 *
 *       Filename:  Stack.h
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  08/23/2020 09:52:11 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Ji-In Moon (jmoon), jmoon@jiinmoon.com
 *        Company:  
 *
 * =====================================================================================
 */
#ifndef STACK_H
#define STACK_H

#include <string>

class Stack
{
    private:
        int stack_size;
        int top;
        int* A;
        void regrow();
    public:
        Stack(int initial_size=10);
        ~Stack();
        void push(int val);
        int pop();
        int peek();
        bool isEmpty();
        int size();
        std::string toString();
};

#endif
