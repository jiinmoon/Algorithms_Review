# 207. Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to
numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to
first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it
possible for you to finish all courses?

---

We can complete this problem with a topological sorting algorithm. We maintain
a list of inward edges for each of the nodes. Starting from the nodes that does
not have any inward edges, we try to explore using repeated dfs. At the end, if
we do not have any inward edges (no more prerequisites leftover), then we can
complete the courses. Time complexity would be O(V + E) where V is number of
verticies (nodes) and E is the number of edges (prereqs).

---

Python:

```python

from collections import defaultdict

class Solution207:

    def canFinish(self, numCourses, prerequisites):

        indegree = [0] * numCourses
        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[a].append(b)
            indegree[b] += 1

        queue = deque()

        for c, d in enumerate(indegree):
            if not d:
                queue.append(c)

        while queue:
            
            currNode = queue.popleft()

            for neighNode in graph[currNode]:
                
                # one of neighbour's prerequisite is finished
                indegree[neighNode] -= 1

                # if done, we can visit
                if indegree[neighNode] == 0:
                    queue.append(neighNode)

        # no prerequisites should left standing

        return not any(indegree)
```
