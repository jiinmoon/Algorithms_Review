# 994. Rotten Oranges

In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten
orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh
orange.  If this is impossible, return -1 instead.

---

We think of this problem as a graph traversal - starting from each of the
rotten cells, we explore neighbour cells that are marked as fresh. At each
depth, we count the length to record the minimum number of minutes that elapsed
with BFS algorithm - in order to find the shortest path that can take to turn
each fresh cell into a rotten cell.

Time and sapce complexity would be O(n).

---

Java:

```java

import java.util.HashSet;

class Solution {
    public int orangesRotting(int[][] grid) {
        if (grid.length == 0 or grid[0].length == 0)
            return -1;

        int m, n, elapsed;
        m = grid.length;
        n = grid[0].length;
        elapsed = 0

        // collect all starting rotten cells and available fresh cells
        Set<List<Integer>> fresh, rotten, next_rotten;
        fresh = new HashSet<>();
        rotten = new HashSet<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1)
                    fresh.add(List.of(i, j));
                else if (grid[i][j] == 2)
                    rotten.add(List.of(i, j));
            }
        }

        int[][] directions = {{1,0}, {0,1}, {-1,0}, {0,-1}};
        
        // explore as long as fresh cells to cover
        while (!fresh.isEmpty()) {
            next_rotten = new HashSet<>();
            
            // starting from each rotten cell, expand to 4 directions
            for (List<Integer> curr : rotten) {
                int x = curr.get(0);
                int y = curr.get(1);
                for (int i = 0; i < 4; i++) {
                    next_rotten.add(List.of(
                                        x + directions[i][0],
                                        y + directions[i][1]));
                }
            }

            // fresh cells are left to cover but cannot visit them
            if (next_rotten.isEmpty())
                return -1;

            next_rotten.removeAll(fresh);
            fresh.removeAll(next_rotten);

            rotten = next_rotten;
            elapsed += 1
        }
        return elapsed;
    }
}

```

Python:

```python

class Solution:
    def rottingOranges(self, grid):
        if not grid or not grid[0]:
            return -1

        m, n, elapsed = len(grid), len(grid[0]), 0
        rotten, fresh = set(), set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh.add((i,j));
                elif grid[i][j] == 2:
                    rotten.add((i,j))

        while fresh:
            next_rotten = set()
            for i, j in rotten:
                for ni, nj in [(i+x, j+y) for x in (-1, 1) for y in (-1, 1)]:
                    if (ni, nj) in fresh:
                        next_rotten.add((ni,nj))
            
            if not next_rotten:
                return -1

            fresh -= next_rotten
            rotten = next_rotten
            elapsed += 1

        return elapsed
```

