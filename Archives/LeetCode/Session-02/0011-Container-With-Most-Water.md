# 11. Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point
at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
of the line i is at (i, ai) and (i, 0). Find two lines, which, together with
the x-axis forms a container, such that the container contains the most water.

---

We can start by realizing that the minimum of the two heights can only change
at the minimum of the two. Hence, starting from either end of
the given points, we move the current minimum height inward. This would be
linear in time complexity.

---

Python:

```python

class Solution11:

    def maxArea(self, heights):
        
        l, r, result= 0, len(heights) - 1, 0

        while l < r:
            
            result = max(result, (heights[r] - heights[l]) * (r - l))

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return result 
```
