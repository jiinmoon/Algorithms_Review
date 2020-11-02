# 682 Baseball Game

Use stack to maintain the round's scores - it is easy to manipulate the top of
the stack based on the char encountered.

---

Python:

```python

class Solution:
    def calPoints(self, ops):
        stk = list()
        for op in ops:
            if op.lstrip('-').isdigit():
                stk.append(int(op))
            elif op == '+':
                a, b = stk.pop(), stk.pop()
                stk += [b, a, a + b]
            elif op == 'D':
                stk.append(stk[-1] * 2)
            elif op == 'C':
                stk.pop()
        
        return sum(stk)
```
