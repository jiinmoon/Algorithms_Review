# 20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and
']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

---

We can check for the validity using the stack data structure since the input
string is valid iff open brackets must be closed by not only the same type of
brackets but also in "correct" order. This would be O(n) in both time and space
complexity.

---

Python: Stack approach.

```python

class Solution20:

    def __init__(self):
        self.bracketMap = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

    def isValid(self, s):
        stk = []

        for char in s:
            if char in { "(", "[", "{" }:
                stk.append(char)
            else:
                if not stk or stk.pop() != self.bracketMap[char]:
                    return False
                stk.pop()
        
        # edge case:
        # possible that unbalanced number of brackets present
        # i.e. more open brackets then closing ones
        return not stk
```
