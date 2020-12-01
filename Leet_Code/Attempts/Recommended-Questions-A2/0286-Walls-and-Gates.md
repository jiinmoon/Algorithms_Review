# 286. Walls and Gates

You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to
represent INF as you may assume that the distance to a gate is less than
2147483647.

Fill each empty room with the distance to its nearest gate. If it is impossible
to reach a gate, it should be filled with INF.

---

We can approach this from with BFS algorithm as we can increment length from
each gate position to mark the empty room as we discover them. First, collect
all the gates in queue. Starting from these, we expand out depth by depth.

Time complexity would be O(m + n).

---

Python:

```python

class Solution286:

    def wallsAndGates(self, rooms):

        if not rooms or not rooms[0]:
            return

        m, n, length = len(rooms), len(rooms[0]), 0
        queue, toVisit, visited = list(), set(), set()

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i,j))
                elif rooms[i][j] == -1:
                    visited.add((i,j))
                elif rooms[i][j] == 2**31 - 1:
                    toVisit.add((i,j))

        while queue:

            temp = list()
            for i, j in queue:
                if (i, j) in visited:
                    continue
                visited.add((i,j))
                rooms[i][j] = length
                for ni, nj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if (ni, nj) in toVisited:
                        temp.append((ni,nj))
                        toVisited.remove((ni,nj))

            temp = queue
            length += 1

```
