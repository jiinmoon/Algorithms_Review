# 210. Course Schedule II

There are a total of n courses you have to take labelled from 0 to n - 1.

Some courses may have prerequisites, for example, if prerequisites[i] = [ai,
bi] this means you must take the course bi before the course ai.

Given the total number of courses numCourses and a list of the prerequisite
pairs, return the ordering of courses you should take to finish all courses.

If there are many valid answers, return any of them. If it is impossible to
finish all courses, return an empty array.

---

This problem is better visualized as a graph problem - where each course is
represented as a node and each node's prerequsities are represented as an
directed edge. Hence, this is a topological sorting algorithm where we
repeatedly find the nodes with 0 indegree edges to perform dfs while building
the list of courses that have been finished their prerequisites.

---

Python:

```python

class Solution:
    def courseSchedule(self, n, prereqs):
        indeg = [0] * n
        g = collections.defaultdict(list)
        for p, c in prereqs:
            g[p].append(c)
            indeg[c] += 1

        q = collections.deque()
        for i, c in enumerate(indeg):
            if not c:
                q.append(i)

        result = list()
        while q:
            curr = q.popleft()
            result.append(curr)
            for neigh in g[curr]:
                indeg[neigh] -= 1
                if not indeg[neigh]:
                    q.append(neigh)

        return result if not any(indeg) else []
```
