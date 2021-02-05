# Container With Most Water

Given n non-negative integers a1, a2, ..., an,
where each represents a point at coordinate (i, ai).
'n' vertical lines are drawn such that the two endpoints of line i is at (i,
ai) and (i, 0).

Find two lines, which together with x-axis forms a container, such that the
container contains the most water.

Your program should return an integer which corresponds to the maximum area of
water that can be contained ( Yes, we know maximum area instead of maximum
volume sounds weird. But this is 2D plane we are working with for simplicity ).

---

We notice that from arbitary coordinates x, y where x < y, the area of the
water that can be trapped would be based on minimum of two heights * (y - x).
And for next step, only way to potentially find greater container is to move
the minimum of the two. Hence, we can use two pointer method here to find the
result in O(n) time complexity.

---

Python:

```python

class Solution:

    def maxArea(self, A):

        result, l, r = 0, 0, len(A) - 1

        while l < r:

            curr = min(A[l], A[r]) * (r - l)

            result = max(result, curr)

            if A[l] < A[r]:
                l += 1
            else:
                r -= 1

        return result
```
