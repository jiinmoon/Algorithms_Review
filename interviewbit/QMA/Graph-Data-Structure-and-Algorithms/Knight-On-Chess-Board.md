# Knight On Chess Board

Given any source point, (C, D) and destination point, (E, F) on a chess board,
we need to find whether Knight can move to the destination or not.

The above figure details the movements for a knight ( 8 possibilities ).

If yes, then what would be the minimum number of steps for the knight to move
to the said point.
If knight can not move from the source point to the destination point, then
return -1.

Note: A knight cannot go out of the board.

---

Use BFS or astar with distance heuristic to compute the shortest path from
start to goal. O(v + e) in time complexity.

---

Python:

```python

class Solution:
    
    moves = [(2,1), (1,2), (-2,1), (2,-1), (-1,2), (1,-2), (-2,-1), (-1,-2)]
    
    def knight(self, A, B, C, D, E, F):
        
        C, D, E, F = C-1, D-1, E-1, F-1
        
        def neighbours(x, y):
            for nx, ny in [(x + dx, y + dy) for dx, dy in self.moves]:
                if 0 <= nx < A and 0 <= ny < B and (nx, ny) not in seen:
                    yield nx, ny

        q = [(C, D)]
        seen = set([(C,D)])
        steps = 0
        
        while q:
            temp = []

            for x, y in q:
                if (x, y) == (E, F):
                    return steps
        
                for nx, ny in neighbours(x, y):
                    seen.add((nx, ny))
                    temp.append((nx, ny))
        
            q = temp
            steps += 1
        
        return -1
```
