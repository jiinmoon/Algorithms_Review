# 42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it can trap after raining.

---

We can breakdown this problem into a subproblem where the total volume of water
trapped in a given elevation map is the sum of individual waters trapped on
each cell. Then, to compute the amount of water trapped on each of the cell, we
find the it depends upon the minimum of the maximum heights found to the cell's
left and right as well as the height of the cell.

Thus, if we are to brute force this problem, we would iterate on the given
elevation map. And for each of the cell, we would iterate to its left and right
to find the maximum heights to compute the amount of water trapped on that
cell. This will be O(n^2) in time complexity.

To improve upon above naive approach, we could precompute the left and right
maximum heights found for each of the cells. But this would mean that we have
to use O(n) space to store the information about the maximum heights.

The best approach would be to realize that if we use two pointer method to find
the sum of the trapped waters, the only value that can influence the next set
of volume is the minimum of the two heights (left and right). Thus, we do not
actually have to maintain the entire left and right maximum heights, but only
"current" maximum left and right heights and update them as we iterate on. This
approach would be O(n) in time complexity and O(1) in space complexity.

---

Python:

```python

class Solution:
    def trap(self, heights):
        if not heights:
            return 0

        left, right, lMax, rMax, total = 0, len(heights)-1, 0, 0, 0
        while left < right:
            if heights[left] < heights[r]:
                if lMax <= heights[left]:
                    lMax = heights[left]
                else:
                    total += (lMax - heights[left])
                left += 1
            else:
                if rMax <= heights[right]:
                    rMax = heights[right]
                else:
                    total += (rMax - heights[right])
                right -= 1

        return total
```
