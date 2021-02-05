# 59. Spiral Matrix II

Given a positive integer n, generate an n x n matrix filled with elements from
1 to n2 in spiral order.

---

Maintain a start and a end points for rows and cols. Starting from outer layer,
we traverse in spiral order, while decreasing our rows and cols to cover. This
is O(n^2) in time complexity.

---

Python:

```python

class Solution:
    def spiralMatrix(self, n):
        def sprialOrder(r1, r2, c1, c2):
            for col in range(c1, c2+1):
                yield r1, col
            for row in range(r1+1, r2+1):
                yield row, c2
            if r1 < r2 and c1 < c2:
                for col in range(c2-1, c1, -1):
                    yield r2, col
                for row in range(r2, r1, -1):
                    yield row, c1

        result = [[0] * n for _ in range(n)]

        r1, r2, c1, c2, i = 0, n-1, 0, n-1, 0
        while r1 <= r2 and c1 <= c2:
            for r, c in spiralOrder(r1, r2, c1, c2):
                result[r][c] = i
                i += 1
            r1 += 1; c1 += 1
            r2 -= 1; c2 -= 1

        return result
```
