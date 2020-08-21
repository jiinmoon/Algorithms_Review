/*
 * =====================================================================================
 *
 *       Filename:  main-in-cpp.cpp
 *
 *    Description:  Array ADT in C++
 *    
 *
 *        Version:  1.0
 *        Created:  08/20/2020 01:17:52 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Ji-In Moon (jmoon), jmoon@jiinmoon.com
 *        Company:  
 *
 * =====================================================================================
 */

#include <iostream>

using std::cout;
using std::endl;

const size_t DEFAULT_A_SIZE = 10;

template<class T>
class Array 
{
    private:
        T *A;
        size_t length; // current length of A
        size_t size;   // max allowed elements in A
        bool isValidIndex(size_t index);
    public:
        Array() 
        {
            length = 0;
            size = DEFAULT_A_SIZE;
            A = new T[DEFAULT_A_SIZE];
        }
        Array(int SIZE) 
        {
            size = SIZE;
            length = 0;
            A = new T[DEFAULT_A_SIZE];
        }
        ~Array() { delete []A; }
        void Print();
        void Append(T item);
        void Insert(int index, T item);
        void Delete(int index);
        T Get(int index);
        bool IsEmpty();
        bool IsFull();
};

template<class T>
bool Array<T>::isValidIndex(size_t index) { return 0 <= index && index < length; }

template<class T>
bool Array<T>::IsEmpty() { return size == 0; };

template<class T>
bool Array<T>::IsFull() { return length == size; };

template<class T>
void Array<T>::Print()
{
    for (size_t i = 0; i < length; ++i)
        std::cout << A[i] << " ";
    cout << endl;
}

template<class T>
void Array<T>::Append(T item)
{
    if (!IsFull())
        A[length++] = item;
}
