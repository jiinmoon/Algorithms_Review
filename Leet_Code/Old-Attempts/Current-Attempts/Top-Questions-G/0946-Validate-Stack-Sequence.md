# 946 Validate Stack Sequence

Given two sequences pushed and popped with distinct values, return true if and
only if this could have been the result of a sequence of push and pop
operations on an initially empty stack.

---

We simply try to replicate the process with a stack - push every element and
pop every element as given by the list of push and pop elements.

---

Python:

```python

class Solution:
    def isValidStackSequence(self, pushed, popped):
        popped = popped[::-1]
        stk = list()

        for num in pushed:
            stk.append(num)
            while stk and stk[-1] == popped[-1]:
                stk.pop()
                popped.pop()

        return not popped
```
