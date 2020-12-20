# Rain Water Trapped

    Given an integer array A of non-negative integers representing an elevation map
    where the width of each bar is 1, compute how much water it is able to trap
    after raining.

---

## Approach:

We think of this problem as finding the total sum of individual water trapped
on each of the cells. The amount of water that can be trapped is bounded by the
minimum of the two maximum heights found to its left and right. Hence, naive
implementation is to find the left and right maximum heights for every index we
visit. O(n^2) in time complexity. We can improve this further down to O(n) if
we use space to record the left and right max heights first but would also
require O(n) in space.

Better approach would be to use two pointers by realizing that only ever one of
the maximum height can change. Hence, we record the maximum heights as we move
forward our pointers. O(n) in time complexity but O(1) in space.

---

Python:

```python

class Solution:

    def trap(self, height):

        l, r, lmax, rmax, total = 0, len(height) - 1, 0, 0, 0

        while l < r:

            if height[l] < height[r]:
                
                lmax = max(lmax, height[l])
                total += lmax - height[l]
                l += 1
            
            else:
                
                rmax = max(rmax, height[r])
                total += rmax - height[r]
                r -= 1

        return total
```
