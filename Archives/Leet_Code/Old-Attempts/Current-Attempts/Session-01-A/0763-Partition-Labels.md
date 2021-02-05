# 763 Partition Labels

The point here is in maintaining the hashmap of chars to their last appearing
indicies. As we iterate on the given string, if the current index matches with
the last index, then we can record to our result.

---

```python

class Solution:
    def partitionLabels(self, s):
        d = { c: i for i, c in enumerate(s) }
        srt, end = 0, 0
        res = list()

        for i in range(len(s)):
            end = max(end, d[s[i]])
            if i == end:
                res.append(end - srt + 1)
                srt = i + 1

        return res
```
