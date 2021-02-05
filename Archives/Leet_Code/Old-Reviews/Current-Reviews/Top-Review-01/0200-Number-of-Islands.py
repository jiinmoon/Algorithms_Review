# 200 Number of Islands
#
# Simply perform backtracking algorithm span from each of the cells which are
# marked as land. From each position, we expand as far out as possible so long
# as it is land and mark them as such. The time complexity is O(m + n).

class Solution:
    def numberOfIslands(self, grid):
        def explore(i, j):
            grid[i][j] = 0
            for ni, nj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0 <= ni < m and 0 <= nj < n and grid[i][j]:
                    explore(ni, nj)

        if not grid or not grid[0]:
            return 0

        total = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    total += 1
                    explore(i, j)

        return total

