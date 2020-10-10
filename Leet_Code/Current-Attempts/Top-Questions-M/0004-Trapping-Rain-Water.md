# 4 Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it is able to trap after raining.

---

First, we approach this problem by how we can find the water trapped under
a single bar - then, it is only a matter of adding up all the waters that we
find as we iterate on the given elevation map.

To find this, we notice that we will have to find the maximum height to current
bar's left and right - and take a minimum of two minus the current bar height.

However, naively trying to find the maximum height to left and right for every
cell costs us a linear time - which in overall achieves O(n^2) in time
complexity. If we iterate on the given elevation map beforehand, and pre-record
all the left and right maximum heights for each bar, then we can reduce the
time complexity to O(n) but it will also require O(n) in space.

Here, we notice a crucial point that the amount of the water trapped is only
ever bounded by the minimum of the left or right - meaning that we only have to
change the minimum of the bar to find the amount of water trapped. Hence, we
start from both end of the map. Then, we compare their heights - this allows us
to determine which bar that we need to move and how it will affect the total
water.

---

Python:

```python

class Solution:
    def trap(self, height):
        if not height:
            return 0

        l, r = 0, 0
        lmax, rmax, total = 0, 0, 0

        while l < r:
            if height[l] < height[r]:
                if lmax <= height[l]:
                    lmax = height[l]
                else:
                    total += (lmax - height[l])
                l += 1
            else:
                if rmax <= height[r]:
                    rmax = height[r]
                else:
                    total += (rmax - height[r])
                r -= 1

        return total
```
