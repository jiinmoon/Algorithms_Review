# 42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it can trap after raining.

---

We can break the problem down to a single cell - and ask how much water is
trapped by each of the cells, and sum all the waters trapped for each cell. To
compute how much water that each cell can contain, we have to find the minimum
of the two maximum heights found to the cell's left and right.

Hence, in naive implementation, the time complexity would be O(n^2) due to
having to iterate the array every time we need to find the maximum heights to
each cell's left and right. We can further make an improvement by using hashmap
or array to record the left and right maximum heights for each position - in
this case, we can reduce the time complexity to O(n).

The best approach here would be using two pointer method by realizing that
by starting from either end of the array, the amount of water stored can only
change by moving the smaller of the two heights as indicated by the two
pointers. Hence, O(1) space is enough to keep track of the two current left and
right heights. To do so, we maintain the two variables to track maximum left
and right heights we have seen thus far - and move whichever pointer that is
smaller.

---

Python:

```python

class Solution42:

    def trap(self, height):

        l, r = 0, len(height) - 1
        lmax, rmax, total = 0, 0, 0

        while l < r:
            if height[l] < height[r]:
                lmax = max(height[l], lmax)
                total += lmax - height[l]
                l += 1
            else:
                rmax = max(height[r], rmax)
                total += rmax - height[r]
                r -= 1

        return total
```
