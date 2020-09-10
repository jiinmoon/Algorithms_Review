54 Spiral Matrix
================

Given a matrix of m x n elements, return all elements of the matrix in spiral
order.

---

Python:

```python
class Solution:
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]: return []
        
        r1, r2 = 0, len(matrix)-1
        c1, c2 = 0, len(matrix[0])-1

        def spiralCoords(r1, r2, c1, c2):
            # top row (left to right)
            for col in range(c1, c2+1):
                yield r1, col
            # right col (top to bottom)
            for row in range(r1+1, r2+1):
                yield row, c2
            # more layer
            if r1 < r2 and c1 < c2:
                # bottom row (right to left)
                for col in range(c2-1, c1, -1):
                    yield r2, col
                # left col (bottom to top)
                for row in range(r2, r1, -1):
                    yield row, c1

        res = list()

        while r1 <= r2 and c1 <= c2:
            for row, col in spiralCoords(r1, r2, c1, c2):
                res.append(matrix[row][col])
            r1 += 1; r2 -= 1
            c1 += 1; c2 -= 1
            
        return res
```
