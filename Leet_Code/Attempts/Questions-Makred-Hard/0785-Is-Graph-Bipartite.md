# 785. Is Graph Bipartite

Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split its set of nodes into two
independent subsets A and B, such that every edge in the graph has one node in
A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for
which the edge between nodes i and j exists.  Each node is an integer between
0 and graph.length - 1.  There are no self edges or parallel edges: graph[i]
does not contain i, and it doesn't contain any element twice.

---

In short, this is a graph colouring problem where we perform traversal on the
graph - and we should not visit any neighbours that are marked same as current.

As there are two colors present, we can use boolean to denote each of the
visited node's color. Since the graph (adjacency list) is given, we can perform
simple traversal using a queue.

For each node, we perform traversal as far out as possible - we first mark the
current node as visited and color it "True". Then, for every neighbour of this
node, there are three possibilities. (1) the neighbour node has not been
visited yet, meaning it is not "colored". Then, we mark it as opposite of
current node's color, and add to our queue to explore as far out as possible.
(2) the neighour node has been visited and marked. In this case, we can
terminate to determine that the graph is not bipartite. (3) otherwise, we can
continue as marked neighbours color is opposite of current.

The time complexity should be O(n).

---

Python:

```python

class Solution:
    def isGraphBipartite(self, graph):
        visited = [None] * len(graph)
        for node in range(len(graph)):
            # if node already explored, no need to traverse
            if visited[node]:
                continue

            q = [node]
            visited[node] = True

            while q:
                curr = q.pop()
                for neigh in graph[neigh]:
                    if not visited[neigh]:
                        visited[neigh] = not visited[curr]
                        q.append(neigh)
                    elif visited[neigh] == visited[curr]:
                        return False

        return True
```
