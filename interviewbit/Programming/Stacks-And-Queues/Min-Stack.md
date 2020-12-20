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

## Approach:

We can do this wither either two stacks or single one. In the case of single
stack, we maintain the tuple of (x, minVal). When we push, we update the minVal
as minimum of previous and current x.

---

Python:

```python

class MinStack:

    def __init__(self):
        self.stack = [(float('inf'), float('inf')]

    def push(self, x):
        self.stack.append((x, min(x, self.stack[-1][1])))

    def pop(self):
        if len(self.stack) > 1:
            self.stack.pop()

    def top(self):
        if len(self.stack) > 1:
            return self.stack[-1][0]
        return -1

    def getMin(self):
        if len(self.stack) > 1:
            return self.stack[-1][1]
        return -1
```
