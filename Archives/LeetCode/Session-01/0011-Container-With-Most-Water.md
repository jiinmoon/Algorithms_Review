# 11. Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point
at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
of the line i is at (i, ai) and (i, 0). Find two lines, which, together with
the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

---

We can find the maximum area formed by the two lines in a linear time
complexity by using two pointer method. By starting from both end of the line,
we can compute the current area occupied by the two points - then, only way
that the area can increase would be to move the "smaller" point line inwards.
Hence, only a single pass is enough to gurantee the maximum area.

---

Python:

```python

class Solution11:

    def maxArea(self, height):

        l, r = 0, len(height) - 1
        result = 0

        while l < r:
            
            result = max(result, min(height[l], height[r]) * (r - l))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return result
```
