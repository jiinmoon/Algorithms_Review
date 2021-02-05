# 56 Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

---

In order to merge all intervals, we first need to sort the given intervals by
their starting times. Then, we iterate on each of the intervals to check the
end times. If the previous interval's end time is less than the start time of
the next interval, we can safely include the interval to our result. Otherwise,
we need to update the end time and skip the next interval.

---

Python:

```python

class Solution:
    def merge(self, intervals):
        intervals.sort()
        result = [ intervals[0] ]

        for interval in intervals[1:]:
            if result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])

        return result
```
