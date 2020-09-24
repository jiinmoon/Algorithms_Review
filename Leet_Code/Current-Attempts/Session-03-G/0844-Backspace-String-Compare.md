# 844 Backspace String Compare

Use stack to maintain the string as we iterate on them.

---

Python:

```python

class Solution:
    def backspaceCompare(self, s, t):
        def helper(str):
            stk = list()
            for char in str:
                if char != "#":
                    stk.append(char)
                elif stk:
                    stk.pop()
            return "".join(stk)
        return helper(s) == helper(t)
```
