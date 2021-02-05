# 529. Minesweeper

Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. 'M' represents an
unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents
a revealed blank square that has no adjacent (above, below, left, right, and
all 4 diagonals) mines, digit ('1' to '8') represents how many mines are
adjacent to this revealed square, and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the
unrevealed squares ('M' or 'E'), return the board after revealing this position
according to the following rules:

If a mine ('M') is revealed, then the game is over - change it to 'X'.
If an empty square ('E') with no adjacent mines is revealed, then change it to
revealed blank ('B') and all of its adjacent unrevealed squares should be
revealed recursively.
If an empty square ('E') with at least one adjacent mine is revealed, then
change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.

---

We traverse starting from clicked cell and expand out so long as it is not
explored yet ("E"). For each cell that we visit, we first check its surrounding
areas for mines ("M"). If mines are found, then current cell is updated as
a count of mines that we have discovered. Otherwise, we mark the cell as
revealed "B" and continue our traversal.

Time complexity would be O(m * n) as worst case we have to explore out.

---

Python:

```python

from collections import deque

class Solution529:

    def updateBoard(self, board, click):

        if not (board and board[0] and click):
            return board

        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board

        queue = deque([click])

        def neighbours(x, y):
            for nx, ny in [(x+i,y+j) for i in (-1,0,1) for j in (-1,0,1)]:
                if nx == x and ny == y:
                    continue
                yield nx, ny

        def countMines(x, y):
            mines = 0
            for nx, ny in neighbours(x, y):
                mines += board[nx][ny] == "M"
            return mines


        while queue:

            x, y = queue.popleft()
                
            if board[x][y] == "E":
                continue

            mines = countMines(x, y)

            if mines:
                board[x][y] = str(mines)
            else:
                board[x][y] = "B"
                for nx, ny in neighbours(x, y):
                    queue.append((nx,ny))

        return board
```
