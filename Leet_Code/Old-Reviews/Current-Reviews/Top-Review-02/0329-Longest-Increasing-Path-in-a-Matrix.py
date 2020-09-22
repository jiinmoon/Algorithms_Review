# 329 Longest Increasing Path in a Matrix

from functools import lru_cache

class Solution:
    def longestIncreasingPath(self, matrix):
        @lru_cache(None)
        def helper(i, j):
            length = 1
            for ni, nj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0 <= ni < m and 0 <= nj < n and matrix[i][j] < matrix[ni][nj]:
                    length = max(length, 1 + helper(ni, nj))
            return length

        if not matrix or not matrix[0]:
            return 0

        m, n, longest = len(matrix), len(matrix[0]), 0
        for i in range(m):
            for j in range(n):
                longest = max(longest, helper(i, j))

        return longest
