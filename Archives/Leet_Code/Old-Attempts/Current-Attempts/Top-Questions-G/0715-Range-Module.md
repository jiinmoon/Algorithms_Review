# 715 Range Module

A Range Module is a module that tracks ranges of numbers. Your task is to
design and implement the following interfaces in an efficient manner.

```
addRange(int left, int right) Adds the half-open interval [left, right),
tracking every real number in that interval. Adding an interval that partially
overlaps with currently tracked numbers should add any numbers in the interval
[left, right) that are not already tracked.

queryRange(int left, int right) Returns true if and only if every real number
in the interval [left, right) is currently being tracked.

removeRange(int left, int right) Stops tracking every real number currently
being tracked in the interval [left, right).
```

---

To implement range interface, we view this problem as a number line - not as
list of intervals as we would be led to believe. Hence, we have our list of
points - also, for each of these points, we have a boolean indicator to mark
the point as whether the points upto i + 1 within the range.

Hence, insertion is finding the insertion point using binary search method on
this number line. Once left and right points are added unto the points, we
consolidate the points upto right insertion point (but exclude), as well as our
boolean indicator upto right insertion point (but exclude) as well. By default,
it should be set to True; only time we set to False would be when we find the
right insertion point is marked for deletion.

Hence, querying for a range is a simply binary search for left and right
insertion points, and check to see whether all boolean indicators within the
range are marked as True.

---

```python

import bisect

class RangeModule:
    def __init__(self):
        self.points = [0, float('inf')]
        self.isInRange = [False, False]

    def addRange(self, left, right, add=True):
        l = bisect_left(self.points, left)
        # value does not exist in points; insert new value
        if self.points[l] != left:
            self.points.insert(l, left)
            self.isInRange.insert(l, self.isInRange[l-1])

        r = bisect_left(self.points, right)
        if self.points[r] != right:
            self.points.insert(r, right)
            self.isInRange.insert(r, self.isInRange[r-1])

        # values in between are consolidated
        self.points[l:r] = [left]
        self.isInRange[l:r] = [add]

    def quertRange(self, left, right):
        l = bisect(self.points, left) - 1
        r = bisect_left(self.points, right)
        return all(self.isInRange[l:r])

    def removeRange(self, left, right):
        # to remove range, we mark the values in between as False
        self.addRange(left, right, False)
```
