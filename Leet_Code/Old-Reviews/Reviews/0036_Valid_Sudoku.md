36 Valid Sudoku
===============

Question:
---------

Determine whether the given 9 x 9 Sudoku board is valid.

Solutions:
----------

The keyword here is "valid" - we do not have to solve the Sudoku board in order
to determine that it is a valid board.

Codes:
------

Python:

```python
class Solution:
    def isValidSudoku(self, board):
        rows = [ set() for _ in range(9) ]
        cols = [ set() for _ in range(9) ]
        boxes = [ set() for _ in range(9) ]

        for i in range(9):
            for j in range(9):
                if board[i][j] != ' ':
                    curr = board[i][j]
                    box = (i // 3) * 3 + (j // 3)
                    if curr in cols[j] or curr in rows[i] or \
                        curr in boxes[box]:
                        return False
                    cols[j].add(curr)
                    rows[i].add(curr)
                    boxes[box].add(curr)
        return True
```

---

**Source:**

LeetCode: [Valid-Sudoku](https://leetcode.com/problems/valid-sudoku/)
