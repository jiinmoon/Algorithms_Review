# 403 Frog Jump

Perform the jumpings - from each stone, take a look at previous jump distances
to compute the current jump distances and record back.

---

Python:

```python

class Solution:
    def canCross(self, stones):
        g = { stone: set() for stone in stones }
        g[0].add(0)

        for stone in stones:
            for j in g[stone]:
                for nj in [j + i for i in (-1,0,1)]:
                    g[stone+nj].add(nj)

        return g[stones[-1]]
```
