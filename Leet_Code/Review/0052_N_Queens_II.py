""" 52. N-Queens II

Question:

    The n-queens puzzle is the problem of placing n queens on an
    n x n cheeboard such that no two queens attack each other.

    Given an integer n, return the number of distinct solutions to the n-queens
    puzzle.

+++

Solution:

    Previously, we had to build the board state as a result. This time, we can
    forego that - when our row simply reaches the n, it implies that there
    exists a path which successfully solves the problem.

"""

class Solution:
    def solveNQueens(self, n):
        cols, up, down = set(), set(), set()
        total = [0]
        
        def backtrack(row):
            if row == n:
                total[0] += 1
                return
            for col in range(n):
                if col in cols or (row-col) in up or (row+col) in down:
                    continue
                cols.add(col); up.add(row-col); down.add(row+col)
                backtrack(row+1)
                cols.remove(col); up.remove(row-col); down.remove(row+col)

        backtrack(0)
        return total[0]

