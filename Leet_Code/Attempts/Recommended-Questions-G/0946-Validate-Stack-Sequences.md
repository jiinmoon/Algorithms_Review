# 946. Validate Stack Sequences

Given two sequences pushed and popped with distinct values, return true if and
only if this could have been the result of a sequence of push and pop
operations on an initially empty stack.

---

We simply create a stack and emulate the sequence that is given from the
"pushed" and "popped" list. For each value we find the the pushed, we push onto
our stack. Then, until top of our stack is equal to the top of popped, we pop
from our stack. In the end, our stack and popped stack should be empty.

---

Python:

```python

class Solution:
    def isValidStackSequence(self, pushed, popped):
        stk = list()
        popped.reverse()
        for num in pushed:
            stk.append(num)
            while popped and stk and stk[-1] == popped[-1]:
                stk.pop()
                popped.pop()
        return not stk and not popped
```
