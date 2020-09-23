# 348 Design Tic-Tac-Toe

We could maintain the entire board state, but we can save space by only
maintain the winning conditions which are cumulative scors on rows, cols, up
diagonal and down diagonals.

---

Python:

```python

class TTT:
    def __init__(self, n):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.ud, self.dd = 0, 0

    def move(self, player, r, c):
        score = -1 if player == 1 else 1
        self.rows[r] += score
        self.cols[c] += score
        if abs(self.rows[r]) == self.n or abs(self.cols[c]) == self.n:
            return player

        if r + c == n - 1:
            self.ud += score
            if abs(self.ud) == self.n:
                return player

        if r == c:
            self.dd += score
            if abs(self.dd) == self.n:
                return player

        return 0
```
