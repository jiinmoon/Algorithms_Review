# 155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element
in constant time.

```
push(x) -- Push element x onto stack.

pop() -- Removes the element on top of the stack.

top() -- Get the top element.

getMin() -- Retrieve the minimum element in the stack.
```

---

#### (1) Two Stacks.

We can implment min stack via using two stacks. One stack is dedicated to
maintain the current minimum of the elements in the stack on the top. This is
done by when we push unto our stack, we check on top of our min stack; if the
value is found to be the less than (or new minimum), then we can also push unto
our min stack. Likewise, when we pop, we should also check against the top of
our min stack to update our minimum. This approach can implement all the
operations in constant time complexity.

#### (2) Single Stack.

We may also consolidate above approach into a single stack by storing not just
the value, but also the minimum of the stack that is propagated upwards to the
top.

---

Python: Two Stacks.

```python

class Solution155:

    def __init__(self):
        self.stk = []
        self.mStk = []

    def push(self, x):
        if self.mStk and self.mStk[-1] >= x:
            self.mStk.append(x)
        self.stk.append(x)

    def pop(self):
        if self.stk:
            val = self.stk.pop()
            if self.mStk and self.mStk[-1] == val:
                self.mStk.pop()
            return val
        return -1

    def top(self):
        if self.stk:
            return self.stk[-1]
        return -1

    def getMin(self):
        if self.mStk:
            return self.mStk[-1]
        return -1
```

Python: Single Stack.

```python

class Solution155:

    def __init__(self):
        self.stk = [ (float('inf'), float('inf') ]

    def push(self, x):
        self.stk.append( (x, min(x, self.stk[-1][1]) )

    def pop(self):
        return self.stk.pop()[0]

    def top(self):
        return self.stk[-1][0]

    def getMin(self):
        return self.stk[-1][1]
```
