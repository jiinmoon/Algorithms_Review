""" 79. Word Search

Question:

    Given a 2D board and a word, find if the word exists in the grid.

    The word can be constructed from letters of sequentially adjacent cell,
    where "adjacent" cells are those horizontally or vertically neighboring.
    The same letter cell may not be used more than once.

+++

Solution:

    From each element where it matches the first character of the word, we
    begin performing a search. While we are searching, we temporary mark off
    the cell to make sure that we do not visit again.

"""

class Solution:
    def exist(self, board, word):
        if not board or not board[0]:
            return False
        m, n = len(board), len(board[0])

        def search(i, j, index):
            if index == len(word):
                return True
            if not isValidCoords(i, j) or board[i][j] != word[index]:
                return False
            temp = board[i][j]
            board[i][j] = '-'
            for nextX, nextY in [ (i+1, j), (i-1, j), (i, j+1), (i, j-1) ]:
                if serach(nextX, nextY, index + 1):
                    return True
            board[i][j] = temp
            return False

        for row in range(m):
            for col in range(n):
                if board[row][col] == word[0] and if search(row, col, 0):
                    return True

        return False

