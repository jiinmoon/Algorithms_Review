# 85 Maximal Rectangle

class Solution:
    def maxRect(self, grid):
        def helper(hist):
            hist = [0] + hist + [0]
            stk = [0]
            res = 0
            for i, bar in enumerate(hist[1:], 1):
                while stk and hist[stk[-1]] > bar:
                    h = hist[stk.pop()]
                    w = i - stk[-1] + 1
                    res = max(res, h * w)
                stk.append(i)
            return res

        if not grid or not grid[0]:
            return 0

        m, n, maxA = len(grid), len(grid[0]), 0
        hist = [0] * n

        for i in range(m):
            for j in range(n):
                hist[j] = hist[j] + 1 if grid[i][j] == '1' else 0
            maxA = max(maxA, helper(hist))

        return maxA
