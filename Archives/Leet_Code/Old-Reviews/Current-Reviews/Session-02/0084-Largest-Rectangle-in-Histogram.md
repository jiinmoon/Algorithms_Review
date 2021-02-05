84 Largest Rectangle in Histogram
=================================

Given n non-negative integers representing the histogram's bar height where the
width of the bar is 1, find the largest rectangle area.

---

Brute Force approach would be to for each bar, we expand left and right until
we can build the largest rectangle. This would be O(n^2) approach.

A better approach would be to treat each bar as the minimum of the running
rectangle. We look-back to previous bars to left as long as previous bars are
higher than current bar - and for each bar we found this way, we compute the
largest area for them. To maintain the previous bars, we use stack to push in
the indicies of each bars. And pop when we compute the area.

---

Python:

```python
class Solution:
    def largestRectangleInHist(self, histogram):
        if not histogram:
            return 0
        maxAreaThusFar = 0
        # since we need to look behind, we need extra 0s at start and end
        histogram = [0] + histogram + [0]
        # stack guard to start the process
        stk = [0]
        for index, bar in enumerate(histogram[1:], 1):
            # look behind as far as heights are greater than current
            while histogram[stk[-1]] > bar:
                height = histogram[stk.pop()]
                width = i - stk[-1] - 1
                maxAreaThusFar = max(maxAreaThusFar, height * width)
            stk.append(index)
        return maxAreaThusFar
```

