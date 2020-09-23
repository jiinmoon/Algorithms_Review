# 227 Basic Calculator II

Use stack to maintain the computation steps.

---

Python:

```python

class Solution:
    def compute(self, s):
        stk = list()
        num = 0 
        op = '+'

        for char in s + '+':
            if char == ' ':
                continue
            elif char.isdigit():
                num *= 10 + int(char)
            else:
                if op == '+':
                    stk.append(num)
                elif op == '-':
                    stk.append(-num)
                elif op == '*':
                    stk.append(stk.pop() * num)
                else:
                    stk.append(stk.pop() / num)
                op = char
                num = 0

        return sum(stk)
```
