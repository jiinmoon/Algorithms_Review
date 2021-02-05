# 1091. Shortest Path in Binary Matrix

In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is
composed of cells C\_1, C\_2, ..., C\_k such that:

Adjacent cells C\_i and C\_{i+1} are connected 8-directionally (ie., they are
different and share an edge or corner)
C\_1 is at location (0, 0) (ie. has value grid[0][0])
C\_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
If C\_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
Return the length of the shortest such clear path from top-left to
bottom-right.  If such a path does not exist, return -1.

---

This problem can be visualized as a graph problem where are to find the
shortest path from the start (0,0) to the goal (n-1,n-1). For this we can use
BFS algorithm. In particular, bidirectional BFS can be used here to better
reduce the time complexity where the depth to explore will be reduced by half
as well as avoiding exploring on the path that has the worst branching factor.

---

Java:

```java

import java.util.Deque;
import java.util.LinkedList;

// approach this problem by visualizing it as a single number line
// entire line spans from 0 to m + n - 1
// hence, current cell at (row, col) can be represented as (row * col + col)
// row = (current / col)
// col = (current % col)

class Solution {

    public int shortestPathBinaryMatrix(int[][] grid) {
        if (grid.length == 0 || grid[0].length == 0) return -1;
        if (grid.length == 1) return (grid[0] == 0) ? 1 : 0;

        int m = grid.length;
        int n = grid[0].length;
        
        if (grid[0][0] == 1 || grid[m-1][n-1] == 1) return -1;
        
        // start from (0,0) and (m-1,n-1)
        Deque<Integer> front = new LinkedList<>(List.of(0));
        Deque<Integer> back = new LinkedList<>(List.of((m-1)*n + n));
        
        // visited; mark front and back separately to detect overlap
        boolean[][] visitedFront = new boolean[m][n];
        boolean[][] visitedBack = new boolean[m][n];
        visitedFront[0][0] = true;
        visitedBack[m-1][n-1] = true;
        
        // already covered trivial case of length 1; start from 2
        int result = 2;

        while (!front.isEmpty() && !back.isEmpty()) {
            if (front.size() > back.size()) {
                Deque<Integer> tempDeque = front;
                front = back;
                back = tempDeque;

                boolean[][] tempVisited = visitedFront;
                visitedFront = visitedBack;
                visitedBack = tempVisited;
            }

            int size = front.size();
            while (size-- > 0) {
                int pos = front.removeFirst();
                int x = pos / n;
                int y = pos % n;
                for (int dx : new int[]{-1, 0, 1}) {
                    for (int dy : new int[]{-1, 0, 1}) {
                        int nx = x + dx;
                        int ny = y + dy;
                        if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
                        if (visitedFront[nx][ny]) continue;     // visited
                        if (grid[nx][ny] == 1) continue;        // blocked
                        if (visitedBack[nx][ny]) return result; // goal reached

                        visitedFront[nx][ny] = true;
                        front.addLast((nx*n) + ny);
                    }
                }
            }

            result++;
        }
        return -1;
    }
}


```

Python:

```python

class Solution:
    def findShorestPath(self, matrix):
        # matrix does not exist or start/goal is blocked
        if not matrix or matirx[0][0] or matrix[-1][-1]:
            return -1

        n = len(matrix)
        f, b, visited = {(0,0)}, {(n-1,n-1)}, {}
        length = 1
        while f and b:
            if f & b:
                return length

            if len(f) > len(b):
                f, b = b, f

            newf = set()
            for i, j in f:
                visited.add((i,j))
                # 8 directions to explore
                for ni, nj in [(i+x, j+y) for x in (-1,0,1) for y in (-1,0,1)]:
                    if 0 <= ni < n and 0 <= nj < n and not matrix[ni][nj] and not (ni,nj) in visited:
                        newf.add((ni,nj))

            f = newf
            length += 1
        
        return -1
```
