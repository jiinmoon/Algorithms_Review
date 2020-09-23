# 56 Merge Intervals

Iterate on each intervals - if the next interval has a front value greater than
the last interval's back value, we update the last interval to merge with next.
Otherwise, we can safely append.

---

Python:

```python

class Solution:
    def mergeIntervals(self, intervals):
        intervals.sort()
        res = [intervals[0]]
        for interval in intervals[1:]:
            if res[-1][1] >= interval[0]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)

        return res
```

