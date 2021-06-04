# 73. Set Matrix Zeroes

Given an m x n matrix. If an element is 0, set its entire row and column to 0.
Do it in-place.

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

---

Naive approach to this problem where we set the row and col to zero as we
encounter them quickly becomes a problem as we overwrite the furture
information and will eventually fill all the rows and cols with zeroes.

Hence, we realize that we need to record the rows and cols that whic should be
set to zero. First naive implementation of such idea would be to use O(m * n)
space where we have a duplicate m x n matrix where we would denote the rows and
cols to be zeroed out. A slight improvement in terms of space complexity can be
made with a single array where we can just simply add the coordinates of zeros
found - which reduces the space complexity to O(m + n).

But we can perform this in-place by using the first row and col as flag to
whether we should zero the rows and cols - to do so, we should first record
whether we should zero the "first" row and col.

---

Python:

```python

class Solution73:

    def setMatrixZeroes(self, matrix):

        if not (matrix and matrix[0]):
            return None

        m, n = len(matrix), len(matrix[0])

        zeroFirstRow = 0 in matrix[0]
        zeroFirstCol = 0 in [matrix[row][0] for row in range(m)]

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][col] == 0 or matrix[row][col] == 0:
                    matrix[row][col] = 0

        if zeroFirstRow:
            for col in range(n):
                matrix[0][col] = 0

        if zeroFirstCol:
            for row in range(m):
                matrix[row][0] = 0
```
