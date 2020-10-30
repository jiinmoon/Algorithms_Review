# 1192 Critical Connections in a Network

There are n servers numbered from 0 to n-1 connected by undirected
server-to-server connections forming a network where connections[i] = [a, b]
represents a connection between servers a and b. Any server can reach any other
server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server
unable to reach some other server.

Return all critical connections in the network in any order.

---

Finding "critical connections" problem is essentially about finding the list
where the cycles occur in the undirected graph. To do so, we maintain each node
and its depth.

---

Python:

```python

class Solution:
    def criticalConnections(self, n, connections):
        # build undirected graph
        g = collections.defaultdict(list)
        for con in connections:
            g[con[0]].append(con[1])
            g[con[1]].append(con[0])

        # order connections
        connections = {tuple(sorted(con)) for con in connections}

        # depths tracker
        depths = [float('-inf') for _ in range(n)]

        def helper(node, depth):
            # visited prior
            if depths[node] >= 0:
                return depths[node]

            # new node encountered
            # traverse down to find the cycles
            depths[node] = depth
            minPathDepth = n
            for neigh in g[node]:
                # ignore visiting parent
                if depths[neigh] == depth - 1:
                    continue
                currPathDepth = helper(neigh, depth + 1)
                # was cycle discovered down the path?
                if currPathDepth <= depth:
                    # delete the edge
                    connections.discard(tuple(sorted(node, neigh)))
                minPathDepth = min(minPathDepth, currPathDepth)
            
            # mark so that it is fully explored
            depths[node] = n
            return minPathDepth

        helper(0, 0)
        return list(connections)
```
