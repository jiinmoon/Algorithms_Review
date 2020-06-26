""" 62. Unique Paths

Questions:

    A robot is located at the top-left corner of a m x n grid. This robot may
    only move right or down - and it is trying to reach the bottom-right corner
    of the grid. How many unique paths that the robot can take to reach the
    goal?

+++

Solution:

    We can view this problem as a pure combinatory problem - at each cell, we
    are given possible two choices, and there are m + n cells to traverse. Thus
    this would be (m + n) choose 2 combination problem.

    Alternatively, we can use the DP solution here. At any cell (DP[i][j]), the
    total paths that took to reach that cell would depend on both the total cell
    from previous cells which if from its left and up.

"""

class Solution:
    def uniquePaths(self, m, n):
        DP = [[1] * n for _ in range(m)]
        # first row and first col must be all 1s since it only takes single path
        # to reach them.
        for i in range(1, m):
            for j in range(1, n):
                DP[i][j] = DP[i-1][j] + DP[i][j-1]
        return DP[-1][-1]
