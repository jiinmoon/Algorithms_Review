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

Follow up:
Could you do better than O(n2) per move() operation?

---

The problem with implementing the Tic-Tac-Toe is that saving the entire state
of the game board is a costly both in time and space. Not only we have to
iterate to update the each rows, cols, and diagonal, but sum them every time to
check whether player has won after certain move.

To solve this, we compress the information about the game; in fact, we only
maintain a list of cols and rows where we maintain the cumulative moves so far
from the players. To do this, we assign -1 to a player 1 and 1 to a player 2.
So, when current row and col has absolute value summed upto N, we know that
current player has won. Also, we maintain diagonal lines as well - up diagonal
line and down diagonal line. Whether current move occupies the diagonal line is
checked by whether current row and col are equal to one another (down diagonal)
or current row plus col equates to N - 1 (up diagonal).

---

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
        if abs(self.rows[r]) == self.n or abs(self.cols[c]) == self.n:
            return player

        if r == c:
            self.dd += score
            if abs(self.dd) == self.n:
                return player

        if r + c == self.n - 1:
            self.ud += score
            if abs(self.ud) == self.n:
                return player

        return 0
```
