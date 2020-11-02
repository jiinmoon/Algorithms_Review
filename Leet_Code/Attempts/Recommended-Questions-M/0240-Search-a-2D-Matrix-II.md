# 240. Search a 2D Matrix II

Write an efficient algorithm that searches for a value in an m x n matrix. This
matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

---

The particular ordering of the matrix allows for linear time search in O(m * n)
if we start our search from the top right corner. From here, we can manipulate
the row and col such that if the target value is less than current, the we can
move the col inwards; otherwise, the target value must lie in other row.

---

Python:

```python

class Solution:
    def search(self, grid, target):
        if not grid or not grid[0]:
            return False

        m, n = len(grid), len(grid[0])
        r, c = 0, n - 1
        while r < m and c >= 0:
            if grid[r][c] == target:
                return True
            if grid[r][c] < target:
                c -= 1
            else:
                r += 1
        return False
```
