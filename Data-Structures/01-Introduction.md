# 1 Data Structures Introduction
## Data structure

- How to arrange data in a such way that we can access and move them
  efficiently throughout our machine.
- Also, how to define _efficient_ operations on data?

- Data resides in the main memory (RAM).
- Our program and some data files will reside within the disk storage (SSD or
  HDD).
- When the program executes, CPU will place a necessary data onto the main
  memory as process runs.

- Application will sometimes need to access the data on the disk and put it
  unto the main memory as required. Think of a typical databases.

## Stack v Heap Memory

- Every memory is divided into a byte. And every byte memory location has an
  address.
- Suppose a segment of a main memory address that starts at 0 and ends at
  65535.
- This means that this segment can store about ~64 KB of memory.

- CPU loads the program into the code section of the memory (usually starts at
  0); it contains actual machine instructions to carry out, static and
  constants, and so on.
- On top, there will be a stack - where functions allocate their locally scoped
  variables. It will grow up and down as program executes.
- Heap begins at high address (in this case, 65535) and grows downward. Once
  allocated on the heap, the objects here will not be destroyed unlike those on
  the stack which can be deallocated once the function terminates.

- Stack is organized; every function call will sit on top of each other.
- Heap is unorganized; it is regarded as a resource.

- In C, we use `malloc` and in C++, `new` is used to allocate to Heap.
- Proper management of lifecycle of objects created on Heap is mandatory to
  avoid memory leaks - uncleaned up memory that is left in the heap. This will
  cause application to take up more and more space in the heap; and ask for
  more pages from kernel.
- Deallocate with `free` or `delete`.

- This applies to langauges where garbage collector is not used such as C and
  C++; Java, Go and other languages trade off runtime speed to run extra
  garbage collector that take care of unused objects to prevent memory leaks.
  This is done by identifying whethere there exist any object in memory that no
  one is referencing to - which marks it safe to delete.

## Physical v Logical Data Structures
### Physical

- Array and Linked List are "physical" since it determines how the memory is
  allocated and organized within the main memory.

- For example, in array, its elements are next to one another; and it is
  statically sized.
- It can be created in stack or heap.

- Linked List by contrast is dynamically resizable - adding more nodes.
- Nodes will be created on the heap. Head pointer can be in stack.

### Logical

- Stack, Queue, Trees, HashMap, and Graphs are "logical".

- Stack and Queue are refered to as "linear".
- Stack is LIFO; Queue is FIFO.

- To implment these logical data structures, we use physical data structure(s).

## ADT

- Abstract Data Type (ADT).
- Data Type is defined as
    - Representation of Data and,
    - Operation on Data.

- For example, `int` data type can be represented with 2 bytes; if it is
  signed, first bit is reserved for indicate sign otherwise nothing.
- And `int` allows for operations such as addition, subtraction,
  multiplication, and so on.

- Abtract means "hiding" the detail about the implmentation.
- For example, we do not need to know how addition is carried out with two
  `int` in low level in order for us to use it.

### List ADT

- List ADT is represented as a list of elements.
- It requires a space for storing elements.
- It may also define operations.
    - Add(T);
    - Remove(T);
    - Find(T);
    - Size();
    - IsEmpty();

- To implement it, we may either use Array or LinkedList.
