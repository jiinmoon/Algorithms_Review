# 311. Sparse Matrix Multiplication

Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

---

This would be of a typical matrix multiplication algorithm that would be O(m
* n * o) in time complexity where m and n are the dimensions of A and o is the
  length of columns from B.

But since the matrix is "sparse", we may save some time by skipping over the
multiplication process if one is found to be 0.

```
A = [[1,2,3], [4,5,6]] has dimension of 2 x 3
B = [[7,8], [9,10], [11,12]] has dimension of 3 x 2

Resulting matrix should then be 2 x 2.

Result = [
    [(1*7 + 2*9 + 3*10), ....]
    ...
]

Hence, we iterate on each of the elements on A. For every value that we find
that is not zero, we iterate on the B and find corresponding to add to result.
```

---

Python:

```python

class Solution:
    def matrixMultiplication(self, A, B):
        # dimensions are guranteed to be match
        m, n, o = len(A), len(A[0]), len(B[0])
        # final dimension is len(A) by len(B[0])
        result = [[0] * o for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if A[i][j]:
                    for k in range(o):
                        if B[j][k]:
                            result[i][k] += A[i][j] * B[j][k]
        return result
```
