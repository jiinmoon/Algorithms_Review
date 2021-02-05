# Sudoku

    Write a program to solve a Sudoku puzzle by filling the empty cells.
    Empty cells are indicated by the character '.'
    You may assume that there will be only one unique solution.

---

## Approach:

Use backtrack to explore far out as possible; first iterate on the column and
when column reaches the end, we move to next row. If row and col reaches the
end, we have our solved board.

For each of the positions, we try all 9 candidates; if we can place the number
as determined by record of previous rows, cols, and boxes which makes up the
criteria for valid sudoku board, we record current value in the board and
recurse down the path for possible solution. If we cannot find it, restore the
state of backtrack.

O(9 ^ n!) time complexity, and space is bounded by the size of the given board
as we perform this in-place.

---

Python:

```python

class Solution:

    def solveSudoku(self, board):

        N = len(board)
        
        # records previously seen or already added values on board
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        # initialize with partially solved values
        for row in range(N):
            for col in range(N):
                if board[row][col] == ".":
                    continue
                curr = str(board[row][col])
                box = (row // 3) * 3 + (col // 3)
                rows[row].add(curr)
                cols[col].add(curr)
                boxes[box].add(curr)

        def helper(row, col):

            # Solved board when we have reached end of row and col
            if row == N - 1 and col == N:
                return True

            # Current row is finished; move onto next row
            if col == N:
                row += 1; col = 0
            
            # Current cell is occupied
            if board[row][col] != ".":
                return helper(row, col + 1)
            
            # Consider 9 candidates from 1 - 9
            for curr in range(1, N + 1):
                box = (row // 3) * 3 + (col // 3)

                # if duplicate value for row, col, box? skip
                if curr in rows[row] or curr in cols[col] or curr in boxes[box]:
                    continue
                
                # otherwise, valid; record and recurse down the path
                board[row][col] = str(curr)
                rows[row].add(curr); cols[col].add(curr); boxes[box].add(curr)
                if helper(row, col + 1):
                    return True
                
                # restore for next candidate
                rows[row].remove(curr); cols[col].remove(curr); boxes[box].remove(curr)
                board[row][col] = "."

            return False

        helper(row, col)
```
