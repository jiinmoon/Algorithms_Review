# 161. One Edit Distance

Given two strings s and t, return true if they are both one edit distance
apart, otherwise return false.

A string s is said to be one distance apart from a string t if you can:

Insert exactly one character into s to get t.
Delete exactly one character from s to get t.
Replace exactly one character of s with a different character to get t.

---

Here, we do not actually have to perform string operations to check for whether
edited string equals to each other. Rather, we simply use pointers. If two
characters are not equal, we mark it one edited and move then smaller string
pointer backward to denote that we have inserted a value. If we encounter
different character second time, we can determine that we are editing more than
once.

Time complexity would be O(max(m, n)) and space complexity would be O(1).

---

Python:

```python

class Solution161:

    def isOneEditDistance(self, s, t):

        m, n = len(s), len(t)

        if abs(m - n) > 1 or s == t:
            return False

        if m > n:
            return self.isOneEditDistance(t, s)

        i, j, edited = 0, 0, False

        while i < m and j < n:
            if s[i] != s[j]:
                if edited:
                    return False

                edited = True
                if m != n:
                    i -= 1
            i += 1
            j += 1

        return True
```
