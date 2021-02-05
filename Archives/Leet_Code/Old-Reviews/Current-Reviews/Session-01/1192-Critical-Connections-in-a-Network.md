1192 Critical Connections in a Network
======================================

There are n servers numbered from 0 to n-1 connected by undirected
server-to-server connections forming a network where connections[i] = [a, b]
represents a connection between servers a and b. Any server can reach any other
server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server
unable to reach some other server.

Return all critical connections in the network in any order.

---

The problem is about traversing through the undirected graph - and discover
which edges are safe to remove so that we only have the edges left over which
are marked unsafe, and critical.

The edges are unsafe iff it is within a part of a network that contains
a cycle.

We will perform DFS on the graph - and propagate as far as possible until we
have seen the parent, no more neighbours to visit, or the neighbour is from
a depth that is lower than current which indicates that it is a cycle.

---

Python:

```python
from collections import defaultdict

class Solution:
    def criticalConnections(self, n, connections):
        neighbours = defaultdict(list)
        for conn in connections:
            # undirected graph
            neighbours[conn[0]] = conn[1]
            neighbours[conn[1]] = conn[0]
        # keep the connections sorted so we know which one to discard
        # 1 -> 2 and 2 -> 1 should be same
        connections = { tuple(sorted(conn)) for conn in connections }
        # indicator of cycles and visited
        depths = [ inf('-inf') for _ in range (n) ]

        def DFS(node, depth):
            # have we visited the node? (depths[node] == n)
            # or in process of visiting? (0 <= depths[node] < n)
            if depths[node] >= 0:
                return depths[node]

            # update record of current node's depth
            depths[node] = depth
            # minimum of the depth that has been explored on this path
            minPathDepth = n
            for neigh in neighbours[node]:
                # ignore its parent (returning to where it came from)
                if depths[neigh] == depth-1:
                    conitnue
                currentDepth = DFS(neigh, depth+1)
                # cycle detected (visiting back to lower depth node)
                # safe to delete current edge
                if currentDepth <= depth:
                    connections.discard( tuple(sorted((node, neigh)) ) 
                # update minPathDepth by comparing this neighbour's path depth
                minPathDepth = min(minPathDepth, currentDepth)
            # mark the node done - indicated by n
            depths[node] = n
            return minPathDepth 
```

