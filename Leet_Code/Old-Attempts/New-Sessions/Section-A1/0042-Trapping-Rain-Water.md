# 42 Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it can trap after raining.

---

We think of the simplest case of a single cell - the amount of water that can
be trapped within a single cell is bounded by the minimum of maximum heights to
its left and right; so we can repeat this process and sum to find the total
water trapped.

The problem is that to repeatedly find the left and right maximum heights on
every cell will be exhaustive and cost us O(2n) in time complexity for each
iteration. This can be avoided by precomputing the left and right maximum
heights and record the information.

Even better approach that does not require any additional space is realizing
that only height that influences the amount of water trapped should be the
minimum of the two heights - hence, we treat this problem as two-pointer
problem and maintain the left and right max heights found thus far.

---

Python:

```python

class Solution:
    def trap(self, heights):
        if not heights:
            return 0

        l, r, lmax, rmax, total = 0, len(heights)-1, 0, 0, 0
        
        while l < r:
            if heights[l] < heights[r]:
                if lmax <= heights[l]:
                    lmax = heights[l]
                else:
                    total += (lmax - heights[l])
                l += 1
            else:
                if rmax <= heights[r]:
                    rmax = heights[r]
                else:
                    total += (rmax - heights[r])
                r -= 1

        return total
```
