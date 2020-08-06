""" 51. N-Queens

Question:

    The n-queens puzzle is the problem of placing n queens on an n x n
    chessboard such that no two queens attack each other.

    Given an integer n, return all distinct solutions to the n-quuens puzzle.

    Each solution contains a distinct board configuration of the n-queens'
    placement, where 'Q' and '.' both indicate a queen and an empty space
    respectively.

+++

Solution:

    The N-Quees problem can be solved via backtracking algorithm - with trying
    to place the queens at their valid place. The problem here is the finding
    that valid space. We know that queens can attack across the row, col, and
    diagonally. This implies that once queen is placed, we cannot place on the
    same row - meaning, all we need to concern our selves with is the cols and
    diagonals as we can increase the row as we explore further into the depth.

    Hence, we need three record structure for cols, upDiagonal, downDiagnoal.
    We know that line formula for increasing is y = x and y = -x, which can be
    used to keep track of upDiagonal and downDiagnoal lines of placed Queens.

"""

class Solution:
    def solveNQueens(self, n):
        result = []
        path = [[''] * n for _ in range(n)]
        cols, upDiag, downDiag = set(), set(), set()

        # building the board row after row since only a single queen can be
        # placed in the board.
        def backtrack(path, row):
            if row == n:
                result.append([''.join(row) for row in path])
                return
            # at each row, we can consider to place queen at any col.
            for col in range(n):
                if col not in cols and row-col not in upDiag and row+col not in downDiag:
                    # path[row][col] is availble for Queen.
                    path[row][col] = 'Q'
                    cols.add(col)
                    upDiag.add(row-col)
                    downDiag.add(row+col)
                    backtrack(path, row+1)
                    # remember to restore the state for next iteration.
                    downDiag.remove(row+col)
                    upDiag.remove(row-col)
                    cols.remove(col)
                    path[row][col] = '.'

        backtrack(path, 0)
        return result
