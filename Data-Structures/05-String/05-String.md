# 5 String

- Text in the computer is represented as binary numbers ultimately.
- The standard mapping from number to text is down with standards.
- English alphabet and common used characters are represented in ASCII.
- Other langauges in Unicode.

- There are total 0 to 128 ASCII codes - which can be represented in 7 bits
  (but it will be stored to whichever word size of the architecture).
- Unicode is represented in 2 bytes and in hexadeciaml format (four 4 bits or
  0x0000).

## String as char array

- In C, string is a sequence of characters put together.

```c
char c;
c = 'A';    // ok;
c = 'AB';   // error; not a single character
c = "A";    // error; double quote is for string literals
printf("%d", c);
```

- In above code, c will store number 65.

```c
// [ D, o, o, m, \0, 0, 0, 0, 0, 0 ]
char name[10] = {'D', 'o', 'o', 'm', '\0'};
```

- In both C and C++, strings are terminated with null character '\0' to
  represents the end of string.

```
char name2[] = {'D', 'o', 'o', 'm', '\0'};
char name3[] = "Doom";      // compilter automatically adds null char
printf("%s", name2);        // terminates on null char
scaf("%s", name);           // reads and appends null char 
gets(name);                 // reads until newline
```

- Notes on `char *` to initialize a string:

```
char *pname = "John";
```

- Here, "John" is not created on the heap! It is located in the static data
  section of the program memory. Thus, the correct way would be to declare it
  `const` since panme is pointing at constant and read-only memory.

- Also note that arrays decay to pointers, and pointers can be used with array
  syntax, they are still different entities; for example, you cannot use
  `sizeof` to get the size of pointed segment of data while array can.


