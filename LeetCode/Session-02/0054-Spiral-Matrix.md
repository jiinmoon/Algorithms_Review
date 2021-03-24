# 54. Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.

---

There are several approaches to this problem, but one approach could be to
generate the (i, j) coordinates in spiral fashion from outer layer to the inner
layer.

---

Python:

```python

class Solution54:

    def sprialMatrix(self, matrix):

        def sprialCoords(r1, r2, c1, c2):

            for col in range(c1, c2 + 1):
                yield r1, col
            for row in range(r1 + 1, r2 + 1):
                yield row, c1
            if r1 < r2 and c1 < c2:
                for col in range(c2 - 1, c1, -1):
                    yield r2, col
                for row in range(r2, r1, -1):
                    yield row, c1

        if not (matrix and matrix[0]):
            return []

        result = []
        r1, r2 = 0, len(matrix) - 1
        c1, c2 = 0, len(matrix[0]) - 1

        while r1 <= r2 and c1 <= c2:
            for row, col in spiralCoords(r1, r2, c1, c2):
                result.append(matrix[row][col])
            r1 += 1; c1 += 1
            r2 -= 1; c2 -= 1

        return result
```
