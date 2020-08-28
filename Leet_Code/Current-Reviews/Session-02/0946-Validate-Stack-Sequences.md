946 Validate Stack Sequences
============================

Given two sequences pushed and popped with distinct values, return true if and
only if this could have been the result of a sequence of push and pop
operations on an initially empty stack.

---

Simply, we maintain a stack. For every value in the pushed, we first push unto
the stack. Then, while the top of the stack matches the top of the popped, we
pop from both our stack and the popped. If we do not have any elements left
over in popped, we have our valid stack sequence.

---

Python:

```python
class Solution:
    def isValidStackSequence(self, pushed, popped):
        stk = []
        popped.reverse()
        for num in pushed:
            stk.append(num)
            while stk and stk[-1] == popped[-1]:
                stk.pop()
                popped.pop()
        return not popped
```

