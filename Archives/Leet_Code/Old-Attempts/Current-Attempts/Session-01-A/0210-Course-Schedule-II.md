# 210 Course Schedule II

Maintain the number of edges that formed into the verticies; and perform dfs on
each vertex that does not have any. This topological sort can complete in O(v
+ e).

---

Python:

```python

class Solution:
    def courseSchedule(self, n, prereqs):
        g = collections.defaultdict(list)
        indegs = [0] * n

        for p, c in prereqs:
            g[p].append(c)
            indegs[c] += 1

        q = list()
        for i, c in enumerate(indegs):
            if not c:
                q.append(i)

        res = list()
        while q:
            curr = q.pop()
            res.append(curr.val)
            for neigh in g[curr]:
                indegs[neigh] -= 1
                if not indegs[neigh]:
                    q.append(neigh)

        return res
```
