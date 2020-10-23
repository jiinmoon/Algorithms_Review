# 210 Course Schedule II

There are a total of n courses you have to take labelled from 0 to n - 1.

Some courses may have prerequisites, for example, if prerequisites[i] = [ai,
bi] this means you must take the course bi before the course ai.

Given the total number of courses numCourses and a list of the prerequisite
pairs, return the ordering of courses you should take to finish all courses.

If there are many valid answers, return any of them. If it is impossible to
finish all courses, return an empty array.

---

The problem is a topological sorting - starting from each of the nodes that
does not have any "indegrees" we repeatedly find next connected nodes and
delete its indegree counts. If at the end we do not have any more nodes with
indegrees left, we can complete the schedule.

---

Python:

```python

class Solution:
    def findOrder(self, n, prereqs):
        indeg = [0] * n
        g = collections.defaultdict(list)
        for p, c in prereqs:
            g[p].append(c)
            indeg[c] += 1

        q = collections.deque()
        for i, degree in indeg:
            if not indeg:
                q.append(i)

        result = list()
        while q:
            curr = q.popleft()
            result = [curr] + result

            for neigh in g[curr]:
                indeg[neigh] -= 1
                if not indeg[neigh]:
                    q.append(neigh)
        
        return result if not any(indeg) else list()
```
