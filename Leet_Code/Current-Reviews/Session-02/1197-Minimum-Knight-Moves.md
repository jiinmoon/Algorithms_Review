1197 Minimum Knight Moves
=========================

In an infinite chess board with coordinates from -infinity to +infinity, you
have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is
two squares in a cardinal direction, then one square in an orthogonal
direction.

Return the minimum number of steps needed to move the knight to the square [x,
y].  It is guaranteed the answer exists.

---

Rather than performing a blind search such that whether knight can reach (x,
y), we rather use heuristic to determine at each step whether we are getting
closer to the goal or not. To do this, we use a min heap based on the possible
minimum moves required to reach the target and store actual value of the moves to
took to get to that square and current square.

This A* is based on the minimum moves that will take to reach the target.

The cases are as follows:

1. if the either distance to x or y from current square's x and y is greater
   than other by factor of two or more, then we can reach that cell in half the
   time since knight can move 2/1 in either direction.

2. if not, then we need to factor in additional moves that will take to reach
   the target from the smaller dist to x or y.

The time complexity of this algorithm would be based on the number of moves to
complete the search: O(n**8) since there are 8 possible moves that knight can
make to reach the target.

---

Python:

```python
from heapq import heappush, heappop

class Solution:
    def minKnightMoves(self, x, y):
        
        def astar(currentSquare):
            distToX, distToY = abs(currentSquare - x), abs(currentSquare - y)
            minDist, maxDist = sorted([distToX, distToY])
            maxMoveToTarget = (maxDist + 1) // 2
            return maxMovesToTarget + max(0, (midDist - maxMovesToTarget + 1) // 2)

        # q is a min heap that chooses minimum moves determined by astar
        # heuristic from current square to target square
        # [heuristic_value, movesTakenThusFar, currentSquare]
        q = [ [astar( (x,y) ), 0, (0,0)] ]
        # needed to avoid cycle
        visited = set()

        while q:
            _, movesThusFar, currentSquare = heappop(q)
            if currentSquare == (x, y):
                return movesThusFar
            movesThusFar += 1
            if currentSquare in visited:
                continue
            visited.add(currentSquare)
            # total 8 possible moves to make
            i, j = currentSquare
            nextCandidates = [
                (i-1,j-2), (i-2,j-1), (i-2,j+1), (i-1,j+2),
                (i+1,j-2), (i+2,j-1), (i+2,j+1), (i+1,j+2)
            ]
            for nextSquare in nextCandidates:
                if nextSquare not in visited:
                    heappush(q, [ astar(nextSquare)+movesThusFar, movesThusFar, nextSquare ])
        return -1
```


