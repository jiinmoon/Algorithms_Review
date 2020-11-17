# 42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it can trap after raining.

---

We can think of the total amount of water trapped as a sum of subproblems where
computes the individual amount of water trapped in a cell. To compute this, we
have to determine the minimum of the two maximum heights found to cell's left
and right, and take away the height of the cell.

Naively, we can attempt to compute the left and right maximum heights for each
cell that we visit by scanning left and right. This is O(n^2) in time
complexity as we are required to scan for every cell.

Improvement can be made by trading off space where we can record the maximum
heights starting from each cell, which allows us to compute in O(n) time
complexity as well as space.

Best approach that can still compute in O(n) but does not require any space
would be to use two pointer method. We realize that at any given cell, the
one of the maximum heights is fixed - and that either left or right can change.
Hence, by starting from either ends of the list, we can update the left and
right maximum heights as we iterate inwards.

---

Python:

```python

class Solution:
    def trap(self, heights):
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

