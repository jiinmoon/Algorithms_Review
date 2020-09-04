#ifndef ARRAY_H
#define ARRAY_H

#include <stdexcept>

template <typename T>
class Array
{
    private:
        std::size_t length;
        std::size_t capacity;
        T *arr;

    public:
        Array();
        Array(int);
        ~Array();

        std::size_t size();
        bool isEmpty();
        T get(int);
        void set(int, T);
        void clear();
        void add(T);
        T removeAt(int);
};

template <typename T>
Array<T>::Array() : Array(10) {};


template <typename T>
Array<T>::Array(int const initialCapacity) 
{ 
    if (initialCapacity < 0)
        throw std::invalid_argument(
                "Invalid initial capacity specified: " + std::to_string(initialCapacity));
    length = 0;
    capacity = initialCapacity;
    arr = new T[initialCapacity];
}

template <typename T>
Array<T>::~Array() { delete [] arr; }

template <typename T>
std::size_t Array<T>::size() { return length; }

template <typename T>
bool Array<T>::isEmpty() { return size() == 0; }

template <typename T>
T Array<T>::get(int index) 
{  
    if (index < 0 || index > capacity)
        throw std::out_of_range(
                "Error: Index out of bounds: " + std::to_string(index));
    return arr[index];
}

template <typename T>
void Array<T>::set(int index, T element) 
{
    if (index < 0 || index > capacity)
        throw std::out_of_range(
                "Error: Index out of bounds: " + std::to_string(index));
    arr[index] = element;
}

template <typename T>
void Array<T>::clear()
{
    delete [] arr;
    arr = new T[capacity];
    length = 0;
}

template <typename T>
void Array<T>::add(T element)
{



}
#endif
