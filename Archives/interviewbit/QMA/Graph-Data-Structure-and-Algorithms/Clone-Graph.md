# Clone Graph

Clone an undirected graph. Each node in the graph contains a label and a list
of its neighbors.

---

Traverse on the given graph, visiting each of the neighbours. For each
neighbour that we visit, we also check whether we have cloned the neighbours
and add the cloned neighbors to the current cloned node's neigbors.

O(v + e) in time complexity.

---

Python:

```python

# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        
        queue, d = [node], {node : UndirectedGraphNode(node.label)}
        
        while queue:
            
            currNode = queue.pop()
            currNodeCopy = d[currNode]
            
            for neighNode in currNode.neighbors:
                if neighNode not in d:
                    neighNodeCopy = UndirectedGraphNode(neighNode.label)
                    d[neighNode] = neighNodeCopy
                    queue.append(neighNode)
                else:
                    neighNodeCopy = d[neighNode]
                currNodeCopy.neighbors.append(neighNodeCopy)
        
        return d[node]
```
