# 289. Game of Life

According to the Wikipedia's article: "The Game of Life, also known simply as
Life, is a cellular automaton devised by the British mathematician John Horton
Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or
dead (0). Each cell interacts with its eight neighbors (horizontal, vertical,
diagonal) using the following four rules (taken from the above Wikipedia
article):

Any live cell with fewer than two live neighbors dies, as if caused by
under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by
over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by
reproduction.


Write a function to compute the next state (after one update) of the board
given its current state. The next state is created by applying the above rules
simultaneously to every cell in the current state, where births and deaths
occur simultaneously.

---

Here, state of the cell is either 1 or 0. As we do not want to simultaneously
update the board to contaminate further information, we appear to have no
choice but create a fresh board to replace the original. However, using bit
operation, we can denote the next state of the cell in-place; we use the second
bit as our indicator as to whether current cell should be turned on or down.
This is done by adding 2 (`10`) to our cells that we have determined to let
live (determined by counting 8 neighbours). Then, when we are done, we can
reduce it by right bit shift by one.

Time complexity would be O(m * n) and no additional space required.

---

Java:

```java

class Solution {
    
    private int[][] board;
    
    private int countLiveNeighbours(int i, int j)
    {
        int count = 0;
        
        for (int dx : new int[] {-1, 0, 1})
        {
            for (int dy : new int[] {-1, 0, 1})
            {
                if (dx == 0 && dy == 0)
                    continue;
                
                int ni = i + dx, nj = j + dy;
                
                if (ni >= 0 && ni < this.board.length && nj >= 0 && nj < this.board[0].length)
                    count += board[ni][nj] % 2;
            }
        }
        
        return count;
    }
    
    public void gameOfLife(int[][] board) {
        this.board = board;
        
        for (int i = 0; i < board.length; i++)
        {
            for (int j = 0; j < board[0].length; j++)
            {
                int count = countLiveNeighbours(i, j);

                if (count == 3|| (count == 2 && board[i][j] != 0))
                    board[i][j] += 2;
            }
        }
        
        for (int i = 0; i < board.length; i++)
        {
            for (int j = 0; j < board[0].length; j++)
                board[i][j] >>= 1;
        }
    }
}
```

