# 1463. Cherry Pickup II

Given a rows x cols matrix grid representing a field of cherries. Each cell in
grid represents the number of cherries that you can collect.

You have two robots that can collect cherries for you, Robot #1 is located at
the top-left corner (0,0) , and Robot #2 is located at the top-right corner (0,
cols-1) of the grid.

Return the maximum number of cherries collection using both robots  by
following the rules below:

From a cell (i,j), robots can move to cell (i+1, j-1) , (i+1, j) or (i+1, j+1).
When any robot is passing through a cell, It picks it up all cherries, and the
cell becomes an empty cell (0).
When both robots stay on the same cell, only one of them takes the cherries.
Both robots cannot move outside of the grid at any moment.
Both robots should reach the bottom row in the grid.

---

The problem is best approached using the dynammic programming. At each cell
that we arrive at, we try to compute the maximum amount of cherry that can be
picked by both of the robots as they move. Suppose column position j is where
robot 1 is and column position k is where robot 2 would be. Then, the current
position dp[j][k] represents the maximum amonut of cherry obtainable after
computing this row for col j, k chosen.

Starting from bottom, we try to move two robots into their next respective
positions. As we are doing so, we check against our previous dp array for
previously seen maximum amount of cherry that can be picked by moving onto new
position. Once all the positions are considered, then current dp position is
updated to the maximum from previous dp as well as sum of cherrys picked up by
moving robot1 and robot2 into (i,j) and (i,k).

This process would take O(m * n^2) in time complexity as for each row m, we
have to iterate to consider every column positions for "two" of the robots that
can move.

---

Python:

```python

class Solution:
    def cherryPickup(self, grid):
        if not grid or not grid[0]:
            return -1

        m, n = len(grid), len(grid[0])
        # dp[j][k] represents for each row i in grid,
        # maximum number of cherry picked up by robot1 moving to column j
        # and robot 2 moving to column k
        dp = [[0] * n for _ in range(n)]

        # initialize dp; we are moving bottom up
        for i in range(n-1):
            for j in range(i+1, n):
                dp[i][j] = grid[-1][i] + grid[-1][j]

        # for each row, compute all possible robot movements
        for i in range(m-2, -1, -1):
            # dp is to be updated; save previous dp for reference
            prev = [row[:] for row in dp]
            for j in range(n-1):
                for k in range(j+1, n):
                    maxThusFar = 0
                    # move robots to their positions
                    for nj, nk in [(j+x,k+y) for x in (-1,0,1) for y in (-1,0,1)]:
                        # robot1 should not move over robot2 column and they cannot overlap
                        if 0 <= nj <= k and j < nk < n and nj != nk:
                            maxThusFar = max(maxThusFar, prev[nj][nk])
                    # update current dp as maximum amount obtained
                    # if robots were to move onto current rows col j and k
                    dp[j][k] = maxThusFar + grid[i][j] + grid[i][k]

        return dp[0][-1]
```
