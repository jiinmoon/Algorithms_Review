# Possibility of finishing all courses given prerequisites

There are a total of A courses you have to take, labeled from 1 to A.

Some courses may have prerequisites, for example to take course 2 you have to
first take course 1, which is expressed as a pair: [1,2].

Given the total number of courses and a list of prerequisite pairs, is it
possible for you to finish all courses?

Return 1 if it is possible to finish all the courses, or 0 if it is not
possible to finish all the courses.

---

We can use topological sorting to find whether all courses have been covered.
For each node, we record the amount of prereqs that need to cover it. Traverse
each node to neighbours, updating the inward degree of the visited neighbour.
If at the end we do not have any outstanding courses with inward edges, we can
complete.

O(v + e) in time complexity.

---

Python:

```python

from collections import defaultdict, deque
class Solution:

    def canFinished(self, A, B, C):

        indeg = [0] * (A + 1)
        graph = defaultdict(list)

        for a, b in zip(B, C):
            graph[a].append(b)
            indeg[b] += 1

        queue = deque([i for i, c in enumearte(indeg) if not c])

        while queue:
            curr = queue.popleft()
            for neigh in graph[curr]:
                indeg[neigh] -= 1
                if not indeg[neigh]:
                    queue.append(neigh)

        return 1 if not any(indeg) else 0
```
