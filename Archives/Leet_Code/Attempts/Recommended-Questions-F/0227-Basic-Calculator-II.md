# 227. Basic Calculator II

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators
and empty spaces . The integer division should truncate toward zero.

---

We may save the computed values onto the stack so that we can deal with the
precedence of the operators ("*" and "/") easily by looking back on the top of
the stack. The algorithm should be O(n) in time complexity.

---

Python:

```python

class Solution:
    def calculate(self, s):
        op = "+"
        stk = list()
        num = 0
        for char in s + "+":
            if char.isdigit():
                num *= 10 + int(char)
            elif char == " ":
                continue
            else:
                if op == "+":
                    stk.append(num)
                elif op == "-":
                    stk.append(-num)
                elif op == "*":
                    stk.append(stk.pop() * num)
                elif op == "/":
                    stk.append(stk.pop() / num)
                num = 0
                op = char
        return sum(stk)
```
