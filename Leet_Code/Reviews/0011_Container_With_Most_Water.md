11 Container With Most Water
============================

Question:
---------

Given n non-negative integers where each represents a point at a coordinate,
n vertical lines are drawn between two points. Find two lines such that
together with the x-axis, it forms a container that which contains most water.

Solutions:
---------

The simple solution is that we use two pointers which starts at either end of
the given list of integers. This forms our current container and to increase
its size, the only possible way would be to move the pointer that is smaller in
its height.

Codes:
------

```python
class Solution:
    def maxArea(self, heights):
        lo, hi = 0, len(heights)-1
        maxThusFar = float('-inf')
        while lo < hi:
            currArea = min(heights[lo], heights[hi]) * (hi - lo)
            if heights[lo] < heights[hi]:
                lo += 1
            else:
                hi -= 1
            maxThusFar = max(maxThusFar, currArea)
        return maxThusFar
```

---

**Source:**

LeetCode: [Container-With-Most-Water](https://leetcode.com/problems/container-with-most-water/)
