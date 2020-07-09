""" 64. Minimum Path Sum

Question:

    Given a m x n grid filled with non-negative numbers, find a path from top
    left to bottom right which minimizes the sum of all numbers along its path.

+++

Solution:

    One possible approach is to treat this problem as a graph problem - finding
    the minimum spanning tree.

    Another solution is utilizing DP; we define each DP[i][j] as the minimum
    path sum thus far, which depends on the minimum of DP[i-1][j] and
    DP[i][j-1].

"""

class Solution:
    def min_path_sum(self, grid):
        m, n = len(grid), len(grid[0])
        prev_row = [ float('inf') for _ in range(n+1) ]
        prev_row[1] = 0

        for row in range(1, m+1):
            new_row = [ float('inf') for _ in range(n+1) ]
            for col in range(1, n+1):
                new_row[col] = grid[row-1][col-1] + min(prev_row[col],
                        new_row[col-1])
            prev_row = new_row
        return prev_row[-1]
