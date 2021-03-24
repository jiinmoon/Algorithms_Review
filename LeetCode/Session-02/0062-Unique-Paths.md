# 62. Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in
the diagram below).

The robot can only move either down or right at any point in time. The robot is
trying to reach the bottom-right corner of the grid (marked 'Finish' in the
diagram below).

How many possible unique paths are there?

---

We can approach this problem in multiple different ways.

First approach would be to think of the problem as a combination problem where
for each grid from top-left to bottom-right, we have a choice to make - either
we move to right or downward. Hence, this can be solved using the combinatory
algorithm.

Another approach would be dynammic programming solution where at each cell, we
try to compute the number of unique paths to reach that particular cell. As the
robot can only make two possible movement at each cell, the new unique path
value at each cell is simply the sum of two previous positions where the robot
was.

The DP solution would require O(m * n) in time complexity and space complexity
if implemented naively. We can reduce the space complexity by realizing that we
only need the information from the previous row; hence, the space can be
further reduced by O(n).

---

Python:

```python

class Solution62:

    def uniquePaths(self, m, n):

        prevRow = [1] * n

        for _ in range(1, m):
            nextRow = [1]
            for col in range(1, n):
                nextRow.append(nextRow[-1] + prevRow[col])
            prevRow = nextRow
        
        return prevRow[-1]
```
