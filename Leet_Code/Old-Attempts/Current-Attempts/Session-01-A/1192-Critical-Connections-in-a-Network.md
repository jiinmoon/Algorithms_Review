# 1192 Critical Connections in a Network

In essence, this is about finding the cycle in undirected graph; to detect
a cycle, we traverse while maintaining our depths - if the path that we are
exploring encounters a node that has been explored previously (either parent or
cycle), it is detected by checking its depth.

---

Python:

```python

class Solution:
    def criticalConnections(self, connections, n):
        def helper(node, depth):
            if depths[node] >= 0:
                return depths[node]
            depths[node] = depth
            minDepth = n
            for neigh in g[node]:
                if depths[neigh] == depth - 1:
                    continue
                currDepth = helper(neigh, depth + 1)
                if currDepth <= depth:
                    connections.discard(tuple(sorted(neigh, node)))
                minDepth = min(currDepth, minDepth)
            depths[node] = n
            return minDepth

        g = collections.defaultdict(list)
        for conn in connections:
            g[conn[0]].append(g[conn[1]])
            g[conn[1]].append(g[conn[0]])

        depths = [-1 for _ in range(n)]
        connections = {tuple(sorted(conn)) for conn in connections}

        helper(0, 0)

        return len(connections)
```
