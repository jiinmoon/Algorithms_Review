# LeetCode Daily Challenge: August Week.2 - Day.2

## Question

In a given grid, each cell can have one of three values:

    the value 0 representing an empty cell;
    the value 1 representing a fresh orange;
    the value 2 representing a rotten orange.

Every minute, any fresh orange that is adjacent (4-directionally) to a rotten
orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh
orange.  If this is impossible, return -1 instead.

## Solution

Use BFS to start from fresh cells; while we have fresh oranges, we check its
neighbours and add them to the rotten set. If we do not discover new rotten
oranges, then we cannot complete the task. If we do discover, then remove newly
discovered rotten oranges from the fresh list and start over.

Python:

```python
class Solution:
    def orangesRotting(self, grid):
        m, n = len(grid), len(grid[0])
        fSet, rSet = set(), set()
        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fSet.add( (i, j) )
                if grid[i][j] == 2:
                    rSet.add( (i, j) )

        while fSet:
            nextRotten = set()
            for i, j in rSet:
                for nextX, nextY in [ (i+1, j), (i-1, j), (i, j+1), (i, j-1) ]:
                    if (nextX, nextY) in fSet:
                        nextRotten.add( (nextX, nextY) )

            if not nextRotten:
                return -1

            fSet -= nextRotten
            rSet = nextRotten
            res += 1

        return res
```

