# 323. Number of Connected Components in an Undirected Graph

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge
is a pair of nodes), write a function to find the number of connected
components in an undirected graph.

---

Here, we use union-find algorithm; for every edge A -> B, we check to see that
they can be collasped into a single group - indicating that there is
a connection. Initially, we have n number of edges to start with. Then, for
every node, we check their union-find groups.

Time complexity would be O(m * log(n)) for m edges and n nodes.

---

Python:

```python

class Solution323:

    def numConnectedComponents(self, n, edges):

        def helper(node):
            while node != union[node]:
                union[node] = union[union[node]]
                node = union[node]
            return node

        result = n
        union = [i for i in range(n)]

        for a, b in edges:
            groupA = union(a)
            groupB = union(b)
            if groupA != groupB:
                result -= 1
                union[groupA] = groupB

        return result
```
