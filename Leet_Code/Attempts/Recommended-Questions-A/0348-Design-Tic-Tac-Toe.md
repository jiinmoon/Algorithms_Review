# 348. Design Tic-Tac-Toe

Assume the following rules are for the tic-tac-toe game on an n x n board
between two players:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves are allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or
diagonal row wins the game.

Implement the TicTacToe class:

```
TicTacToe(int n) Initializes the object the size of the board n.

int move(int row, int col, int player) Indicates that player with id player
plays at the cell (row, col) of the board. The move is guaranteed to be a valid
move.
```

Follow up:

Could you do better than O(n2) per move() operation?

---

Naive approach of maintaing the entire 2D board state is a problem since
finding the score after move() operation will be O(n^2) to check all the cols,
diagnoal lines and rows. Hence, instead, we forego maintain the entire board
state - instead, we only maintain a cumulation of the player moves for rows,
cols, up-diagonal, down-diagonal lines. This way, we can check who won in O(1).

---

Java:

```java

class TicTacToe {
    
    private int BoardSize, upDiag, downDiag;
    private int[] rows, cols;

    public TicTacToe(int n) {
        this.BoardSize = n;
        this.upDiag = this.downDiag = 0;
        this.rows = new int[n];
        this.cols = new int[n];
    }

    public int move(int row, int col, int player) {
        int score = (player == 1) ? -1 : 1;

        this.rows[row] += score;
        this.cols[col] += score;

        if (Math.abs(this.rows[row]) == this.BoardSize || Math.abs(this.cols[col]) == this.BoardSize)
            return player;

        if (row == col) {
            this.downDiag += score;
            if (Math.abs(this.downDiag) == this.BoardSize) return player;
        }

        if (row + col == this.BoardSize - 1) {
            this.upDiag += socre;
            if (Math.abs(this.upDiag) == this.BoardSize) return player;
        }
        
        return 0;
    }

}


```

Python:

```python

class TicTacToe:
    def __init__(self, n):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.ud, self.dd = 0, 0

    def move(self, r, c, player):
        score = -1 if player == 1 else 1

        self.rows[r] += score
        self.cols[c] += score
        if abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n:
            return player

        if r + c == self.n - 1:
            self.ud += score
            if abs(self.ud) == self.n:
                return player

        if r == c:
            self.dd += score
            if abs(self.dd) == self.n:
                return player

        return 0
```
