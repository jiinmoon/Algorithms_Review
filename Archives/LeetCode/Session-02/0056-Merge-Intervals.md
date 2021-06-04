# 56. Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all
overlapping intervals, and return an array of the non-overlapping intervals
that cover all the intervals in the input.

---

We can easily merge intervals by comparing every pair of intervals; previous
interval's end time should be less than the next interval's start time. To do
so, we should first sort the given list of intervals by its starting time.
Hence, the time complexity is bounded by the sorting algorithm's time
complexity of O(n * log(n)).

---

Python:

```python

class Solution56:

    def merge(self, intervals):

        intervals.sort()

        result = [intervals[0]]

        for i in intervals[1:]:
            if result[-1][1] < i[0]:
                result.append(i)
            else:
                result[-1][1] = max(result[-1][1], i[1])

        return result
```
