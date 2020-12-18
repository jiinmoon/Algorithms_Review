# 1192. Critical Connections in a Network

There are n servers numbered from 0 to n-1 connected by undirected
server-to-server connections forming a network where connections[i] = [a, b]
represents a connection between servers a and b. Any server can reach any other
server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server
unable to reach some other server.

Return all critical connections in the network in any order.

---

We can use Tarjan's algorithm for finding SCC (Strongly-Connected-Components)
and modify it to find the "critical" connections, or connection that is not
part of the SCC group.

First, we prepare a table of times or depths that we can mark the times or
depths of the nodes that we visit. For each node that we visit with DFS, we
mark the current node as visited and record the time or depth that it was
discovered with.

For each neighbour of this node, we check for two conditions:

(1) neighbour is a parent of the current node:

In this case, we skip; this is required for undirectd graph.

(2) neighbour is not visited yet:

Then, we continue to traverse down to the neighbours, marking them with time or
depth that it was discovered with.

For each neighbour down the path that we have completed, we update the current
node's discovered time to minimum of the discovered time or minimum depths that
we have found thus far down the path. Consider that path has looped back and
revisited one of the ancestor. Then, its discovered time will be carried over,
marking all nodes along that path with the parent's discovered time or
discovered depth.

However, if we find that discovered time registered for our neighbour has not
been changed; it indicates that it is a start of the SCC or root of the
beginning of subtree for its component.

Here is an example:

```

Suppose we have a graph

                0
            /       \
            1   -   2
        /
    3

Starting from node 0, we DFS down the path, marking each of the depths.

DFS(0)
    
    visited     = [T, F, F, F]
    depths      = [0, -1, -1, -1]       # discovered at 0

    calls --> DFS(1)

        visited = [T, T, F, F]
        depths  = [0, 1, -1, -1]

        calls --> DFS(2)

            visited = [T, T, T, F]
            depths  = [0, 1, 2, -1]

            "0" already visited; update depth of "2" with "0".
            "1" is parent of "2"; skip.

            depths  = [0, 1, 0, -1]
        
        DFS(2) updated its depth; update depth of "1" as well.

        depths = [0, 0, 0, -1]

        calls --> DFS(3)
            
            visited = [T, T, T, T]
            depths = [0, 0, 0, 2]

            "1" is parent of "3"; skip.

        DFS(3) has returned; but depth of neighbour "3" is found to be
        1 + current depth of 1 which was the original depth that is was called
        (DFS(1)). Hence, (1 -> 3) is found to be critical and 3 denotes the
        beginning of another strongly connected component.
...

```

---

Python:

```python

from collections import defaultdict

class Solution1192:

    def criticalConnections(self, n, connections):

        graph = defaultdict(list)

        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)

        visited = [False] * n
        depths = [-1] * n
        result = []


        def dfs(node, parent, depth):

            visited[node] = True
            depths[node] = depth

            for neighbour in graph[node]:
                if neighbour == parent:
                    continue

                elif not visited[neighbour]:
                    dfs(neighbour, node, depth + 1)

                depths[node] = min(depths[node], depths[neighbour])

                if depths[neighbour] == depth + 1:
                    result.append((node, neighbour))

        dfs(0, None, 0)

        return result
```
