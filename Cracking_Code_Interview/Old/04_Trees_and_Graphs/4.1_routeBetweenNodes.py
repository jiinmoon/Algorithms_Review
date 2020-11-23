""" 4.1 Route Between Nodes

Question:

    Given a directed graph, design an algorithm to find out whether there is a
    route between two nodes.

---

This is asking for definition of the directed graph, and whether one has
knowledge about the traversal algorithm.

Directed graph implies that the nodes in the graph has a directed path to
another neighbouring node. Thus, in order for us to find whether there exists a
path between two nodes, we have to perform a graph traversal algorithm: we can
do either DFS or BFS.

DFS: Depth-first Search.

    - it is a recursive in nature in that we first visit all the neighbours to
      the point where there is no neighbours left; then we move back up to start
      visiting other negihbours.

BFS: Breadth-first Search.

    - it is also called the level search as we first visit all neighbours at the
      particular depth, then move onto the next depth.

Both traversal algorithms will work but the time complexity will differ based on
the shape of the tree. Also, it is interesting to note that the BFS will always
result in the shortest path possible between two nodes.

"""
class GraphNode:

    def __init__(self, val):
        self.val = val
        self.visited = False
        self.neighbours = []


class Solution:

    def searchRoute(self, graph, startNode, endNode):
        if startNode == endNode: return True

        queue = [startNode]
        while !queue.isEmpty():
            currNode = queue.dequeue()
            for neighbour in currNode.neighbours():
                if !neighbour.visited:
                    if neighbour == endNode: return True
                    else:
                        neighbour.visited = True
                        queue.add(neighbour)
            currNode.visited = True

        return False

