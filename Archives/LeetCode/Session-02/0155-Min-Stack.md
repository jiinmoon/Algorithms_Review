# 155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element
in constant time.

Implement the MinStack class:

```
MinStack() initializes the stack object.

void push(val) pushes the element val onto the stack.

void pop() removes the element on the top of the stack.

int top() gets the top element of the stack.

int getMin() retrieves the minimum element in the stack.
```

---

To maintain the min such that we can retrieve it in constant time, we can
simply implment another stack that is used solely for maintain the minimum
elements that we have encountered thus far. As new elements are pushed, we also
check against this extra "min" stack; if the new element is new minimum, then
we also push this element unto our min stack as well. Same principle applies to
pop operation as well.

We can ideally use a single stack here as well where we would instead store
tuple of element and the minimum of the stack. We can do this by whenever we
push in, we compare against the top of our stack and propagate up the minimum
if the previous minimum is found to be lower.

---

Python: Single-stack approach.

```python

class Solution155:

    def __init__(self):
        self.stack = [(None, float('inf'))]

    def push(self, val):
        self.stack.append( (val, min(self.stack[-1][1], val)) )
    
    def pop(self):
        return self.stack.pop()[0]

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]
```

