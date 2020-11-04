# 986. Interval List Intersections

Given two lists of closed intervals, each list of intervals is pairwise
disjoint and in sorted order.

Return the intersection of these two interval lists.

---

To find all the overlapping intersection between two list of closed intervals,
we iterate on the both lists, taking a look at both intervals at the time. The
start time should be the maximum of the either two starting time; and end time
is the minimum of the either two ending times. If we can find the start time
indeed is less than the end times, then currently found interval between start
to end is the intersection. Otherwise, we need to check the end times of two:
if first end time is less than second, then we move forward the first pointer
and vice versa. It should complete in O(m + n).

---

Python:

```python

class Solution:
    def intervalIntersection(self, A, B):
        i, j = 0, 0
        result = []

        while i < len(A) and j < len(B):
            start = max(A[i][0], B[j][0])
            end = min(A[i][1], B[j][1])
            if start <= end:
                result.append([start, end])

            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return result
```
