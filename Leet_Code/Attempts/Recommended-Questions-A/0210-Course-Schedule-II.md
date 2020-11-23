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

Java:

```java

import java.util.Deque;
import java.util.HashMap;
import java.util.LinkedList;

class Solution {
    
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        int[] degree = new int[numCourses];
        for (int[] prereqs : prerequisites) {
            int prevCourse = prereqs[0];
            int nextCourse = prereqs[1];
            List<Integer> neighbours = graph.getOrDefault(prevCourse, new LinkedList<>());
            neighbours.add(nextCourse);
            graph.put(prevCourses, neighbours);

            degree[nextCourse]++;
        }

        Deque<Integer> queue = new LinkedList<>();
        for (int course = 0; course < numCourses; course++) {
            if (degree[course] == 0) queue.add(course);
        }

        Deque<Integer> result = new LinkedList<>();
        while (!queue.isEmpty()) {
            int curr = queue.removeFirst();
            result.addFirst(curr);
            for (int neigh : graph.getOrDefault(curr, new LinkedList<>())) {
                degree[neigh]--;
                if (degree[neigh] == 0) queue.addLast(neigh);
            }
        }

        return (Arrays.stream(degree).sum() == 0) ?
            result.stream().mapToInt(i->i).toArray() :
            new int[]{};
    }
}

```


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
