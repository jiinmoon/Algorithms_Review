# 54 Spiral Matrix

Given a matrix of m x n elements (m rows, n columns), return all elements of
the matrix in spiral order.

---

To traverse the matrix in spiral order, we consider moving from outer layer to
the inner layer in sprial order via maintaining the current start and ending
rows and cols. Starting from top row, we move to left. Then move downward from
leftmost col. From rightmost corner, we move to right on bottom most row. And
we move upward from leftmost corner.

---

Python:

```python

class Solution:
    def spiralMatrix(self, matrix):
        def spiralcoords(sr, er, sc, ec):
            # Top row; move left
            for col in range(sc, ec + 1):
                yield sr, col
            # Left col; move downward
            for row in range(sr + 1, er + 1):
                yield row, ec
            # if sr > er or sc > ec, it indicates end of spiral ordering
            if sr < er and sc < ec:
                # Bottom row; move right
                for col in range(ec - 1, sc, -1):
                    yield er, col
                # Right col; move upward
                for row in range(er, sr, -1):
                    yield row, sc

        if not matrix or not matrix[0]:
            return []

        result = []
        m, n = len(matrix), len(matrix[0])
        sr, er, sc, ec = 0, m - 1, 0, n - 1

        while sr <= er and sc <= ec:
            for row, col in sprialcoords(sr, er, sc, ec):
                result.append(matrix[row][col])
            sr += 1; sc += 1;
            er -= 1; ec -= 1;

        return result
```
