# 20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and
']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

---

Here, we can use LIFO nature of the stack to look at previous characters
examined. So long as the character is open parentheses, we can push unto our
stack. Otherwise, closing bracket encountered must have a matching opening
bracket on top of our stack. Time complexity would be O(n) and space complexity
would be O(n).

---

Python:


```python

class Solution20:

    def isValid(self, s):

        m = { ")" : "(", "}" : "{", "]" : "[" }
        stack = []

        for char in s:
            if char in {"(", "{", "["}:
                stack.append(char)
            else:
                if not stack or m[char] != stack[-1]:
                    return False
                stack.pop()
        
        return not stack
```
