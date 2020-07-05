""" 36. Valid Sudoku

Question:

    Determine if 9 x 9 Sudoku board is valid.

+++

Solution:

    Do not be confused to think that we need to solve the Sudoku board in order
    for us to determine whether it is valid! All we need to do is check whether
    the board is valid by checking the three rules: the numbers in each of the
    9 rows, cols, and boxes has to contain unique integer from 1 to 9.

"""

class Solution:
    def is_valid_sudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                curr = board[r][c]
                if curr != '.':
                    box = (r // 3) * 3 + (c // 3)
                    if curr in rows[r] or curr in cols[c] or curr in
                    boxes[box]:
                        return False
                    rows[r].add(curr)
                    cols[c].add(curr)
                    boxes[box].add(curr)
        return True

