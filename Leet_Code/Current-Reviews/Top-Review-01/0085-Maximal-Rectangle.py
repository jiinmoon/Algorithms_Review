# 85 Maximal Rectangle
#
# To find the maximum area of rectangle that can be formed, we treat this as
# a collection of histograms from top to bottom - hist is updated so long as
# the elements does not break down. Then, the cumulative height (bars) can be
# examined at each row to produce the maximum area of ths cumulative histogram
# thus far.

class Solution:
    def maxRectangle(self, grid):
        if not grid or not grid[0]:
            return 0

        maxArea = 0
        m, n = len(grid), len(grid[0])
        hist = [0] * n

        for i in range(m):
            for j in range(n):
                hist[j] = hist[j] + 1 if grid[i][j] == '1' else 0
            maxArea = max(maxArea, self.maxHistogram(hist))

        return maxArea

    def maxHistogram(self, hist):
        maxArea = 0
        stk = [0]
        hist = [0] + hist + [0]
        for i, num in enumerate(hist[1:], 1):
            while stk and hist[stk[-1]] > num:
                h = hist[stk.pop()]
                w = i - stk[-1] - 1
                maxArea = max(maxArea, h * w)
            stk.append(i)
        return maxArea


