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

This problem can be thinked of as a graph colouring problem where as we
traverse on the graph, we are colouring each node alternatively. It should be
such that when we explore on the neighbour, if it has been visited before, its
colour should be same as the current. The time complexity would be O(e) where
e is the number of the edges present.

---

Python:

```python

class Solution:
    def isBipartite(self, graph):
        colors = [None] * len(graph)
        for node in range(len(graph)):
            # skip nodes where we have explored prevously
            if colors[node] != None:
                continue
            
            # mark the node and explore as far as possible (DFS)
            colors[node] = True
            stk = [node]
            while stk:
                curr = stk.pop()
                for neigh in graph[curr]:
                    # two cases when we visit neighbour
                    # We have visited the neighbour before or not
                    # If we have not visited, mark it as opposite color of
                    # current, and push unto queue for further visit.
                    if not colors[neigh]:
                        colors[neigh] = not colors[curr]
                        stk.append(neigh)
                    # otherwise, check to see it is not the same color as 
                    # current, which indicates cycle
                    # adjacent nodes should not be colored same
                    elif colors[neigh] == colors[curr]:
                        return False

        return True
```
