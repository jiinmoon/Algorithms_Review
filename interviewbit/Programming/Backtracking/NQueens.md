# NQueens



---

## Approach:

We use backtrack to discover all possible board state where none of the
n queens are threat to each other. To do this, we record the positions of the
previous queens and check that whether current position of the queen is in
valid spot to place the queen.

O(n!) in time complexity due to having to explore all possible queen positions.

---

Python:

```python

class Solution:

    def solve(self, n):

        cols, upDiag, downDiag = set(), set(), set()

        path = [["."] * n for _ in range(n)]

        def helper(row, path):

            if row == n:
                result.append(["".join(r) for r in path])

            else:

                for col in range(n):
                    if col in cols or row + col in upDiag or row - col in downDiag:
                        continue

                    path[row][col] = "Q"
                    cols.add(col)
                    upDiag.add(row + col)
                    downDiag.add(row - col)
                    helper(row + 1, path) 
                    downDiag.remove(row - col)
                    upDiag.remove(row + col)
                    cols.remove(col)
                    path[row][col] = "."

        result = []

        helper(0, path)

        return result

```
