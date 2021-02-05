02 Big-O
========

How much time and space does the algorithm take to finish?

Big-O notation (among thetha, omega, ...) is created to give an uppoer bound of
the complexity in its **worst case**; allowing us to guage how much resource
that the program is going to require when the input data is arbitarily large.

i.e. if we are sorting a number, think of worst arrangement of the numbers
possible.


The order based on input size n from smallest to largest:

    1 < log(n) < n < n * log(n) < n^2 < n^3 < b^n < n!


One crucial property of the O is that it does not care for constants applied to
it and always bounded to highest. For example, we may have an algorithm whose
precise running time would be

    F(n) = 11 * n^3 + n * log(n) + n + 19

But this only is bounded as `O(F(n)) = O(n^3)`.

One important aspect of this is that we may have a case as follows:

```
int i = 0
while i < 15 do
    // code
    i += 1
```

Even though we are within a loop, this algorithm only runs for fixed amount of
time for any input sizes; just for this particular loop (without consideration
of the code that may run in the body), its time complexity would be O(1).

Another example is a case of nested loop:

```
for i in range(n):
    for j in range(i, n):
        ...
```

Here, j in the inner loop runs for n, n-1, n-2, ... , 2, 1; this is bounded by
O(n^2), no better than running a full loop.

Logrithmic complexity arises commonly with the divide-and-conquer algorithms
- where we can reduce the number of problem to solve in each step by half.
  A common one to think about is binary search. The solution can be found in
  log(n) depth as we can divide the search space in half each time.




