# 26. Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9
without repetition.

Note:

A Sudoku board (partially filled) could be valid but is not necessarily
solvable.
Only the filled cells need to be validated according to the mentioned rules.

---

It is important to note that we are not asked to solve the partially solved
Sudoku board in order to validate it. In fact, this is far simplier problem
that can be solved in linear time by just checking whether we have duplicate
entries in the rows, cols, and boxes.

To do so, we use extra space to record the each of the rows, cols, and boxes
entries from 1 - 9. As we only have to store digits upto 9, we can do this with
simple numeric types such as bytes - array of bits.

---

Python:

```python

class Solution26:

    def isValidSudoku(self, board):

        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                
                b = (r // 3) * 3 + (c // 3)
                curr = 1 << int(board[r][c])

                # Bit-wise & operation
                # True iff both a and b are True
                if rows[r] & curr or cols[c] & curr or boxes[b] & curr:
                    return False

                rows[r] |= curr
                cols[c] |= curr
                boxes[b] |= curr

        return True
```

