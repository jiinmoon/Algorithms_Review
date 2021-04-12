# 289. Game of Life

According to Wikipedia's article: "The Game of Life, also known simply as Life,
is a cellular automaton devised by the British mathematician John Horton Conway
in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial
state: live (represented by a 1) or dead (represented by a 0). Each cell
interacts with its eight neighbors (horizontal, vertical, diagonal) using the
following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by
under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by
over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by
reproduction.

The next state is created by applying the above rules simultaneously to every
cell in the current state, where births and deaths occur simultaneously. Given
the current state of the m x n grid board, return the next state.

---

To find the next state of the given board, we have to iterate on each of the
cells, and check surrounding neighbours for the condition - in particular there
are two conditions to decide whether our current cell lives or dies that is
there are 3 live cells in total including the current cell. Hence, we iterate
and visit each of the cell and count the 8 neighbour's state.

We can save the space by performing this in-place where we use extra second
digit to denote whether the cell is alive or dead. By doing so, we can mark the
live cell by simply adding two to our cells ( which would be either 1 or 0 ),
and next state can be simply right shift by one to overwrite the previous
state.

---

Python:

```python

class Solution289:

    def nextState(self, board):

        if not (board and board[0]):
            return None
        
        # count 8 neigbours who are alive
        def countNeighbours(i, j):
            count = 0
            for x, y in [(x,y) for x in (-1,0,1) for y in (-1,0,1) if x != 0 and y != 0]:
                if 0 <= i + x < m and 0 <= j + y < n:
                    count += board[i + x][j + y] % 2
            return count

        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                count = countNeighbours(i, j)
                # current cell lives iff ...
                if count == 3 or (count == 2 and board[i][j]):
                    count += 2

        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1
```
