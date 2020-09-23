# 42 Trapping Rain Water

The total trapped rain water is equal to the amount that each cell can hold
 which is bounded by the minimum of the left and right maximum heights found
 from that cell.

If so, then the naive approach would be to for each cell, expand left and right
to find the maximum heights. The better approach that can reduce this time
complexity further would be to use extra data structure to store all the left
and right maximum heights at each index.

But we can also realize that only the minimum of the two heights can affect the
changing trapped rain water from the current position. So, we only have to move
down from the left or right while keeping track of the maximum height from the
left and right. This can complete the algorithm in O(n) time complexity and
O(1) in space complexity.

---

Python:

```python

class Solution:
    def trap(self, heights):
        l, r, lm, rm = 0, len(heights)-1, 0, 0
        total = 0
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
