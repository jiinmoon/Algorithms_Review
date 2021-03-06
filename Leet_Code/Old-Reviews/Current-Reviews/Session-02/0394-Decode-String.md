394 Decode String
=================

Given an encoded string, return its decoded string.

The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside
the square brackets is being repeated exactly k times. Note that k is
guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces,
square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits
and that digits are only for those repeat numbers, k. For example, there won't
be input like `3a` or `2[4]`.

---

We can use recursion to evaluate the result inside the brackets - or likewise,
iteratively but use stack.

---

Python: Stack approach.

```python
class Paren:
   OPEN = "["
   CLOSED = "]"

class Solution:
    def decodeString(self, s):
        stk = list()
        n = 0
        for char in s:
            if char is Paren.OPEN:
                stk.append(n)
                n = 0
            elif char is Paren.CLOSED:
                currCharSegment = list()
                curr = stk.pop()
                while not isinstance(curr, int):
                    currCharSegment.append(curr)
                    curr = stk.pop()
                stk += (currCharSegment * curr)
            elif char.isdigit():
                n = (n * 10) + int(char)
            else:
                stk.append(char)
        return "".join(stk)
```

Python: Recursive solution.

```python
class Solution:
    def decodeString(self, s):
        self.i = 0
        
        # each decode calls will decode segment upto "]"
        def decode(s):
            res = []
            currChar = s[self.i]
            while self.i < len(s) and currChar != ']':
                if !currChar.isDigit():
                    # simple case of a character without repeating
                    res.append(currChar)
                    self.i += 1
                else:
                    # repeat number encountered
                    n = 0
                    while s[self.i].isdigit():
                        n += 1
                    # repeat the segment inside the "[...]"
                    # discard "["
                    self.i += 1
                    res += (decode(s) * n)
                    # discard "]"
                    self.i += 1
            return res

        return "".join(decode(s))
```



