""" 36. Valid Sudoku

Question:

    Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
    validated according to the following rules, that is, rows/cols/boxes should
    never contain duplicates from 1-9.

+++

Solution:

    The question does not ask us to check whether the given board is 'solvable'.
    Hence, all we are required to do is check whether rules have been met -
    thus, simply, we iterate on the Sudoku board and check.

"""

class Solution:
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num != '.':
                    box = (row // 3) * 3 + (col // 3)
                    if num in rows[row] or num in cols[col] or num in boxes[box]:
                        return False
                    rows[row].add(num)
                    cols[col].add(num)
                    boxes[box].add(num)
        return True
