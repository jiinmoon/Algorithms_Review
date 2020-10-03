# 210 Course Schedule II

There are a total of n courses you have to take labelled from 0 to n - 1.

Some courses may have prerequisites, for example, if prerequisites[i] = [ai,
bi] this means you must take the course bi before the course ai.

Given the total number of courses numCourses and a list of the prerequisite
pairs, return the ordering of courses you should take to finish all courses.

If there are many valid answers, return any of them. If it is impossible to
finish all courses, return an empty array.

---

This particular problem can be viewed as a graph problem which can be
approached with topological sorting where we basically repeatedly perform DFS
on nodes that does not have any "prerequisites" or "indegrees" - the number of
directed edges that points at the node.

---

Python:

```python

class Solution:
    def courseSchedule(self, N, prereqs):
        indegs = [0] * N
        g = collections.defaultdict(list)
        for p, c in prereqs:
            g[p].add(c)
            indegs[c] += 1

        q = [i for i, c in indegs if not c]
        q = collections.deque(q)

        res = list()
        while q:
            curr = q.popleft()
            res.append(curr)

            for neigh in g[curr]:
                indegs[neigh] -= 1
                if not indges[neigh]:
                    q.append(neigh)

        return res if not any(indegs) else list()
```
