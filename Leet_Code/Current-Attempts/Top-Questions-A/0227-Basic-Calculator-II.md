# 227 Basic Calculator II

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators
and empty spaces . The integer division should truncate toward zero.

---

We use stack data structure to maintain our integers and perform operations.
Due to operator precedence, operators such as * and / can be easily performed
with stack by performing these arithmetic operations with top of the stack
immediately when encountered.

---

Python:

```python

class Solution:
    def calculate(self, s):
        stk = list()
        op = "+"
        num = 0

        for char in s + "+":
            if char == " ":
                continue
            elif char.isdigit():
                num *= 10 + int(char)
            else:
                if op == "+":
                    stk.append(num)
                elif op == "-":
                    stk.append(-num)
                elif op == "*":
                    stk.append(stk.pop() * num)
                else:
                    stk.append(stk.pop() / num)
                op = char
                num = 0

        return sum(stk)
```
