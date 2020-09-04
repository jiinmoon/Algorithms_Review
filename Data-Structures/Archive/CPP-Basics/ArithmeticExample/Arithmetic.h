/*
 * =====================================================================================
 *
 *       Filename:  Arithmetic.h
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  08/18/2020 08:23:55 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Ji-In Moon (jmoon), jmoon@jiinmoon.com
 *        Company:  
 *
 * =====================================================================================
 */

#ifndef ARITH_H
#define ARITH_H

// generic
template<class T>
class Arithmetic
{
    private:
        T a;
        T b;
    public:
        Arithmetic(T a, T b);
        T add();
        T sub();
        ~Arithmetic();
};

template<class T>
Arithmetic<T>::Arithmetic(T a, T b)
{
    this->a = a;
    this->b = b;
}

template<class T>
T Arithmetic<T>::add() { return a + b; }

template<class T>
T Arithmetic<T>::sub() { return a - b; }

template<class T>
Arithmetic<T>::~Arithmetic() {};

#endif
