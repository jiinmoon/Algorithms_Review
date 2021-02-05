""" 130. Surrounded Regions

Question:

    Given a 2D board containing 'X' and 'O', capture all regions surrounded by
    'X'.

+++

Solution:

    By default, all 'O's should be flip-able. But those that touches the borders
    should not be. Thus, we use bactracking algorithm that spans from borders to
    explore and mark all the '0's that touches the border.

"""

class Solution:
    def solve(self, board):
        m = len(board)
        if not m:
            return
        n = len(board[0])

        def backtrack(i, j):
            board[i][j] = ''
            for x, y in [ (i+1, j), (i-1, j), (i, j+1), (i, j-1) ]:
                if x >= 0 and x < m and y >= 0 and y < n and board[x][y] == 'O':
                    backtrack(x, y)

        # backtrack to mark all 'O's touching border.
        for i in range(m):
            if board[i][0] == 'O':
                backtrack(i, 0)
            if board[i][n-1] == 'O':
                backtrack(i, n-1)

        for i in range(n):
            if board[0][i] == '0':
                backtrack(0, i)
            if board[m-1][i] == '0':
                backtrack(m-1, i)

        # flip all unmarked 'O's.
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '':
                    board[i][j] = 'O'
