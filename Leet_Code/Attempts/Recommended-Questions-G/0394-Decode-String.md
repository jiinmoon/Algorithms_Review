# 394. Decode String

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

Here, we may use backtracking or stack to build our string. We iterate on the
given string. Based on characters encountered, we have following cases:

(1) Current character is closed square bracket.

Closed square bracket indicates that we have finished with current segment of
characters - and this segment needs to be repeated by the amount we have
determined previously. Until we have our repeat number which is placed in the
stack as a guard, we pop and build up the segment. Then, we extend our stack
with the repeated string segment. Reverse the string as we have used stack.

(2) Current character is open square bracket.

This indicates that starting of the new character segment to be repeated. This
also means that previous characters encountered was number. We push our number
onto the stack so that we can repeat the segment upto next matching closed
square bracket. After that, the number should be reset.

(3) Current character is number.

It is possible that number can be multiple digits. Build upon previously seen
numbers.

(4) Otherwise, we push onto the stack.

The time complexity depends on the length of the sequence that we are going to
generate and it is O(2**n).

---

Python:

```python

class Solution:
    def decodeString(self, s):
        stk, num = list(), 0
        for char in s:
            if char == ']':
                segment = list()
                curr = stk.pop()
                while not isinstance(curr, int):
                    segment.append(curr)
                    curr = stk.pop()
                stk += (segment[::-1] * curr)
            elif char == '[':
                stk.append(num)
                num = 0
            elif char.isdigit():
                num = (num * 10) + int(char)
            else:
                stk.append(char)

        return "".join(stk)
```
