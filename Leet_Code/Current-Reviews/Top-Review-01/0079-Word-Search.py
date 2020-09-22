# 79 Word Search
#
# For each cell where it is same as the starting char of the target word, we
# perform backtracking so long as the next cell matches the word.

class Solution:
    def wordSearch(self, grid, word):
        def helper(i, j, k):
            if k == len(word):
                return True
            if not (0 <= i < m or 0 <= j < n) and not (grid[i][j] == word[k]):
                return False
            temp = grid[i][j]
            helper(i+1, j, k+1)
            helper(i-1, j, k+1)
            helper(i, j+1, k+1)
            helper(i, j-1, k+1)
            grid[i][j] = temp

        if not grid or not grid[0] or not word:
            return False

        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == word[0] and helper(i, j, 0):
                    return True

        return False
