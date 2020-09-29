# 53 Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

---

Firstable, we sort the intervals by its start times. Then, we iterate on the
intervals, comparing against the previous interval. If the last element of the
previous interval is "greater" than the first element of the current interval
(i.e. (10,15), (7, 20)), then we can safely merge two by updating the last
element of the previous interval as a maximum of the two last element of the
intervals.

This process should be O(n * log(n)) - lower bound on the comparison based
sorting.

---

Python:

```python

class Solution:
    def mergeIntervals(self, intervals):
        intervals.sort()
        result = [intervals[0]]

        for interval in intervals[1:]:
            if result[-1][1] >= interval[0]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)

        return result
```
