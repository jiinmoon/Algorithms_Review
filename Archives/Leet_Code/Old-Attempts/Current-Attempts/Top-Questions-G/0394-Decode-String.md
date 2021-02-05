# 394 Decode String

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded\_string], where the encoded\_string inside the
square brackets is being repeated exactly k times. Note that k is guaranteed to
be a positive integer.

You may assume that the input string is always valid; No extra white spaces,
square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits
and that digits are only for those repeat numbers, k. For example, there won't
be input like 3a or 2[4].

---

We can use stack to maintain the string while we are decoding the encoded part
of the string as we exaimning each characters.

There are four cases:

1. Encountered character is of digit; then, character is a k that denotes the
   repeat amount for encoded\_string to follow. Since we do not know how many
   digits, we update our num but do not push to stack yet.

2. Encountered character is open bracket; then, it denotes the start of the
   encoded\_string. Hence, we can now push the stored num (repeat amount) and
   reset the num for next. Discard the current char as it served no purpose (we
   may use it as a guard when we pop, but we have integer that already present.

3. Encountered character is closed bracket; this signals the end of
   encoded\_string. We pop off from the stack until we encounter a integer that
   will represent a repeat amount for current segment.

3. Otherwise, we can push unto the stack the regular characters.

---

Python:

```python

class Solution:
    def decodeString(self, s):
        stk = list()
        num = 0
        for char in s:
            if char.isdigit():
                num *= 10 + int(char)
            elif char == '[':
                stk.append(num)
                num = 0
            elif char == ']':
                curr = list()
                tok = stk.pop()
                while not isinstance(tok, int):
                    curr = [tok] + curr
                    tok = stk.pop()
                stk += (curr * tok)
            else:
                stk.append(char)
        return "".join(stk)
```
