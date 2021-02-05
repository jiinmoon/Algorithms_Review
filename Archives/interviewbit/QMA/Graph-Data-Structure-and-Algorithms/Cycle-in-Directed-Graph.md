# Cycle in Directed Graph

Given an directed graph having A nodes. A matrix B of size M x 2 is given which
represents the M edges such that there is a edge directed from node B[i][0] to
node B[i][1].

Find whether the graph contains a cycle or not, return 1 if cycle is present
else return 0.

NOTE:

The cycle must contain atleast two nodes.
There are no self-loops in the graph.
There are no multiple edges between two nodes.
The graph may or may not be connected.
Nodes are numbered from 1 to A.
Your solution will run on multiple test cases. If you are using global
variables make sure to clear them.

---

There are multiple algorithms to detect the cycle (using DFS - topological
sort); but simple one would be to record the parents as we exaimne each of the
pair of the edges. If we find the while traversing to recorded parents, we
return back to the same node as current next node, then we have a cycle.

O(v + e) in time complexity and O(v) in space complexity.

---

Python:

```python

class Solution:

    def hasCycle(self, A, B):

        parents = [None] * (A + 1)

        for x, y in B:
            
            parentX = parents[x]

            while parentX != None:
                # circled back to same place
                if parentX == y:
                    return 1
                parentX = parents[parentX]

            # record x as parent of y
            parents[y] = x

        return 0
```
