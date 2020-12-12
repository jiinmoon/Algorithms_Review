# Set Matrix Zeroes

Given a matrix, A of size M x N of 0s and 1s. If an element is 0, set its
entire row and column to 0.

Note: This will be evaluated on the extra memory used. Try to minimize the
space and time complexity.

---

We appear to require additional O(m + n) memory to store which rows and cols to
set zero, but we can do this in-place by first record the information about the
first row and col; and use first row and col as a marker to set entire row and
col to zero.

---

Python:

```python

class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):

        m, n = len(A), len(A[0])
        setFirstRow = 0 in A[0]
        setFirstCol = 0 in [(A[i][0]) for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                if not A[i][j]:
                    A[i][0] = 0
                    A[0][j] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                if not A[i][0] or not A[0][j]:
                    A[i][j] = 0
        
        if setFirstRow:
            for i in range(n):
                A[0][i] = 0
        
        if setFirstCol:
            for i in range(m):
                A[i][0] = 0
        
        return A

```
