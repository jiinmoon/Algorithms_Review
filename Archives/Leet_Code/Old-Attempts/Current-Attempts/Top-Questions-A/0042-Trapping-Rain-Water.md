# 42 Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it is able to trap after raining.

---

We can think of total water trapped as a individual cell collecting the max
water possible - this is computed by first finding the highest height to the
cell's left and right; the minimum of the two is the highest amount of water
that can be trapped for the particular cell, but we also need to account for
the cell's own height.

One way to approach this is that for each cell, we repeatedly traverse left and
right to find the left and right maximum heights. This will take O(n^2).

O(n) time complexity is achieved by using an extra space, and precomputation on
the given integers to find the left and right max heights so that we can look
it up easily.

We can achieve the same linear time complexity but without the need for O(n)
space once we realize that at each cell, it is bounded by the minimum of the
two heights to its left and right. Then, for next cell, only way that the total
water trapped can be influenced is the changing the which ever was the lowest
from the left or right. Hence, we only need to maintain a single left max and
a right max value and update them as necessary from both end of the integers.

---

Python:

```python

class Solution:
    def trap(self, nums):
        l, r = 0, len(nums)-1
        lmax, rmax, total = 0, 0, 0
        while l < r:
            if nums[l] < nums[r]:
                if lmax <= nums[l]:
                    lmax = nums[l]
                else:
                    total += (lmax - nums[l])
                l += 1
            else:
                if rmax <= nums[r]:
                    rmax = nums[r]
                else:
                    total += (rmax - nums[r])
                r -= 1
        return total
```
