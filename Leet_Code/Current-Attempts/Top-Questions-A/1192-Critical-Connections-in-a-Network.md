# 1193 Critical Connections in a Network

There are n servers numbered from 0 to n-1 connected by undirected
server-to-server connections forming a network where connections[i] = [a, b]
represents a connection between servers a and b. Any server can reach any other
server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server
unable to reach some other server.

Return all critical connections in the network in any order.

---

This problem is essentially about finding where the cycles occur, and severing
the connections that are cycles - such that we are only left with connections
which are not critical.

To detect cycles as we traverse (DFS) on the graph, we maintain the "depth" of
the each node that we are visiting starting from 0 in the starting node. This
allows us to find that if the depth returned from a downward path is less than
the current, it implies that we have visited it beforehand, and it is safe to
mark it as critical connection.

The time complexity should be of O(V + E).

---

Python:

```python

class Solution:
    def criticalConnections(self, n, connections):
        depths = [-1 for _ in range(n)]

        g = collections.defaultdict(list)
        for conn in connections:
            g[conn[0]].append(conn[1])
            g[conn[1]].append(conn[0])
        
        connections = { tuple(sorted(conn)) for conn in connections }

        def DFS(node, depth):
            if depths[node] >= 0:
                return depths[node]
            depths[node] = depth
            minDepth = n
            for neigh in g[node]:
                if depths[neigh] == depth - 1:
                    continue
                currDepth = DFS(neigh, depth + 1)
                if currDepth <= depth:
                    connections.discard(tuple(sorted(neigh, node)))
                minDepth = min(minDepth, currDepth)
            depths[node] = n
            return minDepth

        DFS(0, 0)
        return list(connections)
```
