# 56. Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

---

We first sort the given intervals by its first starting times. Once we have
done so, we can do a comparison between previous and next intervals. If the
last ending time of the previous interval is less than the start time of the
next intervals, we can update the previous to merge the two together by
updating the last element by the maximum of the two. Otherwise, we can add the
next intervals as is. Since the sorting is involved, the time complexity would
be of O(n * log(n)).

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
