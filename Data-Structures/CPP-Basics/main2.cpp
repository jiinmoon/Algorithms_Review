/*
 * =====================================================================================
 *
 *       Filename:  main2.cpp
 *
 *    Description:  Converting C to C++. 
 *
 *        Version:  1.0
 *        Created:  08/18/2020 07:23:50 PM
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

// previously, we had struct Rectangle
// and have functions outside where it takes in Rectangle pointers
// in order to modify.

// now, change to class; and class will have public/private members.
// we may also move the functions within the class
// so that it makes more sense
class Rectangle
{
    private:
        int length;
        int width;
    public:
        // constructor
        Rectangle(int l, int w)
        {
            length = l;
            width = w;
        }

        void set_length(int l) { length = l; }
        void set_width(int w) { width = w; }
        int area() { return length * width; }
};

int main()
{
    // heap allocation
    Rectangle *r = new Rectangle(10, 20);
    cout << r->area() << endl;
    free(r);
    return 0;
}
