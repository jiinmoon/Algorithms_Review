# 1192. Critical Connections in a Network

There are n servers numbered from 0 to n-1 connected by undirected
server-to-server connections forming a network where connections[i] = [a, b]
represents a connection between servers a and b. Any server can reach any other
server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server
unable to reach some other server.

Return all critical connections in the network in any order.

---

To identify all the critical connections, the problem can be simplified to
finding the cycles on the undirecitonal graph. To find them, we maintain the
depths at which each nodes are found as we perform dfs. If the depths of the
node is not what we expect, it marks it as a cycle to be deleted from our
collection of connections.

---

Python:

```python

class Solution:
    def criticalConnections(self, n, connections):
        g = collections.defaultdict(list)
        for conn in connections:
            g[conn[0]].append(conn[1])
            g[conn[1]].append(conn[0])

        connections = {tuple(sorted(conn)) for conn in connections}

        depths = [-1 for _ in n]

        def helper(node, depth):
            if depths[node] >= 0:
                return depths[node]
            depths[node] = depth
            minDepthThusFar = n
            for neigh in g[node]:
                # parent neighbour revisited; skip
                if depths[neigh] == depth - 1:
                    continue
                currDepth = helper(neigh, depth + 1)
                if currDepth <= depth:
                    connections.discard(tuple(sorted(neigh, node)))
                minDepthThusFar = min(minDepthThusFar, currDepth)
            depths[node] = n
            return minDepthThusFar

        helper(0, 0)
        return list(connections)
```
