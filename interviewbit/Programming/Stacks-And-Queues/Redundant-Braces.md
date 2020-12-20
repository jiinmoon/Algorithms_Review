# Redundant Braces

    Given a string A denoting an expression. It contains the following operators
    ’+’, ‘-‘, ‘*’, ‘/’.

    Chech whether A has redundant braces or not.

    Return 1 if A has redundant braces, else return 0.

    Note: A will be always a valid expression.

---

## Approach:

Use stack to maintain braces; if encountered brace is closing one, we should
pop from stack until matching open one is found. However, there is an added
condition to check for redundant - there should be an operator in between while
we do so.

O(n) in time complexity.

---

Python:

```python

class Solution:

    def isRedundant(self, A):

        stack = []

        for char in A:

            if char == ")":
                found = False
                while stack and stack[-1] != "(":
                    if stack[-1] in {"+", "-", "*", "/"}:
                        found = True
                    stack.pop()
                if not found:
                    return 1
                stack.pop()
            else:
                stack.append(char)

        return 0
```
