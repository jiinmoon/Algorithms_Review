# Commutable Islands

There are A islands and there are M bridges connecting them. Each bridge has
some cost attached to it.

We need to find bridges with minimal cost such that all islands are connected.

It is guaranteed that input data will contain at least one possible scenario in
which all islands are connected with each other.

---

We can solve this problem with finding minimal spanning tree in the graph with
either Kruskal's or Prim's algorithm.

First, we sort the given edges by their weights so that we always examine the
minimum weight. For each edges that we examine, if we have not conjoined two,
we add them to the same disjointed set and increase our cost to connect by
current weight. After we have finished examining all the edges, we should have
our minimum cost to connect the islands.

Time complexity is O(E * log(E)) due to sorting involved and linear time to
examine all the edges; for each edge log(E) to connect the parents in disjoint
set.

---

Python:

```python

class Solution:

    def minCostToConnect(self, A, B):

        def unionFind(node):

            # node has not been discovered yet; return itself as a root
            if not union[node]:
                return node
            # collapse by all the root
            union[node] = unionFind(union[node])
            return union[node]


        def kruskal(edges):
            
            minCost = 0
            for x, y, weight in edges:
                rootX, rootY = unionFind(x), unionFind(y)
                # parents differ, add them to same set
                # new connection to form, add weight to total min cost
                if rootX != rootY:
                    union[rootX] = rootY
                    minCost += weight
            return minCost


        union = [None for _ in range(len(A)+1)]
        
        # sort by weights in ascending order
        B.sort(key=lambda E : E[2])

        return kruskal(B)
```
