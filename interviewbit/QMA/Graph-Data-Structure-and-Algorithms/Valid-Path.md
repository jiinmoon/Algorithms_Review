# Valid Path

There is a rectangle with left bottom as  (0, 0) and right up as (x, y). There
are N circles such that their centers are inside the rectangle.
Radius of each circle is R. Now we need to find out if it is possible that we
can move from (0, 0) to (x, y) without touching any circle.

Note : We can move from any cell to any of its 8 adjecent neighbours and we
cannot move outside the boundary of the rectangle at any point of time.

1st argument given is an Integer x.
2nd argument given is an Integer y.
3rd argument given is an Integer N, number of circles.
4th argument given is an Integer R, radius of each circle.
5th argument given is an Array A of size N, where A[i] = x cordinate of ith
circle
6th argument given is an Array B of size N, where B[i] = y cordinate of ith
circle

---

We first create a 2D visited array to denote invalid coordinates to visit
again. For each (x, y), we cannot visit them if (1) we have visited them
previously, or (2) the coordinate lies within the circle.

To determine whether the current coordinate is within the circle, we use the
distance formula; the distance from the origin of the circle to target
coornidates should not be within the 2 * radius.

So, we first iterate to mark all coordinates that are within the circle. Then,
perform either DFS or BFS to explore whether we can reach the target (x, y).

O(m * n) in time complexity.

---

Python:

```python

class Solution:

    def validPathExists(self, m, n, N, radius, circle1, circle2):

        visited = [[False] * (n + 1) for _ in range(m + 1)]

        # iterate to initialize visited
        # mark all (x, y) where it lies within the radius of circle
        for x in range(m + 1):
            for y in range(n + 1):
                for x0, y0 in zip(circle1, circle2):
                    visited[x][y] = (x - x0) ** 2 + (y - y0) ** 2 <= 2 * radius
        
        # start from (0, 0) to reach (m, n)
        queue = [(0, 0)]
        visited[0][0] = True

        while queue:

            x, y = queue.pop()
            if (x, y) == (m, n):
                return "YES"

            for nx, ny in [(x+dx,y+dy) for dx in (-1,0,1) for dy in (-1,0,1)]:
                if 0 <= nx <= m and 0 <= ny <= n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx,ny))

        return "NO"
```
