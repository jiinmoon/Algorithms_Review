# Path with good nodes

Given a tree with N nodes labelled from 1 to N.

Each node is either good or bad denoted by binary array A of size N where if
A[i] is 1 then ithnode is good else if A[i] is 0 then ith node is bad.

Also the given tree is rooted at node 1 and you need to tell the number of root
to leaf paths in the tree that contain not more than C good nodes.

NOTE:

Each edge in the tree is bi-directional.

---

Use dfs to recursively traverse down to the leaves while counting the good
nodes. If we find that we have more good nodes than allowed, we exit.

---

Python:

```python

from collections import defaultdict

class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        
        def helper(node, goodCount):
            if A[node-1]:
                goodCount += 1
            if goodCount > C:
                return 0
            if node not in graph:
                return 1
            pathCount = 0
            for neigh in graph[node]:
                pathCount += helper(neigh, goodCount)
            return pathCount
            
        graph = defaultdict(list)
        
        for edge in B:
            graph[min(edge)].append(max(edge))
        
        return helper(1, 0)
```
