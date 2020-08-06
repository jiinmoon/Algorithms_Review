73 Set Matrix Zeroes
====================

Question:
---------

Given a m x n matrix, if an element is 0, set its entire row and col to 0.

Solutions:
----------

We cannot simply iterate and replace - as this will crate problems for future
operations and eventually zero out everything.

On first iteration, we need to record which row and col can be set to zero. And
then actually perform the zeroing operations. While we can use extra structure
to denote the marked rows and cols, we can store them in-place on first row/col
given that we records whether first row or col should be zero'd later.

Codes:
------

Python:

```python
class Solution:
    def setZeroes(self, matrix):
        m = len(matrix)
        if not m:
            return
        n = len(matrix[0])
        
        zeroFirstRow = 0 in matrix[0]
        zeroFirstCol = 0 in [matrix[i][0] for i in range(m)]

        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        if zeroFirstRow:
            for i in range(n):
                matrix[0][i] = 0
        if zeroFirstCol:
            for i in range(m):
                matrix[i][0] = 0
```

---

**Source:**

LeetCode: [Set-Matrix-Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)
