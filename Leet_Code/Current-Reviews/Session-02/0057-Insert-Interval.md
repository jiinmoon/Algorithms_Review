57 Insert Interval
==================

Given a set of non-overlapping intervals, insert a new interval into the
intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their
start times.

---

First, we find the position of the new interval on the given intervals list.
This is done by expanding to left and right - finding the left interval and
right interval.

If they are found, then we update the new interval; its first value should be
minimum of either its first value of left interval or itself and likewise for
its second value.

Then, we may insert the new interval.

---

Python:

```python
class Solution:
    def insert(self, intervals, new):
        m = len(intervals)
        left, right = 0, m-1

        while left < m and new[0] > intervals[left][1]: left += 1
        while right >= 0 and new[1] < intervals[right][0]: right -= 1

        if left <= right:
            new[0] = min(new[0], intervals[left][0])
            new[1] = max(new[1], intervals[right][1])

        return intervals[:left] + [new] + intervals[right+1:]
```

