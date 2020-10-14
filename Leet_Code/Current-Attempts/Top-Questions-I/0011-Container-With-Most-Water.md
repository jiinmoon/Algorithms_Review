# 11 Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point
at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
of the line i is at (i, ai) and (i, 0). Find two lines, which, together with
the x-axis forms a container, such that the container contains the most water.

---

Naive solution would involve searching for every line to check for valid
conatiner and its water content. We can improve upon this by utilizing the two
pointer method since only way for the water content to change once we have
chosen two heights is that we move the lower height to find the potentially
better position. This should be able to complete within O(n) time complexity.

---

Python:

```python

class Solution:
    def maxArea(self, height):
        def helper(lo, hi):
            return min(height[lo], height[hi]) * (hi - lo)

        l, r, result = 0, len(height) - 1, 0
        
        while l < r:
            result = max(result, helper(l, r))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return result
```
