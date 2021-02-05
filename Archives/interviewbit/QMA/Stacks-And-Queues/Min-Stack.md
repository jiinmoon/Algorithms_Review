# Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element
in constant time.

push(x) – Push element x onto stack.
pop() – Removes the element on top of the stack.
top() – Get the top element.
getMin() – Retrieve the minimum element in the stack.


Note that all the operations have to be constant time operations.

Questions to ask the interviewer :

Q: What should getMin() do on empty stack? 
A: In this case, return -1.

Q: What should pop do on empty stack? 
A: In this case, nothing. 

Q: What should top() do on empty stack?
A: In this case, return -1

---

### (1) Two Stacks.

Dedicate one stack solely to maintain min values on top of its stack. As we
push, we check against the minStack and also push onto minStack. When we pop,
check top of minStack as well and pop if match.

### (2) Single Stack.

Create a pair of (val, min) and have stack propagate up the min to top whenever
we push by checking the top of stack.

---

Python:

```python

class MinStack:
    
    def __init__(self):
        self.stack = [(float('inf'), float('inf'))]
        
    # @param x, an integer
    def push(self, x):
        self.stack.append((x, min(self.stack[-1][1], x)))

    # @return nothing
    def pop(self):
        if len(self.stack) == 1:
            return
        self.stack.pop()

    # @return an integer
    def top(self):
        if len(self.stack) > 1:
            return self.stack[-1][0]
        return -1

    # @return an integer
    def getMin(self):
        if len(self.stack) > 1:
            return self.stack[-1][1]
        return -1

```
