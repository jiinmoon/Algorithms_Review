""" 64. Minimum Path Sum

Question:

    Given a m x n grid filled with non-negative numbers, find a path from top
    left to bottom right which minimizes the sum of all numbers along its path.

+++

Solution:

    We can treat this problem as a graph problem - then apply the minimum
    spanning tree algorithm. However, DP appraoch is simpler and just as
    efficient in time complexity, if not faster.

    Again, we need to carefully think about the initial set up of our DP. Our
    DP[i][j] will be defined as minimum path cost to reach that coords. The
    first row and col will have a single path - thus, their values will be
    cumulative sum.

"""

class Solution:
    def minPathSum(self, grid):
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        DP = [[0] * n for _ in range(m)]
        DP[0][0] = grid[0][0]

        for i in range(1, n):
            DP[0][i] = DP[0][i-1] + grid[0][i]

        for i in range(1, m):
            DP[i][0] = DP[i-1][0] + grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                DP[i][j] = min(DP[i-1][j], DP[i][j-1]) + grid[i][j]

        return DP[-1][-1]
