# 54. Sprial Matrix

Given a matrix of m x n elements (m rows, n columns), return all elements of
the matrix in spiral order.

---

In order to return the elements from the given matrix in sprial order, we
visualize it by peeling the onion. We start from the outer-layer, and move onto
the inner-layer one at a time.

---

Python:

```python

class Solution:
    def sprialMatrix(self, matrix):
        def sprialCoords(r1, r2, c1, c2):
            # top row (left to right)
            for col in range(c1, c2 + 1):
                yield r1, col
            # right col (top to bottom)
            for row in range(r1 + 1, r2 + 1):
                yield row, c2
            if r1 < r2 and c1 < c2:
                # bottom row (right to left)
                for col in range(c2 - 1, c1 - 1, -1):
                    yield r2, col
                # left col (bottom to top)
                for row in range(r2, r1, -1):
                    yield row, c1

        if not matrix or not matrix[0]:
            return []

        result = list()
        r1, r2 = 0, len(matrix) - 1
        c1, c2 = 0, len(matrix[0]) - 1
        while r1 <= r2 and c1 <= c2:
            for r, c in sprialCoords(r1, r2, c1, c2):
                result.append(matrix[r][c])
            r1 += 1; c1 += 1
            r2 -= 1; c2 -= 1

        return result
```
