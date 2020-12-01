# 1293. Shortest Path in a Grid with Obstacles Eliminations

Given a m * n grid, where each cell is either 0 (empty) or 1 (obstacle). In one
step, you can move up, down, left or right from and to an empty cell.

Return the minimum number of steps to walk from the upper left corner (0, 0) to
the lower right corner (m-1, n-1) given that you can eliminate at most
k obstacles. If it is not possible to find such walk return -1.

---

We can find the shortest path using either BFS or astar algorithm. Using astar,
we use heuristic of distance between the goal (m-1,n-1) and the current
position (x,y) - and at each visit, we take a look at the position that is
closest to the goal. We can do this using a minheap as compare by the distance
of each positions.

---

Python: BFS approach;

```python

class Solution1293:

    def shortestPath(self, grid, k):
        
        if not grid or not grid[0] or k - grid[0][0] < 0:
            return -1

        m, n, length = len(grid), len(grid[0]), 0
        q, visited = [(0, 0, k - grid[0][0])], dict()

        while q:

            temp = list()

            for x, y, obsCount in q:
                # revisited same position but with worse obsCount; ignore
                if (x, y) in visited and visited[(x, y)] >= obsCount:
                    continue

                if (x, y) == (m-1, n-1):
                    return length

                visited[(x,y)] = obsCount

                for nx, ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                    if 0 <= nx < m and 0 <= ny < n and obsCount - grid[nx][ny] >= 0:
                        temp.append((nx, ny, obsCount - grid[nx][ny]))
            
            q = temp
            length += 1

        return -1
```

Python: astar approach;

```python

from heapq import heappush, heappop

class Solution1293:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        def helper(i, j):
            return abs(m - i - 1) + abs(n - j - 1)
        
        if not grid or not grid[0]:
            return -1
        
        m, n = len(grid), len(grid[0])
        pq = [(helper(0,0), k - grid[0][0], 0, (0,0))]
        visited = dict()
        
        while pq:
            _, eCount, jumps, curr = heappop(pq)
            if eCount < 0:
                continue
            if curr == (m-1, n-1):
                return jumps
            if curr in visited and visited[curr] >= eCount:
                continue
            visited[curr] = eCount
            i, j = curr
            for ni, nj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0 <= ni < m and 0 <= nj < n:
                    heappush(pq, (helper(ni,nj) + jumps, eCount - grid[ni][nj], jumps + 1, (ni,nj)))
        
        return -1
```
