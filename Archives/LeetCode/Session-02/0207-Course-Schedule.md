# 207. Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to
numCourses - 1. You are given an array prerequisites where prerequisites[i]
= [ai, bi] indicates that you must take course bi first if you want to take
course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first
take course 1.

Return true if you can finish all courses. Otherwise, return false.

---

We may think of this problem as a graph problem where we are to topologically
visit (or sort) all the nodes in order of prereqs to next. This is done so by
maintain the number of "indegrees" or "inward" edges to each of the nodes which
represents the number of prerequisites to complete before that node is
finished.

---

Python:

```python

from collections import defaultdict, deque

class Solution207:

    def canFinish(self, prereqs, numCourses):
        
        indeg = [0] * numCourses
        graph = defaultdict(list)
        
        # build our graph and record number of indegrees for each node
        for pre, nxt in prereqs:
            graph[pre].append(nxt)
            indeg[nxt] += 1
        
        # start from courses that does not have any indegrees
        queue = deque()
        for course, deg in indeg:
            if not deg:
                queue.append(course)

        while queue:
            curr = queue.popleft()
            for neigh in graph[curr]:
                indeg[neigh] -= 1
                # neighbour is good for visit if no more prereqs left (indeg == 0)
                if not indeg[neigh]:
                    queue.append(neigh)
        
        return not any(indeg)
```
