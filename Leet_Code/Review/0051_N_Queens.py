""" 51. N-Queens

Question:

    Given an integer n, return all distinct solutions to the n-queens puzzle.

    The board consists of 'Q' and '.' for queen and empty space respectively.

+++

Solution:

    The backtracking algorithm is used to explore different configurations for
    the queens placement. At each depth, we are build row after another,
    placing our queens. What we need to confirm is that whether we can place
    the Queen at the current location or not. Since we are building row after
    another, we have to only maintain the columns, and diagnoal slopes that the
    queens cannot be placed at.

"""

class Solution:
    def solveNQueens(self, n):
        result = []
        board = [[''] * n for _ in range(n)]
        cols, upDiag, downDiag = set(), set(), set()

        def backtrack(row, path):
            if row == n:
                # finished building the board.
                result.append([''.join(_) for _ in path])
                return
            for col in range(n):
                if col not in cols and row - col not in upDiag and row + col
                not in downDiag:
                    path[row][col] = 'Q'
                    cols.add(col)
                    upDiag.add(row - col)
                    downDiag.add(row + col)
                    backtrack(row+1, path)
                    downDiag.remove(row + col)
                    upDiag.remove(row - col)
                    col.remove(col)
                    path[row][col] = '.'

        backtrack(0, board)
        return result


