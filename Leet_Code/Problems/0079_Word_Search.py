""" 79. Word Search

Question:

    Given a 2D board and a word, find if the word exists in the grid.

+++

Solution:

    We may use backtracking algorithm (DFS) to start the search for the word
    whenever we encounter the beginning of the word. Remember to track visited
    cells as this fundamentally is a graph traversal problem. Also, tricky in
    when to check for the current word - or next word. Make sure to go through
    the diferent possible example cases.

"""

class Solution:
    def exist(self, board, word):
        if not board or not word:
            return False

        m, n = len(board), len(board[0])

        def isValidCoords(x, y):
            return x >= 0 and x < m and y >= 0 and y < n

        def search(i, j, index):
            if index == len(word):
                return True
            if not isValidCoords(i, j) or board[i][j] != word[index]:
                return False
            temp = board[i][j]
            board[i][j] = '*'
            for nextX, nextY in [ (i+1, j), (i-1, j), (i, j+1), (i, j-1) ]:
                if backtrack(nextX, nextY, index+1):
                    return True
            board[i][j] = temp
            return False

        for row in range(m):
            for col in range(n):
                if board[row][col] == word[0] and backtrack(row, col, 0):
                    return True
        return False
