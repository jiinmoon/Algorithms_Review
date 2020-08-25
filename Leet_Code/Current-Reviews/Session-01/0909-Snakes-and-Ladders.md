909 Snakes and Ladders
======================

Compute minimum number of moves to complete the game of snakes in N x N board
where each cell is either -1 which is non-snake cell or a number that indicates
the where next move is going to take place. The board is written in
boustrophedonical order.

----

The problem appears to be a DP solution - and there may well be but it is
rather difficult to see it. The best we can do is a breadth-frist search to
simulate the game. At each depth, we move to 1 to 6 different possible moves
while taking account for whether the current cell is a snake, in which case we
take the snake when computing for next possible movements.

The slight difficulty is trying to deal with the particular ordering that this
board has - we could either use some map of coordinates, or simply convert the
given list into a line.

Time complexity of this problem is O(n^2) since for each cell in board, we may
need to move down as far as end of the board.

---

Python:

```python
class Solution:
    def snakesAndLadders(self, board):
        new_board = [-1]
        flipped = False
        for row in board[::-1]:
            if flipped:
                new_board += row[::-1]
            else:
                new_board += row
            flipped = not flipped
        q = {1}
        visited = {}
        m = len(board)
        moves = 0
        while q:
            next_q = {}
            for curr in q:
                if curr in visited or curr >= m:
                    continue
                visited.add(curr)
                if board[curr] != -1:
                    curr = board[curr]
                if curr == m-1:
                    return moves
                for i in range(1, 7):
                    next_q.add(i + curr)
            visited |= next_q
            q = next_q
            moves += 1
        return -1
```


