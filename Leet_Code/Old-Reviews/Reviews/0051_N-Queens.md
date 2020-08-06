51 N-Queens
===========

Question:
---------

Given integer n, find all possible board states that solves N-Queens problem.

Solutions:
----------

A backtracking algorithm is used here to explore all possible positions where
a queen can be placed. Because we are going to build the board row after row,
we only have to manage locations of columns where queen has been placed
previously, and also the cells diagonal to the queens.

Codes:
------

Python:

```python
class Solution:
    def solveNQueens(self, n):
        result = []
        path = [ [''] * n for _ in range(n)]
        cols, upDiag, downDiag = set(), set(), set()

        def backtrack(path, row):
            if row == n:
                result.append([''.join(row) for row in path])
                return
            for col in range(n):
                if (col not in cols) and (row-col not in upDiag) and \
                    (row+col not in downDiag):
                    path[row][col] = 'Q'
                    cols.add(col)
                    upDiag.add(row-col)
                    downDiag.add(row+col)
                    backtrack(path, row+1)
                    downDiag.remove(row+col)
                    upDiag.remove(row-col)
                    cols.remove(col)

        backtrack(path, 0)
        return result 
```

---

**Source:**

LeetCode: [N-Queens](https://leetcode.com/problems/n-queens)
