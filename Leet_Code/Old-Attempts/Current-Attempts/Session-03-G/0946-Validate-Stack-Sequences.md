# 946 Validate Stack Sequences

Using our own stack, we try to simulate the stack sequences as given.

---

Python:

```python

class Solution:
    def validateStack(self, pushed, popped):
        popped.reverse()
        stk = list()
        for num in pushed:
            stk.append(num)
            while stk and popped and stk[-1] == popped[-1]:
                stk.pop()
                popped.pop()
        return not popped
```
