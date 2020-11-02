# 227. Basic Calculator II

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators
and empty spaces . The integer division should truncate toward zero.

---

Due to the operator precedence, we use stack to maintain our integers
encountered. By doing so, we can update the result of the operations easily by
checking the top of the stack. In the end, the result would be the sum of all
the values pushed onto the stack.

---

Python:

```python

class Solution:
    def compute(self, s):
        # by default, push onto the stack
        op = "+"
        num = 0
        stk = list()
        for char in s + "+":
            if char == " ":
                continue
            elif char.isdigit():
                num = int(char)
            else:
                if op == "+":
                    stk.append(num)
                elif op == "-":
                    stk.append(-num)
                elif op == "*":
                    stk.append(stk.pop() * num)
                elif op == "/":
                    stk.append(stk.pop() / num)
                op = char
                num = 0
        return sum(stk)
```
