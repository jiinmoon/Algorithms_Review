# Balanced Parentheses

    Given a string A consisting only of '(' and ')'.

    You need to find whether parantheses in A is balanced or not ,if it is balanced
    then return 1 else return 0.

---

Python:

```python

class Solution:

    def isBalanced(self, A):

        stack = []

        for char in A:

            if char == "(":
                stack.append(char)
            elif char == ")":
                if not stack:
                    return 0
                stack.pop()
        
        return not stack
```
