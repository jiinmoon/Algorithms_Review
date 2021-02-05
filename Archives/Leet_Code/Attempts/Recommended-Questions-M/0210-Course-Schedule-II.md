# 210. Course Schedule II

There are a total of n courses you have to take labelled from 0 to n - 1.

Some courses may have prerequisites, for example, if prerequisites[i] = [ai,
bi] this means you must take the course bi before the course ai.

Given the total number of courses numCourses and a list of the prerequisite
pairs, return the ordering of courses you should take to finish all courses.

If there are many valid answers, return any of them. If it is impossible to
finish all courses, return an empty array.

---

This is a graph problem where we are trying to find the topologically sorted
order of the nodes. To find the ordering, starting from each of the nodes that
does not have any "indegree" or inward edges (meaning that it has completed its
prerequisites) we perform dfs. This process is repeated until we have exhusated
all the nodes.

---

Python:

```python

class Solution:
    def courseSchedule(self, prereqs, m):
        indeg = [0] * m
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
            # only nodes that we examine are those that have completed the prereqs
            result.append(curr)
            for neigh in g[curr]:
                indeg[neigh] -= 1
                if not indeg[neigh]:
                    q.append(neigh)

        return result if not any(indeg) else []
```

