# 73. Set Matrix Zeroes

Given an m x n matrix. If an element is 0, set its entire row and column to 0.
Do it in-place.

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.

A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

---

The naive approach becomes a problem where we simply set the rows and cols to
zero whenever we encounter zero - this will quickly result in error where all
the rows and cols will be set to zero. This is due to next informations are
being overwritten. Hence, we realize that we need to record the rows and cols
to zero out after a single iteration. We do not require to store this
information in 2D grid - as we can save the corrdinates instead for O(m + n)
space complexity.

We can further improve the space complenxity by marking the row and col to zero
out in the first col and first row. To do so, we need two additional boolean
flag to denote whether first row and col is to be set to zero in the end.

---

Python:

```python

class Solution73:

    def setMatrixZeroes(self, matrix):

        m, n = len(matrix), len(matrix[0])

        zeroFirstRow = 0 in matrix[0]
        zeroFirstCol = 0 in [matrix[i] for i in range(m)]
        
        # find row and col to zero
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        # set row and col to zero based on first row/col
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = = 0

        # set first row and col to zero
        if zeroFirstRow:
            for c in range(n):
                matrix[0][c] = 0

        if zeroFirstCol:
            for r in range(m):
                matrix[r][0] = 0
```
