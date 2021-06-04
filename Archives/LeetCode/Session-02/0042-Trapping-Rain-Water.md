# 42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it can trap after raining.

---

We can break the problem down as a sum of individual waters trapped in a single
cell. For every cell that we visit, we can compute the amount of water that can
be trapped in this cell by finding the minimum of the two maximum heights to
the cell's left and right.

Naive implementation of above idea would result in O(n^2) time complexity where
we have to traverse to left and right for each cell that we visit in order to
find the maximum heights to left and right.

We can further make improvement in time complexity by creating record of left
and right maximum heights for each cells in linear time - but this would also
require us to have O(n) in memory as well to store these values.

Instead, we realize that we do not necessarily have to find the left and right
maximum heights for each of the cells as for any cell, only minimum of the two
heights to its left and right can possibly impact the next computation for the
amount of the water trapped for next cells.

This can be done with the two pointers and maintaining the left and right
maximum height values - hence, we can solve this problem in linear time and
O(1) in space complexity.

---

Python:

```python

class Solution42:

    def trap(self, heights):

        lmax, rmax, result = 0, 0, 0
        l, r = 0, len(heights) - 1

        while l < r:
            if heights[l] < heights[r]:
                lmax = max(lmax, heights[l])
                result += lmax - heights[l]
                l += 1
            else:
                rmax = max(rmax, heights[r])
                result += rmax - heights[r]
                r -= 1

        return result
```
