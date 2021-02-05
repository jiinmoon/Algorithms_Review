# 1277. Count Square Submatrices with All Ones

Given a m * n matrix of ones and zeros, return how many square submatrices have
all ones.

---

We may apply dynamic programming to solve this problem. We can breakdown this
problem as a determining number of squares that ends at (i,j) by examining
three other positions which are (i-1,j), (i,j-1), and (i-1,j-1). The number of
squares for each cell can be updated as a minimum of three cells so long as the
current is 1. We also need to factor in that 1s are square in itself.

The time complexity should be O(m * n) to traverse on every cell and O(1) in
space as we can perform this in place.

---

Python:

```python

class Solution:
    def countSquares(self, matrix):
        if not matrix or not matrix[0]:
            return -1

        m, n, result = len(matrix), len(matrix[0]), 0

        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0:
                    # current cell can be 0
                    # use *
                    matrix[i][j] *= 1 + min(
                        matrix[i-1][j],
                        matrix[i][j-1],
                        matrix[i-1][j-1])
                result += matrix[i][j]

        return result
```
