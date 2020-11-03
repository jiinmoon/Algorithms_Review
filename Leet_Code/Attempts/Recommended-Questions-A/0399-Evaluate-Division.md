# 399. Evaluate Division

You are given an array of variable pairs equations and an array of real numbers
values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai
/ Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth
query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined,
return -1.0.

Note: The input is always valid. You may assume that evaluating the queries
will not result in division by zero and that there is no contradiction.

---

We visualize this problem as a graph problem where each node represents value
and directed edge is created with a weight that computes the division operation
from node A to node B (A/B). Then, it is about finding all the connected paths
and its weights using the Floyd-Warshall algorithm. The time complexity would
be O(n^3).

---

Python:

```python

class Solution:
    def calcEquation(self, equations, values, queries):
        graph = collections.defaultdict(dict)
        for i in range(len(equations)):
            src, dst, val = equations[i][0], equations[i][1], values[i]
            graph[src][dst] = val
            graph[dst][src] = 1/val

        for A in graph:
            for B in graph[A]:
                for C in graph[A]:
                    # B/C = B/A * A/C
                    graph[B][C] = graph[B][A] * graph[A][C]

        result = list()
        for src, dst in queries:
            if src in graph and dst in graph[src]:
                result.append(graph[src][dst])
            else:
                result.append(-1.0)

        return result
```
