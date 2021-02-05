# Spiral Order Matrix II

Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order.

---

Python:

```python

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        
        def spiral_coords(r1, r2, c1, c2):
            for col in range(c1, c2 + 1):
                yield r1, col
            for row in range(r1 + 1, r2 + 1):
                yield row, c2
            if r1 < r2 and c1 < c2:
                for col in range(c2 - 1, c1, -1):
                    yield r2, col
                for row in range(r2, r1, -1):
                    yield row, c1
                    
        r1, r2, c1, c2 = 0, A - 1, 0, A - 1
        i, result = 1, [[0] * A for _ in range(A)]
        
        while r1 <= r2 and c1 <= c2:
            for r, c in spiral_coords(r1, r2, c1, c2):
                result[r][c] = i
                i += 1
            r1 += 1; c1 += 1;
            r2 -= 1; c2 -= 1;
        
        return result

```
