# 715. Range Module

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

To support this module, a binary search method would be most efficient way to
be able to add, query, and remove given ranges as we can find their positions
on our number line in logrithmic time.

However, difficulty here is that we may remove or add over the ranges that are
already present. For this case, we maintain a separate boolean list that can
tell us whether the included number in the number line is present or not.

Suppose adding a range, (left, right). We can first perform binary search for
its insertion point in our number line as far left as possible. If the added
value is not already present, then we add a value at its found insertion point.
While doing so, we also need to mark the value as a valid part of number (that
is not to be tracked or not). Suppose that we have inserted left and right at
position i and j. Then, every value in between should be updated as well as
mark them as True for query.

Querying for a range should then be performing binary search for left and right
range values, and looking up its validity - every value inbetween left and
right should be marked as True.

Then, removing a range is actually same as adding a range, but simply reversing
the mark as False.

---

Python:

```python

from bisect import bisect_left, bisect_right

class RangeModule:
    def __init__(self):
        # number line
        self.range = [0, float('inf')] 
        # marks whether number is to track and included in range or not
        self.isInRange = [False, False]

    def addRange(self, left, right, toAdd=True):
        # insert left to number line
        i = bisect_left(self.range, left)
        if self.range[i] != left:
            self.range.insert(i, left)
            # also insert mark
            self.isInRange.insert(i, self.isInRange[i-1])

        # insert right to number line
        j = bisect_left(self.range, right)
        if self.points[j] != right:
            self.range.insert(j, right)
            self.isInRange.insert(j, self.isInRange[j-1])

        # update in-between (left ~ right)
        self.range[i:j] = [left]
        self.isInRange[i:j] = [toAdd]

    def queryRange(self, left, right):
        # find rightmost occurrence of left
        i = bisect_right(self.range, left)
        j = bisect_left(self.range, right)
        # range inbetween should all be marked as in-range
        return all(self.isInRange[i:j]

    def removeRange(self, left, right):
        # inverse of addRange - mark them as False
        self.addRange(left, right, toAdd=False)
```
