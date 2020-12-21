# Valid Sudoku

    Determine if a Sudoku is valid, according to:
    http://sudoku.com.au/TheRules.aspx

    The Sudoku board could be partially filled, where empty cells are filled with
    the character ‘.’.

---

## Approach:

The rules of Sudoku to follow are there should be no duplicate elements within
the rows, cols and the boxes. So, we create a set for each of theses conditions
to check for duplicates.

O(n^2) in time complexity.

---

Python:

```python

class Solution:

    def isValidSudoku(self, board):

        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                curr = 1 << (int(board[r][c]))
                b = (r // 3) * 3 + (c // 3)

                if curr & rows[r] != 0 or curr & cols[c] != 0 or curr & boxes[b] != 0:
                    return False

                rows[r] |= curr
                cols[c] |= curr
                boxes[b] |= curr

        return True
```
        

