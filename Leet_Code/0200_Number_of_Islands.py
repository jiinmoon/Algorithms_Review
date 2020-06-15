""" 200. Number of Islands

Question:

    Given a 2D grid of '1's and '0s', count the number of islands - '1's
    surrounded by '0's.

+++

Solution:

    Simply, as we iterate on the 2D grid, whenever we encounter '1', we start
    backtracking algorithm to mark all '1's within the same island.

"""

class Solution:
    def numIslands(self, grid):
        m, n = len(grid), len(grid[0])

        def isValidLand(x, y):
            return x >= 0 and x < m and y >= 0 and y < n and grid[x][y] == '1'

        def markLands(x, y):
            stack = [ (x, y) ]
            while stack:
                x, y = stack.pop()
                grid[x][y] = '-1'
                for nextX, nextY in [ (x+1, y), (x-1, y), (x, y+1), (x, y-1) ]:
                    if isLand(nextX, nextY):
                        stack.append( (nextX, nextY) )

        totalIsl = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == '1':
                    totalIsl += 1
                    markLands(x, y)

        return totalIsl
