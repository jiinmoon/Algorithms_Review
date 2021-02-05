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

#### (1) Maintain entire game board.

This approach is to maintain entire n x n board to save the state of the
on-going game. But this would be O(n^2) per move operation as we have to update
the board as well as check to see whether current player has won. Also, space
complexity would be O(n * n).

#### (2) Maintain only the scores.

Here, we do not have to maintain entire board states - but only the on-going
sum of scores. Assign value of -1 to player1 and 1 to player2. Then, if any one
of them wins, their rows, cols, updiagonal, or downdiagonal score will sum up
to n. By doing so, we can reduce time complexity of move down to O(1) as well
as space down to O(n).

---

Python:

```python

class Solution348:

    def __init__(self, n):

        self.n, self.upDiag, self.downDiag = n, 0, 0
        self.rows = [0] * n
        self.cols = [0] * n


    def next(self, row, col, player):

        score = -1 if player == 1 else 1

        self.rows[row] += row
        self.cols[col] += col

        if row == col:
            self.downDiag += score

        if row + col == self.n - 1:
            self.upDaig += score

        if any(abs(sum) == self.n for sum in [self.rows[row], self.cols[col], self.downDiag, self.upDiag):
            return player

        return 0

```
