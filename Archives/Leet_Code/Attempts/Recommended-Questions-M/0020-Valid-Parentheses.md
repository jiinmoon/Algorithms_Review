# 20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and
']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

---

To confirm whether given string contains the characters which are valid, we
employ stack and its LIFO nature to match the given brackets. It is as follows:
 when we encounter the open bracket, we push unto the stack. If the encountered
 bracket is closed, then we check the top of the stack - it should be of the
 correct matching open braket. In the end, the stack should be empty.

This algorithm should complete in O(n) time complexity.

---

Python:

```python

class Solution:
    def isValidParentheses(self, s):
        bracketMap = {
            "]" : "[",
            ")" : "(",
            "}" : "{"
        }
        stk = list()
        for char in s:
            if char in { "[", "{", "(" }:
                stk.append(char)
            else:
                if not stk or stk[-1] != bracketMap[char]:
                    return False

        return not stk
```
