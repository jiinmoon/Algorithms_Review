# 733 Flood Fill

An image is represented by a 2-D array of integers, each integer representing
the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of
the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels
connected 4-directionally to the starting pixel of the same color as the
starting pixel, plus any pixels connected 4-directionally to those pixels (also
with the same color as the starting pixel), and so on. Replace the color of all
of the aforementioned pixels with the newColor.

At the end, return the modified image.

---

This is a simple traversal on the given grid - starting from each cell that has
the non-newColor, we search out as far as possible and mark it with the new
color.

---

Python:

```python

class Solution:
    def floodFill(self, grid, sr, sc, newColor):
        def helper(r, c):
            if 0 <= r < m and 0 <= c < n and grid[r][c] != startColor:
                return
            grid[r][c] = newColor
            for nr, nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                helper(nr, nc)

        if not grid or not grid[0]] or grid[sr][sc] == newColor:
            return grid

        m, n = len(grid), len(grid[0])
        startColor = grid[sr][sc]
        helper(sr, sc)

        return grid
```
