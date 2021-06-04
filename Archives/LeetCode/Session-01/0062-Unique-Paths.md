# 62. Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in
the diagram below).

The robot can only move either down or right at any point in time. The robot is
trying to reach the bottom-right corner of the grid (marked 'Finish' in the
diagram below).

How many possible unique paths are there?

---

One way to find the number of unique paths is to use the dynamic programming
method where we will compute the number of unique path at current position
based on previous row and col information. In other words, for every position
`(i, j)` we can compute the maximum number of unique paths to that position by
adding up number of ways to reach the previous positions from its left and up
(as we can only move down or right at any point in time).

Here, we do not need 2D grid to save entire information about the number of
paths as all we need is the previous row information. Hence, we can reduce the
size from O(m * n) to O(n) instead. The time complexity would be linear O(m * n).

---

Python:

```python

class Solution62:

    def uniquePaths(self, m, n):

        prevRow = [1] * n

        for r in range(m - 1):
            currRow = [1]
            for c in range(1, n):
                currRow.append(prevRow[c] + currRow[-1])
            prevRow = currRow

        return prevRow[-1]
```

