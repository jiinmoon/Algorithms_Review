# 1293. Shorest Path in a Grid with Obstacles Elimination

Given a m * n grid, where each cell is either 0 (empty) or 1 (obstacle). In one
step, you can move up, down, left or right from and to an empty cell.

Return the minimum number of steps to walk from the upper left corner (0, 0) to
the lower right corner (m-1, n-1) given that you can eliminate at most
k obstacles. If it is not possible to find such walk return -1.

---

To find the shortest path, there are many algorithms to choose from. But here
we have a heuristic that we can use which is the manhattan distance formula.
Hence, we can use astar search algorithm.

At each stage of our search, we need to repeatedly pick a node where it is most
likely to reach the destination - which is the heuristic mentioned above. To do
so, we maintain a max heap. Also, we need to be mindful of the obstacles that
we encounter - so we also maintain the obstacles elimination count along with
the pq to examine.

---

Python:

```python

import heapq

class Solution:
    def shorestPathWithObs(self, grid, k):
        def helper(i, j):
            return abs(m - i - 1) + abs(n - j - 1)

        if not grid or not grid[0]:
            return -1

        m, n = len(grid), len(grid[0])
        visited = dict()
        pq = [(helper(0,0), -k + grid[0][0], 0, (0,0))]

        while pq:
            _, eCount, jumps, curr = heappop(pq)
            # eCount expired
            if eCount > 0:
                continue
            # reached the goal
            if curr == (m-1, n-1)
                return jumps
            # visited and expired
            if curr in visited and visited[curr] <= eCount:
                continue
            visited[curr] = eCount
            i, j = curr
            for ni, nj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0 <= ni < m and 0 <= nj < n:
                    heappush(pq, (helper(ni,nj) + jumps, eCount + grid[ni][nj], jumps + 1, (ni,nj))

        return -1
```

