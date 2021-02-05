133 Clone Graph
===============

Given a reference of a node in a connected undirected graph, return a depp copy
of the graph.

---

Perform a traversal from the starting node - while doing so, we maintain
a hashmap of node : clonedNode until the end. Time complexity should be in O(v
+ e) for # of verticies and edges.

---

Python:

```python

class Node:
    def __init__(self, val = 0, neighbours = None):
        self.val = val
        self.neighbours = neighbours if neighbours else list()

class Solution:
    def cloneGraph(self, node):
        if not node:
            return

        nodeCopy = Node(node.val)
        q = [ node ]
        d = { node : nodeCopy }

        while q:
            curr = q.pop()
            currCopy = d[curr]

            for neigh in curr.neighbours:
                if neigh not in d:
                    neighCopy = Node(neigh.val)
                    d[neigh] = neighCopy
                    q.append(neigh)
                else:
                    neighCopy = d[neigh]
                currCopy.neighbours.append(neighCopy)

        return nodeCopy
```
