57 Insert Interval
==================

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
    def insert(self, intervals, new_interval):
        m = len(intervals)
        l, r = 0, m-1

        while l < m and new_interval[0] > intervals[l][1]:
            l += 1;
        while r >=0 and new_interval[1] < intervals[r][0]:
            r -= 1;

        if l <= r:
            new_interval[0] = min(new_interval[0], intervals[l][0])
            new_interval[1] = min(new_interval[1], intervals[r][1])

        return intervals[:l] + [new_interval] + intervals[r+1:]
```
