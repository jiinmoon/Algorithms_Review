#include <iostream>
#include "Array.h"

using std::cout;
using std::endl;

int main()
{
    Array<int> A = Array<int>(10);
    for (int i = 0; i < 5; ++i)
        A.set(i, i);
    for (int i = 0; i < 5; ++i)
        cout << A.get(i) << " ";
    cout << endl;


    return 0;
};
