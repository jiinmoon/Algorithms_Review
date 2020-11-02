# 763. Partition Labels

A string S of lowercase English letters is given. We want to partition this
string into as many parts as possible so that each letter appears in at most
one part, and return a list of integers representing the size of these parts.

---

To partition the given string S, first we create a mapping of the "last" index
that each of the character appears in. As we iterate on the given string, if
the current index is marked as the last index in the mapping, then we can add
it onto our result.

---

Python:

```python

class Solution:
    def partitionLabels(self, s):
        counter = {c:i for i, c in enumerate(s)}
        start, end = 0, 0
        result = list()
        for i, c in enumerate(s):
            end = max(end, counter[c])
            if i == end:
                result.append(end - start + 1)
                start = i + 1
        return result
```

