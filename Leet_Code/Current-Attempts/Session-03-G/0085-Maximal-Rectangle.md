# 85 Maximal Rectangle

We can view the rectangle in the given grid in row by row cumulative histogram.
Hence, we find the max area under the histogram on each row and maintain the
max area among all rows.

---

```python

class Solution:
    def maxHist(self, hist):
        hist = [0] + hist + [0]
        stk = [0]
        maxA = 0
        for i, num in enumerate(hist[1:], 1):
            while stk and hist[stk[-1]] > num:
                h = hist[stk.pop()]
                w = i - stk[-1] + 1
                maxA = max(maxA, h * w)
            stk.append(i)

        return maxA

    def maxRect(self, grid):
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        hist = [0] * n
        maxA = 0

        for i in range(m):
            for j in range(n):
                hist[j] = hist[j] + 1 if grid[i][j] == '1' else 0
            maxA = max(maxA, self.maxHist(hist))

        return maxA
```
