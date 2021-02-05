# 348 Design Tic-Tac-Toe

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
---

The trick is maintaining only the scores for each of the rows, and cols instead
of the entire state of the board. Rows, cols, and diagonal sum of the points
which are assigned to the players (player 1 == -1, player 2 == 1) will let us
determine whether a player has won after making the move by checking the
absolute sum to equal to the length of the Tic Tac Toe grid.

---

Python:

```python

class TicTacToe:
    def __init__(self, n):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.ud, self.dd = 0, 0

    def move(self, player, r, c):
        score = -1 if player == 1 else 1

        rows[r] += score
        cols[c] += score
        if abs(sum(rows[r])) == self.n or abs(sum(cols[c])) == self.n:
            return player

        if r == c:
            self.dd += score
            if abs(self.dd) == self.n:
                return player

        if r + c == self.n - 1:
            self.ud += score
            if abs(self.id) == self.n:
                return player

        return 0
```
