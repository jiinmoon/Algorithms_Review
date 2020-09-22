844 Backspace String Compare
============================

Given two strings S and T, return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

---

We can either use stack data structure or two pointers to simulate the input
from the both of the strings.

---

Python: stack approach:

```python
class Solution:
    def backspaceCompare(self, S, T):
        def helper(s):
            stk = list()
            for char in s:
                if char != "#":
                    stk.append(char)
                elif stk:
                    stk.pop()
            return "".join(stk)

        return helper(S) == helper(T)
```


