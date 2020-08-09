240 Search a 2D Matrix II
=========================

Write an efficient algorithm that searches for a value in an m x n matrix. This
matrix has the following properties:

- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.


Example:

```
Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

Given target = 5, return true.

Given target = 20, return false.
```
---

The particular properties of this matrix allows us to efficiently search if we
adjust our starting position first. If we start from the top-right corner, then
we can check whether the current value against the given target. If it is less
than, we can safely move inwards into the same row. If it is greater, than the
num has to be in another row. This would take O(m + n) time complexity to
complete.

---

Go:

```go
func searchMatrix(mat [][]int, target int) bool {
    if len(mat) == 0 {
        return false
    }
    var (
        m = len(mat)
        n = len(mat[0])
        r = 0
        c = n - 1
    )
    for r < m && c >= 0 {
        if matrix[r][c] == target {
            return true
        }

        if matrix[r][c] < target {
            c -= 1
        } else {
            r += 1
        }
    }
    return false
}
```
