# 85. Maximal Rectangle

Given a rows x cols binary matrix filled with 0's and 1's, find the largest
rectangle containing only 1's and return its area.

---

The problem can be visualized as a cumulative histograms - and finding the
largest area that can be generated from each of the histrograms generated as we
examine the matrix row after another.

---

Python:

```python

class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        m, n, result = len(matrix), len(matrix[0]), 0
        hist = [0] * n

        for i in range(m):
            for j in range(n):
                hist[j] = hist[j] + 1 if matrix[i][j] == '1' else 0
            result = max(result, self.maximalHist(hist))

        return result

    def maximalHist(self, hist):
        hist = [0] + hist + [0]
        stk = [0]
        result = 0
        for i, bar in enumerate(hist[1:], 1):
            while stk and hist[stk[-1]] > bar:
                h = hist[stk.pop()]
                w = i - stk[-1] - 1
                result = max(result, h * w)
            stk.append(i)
        return result
```
