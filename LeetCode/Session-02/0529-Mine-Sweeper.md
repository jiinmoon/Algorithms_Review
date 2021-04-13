# 529. Mine Sweeper

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

This can be visualized as a graph problem - and traversal one at that.

Starting from the clicked cell (i, j), we examine surrounding tiles for
presence of a mine - if we found any, we record its count to current cell.
Otherwise, we mark it as blank and add surrounding neighbours to visit in next
iteration to our queue.

---

Python:

```python

from collections import deque

class Solution529:

    def upateBoard(self, board, click):
        
        if not (board and board[0] and click):
            return board

        # edge case; clicked on mine tile at start
        i, j = click[0], click[1]
        if board[i][j] == "M":
            board[i][j] = "X"
            return board
        
        # find valid 8 surrounding neighbour coordinates
        def neighbourCoords(i, j):
            for ni, nj in [(i+x,j+y) for x in (-1,0,1) for y in (-1,0,1)]:
                if ni == i and nj == j:
                    continue
                if 0 <= ni < m and 0 <= nj < n:
                    yield ni, nj

        m, n, queue = len(board), len(board[0]), deque([click])

        while queue:

            i, j = queue.popleft()
            
            # current (i, j) is already explored (NOT unrevealed)
            if board[i][j] != 'E':
                continue

            # explore neighbours to count mines
            mines = 0
            for ni, nj in neigbourCoords(i, j):
                mines += neighbourCoords == "M"

            # mark current cell with count of mines if there are any
            if mines:
                board[i][j] = str(mines)
            # otherwise, continue to explore while marking current as explored
            else:
                board[i][j] = "B"
                for ni, nj in neighbourCoords(i, j):
                    queue.append( (ni, nj) )

        return board
```

