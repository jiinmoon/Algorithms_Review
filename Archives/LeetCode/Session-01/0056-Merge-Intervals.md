# 56. Merge Intervals

Given an array of intervals where intervals[i] = [start\_i, end\_i], merge all
overlapping intervals, and return an array of the non-overlapping intervals
that cover all the intervals in the input.

---

We can simplify the merging process by first sorting the intervals by its
starting times. Then, as we iterate forward, we compare previous interval's end
time against the current interval's start time. If previous end time is
smaller, we can safely add current interval; otherwise, we have to update the
previous end time by whichever end time that is larger.

---

Python:

```python

class Solution56:

    def mergeIntervals(self, intervals):

        if not intervals:
            return []

        intervals.sort()

        result = [intervals[0]]

        for i in intervals[1:]:
            if result[-1][1] < i[0]:
                result.append(i)
            else:
                result[-1][1] = max(result[-1][1], i[1])
        
        return result
```
