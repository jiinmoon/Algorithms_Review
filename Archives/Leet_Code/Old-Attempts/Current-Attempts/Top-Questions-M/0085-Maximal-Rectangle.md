# 85 Maximal Rectangle

Given a rows x cols binary matrix filled with 0's and 1's, find the largest
rectangle containing only 1's and return its area.

---

The maximal rectangle in a given grid can be thought of as a cumulative,
unbroken sum of 1s row after row - that is thinking of it as a finding the
maximum of the cumulative area under the histogram.

To find maximal area under the histogram, we use stack to maintain each index
of the height. At each index, we look behind in the stack as far out as
possible until the current height is less than what is on top of the stack.
Last element pop'd from the stack will indicate the height of the maximal area
of the histogram and difference of the current index to last element's index
would be the width.

---

Python:

```python

class Solution:
    def maximalRectangle(self, grid):
        if not grid or not grid[0]:
            return 0

        m, n, total = len(grid), len(grid[0]), 0
        hist = [0] * n

        for i in range(m):
            for j in range(n):
                hist[j] = hist[j] + 1 if hist[j] else 0
            total = max(total, self.maximalHist(hist)

        return total

    def maximalHist(self, hist):
        hist = [0] + hist + [0]
        stk = [0]
        total = 0

        for i, num in enumerate(hist[1:], 1):
            while stk and hist[stk[-1]] > num:
                h = hist[stk.pop()]
                w = i - stk[-1] - 1
                total = max(total, h * w)
            stk.append(i)

        return total
```
