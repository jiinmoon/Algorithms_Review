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

Time complexity would be to traverse on each nodes which is O(m + n) and same
for space complexity.

---

Java:

```java

import java.util.HashMap;
import java.util.HashSet;

class Solution {
    private Map<Integer, List<Integer>> graph;

    public List<List<Integer>> criticalConnections(int n, List<List<Integer>> connections) {
        // initialize depths for cycle detection
        int[] depths = new int[n];
        Arrays.fill(depths, Integer.MIN_VALUE);
        
        // initialize bidirectional graph
        graph = new HashMap<>();
        connections.forEach(con -> {
            List<Integer> temp;
            int from = con.get(0);
            int to = con.get(1);
            
            temp = graph.getOrDefault(from, new ArrayList<>());
            temp.add(to);
            graph.put(from, temp);

            temp = graph.getOrDefault(to, new ArrayList<>());
            temp.add(from);
            graph.put(to, temp);
        });

        connections.forEach(con -> { Collections.sort(con); });

        Set<List<Integer>> result = new HashSet<>(connections);

        helper(0, 0, depths, result);

        return new ArrayList<>(result);
    }

    public int helper(int node, int depth, int[] depths, Set<Integer> result) {
        // node has been explored previously
        if (depths[node] >= 0) return depths[node];
        
        depths[node] = depth;
        int minDepth = Integer.MAX_VALUE;

        List<Integer> neighbours = graph.get(node);
        for (int neigh : neighbours) {
            // parent visited; skip
            if (depths[neigh] == depth - 1) continue;

            int currDepth = helper(neigh, depth + 1, depths, result);

            if (currDepth <= depth) {
                // current edge between node to neigh is a cycle
                List<Integer> toRemove = new ArrayList<>(List.of(neigh, node));
                Collections.sort(toRemove);
                result.remove(toRemove);
            }

            minDepth = Math.min(minDepth, currDepth);
        }

        // mark current node as finished
        depths[node] = Integer.MAX_VALUE;
        return minDepth;
    }
}

```

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
