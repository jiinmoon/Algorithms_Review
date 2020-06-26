""" Valid Sudoku

Solution:

    The important fact is that you do not have to solve the given Sudoku board
    in order to know that whether it is valid; we would simply have to check its
    3 rules on rows, cols, and boxes.

"""

class Solution:
    def isValidSudoku(self, matrix):
        # interesting, judge wouldn't accept following:
        # rows = [ set() ] * 9
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                curr = matrix[row][col]
                if curr != '.':
                    box = (row // 3) * 3 + (col // 3)
                    if curr in rows[row] or curr in cols[col] or curr in boxes[box]:
                        return False
                    rows[row].add(curr)
                    cols[col].add(curr)
                    boxes[box].add(curr)

        return True

