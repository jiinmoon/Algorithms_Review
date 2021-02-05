# 42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it can trap after raining.

---

We can visualize this problem as a collection of individual water trapped on
the cell. To determine the amount of water trappd on any particular cell
requires us to find the left and right maximum heights from the cell. We may
precompute the left and right maximum heights for each of the cells but this
requires O(n) additional space. If we approach this problem as a two pointer
problem, we notice that only minimum of the left and right maximum heights
matter for every computation. This will complete the problem in O(n) in time
complexity without additional space.

---

Python:

```python

class Solution:
    def trap(self, heights):
        if not heights:
            return 0

        l, r, lm, rm, total = 0, len(heights)-1, 0, 0, 0
        while l < r:
            if heights[l] < heights[r]:
                if lm <= heights[l]:
                    lm = heights[l]
                else:
                    total += (lm - heights[l])
                l += 1
            else:
                if rm <= heights[r]:
                    rm = heights[r]
                else:
                    total += (rm - heights[r])
                r -= 1

        return total
```
