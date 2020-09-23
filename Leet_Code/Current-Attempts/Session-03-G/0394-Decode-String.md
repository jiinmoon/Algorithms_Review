# 394 Decode String

Use stack to maintain the characters. Reverse back when "]" is encountered upto
integer.

---

Python:

```python

class Solution:
    def decode(self, s):
        stk = list()
        num = 0
        for char in s:
            if char.isdigit():
                num *= 10 + int(char)
            elif char == '[':
                stk.append(num)
                num = 0
            elif char == ']':
                curr = collections.deque()
                tok = stk.pop()
                while not isinstance(tok, int):
                    curr.appendleft(tok)
                    tok = stk.pop()
                stk += (list(curr) * tok)
            else:
                stk.append(char)

        return "".join(stk)
```
