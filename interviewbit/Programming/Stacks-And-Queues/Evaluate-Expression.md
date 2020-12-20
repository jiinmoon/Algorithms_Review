# Evaluate Expression

    Evaluate the value of an arithmetic expression in Reverse Polish Notation.

    Valid operators are +, -, *, /. Each operand may be an integer or another
    expression.

---

## Approach:

We use stack to maintain previous values we encounter. If operator is
encountered, we perform operation on previous two values in the stack, and
return the result back to the stack.

O(n) in time complexity.

---

Python:

```python

class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        
        stack = []
        
        for s in A:
            
            if s in {"+", "-", "*", "/"}:
                num2, num1 = stack.pop(), stack.pop()
                if s == "+":
                    stack.append(num1 + num2)
                elif s == "-":
                    stack.append(num1 - num2)
                elif s == "*":
                    stack.append(num1 * num2)
                elif s == "/":
                    stack.append(num1 // num2)

            else:
                stack.append(int(s))
        
        return stack[-1]
```
