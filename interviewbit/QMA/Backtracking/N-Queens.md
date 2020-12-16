# N-Queens

The n-queens puzzle is the problem of placing n queens on an n×n chessboard
such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens’
placement, where 'Q' and '.' both indicate a queen and an empty space
respectively.

---

Backtrack to explore the board state row after another. We keep track of the
threatend columns, updiagonal and downdiagonal lines to avoid placing them down
the path.

O(n!) in time complexity as we have n! choices to place our first queen, then
next row, we have n * (n-2)! choices and so on.

---

Python:

```python

class Solution:

    def solveNQueens(self, A):

        def helper(row, path):
            
            if row == A:
                result.append(["".join(r) for r in path])
            else:
                for col in range(A):
                    if col in cols or col+row in upDiag or col-row in downDiag:
                        continue
                    path[row][col] = "Q"
                    cols.add(col)
                    upDiag.add(col+row)
                    downDiag.add(col-row)
                    helper(row + 1, path)
                    downDiag.remove(col-row)
                    upDiag.remove(col+row)
                    cols.remove(col)

        path = [["."] * A for _ in range(A)]
        cols, upDiag, downDiag = set(), set(), set()
        result = []
        helper(0, path)

        return result
```
