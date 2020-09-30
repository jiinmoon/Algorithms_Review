# 763 Partition Labels

A string S of lowercase English letters is given. We want to partition this
string into as many parts as possible so that each letter appears in at most
one part, and return a list of integers representing the size of these parts.

---

We record each character's last appearance (its index). Then, as we iterate on
the given string, we check to see whether current char is at its last index
- indicating that we can split into a part and save current partition point.

---

Python:

```python

class Solution:
    def partitionLabels(self, s):
        srt, end = 0, 0
        result = list()
        d = { c: i for i, c in enumerate(s) }

        for i, char in enumerate(s):
            end = max(end, d[char])
            if i == end:
                result.append(end - srt + 1)
                srt = i + 1

        return result
```
