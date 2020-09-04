03 Dynamic and Static Arrays
============================


Static Array
------------

Array with a fixed length containing n elements indexed from 0 to n-1 (meaning
that we can access the value within the array with a number).

This is used in many cases but here are some examples:

1. Storing and accessing sequential data
2. Temporarily storing objects
3. Used by IO routines as buffers
4. Lookup tables and inverse lookup tables
5. Can be used to return multiple values from a function
6. Used in dynamic programming to cache subproblem

Static Array has an access time of O(1) and linear serach of O(n); since it is
static and fixed, it cannot support insertion. append or deletion.



Dynamic Array
-------------

We may implement a resizable array to support growing data. One way to
implement this would be using the static array:

1. Create Static Array with some capacity.
2. Add elements to array while tracking the size.
3. If size reaches the capacity, allocate a new array with larger capacity and
   move over the previous to new array.


