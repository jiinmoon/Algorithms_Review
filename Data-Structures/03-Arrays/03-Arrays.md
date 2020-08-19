# 3 Arrays
## Array in Memory

- Suppose we are declaring an array of ints sized 5.

    int A[5];

- Array is nothing but pointers to the contiguous segment of memory that has
  been allocated and reserved to be used as an array.
- So, above is simply same as a pointer to the first element in the array.
- Suppose that this address is 4000.
- Then, second element would be found at 4004; and continue in every 4 bytes
  - 4008, 4012, 4016.
- This 4 bytes refer to `sizeof(int)`.

## Static vs Dynamic

- If the size of the array is known at COMPILE time, this is static array.
- If the size of the array has to be figured out at RUN time, this is dynamic
  array.

- C only has static arrays whereas C++ also supports dynamic array to allocate
  on stack.

```cpp
int main()
{
    std::cin >> n;
    int A[n];
}
```

- To assign on heap, we need a pointer then use `new` or `malloc` depending on
  C++ or C.
- Need to delete allocated memory in heap with `delete`.

```cpp
int main()
{
    int *p;
    // c++
    p = new int[5];
    delete([]p);
    // c
    int *p2;
    p2 = (int *) malloc(5 * sizeof(int));
    free(p2);
}
```

- Array elements are accessed with subscript (index) or pointer.

## Increasing Size of Array

```cpp
size_t size = 5;
int *p = new int[size];
int *q = new int[size*2];
// copy over
// there are other options in STL such as std::copy;
// in case of C, memcpy; but careful since if it is pointers, then they will
// simpy point to old objects.
for (int i = 0; i < size; ++i)
    q[i] = p[i];
delete ([]p);
p = q;
q = Null;
```

## 2D Array

```
// array of 3 rows and 4 columns
int A[3][4];
// but in actuality, this is simply a single array with rows coming after
// another, and we could write a wrapper function to treat it as such.


// rows in heap
int *A[3];
A[0] = new int[4];
A[1] = new int[4];
A[2] = new int[4];

// even A is on heap
int **A;
A = new int*[3]; // array of pointers to int array size 3 on heap
A[0] = new int[4];
A[1] = new int[4];
A[2] = new int[4];
```

## Array Management by Compiler

- At compile time, we do not know the address of where array (or any variable
  for this matter) is going to be allocated.

```
int A[3] = {1,2,3};
A[2] = 10;
```

- Here, compiler needs to know the address of `A[2]` but this won't be known
  until runtime and arrays are actually allocated.

- Compiler solves this by have a L0 as address of the first element in the
  array, then performs pointer arithmetic.
- In this case, let's assuome `A` is at memory location 200. Then, compiler
  will perform `200 + 3 * (sizeof int)` to find the location where value lies.

- So, `L0 + 3 * sizeof(int)` where sizeof int is compiler/architecture
  dependent;`L0 + i * w` where i is index, w is size of data type.
- This is a related, logical address.

- We seen that previous 2D array is actually represented as a consecutive
  linear memory.

- This is done by mapping the rows and columns; this is called row-major, and
  column-major mappings.

- **row-major** maps the rows one after another ([row1, row2, row3, ...]).
- **column-major** maps the cols one after another ([col1, col2 col3, ...]).

- Let's take a look at **row-major** mapping example:
    - Suppose `int A[3][4]`, and array begins at address 200, and int size is 2 bytes.
    - first row is located from 200 ~ 206; second from 208 ~ 214; and last 216~222;
    - To access `A[1][2]`, row 1 needs to be converted.
    - `(200) + (1 * 4 + 2) * 2`
    - The `Address of A[i][j]` is `L0 + [i * n + j] * w` where n is # of cols.

- In the case of **column-major** mapping.
    - `Address of A[i][j]` is `L0 + [j * m + i] * w` where m is # of rows.

- C and C++ compilers follow row-major format.



