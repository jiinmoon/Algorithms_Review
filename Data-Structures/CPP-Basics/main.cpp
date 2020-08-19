/*
 * =====================================================================================
 *
 *       Filename:  main.cpp
 *
 *    Description:  Basic reviews on C/CPP.
 *
 *        Version:  1.0
 *        Created:  08/18/2020 02:28:08 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Ji-In Moon (jmoon), jmoon@jiinmoon.com
 *        Company:  
 *
 * =====================================================================================
 */

#include <iostream>

struct Cards
{
    enum Shape 
    { 
        DIAMOND = 'D', 
        CLUB = 'C', 
        HEART = 'H', 
        SPADE = 'S'
    };
    int face;
    Shape shape;
};

void intSwap(int a, int b)
{
    int temp;
    temp = a;
    b = a;
    a = temp;
}

// overloaded function
void intSwap(int* a, int* b)
{
    int t = *a;
    // dereference, and change its value at that pointed location
    *a = *b;
    *b = t;
}

void intSwapRef(int& a, int& b)
{
    int t = a;
    a = b;
    b = t;
}

void doubleArr(int *A, const int n)
{
    for (int i = 0; i < n; ++i)
        // this is exactly same as A[i]
        // it is syntatic sugar
        *(A+i) *= 2;
}

// creating an array on heap
int* createArr(const int size)
{
    int *p;
    p = (int *) malloc(size * sizeof(int));
    return p;
}

void changeCard(Cards &c)
{
    c.face = 13;
    c.shape = Cards::HEART;
}

void changeCard(Cards *c)
{
    (*c).face = 22;
    c->shape = Cards::CLUB;
}

int main()
{
    Cards c;
    c.face = 10;
    c.shape = Cards::Shape::DIAMOND;
    std::cout << (char) c.shape << c.face << std::endl; 

    int a = 10;
    int *pa = &a;
    *pa = 100;
    std::cout << "a: " << a << " *pa: " << *pa << std::endl;
    std::cout << "&a: " << &a << " &pa: " << &pa 
            <<  " pa : " << pa << std::endl;

    // Creating an array in heap 
    // using C
    // p = (int *) malloc(5 * sizeof(int));
    // using C++
    // p = new int[5];
   
    // reference is just an alias
    // its address is exactly same as int a
    // note that pointer HAS a different address
    // pointer stores the address of its pointed value
    int &r = a;
    std::cout << "r: " << r << " &r: " << &r << std::endl;
    r += 10;
    std::cout << "a: " << a << " r: " << r <<" &r: " << &r << std::endl;
    // why have reference/alias?
    // it is for passing parameters to the function
    // by default, parameters are initialized with arguments passed in 
    // so, its copy by value
    // changes made to the parameter won't be reflected once function is
    // terminated; thus, we either pass in the pointer or reference
    
    // Pointer to struct
    Cards c2 {11, Cards::Shape::CLUB};
    Cards *pc = &c2;
    // (*pc).face dereferences first then access face member
    // otherwise *pc.face gets pointer to non-existent face in pc
    // more simply, we may use -> to access member of pointed
    std::cout << (*pc).face << " " << (char) pc->shape << std::endl;
    
    // creating pointer to struct on heap
    Cards *pc2;
    pc2 = (Cards*) malloc(sizeof(Cards));
    pc2->face = 13;
    pc2->shape = Cards::DIAMOND;
    free(pc2);


    // passing parameters to function
    // pass by value
    // this does NOT change the value of x and y
    int x (0), y (10);
    std::cout << "x : " << x << " y : " << y << std::endl;
    intSwap(x, y);
    std::cout << "x : " << x << " y : " << y << std::endl;

    // pass by pointer
    intSwap(&x, &y);
    std::cout << "x : " << x << " y : " << y << std::endl;

    // pass by reference;
    // only for C++
    intSwapRef(x, y);
    std::cout << "x : " << x << " y : " << y << std::endl;

    // pass array as parameter
    // array is already pointers
    // so this will be passed in as a pointer to first element
    // this implies determining size will be difficult
    int arr[] = { 1, 2, 3 };
    doubleArr(arr, sizeof(arr)/sizeof(int));
    for (auto i : arr)
        std::cout << i << " ";
    std::cout << std::endl;

    int *p;
    p = createArr(10);
    for (size_t i = 0; i < 10; ++i)
        p[i] = i;
    doubleArr(p, 10);
    for (size_t i = 0; i < 10; ++i)
        std::cout << p[i] << " ";
    std::cout << std::endl;
    free(p);

    // structures as parameter
    // structures are likely to be modified within a function
    // we can either pass as a reference or pointer
    Cards c3;
    changeCard(c3);
    std::cout << c3.face << " " << (char) c3.shape << std::endl;
    changeCard(&c3);
    std::cout << c3.face << " " << (char) c3.shape << std::endl;

    return 0;
}

