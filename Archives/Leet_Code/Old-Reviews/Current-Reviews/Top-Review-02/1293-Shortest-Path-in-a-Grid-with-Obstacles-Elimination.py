# 1293 Shortest Path in a Grid with Obstacles Elimination

class Solution:
    def shortestPath(self, grid, k):
        def astar(x, y):
            return abs(m - x - 1) + abs(n - y - 1)

        m, n = len(grid), len(grid[0])

        pq = [(astar(0, 0), -k + grid[0][0], 0, (0, 0))]
        visited = dict()

        while pq:
            _, eCount, moves, pos = heappop(pq)
            if eCount > 0:
                continue
            if pos == (m-1, n-1):
                return moves
            if pos in visited and visited[pos] <= eCount:
                continue
            moves += 1
            i, j = pos
            for ni, nj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0 <= ni < m and 0 <= nj < n:
                    heappush(pq, (astar(ni,nj)+moves, eCount + grid[ni][nj],
                        moves, (ni,nj)))

        return -1
