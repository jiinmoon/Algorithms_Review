# 36. Valid Sudoku

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

We can check for validity by recording each of the numbers appearing on the
board, where each are categorized by its row, column and 3 x 3 boxes. For each
cell examined, we check to see whether duplicate entry has been found before in
our record.

As the board is gurantee'd to be 9 x 9, the overall time and space complexity
would be constant. However, we can make further improvement in space and time
by using bit operation (bit-wise OR and bit-wise AND) and use 4-bit primitive
integer type since the digits are from 1 - 9.

---

Python:

```python

class Solution36:

    def isValidSudoku(self, board):
        
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        
        for r in range(9):
            for c in range(9):
                if not board[i][j]:
                    continue
                
                val = 1 << int(board[i][j])
                b = (r // 3) * 3 + (c // 3)
                
                if rows[r] & val or cols[c] & val or boxes[b] & val:
                    return False

                rows[r] |= val
                cols[c] |= val
                boxes[b] |= val

        return True
```

