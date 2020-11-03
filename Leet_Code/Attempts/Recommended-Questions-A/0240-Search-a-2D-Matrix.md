# 240. Search a 2D Matrix

Write an efficient algorithm that searches for a value in an m x n matrix. This
matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

---

The particular board has features that we can use to our advantage - in
particular, once we start our search from the top right most corner, we can
check against the current value against the target value. If it is less than
the target value, then it must lie somewhere within the current row so we can
move our column inwards. If it is greater, then it must lie some other row
hence we can increase our row to search. The search algorithm can complete in
O(m * n) time complexity.

---

Python:

```python

class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        r, c = 0, n - 1
        while r < m and c >= 0:
            if matrix[r][c] == target:
                return True
            if matrix[r][c] < target:
                c -= 1
            else:
                r += 1
        return False
```
