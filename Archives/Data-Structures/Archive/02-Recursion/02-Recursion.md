# 2 Recursion

- A function that calls upon itself.

```
T func(parameter)
{
    if (condition) { // terminate }
    // code
    func(parameter)
    // code
}
```

- Base condition defines how the function will terminate.
- Otherwise, this will loop indefinately.

```cpp
void printNum(int n)
{
    if (n < 0) { return; }
    cout << n << endl;
    printNum(n-1);
}
```

- Above, we have a base condition that will terminate the recursion once it
  reaches below 0.
- This will print number from 10 to 0.
- What would hapeen IF the print statement was placed AFTER the recursive call
  to itself?
- First, the function will recursively call itself down until n reaches -1.
- Then, functions will start to "come back out" of recursion, terminating one
  after another.
- `printNum(-1)` terminates -> `printNum(0)` is next in line, printing 0.
- This continues and will print number from 0 to 10 in this case.

## Recursion and Stack

- We know that function is placed onto the stack while executing.
- Same is true for recursive function calls; each call will place the function
  onto the stack on top of each other.
- If not careful, this can quickly fill up the stack and run out of memory!
- Especially true for recursive calls that makes more recursive calls each time
  (i.e. recursive Fibonacci).

## Static Variable and Stack

- Static variable exists outside of each functions.
- Same would be true for a global variable.

## Types of Recursion
### Tail Recursion

- if the last statement of the recursive funcsion it calling itself, then it is
  called "Tail Recursion".

```
fn(n) {
    if (n > 0)
        fn(n-1);
}
```

- Everything would be performed at call time.
- If there is some remaining work to perform AFTER recursive call, it is not
  tail recursion.

```
fn(n) {
    if (n <0)
        fn(n-1) + 1;    // still work left over; not tail recursion
}
```

- One noticeable aspect of tail recursion is that it can be easily mapped to
  iterative loop.

```
fn(n) {
    while (n >0) {
        // do something
        --n;
    }
}
```

- Difference is in space: since recursive function require stack space for each
  function created, above trivial logic will be in O(n) space.
- But iterative approach would be in O(1).

- A good compiler will catch this kind of Tail Recursions; and then optimize it
  to iterative counterpart whenever possible.

### Head Recursion

- If the recursive call is made as a first statement, then it is a "head
  recursion".

```
fn(n) {
    if (n > 0) {
        fn(n-1)
        // do something
    }
}
```

- All process is done at returning time.
- This is not so easily converted to the iterative loop - will most likely
  require additional variables to count.
- But like all recursions, it can be done - just not as obvious as tail
  recursions.

### Tree Recursion

- "Linear recursion" makes recursive call once.
- "Tree recursion" will make recursive call multiple times.

```
fn(n) {
    if (n < 0) {
        fn(n-1);
        fn(n-1);
    }
}
```

- Above example, at each level, two more functions will be created.
- i.e. if `fn(3)` is called, first level will be 1 call; next level, 2 calls;
  third level, 4 and finally reaches 8 on last level.
- O(2^n) time complexity. Space will require height of the tree O(n).

### Indirect Recursion

- There will be multiple recursive functions calling one another - in circular
  fashion.

```
fn_A(n) {
    if (n > 0) {
        fn_B(n-1)
    }
}

fn_B(n) {
    if (n >0) {
        fn_A(n-1)
    }
}
```

- A -> B -> A -> ... until terminating condition is met; then start returning

### Nested Recursion

- "Nested recursion" refers to functions that makes recursive calls with
  a parameter that itself is a recursive call.

```
fn(n) {
    if (n > 0) {
        fn(fn(n-1));
    }
}
```


