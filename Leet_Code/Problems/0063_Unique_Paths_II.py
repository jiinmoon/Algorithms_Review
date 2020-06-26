""" 63. Unique Paths II

Question:

    Same as 62, but now there exists obstacles which prevents robot from
    traversing.

+++

Solution:

    Same DP approach can work here - but we need to carefully set up the intial
    conditions. For first row and cols, they should have a single path unless
    blocked by a obstacle. This also applies when we are computing DP as well,
    the DP value only gets updated if it is not the obstacle value.

"""

class Solution:
    def uniquePathsWithObstacles(self, obsGrid):
        if not obsGrid:
            return 0
        m, n = len(obsGrid), len(obsGrid[0])
        DP = [[0] * n for _ in range(m)]

        i = 0
        while i < n and obsGrid[0][i] != '1':
            obsGrid[0][i] = 1
            i += 1

        i = 0
        while i < m and obsGrid[i][0] != '1':
            obsGrid[i][0] = 1
            i += 1

        for i in range(1, m):
            for j in range(1, n):
                if obsGrid[i][j] != 1:
                    DP[i][j] = DP[i-1][j] + DP[i][j-1]
        return DP[-1][-1]
