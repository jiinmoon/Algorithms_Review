# 763 Partition Labels

A string S of lowercase English letters is given. We want to partition this
string into as many parts as possible so that each letter appears in at most
one part, and return a list of integers representing the size of these parts.

---

Since we want to partition in such way that each letter appears in at most one
part, we want to know the "last" time that the element appears. Hence, as we
iterate on the given string, we check to see whether the end point of the
current character has reached its end in the string.

---

Python:

```python

class Solution:
    def partition(self, s):
        lastIndex = { c:i for i, c in enumerate(s) }
        result = list()
        srt, end = 0, 0

        for i, c in enumerate(s):
            end = max(end, lastIndex[c])
            if i == end:
                result.append(end - srt + 1)
                srt = i + 1

        return result
```

