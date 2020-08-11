348 Design Tic-Tac-Toe
======================

Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves is allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or
diagonal row wins the game.

---

Instead of maintaing entire board state, and compute the winning condition each
time, we will simply maintain the sum of rows and cols; as well as indicators
for diagonal cases.

Convert the players to 1 and -1; then, we can record the spots marked by each
player, and compute the winning condition easily by checking whether the sum of
marked spot reached the n.

---

Python:

```python
class TicTacToe:
    def __init__(self, n):
        self.rows = [ 0 for _ in range(n) ]
        self.cols = [ 0 for _ in range(n) ]
        self.diag_up = self.diag_down = 0
        self.n = n

    def move(self, r, c, player):
        # convert player into 1 or +1.
        mark = (2 * player) - 3
        self.rows[r] += mark
        self.cols[c] += mark

        # winning cond #1
        # have rows and cols marked by current player?
        if self.rows[r] == self.n or self.cols[c] == self.n:
            return player

        # winning cond #2
        # check the diagnoally up and down.
        if row == col:
            self.diag_up += mark
            if abs(self.diag_up) == n:
                return player
        if row+col == n-1:
            self.diag_down += mark
            if abs(self.diag_down) == n:
                return player

        return 0
```
